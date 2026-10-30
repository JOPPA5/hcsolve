REVISE

# HCP1554 (pc_hcp_235) — Review round 1

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29.

**Overall assessment:** the reading stands. This is a Czech love letter from "Pepouš" to Anna Tichá, the teacher in Žirovnice, dated 22 May 1903, enciphered in the known Anna Tichá family substitution. The key, the decryption and nearly all of the transcription check out. Three things need fixing before FINAL:

- one sign is mis-transcribed (`k hradce` should be `z hradce`);
- the "completion" readings (TELEGRAM, MNE) are not in the reproducible output;
- `SOLUTION.md` contradicts itself.

## What I verified and how

1. **The solver's command.** I ran `…/python3 ciphers/hcp-1554/work/decode.py`.
   - The audit passes: 3/4/41 hashes, 21 rows, 566 units, 571 letters, 5 CH, 22/23 classes.
   - The output matches the "Exact literal reading" in SOLUTION.md row for row.
   - **However, the output still contains `tele⟦U4⟧ram` and `srdecko ⟦U6⟧ bude`.** The TELEGRAM and MNE readings proposed in "Completion and handover" are not produced by the command.
2. **Independent decoder.** My own script is `review/work/mydecode.py`. It parses `work/transcription.txt`, uses its own copy of the 23-unit key and keeps `⟦…⟧` and `[…]` opaque.
   - All 21 rows are identical to `work/literal.txt`.
   - Counts: 566 known units; 22 classes used; only shallow-v `v`/F is unused.
   - Letter frequencies (e 62, a 56, i 47, s 45, o 38 …) fit Czech.
3. **Key consistency.** `work/key.json` is the Anna Tichá family key (`ciphers/hcp-1545/work/key.json`) under different shape labels:
   - `y` here = family `7` = J;
   - `H` = family `ř` = CH;
   - `v` → F is added from the public study.
   - No sign is mapped to two values and no letter has two signs, apart from the CH unit.
4. **Transcription against the scan.** I made my own crops in `review/work/`, enlarged 5–10x with nearest-neighbour or Lanczos scaling.
   - Rows checked sign by sign: M01, M02, M03 (start), M06–M08, M12 end (U4), M13 (`do veseli`), M15 (U6), and the three marginal rows (`margin.png`).
   - Also checked: the anomaly words KDA, VZDIT, TIKAJICI and PRIJESTI, and the I12 insertion.
   - Built a g/q comparison panel, `review/work/gq-panel.png`. It contains: the M02 standalone sign; ZA in M01 and M07; JEZ in M05; KDO in M11; KAZDY in M08; U2, U3 and U5.
   - On this card, q/Z is consistently a compact "9" with a short open hook. g/K is larger, with a long returning descender loop. SCHUZKU in M03 shows both signs side by side (`schuzku.png`, `schuzky.png`).
   - The solver's U1, U2, U3 and U5 decisions agree with what I see.
5. **Language and context.**
   - The text is fluent Czech of about 1900, in the register of the other Pepouš cards.
   - Period details fit: rychlík ("express train"), poste restante, telegram.
   - Veselí (Veselí nad Lužnicí, a railway junction) and Hradec (Jindřichův Hradec) are both in the Počátky/Žirovnice area of the address.
   - Pepouš, Anunka and "na středu" match the family.
6. **Sources.** The family key and the partial study by Maxim Egorov are credited. No target-specific published plaintext is claimed or found.

## Findings

1. **[major] M02 transcribes the standalone sign before `rh6ts5` as `g`/K, but the scan shows `q`/Z.**
   - Evidence: `review/work/m02-standalone.png` and `gq-panel.png`. The sign is a compact "9" with a short open leftward tail and no returning loop. It is identical in form to the solver's own q controls (ZA, JEZ, U2, U3). It is unlike the `g` of KDO, KAZDY and MINKU.
   - This sign was never part of the solver's g/q controls.
   - The literal therefore reads `z hradce` ("from Hradec"), which is also the grammatical form. `k hradce` is not grammatical Czech.
   - At present, the literal, the command output, the first editorial reading and the Slovak translation all give `k hradce`. Only the later "Completion" editorial silently writes "z Hradce".
   - Fix: change `g` to `q` in `transcription.txt` and propagate the change to the literal, the counts (q +1, g −1) and both readings.
