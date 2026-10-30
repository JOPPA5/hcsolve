REVISE

# Review 1 — HCP 1403 (pc_hcp_84)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Round 1, state DONE1.

## Summary

The cipher type and key are right: Caesar with a shift of +1 on encipherment, decrypted by −1. They match the sister cards HCP1386…1407. Most body words are read correctly: I AM SO SORRY / I CAN'T WRITE / TO-NIGHT, and YOUR, GIRL in the closing.
**Two body words are mis-transcribed and the claimed plaintext is wrong in both
places.** Line 1 is `Nz. Pxo. El. Cpz.` (“My own El. Boy”), not `Nz. Pxo. Efbs.`
(“My own dear”). Line 4 is `mfuufs` (LETTER), not `npsf` (MORE). As a result the addressee's gender (“Boy”) and the
wording of the message both change. The decoder only replays the manual transcript, so it reproduces these errors faithfully. The corrected reading is:

> My own El. Boy, I am so sorry I can't write letter “to-night”. … Your own El. Girl.

That is a substantial change to the plaintext and the transcription, so per README step 5 a corrected solution
should come back as DONE2, not go straight to FINAL.

## What I verified and how

1. `python3 -I ciphers/hcp-1403/work/decode.py` runs, the source hashes pass, and the output matches the
   plaintext claimed in SOLUTION.md (MY OWN DEAR / I AM SO SORRY / I CAN'T WRITE / MORE /
   "TO-NIGHT" / YOUR / GIRL; 48 frozen letters).
2. Independent decoder: `review/work/indep_decode.py` (my own Caesar −1 code). It reproduces the solver's
   plaintext from the solver's transcript, and it decodes my own reading of the scan for comparison:
   `Nz. Pxo. El. Cpz.` → MY OWN DK. BOY; `mfuufs` → LETTER. It also confirms that
   1908-02-07 (portal date, postmark WIMBORNE FE 7 08) was a Friday, which fits the
   plain heading “C. H. Friday”.
3. Pixel check. I rotated `source/address.jpg` by 90° to make `review/work/rot.png` and enlarged crops 4–8×, some with
   autocontrast:
   `l1.png`, `l1b.png` (salutation), `l2.png`, `l2b.png`, `l3.png`, `l3b.png`, `l4.png`, `l4b.png`,
   `l4c.png`, `l4d.png` (line 4), `cl1.png`, `cl1a.png`, `cl1b.png`, `cl2.png` (closing).
4. Sister-card comparison: `ciphers/hcp-1386/work/crops/band3.png` shows `nvdi. gps. mfuufs.`
   (“much for letter”), written by the same hand.

## Findings

### 1. Salutation mis-transcribed: `Efbs` (DEAR) does not exist on the card. Severity: major
Crop `review/work/l1b.png` (6×) shows the following after `Pxo.`:
- a cursive capital **E** (ε-shaped, with the top flourish), followed by a dot;
- a separate tall **l** with a dot;
- a word **`Cpz`**: a large looped C, then p with a descender, then a z of the same form as the final z of `Tpssz`.

No `f`, `b` or `s` is present between E and the next word. The salutation is therefore
`Nz. Pxo. El. Cpz.` → “My own El. Boy”. This is the same formula as the opening of HCP1386
(`Nz. Pxo. E.[l?]. Cpz.`). It also matches the closing of this card, `El. Hjsm` (“El. Girl”), which the solver
itself reads. The solver's “Completion and handover” section discusses `El.` as this couple's
fixed abbreviation, yet the body table still freezes `Efbs`/DEAR. The plaintext, the translation (“Môj
drahý / moja drahá”) and the statement that gender is not established all need revising. The card has
“Boy” in the salutation and “Girl” in the closing.

### 2. Line 4 mis-transcribed: `npsf` (MORE) should be `mfuufs` (LETTER). Severity: major
Crops `l4b.png`, `l4c.png` and `l4d.png` show at least six letter units, not four:
1. a lead-in stroke plus humps (m);
2. a long descending f;
3. a run of minims (`uu`);
4. a second long looped f;
5. a small detached final **s**, followed by a period.

`npsf` would need a p bowl followed by s and then a final f. Instead the last sign is a
small s that comes *after* the looped f. The word matches, stroke for stroke, `mfuufs` in
HCP1386 band3 (“much for letter”) by the same writer, who also drops the article there.
Reading: “I can't write letter ‘to-night’.” The word count and the 40-letter body
total in SOLUTION.md and `transcription.json` change accordingly: body = 41 letters with El./Cpz.
handled as below.

### 3. Faint word after YOUR read as OWN with more confidence than the pixels support. Severity: minor
`cl1b.png` shows only a long faint diagonal, a short cross-stroke at the top and a few baseline
marks. A P-like form is plausible and OWN fits the formula “Your own El. Girl”. However, no `o` is
visible and the `x` is not clear. The completion section says it is “read, though faint” and the
reading text prints “YOUR OWN” without brackets. It should be presented as [OWN], a
contextual restoration, which is how the earlier solver section treated it. The decoder output still says
`[unclear]`, so SOLUTION.md's two sections contradict each other on this point.

### 4. The claim about HCP1386 overstates that card's reading. Severity: minor
SOLUTION.md says that HCP1386 reads “My own El. Boy” and “Your own El. Girl”. HCP1386's own
SOLUTION.md leaves both the `E.[l?].` group and `Cpz` explicitly **unresolved**. The
parallel is real and visible, but it should be cited as a visual parallel and not as an established
reading of HCP1386. This card's clearer `El. Cpz` could in turn be noted as supporting evidence
for HCP1386.

### 5. The first token of the closing line is not transcribed. Severity: minor
The closing line starts with a group shown in `cl1a.png` as `Nr.`/`Nz.`-like, followed by `N.`, then `&` and `L.`.
SOLUTION.md gives it as “…hr.”. If it is `Nz.` (MY), it parallels “To-Day. My.” on HCP1386. The solver should
transcribe it, even with uncertainty, and not leave it as an ellipsis. Keeping `N. & L.` and `El.` literal,
without expansion, is correct and properly disclosed.

### 6. The decoder and transcription need to follow the corrected reading. Severity: minor, but tied to findings 1 and 2
`work/transcription.json` freezes `Efbs` and `npsf`. The required changes:
- body line 1 becomes `Nz. Pxo. El. Cpz.`, and line 4 becomes `mfuufs.`;
- `El.` should be marked as a literal abbreviation (its shifted value is Dk), as in the closing;
- the “40 letters / 48 letters” counts need updating.

## Checks that passed

- The key covers every alphabetic body sign I examined. No sign needed a non-Caesar value apart from the
  literal abbreviations `El.`, `N. & L.`
- Lines 2, 3 and 5 match the pixels: `J. bn. tp. Tpssz.`, `J. dbo'u. xsjuf.`, `"up-ojhiu."`.
  The apostrophe in `dbo'u` is visible.
- `Zpvs` (YOUR) and `Hjsm` (GIRL) match the pixels.
- The context fits. The postmark reads WIMBORNE 10 PM FE 7 08 and the heading reads Friday, matching
  the portal date 1908-02-07. The addressee is Mr W. Abbott, Chudleigh, S. Devon, the same as on HCP1386. The language is
  ordinary Edwardian English.
- Source honesty: the portal status was Not solved, with no attached solution. The key was disclosed as a hypothesis supplied
  from sister cards. No published solution was used without saying so.

## Could not verify

- What `El.` and `N. & L.` stand for (a pet name or initials). Both are reported literally, which is correct.
- The faint word after YOUR, beyond the plausible restoration [OWN].
- The exact identity of the first sign of the closing line.
