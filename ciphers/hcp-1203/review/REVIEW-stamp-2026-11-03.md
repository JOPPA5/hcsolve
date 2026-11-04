CORRECTIONS

# Review of the stamp-box message, hcp-1203 (2026-11-03)

Reviewer: Claude Opus 5.5, independent check of SOLUTION.md section "Stamp-box message (2026-11-03)".
Claim under review: "Isten vele, édesem, a boldog viszontlátásra. Üdvözli hű kedvese Jolánka." with type MASC + Steganography.

Summary: the plaintext and the type change stand. The corrections are minor. The ledger (C03-C05), and therefore the literal output of the command, prints three letters as read when the audit itself says they are not seen or are restored. Also, "dog" is better supported than the audit says.

## What I checked

- Original: `work/hires/cpc_--23_HU__HU_Rakos-Palota-Ujfalu_jolanka-88_adr.jpg` (3671x2445). My crops, made with my own script (autocontrast, LANCZOS upscale, blue channel where noted), are in `review/work/stamp-2026-11-03/`:
  `overview.png`, `box_1x.png` (x 2900-3450, y 330-960), `row1_4x.png`, `row2_4x.png`, `row3_4x.png`, `row3_start_6x.png`, `row4_4x.png`, `row4_blue.png`, `row5_4x.png`, `row5_blue.png`, `row67_3x.png`, and the comparison crop `cmpA05_06.png` (body rows A05-A06).
- Command `python3 -I ciphers/hcp-1203/work/decode.py`: it prints C01-C07 exactly as the ledger has them (`isten vele / edesem a bol / dog viszintl / a tasra / üdvözli Hű / Kdvese / jolanka`).
- Key: Jolánka family table (hcp-1216 SOLUTION.md) plus this hand's variants, checked against body row A06 "a fogadtatasal".

## Stamp box and type

The dashed stamp frame (upper right of the address side) is empty of the stamp. Torn green stamp paper sits at the lower left corner, lower edge, left edge (beside rows 4-5) and right edge, with glue/brown stains. Seven rows of blue cipher signs fill the frame, in the same hand as the body. There is no plain Hungarian in the box. So writing under the stamp exists, and **MASC + Steganography is justified**.

## My sign-by-sign reading

| row | signs seen (left to right) | reading |
|---|---|---|
| 1 | ʃ, right bowl, Γ, three bars, two strokes, chevron, three bars, wave (crossed at its start), three bars | isten vele: clean |
| 2 | three bars (frame edge), two slashes, three bars, right bowl, three bars, three strokes, two bars, six, 7-shaped loop with descender, wave | edesem a bol: clean |
| 3 | single long slash; 7-shaped sign with tick; e-shaped loop (dot below); chevron; ⅃-hook; right bowl; crossed diagonal; ∂-loop; two strokes; Γ | dog visz-i-nt: all signs separate (see 1) |
| 4 | two bars; Γ; short bar visible above an ink blot, rest of sign under blot; right bowl; F; two bars | a t [a] s r a |
| 5 | (smudge plus green stamp remnant at frame edge, no sign readable even in the blue channel); short slash; chevron; loop with descender plus two dots; crossed diagonal; wave; ∂ with dot; two slashes; cross with double mark | [ü] d v ö z l i H ű |
| 6 | barred three-bar sign (ke); two slashes; chevron; three bars; right bowl; three bars | Kdvese: clean |
| 7 | inverted T; 7-shaped loop; wave; two bars; two strokes; small tick plus hook (k); two bars | jolanka: clean |

My reading matches the claim word for word. The differences are in how certain each letter is and in how the ledger records it.

## Findings

1. **Row 3 "dog" is readable sign by sign, not just a formula reading (minor, in the claim's favour).** `row3_start_6x.png` shows three separate signs: a long slash, then a 7-shaped sign with a tick, then an e-shaped loop. Body row A06 "a fogadtatasal" (`cmpA05_06.png`) shows the same writer's o as the 7-shaped loop-with-descender and her g as the e-shaped loop, immediately after the f-cross. The single slash fits her d (row 5 "dvözli" has the same short slash before the chevron). So d-o-g is read from the pixels. The audit's wording ("crowded, not cleanly separable ... rests on the formula") can be tightened. The dot under the g is stray and has no letter value.

2. **The l of "viszontl-" is in the ledger as if read (minor, correction).** `row3_4x.png`: after the two strokes (n), the row ends with the Γ (t), whose top bar runs out to the frame edge. There is no wave sign. The audit says this correctly, but ledger C03 and the command's literal output read `viszintl`. The l should be marked as not on the card (for example `viszint{l}` or omitted, then supplied in normalization). As it stands, the literal line contradicts the disclosed uncertainty.

3. **The blotted á in row 4 is printed as plain `a` (minor, correction).** `row4_4x.png` and `row4_blue.png` show only a short top bar above the blot. That is consistent with a two-bar sign, and á is the only letter that makes "átásra", so the disclosed restoration is legitimate. Ledger C04 `a tasra` still gives it no mark. It should be marked as restored (for example `a t{a}sra`).

4. **The ü of "üdvözli" is a restoration, not a reading (minor, correction).** In `row5_4x.png` and `row5_blue.png`, the frame edge before the slash (d) is covered by the green stamp remnant and a blue smudge. No cross or dots can be separated there. The audit calls it "not clearly visible". By the standard it is a physically hidden sign restored by sense (the only letter that makes "üdvözli"), and it should be labelled a restoration, as the á is. Ledger C05 prints `ü` unmarked.

5. **"Hű": the h is the near-homograph pair of slashes (minor, already marked).** The sign before ű is two slashes, the same shape as d in rows 2 and 6. The ledger's capital H marks it as an h/p/d near-homograph, and "hű kedvese" settles it by sense. The audit text says "h ű ... is read" and should say h is a sense choice on that sign.

No word in the claim is forced. "viszint" (∂-loop where o is wanted) matches the writer's habit noted in NOTES.md, and the ∂ here has the same shape as the i of "üdvözli" in row 5.

## Could not verify

- Whether a sign sits under the green remnant at the far left of rows 4 and 5, beyond the restored ü. Nothing is visible there.
- The acute accents. As elsewhere on the card, they are not seen and are supplied in normalization.
- No register entry exists (status PARTIAL), so there was no register line to check for this card.
