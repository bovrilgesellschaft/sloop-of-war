"""Automated playtest for Sloop of War.

Run:  python3 tools/playtest.py [runs]

Opens index.html in headless Chromium and checks:
  1. the Content check reports no mistakes;
  2. N random playthroughs (a third of them by a captain who never turns
     back early) all reach an Ending, never strand the player
     ("The Log Runs Out") and never leave a screen with no open choice;
  3. lists any event no random playthrough reached (a caution, not a failure);
  4. the same seed and the same choices give exactly the same state;
  5. every combat sandbox action ends, and replays the same.

Exits non-zero if any check fails.
"""
import json
import os
import sys
import tempfile

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = int(sys.argv[1]) if len(sys.argv) > 1 else 200
MAX_STEPS = 600

# The published page is wrapped in a document skeleton; do the same here.
html = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
tmp = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8')
tmp.write('<!doctype html><html><head><meta charset="utf-8">'
          '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
          '</head><body>' + html + '</body></html>')
tmp.close()

failures = []


WALK_JS = """
([seed, n, stubborn, maxSteps]) => {
  // a small seeded generator for the test's own choices (the game has its own)
  let x = n * 2654435761 % 4294967296 || 1;
  const rnd = () => { x ^= x << 13; x >>>= 0; x ^= x >>> 17; x ^= x << 5; x >>>= 0; return x / 4294967296; };
  const T = window.SloopTest;
  T.newGame('Test Hand', seed);
  const seen = [];
  for (let steps = 0; steps < maxSteps * 2; steps++){
    const st = T.state;
    seen.push(st.eventId);
    if (st.ended || st.eventId === '__nowhere__') return { st, seen };
    if (st.pending){ T.carryOnQuiet(); continue; }
    const open = T.open();
    if (!open.length){ st.stuck = true; return { st, seen }; }
    let pick = open[Math.floor(rnd() * open.length)];
    if (stubborn){
      // a captain who never turns back and never stints: reaches the far ends of the stores
      const texts = T.content.events[st.eventId].choices.map(c => c.text);
      const keen = open.filter(i => /^(Stand on|Crack on|Begin|Make sail|Return aboard)/.test(texts[i]));
      if (keen.length && rnd() < 0.9) pick = keen[keen.length - 1];
    }
    T.chooseQuiet(pick);
  }
  const st = T.state; st.loop = true; return { st, seen };
}
"""


def walk(pg, seed, n, stubborn=False):
    """Play one commission with random choices. Returns the final state and the events seen."""
    r = pg.evaluate(WALK_JS, [seed, n, stubborn, MAX_STEPS])
    return r['st'], r['seen']


with sync_playwright() as p:
    browser = p.chromium.launch()
    pg = browser.new_page(viewport={'width': 390, 'height': 844})
    page_errors = []
    pg.on('pageerror', lambda e: page_errors.append(str(e)))
    pg.route('**/fonts.googleapis.com/**', lambda r: r.abort())
    pg.route('**/fonts.gstatic.com/**', lambda r: r.abort())
    pg.goto('file://' + tmp.name)
    pg.wait_for_timeout(300)

    problems = pg.evaluate("SloopTest.content.problems")
    mistakes = [x for x in problems if x['sev'] == 'error']
    print(f"Content check: {len(mistakes)} mistakes, {len(problems) - len(mistakes)} cautions")
    for x in problems:
        print(f"  {x['sev']}: {x['msg']} ({x['where']})")
    if mistakes:
        failures.append('content check has mistakes')

    endings, orders, visited = {}, {}, set()
    for k in range(RUNS):
        st, seen = walk(pg, f'TEST-{k}', k + 1, stubborn=(k % 3 == 2))
        visited.update(seen)
        if st.get('stuck'):
            failures.append(f'seed TEST-{k}: no open choice at {st["eventId"]}')
        elif st.get('loop'):
            failures.append(f'seed TEST-{k}: still going after {MAX_STEPS} choices, at {st["eventId"]}')
        elif st['eventId'] == '__nowhere__':
            failures.append(f'seed TEST-{k}: the log runs out after {st.get("nowhere")}')
        else:
            endings[st['eventId']] = endings.get(st['eventId'], 0) + 1
            orders[st.get('orders')] = orders.get(st.get('orders'), 0) + 1
    print(f"{RUNS} playthroughs. Endings: {endings}. Orders: {orders}")

    never = set(pg.evaluate("SloopTest.content.order")) - visited
    if never:
        print(f"Caution, never reached by random play: {sorted(never)}. Rare events need a scripted check.")

    a, _ = walk(pg, 'SAME-SEED', 99)
    b, _ = walk(pg, 'SAME-SEED', 99)
    a.pop('startedAt', None)
    b.pop('startedAt', None)
    same = a == b
    print(f"Replay is deterministic: {same}")
    if not same:
        failures.append('replay is not deterministic')

    # the combat sandbox: every action ends, and the same seed and orders fight the same action
    actions = pg.evaluate("Object.keys(SloopTest.content.actions)")
    outcomes = {}
    for act in actions:
        for k in range(6):
            cfg = {'action': act, 'arm': k % 2, 'policy': ['for', 'stern'][k // 3 % 2], 'seed': f'SB-{k}', 'sail': 'auto'}
            r1 = pg.evaluate("c => SloopTest.sandboxRun(c)", cfg)
            r2 = pg.evaluate("c => SloopTest.sandboxRun(c)", cfg)
            if r1 != r2:
                failures.append(f'sandbox {act} seed SB-{k} is not deterministic')
            if not r1['over']:
                failures.append(f'sandbox {act} seed SB-{k} never ended')
            outcomes.setdefault(act, {}).setdefault(r1['over'], 0)
            outcomes[act][r1['over']] += 1
    print(f"Combat sandbox outcomes: {outcomes}")

    if page_errors:
        failures.extend(f'page error: {e}' for e in page_errors)
    browser.close()

os.unlink(tmp.name)
if failures:
    print('\nFAILED')
    for f in failures[:20]:
        print('  ' + f)
    sys.exit(1)
print('\nAll checks passed.')
