# Sloop of War: Design Document

Oct 17, 2026 · @Bovril

## Concept and pillars

*Sloop of War* is a text-first roguelike in which the player, a newly made Master and Commander, takes a 16-gun sloop out of Port Mahon around 1800 and tries to win prize money, reputation and a post-captaincy before shot, shoal, scurvy or the Admiralty end the run. Each run is one commission: typically 6 to 18 in-game months, 2 to 5 hours of play.

The game borrows the period and the genre the novels made famous, and nothing else: no characters, ships, incidents or text from the sequence. Its cast comes from the service itself: the rich-but-dim post-captain, the Maltese agent, the Admiral's secretary with a grudge, the gunroom's resident bore.

### Design pillars

- **Seamanship is the game.** Wind, sail and position decide most outcomes before a gun is fired. A player who understands the weather gauge should beat one who merely has more guns.

- **The commander never knows enough.** Information arrives late, partial and second-hand: the ship's position is an estimate, a strange sail is a guess, and damage below decks is learned only when the carpenter reports. Much of the skill is deciding on incomplete knowledge.

- **Men, not hit points.** The ship is a society of about 100 souls. Morale, skill and loyalty are as much a resource as powder, and they are spent and replenished in recognisably human ways.

- **The Navy is a bureaucracy with cannon.** Orders, prize courts, patronage, seniority and paperwork shape the run as much as the enemy does.

- **Prose as interface.** Text carries the atmosphere: period diction, the log-book register, the occasional dry aside. Diagrams appear only where position matters (combat, pilotage).

- **Every run tells a story.** The end screen is a Gazette letter or a court-martial transcript, not a score table.

### Tone

Dry, exact and humane. Period vocabulary is used freely but always glossed on hover. Death is sudden and unsentimental; comedy comes from character and institution, not from the narrator winking. The register sits somewhere between a captain's log and a well-read letter home.

### Audience

Readers of O'Brian, Forester and Kent; players of *FTL*, *Sunless Sea*, *Out There* and *Sid Meier's Pirates!* who want more friction and less arcade. No prior knowledge of sailing is assumed, but it is rewarded.

## Core loop and run structure

A run is a sequence of cruises, each beginning and ending in a friendly port, framed by orders from the Commander-in-Chief at Mahon.

### The cruise loop

- **In port.** Receive or negotiate orders, recruit and press men, buy and beg stores, refit, sell prizes, dine with people who matter.

- **Sail.** Plot a course on the chart; time advances in watches (4 hours). Weather, encounters and shipboard events fire per watch.

- **Sight a sail.** Identify, decide: chase, close, avoid, or show false colours.

- **Engage or evade.** Tactical combat (see below), or a chase resolved over several watches.

- **Aftermath.** Butcher's bill, repairs at sea, prize crews detached, prisoners secured.

- **Return.** Sell prizes, file reports, face the consequences. Repeat or end the commission.

### Run length and ending conditions

A commission ends when one of the following occurs:

- **Promotion to post-captain** (victory). Triggered by a single brilliant action, accumulated reputation plus interest, or a capture of sufficient political value.

- **Loss of the ship** by sinking, wreck, capture or fire. Followed by a court-martial screen whose outcome depends on the circumstances and the log.

- **Superseded or beached** for disobedience, disgrace or a powerful enemy ashore.

- **Death** of the commander. Rare but possible: a sniper in the tops, a fever, a duel.

- **Peace.** The war follows its own loose course, not the historical calendar. Rumours of an armistice can begin after the first year, growing likelier with each cruise; a run that reaches the peace unpromoted ends on half-pay.

### Permadeath and meta-progression

The commander dies with the run; the world does not. Between runs the player keeps:

- **The Navy List.** Officers who served well under you can reappear as "followers" in later commissions, carrying their traits.

- **Interest.** A small pool of patronage carried forward, representing the family name and old shipmates.

- **The Log Library.** Every completed run's Gazette letter or court-martial transcript, readable and shareable.

There are no permanent stat upgrades. Progression is knowledge of the sea and a slowly improving starting position, as in a real naval family.

### Difficulty

