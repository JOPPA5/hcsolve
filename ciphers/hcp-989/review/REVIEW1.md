ACCEPT

# hcp-989 – review round 1 (Claude Opus 5.5, reviewer, 2026-11-03)

The reading of the enciphered words, APFELWEIN. STUBE. ("in der Apfelweinstube"), stands. The plain Kurrent message
around it is transcribed correctly. The key is the hcp-1194/1195 rune alphabet applied without change. The one
unread item is the 8-sign parenthetical word on line 4. It is a single word, the rest of the card reads without it,
and the solver disclosed it. Under the run rules that counts as a complete card. The findings below are minor wording
and disclosure fixes for SOLUTION.md and the report. None of them changes the reading.

## What I verified and how

1. **Solver's command.** I ran `python3 -I ciphers/hcp-989/work/decode.py` from the repo root. All four SHA-256
   checks print OK, and the output is `AP/BFELWEIN. STUP/BE.` → `APFELWEIN. STUBE.`, identical to SOLUTION.md.
2. **Independent transcription and decode.** I cropped the message strip from the hi-res original and rotated it 90°
   (review/work/strip.png). I enlarged the cipher words 4–8x (review/work/w1.png, w2.png, s4to9.png, s7to9.png,
   w2b.png) and read every sign myself. My script review/work/mydecode.py applies the sister-key values literally
   and gives `ABFELFEIN. STUBE.`. APFELWEIN only appears after two word-sense substitutions: B→P at position 2 and
   F→W at position 6 (see findings 1 and 2).
3. **Sign by sign** (own reading):
   - ᛅ-diag = A.
   - B with long tail = B/P.
   - ᚠ = F.
   - Slanted cross = E.
   - Λ-like sign with a short right leg = L. Its leg is clearly shorter than that of the N (sign 9), which reaches
     the baseline, so the L/N split is supported but thin.
   - ᚠ = F/W.
   - Cross = E.
   - Short dark horizontal dash with only a ghost of a stem = I (see finding 3).
   - Λ with a dark left stroke and a faint right leg = N.
   - Full stop.
   - ϟ = S.
   - ᛏ with a faint left barb and a heavy right hook = T.
   - Γ/Π hook = U.
   - B = B.
   - Cross = E.
   - Full stop.

   All 14 signs of line 3 are covered by the key, and no sign value was invented for this card.
4. **Plain text** (strip.png):
   - "Lieber Hugo", with "3/4 7 - 7 Uhr" at the top right.
   - "Ich erwarte Dich zwischen [ink blot] Uhr in der …".
   - Line 4: "[inked-over word] ( … ) am Samstag 19/10 Toni".

   All of this agrees with SOLUTION.md. The blot after "zwischen" and the inked-over word at the start of line 4
   (review/work/struck.png) are solid ink masses with no legible strokes. They are writer's deletions, not
   ciphertext.
5. **Parenthetical word** (review/work/paren4.png, 5x). I read eight signs:
   - Sign 1 is ϟ-like with a top bar.
   - Sign 2 is a Y-form (E on hcp-1195).
   - Signs 3–5 are heavily overwritten (fork/Ψ- and W-like masses).
   - Sign 6 is the one-twig ᚴ (K).
   - Sign 7 is ᛁ (I).
   - Sign 8 is a 大/ᚼ-like sign.

   I tried S-E-M-M-E-K-I-H and similar sequences and found no defensible word either. I agree it is unread and
   rightly not forced.
6. **Date.** 19 October 1901 was a Saturday (Python `datetime`). The dispatch cancel on the stamp reads
   "19 10 01 … WIEN 64", and the arrival cancel at the right reads WIEN 17/105 with the same date
   (review/work/stamp.png). Both agree with "am Samstag 19/10" and with a same-day meeting.
7. **Steganography / stamp.** The printed stamp box is empty apart from a faint bluish offset smudge
   (review/work/stampbox.png). The 5-heller stamp is glued diagonally over "Postkarte / Post card" in the header,
   and nothing shows around its edges. The picture side has no other writing besides the margin message.
   The user's note on stamp-hidden messages concerns the Jolánka (Arokszállás) series, not this Vienna card. Still,
   the off-box, diagonal stamp means a hidden note under it cannot be excluded. The solver disclosed this (unc. 8).
8. **Sources.** SOURCES.md and the hashes match. The portal shows Not solved with no attached solution, and the
   solver credits the sister cards. I found no use of a published solution.

## Findings

1. **(minor) The W in APFELWEIN is not a "heavy" ᚠ on this card.**
   - **Evidence:** In review/work/s4to9.png, sign 3 (F) and sign 6 (claimed W) have the same stroke weight and the
     same two-twig form. Sign 6 is not visibly heavier, and it carries no dot. On hcp-1195, W is a dotted fehu.
   - **Problem:** The key table entry "fehu written heavily (f2heavy) → W" and uncertainty 5 ("written much more
     heavily than sign 3") overstate what the pixels show.
   - **Fix:** State that this card writes F and W with the same sign, so W rests wholly on word sense, as P does.
     Change the key table and the report to match.
2. **(minor) Two of the nine letters of APFELWEIN come from word sense, not from distinct signs.**
   - **Evidence:** P (B without dot) and W (F without dot) are both word-sense calls. The literal sister-key output
     is ABFELFEIN.
   - **Fix:** The "Why I believe it is correct" section should say this plainly rather than "B/P the only shared-sign
     compromise". The reading stays very strong: Apfelweinstube is a real Viennese tavern type, and the result fits
     the grammar of "in der ___".
3. **(minor) Sign 8 of APFELWEIN (I) is mainly a short horizontal dash.**
   - **Evidence:** In review/work/s7to9.png the dark ink of sign 8 is a short horizontal dash, and the vertical stem
     is only a ghost.
   - **Fix:** The solver mentions the drying pen, but should say explicitly that I rests on word sense. A hyphen
     inside a word would make no sense here.
4. **(minor) Proportion of the ciphertext left unread.**
   - **Evidence:** The unread parenthetical is 8 of the 22 cipher signs on the card, about a third.
   - **Why it is not a blocker:** It is one word, and the rest of the card reads, so under this run's rule the card
     counts as complete.
   - **Fix:** The report should state the proportion plainly. The register type should be plain `MASC`: no
     steganography was found on this card, so `MASC + Steganography` does not apply.
5. **(minor) Address street name.**
   - **Evidence:** In review/work/rcpt.png the street could be read "Weidmanngasse" or "Weidmannsgasse".
     Weidmanngasse is a real street in Wien-Hernals (XVII).
   - **Status:** The solver marked it (?). That is fine, and nothing needs to change.

## What I could not verify

- The parenthetical word: its overwritten signs 3–5 cannot be resolved from the scan.
- Anything that might be written under the stamp.
- The exact names in plain script: the recipient's surname (P?ell/Pöll), the T/J initial of "Toni", and the
  sender's note "J. Kraus, XVIII., Schulgasse 9". These are uncertain Kurrent readings and are already disclosed.
- Whether the writer of this card is the same person as on hcp-1194/1195 (Tepl, 1900, to Schönfelder). The
  alphabet is the same family, but the recipient and the city are different.
