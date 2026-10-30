# HCP 1356 / pc_hcp_37 — Caesar −1 English love postcard, 24–25 March 1907

**Status: complete reading of the enciphered message (62 letters). Two letters lie under ink blots and are disclosed restorations.** Solver: Claude Opus 5.5, 2026-10-30. There is no earlier work on this number.

## Source and context

Portal record https://crypto.hcportal.eu/dashboard/cryptograms/1356 (`pc_hcp_37`), status Not solved, date 1907-03-25, language Unknown, recipient field "W. Abboú" (a catalogue misspelling of Abbott). No transcription or solution is attached (see `SOURCES.md`, `source/metadata.md`). No published solution of this card was found or used; the orchestrator's check of the AI register on 2026-10-30 found no record.

- Picture side: printed colour view "Wick Ferry, Christchurch", Valentine's (J.V. 46288), no handwriting.
- Address side: halfpenny Edward VII stamp, postmark WIMBORNE 10 PM MR 25 07. Plain address: Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. The farm name is spelled with an unclear second letter and is read with the sister cards.
- Plain heading: "Sunday 24th". 24 March 1907 was a Sunday, the day before the postmark.
- The grey A–Z disc and building logo on both scans are an overlay of the scan, not part of the card.

Same recipient, postmark town and key as the closed cards hcp-1386…1407. Each word below was read and decoded on this card; sister cards served only as a parallel for the closing formula (hcp-1397 has `wjfx. Mpwf gspn / Zpvs. Pxo Hjsm.` in its SOLUTION.md table; its reviewed transcription has `wjfx Mpwf gspn / zpvs. Pxo. Hjsm.`, that is LOVE FROM YOUR OWN GIRL).

## Cipher and key

Caesar substitution: each plaintext letter is written as the **next** letter of the alphabet (encrypt +1, decrypt −1). Case and the writer's dots are kept.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext

`[x]` marks a letter under a blot. All other letters were read, two of them only in part (uncertainty 9), from enlarged crops of `work/hires/pc_hcp_37_adr.JPG` rotated 90° counter-clockwise (`work/crops.py`, `work/crops2.py`, `work/crops3.py`).

| Ciphertext | Plaintext |
|---|---|
| *(plain)* Sunday 24th | Sunday 24th |
| Nz. px[o]. Efbsftu. Cpz | My. ow[n]. Dearest. Boy |
| Nboz. uibolt gps. | Many. thanks for. |
| bmm. uijt npsojoh | all. this morning |
| Xjui Mpwf. Gspn | With Love. From |
| Zp[v]s. Hjsm | Yo[u]r. Girl |

**English (original; punctuation editorial):** "Sunday 24th. My own dearest boy, many thanks for all this morning. With love from your girl."

**Slovak:** „Nedeľa 24. Môj vlastný najdrahší chlapče, veľmi pekne ďakujem za všetko dnes ráno. S láskou od tvojho dievčaťa.“


## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1356/work/decode.py
```

It checks the SHA-256 of the four image files, decodes `work/transcription.txt`, tests the round trip and prints the letter count and the plaintext.

## Uncertainties

1. **Restoration, `px[o]`.** After `px` there is an o-sized ink blot, then a separate dot. No letter shape can be seen in it. OWN is the only word that fits `MY OW? DEAREST`.
2. **Restoration, `Zp[v]s`.** Between `Zp` and `s` there is a blot of one letter's width. `YO?R` gives YOUR as the only fitting word.
3. **`Efbsftu`, end of the word.** The `u` is cramped: a low ripple running on from the barred `t`. Its two strokes are small and could be taken for a tail of `t`. The word DEAREST is secure from the other letters; the `u` is the weakest letter read directly.
4. **`npsojoh`, sixth letter.** This `o` has a tall exit stroke and looks like δ. MORNING fits, and no other word fits the frame.
5. **`Xjui`.** No clear dot stands over the `j`; one dot stands over the `i`. The letter shapes and WITH agree.
6. **"all this morning".** The sense is elliptical: she thanks him for "all" that came this morning, presumably letters. The letters are certain; what "all" refers to is not stated. Compare hcp-1387 "Thanks very much for all".
7. **Date.** The digit after 2 has an open, 6-like form, but its crossing stroke and the calendar support 4: the 24th was a Sunday, the 26th a Tuesday. The small raised letters after it are read as plain "th"; they are worn and could be taken for `ui` (enciphered TH). This changes nothing in the sense.
8. **Punctuation and word case.** Dots are transcribed as seen; some are faint. Capitals in the English are editorial.
9. **Two partly smeared letters.** Of the 60 letters read, 58 are clear and 2 are read only in part. The `s` of `Zp[v]s` keeps its top hook; its lower half is a blob. The final `m` of `Hjsm` is clotted, so its strokes cannot be counted. The frames YO?R and GIRL settle both, but neither letter is independent evidence.

## Why it is correct

- One fixed shift turns all 60 letters read from the card (58 clear, 2 partly smeared) into running English, with no exception and no per-word adjustment.
- Long words that decode independently on this card: Efbsftu→DEAREST, uibolt→THANKS, npsojoh→MORNING, Gspn→FROM, Hjsm→GIRL.
- The first letter of `Mpwf` has three downstrokes, against two in the `N` of `Nz` and `Nboz`, so M (LOVE) is read from the sign itself and is not assumed from the formula.
- The heading day, the calendar and the postmark agree. Recipient, town of posting, key and formula agree with the closed cards of this correspondence.

## Response to review 1

Verdict ACCEPT, two minor findings, both disclosure points. The reading and `work/transcription.txt` are unchanged. `python3 -I ciphers/hcp-1356/work/decode.py` was re-run after the edits: 4 hashes OK, round trip OK, same plaintext. Its "60 read from the pixels" means not restored, and that is still true; the split into 58 clear and 2 partial is in uncertainty 9.

1. **Smeared `s` of `Zp[v]s` and final `m` of `Hjsm`: fixed.** I checked `review/work/blot2.png` and `review/work/hjsm.png` and agree. Uncertainty 9 is added, and "Why it is correct" no longer implies that all 60 letters are clear.
2. **Normalised hcp-1397 parallel: fixed.** The quote now gives the sister card's text with its line break, and notes that its SOLUTION.md table and its reviewed transcription differ in case and dots. The reading of this card does not rest on it.
