ACCEPT

# Review 1 – hcp-1038 (Dresden – Blick von der Kreuzkirche, 1908, to Meistrovich Jolánka, Arad)

Reviewer: Claude Opus 5.5, 2026-11-03. Solution under review: SOLUTION.md round 1 (Claude Opus 5.5, 2026-11-03).

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1038/work/decode.py` runs: hashes of the 4 scans OK, 135 signs, 28 distinct, the only letter-level difference is `varok vahaszt` -> `várok választ`. The printed plaintext matches SOLUTION.md word for word.

2. **Own transcription from the pixels.** I cropped and rotated the hi-res address scan myself (`review/work/crop.py`; crops `all.png` (whole cipher block, rotated 90°), `l1.png`, `line3a.png`, `l5.png` (lines 1, 2–3, 4–5 at 1.3x), `bottom.png` and `bot5.png` (bottom-edge line, 1.2x and 4x), `plain.png` (signature block), `stamp.png`, `pic.png`). I read every line sign by sign before comparing with the solver's LINES. My transcription matches the solver's in all 135 signs, including the diacritic-like marks that carry the key: the two dots of `1..` (i) in Jolikám, kikapott, miatt, igazán, is, Sanyi; the comma of `1,` (b) in kezébe; the dot before the 1 (`·1`, ü) in kerülnek; the top dot of `1'` in igazán; `4.` (gy) in nagyon ×2 and hogy; `6.` (ny) in Sanyi.

3. **Independent decoder.** `python3 -I review/work/my_decode.py` (own key table, own transcription, no word breaks) gives
   `édesjolikam / hallottamnagyonkikapottmiatt / amigazánnagyonsajnalomdeénem / isgondoltamhogyédesapjakez / ébekerülnekalapok / sokszorcsokolom / sanyi / varokvahaszt` – 135 signs, 28 distinct, none unmapped. Same as the solver.

4. **Key consistency.** One sign one letter throughout (the a-type `1.`/`1·` pair is the only near-variant and both give a/á). I compared with the Mezőkövesd key in `ciphers/hcp-1174/work/decode.py`: 0 o, 1. a, 1: e, 1' á, 2, cs, 2. é, 3 d, 3, r, 3. v, 4, g, 5 h, 5, l, 6, n, 7 k, 7, s, 7. sz, 8 m, 8, t, 9 p, 9, z agree. Differences are correctly reported as new or different: here i = `1..` (hcp-1174 has plain `1` = i), ü has the dot before the 1 (hcp-1174 writes `:1`). The agreement of ~20 values with an independently reconstructed key, plus the plain signature "Sanyi" equalling the enciphered `7, 1. 6. 1..`, makes the key solid.

5. **Disclosed irregularities, checked on pixels.**
   - `vahaszt`: at 4x (`bot5.png`) the 5 in `3. 1· 5 1·` has no comma beneath it; the blob left of it is the mid-height dot of the preceding 1. So as written it is h; "választ" is a sense correction, correctly disclosed.
   - `2` = l in Jolikám: line 1 (`l1.png`) clearly shows a plain 2 with no mark, between `6 0` and `1..`. Single occurrence, disclosed as resting on word sense.
   - "de énem" for "de én nem": the signs `3 1: 2. 6, 1: 8` are clear; the haplography is disclosed.

6. **Plain parts.** Signature block (`plain.png`): "Szívélyesen üdvözlöm / Sanyi" with paraph – agreed. Picture side: printed "Dresden – Blick von der Kreuzkirche", handwritten "1908. Okt. 16." – agreed; no other writing in the picture or margins.

7. **Language and context.** Period Hungarian, polite third-person address (kikapott, édesapja, csókolom) consistent throughout; content (apology that earlier cards reached her father) fits a love-letter cipher and the addressee Jolánka (Jolika). The English and Slovak translations are accurate.

8. **Sources.** Portal status Not solved, no attached transcription or solution; the solver says so and says the HistoCrypt article was not checked card by card. No sign of an undisclosed published solution.

## Findings

1. **minor – orientation of the bottom-edge line is misdescribed.** SOLUTION.md and NOTES.md say `Várok választ` runs "upside down along the bottom edge". In the scan (`bottom.png`, unrotated) it reads upright, left to right, in the address orientation; it is at 90° to the message, not upside down relative to it or to the address. Please correct the wording (it does not affect the reading).

2. **minor – steganography / stamp.** The human's note in this run says that on the Jolánka cards there is almost always a hidden (plain or enciphered) message under the stamp, and suggests the type `MASC + Steganography`. This card goes to Meistrovich Jolánka in Arad, a different person and a different (digit) cipher family from the Tóth Jolánka / Árokszállás graphic-cipher cards; still, the warning is relevant. Here the 5-Pf Germania stamp is still attached (upside down) and nothing shows through or around its perforations (`stamp.png`), so whether anything is written under it cannot be checked from the scan. The solver discloses this correctly. Recommendation: keep the register type `MASC` (there is no evidence of hidden writing on this card), but state explicitly in SOLUTION.md and the report that, given the collection's habit, a message under the stamp is possible and could only be checked on the physical card – and do not call the card complete with respect to the stamp area.

3. **minor – self-referential check.** `work/decode.py` asserts against a READING list that the script itself contains, so its "only one difference" assertion is a consistency check of the solver's own notes, not independent evidence. Acceptable as is; just do not present it as more than that in the report.

4. **minor – address street.** "Boczkó tér 7." is partly under the collection stamp; the visible letters read more like "Bockó tér" / "Bocskó tér". Mark the street name as uncertain (it does not affect the decipherment).

## What I could not verify

- The area under the attached stamp (cannot be seen on a scan).
- Whether the HistoCrypt article linked from the portal discusses this card.
- The identity of "Sanyi" and of Meistrovich Jolánka beyond the address.
