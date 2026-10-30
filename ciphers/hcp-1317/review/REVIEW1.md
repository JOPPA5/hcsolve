REVISE

# Review 1 of HCP1317 (Claude Opus 5.5 as reviewer, 2026-10-30)

The reading stands: the key is right, the Hungarian is real, and the letter is Feri's to Jolánka. No word of the normalized text changes because of this review, apart from one comma (finding 4). Concrete fixes are needed in the ledger and in the disclosures: one sign is mistranscribed (finding 1), which also makes one claimed misspelling false, and two word-sense calls under the stamp are not disclosed (findings 2, 3).

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1317/work/decode.py` ran. All four SHA-256 checks passed and it reported 491 signs. A script check confirmed that all 33 printed rows appear in SOLUTION.md and that the normalized main text matches.
- **Independent decryption.** `review/work/my_reading.txt` is my own sign-by-sign reading of all 33 rows, using my own glyph names. `review/work/my_decode.py` has its own key and compares against the solver's ledger. This was not blind: I had already seen the ledger. Run it from `review/work/`. Result: 29 rows identical, 4 differ.
  - Row 16 is a real error (finding 1).
  - S2 and S5 are undisclosed word-sense calls (findings 2, 3).
  - Row 26 `zeri` is only my glyph class for the tilted cross. That sign is disclosed by the solver and is read as f from the signature; I agree.
- **Pixels.** Crops of `work/hires/*_adr.jpg` are in `review/work/` (`la0-5`, `lb0-5`, `bot1-3`, `stamp`, `z_*`). I read every row, not a sample. I counted bars on every a/e sign, because that is where a slip is hardest to see.
- **Restorations under the stamp.**
  - S1 t: the tear is wide enough for one sign, and i, s, e, n, v, e show around it.
  - S2 second e: under the tear; the m follows clearly.
  - S6 i: the dot is visible above the tear.
  - S7 f and e: f is hidden; two bar ends show at the tear edge.
  - All are disclosed as restorations, and each is what the visible signs require.
- **Blank paper after S3 `csokol`:** confirmed, so third person *csókol* is right.
- **Row 10:** the third sign is plainly long stroke plus right tick (h/p), not d. Row 10 stays unresolved, as the solver says.
- **Row 25, row 26:** the row runs along the bottom edge as described. The ü of *hű* has its dots beside the portal stamp. The curled r of row 26 is an F with a mid-bar.
- **Key.** It matches the HCP1216 table. Here gy is two separate signs, as the solver says (rows 2, 8, 21).
- **Repetition claims:** *hogy* ×4, *fényképet* ×2, *édesem* ×4, *soraim* ×2, *küldje* ×2, *már* ×3 and *volnék* ×2 all checked out in the literal text.
- **Language and context.**
  - The prose is period Hungarian with the family's formal address and closings.
  - *Hatvan* fits: HCP1216 places Vámosgyörk on the Budapest–Hatvan–Miskolc line near the addressee.
  - The word run-ons across rows are genuine.
  - The picture side and the plain address read as stated.
  - The English and Slovak follow the Hungarian.
  - I found no sign of a published solution being used: the portal status is Not solved and nothing is attached.

## Findings

1. **Row 16, last sign is a, not e (major).** See `review/work/z_r16end.png`: the sign after the six has exactly two bars, crossing the red line, with no third bar above or below. The ledger has `B E`, so the command prints `ujvarbe` and SOLUTION item 10 lists a misspelling *Újvárbe* → *Újvárba* that the writer did not make. Fix: change ledger row 16 to `... F B A`, the literal block, and item 10. The normalized *Újvárba* stays and is now literal. Every other a/e sign on the card agrees with the ledger on my bar count, apart from S2 (finding 2).

2. **S2, third sign shows two bars, read as e (minor).** See `review/work/z_s2_e.png`: two short bars are visible, and the neighbouring e has three clear ones. Literally this is `leadesem`. *vele édesem* is certainly the sense, but it is a word-sense call or a lost faint bar, and item 2 does not list it. Fix: disclose it.

3. **S5, last sign looks like a gamma, read as r (minor).** See `review/work/z_s_s5.png`: top bar and stem, no mid-bar visible, so literally t. *számtalanszor* is certainly the sense, and the ink is faint enough that a bar may be lost. Item 2 mentions only *la* of S5. Fix: disclose it.

4. **Normalized punctuation rows 19-20 (minor).** *…Hatvanba is menni már, az érzés i[s] jól esne* attaches the second *már* to *menni*. Item 10 then treats *már … már* as a repetition. The natural parse is *…Hatvanba is menni, már az érzés is jól esne*, "the very feeling would do me good", which is what the English already says with "the feeling alone". Fix: move the comma and reword item 10.

5. **Item 9, explanation of `ijjol` (minor).** The normalization *i[s] jól* is fine, but "phonetic spelling of the assimilation *is jól* > *ijjól*" is unsupported as stated. I know of no such ordinary assimilation of s + j across a word boundary, though I checked this from my own knowledge of Hungarian and not against a source. It is safer to call it a writing slip (s dropped, j doubled) and keep it as editorial.

6. **Row 10, one unadopted candidate worth recording (minor).** SOLUTION gives only `kihe/kipe`. NOTES says *de* and *neki* were tried separately. The combination *írni kéne [ne]ki, de azt várom* ("I ought to write to her, but I am waiting…") would fit the sentence about Ilonka very well. It needs two writer's errors: *ne* dropped at the row break, and the tick of d put on the wrong side. The sign itself is not d, so I do **not** propose adopting it. List it in item 1 as an unadopted hypothesis, with those two costs stated.

7. **Small writing accidents not recorded (minor).**
   - Row 12 has a fourth, short stroke after the three of *m* (`review/work/z_r11_12_end.png`). It is not in the ledger and not mentioned; it may be a comma-like mark, but it should be noted.
   - The k of row 11 *megkapjam* is a heavy blot, and the o of row 24 *volnék* is overwritten. Both are readable, and neither is noted.

8. **"No sign left without a value" counts restorations (minor).** The 491 signs include 5 that are not visible (the bracketed tokens), so 486 are seen. Say so in "Why it is correct".

9. **Item 12, cancellation (minor).** "The place not legible" is slightly too strong: a clear B and a following stroke show at the top of the right-hand cancellation, and an F at the bottom (`review/work/z_pm.png`). I do not claim a place name. State what is visible.

## What I could not verify

- The five restored signs are by nature unverifiable beyond their fit with the surrounding signs.
- The identity of Újvár, Ilonka and Feri, and the row 10 word.
- The hires originals against the portal: I relied on the recorded hashes and did not re-fetch.
- Hungarian usage was judged from my own knowledge, with no dictionary or corpus.
- Independence is limited: my reading was not blind, and solver and reviewer are the same model.
