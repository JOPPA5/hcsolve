REVISE

# Review 1 — hcp-1395 (pc_hcp_76), Caesar −1 postcard, 1907

Reviewer: Claude Opus 5.5, 2026-10-30. Role: reviewer, round 1 (highest marker DONE1).

## Summary

The body reading is correct. I checked it on the pixels and decoded it with my own script: "My dearest, I am just going to post … from your own girl". It uses one fixed Caesar shift of −1, covers all 44 letters and leaves no unknowns. The only weak point is the closing group before *gspn*. The solver now reads it as ciphertext "M. & L." → **L. & K.** and expands that to "Love & Kisses". The uncertainty section discloses this, but the headline quote and the English/Slovak translations present the expansion as read text. The solver also fails to mention the competing N-reading (→ M & K), which sister cards of the same writer support. These are presentation and disclosure fixes; the reading stands. Hence REVISE, not REJECT.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1395/work/decode.py` (from the repo root) prints "source hashes OK", six rows and "44 cipher letters". It ends with `MY. DEAREST. I AM. JUST GOING TO POST L. & K. FROM. YOUR. OWN GIRL`. This matches the table in SOLUTION.md and `work/plaintext.txt`.
2. **Independent decoder.** I wrote `review/work/mydecode.py` from scratch: a shift of −1 applied to my own transcription. It gives an identical output with 44 letters. For the alternative initial `N. & L.` it gives `M. & K.`.
3. **Transcription against the scan.** I rotated `source/address.jpg` 90° CCW (`review/work/rot.png`) and enlarged it to 3×: `review/work/top3x.png` and `review/work/bot3x.png`. Line by line:
   - `Nz. Efbsftu.`: the N is a hooked stem with one arch, and the z is a cursive 2-like z. Efbsftu is clear. ✔
   - `J bn. kvtu`: long J; "bn."; kvtu is written loosely (v open, u with a final flourish), but kbtu/kvtw give nothing and kvtu = JUST. ✔
   - `Hpjoh up qptu`: clear. ✔
   - `Zpvs. pxo`: clear. ✔
   - `Hjsm` inside the ornamental outline: H, a long slanted j, s, m. ✔ This is the enciphered GIRL, not a signature, which agrees with hcp-1397 (FINAL) "Hjsm".
   - Heading "G. H. Wednesday" and "April 24th 07." are in clear, and the date agrees with the postmark WIMBORNE AP 24 07. The address reads Mr Abbott, Stokelake Farm, Chudleigh, Devon. The portal's "W. Abboú" is a misreading. ✔
4. **Closing initial.** Crops: `review/work/initials5x.png`, `review/work/N_vs_M_6x.png` (N of "Nz" next to the closing initial, same scale) and `review/work/initialM_10x.png` (10×, autocontrast). The closing initial is clearly wider than the N of "Nz". After the hooked stem I can see two descending legs, against one in "Nz". It also matches the solver's hcp-1407 comparison crop. I accept **M** as the better reading, though not a certain one: this hand's M and N differ only in the number of short legs.
5. **Key coverage.** All 44 alphabetic signs decode under the one shift. Nothing is skipped and no sign is outside the key. The ampersand and dots pass through.
6. **Language and context.** The text is idiomatic Edwardian English for a postcard and uses the same formulae as sister cards hcp-1397 ("Love from your own girl"), 1388 and 1407. Wimborne → Chudleigh, April 1907, fits the 1907–08 correspondence.
7. **Published solution.** The portal status is "Not solved" with no attached solution. I found no use of a published solution. The credit section truthfully separates the GPT-6 Astra work (2026-10-26) from the Claude Opus 5.5 completion (2026-10-29).

## Findings

1. **(major) The expansion "Love & Kisses" is presented as read text.** The headline is "L[ove] & K[isses]". The English line in "Transcription and plaintext" says "Love and kisses from your own girl", and the Slovak says "Láska a bozky" with no brackets. The only letters that can be deciphered are "L. & K."; "Love & Kisses" is an editorial expansion of two initials. Uncertainty 1 admits this, but the translations must match it: write "[L. & K. — probably love & kisses]" or similar in both translations and in the headline.
2. **(major) A competing reading of the initials is not disclosed, and it is inconsistent with sister cards.** The solver gives only one alternative (initials in clear → "M. & L."). It omits **N. & L. → M. & K.**, and the writer's own cards support that reading:
   - hcp-1388 has an enciphered `N yy` = **M xx** (M + kisses) before "from your own girl".
   - hcp-1399 reads the same slot as `N & Lt` → **M & Ks**.
   - hcp-1407, the solver's own comparison card, keeps the same group literal as "[M. & L.]" and explicitly does *not* claim L & K.

   My crops favour M over N here (finding 4 above), so L & K is a defensible literal output. But this card now classifies the group with more confidence than its siblings do. SOLUTION.md should list N→"M & K" as an alternative with this evidence, and should say plainly that the classification differs from 1399/1407.
3. **(minor) The hcp-1397 slot argument is weaker than stated.** In hcp-1397 the word in the slot is a full enciphered word (Mpwf = LOVE). That shows the writer enciphers the closing, but it does not show that the *initials* are enciphered. Present it as supporting evidence, not as proof.
4. **(minor) The NOTES.md entry of 2026-10-26 has lost its spaces** ("ReadREADMEfull. Rootall3tabcapture…"), which makes it hard to read. It is cosmetic; the content can still be followed.
5. **(minor) Unclear wording for "post".** Uncertainty 2 says nothing is added to "post". That is fine, but the English "going to post" could be glossed "going to the post [office]" so readers who do not know the idiom are not puzzled. Optional.

## What I could not verify

- Whether the writer meant the closing initials to be enciphered: the card itself cannot settle it, and the M/N distinction in this hand rests on one extra short stroke.
- The meaning of the heading initials "G. H." (or "C. H."): they are in clear and not part of the cipher.
- I did not re-open the portal page. I rely on `source/metadata.md` and SOURCES.md for the status and attachments, and the source hashes match the solver's recorded values.
