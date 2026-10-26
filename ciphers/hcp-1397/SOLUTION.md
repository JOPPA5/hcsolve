# HCP 1397 / pc_hcp_78 — Caesar substitution candidate

The four encrypted lines read:

> My dearest, this one is a Scotch view. Love from your own girl.

This is a solver candidate for independent review, not an accepted/final solution.

## Source and context

Root read the rendered General, Description and Attachments tabs on 2026-10-26. Portal status was Not solved; no attached transcription or solution was displayed. Both immutable original scans were inspected by this solver. The postcard picture is captioned “Trossachs Hotel & Loch Achray.” No handwritten cipher continuation was observed on the picture side.

The address apparently reads Mr W. Abbott, Stokelake Farms, Chudleigh, Devon. The portal's preserved recipient field is W. Abboú. The message has the ordinary date April 10th 1907 and an ordinary circled signature, probably C. H. (G. H. also possible); their expansions and the sender's identity are not claimed. The date agrees with portal metadata 1907-04-10. The picture's Scottish scene is contextual agreement with SCOTCH VIEW, not a replacement for reading its encrypted letters.

No published solution was used. Root supplied a Caesar −1 hypothesis from related correspondence; it was checked against every body group in this scan.

## Method and key

The writer substitutes the next Latin letter for each plaintext letter. Decryption subtracts one, wrapping A to Z:

```
Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain:  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The full manual visual transcript and its literal decryption are:

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Efbsftu uijt | MY. DEAREST THIS |
| pof. jt b. Tdpu di | ONE. IS A. SCOT CH |
| wjfx. Mpwf gspn | VIEW. LOVE FROM |
| Zpvs. Pxo Hjsm. | YOUR. OWN GIRL. |

All **48 encrypted letters** are covered by this single key; there are no unknown cipher letters in the proposed transcript. The writing gap inside Tdpu di is preserved literally as SCOT CH, then joined editorially as SCOTCH in the normal reading. No letters are inserted by this join. Frequent writer's dots are retained in the literal output; punctuation in the readable English sentence is editorial.

The strong checks include Efbsftu→DEAREST, Tdpu di→SCOT CH, wjfx→VIEW, Mpwf→LOVE and gspn→FROM. Together they establish a coherent whole-message reading rather than an isolated greeting match.

## Translation

> Môj najdrahší, táto pohľadnica zobrazuje Škótsko. S láskou, tvoje dievča.

The source's literal “a Scotch view” is a view of Scotland. The translation adds “pohľadnica” only to explain “this one,” not as a deciphered word. The gendered closing follows GIRL; no personal identity is inferred.

## Reproduction and scope

Run from the repository root:

```
python3 ciphers/hcp-1397/work/decode.py
```

The script checks the SHA-256 hashes of every original source file, reads the frozen manual transcript in `work/transcript.json`, applies the key, verifies exact encipherment round trips, prints the four literal lines, and derives the joined reading from those outputs. It also prints the ordinary date and signature without shifting them.

This is a reproducible **manual-transcript decryption**, not OCR or an automatic image-to-text claim. The key cannot independently validate whether the human-readable cursive transcription matches the scan; that is a required visual check for independent review. Working row crops are supplied to make that check easy. Original source files are unchanged.

## Uncertainty and exclusions

- Capital T and M are ornate; the proposed readings were checked against the original and individual row crops. The complete ciphertext proposed for review is explicit above.
- Spacing and dots are manual visual readings; the only merged word is the stated SCOT CH/SCOTCH join.
- Date, circled C. H., ordinary address, postmark, stamp and printed caption are outside the four encrypted lines. They are not blindly shifted under the cipher key.
- No expansion of the circled [C/G]. H., dating beyond the written/portal date, sender attribution or identity claim is made.
- No review verdict, PDF report, register entry or FINAL is claimed. No watcher/reviewer was launched, following the persistent user override.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-27). The reviewer ran the command above, read all 48 cipher letters from source/address.jpg independently and decoded them with its own script (review/work/my_decode.py); its letters agree with work/transcript.json exactly (48 = 48), one shift covers every letter, and it found no untranscribed cipher on either side. The plaintext is unchanged.

Key, stated precisely: each plaintext letter is written as the letter after it in the alphabet (Caesar shift +1 for encryption, −1 for decryption; plain Z would be written A, which does not occur on this card). "Caesar −1" above refers to the decryption direction. The register entry uses the encryption direction, "Caesar (shift +1)", because the earlier entries "Caesar (shift −1)" in this repository (hcp-1446, hcp-1471) denote cards whose writers wrote the letter before; using the same label here would describe the opposite key.

1. Transcription details that do not affect any letter (minor). Accepted.
   - (a) The line-2 word is one continuous cursive word written with an ordinary lowercase t, tdpudi (review/work/z-tdpudi.png; checked again in the closing pass), not "Tdpu di". The remarks above about a "writing gap" and an editorial join SCOT CH → SCOTCH are superseded: SCOTCH is the literal reading, and no join is needed. work/transcript.json and the command output are left as they are, so the command still prints "SCOT CH"; the letters are the same.
   - (b) Punctuation and case follow the reviewer's reading in the report: `Nz. Efbsftu uijt / pof. jt.b. tdpudi / wjfx Mpwf gspn / zpvs. Pxo. Hjsm.` (a dot after jt as well as after b, none after wjfx, a dot after Pxo, and lowercase z in zpvs). Punctuation and capitals remain editorial in the English sentence.
2. Circled initials more likely G. H. than C. H. (minor). Accepted as a stated preference. In review/work/z-sig.png the first initial has a descending tail that turns back at the baseline, like this writer's G; the report gives "G. H. (C. H. not excluded)". The initials are not expanded and are not shifted, and the sender's identity is not claimed.
3. Context not used (minor). Accepted.
   - The halfpenny Edward VII stamp is cancelled `…ORNE / 7 PM / AP 10 / 07` (review/work/z-postmark.png): this agrees with the written date "April 10th 1907" and the portal date 1907-04-10, a Wednesday. Only the last letters of the office name are legible; it is an English office, so the card was posted in England, and "this one is a Scotch view" refers to the picture (a Frith's Series view, "Trossachs Hotel & Loch Achray", in the Scottish Trossachs), not to where the sender was.
   - The "related correspondence" from which the root's −1 hypothesis came is the run of HC Portal records addressed to the same recipient (portal recipient field "W. Abboú"): records 1386–1398 and 1401–1407 (pc_hcp_67 to pc_hcp_79 and pc_hcp_82 to pc_hcp_88), dated 1907–1908, which have their own working directories in this repository. Which of these the root actually used was not recorded; none of them is closed, so they are cited as context only. SOURCES.md is not changed after the review; this section and the report carry the reference. The key is verified on this card alone.
4. Translation in Slovak only (minor). Accepted. The report states that the plaintext's language is English (the portal lists the language as Unknown), gives the English sentence, and keeps the Slovak translation alongside.

Additional notes from the closing pass:
- The circular alphabet disc visible on both scans (A–Z around an outer ring, a building in the centre) lies in the same position on both sides; it is an overlay on the scans, not part of the card, and it is not cipher text.
- Metadata: the portal recipient "W. Abboú" is the plain address "Mr W. Abbott, Stokelake Farm(s), Chudleigh, Devon" misread; the portal language "Unknown" is English. These corrections are recorded here and in the report only; source/metadata.md is unchanged.

Remaining uncertainties carried into the report: the sender's identity and the expansion of the initials (G or C); the full postmark office name; no search for a prior publication was made beyond the portal status (Not solved), skip.txt and the absence of an attached solution.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-27.
