# Event writing format

How to write events for *Sloop of War*. The game reads this format directly. Write it anywhere (a note, a doc, a message) and send it over; it goes into the game as written. The Content check screen (under Papers) lists any mistakes with their line numbers.

## A complete example

```
EVENT: secretary_wait
Title: The Admiral's Office
Place: mahon

The office is a cool, high room with a sentry at the door and a clerk who does not look up.

[if pardoe_grudge] He does not offer you a chair.

CHOICE: Wait, with every appearance of patience
Effects: pass 1 watch; set waited_patiently
Next: secretary_meeting

CHOICE: Slip the clerk a guinea
Needs: money 1gn or more
Effects: money -1gn "A guinea to the Admiral's clerk"
Chance 70, +20 if new_coat:
Text: The guinea goes where guineas go.
Next: secretary_meeting
Otherwise:
Effects: set pardoe_grudge
Text: The clerk says he is not that kind of clerk. He keeps it, all the same.
Next: secretary_meeting
```

## The event

- `EVENT: name` starts an event. Names use letters, numbers and underscores only.
- `Title:` the heading the player sees.
- `Place:` where it happens: `mahon`, `ship`, `office`, `dockyard`, `agent`, `governor`, and more as they are built. Entering the event moves the player there.
- `Tags:` puts the event into a random pool (see Random events).
- `Requires:` conditions for the event to come up at random.
- `Weight:` how likely it is to be picked from its pool, compared with the others (default 1). Can take modifiers: `Weight: 2, +3 if asked_cruise, +1 per standing`.
- `Effects:` things that happen as soon as the event is entered.
- One-word lines:
  - `Start`: the first event of a run.
  - `Once`: never repeats.
  - `Urgent`: if it can come up, it comes up before anything else in its pool.
  - `Hub`: the place's home screen. Choices with no `Next:` return to the hub of the place they are in.
  - `Ending`: ends the run and shows the log.
- Everything else, until the first `CHOICE:`, is the scene. Separate paragraphs with a blank line. Keep it under 150 words so the choices fit on a phone.

## Paragraphs that only sometimes appear

Start a paragraph with `[if condition]` and it appears only when the condition holds: `[if new_coat] His eye rests on the new epaulette.` Any condition works, including times: `[if after 20:00] The lights of the town are going out.`

## Choices

- `CHOICE: text` starts a choice. Two to four per event; a hub may have more.
- `Requires:` the choice is hidden unless this holds.
- `Needs:` the choice is shown greyed out unless this holds.
- `Why not:` the reason shown under a greyed-out choice. Without one, a money shortfall explains itself and anything else says "Not open to you now."
- `Effects:` what happens when chosen.
- `Text:` a short result passage shown before moving on. Optional.
- `Log:` a line written into the commander's log, in his own voice.
- `Next:` where to go: an event name, `any <tag>` (a random event from that pool), `watches 6` (sail on; see At sea), or `end`.

## Chances

`Chance 60:` starts what happens on success (60 in 100); `Otherwise:` starts what happens on failure. Each can have its own `Effects:`, `Text:`, `Log:` and `Next:`. Lines before `Chance` happen either way.

Modifiers go after the number, separated by commas:

- `Chance 40, +20 if clerk_obliged, -30 if pardoe_grudge:`
- `Chance 25, +15 per standing:` (adds 15 for each point of standing; subtracts if standing is below zero)

The player never sees the numbers.

## Random events

`Next: any mahon` picks one event tagged `mahon` that can currently come up, weighing each by its `Weight`. An `Urgent` event is always picked first. If nothing fits, the player goes to the Mahon hub. Events without `Tags:` are never picked at random; you reach them only by name.

## Conditions

Separate with commas.

- `new_coat` (a flag is set), `not new_coat`
- `morale 3 or more`, `morale 0 or less`
- `money £8 or more`
- `day 3 or more` (the day of the commission; the first day is day 1)
- `before 16:00`, `after 20:00` (time of day)
- `sail_by 3 days or more` (time since a timer was started; also `hours` and `watches`)
- `place mahon`

## Effects

Separate with semicolons.

- `set new_coat`, `clear new_coat`
- `morale +1`, `morale -2`, `morale = 0`
- `money -£8 "A commander's coat"`: the words in quotes go into the Accounts. Without them, the event's title is used.
- `debt +£31 10s "Mr Crouch, thirty pounds advanced"`: money owed, kept in its own account.
- Amounts: `£8`, `15s`, `2s6d`, `£4 4s`, `1gn` (a guinea).
- `pass 1 watch`, `pass 3 hours`, `pass 2 days`, `pass 30 minutes`
- `until 19:00` (move the clock forward to that hour, into the next day if need be)
- `start sail_by`, `stop sail_by` (timers)
- `orders cruise_catalan` (gives the player those written orders; see Orders)
- `log "Wrote home."`

Flags and numbers can be invented as needed; any new name simply starts at zero. They are hidden from the player. The Writer's view shows them while testing.

