REVISE

# Review 1 — HCP 1535 / pc_hcp_216 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-28. Short version: **the key and the reading are right, but one literal letter is not.** I re-read all 16 body rows and the 3 rotated margin rows sign by sign, and I agree with 436 of the solver's 437 signs. The disputed sign is in B04: the word the solver gives as `KDYZ` is written with the **I** sign. The literal text is therefore `KDIZ` (finding 1). The solver makes a point of keeping this writer's I/Y slips literally (JAHODI on this card, VZDIT on HCP 1533). This is a case of the same kind that the transcription normalises silently. Everything else stands. The fixes are local, and I see no need for another full review round.

## What I verified and how

1. **The documented command.** `SOLUTION.md` gives `/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1535/work/decode.py`. With `-I` it exits 0 and prints the 19 literal rows exactly as in `SOLUTION.md`, followed by `19 active rows; 437 active indexed units … 442 base letters; 5 CH units; 22 observed assigned classes. Tokenwise round-trip OK.` The same script also runs unchanged under the system `python3 -I` (exit 0). The script only reads files (`csv`, `hashlib`, `json`; no writes).
2. **Independent decoder.** `review/work/decode_review.py` is my own decoder and does not use solver code. I wrote `key_review.json` from the family table, with `ř` for the CH glyph (the solver uses the label `H`) and `v`→F. It decodes the solver's cipher rows (`solver_cipher.txt`, with `H`→`ř`) to output byte-identical to the solver's (`diff` empty). The 437 units contain no unknown symbols. The key is a bijection. The F class is not used on this card.
3. **Independent reading of the scan.** I made the main frame with `ffmpeg transpose=2` (90° CCW, `ccw_review.png`) and the margin frame with a 180° rotation (`rot180_review.png`). Crops: rows as 5× half-row strips (`m1_a … m7_b.png`), the bottom rows (`bot_*.png`, `b16_full.png`), the margin (`mg_a.png`, `mg_b.png`), and 8–12× details (`z_*.png`, `cmp_*.png`). My reading is in `review/work/reading_review.txt`, and its decoding is in `reading_review_decoded.txt`. The only difference from the solver is in B04: the sign `1`→`4` and `.`→`!`.
   - Confirmed: ANUNKA `6m2mg6` (B02); the single CH in TROCHU (B08); the five CH glyphs in all; CTVRT ROKU `sdfhd h3g2` (`z_roku.png`); MUSEL `n2c58` (`z_musel.png`); BEZ underlined (B15); ABY `6p1`, where the 3rd sign is the footed `1`, not `4` (`cmp_aby.png`); B15 JAHODY `76r3t1` against M01 JAHODI `76r3t4`. The final M01 sign is faint (`z_jahodi.png`), but its shape fits `4` better than `1`, and I accept the solver's literal reading.
   - **No missed text**, apart from what is listed in findings 3–4. The address side (`addr_small.png`) is ordinary cursive with the PRAHA and ŽIROVNICE ✱ SEROWITZ postmarks (arrival day apparently `14`). The date `13./X.1903` is in the margin frame.
4. **Language and context.** The text is fluent Czech of 1903 with period forms (*čekati*, *trvati*, *neb dále*, *míti*, *odvážiti*, *žádati*). It continues the story of HCP 1533 (28 Oct) and 1532 (2 Nov): Anunka promised to come to Prague in October, and the writer, PEPOUSE, grumbles about strawberries sent "bez významu" ("without meaning"). 13 October 1903 was a **Tuesday**. The address reads "Velectěná Slečna / slečna Anna Tichá / učitelka v Žirovnici / u Počátek". The postmarks agree with the date.
5. **Disclosure.** The transferred key, the Egorov / Cipher-Atelier public partial study, the pc199 reference image and the register check are all disclosed. I found no sign that a target plaintext was used.

## Findings

1. **major — B04 `KDYZ` is written `KDIZ`.** The 3rd sign is the I sign `4`, not the Y sign `1`. Evidence: `review/work/cmp_kdyz_b04_m01_dik_prahy.png`. The panels, left to right, are the B04 sign, the M01 KDYZ sign, the B01 DIK `4`, and the B04 PRAHY `1`. Also `z_b04start.png` and `cmp_b04.png`. The B04 sign has two up-strokes, a curved left arm and a right arm, standing on a foot. That is the `4`/I form, as in DIK. The M01 KDYZ and PRAHY signs are the single-stem, flagged `1`/Y form. So the writer spelt the same word KDIZ in B04 and KDYZ in M01, just as he wrote JAHODY in B15 and JAHODI in M01, and VZDIT on HCP 1533. The meaning does not change, but the literal transcription the solver claims ("retains source I/Y") is wrong here. **Required:** B04 `gt1q` → `gt4q` (literal KDIZ). Disclose it next to JAHODI as a writer's I/Y slip, normalise it to *když* only in the editorial Czech, and update the I/Y class counts and hashes. I rate this "major" only because it is exactly the class of literal fidelity the solution says it guarantees. If the solver keeps `1` after its own comparison, it must at least list the sign as uncertain.
2. **minor — B04 punctuation after PRAHY is `!`, not `.`.** `z_b04start.png` shows a vertical stroke above the dot. This is punctuation only, but the literal row should read `DO PRAHY! KDIZ …`.
3. **minor — the cancelled B09 span is partly legible.** `z_cancel.png`: after PRACI there are at least three sign positions. The first is a solid blot. The second is clearly an `f`-form (V), with its upper loop and descender above and below the overink. The third ends in a looped ascender (`h` or `8`?). The solver's "original characters … not recoverable" is right for the word as a whole, but the note should record what can be seen (≥3 signs, the 2nd being `f`/V). The exclusion from the active count is correct.
4. **minor — the "curl" after M03 is a distinct `u`-like sign.** `z_m03end.png`: after the two dots `..` and slightly above the line there is a clear upright `u`-shaped mark in the same ink. It matches no key shape (the `2`/U of this hand is different). It is probably not cipher, but "small curl" undersells it. The solver should describe it, and say that it is excluded and that its meaning is unknown.
5. **minor — the reproduction command is tied to one machine.** The given interpreter path is under `/Users/tomaspavuk/.cache/codex-runtimes/…`. The script runs unchanged under any Python 3, so `SOLUTION.md` should use `python3 ciphers/hcp-1535/work/decode.py`, like the sister cards.

## Required for closing

- B04: `t3 bh6r1. gt1q` → `t3 bh6r1! gt4q` (literal `DO PRAHY! KDIZ`), with the I/Y slip disclosed and normalised editorially. Regenerate the index and hashes.
- Add the observations on the cancelled span and the M03 sign, and make the command portable.
- If these are done exactly, the solution can go to FINAL without another review round.

## What I could not verify

- The cancelled B09 word, and whether the margin block attaches after B13's arrow or after B16. I agree with the solver that the order is editorial.
- The faint last sign of M01 JAHODI: I accept `4`, but at 1024 px `1` cannot be excluded completely.
- Accents and diacritic marks (treated as editorial), and the full postmark dates.
- Whether pc_hcp_216 has been deciphered anywhere outside the sources the solver checked.