2. **[major] The proposed U4/U6 readings are not reproducible, and SOLUTION.md contradicts itself.**
   - The README requires a single command that produces the full plaintext. That command still prints `⟦U4⟧` and `⟦U6⟧`.
   - The older sections, which remain unchanged, say things the completion section reverses:
     - "not a complete glyph-verified solution";
     - "Nothing is assigned a new `g` plaintext value";
     - "No watcher, reviewer, marker…";
     - "candidate remains PARTIAL, with no DONE marker";
     - the key table has no G sign.
   - The completion section then asserts TELEGRAM, with a G sign, and MNE.
   - Fix:
     - add the k-shaped G unit to the key, citing HCP1541, 1553 and 1570;
     - put G at U4 and the U6 reading, explicitly marked as uncertain, into the transcription and literal;
     - update the counts;
     - rewrite SOLUTION.md so it states one current position. A history note can stay, but it must be marked as superseded.
3. **[minor] U4 (TELE?RAM): one sign, k-shaped, written over an earlier stroke. The reading is supported.**
   - Evidence: `review/work/u4x7.png`. There is exactly one tall looped sign with an arm between `d585` and `h6n`, which matches the family's k-shaped G sign.
   - I accept G here. Note, however, that the overwriting means the underlying first stroke is unknown. Say so.
4. **[minor] U6 is a guess and must be presented as one.**
   - Evidence: `review/work/u6x10.png`. I see, in order:
     - a heavy `n`;
     - a `3` with a looped stroke written above it;
     - a lighter `n`-like double hump;
     - an `m`;
     - a heavy final sign that could be 5 or 6, with a flat top bar.
   - Read literally this gives "monn…" or "momn…", which is not a word.
   - "mne", with "mo" abandoned and inked over, is plausible and grammatical. However, the 5/6 decision and the cancellation are inferences.
   - Keep `[mne?]` bracketed in the editorial text and the PDF, and list the alternatives in the uncertainty section.
5. **[minor] TIKAJICI: the second sign is an ink blob over a 4-like stem.**
   - Evidence: `review/work/tik2.png`. This looks like a correction, plausibly to `1`/Y, which would give *týkající*.
   - The solver lists it only as a base-letter anomaly. Disclose the overinking.
   - KDA (`kda2.png`, clear 6/A), VZDIT and PRIJESTI (visible `c` before `d4`) do look as transcribed. Keeping them as writer's forms is fine.
6. **[minor] Stale or contradictory administrative text.**
   - `SOURCES.md`/`SOLUTION.md` say "Human override: never watchers/reviewers" and "The portal's captured status is Not solved…no marker". `SOURCES.md` also gives the register count as 337, while the notes and orchestrator say 357.
   - Update these lines to the current state.
   - Also check the "do Veselí" final sign (`veseli3.png`). It is a stem with a foot and is closer to 1/Y than to 4/I in this hand.
     - The reading *Veselí* is surely intended, so this is low priority.
     - Either confirm `4` against the 4/I controls or note it as a possible `1`.

## What I could not verify

- **Resolution.** The image is only 1024 px wide, so fine distinctions such as 1/4 and 5/6 under overink rest on 10–20 px glyphs.
- **Coverage.** I did not check every glyph of rows M04, M05, M09–M11, M13 (apart from VESELI) or M14 at maximum zoom. In those rows I checked word shapes at 2x, and they agree with the transcription.
- **Hidden ink.** The ink under the U4 and U6 overwriting cannot be recovered from this scan.
- **Identity of "Pepouš".** Not established. This is a family-wide open question.