## In the text

- `{name}`, `{surname}`, `{ship}`, `{money}`, `{debt}`, `{cash}`, `{date}`, `{place}`, `{orders}` and `{voyage}` are filled in, and so is any number, such as `{leak}` or `{water_days}`.
- `*Wryneck*` sets italics. Ordinary quotes and apostrophes are curled automatically.
- Glossary terms are underlined automatically: write the word and the game finds it.

## Orders

Written orders the player can read under Orders. Giving new orders replaces the old ones, and sets the flags `has_orders` and `orders_<name>` (for example `orders_cruise_catalan`).

```
ORDERS: cruise_catalan
Heading: A cruise on the coast of Catalonia

By Sir Robert Lessingham, ...

You are hereby required and directed ...

> Given under my hand at Port Mahon, {issued}.
> R. Lessingham
```

A line starting with `>` is set to the right, like a signature. `{issued}` is the date the orders were given.

Orders also say how long each leg of the voyage takes, until the chart arrives:

```
Passage: 8 watches
Station: 42 days
Return: 8 watches
```

## At sea

- `Next: watches 6` sails up to six watches (four hours each), one at a time. After each watch, an `Urgent` event tagged `sea` happens at once if one fits; otherwise there is a small chance (`sea event chance` in Settings, per watch) of an ordinary `sea` event. If nothing happens, the player comes back to the sea hub.
- `voyage outward`, `voyage station`, `voyage homeward` start a leg, with its length taken from the orders. `voyage station 10 days` sets the length yourself. When a leg runs out, the flag `outward_done`, `station_done` or `homeward_done` is set, so an `Urgent` event can pick it up.
- Conditions: `voyage station`, `not voyage homeward`.
- Stores are issued at noon each day while the flag `at_sea` is set.

## The ship and her stores

The `SHIP` block gives the ship's starting numbers. They behave like any other number (`leak +3`, `hull 80 or more`):

```
SHIP
victualled: 98
leak: 2
hull: 86
cash: £11 4s 6d
```

Each `STORE` block describes one kind of store:

```
STORE: beef
Name: Beef
Unit: cask | casks
Holds: 152 lb
Pieces: 38
Ration: 2 lb on Tuesday and Saturday
Capacity: 28
Keeps: 365
Bad: 3
Short: 15
Bad word: stinking
Log openings
Stock: 9 casks, Nos 205–213, received 1799-10-14 from the victualling yard at Gibraltar
```

- `Holds:` what one cask (bag, butt) holds: `112 lb`, `108 gallons`, `64 pints`, or a plain `1` for things counted singly, like shot.
- `Ration:` per man, `every day` or `on` named days. Use the same kind of measure as `Holds`.
- `Kept by:` purser (the default), master, gunner, boatswain or carpenter. It decides which page of the Books it appears on, and only the purser's stores can be skimmed.
- `Capacity:` how many the ship can stow.
- `Keeps:` days before it goes off. `Bad:` the chance in 100 that a cask opened is found bad, trebled once it is past keeping. `Bad word:` how the steward describes it.
- `Pieces:` and `Short:` for salt meat: pieces to a cask, and the chance in 100 that a cask opened is short of some.
- `Log openings`: write each cask opened into the log, by number.
- `Instead of: wine`: issued only when that store has run out.
- `Only if: carronades`: starting stock only if the condition holds.
- `Bought`: not supplied by the victualler, so not filled by "complete provisions".
- `Stock:` lines give what is aboard at the start: how many, the first cask number, when and where received.

In events:

- Conditions: `water_days 10 or less` (days left at the present allowance, by the books), `powder 1 or more` (casks, by the books).
- `store powder -0.48 "Expended in exercise"`, `store lemon_juice +3 "Bought of the contractor"`
- `empty shot6 "Returned into store"`
- `fill provisions "Received of the agent victualler"` (all the purser's victualling stores), `fill water "..."`
- `allowance short`, `allowance full` (two-thirds allowance; also sets or clears the flag `short_allowance`)
- `survey`: counts the hold and corrects the books, setting `survey_over`, `survey_short` or `survey_right`. `{survey}` gives the result in words.
- When a cask is found bad, the flag `bad_cask` is set. `{bad_item}`, `{bad_no}` and `{bad_word}` describe it, and `condemn` throws it out and enters it in the books.
- `roll purser_skims 50` sets a flag with that chance in 100.

## Glossary

```
GLOSSARY
bumboat: A shore boat that sells fruit, drink and small wares to ships in harbour.
guinea | guineas: A gold coin worth twenty-one shillings.
```

Alternative forms go before the colon, separated by `|`.

## Settings

`money values: debt, cash` marks a number as money, so it is written in pounds, shillings and pence and kept in the Accounts. `place.office: The Admiral's office` sets the name shown in the strip for a place.

## Comments

A line starting with `#` is a note to yourself and is ignored.
