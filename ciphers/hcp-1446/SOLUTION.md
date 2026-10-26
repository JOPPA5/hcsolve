# HCP1446 — full message candidate, awaiting independent review

## Method and key
Caesar shift, ciphertext A→B, B→C, … Z→A. Portal name pc_hcp_127; date1907-01-30, recipient N.F.Sawdy, sender unknown. Cipher transcription was made manually from source/address.jpg after rotation; no attached or published solution used.

## Literal output
```
THANKS VERY M UCH FOR
THE CARD YOU, SENT ME,
AND GOOD WISHES
YOURS
SINC ERELY
JOHN
```
Spacing in L TBG and RHMB DQDKX is visual grouping, not a key exception. With ordinary word spacing:

> Thanks very much for the card you sent me, and good wishes. Yours sincerely, John.

Slovak: Ďakujem veľmi pekne za pohľadnicu, ktorú si mi poslala, aj za dobré priania. S úctou, John. Gender of recipient is inferred only from visible address Miss, not the cipher.

## Reproduce
From repository root:
```
python3 ciphers/hcp-1446/work/decode.py
```
The command verifies all immutable source hashes and decodes the explicitly manual work/transcription.txt; it does not perform OCR. This makes key application reproducible while leaving image-to-letter transcription available for independent inspection. Entire alphabetic cipher is covered by one uniform shift; ordinary address, date and printed picture caption are outside cipher scope.

## Uncertainties
Signature's first glyph is read as I, giving JOHN. Its short lower serif can resemble L, whose literal alternative would be MOHN. This is disclosed and should be checked independently; the writer's identity is not established. The source's unusual punctuation/spaces remain in literal output. No other unresolved cipher letters observed. No independent reviewer has checked this candidate, and no FINAL/register entry is claimed.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-26). The reviewer read all 64 cipher letters from source/address.jpg independently and decoded them with its own script; the letters agree with work/transcription.txt exactly (64 = 64), with one shift for every letter and no other shift giving English. It found no untranscribed cipher on either side. The plaintext is unchanged.

Key, stated precisely: each plaintext letter is written as the letter before it in the alphabet (Caesar shift −1 for encryption, +1 for decryption; plain A is written Z, as in ZMC = AND and BZQC = CARD). "Ciphertext A→B" above means decryption.

1. Signature JOHN, not MOHN (minor, strengthens the claim). Accepted. In review/work/sig.png the first sign of INGM carries a dot above it (a dotted i), and its foot turns to the left, whereas this writer's L (in LTBG and LD) has a horizontal foot to the right. The first sign is therefore I and the signature JOHN; MOHN is a rejected alternative, no longer an open uncertainty. The writer's identity remains unknown.
2. Two word gaps not visible on the card (minor). Accepted. The spaces in "L TBG" (line 1) and "RHMB DQDKX" (line 5) of work/transcription.txt, and hence "M UCH" and "SINC ERELY" in the literal output, are artefacts of the solver's reading: on the reviewer's crops (row1b.png, sincerely.png) LTBG and RHMBDQDKX run evenly. The earlier remark that these gaps are "visual grouping" is superseded. The report gives the literal text as LTBG / MUCH and RHMBDQDKX / SINCERELY. The decoded letters do not change; work/transcription.txt and the command output are left as they are, so the command still prints the two internal spaces.
3. Card context not recorded (minor). Accepted. The card is addressed in plain writing to "Miss N. J. Sawdy, The Manse, Nayland" (the portal gives N. F. Sawdy; in this copperplate F and J are close, and the card looks more like J). The halfpenny Edward VII stamp is cancelled NAYLAND B JA 30 07, and a plain cursive date along the lower left edge reads "Jan 30th 07". Both agree with the portal date 1907-01-30, a Wednesday. Nayland is in Suffolk, England, which fits the portal location Europe and the printer's imprint "P.P. & P. Co. Croydon". The picture side shows the Great Wheel at Earls Court, London, with only the printed caption. These details are in the report; source/metadata.md is unchanged.
4. Protocol (minor). Acknowledged. The mtimes of source/ and work/ are later than DONE1, so a file was added to or removed from those directories after the marker; the image hashes in work/source-sha256.json still match and the decoded text is unaffected. No watcher was started during solving, at the user's instruction.

Additional note from the closing pass: the signature ends with a full stop (INGM.), which the transcription omits; punctuation only.

Remaining uncertainties carried into the report: the identity of John and of the recipient (second initial F or J); the gender wording of the Slovak translation ("si mi poslala") rests on "Miss" in the plain address, not on the cipher; no search for a prior publication was made beyond the portal status, skip.txt and the AI Decipherment Register snapshot.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