Three settings, named for the period: **Half-pay** (forgiving weather, generous prize courts), **Mediterranean Station** (default), **Channel Fleet** (ironman saves, fog, vindictive Admiralty).

## Navigation

The player never knows exactly where the ship is; navigation is the management of that uncertainty against wind, current and coast.

### The chart

The Western Mediterranean from Gibraltar to Sicily, rendered as a period chart on a hex grid of roughly 10 nautical miles per hex. Key zones:

| Zone | Character | Typical prey and threats |
| --- | --- | --- |
| Balearics and Mahon | Home waters, well charted | Privateers, French packets |
| Catalan and Valencian coast | Rich coastal trade, Spanish batteries | Tartanes, xebecs, gunboats, shore guns |
| Gulf of Lion | Mistral, heavy seas, few refuges | French convoys out of Marseille and Toulon |
| Toulon approaches | Blockade waters | French frigates, the fleet itself |
| Ligurian and Tuscan coast | Neutral ports, intrigue | Genoese traders, Leghorn privateers |
| Barbary coast | Dey's corsairs, uncertain treaties | Algerine galleys, plague ships |
| Straits and Alboran | Strong east-going current | Spanish gunboats from Algeciras, Atlantic convoys |

### Wind and points of sail

Wind has a direction (8 points of the compass in play, 32 in the log) and a Beaufort force. The sloop's speed is read from a polar table: fastest on a broad reach, slow close-hauled, unable to sail closer than about 6 points off the wind. Beating to windward means tacking, and each tack is a crew-skill check that can miss stays in heavy weather.

Regional weather systems drive the wind: the Mistral (north, violent, cold), the Levanter (east, fog in the Straits), the Sirocco (south, hot, dust), the Tramontana, and dead calms in high summer. A three-watch forecast is available from the sailing master, with accuracy tied to his skill.

### Dead reckoning

The ship's true position and the plotted position diverge each watch by an error driven by current, leeway, weather and the master's skill. The player sees a circle of uncertainty on the chart. It shrinks when:

- a noon sight is taken (clear sky required; error depends on the master and the chronometer, if one has been bought);

- a known headland or light is sighted and identified;

- soundings match the chart's depth markings.

Running on a lee shore at night with a wide uncertainty circle is the game's principal source of dread.

### Hazards

- **Lee shores** in onshore gales: clawing off is a multi-watch crisis using sail, anchors and crew strength.

- **Shoals and reefs**, some uncharted, revealed by leadsman calls.

- **Fog**, which hides both prey and predators and makes collision possible.

- **Calms**, during which galleys and gunboats can row up to a helpless sloop, and boats or sweeps are the only answer.

### Landfall and inshore work

Inshore actions switch to a local pilotage map: anchoring, warping, cutting-out expeditions, landing parties against signal stations and batteries. A hired local pilot, if trustworthy, removes much of the uncertainty.

## Naval combat

Combat is strictly turn-based on a small tactical grid, on a two-speed clock, and most fights are won or lost in the approach.

### Turns and time

- **Manoeuvring turns: about 5 minutes each**, from the moment the tactical grid opens until either side fires. This gives room for the long approach: tacking and wearing for the gauge, shortening sail, clearing for action.

- **Firing turns: about 30 seconds each** once a gun is fired. Reloading a broadside takes several turns, so drill shows on the clock: a crack crew reloads in 3 turns (90 seconds), an average one in 4, a slack one in 5 or more.

- **Reversion.** If no gun is fired by either side for 10 firing turns, the clock returns to 5-minute turns, for example when one ship has drawn out of range or the action has become a chase.

### Phases

- **Sighting and identification.** At extreme range a sail is only a sail. Each watch brings it closer to identification: rig, hull, flag, behaviour. False colours and private signals let both sides lie.

- **The approach.** Played in 5-minute turns. The player chooses a heading relative to the wind; the key question is who holds the **weather gauge** (upwind position), which lets that ship choose when and whether to engage.

- **The engagement.** Ships on the grid with heading, sail state and speed. Each turn the player issues helm, sail and gunnery orders, then both sides move simultaneously.

- **Resolution.** One side strikes, flees, sinks, burns or is carried by boarding.

### Movement

