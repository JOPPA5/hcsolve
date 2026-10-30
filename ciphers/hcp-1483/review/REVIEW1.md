ACCEPT

# Review 1 - hcp-1483 (pc_hcp_164), reviewer Claude Opus 5.5, 2026-10-30

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1483/work/decode.py` (run from the repo root).
   The source hashes check out, and it ends with "468 enciphered letters decoded, all signs mapped".
   The output matches the plaintext block in SOLUTION.md line for line.
2. **Independent decoder.** `review/work/indep.py` does not read `key.json`. It rebuilds the key
   only from the stated rule: consonants B C D F G H J K L M N P Q R S T V W in order over
   side (l, r, x) x position (t, b) x bar count (1-3), plus the six closed vowel/Y shapes.
   Run: `python3 -I review/work/indep.py work/transcription.txt` (from the cipher directory).
   - It gives the same text for all 20 lines.
   - 17 of the 18 consonant slots are used. Only r1t (J) never occurs.
   - Sign frequencies look like English: Δ (E) and □ (O) 43 each, ⊥ (T) 39, ⊙ (A) 34.
   - Because the decoder is derived from a rule, the key cannot have been tuned sign by sign.
     Continuous, fluent English from such a rule is strong evidence that the key is right.
3. **Transcription against the scan.** I rotated `source/address-large.jpg` by 180 degrees myself
   (`review/work/crop.py`) and enlarged it 3-7x. Crops are in `review/work/`.
   - **P.S. line** (`ps_a.png`, `ps_b.png`): ⊥∃Δ丰 with ⊥ above the line and a caret, then ⊙ L Ē, □Ŀ, ⊥∃Δ丰,
     7⊙Ŧ∃, ⅃⊙丰, 7Δ²Ŀ, FΔ丰²Δ∃ !!!. The sign in "FAS" is clearly a single-bar ⅃, not a three-bar ∃,
     so the "FAS" slip is real. The first triangle of "THES" has no visible inner stroke, which
     agrees with the solver's disclosure.
   - **Lines 1-2** (`l1.png`, `l12a/b.png`): MY OWN CARIAD … YOU SO / MUCH FOR THE CARD. I KNOW YOU WILL.
     The signs match the transcription.
   - **Line 5** (`l5.png`): RECEIPT uses the three-bar low-right sign Ē (P). The word in quotes starts
     with a plain L (M). The writer therefore did distinguish P from M, and "MIONEER" is a genuine
     slip, correctly reported literally.
   - **Lines 11-13** (`l11_14.png`): I AM SO GLAD TO HEAR THAT YOU / ARE STILL GETTING BETTER. BE QUICK /
     AND GET QUITE ALL RIGHT, DARLING. The signs match, including T-shaped Q + ⧄ in QUICK and QUITE.
   - **Line 15** (`l15a.png`, `l15b.png`):
     - 7 □ L [slanted crossed sign with an ink blob] Ē F Δ ⊥ Δ F ⊠ gives COM?PLETELY. The extra sign
       is visible, as stated.
     - The underlined Δ and ±□⧄F∃ Ŀ□⊥ give I WOULD NOT.
     - 丰 ± □ give S W O. The last sign is overlapped by the printed "& Sons" margin text, so P (bars
       low) cannot be confirmed. SWOL vs SWOP is disclosed.
   - **Line 17 and signature** (`sig.png`): FΔ丰² LΔ ⅃□² ĿΔ⅃∃⊥ gives KISS ME GOONIGHT (no D sign;
     the sign after OO is the two-bar Ŀ). The quoted signature ⊠□⧄F 7□⊠ fits YOUR BOY. The first
     signs are small and cramped, so "probable" is the right label.
   - **Address** (`addr.png`, upside down relative to the message): "Miss G(?). Williams,
     'Baronhill', York Road, Colwyn Bay, N. Wales" agrees with SOLUTION.md.
4. **Language and context.**
   - The text is idiomatic Edwardian English for a love card: "unthankful beast", "sweetheart
     mine", "I would not swop with … for forty worlds", "this stamp has been kissed".
   - The Welsh endearment "cariad" fits an addressee in Colwyn Bay. The date (Feb 1908) raises no
     anachronism.
5. **Disclosure and sources.**
   - The portal is "Not solved", with no attached solution. SOURCES.md records no published
     solution.
   - The credits split the work truthfully: the GPT solver did the triage, and Claude Opus 5.5
     did the decipherment.
   - Every writer slip and uncertain sign I found on the scan is listed in SOLUTION.md.

## Findings

1. **minor – Address street is inconsistent across the solver's files.** `source/metadata.md` and
   the GPT triage note say "Oak Road" (provisional). SOLUTION.md says "York Road", and the scan
   supports York Road. SOURCES.md or NOTES.md should note that the triage reading was wrong
   (source/ itself must stay unchanged).
2. **minor – Initial of the recipient.** The portal lists the recipient as "J.Willams". SOLUTION.md
   states "Miss G. Williams" as fact. The capital on the scan is a looped script letter that could
   be G or J. Mark it as uncertain.
3. **minor – The J slot in the key is inferred, not observed.** r1t = J never occurs on the card.
   It comes only from the alphabetical rule, which is sound but unattested here. key.json and the
   key table should say so. SOLUTION.md already says J, X and Z do not occur, but it does not say
   that the J *assignment* is a deduction. The same applies to Q (x1t), which is attested only in
   QUICK and QUITE (2 occurrences, both consistent).
4. **minor – Literal decode line P1 prints "THES^TAMP".** This is disclosed and normalised to
   "This stamp", so it is fine. The report should explain the shared S and the caret insertion
   once, so a reader of the PDF is not confused.

None of these affects the decipherment.

## What I could not verify

- I did not re-check every one of the 468 signs at high magnification. I checked the P.S., lines
  1, 2, 5, 11-13, 15 and 17 and the signature sign by sign, and the other lines at 3x. The
  independent rule-based decode gives fully coherent English on every line, which makes an
  undetected misreading very unlikely to change the meaning.
- Two-bar vs three-bar crossings in TOMOROW (W vs V) and the covered last sign of SWOL could not
  be resolved from the 1024-px scan. The solver discloses both.
- Identities: the sender, "Mister Kay" and "the Pioneer" periodical are not identified.
- I did not test the key on sister cards hcp-1484 and hcp-1485. That is outside this review.
