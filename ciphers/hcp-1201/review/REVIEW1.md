ACCEPT

# Review 1 of hcp-1201 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1201/work/decode.py` was run from the repo root. All four SHA-256 checks print OK. The output is `19-15-21-22-3-14-9-18 -> SOUVCNIR` and `1-6-6-5-3-20-21-5-21-23 -> AFFECTUEUX`, which matches what SOLUTION.md claims, including the disclosed literal C in line 1.
2. **Independent transcription.** I made my own enlarged crops of the hires address side (`review/work/l1_left.jpg`, `l1_right.jpg`, `l2_left.jpg`, `l2_right.jpg` at 2x, and `l1_22_3.jpg`, `l2_3.jpg`, `l2_23.jpg` at 4x) and read every number myself. My reading is the same as the solver's on all 18 numbers:
   - Line 1: `19-15-21-22-3-14-9-18.` The 9s in "19" and "-9-" are open q-shaped nines with a straight descender. The fifth group is a looped descending French 3 ("ʒ" shape), not a 5: the card's 5s (in "15", in "65" and the lone "-5-") all have a flat top flag, and this glyph has none.
   - Line 2: `1-6-65-3-20-21-5-21-23.` "65" is a 6 and a flagged 5 with no dash between them. The fifth group has the same descending 3 as in line 1. The last group is 2 plus a closed-loop 3 that stays on the baseline and ends in a left hook; it has the 3's right-hand bulge, not a 9's straight stem, so it reads 23, not 29.
3. **Independent decode.** `review/work/verify.py` decodes my own number list with (a) the plain 26-letter A=1 count, giving `SOUVCNIR AFFECTUEUW`, and (b) the 25-letter count without W, giving `SOUVCNIR AFFECTUEUX`. Only the final number tells the two apart. 18 numbers and 13 distinct values, all mapped by one key, so the key covers the whole ciphertext.
4. **Plaintext and context.** "Souvenir affectueux" is the standard French postcard closing formula of the period. "Devine" (guess [who]) plus initials is a normal teasing signature, and it explains why the writer enciphered the text. Counting the alphabet without W is historically natural for French in 1907, because W was then treated as a foreign letter outside the 25-letter school alphabet. This makes X=23 more likely to be intended than to be a slip.
5. **Plain parts.** From `review/work/sig.jpg` I read "Devine" and "A. M". The first initial is a looped script capital, most likely A. From `review/work/addr_name.jpg` I read the address as "Mlle Madeleine [R/V]ocheron (or -acheron), grande-rue, Parigné-l'Évêque, Sarthe". The postmarks say PARIGNÉ-L'ÉVÊQUE SARTHE, 24-6-07 and 25-6-07. Everything on the card reads; nothing is left unread.
6. **Picture side.** At full size the picture side shows three kittens, a fence and a stag beetle. A 5 c Blanc stamp sits upright at top left, with a postmark. I found no writing in the picture, along the edges or in the margins.
7. **Portal mismatch.** The hires file names (`cpc_1901-03-05_DE_Kiel_DE_Zeitz_hedwigzipfel-13_*`) and SOURCES.md confirm that these French images are what the portal serves for record 1201, even though its metadata describes a Kiel to Zeitz card to Hedwig Zipfel dated 1901. The solver disclosed this.
8. **Published solution.** The portal shows Not solved with no solution attached. The solver says no web search was made. I made none either, so this item is not independently checked (see below).

## Findings

1. **minor — the address-side stamp is mounted upside down, and the solution does not mention it.** `review/work/stamp.jpg` shows the 5 c Blanc on the address side inverted: "POSTES" and the "5c" are upside down. The picture-side stamp is upright. Under the period "langage des timbres", an inverted stamp was a deliberate signal (typically affection), which fits "Souvenir affectueux. Devine." It is not a cipher and does not change the reading. It should be noted in the uncertainties or context, and it is another reason why what lies under the stamps cannot be checked (finding 3).
2. **minor — "X = 23" is presented as a possible counting slip on equal footing.** The 25-letter alphabet without W was the normal French school alphabet in 1907, so 23 = X is more likely intended than a slip. The solver could say so in the report. This does not change the reading.
3. **minor — steganography under the stamps.** The human's note for this run is that stamp-area hidden messages are common on some series (the Jolánka cards). The solver correctly says the stamps are attached and the area under them cannot be inspected. Nothing on this card points to a hidden message: no traces at the stamp edges, and the visible text is complete. The cipher type should therefore stay MASC, not "MASC + Steganography". The report should keep the explicit statement that nothing under the stamps could be checked.
4. **minor — the recipient's surname.** The capital is a looped script letter, and the second letter looks more like o than a. I would give "Rocheron" at least equal weight with "Vacheron". It is already disclosed as uncertain and is not part of the cipher.
5. **minor — 3 written for 5 in line 1.** I confirm the solver's reading on the pixels: the glyph is a 3, so the plaintext correction to SOUVENIR is an interpretation and not a reading. It is disclosed clearly in SOLUTION.md and in the decoder's output, and it should stay that way in the report.

## Could not verify

- What lies under the two stamps.
- Whether a published solution exists elsewhere, since I made no web search. The portal itself has none.
- Why the portal metadata (Kiel to Zeitz, 1901, Hedwig Zipfel) does not match the images. It may be a mix-up on the portal side.

## Register note

The reading is complete apart from one disclosed sender slip, and every part of the card is read. Type label: `MASC`. Name: `cpc_1901-03-05_DE_Kiel_DE_Zeitz_hedwigzipfel-13`, as on the portal. Check register-exclusions.json before writing the entry.
