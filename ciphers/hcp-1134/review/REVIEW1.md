ACCEPT

# Review 1 – hcp-1134 (Fritz Lehmann, Freiburg i. Schl. 11.3.1910)

Reviewer: Claude Opus 5.5, 2026-11-03. Solver round 1: Claude Opus 5.5.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1134/work/decode.py` (from repo root): three SHA-256 checks OK, output
   `LIEBES SCHÄTZCHEN / SENDE DIER DIE / BESTEN GRÜSZE / DEINEN WUNSCH / FÜR SONNTAG / KANN ICH NICHT / ERFÜLLEN / SUSI`,
   identical to the claimed plaintext.
2. **Independent decryption.** `python3 -I ciphers/hcp-1134/review/work/indep_decode.py` – my own script with the numbers
   I re-read from the scan (not the solver's transcription file) and the J-less alphabet A=2 … Z=26, `"` = umlaut. Output is
   identical, letter for letter. 86 numbers, values used {2,3,4,5,6,7,8,9,10,11,12,14,15,18,19,20,21,23,26}; every one maps under
   the single table, no leftover sign.
3. **Transcription vs. scan.** Rotated crops of the hi-res address scan (`review/work/all.png`, `top.png`, `bot.png`,
   `l1tail.png`, `w.png`, made with `review/work/crop.py`). I read every number of all 8 rows; all agree with
   `work/transcription.txt`, including the line-1 tail `…20.26.4.9.6.14` (SCHÄTZCHEN, umlaut over the 2), the umlaut over 21 in
   GRÜSZE and ERFÜLLEN, `9.20` at the end of row 6 (NICHT), and the signature `19.21.19.10`.
4. **Key sanity.** The key is a trivial, natural numbering (alphabet without J, starting at 2), not something fitted to the text;
   the first two words fix it and the remaining ~70 numbers follow with no adjustment. Plaintext is fluent period German
   ("Liebes Schätzchen! Sende dir die besten Grüße. Deinen Wunsch für Sonntag kann ich nicht erfüllen. Susi."). It fits a love note
   to a young man; the sister cards in this run that use the same key reuse this card as their key source.
5. **Steganography / hidden writing.** Checked the stamp area (`review/work/stamp.png`) and the whole picture side
   (`review/work/pic_half.png`): no writing on the picture side beyond the printed caption and the HCPortal watermark; the stamp is
   still affixed and no ink is visible at its perforated edges. Nothing under the stamp can be inspected from these scans – correctly
   disclosed by the solver.

## Findings

1. **minor – overwritten W numeral.** Row 4, first number (`w.png`): a 22 with a second stroke group forming a 3 over the last
   digit. I see both layers too; the solver's reading 23 = W (WUNSCH) is the only one that gives a word, and it is disclosed as resting
   on word sense. No change needed beyond what is written.
2. **minor – wrong count in "Why I believe it is correct".** SOLUTION.md says "8 lines (61 numbers)"; the transcription holds 86
   numbers (my script counts them). Cosmetic; fix the figure in SOLUTION/report.
3. **minor – umlaut on FÜR.** The only `″` near FÜR sits under the 10/14 of row 4 rather than over 21 of row 5. The solver's
   attribution is reasonable and disclosed; it does not change the reading (FUR/FÜR).
4. **minor – published-solution check.** The portal links the HistoCrypt article on the Schrödel collection
   (ecp.ep.liu.se/…/166). The solver reports one web search with no find but does not say whether that article was consulted; it may
   discuss the Lehmann card family. The report should state whether it was checked, and credit it if it shows this alphabet.

## Register

Type label `MASC` is appropriate (number substitution); no steganographic part was found on the inspectable surfaces, so
`MASC + Steganography` is not warranted for this card.

## What I could not verify

- Whatever might lie under the still-affixed stamp.
- The contents of the HistoCrypt article (not opened in this review).
- The identity of "Susi" and the street name in the plain address (not part of the cipher).