Ships move by heading and sail plan (bare poles, fighting sail, all plain sail, studdingsails). Turning through the wind (tacking) or away from it (wearing) takes turns and crew. Damage to rigging slows a ship and can leave it in irons. Raking positions (across the bow or stern) are the prize: a raking broadside does triple hull damage and sweeps the deck lengthwise.

### Gunnery

The sloop carries 16 6-pounders or 16 18-pounder carronades, depending on fit-out. Each broadside is resolved by:

- **Range bands:** point-blank, close, long, extreme. Carronades are devastating close and useless far.

- **Aim:** at the hull (kill men, hole the ship), at the rigging (slow and disable, for a chase or a prize), or double-shotted at point-blank.

- **Rate of fire:** measured in firing turns to reload, set by the gun crews' drill level (see Turns and time).

- **Roll and sea state:** firing on the uproll favours rigging, the downroll favours hull.

Damage falls on hull, rigging, guns, crew and specific officers. A named officer can be struck down mid-action, which immediately affects whatever he was responsible for.

### What the commander knows

The commander sees only what can be seen from the quarterdeck: spars falling, men carried below, guns on his own side falling silent. Everything else arrives by report.

- **Carpenter's report, every half hour (60 firing turns):** depth of water in the well, leak rate, shot-holes at and below the waterline, the state of the pumps.

- **Surgeon's return, at the same interval:** killed and wounded, by name for officers and as numbers for the people.

- **Gunner's report:** powder and shot remaining, guns dismounted or burst.

- **Early reports** can be ordered at a cost: a midshipman sent below leaves his division for several turns, and calling the carpenter up takes him off his shot-plugs.

The enemy's state is inferred, never shown: his rate of fire, visible damage aloft, a list in the water, men seen leaving his guns. Officers offer readings of these signs, with accuracy tied to their skill, and they can be wrong.

### Boarding and boats

Boarding is resolved as a short sequence of melee rounds: boarders against defenders, weighted by numbers, morale, marines and the officer leading. Cutting-out expeditions (boats against an anchored prize at night) are a distinct mini-scenario with stealth, timing and a high chance of something going wrong.

### Ruses

The player's best weapon against a superior foe. Options include false colours, disguising the ship as a merchantman or plague ship, signalling a non-existent squadron over the horizon, and running inshore where a frigate dare not follow. Each ruse has a plausibility check based on the enemy captain's traits and what he has already seen.

### Chases

Most encounters end as chases. A chase is resolved over watches, not turns: relative speed on the current point of sail, wind shifts, nightfall and the crew's willingness to wet the sails and start the water. Darkness gives the quarry a chance to alter course unseen.

### Prizes and prisoners

A captured ship needs a prize crew, typically a midshipman or master's mate and 6 to 12 men, which weakens the sloop for the rest of the cruise. Prisoners must be fed and guarded, and can rise. Prize value depends on hull, cargo, and the prize court's mood; neutral ships risk being released with costs against the captor.

## Crew management

The crew operates at two resolutions: the foremast jacks as a handful of aggregate gauges, the officers and warrant officers as named individuals with traits, histories and agendas.

### The people (aggregate)

A 16-gun sloop's complement is about 100: officers, warrant officers, petty officers, perhaps 15 marines and some 75 seamen, landmen and boys. The people are tracked as a single body with these gauges:

| Gauge | Range | Raised by | Lowered by |
| --- | --- | --- | --- |
| Numbers | 0 to complement | Recruiting, pressing, volunteers from prizes | Casualties, disease, desertion, prize crews |
| Seamanship | Landsmen to prime seamen | Time at sea, good petty officers | Pressed landsmen, losses of skilled men |
| Gunnery | Slack to crack | Live-fire exercise (costs powder and shot) | Casualties among gun captains |
| Morale | Mutinous to devoted | Prize money, victory, fair discipline, fresh food, grog | Flogging, short rations, defeat, long cruises with no reward |
| Health | Sickly to hale | Fresh provisions, a good surgeon, dry clothes | Scurvy, fevers, foul water, wounds |

The crew also has a small set of **flags**: a known sea-lawyer, a gang of Irish pressed men, a Jonah aboard, a disaffected faction from the previous captain. Flags drive events.

