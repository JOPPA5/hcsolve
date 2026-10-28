REVISE

# Review 1 — HCP 905 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-28. In short, **the key, the decipherment and the message are correct.** I re-read all 14 rows sign by sign from `source/picture.jpg` and get the same German text, with the same 347 positions. My reading differs from the solver's frozen transcription in **exactly one sign**. Position 156, in `GEGENGENOMMENE`, is an *undotted* ⊐, so it is literally D. The solver silently normalized it to N (finding 1). It is the same kind of slip as the undotted ⊔ in `POSTVERHÄBTNISSE`, which the solver did disclose. Because the record must be corrected, the verdict is REVISE, not ACCEPT. The meaning is unaffected.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-905/work/decode.py` is read-only (I checked the source: it only reads and asserts). It verifies both scan hashes. It prints the 14 rows and reports `347 positions: 346 active glyphs + 1 cancelled field`. The diplomatic layout it prints is identical to the "Literal text" block in `SOLUTION.md`. I did not run `make-aids.py` or `make-transcript.py`, because they write files into `work/`.
2. **Independent decoder.** I wrote `review/work/my_decode.py`. It holds my own reading in my own notation: grid cells 1–9 named by drawn strokes, `.` for a dot, `|` `v` `<` `^` for the X-group, `"` for umlaut strokes, `X` for the cancelled field. It decodes with the standard German omitted-J Pigpen. The only solver file it reads is `transcript.json`, and only for the `--diff` comparison. Output of `python3 -I review/work/my_decode.py --diff`:
   ```
   01: IA VERD NICHT EINMAL
   02: DIR KANN ICH'S MEHR RECHT
   03: MACHEN WIE DEINE LETZTE
   04: IM ÜBRIGEN IA WIE AUCH DIE
   05: ANDERN ZWEI KÜNSTLERKARTEN
   06: SEHR HÜBSCHE [X] UND DAHER VON
   07: MIR MIT HERZLICHEM DANK ENT
   08: GEGENGEDOMMENE IN ETWAS MERK
   09: WÜRDIGEM TONE ABGEFASSTE
   10: SONNENKARTE ICH BIN FROH DASS ICH
   11: SIE SELBST VOM POSTBOTEN ENTGEGEN
   12: NAHM AUHSERDEM MUHS ICH IEDE VER
   13: ANTWORTUNG FÜR KÜDINGHOVENER FILIAL
   14: POSTVERHÄBTNISSE ABLEHNEN SCHLUHS U KUHS
   positions (incl. cancelled field) = 347
   Differences vs solver transcript.json notations (J folded to I):
     row 8: solver 'GEGENGENOMMENE' -> reviewer 'GEGENGEDOMMENE'
   ```
   One key covers every sign of the card. No sign needs two values. The dotted ┐ (Q) and the dotted ∨ are not used.
3. **Reading the scan.** All my crops are in `review/work/`:
   - `z-L01-0…z-L14-2.png`: each row in thirds at 4×.
   - `z-e-*.png`: 7–12× details of every sign in doubt.
   - `ascii.sh`: prints pixel darkness (`#` < 100 gray). I used it wherever ink and the grey "HCPortal" watermark overlap. That stamp is printed over rows 8–13 and imitates strokes and dots.

   I specifically re-checked the solver's own contested points:
   - **KANN.** The 3rd sign has an interior dot.
   - **JEDE / VER.** There is no dot in the D (275) or the E (278). The grey shapes there are watermark letters (`z-e-jede.png`).
   - **ABGEFASSTE.** Both S corners have dark interior ink. The first is a clear dot. The second is a short dark stroke under the watermark "A" (ASCII at x=855, y=410).
   - **FILIAL.** The 4th sign is ┌ with a short arm, so I.
   - **ENTGEGEN, 7th sign.** A full box under the watermark "F", so E (ASCII at x=915, y=490).
   - **POSTVERHÄBTNISSE.** The ⊔ is really undotted (`z-e-verhae.png`).
   - **AUHSERDEM / MUHS / SCHLUHS / KUHS.** Undotted ⊓ followed by dotted ┌ in all four (`z-e-auhs.png`, `z-e-muhs.png`, `z-e-kuhs.png`).

   I agree with all of these.
4. **Search for missed cipher text.** The picture side has only the printed caption "Der hol' die Ansichtskarten!" and the 14 cipher rows. The four dots of `VERD....!` and the `=` line-continuation marks are punctuation. On the address side:
   - Printed "Postkarte".
   - Address: "Fräulein Marie Kühnast, Berlin S. 59, Kottbuser Damm 72".
   - Bonn postmark on a 5-Pfennig Reichspost stamp.
   - Berlin arrival mark: "Bestellt vom Postamte 59, 22/12. 99, 8¾–10 V".
   - The small pencil note at the top (`e-pencil.png`) is a dealer/collector mark in Latin letters, not Pigpen.

   I found no uncovered cipher group.
