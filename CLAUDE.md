# Working on Sloop of War

Edmund is the designer and writer. He does not program: Claude writes all the code, and nothing should ever need hand-editing by him. Reply in British English, plainly, leading with the answer.

## Where things live

- **The game** is `index.html`: one self-contained page. Content (events, orders, glossary) sits in `<script type="text/plain" class="content">` blocks at the top; the engine is the last `<script>`. Keep content and engine apart.
- **The published build** is the claude.ai artifact https://claude.ai/artifact/WusHJH3A6ZdvDDcJEZ5SBY. Every build is published to that same link. From a new session, read it first (Artifact `read`), then publish with `url` set to it.
- **The design document** is `docs/design-document.md`, mirrored as "Sloop of War Design Document.docx" in the claude.ai project. The project copy is the one Edmund reads: update both together.
- **The writing format** is `docs/event-writing-format.md`, mirrored as "claude/Event writing format.md" in the project. Update it whenever the format gains a feature.

## Each build

1. Make the change in `index.html`.
2. Run `python3 tools/playtest.py 300`. It must pass: no content mistakes, every random playthrough reaches an Ending, replays are deterministic. Events it lists as never reached need a scripted check of their own.
3. Look at the page once at phone width (390px) in a headless browser.
4. Publish to the artifact link above.
5. Commit and push to `main`, with a message naming the build step.
6. Tell Edmund in plain English what now works, what to test, and what comes next. Tick the step off in `README.md`.

## Rules that are easy to break

- Never show hidden numbers (standing, favour, morale and so on) to the player. The Writer's view under Papers is the only place they appear.
- Random pools: `Next: any <tag>` picks only events with that tag in `Tags:`. Untagged events are reached by name only.
- Keep each scene under 150 words, so the choices fit on a phone without scrolling.
- Saves from earlier builds must keep loading: extend `normalise()` when the state gains a field or an event is renamed.
- Nothing from Patrick O'Brian's novels: no characters, ships, incidents, dialogue or distinctive situations. Flag any echo.
- The design doc is the source of truth. Settled decisions are listed in its Decisions table; don't reopen them unless Edmund does.