### Watch and quarter bill

The player sets the broad organisation once per cruise: two watches or three, how heavily to man the guns versus sails at quarters, the size of the boarding party. These are trade-offs, not micromanagement.

### Discipline

Punishment is a recurring choice: let it pass, stop the grog, start the offender, or flog at the gangway. Too lenient and petty crime and drunkenness rise; too severe and morale and loyalty fall, and the ship acquires a reputation that deters volunteers. A hanging offence requires a court-martial and colours the commander's record.

### Officers and warrant officers (individual)

Each named officer has four core attributes (**Seamanship, Gunnery, Leadership, Sobriety**), one or two **traits**, a **loyalty** score to the commander, a **backstory hook**, and sometimes **interest** (a patron ashore). Typical sloop establishment:

| Post | Number | What they govern |
| --- | --- | --- |
| Lieutenant | 1 | Second in command; watch-keeping, boarding parties, prize command |
| Master | 1 | Navigation, forecasts, pilotage, stowage |
| Surgeon | 1 | Health, wound survival, disease; the casualty return in action |
| Purser | 1 | Stores, slops, provisioning cost; skims if dishonest |
| Boatswain | 1 | Rigging repair, sail handling, discipline among the people |
| Gunner | 1 | Gun drill, powder supply, rate of fire |
| Carpenter | 1 | Hull repair, leaks, fitting new spars |
| Midshipmen and master's mates | 3 to 5 | Prize crews, boat command, divisions; future lieutenants |
| Marine officer | 0 to 1 | Marines' reliability; often absent on a sloop, sergeant instead |
| Captain's clerk and steward | 1 each | Paperwork accuracy; the commander's own table and morale |

### Example traits

- **Old Navy** (master): +navigation, refuses to learn from a younger commander, -loyalty when overruled.

- **Tarpaulin** (lieutenant): came up from the lower deck; superb seamanship, socially awkward ashore, resented by the gunroom.

- **Sawbones** (surgeon): high wound survival, poor with fevers. **Natural philosopher**: requests landings for specimens, fills the bread-room with cases, and is occasionally right about the weather.

- **Nephew of an Admiral** (midshipman): useless, untouchable, valuable.

- **Light-fingered** (purser): stores leak away unless audited.

- **Methodist** or **Ranter** (boatswain): raises crew sobriety, causes friction.

- **Drunkard**: random events, sometimes brilliant, sometimes fatal.

### Gunroom relationships

Officers have opinions of one another, tracked as a simple relationship web. Feuds produce duels, insubordination and refusal to serve together; friendships produce cover in a court-martial. Dinners in the cabin are the main lever: inviting the gunroom raises loyalty and surfaces gossip, at the cost of the commander's limited private stores.

### Promotion and replacement

Dead or disgraced officers are replaced from midshipmen (acting appointments), from prisoners and volunteers of doubtful quality, or from Mahon's pool when in port, where the Admiral's own followers are pushed on you. Writing a strong letter for a midshipman after an action can get him confirmed and make him a follower for later runs.

## Ship management

The sloop is modelled as a few physical systems and a hold full of finite stores; every cruise is a race between what is being consumed and what can be captured.

### Physical systems

| System | Tracked as | Failure looks like | Repaired by |
| --- | --- | --- | --- |
| Hull | Integrity %, leak rate (inches per hour) | Pumps manned every watch, then foundering | Carpenter at sea (partial), dockyard (full) |
| Masts and spars | Fore, main, bowsprit, yards, each sound / sprung / gone | Loss of speed and pointing; a gone mast is a jury-rig crisis | Boatswain and carpenter, spare spars |
| Rigging and sails | Standing rigging, running rigging, sail suits | Slower, cannot tack, cannot set canvas in a blow | Boatswain, sailcloth, cordage |
| Guns | Count, condition, mounts | Burst guns, dismounted pieces | Gunner, dockyard only for replacements |
| Boats | Launch, cutter, jolly boat | No cutting-out, no watering ashore, no escape | Carpenter, prizes |

### Stores

Stores are tracked in days of supply at the current complement:

