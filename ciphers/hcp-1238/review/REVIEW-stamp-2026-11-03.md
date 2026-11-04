CORRECTIONS

# HCP1238 stamp-box review (2026-11-03, Claude Opus 5.5, independent reviewer)

Scope: SOLUTION.md section "Stamp-box message (2026-11-03)", ledger rows S1-S7 in `work/ledger-opus.txt`, and the type note "MASC + Steganography". The main text was not re-reviewed.

## What I checked and how
- Original: `work/hires/cpc_1914--_HU__HU_Jasz-Arokszalas_jolanka-118_adr.jpg` (3445x2210). Stamp box is at about x 2650-3180, y 190-810.
- My own crops are in `review/work/stamp-2026-11-03/`. `box2x.png` is the whole box. `r1_4x` to `r6_4x` and `s7_4x` are rows at 4x with contrast raised. `s1_left6x`, `s2_left6x`, `s7_left6x` and `s3s5_color3x` show the starts of rows next to the torn edge. `box_purple2x`, `tri_purple4x`, `s7_left6x_purple` and `tri_RminusG4x` are channel separations: (R+B)/2-G pulls out the purple pencil and drops the blue ink and the green frame.
- The reference sign shapes come from main-text row 27 (*maradok szerető kedvese Feri*) in `m27a.png` and `m27b.png`. The z comparison is in `cmp_z_s4.png`. The sign values are from the family key `../hcp-1216/work/graphic-key.json`.
- I did not read the solver's crops in `work/stamp-2026-11-03/` before reading the signs.

## Type change: justified
The stamp's middle has been torn out. Green frame and perforation remnants of the stamp paper are still stuck at the edges. Seven rows of purple-pencil cipher signs, in the same hand and key as the main text, are written on the card inside that box. Rows S1-S4 start right at the torn left edge of the remnant, and S7 runs under a green frame fragment, so the writing goes on under the remaining stamp paper. The writing was hidden under the stamp, so `MASC + Steganography` is justified. There is no plain-Hungarian writing in the box. A blue triangle (eye in rays) is stamped over the middle.

## My reading, sign by sign (key values; [ ] = not seen)
- S1: [hidden] ) s, ∂ o, § k, ∂ o, ~ l → `{c}sokol`. Agrees. The c is correctly marked as hidden under the remnant at the left.
- S2: faint arc at the torn edge, then three short strokes m, ↄ s, X-shaped sign, two bars a. Gives `(o)msza`.
- S3: horizontal bar touching the torn edge, two bars a, wave l running into the triangle's apex, two bars a, two short strokes n. Gives `[m](t)alan`.
- S4: ) s, a hooked curve, [one sign under the triangle], F r. Gives `s(z){o}r`.
- S5: one curved sign left of the triangle, about three signs under the triangle, one sign right of it. Unread. This agrees with the claim.
- S6: two strokes h, X u, § k, three bars e, two strokes d. Gives `huked`. No double-acute mark is clearly visible over the u.
- S7: Λ v, bars e, ↄ s, one faint bar at the edge of the green fragment, dark cross f, two bars e, F r, i. Gives `ves(e)feri`.

Normalized, this is the same as the claim: *Csókolom számtalanszor [S5 unread] hű kedvese, Feri.* The English and Slovak are fine. I agree that S5 cannot be recovered. In the purple channel the inside of the triangle shows only JPEG chroma blocks and no pencil strokes. I also agree that not claiming "sírig" is correct.

## Differences (all minor; the normalized message is unaffected)
1. **S3 m is not on the pixels.** The ledger and SOLUTION give `mtalan` with no brackets. The row's first visible mark is a horizontal bar at the torn edge (`s3s5_color3x.png`, top row; `left_mid_4x.png`), with no stem visible, and there is no three-stroke m anywhere in S3. S2 ends with a after X, with empty space to its right. The m of *számtalan* is therefore restored: it is presumably under the stamp remnant, and the t is only partly visible. The literal should be `{m}(t)alan` and the restoration should be disclosed. One letter makes the word, so the restoration is allowed under the standard.
2. **S4 o is under the triangle, but the literal is unbracketed.** Between the hooked sign and the r (F) only the triangle is visible (`r4_4x.png`, `s3s5_color3x.png`). The literal `szor` should read `sz{o}r`. In addition, the second sign of S4 is a hooked curve. It does not match the main-text z, which is an X with a crossbar (`cmp_z_s4.png`, first panel against third). z is a reading by sense and should be disclosed as such.
3. **S2 z and o are not clean matches.** The fourth sign of S2 is a plain X with a small hook and no crossbar, so it is closer to the u sign (x) than to the main-text z (`cmp_z_s4.png`, second panel). z rests on sense. The o of `omsza` is only a faint arc at the torn edge (`s2_left6x.png`) and should be marked as partial.
4. **S7 `ese{..}`.** After v e s there is only one faint bar, at the edge of the green fragment, before the f (`s7_left6x.png` and its purple version). That bar is the second e of *kedvese*, and it is only partly visible. I see no evidence of "one or two" further hidden signs between it and *feri*. The gap there is narrow and may simply be space. The literal should be `ves(e)feri`, and the statement that "one or two signs lie under the green frame fragment" should be dropped or weakened to "possibly".
5. **S6 inconsistency.** The SOLUTION literal block shows `S6 hukedv-` but in the same line says the v begins S7. The ledger has `hukedv?`. On the pixels S6 ends with d (`r6_4x.png`) and S7 begins with the chevron v. S6 should be written `huked`. Also, no double acute is clearly visible over the u, so *hű* is a normalization of literal `hu`.

## What I could not verify
- The signs under the triangle (S5 and the S4 o): no separation recovers them from this scan.
- Whether the S3 m and the S1 c really sit under the stamp remnant, or whether the writer left them out.
- The diacritics in the stamp rows.
