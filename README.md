# Sloop of War

A text-based roguelike for the browser. You are a newly made Master and Commander given a 16-gun sloop at Port Mahon around 1800, with orders to harass the King's enemies in the Western Mediterranean.

The game runs entirely in the browser from a single page, `index.html`, with no server. Runs are seeded, so the same seed and the same choices always give the same commission.

## What's here

| Path | What it is |
| --- | --- |
| `index.html` | The game: the writing (events, orders, glossary) as plain text, then the engine |
| `docs/design-document.md` | The design document, the source of truth for what the game should be |
| `docs/event-writing-format.md` | How to write events, orders and glossary entries |
| `tools/playtest.py` | Automated playtest: content check, hundreds of random playthroughs, replay check |

## Status

Built in thirteen playable steps (see "Build sequence" in the design document).

- [x] 1. Engine shell
- [x] 2. Mahon and orders
- [x] 3. Ship, stores and time
- [x] 4. Wind and weather
- [x] 5. Combat sandbox
- [x] 6. Chart and navigation
- [ ] 7. Crew and officers
- [ ] 8. Encounters and chases
- [ ] 9. Full combat
- [ ] 10. Aftermath and prizes
- [ ] 11. Career and endings
- [ ] 12. Content and balance
- [ ] 13. Polish

## Playing it locally

Open `index.html` in a browser. Saves are kept in the browser, and can be saved to and loaded from a file under Papers.

## Source material

An original game in the period and genre of the great naval novels. Nothing is taken from any novel: no characters, ships, incidents or text.