5. **Context.**
   - 21 December 1899 was a Thursday. The card was delivered by Berlin post office 59 on Friday morning, 22 December. Post office 59 matches "Berlin S 59" in the address.
   - **Küdinghoven** is a village beside Beuel, on the right bank of the Rhine opposite Bonn. A complaint about "Küdinghovener Filialpostverhältnisse" therefore fits a card posted in Bonn exactly. The solver says no external claim is needed, which is fine. This agreement is still independent support and worth a line in the report.
   - The HS/SS pattern is noteworthy. In the 1899 (pre-1901) spelling, all six words concerned were written with ß: *außerdem, muß, Schluß, Kuß, daß, abgefaßte*. The writer renders four of them as HS and two as SS. That is a stronger statement than "typical ß contexts", and it supports the editorial ss/ß rendering.
6. **Prior solutions.** The portal shows "Not solved" with no attached transcription or solution. The key transfer from HCP 995/1016 is openly disclosed. The Schrödel 2021 paper is credited as context only. I found no sign of an undisclosed published reading. I did not repeat the literature check myself.

## Findings

1. **major (transcription; silent normalization) / minor (meaning): position 156 is an undotted ⊐, so `GEGENGENOMMENE` is literally `GEGENGEDOMMENE`.**
   - Evidence: `review/work/z-e-gegen.png`, and the ASCII dump `./ascii.sh 462 366 36 36` against the dotted N at position 153 (`./ascii.sh 382 366 36 36`).
   - The control N has a dark interior dot at rows 10–11.
   - The cell at position 156 is completely empty. Its only heavy ink is the pen-down blob at the left end of the bottom stroke, outside the cell.
   - Fix: record `E` (not `E.`) at 156 in `transcript.json` and in the word notation, `GEGENGE[D]OMMENE` or literal `GEGENGEDOMMENE`.
   - Add it to "Source anomalies and limits" next to POSTVERHÄBTNISSE. The writer dropped a dot twice, and both should be treated the same way.
   - The editorial reading *entgegengenommene* stays.

2. **minor: the cancelled field (position 114) can be described a little more closely.** In `z-e-cancelled.png`, two heavy vertical strokes cross out a sign. Its top, right and bottom strokes still show to the right, so it is of the ⊐/□ family. No dot is visible. *HÜBSCHEN* (an N) or a repeated E are both plausible. I agree it should stay unassigned. One sentence on the visible strokes would help a reader.

3. **minor: context to add to the report.**
   - (a) Küdinghoven lies beside Bonn, which matches the Bonn postmark.
   - (b) The arrival mark of Berlin Postamt 59 is dated 22.12.99, and 59 matches the address.
   - (c) The street number, Kottbuser Damm **72**, is legible. `SOLUTION.md` says it is "outside this cipher transcription", but it can simply be quoted.
   - (d) Under the 1899 spelling, the HS/SS observation covers all six ß-words (verification 5).

4. **minor: the first sentence.** The English translation inserts "[with]" and "[but]" to bridge the incomplete construction. That is honest. However, the editorial German keeps the long apposition as one sentence. It could note that *wie deine letzte … Sonnenkarte* most likely depends on an omitted *z. B.* or reads as an elliptical comparison, so that a reader does not assume a missing cipher line. The cipher rows are complete: row 3 ends at `LETZTE, -` and row 4 continues directly.

## Required for closing

- `transcript.json` and the decoder: position 156 `E.` → `E`, and the GEGENGEDOMMENE notation. The decoder's built-in assertion compares against the notation, so both must change together.
- Literal text and anomaly list: add GEGENGEDOMMENE as a dropped-dot slip.
- Report: the context points in finding 3.

These are corrections of the record, not of the solution. Once they are made, I see no need for another review round.

## What I could not verify

- The day in the Bonn postmark. It is under the stamp and illegible at this resolution. The portal date 1899-12-21 is consistent with the arrival mark of 22.12.99.
- The letter under the cancellation (finding 2).
- Whether a decipherment of this specific card has been published elsewhere. I relied on the solver's and root's bounded checks.
- Identity of the sender. "Mariechen" in the portal name suggests a series to the same addressee, but the card gives no signature.

## Process note

I did not run any solver script that writes files. I only ran `work/decode.py`, which is read-only. Everything I produced is in `review/work/`. `dotscan.py` (which needs a grayscale dump made with `ffmpeg -i source/picture.jpg -vf format=gray -f rawvideo gray.raw`; I deleted that dump afterwards) was an attempted automatic dot screen. It turned out unusable, because the solver's glyph centres are only approximate, as it says itself. I did not rely on it.
