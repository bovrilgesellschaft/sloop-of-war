"""Automated playtest for Sloop of War.

Run:  python3 tools/playtest.py [runs]

Opens index.html in headless Chromium and checks:
  1. the Content check reports no mistakes;
  2. N random playthroughs all reach an Ending, never strand the player
     ("The Log Runs Out") and never leave a screen with no open choice;
  3. every event is reached by at least one playthrough;
  4. the same seed and the same choices give exactly the same state.

Exits non-zero if any check fails.
"""
import json
import os
import random
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


def walk(pg, seed, rnd):
    """Play one commission with random choices. Returns the final state."""
    pg.evaluate(f"SloopTest.newGame('Test Hand', {json.dumps(seed)})")
    seen = []
    for _ in range(MAX_STEPS * 2):
        st = pg.evaluate("SloopTest.state")
        seen.append(st['eventId'])
        if st['ended'] or st['eventId'] == '__nowhere__':
            return st, seen
        if st['pending']:
            pg.evaluate("SloopTest.carryOn()")
            continue
        open_choices = pg.evaluate("SloopTest.open()")
        if not open_choices:
            st['stuck'] = True
            return st, seen
        pg.evaluate(f"SloopTest.choose({rnd.choice(open_choices)})")
    st['loop'] = True
    return st, seen


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
        st, seen = walk(pg, f'TEST-{k}', random.Random(k))
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
        print(f"Never reached: {sorted(never)}")
        failures.append('some events were never reached')

    a, _ = walk(pg, 'SAME-SEED', random.Random(99))
    b, _ = walk(pg, 'SAME-SEED', random.Random(99))
    a.pop('startedAt', None)
    b.pop('startedAt', None)
    same = a == b
    print(f"Replay is deterministic: {same}")
    if not same:
        failures.append('replay is not deterministic')

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
