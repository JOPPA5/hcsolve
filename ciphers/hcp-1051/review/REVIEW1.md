ACCEPT

# Review 1 – hcp-1051 (Fritz Lehmann, Schweidnitz 31.3.1910) – reviewer Claude Opus 5.5, 2026-11-03

## What I verified and how

1. Ran the command from SOLUTION.md (`python3 -I ciphers/hcp-1051/work/decode.py`): all four SHA-256 checks OK; output
   `LIEBER FRITZ ICH KOMME HEUT WIEDER EIN BISCHEN ZZ DIR WEN ES RECHT IST HERZ LIEN GRUS U KUS DEINE MINNA`,
   identical to the claimed literal plaintext.
2. Transcribed the whole 9-line block myself from the hi-res original (crops made with review/work/crop.py:
   review/work/r1_3.png, r4_6.png, r7_9.png, and 30–60x zooms fritz.png, fritz3.png, heut.png, zu.png, herzlien.png).
   My reading is number-for-number identical to work/transcription.txt.
3. Decoded my own transcription with an independent script (review/work/my_decode.py, A=2 … Z=26 without J). Output is
   the same as the solver's. All numbers fall in the table; distinct set {2..15,18,19,20,21,23,26}, as the solver says.
4. Key: the same table as the reviewed Lehmann sister cards hcp-1113 and hcp-1134 (same recipient). On this card it
   fits every group, and the text reads as fluent colloquial German, so the key stands for this card on its own too.
5. Checked the disputed signs on the pixels:
   - FRITZ, third group (fritz3.png): "1" plus a small open loop with no crossing stroke. That is this writer's 0;
     the 8 in the group before it is clearly crossed. So 10 = I, as the solver reads it (not disclosed, but correct).
   - HEUT, last group (heut.png): a clear 2, then a rising stroke cut by the printed vertical divider. It fits the
     writer's open 0. 20 = T is a disclosed restoration based on word sense. Accepted.
   - "26.26" (zu.png): both groups are clearly 2+6. Literally ZZ. The solver discloses ZU as a writer slip. Agreed.
   - "9.6.18.26 . 12.10.6.14" (herzlien.png): the 1 of 12 is retraced in heavy ink, and there is no dash. Literally
     HERZ LIEN. Reading it as "Herzlein" is disclosed as word sense. Plausible.
   - Line 1, "6.3" written close together: 6 and 3 are both distinct. LIEBER is fine.
6. Stamp and picture side: the stamp is still affixed and I see no ink at its edges (review/work/stamp.png). The picture
   side carries only printed captions and the publisher number. The red dots on the dress are part of the hand-tinting
   pattern: they are spread evenly over the lace and do not form letters.
7. Plaintext: "Lieber Fritz! Ich komme heut wieder ein bisschen zu dir, wenn es recht ist, Herzlein. Gruß u. Kuss, deine
   Minna." It is natural 1910 German. The non-standard spellings (bischen, wen, Grus, Kus) are typical of a semi-literate
   writer. The English and Slovak translations are correct.
8. Sources: the portal status is Not solved and nothing is attached. The solver's web search found nothing, and I have
   no evidence of an undisclosed published solution.

## Findings

1. (minor) SOLUTION.md, "Why I believe it is correct", says "55 numbers". The transcription actually has 83 numbers
   (count from review/work/my_decode.py). Correct the count.
2. (minor) The 10 in FRITZ (line 1) resembles 18 at low zoom. The pixels support 10, but the call could be listed
   among the sign checks for completeness.
3. (minor) The address street ("Bögen...straße(?) No 6") is read only loosely. It is a single word, outside the cipher,
   and disclosed, so it does not make the card partial. A firmer reading in the report would be welcome but is not
   required.
4. (minor) The signature is MINNA, while sisters hcp-1113 and hcp-1134 are signed SUSI. The solver discloses this
   correctly. The report should not merge the two writers.

Register type: MASC (number substitution). No steganography found, so "MASC + Steganography" does not apply on these
scans.

## What I could not verify

- Whether anything is written under the affixed stamp (not visible on the scans).
- Who Minna is, and the exact street name in the address.
