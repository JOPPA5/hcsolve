REVISE

# Review 1 of hcp-1786 (reviewer: Claude Opus 5.5, 2026-10-30)

The key and nearly all of the reading stand. Two places in the plaintext are wrong, and both are the ones the solver flagged as unresolved. The key description also misses a rule that the card uses: a heavy pen stroke writes the vowel a. That rule is what settles both places.

Corrected opening and middle:

- "Přijměte prozatím tímto díky **za psaníčko**, nesmíš se, zlatíčko, zlobiti ..." (thanks **for the little letter**), not "zapsaníčko".
- "... pro řepové semeno. **Zaseto** již máme, ještě kousek řepy a bude hotovo." (**[It is] sown** already), not "To seto".

## What I verified and how

- `python3 -I ciphers/hcp-1786/work/decode.py`: hashes OK, 208 signs and marks, 53 words, 0 errors. The output matches the plaintext in SOLUTION.md. Hashes of the source and hires files also recomputed with `shasum`.
- Own transcription and mechanical decoder, `review/work/decode_review.py`. It has no free vowel insertion. Only written signs produce letters: consonant, `-` e, `.` i, `:` u, crossed = +o, heavy = +a. Result: 48 of 53 words match my reading after folding b/p, d/t, h/ch, i/y and accents. The five exceptions are:
  - zlat(í)čko: no í written, disclosed
  - dnes: literal "dines", NOT disclosed (finding 4)
  - Hoř(e): no e written, disclosed
  - (a)ž: no a written, not listed as an exception
  - otevírá: bare 0 for o, disclosed
- Sign-by-sign reading of all ten rows from `work/hires/pc_hcp_467_adr.JPG` at 4x (`review/work/crop.py`, r*.png), with 8-10x zooms of the contested signs (`crop2.py`, z_*.png). Sign values, ordering and word content agree with the solver except as listed below. The key covers every sign on the address side. There are no leftover signs apart from those in finding 4.
- Stroke-width map by morphological erosion (`review/work/heavy.py`, heavy_map.png).
- Word gaps: ink-column profile (`review/work/gaps.py`) and direct measurement on the zooms.
- Language and context: the corrected text is natural early 1900s Czech. Spring sowing of beet, Kutná Hora on the card and in the text, all consistent. "Chladna" as a plural noun (cold spells) is period usage and is rendered acceptably.
- Sister card hcp-1787, read-only: address and solver notes.

## Findings

1. **major: "zapsaníčko" is a misdivision; the text is "za psaníčko".** Evidence:
   - On line 2 the gap between x and 6 is 31 hires px; the gaps inside the group are 2-11 px (`gaps.py`, first group of line2; z_x65.png). It is a real word space, and the solver's own rule is that spaces are kept.
   - The x is heavy (x with a), so it is the word "za". The 5 is heavy too (sa), the same sign the writer uses in 6-5-0 "psal" on line 3. The solver read that heavy 5 as "blotted" in one place and did not comment on the other.
   - Grammar: "díky za psaníčko" is the idiom. "Díky" now has its object, and the unknown word disappears.
   Fix: split the word in T, in the plaintext, in the English ("my thanks for the little letter") and in the Slovak ("vďaku za listček/psaníčko"); drop uncertainty 2.

2. **major: "To seto" is one word, "Zaseto".** Evidence:
   - The first sign is the thickest stroke on the card (heavy_map.png, line 6; z_seto.png). The solver's 1/ is here a heavy x, the same pair as in "za".
   - The gaps X|5 and dash|X are equal (about 13 hires px each on z_seto.png), so no word space divides it. A full stop stands before it, after "semeno".
   - "Zaseto již máme" is ordinary Czech and ends the uncertainty in SOLUTION.md item 3. It also removes the rare "to seto" and the odd demonstrative.
   Caveat for the solver to state: x and crossed 1 are near-homographs on this card; both are X shapes of similar height (32-37 hires px on the instances I measured). The call of heavy x here rests on word sense plus weight, and "za" is the only reading that yields a word. Other X calls (to, do) likewise rest partly on sense and should be listed as such.
   Fix: change T, plaintext, translations ("We have it sown already"; "Zasiate už máme"), and drop "hay or sowing" from the reasons for belief.

