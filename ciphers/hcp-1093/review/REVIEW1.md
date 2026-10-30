ACCEPT

# HCP1093 — Review, round 1

Reviewer: Claude Opus 5.5, 2026-10-30. Target: SOLUTION.md (round 1), work/transcription.txt, work/decode.py.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1093/work/decode.py` (from repo root) runs cleanly:
   source hashes OK, 151 signs, literal text with `FAALS TIRAD` and `BeTTER`, emended text
   `DEAREST BETTY / WHAT ABOUT THIS / FOR A PHOTO OF / BRUCE SHALL GO TO / BED EARLY TONIGHT /
   FEELS TIRED OR SOME / THING COLD A LITTLE / BETTER WITH FONDEST / LOVE AND KISSES FROM YOURS /
   EVER BOB / XXXXXXXX`, identical to the plaintext in SOLUTION.md.
2. **Independent decoder.** `review/work/indep_decode.py` uses an explicitly written table copied
   from the accepted HCP1188 key (BR=A/B, B=C/D, BL=E/F, R=G/H, C=I/J, L=K/L, TR=M/N, T=O/P,
   TL=Q/R, V=S/T, >=U/V, <=W/X, ^=Y/Z), parses every token with a strict regex, and ignores the
   solver's emendation markup. Result: 151 signs, 0 unparsed tokens, the same literal text; the
   only marked tokens are the three `BR0!E` and the one blotted `BL0*`. The key covers all of the
   ciphertext; a single fixed 26-letter alphabet, with 23 letters used.
3. **Transcription against the scan** (crops in `review/work/`, 3–9x, from work/upright.jpg, which
   is a pure rotation of source/address-large.jpg):
   - Sample rows checked sign by sign: DEAREST BETTY (row01), WHAT ABOUT THIS (row02),
     BRUCE (bruce.png: dot clearly left inside the ⅃ → B), SHALL GO TO (row05), BED EARLY TONIGHT
     (row06), THING COLD (row08), BETTER WITH FONDEST (row10), LOVE AND KISSES FROM YOURS / EVER
     (row10, sig.png). All agree with the transcription.
   - **FEELS / TIRED (the 3 slips)** — feels.png, tired.png, tired2.png. Signs 2 and 3 of FEELS
     really are ⅃ (right vertical, foot running left), not L; sign 1 is a dotted L (F), sign 4 a
     dotted ⊏ (L), sign 5 an undotted V (S). In TIRED: V with a faint dot near the apex (T), a
     closed box (I), dotted ⌜ (R), then ⅃ (A), dotted ⊔ (D). The ⌜ and ⅃ are separate signs
     (the ⌜'s top stroke ends well short of the ⅃'s vertical). So the literal FAALS TIRAD is
     a correct reading of the pixels, and the solver did not force E onto the image: it is
     labelled as an editorial emendation, and the literal reading is printed. E is written as L
     in all 15 other places and A as ⅃ in all 8 other places, so FEELS TIRED is the only
     reasonable reading of the passage. Disclosed (Uncertainty 1).
   - **Blot in BETTER** (better2.png): under the blot the left vertical and a bottom stroke running
     right are visible, so the outline is L (E/F); undotted cannot be confirmed. Restoration E is
     well supported and disclosed (Uncertainty 3, lower case in the literal output).
   - **Signature BOB** (bob2.png, bob3.png, pixel map): the first ⅃ has a compact dark mark (about
     3x2 px, darkest 106,90,74) inside its left corner, the same position as the B dots
     elsewhere. It is darker and greyer than the surrounding upside-down orange print (around
     156–173,120–130,87–95). I agree that it is a pen dot: B. The middle sign is an undotted ⊓
     (O), and the third sign is a dotted ⅃ (B). Disclosed (Uncertainty 4).
   - **Kiss row**: see Finding 1.
4. **Language and context.** Natural Edwardian English postcard prose (postcard ellipsis
   "Shall go to bed early tonight, feels tired or something. Cold a little better"), with a
   conventional greeting and closing. "Betty" as a pet form for Miss Unsworth and "Bob" as the
   sender fit; "Bruce" fits the dog on the picture side. The date and place (Shawford/Twyford,
   neighbouring villages near Winchester, April 1913) are consistent with the postmark.
5. **Sources and credit.** SOURCES.md and SOLUTION.md state that no published solution exists or
   was used. The portal status at capture was "Not solved". The key is openly credited as
   transferred from HCP1187/1188, and the GPT earlier work is credited. I found nothing undisclosed.

## Findings

1. **Kiss row has 9 signs, not 8 (minor).** A column projection of grey pen ink in the bottom row
   (y 962–995, excluding orange print by r−b<45) gives nine separate ink runs at
   x ≈ 354–373, 382–399, 413–426, 444–464, 476–492, 500–517, 530–547, 556–571 and 585–604.
   The crops kisses4.png (x from 370) and kisses5.png (x 280–420) confirm that the leftmost run
   (x ≈ 354–373) is a separate dotted < sign, on its own to the left of the eight that the solver
   counted. The transcription, the decoder assertion, SOLUTION.md and any report should read 9 ×
   `<1` = XXXXXXXXX, and the sign total should be 152. This does not affect the message.
2. **Emendation explanation is speculative (minor).** The phrase "local mirror slip" is a
   plausible guess but no more than that. The literal reading FAALS TIRAD, and the fact that 3
   signs are emended, should stay visible in the report next to the normalised text. SOLUTION.md
   already does this; it just needs to carry over to the PDF.
3. **Faint dot in the T of TIRED (minor, disclosed).** The dot is faint but present on tired2.png.
   An undotted reading (S) would give SIRED, so the context agrees with the dot. No change needed
   beyond the existing disclosure.

## What I could not verify

- The physical card. Readings rest on a single 1024 px scan, so the dot under the blot and the
  faint dot in the T cannot be confirmed beyond the pixels described above.
- The identities of Bob, Betty Unsworth and Bruce. I did no genealogical check.
- The postmark date is not fully legible ("AP 15" is visible on the stamp); the year comes from
  the catalogue.
