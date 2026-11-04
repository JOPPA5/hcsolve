ACCEPT

# Review 1 – hcp-1077 (cpc_1908-01-10_DE_Fechenheim)

Reviewer: Claude Opus 5.5, 2026-11-03.

## What I verified and how

1. Ran the solver's command from the repo root:

       python3 -I ciphers/hcp-1077/work/decode.py

   Output: three SHA-256 checks OK, then "Herzlichen Gruss sendet" / "LUDWIG KALBHENN" – identical to the plaintext claimed in SOLUTION.md.

2. Independent decode (review/work/indep_decode.py) from my own reading of the digits, under three alphabets:

       A=1..Z=26 with J     KTDVIG JAKBHEMM
       no J (I=J)           LUDWIG KALBHENN
       no J, no V (U=V)     LUDXIG KALBHENN

   Only the 25-letter alphabet without J (U and V separate) gives language, and it gives it on both lines with one fixed key and no exceptions. All 14 groups are covered; there is no other ciphertext on the card. The same script tries alternatives for the weak sign in line 2, position 6 (1, 3, 5, 6, 8 → KALBHANN, KALBHCNN, KALBHENN, KALBHFNN, KALBHHNN); only 5 gives an attested surname.

3. Transcription checked against work/hires/..._pic.jpg (3468x2298 original), with my own 3–8x crops in review/work/:
   - l1a.png / l1b.png (line 1): 11 . 20 . 4 . 22 . 9 . 7 – the 11 is clear; the 2 of 20 is clear and the 0 is a heavily inked, overwritten oval but is a closed loop; the 4 is the hooked German form; 22 is two identical 2s; 9 clear; 7 has the continental crossbar. I agree with every digit.
   - l2a.png / l2b.png (line 2): 10 . 1 . 11 . 2 . 8 . ? . 13 . 13 – all clear except position 6.
   - five.png (position 6, autocontrast, 8x): a heavy blob at the bottom left, a thin curved stroke rising to the right, and a faint continuation toward a dark tick at the upper right which may be the flag of the 5 or the start of the following 1. The shape is compatible with a hand-written 5 but not decisive on the pixels alone. The solver disclosed this as the weakest call resting partly on word sense; I agree with that description.
   - greet.png: "Herzlichen Gruß sendet" in Kurrent – confirmed.
   - name.png (address side): the recipient surname reads D-i-e-h-l in Kurrent ("Gerda Diehl."), not the portal's "Vinth ?" – I agree with the solver. "Fechenheim, Jubiläumstr. No 18" and the postmark FECHENHEIM 10.1.08 also confirmed on the overview.
   - flourish.png / flourish2.png: the paraph below the numbers.

4. Steganography / hidden writing: I looked at the stamp box, the picture and the edges on both sides. The 5-Pf Germania stamp is on the address side, firmly cancelled; nothing protrudes from under it and the scan cannot show the area beneath it. No other writing in the picture or along the edges.

5. Sources: SOURCES.md and SOLUTION.md say no published solution was found; the portal has none attached (status Not solved). Nothing indicates a published solution was used.

6. Language/context: "Herzlichen Gruß sendet <name>" is a standard German postcard formula of the period; enciphering only the sender's name in A=1… numbers (school alphabet without J) is typical for these cards. Ludwig is a common Hessian first name; Kalbhenn is an attested Hessian surname. Fechenheim (near Hanau, where the card was printed) fits.

## Findings

1. (minor) Position 6 of line 2 ("5" = E) is not legible as a digit on the pixels alone; it rests on word sense. Disclosed correctly in SOLUTION.md (uncertainty 3); the report should keep that wording and say that 1, 3, 6 and 8 in that slot give no name.

2. (minor) The flourish below the numbers begins with a dark, heavy hook in the same dark ink as the digits (top of flourish2.png) and ends with a small dot near its foot. It does not have the dot-separated form of the number groups and I read it as a paraph (possibly an L K monogram), as the solver does, but SOLUTION.md should describe this dark hook explicitly and state why it is not a further cipher group (e.g. "2." = B), so a reader of the report does not wonder about it.

3. (minor) Recipient surname: the Kurrent reading Diehl differs from the portal's "Vinth ?". The reading looks correct to me, but it is a plain-text reading; the report should say that the portal metadata is wrong or uncertain here rather than silently replacing it.

4. (minor) Type label for the register: number substitution with a fixed alphabet is a MASC; "MASC" is the correct allowed label. No steganography was found on this card, so "MASC + Steganography" should not be used.

## What I could not verify

- Whether anything is written under the stamp (scan only).
- That a Ludwig Kalbhenn lived in or near Fechenheim in 1908.
- The exact identity of the weak digit in line 2, position 6, beyond word sense.
