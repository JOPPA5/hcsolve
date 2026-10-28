ACCEPT

# Review 1 — HCP 1537 / pc_hcp_218 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-28. Short version: **the key and the reading are right.** I re-read all 13 rows (289 signs) on the scan myself, and my reading matches the solver's sign for sign except for one: the last sign of OPET. The card has the D-shape there, so it literally reads OPED. The solver normalized this silently (finding 1). Everything else is minor.

## What I verified and how

1. **The documented command.** I ran `python3 -I ciphers/hcp-1537/work/decode.py` (the codex-runtime interpreter named in SOLUTION.md behaves the same, and so does the system `python3`). It exits 0 and prints `VERIFIED: 3 originals; 13 ordered rows; 289 indexed glyphs …`. The 13 printed lines are byte-identical to `work/plaintext-literal.txt`. Output: `review/work/solver_output.txt`. Without `--write-derived` the script writes nothing (I checked the code, and the work/ timestamps did not change).
2. **Independent decoder.** `review/work/decode_review.py` is my own 23-entry table, written from the key table in SOLUTION.md and not importing solver code. Decoding the solver's cipher rows (`solver_cipher.txt`, extracted from `manual-records.json`) gives exactly `work/plaintext-literal.txt` (`solver_decoded_by_reviewer.txt`, `diff` empty). The key is a fixed one-to-one table, so no sign takes two values. 289 signs, all mapped, with no unmapped characters. Counts are in the decoder's stderr. The key is the transferred Anna Tichá family key, with the solver's own shape labels. The published reference names its sign classes only abstractly (G01…G21). I therefore checked the key by its effect, not class by class: the same table yields coherent Czech on every row of this card and of hcp-1542/1544.
3. **Independent reading of the scan.** I rotated `source/picture.jpg` clockwise and cropped every row in two halves at 4–5× with ffmpeg (`review/work/crop.sh`, `up1x.png`, `r*.png`, `s*.png`). I then zoomed into the solver's checkpoints and a few of my own (`z_*.png`): SRDECNY, DIK ZA, JIZ ZE, POJEDU, TYDNE, PRI/PRISTIHO, VAMBERCE, BRZKY, OPET. My reading, made before comparing, is in `review/work/reading_review.txt`, and its decoding is in `reading_review_decoded.txt`. `diff` against the solver's records shows **one difference** (row 13, OPET, finding 1). In particular I confirm:
   - **VAMBERCE**: eight signs `f6np5hs5`, with the descending p-shape (B) and the tall h-shape (R). It is not FAMILCE.
   - **BRZKY**: five signs. The open-hooked q-form (Z) is followed by the closed-loop g-form (K).
   - **PRI / PRISTIHO**: the angular 4 (I), not the upright 1 (Y).
   - **DEFINITIVNE**: the 3rd sign is the shallow-v F, clearly different from the looped f (V) at sign 9 of the same word.
   - The q/g (Z/K) split holds throughout. Every Z (ZA, JIZ, ZE, ZAPOMNELA, ZACINALI, ZACINAL, JIZ, BRZKY) has the open hook, and every K has the closed loop.
4. **Completeness.** Both sides inspected in full. The picture side holds 13 cipher rows to the right of and below the roses, the date `17/IX1903.` (plain), the printed `Flora-Serie II No. 17` and the Eismann/Leipzig imprint. The last three rows continue to the left under the date, and the solver includes them. I found no other cipher group. The address side is plain Czech (`Velectěná Slečna / slečna Anna Tichá, / učitelka v / Žirovnici / u Počátek.`), with the stamp and a `ŽIROVNICE … 03` postmark.
5. **Language and context.** The text is natural Czech of c. 1903 throughout, with no forced words: *Srdečný dík za drahý lístek. Myslil jsem již, že jsi úplně na mne zapomněla. Kdy začínali jste nový školní rok? V klášteře začínal rok asi dnes. Nepřijde-li nic neočekávaného do toho, pojedu asi koncem příštího týdne na dovolenou. Účinkování při večírku ve Vamberce jsem již definitivně odřekl. Tisíc pus posílá ti tvůj Pepouš a těší se opět na brzký lístek.* It fits the context:
   - The recipient is a teacher, hence the question about the new school year.
   - 17 September 1903 was a Thursday, and mid-September is when the school year starts.
   - The postmark is from Žirovnice, matching the address.
   - The signature Pepouš matches the other cards of this family.
6. **Prior work.** SOURCES.md discloses the transfer of the published family key and the pc199 reference. The bounded check of the family index and register shows no published reading of pc216–218. Nothing suggests that a solution of this card was used.

## Findings

1. **minor — OPET ends in the D-shape, not the T-shape. The card literally has OPED, and the solver normalized it silently.** Detail: `review/work/z_opet.png`, compared with `s09mid.png` and `z_r13_ti_tvuj_tesi.png`. The last sign of row-13 word 8 is a plain stem with a separate top bar and no bowl. That is the solver's `t` label (→ D), the same shape as in `t3` DO (row 9). It is not the left-bowl `d` (→ T) of `d3r3` TOHO, `d4` TI, `df2y` TVUJ or `d5c4` TESI on the same row. The solver records `3b5d` and prints `opet`, without a note. The record should be `3b5t`, the literal plaintext `oped`, and the editorial Czech should give *opět* as an explicitly marked correction of a writer's slip, the way the hcp-1544 solution handles MOSI→MOCI. The meaning does not change.
2. **minor — "no undeciphered span remains" is fair, but the uncertainty section should list OPED and the other close calls by name.** The solver's controls cover PRI/PRISTIHO, VAMBERCE, BRZKY and F. After finding 1, the uncertainty list should also state that one sign was a writer's slip, so a reader of the report does not assume the cipher text is flawless.
3. **minor — VAMBERCE can be identified.** *ve Vamberce* is the older Czech locative of **Vamberk** (East Bohemia, Rychnov nad Kněžnou district), on the same pattern as Žamberk → *v Žamberce*. The solver is right not to change the literal text. The report can still say that the reading names a real town, which is further evidence for the reading. Whether this is the place the sender meant remains an inference.
4. **minor — the reproduction command names a machine-specific interpreter** (`/Users/…/.cache/codex-runtimes/…/python3`). Plain `python3 ciphers/hcp-1537/work/decode.py` works the same in read-only mode, and the command in SOLUTION.md/report should use that form.

## Required for closing

- Record row 13 OPET's last sign as `t` (literal `oped`) and list it as a disclosed writer's slip, with *opět* as the editorial reading.
- Optionally identify Vamberk and make the command portable.

No new review round is needed if this is done as stated.

## What I could not verify

- The day digits of the address-side postmark (only `ŽIROVNICE … 03` is clear).
- Who Pepouš and the *klášter* are. Neither is part of the cipher claim.
- Novelty beyond the solver's bounded register and family-index snapshots.
