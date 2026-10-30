REVISE

# Review 1 of HCP 1346 / pc_hcp_27 (reviewer: Claude Opus 5.5, 2026-10-30)

The solution stands: key, German text and translation are right. It needs one transcription correction with disclosure (finding 1) and smaller honesty fixes. I tried to refute it and could not. No alternative key or text came up.

## What I verified and how

- **Solver command:** `python3 -I ciphers/hcp-1346/work/decode.py` ran. Hashes OK, 290 signs, 30 `~`, 0 unkeyed. Its output matches the claimed plaintext word for word, once B/V and the umlauts are normalised as stated.
- **Independent decoder:** `review/work/my_decode.py` has its own key, typed from the two digit-order rows, and does not read `key.json`. Same text. 20 sign types, IC 0.073 on the decoded text, normal for German. The key covers every sign.
- **Scan check:** I checked every row on 3x contrast crops of `work/hires/pc_hcp_27_pic.JPG`. The weak words and all claimed uncertainties were checked at 6-12x. Crops and the helper `crop.py` are in `review/work/` (`r*`, `t16`, `m17*`, `z_*`, `y_*`). The original also carries the portal watermark; it is not cleaner than the large conversion, only larger.
- **Word count check:** sign counts agree with the pixels in the hard words. `verbleibt` looks like 10 signs, but the 7 there is one sign with head, crossbar and long descender, so 9 is right.
- **Key evidence:** `einverstanden`, `verbleibt` and `verlassender` all use 1. for V, as claimed, and the sign is visibly dotted at least in R11. Z = 5.: a mark is visible at both places (R03, R14). The dotted row A B C D P [Z] R S T U and plain row E–I K L, N O, with M on 0, are as described. Z in place of Q is a real oddity, and it is disclosed.
- **Language and context:** the text is natural German of the period (`den Plan ... teile ich dir noch mit`, `verbleibt dein dich nie verlassender August`). The translations are faithful. Address side confirmed: *Fräulein M. Scheck*, *in Neunkirchen*, a street line ending *-park*, 5 Pf. Germania, St. Johann and Neunkirchen (Bez. Trier) postmarks of 16.4.01.
- **Sources:** portal status Not solved, nothing attached. No sign of an undeclared published solution. Grep over `ciphers/*/SOLUTION.md` and metadata found no other Scheck card.

## Findings

1. **major: `ging` (M17) is not what the pixels show, and this is not disclosed.** See `review/work/y_ging2.png` and `m17b.png`. Both 3s carry a clear dot: one under the foot of the first 3, one after the last 3. The last one is separate from the word divider that follows further on, so the two marks cannot both be dividers. Literally the word is `3. 5 8 3.` = DIND, which is no word. The transcription gives `3 5 8~ 3`, with no `~` on either 3, and the only `~` is on the 8. `ging` is almost certainly the intended word, but it is an emendation of two dotted signs (a writer's slip, or stray dots). That conflicts with "the dot is part of the sign" and "none ... leaves a word unread". Fix: transcribe what is there (`3.~ 5 8~ 3.~` or similar), add a note in Uncertainties, and state that G (plain 3) then rests on *Sonntag*, *gestern* and *August*. In my crops *Sonntag* (`y_sonntag.png`) and *August* (`y_aug.png`) have no dot on the 3. The decoder needs an explicit override or apparatus for this word, so that the single command still reproduces the published text honestly.

2. **minor: `Teil` (R02), first sign, not flagged.** See `z_teil.png`, `y_teil_col.png`. It lies on the watermark edge. The shape is between 8 and a footed 2, its lower loop is very small, and no dot is visible with confidence. Compare the clear `8.` in R09 (`y_teil9.png`). `Teil` is right from context and R09, but it should be `8.~`.

3. **minor: the V of `verbleibt` (R15), dot not visible with confidence** (`y_verb1.png`). It is transcribed `1.` without `~`, while the same place in `verlassender` has `~`. Should be `1.~`.

4. **minor: the `~` marking is uneven in other places.** The second sign in *nach* (R13, `r13a.png`, third sign 2.) looks like 9 too, the same confusion disclosed for R05 only. The 6. and neighbouring signs of *gestern* lie under watermark glyphs. Uncertainty 3 should say that the 2/9 confusion is general. The count "30 of 290" will change after findings 1–3.

5. **minor: `nie` is better supported than the solver says; correct the note.** See `z_nie.png`, `y_5s.png`. The writer's 5 regularly has a long top bar running right over the next sign (R15 `5 2.`, R10 `5 1.`, M17). In `nie` the middle sign has an S-shaped body with exactly that bar, reaching the top of the last stroke. The last sign has no crossbar, and this writer's 7 always has one (with hooked head and long descender). So `8 5 1` is a pixel reading once the bar is assigned to the 5, not just a context reading. Uncertainty 1 ("weakest word", "pixels look like 8 3 7") can be restated. The weakest word on the card is now `ging`.

6. **minor: stale statistic.** SOLUTION.md says the plain/dotted split follows from statistics, and NOTES.md gives "2 followed by a dot 17 of 23 times". The final transcription has 2. 15 times and plain 2 three times. Update it or label it as the first-pass count.

## What I could not verify

- The street line of the address, which I did not attempt to read in full.
- Who "Mir" is. The pet-name reading is the solver's disclosed guess, and I have no better one.
- Individual faint dots marked `~` in *Hause*, *Da*, *abend*, *August*, *Stelle*: their letters are determined by the word, not by the pixels. Marks I did find there are consistent with the reading.
- Absence of a published solution beyond the portal page; neither the solver nor I did a literature search.