- **Water**: the hard limit, roughly 6 to 8 weeks. Short allowance buys time at a morale and health cost.

- **Provisions**: biscuit, salt beef and pork, pease, cheese, butter, spirits. Each goes off at its own rate; weevils are flavour, rot is a health hit.

- **Fresh food and lemons**: the scurvy clock. Taken from prizes, bought ashore, or not at all.

- **Powder and shot**: drill and battle both consume it; running dry mid-cruise forces a return.

- **Naval stores**: cordage, canvas, spare spars, timber, pitch.

- **Slops and tobacco**: minor, but their absence costs morale in cold weather.

Stowage is a choice: a hold packed with water rides deeper and sails slower. The master can restow, and trim affects speed by a few percent.

### The Purser's books

Provisioning money comes from a Navy allowance, the commander's own pocket, and sale of prizes. A dishonest purser bleeds stores; auditing him costs his loyalty. Running the ship partly on one's own money is possible and historically common, and debts follow the commander into later runs as a reputation drag.

### Refits and fitting out

At Mahon the dockyard offers repairs and modest refits, gated by the commander's standing with the Master Attendant and Navy Board officials. Choices include:

- Long guns versus carronades (range versus weight of metal).

- Coppering the hull, if not already done (+speed, expensive, slow to approve).

- Extra boats, a chronometer, swivel guns, better sails taken from a prize.

- Re-rigging the sloop as ship- or brig-rigged where the hull allows.

A famous prize may be bought into the service; if the player has been made post, it may become his next ship.

## Career, Admiralty and prize money

The commander has three currencies that matter more than the ship's: **Reputation** with the service, **Interest** with powerful men, and **Fortune** in prize money, and they do not always move together.

### Orders

The Commander-in-Chief issues orders at the start of each cruise. Types:

- **Cruise against the enemy's trade** between given limits (the default, and the most lucrative).

- **Convoy escort**: dull, dangerous, poorly rewarded, and a disgrace if a merchantman is lost.

- **Carry despatches** or a passenger: speed matters, the passenger may be a spy, a diplomat, or the Admiral's tiresome relation.

- **Support the army or allies** ashore on the Spanish coast.

- **Special service**: covert landings, intelligence work, extracting an agent.

Orders can be bent. Leaving station for a rich prize may be forgiven if the prize is rich enough and the Admiral gets his eighth; it is a court-martial matter if it goes wrong.

### Prize money

Prize proceeds are divided in eighths under the pre-1808 rules: three to the commander (one of them to the flag officer under whose orders he sails), the rest down through officers to the people, whose shares drive morale. Payment is slow: the prize court in Mahon or Gibraltar takes months, agents take commission, and some agents go bankrupt with your money. Head money is paid for enemy warships and privateers taken or destroyed.

### Reputation and interest

- **Reputation** rises with actions reported in the Gazette, falls with lost convoys, disobedience and defeats. It is read by the Admiralty when deciding promotion.

- **Interest** comes from patrons: a powerful MP, a peer, an Admiral. Patrons ask favours (take my nephew, carry this cargo, overlook that) and can fall from power with the government.

- **Enemies** are tracked too: a superior offended at dinner, a senior officer whose prize you took, a Spanish grandee.

### The Gazette letter

After a notable action the player writes, or chooses between drafts of, the official letter. Generous mention of officers raises their loyalty and promotion chances; too much self-praise is noticed. Omitting the Admiral's contribution is remembered.

## Events, encounters and text

Events are hand-written vignettes triggered by state, so that what happens aboard follows from the ship's condition rather than from a random table.

### Event structure

Each event has trigger conditions (location, weather, gauges, flags, officer traits), a short prose scene, two to four choices, and outcomes that move gauges, spawn flags or start follow-on chains. Target for launch: about 250 events, with 30 multi-stage chains.

### Sample event families

- **Shipboard:** a man overboard in a gale; theft from the gunroom; a sea-lawyer's petition; a stowaway; the cook's fire; a fight between pressed Irishmen and Cornishmen; a birthday, a crossing-the-line style frolic, a play put on by the people.

- **Officers:** the lieutenant challenges a soldier to a duel ashore; the surgeon is found selling patent remedies to the people; a midshipman is found to be fourteen and terrified.

