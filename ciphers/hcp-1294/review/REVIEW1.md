REVISE

# HCP1294, review round 1 (Claude Opus 5.5, 2026-10-30)

Summary: the transcription and the 200 clear signs stand; I found no misread sign. The card still has an unread 9-sign word, which the solver reported honestly but did not label as partial, and a family spelling lead for that word was missed. Fixes are small and concrete.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1294/work/decode.py`: all four SHA-256 checks OK, 209 signs, none without a value. The output is identical to the literal block and the normalized text in SOLUTION.md.
2. **Independent decode.** `review/work/decode_review.py`: I transcribed all 15 rows myself as shape names from my own crops (`review/work/crop.py`, `crop2.py`, 2x of the 3445 px hires side, output in `review/work/crops/`) and took key values from the table in `ciphers/hcp-1216/SOLUTION.md`. Result: 209 signs. A diff against the solver's output shows 4 places only, all deliberate: my script keeps the shape value `h` for the two p's (rows 3, 11) and `d` for the two n* (rows 7, 9). These are the homographs the solver disclosed as word-sense calls. There is no other difference.
3. **Sign by sign against pixels.** All rows were read at enlargement, including row 8 (extra 4x crop `r8signs.png`), the row 12 and 14 blots, and the two d-shaped n's. Each named sign is visible as claimed. Row 12 `n a` has two strokes, not three; `najd` is literal and *majd* is a correction, correctly disclosed. Row 7 `nnyi` has four strokes.
4. **Key coverage.** Every sign has a family value, nothing is unused or invented, and the sign classes are consistent across the card. The tailed z vs plain u and the d/p tick side behave as the solver says. Key values were not derived from this card alone, and the solver says so.
5. **Language and sense.** Everything outside row 8 is idiomatic 1912 Hungarian with this writer's known slips. The translations (English, Slovak) are faithful. *Becses sorait köszönettel megkaptam* is in HCP1212 (line 65), *okvetlen lemegyek* in HCP1301 (line 35), as claimed.
6. **Plain parts.** Under the stamp I read `csokolja / szamtala[n] / szor hű[n] / kedvese / Feri`, in agreement. Address side *Szépreményű Tóth Jolánka úr leánynak, Jász Árokszállás* agrees. Picture side is a printed verse and is not ciphertext.
7. **Sources.** No use of a published solution is visible. Portal status and the absence of attachments are as recorded in `source/metadata.md`; I did not re-render the portal.

## Findings

1. **major: the card is partial but not labelled so.** The status line says every sign has a value and that 200 of 209 are clear, but one clause cannot be translated. Its role in the sentence is unknown. README step 3 requires a partial solution to be labelled partial, and step 7 gives a partial solution no register entry. Fix: say PARTIAL in the status line (and in the report) unless the word is resolved, and do not write a register entry in that case. Also, "turns all 15 rows into Hungarian" under *Why it is correct* overstates row 8; that line needs the exception.

2. **major: a family spelling lead for row 8 was missed.** NOTES.md says a grep of the family solutions had no hit, and SOLUTION.md says no word was found. But this writer spells *össze* with one sz: `ciphers/hcp-1288/SOLUTION.md` row 22 has literal `ö s z e h ö ? z e h o z`, normalized *összehoz*. Item 10 there also records dots absent on o-signs. So row 8 `oszeho…` most probably begins *ösze-* = *össze-* with the ö dots omitted, or marked by the unexplained lead-in stroke on the first loop. The solver tried o/ö variants but does not report the prefix *össze-*. Fix: test *össze-* + `holad/polad/holan/polan` as a compound, including this writer's usual dropped or repeated letters. I have no reading to offer: *összehoz* itself does not fit, because the sign after o is a clear wave l, not z. Whatever comes of it, record the prefix as a lead.

3. **minor: the claimed function of the word is unsupported.** Uncertainty 1 calls it "a condition, day or place for the trip", and the normalization puts it at the head of the *okvetlen elmegyek* clause. *Okvetlen elmegyek* is a complete sentence opening on its own. An *össze-* verb could as well close the preceding remark about too much work ("why take on so much work? …"). Fix: state that the attachment is unknown in both directions.

4. **minor: the dots under k are misdescribed.** Uncertainty 2 says the dot under the final k of row 8 "matches no sign in row 9" and may be a full stop or stray; NOTES.md says the dots under k in rows 1, 5, 9 belong to the row below. On my crops, 7 of 11 k-signs carry a dot just under them: row 1 second k, rows 2, 3, 5, 6, row 8 last k, row 9. Rows 2, 3 and 6 have no i or ö beneath them. Rows 5 and 9 show two dots, one for the k and a separate i-dot for the row below (`r05_2`, `r09_2`, `r10_2`). So the row 8 dot is this writer's habit with k, not punctuation evidence. No reading changes; fix the text.

5. **minor: two damaged signs are undisclosed.** Row 10 `a` of *bár* has its lower bar swollen into a blot, and row 13 `ö` of *bővebben* is overwritten or thickened. Both still read as claimed, but the solver lists blots only in rows 12 and 14.

6. **minor: ledger housekeeping.** The ledger header documents tokens `h` and `d*`, which do not occur in the rows (it uses H, P and plain d). This is harmless, but the header should match the rows.

## What I could not verify

- The word `oszeholad`: no reading found. I have no Hungarian dictionary here, and a near-match search covered only family SOLUTION.md vocabulary.
- The date 1912-03-26: neither postmark's date is legible to me. It rests on the portal's filename and metadata.
- The h/p and d/n choices rest on word sense, as disclosed, and cannot be confirmed from shape.
- Acute accents cannot be judged at this resolution, so they are editorial, as disclosed.
- Family cards 1285-1319 were not checked for a passage that explains the row 8 word beyond the grep above.