3. **major: the key is misdescribed. The vowel a is written with a heavy stroke, not "normally not written (implicit)".** Heavy signs fall where a stands for 12 of the 13 a's that have no a sign of their own (the a in "ale" and the word "a" use the letter): prozatím (x), za (x), psaníčko (5), zlatíčko (0), psal (5), zaseto (x), máme (first 3), chladna (0 and 2), zlaté (0), otevírá (final 4), krásu (4). The plain signs in the same words stay plain (6 of psal, 1 of zlaté, 8 and 1 of chladna, second 3 of máme). The exception is "až", a bare x with a ring and no heavy stroke. The stroke map confirms the main cases; the 0 of chladna and the 4 of krásu are weaker there and rest partly on the eye. Crossing points also show as thick, and blots exist (the 6 of přijedete, crossed 2 of semeno, crossed 9 of kousek), so the signal is not clean. The independent solver of hcp-1787 reached the same rule ("heavy pen stroke on the sign = a, á"; its item 9 records the same imperfection). Fix: state the rule and its limits in the key, mark heavy signs in T, and stop calling them blots. The 6 of přijedete remains a real anomaly.

4. **minor: transcription T drops things that are on the card.**
   - "dnes" has a clear dot between 1 and 2 (z_dnes.png), so the literal is "dines". Either a slip or a stray, but it must be recorded. The claim "no leftover signs" is not quite true.
   - The stroke on 5 of "se" (line 8) and on the 6 of "přijedete" are disclosed in the text but absent from T.
   - "krásu" is a line-above insertion with a curled insertion mark, not in-line text. It is not disclosed.
   - An accent stands above the e of "pové".

5. **minor: uncertainty 6 is wrong on "nesmíš".** A curved mark stands above and to the right of the final 5 (z_nesmis2.png), so š is written, not omitted. T should show `5^`. This also confirms the word.

6. **minor: the address is under-read.** It says more than SOLUTION.md gives. I read: "Spani[lo]myslné(?) Slečně / Marušce Pařezové, / (u p. Pařeza Pekařská [ul.?] č.(?) 12) / Brno. / Morava." The solver's "(J.?) Pařez" is "p." (pan), and the top line with the honorific is omitted. Compare hcp-1787, "Spanilé Slečně ... Pařezové". SOLUTION.md should give the address and record the link to 1787 (same surname, same style of address).

7. **minor: the mix of "vy" and "ty" is undisclosed.** "Přijměte" and "přijedete" are plural or polite, while "nesmíš" and "ti" are singular. The readings are firm, so this is a feature of the text, perhaps addressing a household. Say so in the uncertainties and the report, and do not smooth it in translation.

8. **minor: `decode.py` is a checker, not a decoder.** The solver says so, but the README asks for a command that produces the plaintext. The plaintext is typed in, and its regex allows an optional a after every sign, which is why both errors in findings 1 and 2 passed with 0 errors. Fix: add a literal output like `review/work/decode_review.py`, with a stated exception list, and tighten the check once heavy signs are marked.

## Checked and upheld

- Sign values, the crossed-sign = +o rule, the ` - . : ` marks, carons, the double-stroke hyphen in ře=pové.
- "hotovo": the last sign has the loop and rising stem of v under a through-stroke (z_hotovo.png). Word sense is needed, as disclosed.
- "vždyť": the first sign sits between 0 and v in shape; sense decides. This is not stated in SOLUTION.md and should join the word-sense list.
- No written í in "zlatíčko" (z_zlat.png), no e in "Hoř", as disclosed.
- Bare 0 for initial o in "otevírá": on hcp-1787 the solver reports a separate initial o sign (σ). On this card I see an ordinary 0 shape. Keep this as a word-sense call.
- The picture-side pencil note is correctly reported as unread. I could confirm "Tebe" and about five lines only, even on the red channel with autocontrast (pencil.png, pencil_red.png). The strokes look like joined handwriting, not this cipher, but I cannot prove that. The solver must keep the "not read" statement in the report. The lower-right block might be a signature; a comparison with "Otta" on the picture side of hcp-1787 is worth one try, as a hypothesis only.

## Not verified

- The picture-side note (above).
- The postmark and year: the stamp and cancel are not legible enough. Only the 1907 imprint is firm, and it is a printing date.
- That the writer of hcp-1786 is the Otta of hcp-1787. The sign system is the same; the hand is similar but I did not test it.
- The absence of a published solution: I ran no search of my own and rely on the portal capture and the orchestrator's register check.
- Exact abbreviations in the address (ul., č.).

## Note on process

Findings 1 and 2 change the plaintext but not the method or the rest of the text. If the solver also rewrites T for heavy signs, a light second round would be reasonable; that is the solver's call under README step 5.
