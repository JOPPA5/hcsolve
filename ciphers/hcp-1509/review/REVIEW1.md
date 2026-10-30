ACCEPT

# Review 1 – hcp-1509 / pc_hcp_190 (German love postcard, Lieblos, 5.4.1912)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. My job was to try to refute the solution.
Solver for this round: Claude Opus 5.5. The earlier capture of the source files was by an OpenAI GPT solver. The credits section in SOLUTION.md states this correctly.

## What I verified and how

1. **The solver's command.** I ran `python3 -I ciphers/hcp-1509/work/decode.py` from the repo root.
   - All three source hashes print OK.
   - The output matches the plaintext in SOLUTION.md line by line.
   - It reports 359 cipher signs and no unknown tokens.
2. **An independent decoder.** I wrote `review/work/decode_rev.py`.
   - It has its own key table, typed from my own reading of the scan rather than loaded from `work/key.json`, and its own parser.
   - It produces the same word sequence, the same 359 signs, and no unknown tokens.
   - Letter frequencies: E 74, I 39, N 27, R 24, H 20, D 20, T 18, A 18, S 16, M 15, B 15 … These are a normal German profile.
   - The key is one fixed table of 23 signs, used for the whole text, with no homophones or exceptions.
3. **The transcription against the scan.**
   - I made my own crops of `source/address-large.jpg`: the message area rotated 90° counter-clockwise (`review/work/rot.png`) and per-line strips at 4–7× (`review/work/L*.png`, `review/work/z_*.png`).
   - I compared the lines with the transcription sign by sign. Checked: lines 1–10, the farewell, the three lines after it, the line "BALD ANTWORTE" and the signature HEINRICH.
   - Every token I could see agrees with `work/transcription.txt`, word dividers `x` included.
   - Points I checked at 5–7×:
     - **GELIETE (line 1)**, at `z_geliete.png`: the signs are `9 8 T · 8 1 8`. There is no 6 (B) sign. The closing formula `9 8 T · 8 6 1 8` does contain the 6. So the missing B is real, and the solver's literal reading is right.
     - **MIR (line 4)**, at `z_mir.png`: the R is a short, closed-loop 9-like sign with no long descender. G in GERNE in the same line (`z_gerne.png`) has a long descender. Reading it as R is the only reading that makes sense, and the solver disclosed it.
     - **DENNE·WIE**, at `z_dennewie.png`: the signs are `h 8 11 11 8 111 · 8` with no divider. The extra 8 is on the card.
     - **VERLIEBTE·IN, MITE·WELCHEM, ZUGEDU**: the transcription matches the scan, and these points are disclosed.
     - **V (`11=`) and O (`11_`)**: line 6 shows a double underline under the 11 in VERLIEBT, and other places show single underlines. This is consistent.
     - **Umlauts**: GRÖSER and GRÜSE have their two dots, visible in `z_line11a.png`.
     - **ALS**, at `z_als.png`: the stray ,, mark under the L is present. Ignoring it is reasonable, and the solver disclosed it.
     - **Plain-script parts**: "Lieblos, 5. 4. 12." and the Kurrent farewell "Auf Wiedersehn" (`z_farewell.png`) read as the solver states.
4. **Language and context.**
   - The plaintext is fluent colloquial German of the period, with typical love-card formulas such as "dein dir auf ewig treu bleibender".
   - 5 April 1912 was Good Friday, since Easter Sunday fell on 7 April 1912. So "2. Feiertag" is Easter Monday, 8 April.
   - Lieblos (Gründau) lies on the Gelnhausen–Gießen line. The Bahnpost cancel "…SSEN–GEL[NHAUSEN] … ZUG 512" is visible on the scan.
   - On the address side I read Elisabeth … in Wächtersbach, im Schloß, Kreis Gelnhausen. This fits the request "schreibe mir mit welchem Zuge du kommst".
   - The addressee's first name, Elisabeth, matches the name in the cipher text twice, which is an independent check.
5. **Sources.** The portal status is "Not solved" and no solution was attached. I found no sign that a published decipherment was used.

## Findings

1. **minor – the "no umlaut" claim for KUSSE cannot be checked.**
   - SOLUTION.md calls KUSSE (Küsse) a writer's spelling with "no umlaut on this U".
   - In `z_kusse2.png`, the plain-script word "Wiedersehn" runs directly above the `3 :` signs. Any two dots over the colon would merge with those Kurrent strokes.
   - The absence of the umlaut is therefore undecidable, not established. Please phrase it as "umlaut not visible (the space above is occupied by 'Wiedersehn')". The meaning is unaffected.
2. **minor – the final T of BESTIMMT is joined to the M at the card edge.**
   - In `z_bestimmt.png`, the last `1` of `N N 1` is written onto the second N, right at the trimmed edge of the card.
   - The reading is supported by the word, but it is worth one line under Uncertainties.
3. **minor – the translation of "zu verliebt".**
   - "denn ich bin zu verliebt in dich" literally means "I am too (much) in love with you".
   - The English "I am so much in love" and the Slovak "príliš zaľúbený" differ slightly. The Slovak is the literal one.
   - Optional: make the English literal too, or note it as idiomatic.
4. **minor – presentation of GELIETE and "deinen Lieben".**
   - In the normalised German, show the omitted letter as restored, e.g. "gelie[b]te".
   - Mark the missing noun the same way it is marked in the translation.
   - This is already done in substance. Just keep it explicit in the PDF report.

There are no blocker or major findings. The key, the transcription and the reading all stand.

## What I could not verify

- **The full address reading.** The surname ("Herb…"?) and the exact place lines are only partly legible at this resolution. The solver does not claim them, and they are not needed for the decipherment.
- **The whole card at higher resolution.** The scan is only 1024 px wide. The 1/7 distinction (T vs R) was judged from context plus shape at 5–7×. In every case I checked, the shape agreed with the word, but a higher-resolution scan would make that firmer.
- **The writer's identity.** I could not identify "Heinrich" or the addressee historically.