- **At sea:** a neutral merchantman whose papers are too good; a drifting boat of survivors; a plague ship; an English deserter in a French prize crew.

- **Ashore at Mahon:** a card game with an army officer; a card party at the Governor's; a moneylender; an agent with an offer; the Governor's ball.

### Encounter generation

Sail encounters are drawn from zone tables weighted by season, war situation and intelligence. Every enemy captain is generated with a nationality, a ship, a temperament (bold, cautious, cunning, drunk) and a reputation, so that a known French frigate captain can be heard of, avoided, and eventually met.

### Intelligence

Espionage is occasional, never a storyline. It appears as events that narrow an information gap about other ships: a Catalan fisherman who has seen a convoy assembling, a bribed clerk in Leghorn with a sailing date, a captured packet's papers, a deserter who knows his old captain's habits. Each is uncertain and may be a plant, and acting on it is the player's gamble.

### Text and voice

Written in a pastiche of late-Georgian naval prose: log-book entries for routine, fuller narrative for events, and dialogue that gives the gunroom distinct voices. Rules for writers:

- Period vocabulary used correctly and glossed on hover; no modern idiom in dialogue.

- Original characters, ships and incidents; historical figures appear only as distant authority (St Vincent, Nelson, Lord Keith).

- Short paragraphs; the player should never scroll to find the choice.

- The log is written by the game in the commander's voice and forms the run's record.

### Writing content

Events are written in a plain-text format the writer drafts directly (see the separate "Event writing format" doc). The game reads it as is; nothing is converted into code. A Content check screen in the game lists any mistakes with their line numbers, and a Writer's view shows the hidden gauges and flags while testing.

## UI, presentation and browser tech

The interface is a single page with prose at its centre and a small number of instrument panels around it, playable on desktop and phone.

### Screens

- **Quarterdeck** (main view): current log entry and event text, choices as buttons, a compact strip for wind, weather, watch and position uncertainty.

- **Chart:** period-styled hex map with plotted course, uncertainty circle, known sails and coasts.

- **Ship's books:** tabs for hull and rigging and guns, plus the purser's full ledger: every cask, bag and barrel with date of issue, condition and running balance, and the cash account beside it. Nothing is summarised into a bar, so a dishonest purser can be caught by a player who checks the figures.

- **Muster:** the people's gauges and flags; officer cards with portraits drawn as silhouettes, traits, loyalty and relationship lines.

- **Action:** tactical grid with wind arrow, ships as simple hull glyphs, firing arcs, and a running action log.

- **Mahon:** a menu of places (dockyard, Admiral's office, prize agent, taverns, the Governor's house).

### Accessibility and controls

Fully keyboard-playable, screen-reader friendly (prose-first helps), adjustable text size, and a glossary that can be toggled from sparse to generous. A compass rose rather than a wind number for players who think visually.

### Technology

- **Client-only** JavaScript app; no server required to play. Written as plain, readable source with no build step, so that every working session can read the live game back from its published page.

- **Deterministic seeded RNG**, so runs can be shared by seed and replayed.

- **Content as data**: events, ships, officers and zones in a plain-text authoring format, kept apart from the engine, so writers can add content without code.

- **Saves** in browser storage, autosaved after every choice, with export/import as a file; ironman mode keeps a single autosave.

- **Rendering**: DOM for text, SVG for chart and tactical grid. No canvas engine needed.

- **Audio** (optional): ambient sea, bells for the watch, a single fiddle motif.

## Scope, MVP and decisions

The minimum viable game is one ship, one station and one year: enough to prove that the navigation, combat and crew systems produce stories worth retelling.

### MVP

- ☐ One sloop type, fixed fit-out choice of long guns or carronades

- ☐ Western Mediterranean chart, four zones (Balearics, Catalan coast, Gulf of Lion, Toulon approaches)

- ☐ Wind, three weather systems, dead reckoning with noon sights

- ☐ Tactical combat with gunnery, raking and boarding; chases by watch

- ☐ Aggregate crew gauges; seven named officer posts with traits

- ☐ 80 events, 10 chains; Mahon with four locations

- ☐ Ending screens: Gazette letter, court-martial, death

