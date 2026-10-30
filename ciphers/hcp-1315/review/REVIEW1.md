REVISE

# Review 1 of HCP1315 (Claude Opus 5.5, reviewer, 2026-10-30)

The reading stands: Hungarian monoalphabetic Jolánka-family cipher, Feri to Jolánka Tóth, with a coherent text. One concrete transcription error must be fixed: a sign that is not on the card (finding 1). The rest is disclosure and accuracy of the evidence.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1315/work/decode_opus.py` ran; four SHA-256 checks OK; 393 signs. Output matches the Literal and Normalized sections of SOLUTION.md exactly.
- **Independent transcription and decode.** I read the card from my own crops of the hi-res address side (`review/work/crop_*.py`, output in `review/work/crops/`) and wrote all rows as sign-class codes in `review/work/my_signs.txt`, without the letter ledger as the input. `review/work/verify.py` decodes them with the key and diffs against `work/ledger-opus.txt`. It is not blind: I had read SOLUTION.md first. Result: 392 signs against 393, **one difference, row 14**. (My file does not separate h from p; both are class hP.)
- **Key coverage.** Every ledger token maps to a key class; no unassigned sign on the main rows. Key matches the HCP1212/1216 family tables, including digraphs written as two signs (HCP1212 says the same; HCP1216 lists a joined gy).
- **Pixels.** Rows 1 to 21 read in full at 1.6x, weak places at 2x to 5x: row 1 *ka* smear, row 2 *l* stain, row 2 joined n, row 7 first sign, *½ 9*, row 12 second g, rows 13 and 14, row 16 end, row 19 blot, row 20 end, row 21 *si hü*, all stamp-corner rows (natural colour and red-channel stretch).
- **Language and context.** Period Hungarian, with family formulas. HCP1301 has the very similar sequence "Remélem, jól. Ami engem illet" (the solver did not cite it). *Ezzel bezárom soraim* and *szerető kedvese Feri* occur in the family, which supports the row 20 and s6 to s8 readings. Picture side verified: "A szerelem hőmérője". Address reads Tóth Jolánka, Budapest, István út 5, plus further figures. Postmark shows BUD… and 914. Translations check out against the normalized text, apart from finding 1.
- **Sources.** No published solution; portal attaches none; solver says so. No sign of undisclosed use.

## Findings

1. **major: phantom sign in row 14; the ledger has an *a* that is not on the card.** Ledger: `E Z T A V A S A R`, literal `magavaleztavasar`, normalized *ezt a vasárnapot*. On `review/work/crops/r14b.png` the row runs wave, three bars, crossed z, gamma t, **then immediately the chevron v**, two bars, bowl s, two bars, F. Nothing lies between t and v, and there is no room for a sign. The article looks supplied from grammar and entered as if read. Fix: delete the token in `work/ledger-opus.txt` (row 14 becomes `magavaleztvasar`, 392 signs) and correct SOLUTION.md's literal block and `work/normalized-opus.txt` to *ezt vasárnapot* (or *ezt [a] vasárnapot*, marked as supplied). The English and Slovak do not change. This row is not listed under Uncertainties, and it was claimed as read.

2. **minor: the d / h-p uncertainty is misdescribed.** Item 1 says h, p and d are near-homographs and that d-words are chosen by word sense. On this card they differ by stroke order: d is a short stroke then a long one, h/p a long stroke then a short one. This held at every place I checked (d in rows 1, 2, 4, 9, 10, 16, 17, 21; h/p in rows 3, 5, 6, 8, 12, 13, 15, 21). Only h against p rests on sense. Restate item 1 and make the key table say which stroke comes first. Over-disclosure is harmless to the reading, but the key description is too weak.

3. **minor: unflagged weak signs.** None of these has a `?` or an entry in the Uncertainties:
   - Row 1 *k a* of *Jolánkám*: both lie in a wet smear (`r1k.png`). A brown S-arc and two bars can still be seen.
   - Row 2 *l* of *egyetlen*: in a stain (`r2l.png`), only a blurred wave.
   - s2 first sign (*l* of *vele*): a green blot, read from sense.
   - s4 last sign (*r* of *-szor*): a spread blot, F-like only in outline.
   - s5 *k, o, l*: laid over the triangle's dense print.
   Mark them `?` or list them.

4. **minor: stamp corner, s8.** The readings s3 to s7 are supported by what is visible, and the three `[s]` are properly disclosed as restorations (in s3 and s6 only traces on the tear; in s4 only a blob and diagonal at the triangle's edge). In s8, `n` before the blot is real ink, two clear strokes, but "no explanation except a slip" is not the only option. The blot has a separate left diagonal at about the right spacing, so n + f might be m + f, giving *kedvesem*, which fits less well after *csókol*. Mention it as an alternative. Normalization silently removes the n: mark the deletion (for example ⟨n⟩), since brackets elsewhere only show additions. Also s6's last sign: a short arc just below it at the height of a third bar (`c67.png`) may make it e rather than `{a|e}`; note it if you agree.

5. **minor: wrong evidence counts and citation in "Why it is correct".** *hogy* occurs **4** times in the ledger, not 5. *édes* occurs **3** times, not 2 (rows 1, 2, s2). *kedvében találja soraim* is credited to HCP1212, but `hcp-1212/SOLUTION.md` does not contain *találja*; a similar phrase, *legjobb egésségben találja soraim*, is in HCP1213. I also did not find *imádja Feri* in HCP1212 or HCP1216. Correct the numbers and cite the cards that really carry the formulas; HCP1301 is the strongest parallel.

6. **minor: normalization not listed consistently.**
   - Row 5 literal *mulatot* is normalized *mulatott* with no bracket and is absent from item 11.
   - Row 4/5 *soraim* (for *soraimat*) is not bracketed, unlike row 20.
   - *tőlthetem* (double mark over o) becomes *tölthetem*, and *ido* becomes *idő*; neither is noted.

7. **minor: key table omits two card-specific forms.** The `TT` token (*attól*, row 11, gamma joined to gamma) is defined only in the ledger. Row 2's n is written with the two strokes joined by a top bar (`r2n.png`), not noted anywhere. Add both to the key section.

## Points checked and accepted

- *½ 9*: fraction and digit plainly written, in clear (`r7a.png`); -kor follows.
- Row 12 second g: the same shape as the g in *agon-*, not a d. The reading as a slip for *gondoktól* is honestly marked.
- Row 7 `j?` and `g?`, row 19 `a?`: overinked as described; word sense decides, as disclosed.
- Row 17 last sign `{a|e}`: as disclosed.
- Row 20/21 *soraim|ma-radok*: three strokes, then three strokes with a bar, then two bars, as claimed.
- Row 21 *si hü*: s, i, h, ü are all there and no *r-i-g* is written. The expansion *sí[rig]* is an editor's conjecture from the family formula, and it is disclosed as such (item 7).

## What I could not verify

- The three `[s]` signs and s6's final sign cannot be proved from pixels; they follow from the words.
- h against p on single signs is word sense only.
- Accents á, é, í, ó are not reliably visible.
- Date: only "914" on the postmark; no full date read. The portal's file name says Jász-Árokszállás, while this card is addressed to Budapest; the card does not explain why.
- My transcription was not blind, so it cannot exclude a reading bias shared with the solver.