### Later

- Barbary, Ligurian and Straits zones; cutting-out mini-scenarios; the Navy List and followers between runs; patrons and enemies; a brig and a ship-sloop as alternative commands; a post-captain epilogue mode in a frigate.

### Build sequence

Thirteen steps, each ending in a playable build published to the same link. Combat is prototyped early as a standalone sandbox because it is the riskiest system.

**Foundations**

1. **Engine shell.** Quarterdeck screen, seeded RNG, browser saves, export/import, hover glossary, and the event engine reading content from the plain-text format. *Test:* play a short scene, save, export, reload; the same seed and choices give the same result.
2. **Mahon and orders.** Four locations, the Commander-in-Chief's orders, money, dining. *Test:* get orders and spend money ashore.
3. **Ship, stores and time.** Watches; hull, spars, rigging, guns and boats; daily stores consumption; the purser's full ledger. *Test:* sail an empty sea, watch the water run down, audit the books.
4. **Wind and weather.** Polar table, tacking and wearing, missing stays, Mistral, Levanter and Sirocco, the master's forecast. *Test:* beat to windward in a blow.

**The risky core**

5. **Combat sandbox.** A standalone two-ship duel on the grid with the two-speed clock, weather gauge, gunnery, raking and the reversion rule, not yet wired into the campaign. *Test:* the fight should feel like seamanship rather than dice; tune it here while change is cheap.
6. **Chart and navigation.** Hex chart of the four MVP zones, dead-reckoning circle, noon sights, headlands, soundings, lee shores and shoals. *Test:* make a landfall at night with a wide circle.
7. **Crew and officers.** The people's five gauges; lieutenant, master, surgeon, purser, boatswain, gunner and carpenter with traits; discipline; gunroom dinners. Each officer is wired into the system he governs. *Test:* a drunk master should visibly hurt navigation.

**The cruise**

8. **Encounters and chases.** Zone tables, sighting and identification over watches, false colours, enemy captain temperaments, chases by watch. *Test:* chase a prize into the night.
9. **Full combat.** The sandbox joins the campaign, with half-hourly reports, inference of the enemy's state, officer casualties and boarding. *Test:* fight blind on reports alone.
10. **Aftermath and prizes.** Butcher's bill, repairs at sea, prize crews, prisoners, prize court, eighths, agents, head money. *Test:* take a prize home and wait to be paid.
11. **Career and endings.** Reputation and interest, the Gazette letter, court-martial, death, promotion. *Test:* play a whole commission end to end. This completes the MVP skeleton.

**Finishing**

12. **Content and balance.** 80 events and 10 chains, the three difficulty settings, tuning.
13. **Polish.** Keyboard play, screen readers, phone layout, optional audio.

### Decisions

| Question | Decision |
| --- | --- |
| Combat timing | Strictly turn-based: 5-minute turns until guns are fired, 30-second turns thereafter, so gunnery drill shows directly on the clock |
| Purser's books | Full ledger, visible and auditable |
| Historical calendar | Loose alternate war; no fixed dates such as Amiens |
| Intelligence work | Occasional events only, as one way of closing information gaps about other ships |
| Information | Deficits are a core driver: damage, casualties and enemy state are learned late, by report or inference |
| Source material | Nothing taken directly from the novel sequence: no characters, ships, incidents or text, and no licence sought |
| Build order | Thirteen playable steps (see Build sequence); combat prototyped as a standalone sandbox at step 5 before it joins the campaign |
| Code | Plain JavaScript with no build step; each build is one page published to a single link that always opens the latest version |
| Content authoring | A plain-text event format the writer drafts directly; the game reads it as is and reports mistakes on a Content check screen |
| Stores | Issued at noon each day at sea on the Navy's 1800 scale, wine in place of beer; casks numbered, oldest first; the purser's books and the real hold kept separately, so skimming shows up only by survey, by short weight, or by comparing cask numbers opened in the log with the books |
| Victualling in port | Simplified: in harbour the people are victualled from shore and the hold is not drawn on; water is about a gallon a man a day |
| Passage times | Until the chart (step 6), each set of orders states its passage, time on station and return in watches or days |
