# HCP 1382 / pc_hcp_63 — Caesar +1 love postcard to W. Abbott, 24 Sep 1907

**Status: whole enciphered text read (40 letters, one key). Review 1 verdict ACCEPT; its five minor findings are addressed below.** Residual points are small and listed under Uncertainties; the largest is one word of *plain* writing ("Dear") that is only probable. All work is by Claude Opus 5.5 on 2026-10-30; there is no earlier work on this number. No published solution of this card was found, and the portal attaches none (status Not solved).

## Source and context
Portal 1382, `pc_hcp_63`, date 1907-09-24, recipient "W. Abboú" (a catalogue misreading of Abbott). Picture side: printed view "Christchurch Priory. Norman Turret." no. 23241, no handwriting (a small dark blob with two rings and short strokes in the sky at lower left looks like set-off from a postmark; it holds no message text and is set aside). Address side: halfpenny Edward VII stamp, postmark BOURNEMOUTH 12.45 PM SP 24 07; address **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon** (plain). Christchurch is next to Bournemouth, so the view fits the postmark. The circular A–Z disc on the scans is an overlay, not part of the card. Writing is on the left half, read after rotating the card 90° counter-clockwise (`work/crops/rot.png`). Same recipient, key and closing formula as the W. Abbott run (e.g. hcp-1386, 1387, 1402).

## Cipher and key
Caesar shift: each plaintext letter is written as the next letter of the alphabet (decrypt −1, Z after A). Case and dots kept. Only the second half of the message is enciphered; the card opens in plain English.
```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext
| Row | On the card | Reading |
|---|---|---|
| 1 | Tues. Morning G. H. | plain writing |
| 2 | I am enjoying | plain writing |
| 3 | myself Dear[?] | plain writing |
| 4 | pomz. Xjti zpv. | only. Wish you. |
| 5 | Xfsf Ifsf. bt. | Were Here. as. |
| 6 | Xfmm. M-L. Gspn | Well. M-L. From |
| 7 | Zpvs Pxo E.L. Hjsm | Your Own E.L. Girl |
| 8 | 24th Sep 07 | plain writing |

**English (original language, punctuation editorial):** "Tuesday morning. G. H. I am enjoying myself, Dear [probable]. Only wish you were here as well. M-L. From your own E.L. girl. 24th Sep 07."

**Slovak:** „Utorok ráno. G. H. Dobre sa bavím, drahý [pravdepodobné]. Len by som si želala, aby si tu bol aj ty. M-L. Od tvojho vlastného E.L. dievčaťa. 24. sept. 07."

(The source language is English, so the English line above is also the English translation.)

## Reproduce
From the repository root:
```
python3 -I ciphers/hcp-1382/work/decode.py
```
It checks the SHA-256 of all four image files, decodes the manual transcription and confirms the weekday. Enlarged and overlay-flattened crops are in `work/crops/` (`norm.png` divides out the overlay bands; scripts `mk*.py`).

## Uncertainties
1. **"Dear" (row 3, plain writing, not enciphered).** Faint and crossed by the overlay band. A large initial and about three low letters with no ascender are visible; D-e-a-r fits and the enciphered form Efbs does not (no tall f). Treat as probable, not certain.
2. **`M-L.` and `E.L.` are kept literal.** They look like abbreviations, as on the sister cards; `M-L.` is the form read on hcp-1383, written the day before from the same town. Their meaning is not established, and it remains open whether either is enciphered: `M-L.` shifted gives L-K, and hcp-1395 reads `M. & L.` as `L. & K.`, probably "love & kisses", which would fit here before "from" (not proved on this card, and the joining sign here is a dash). `E.L.` shifted gives D.K, and the sister form `E.h` gives D.g; neither means anything evident. In `M-L.` the first sign has three feet, so M; part of its top is tangled with the descender of the f of `Ifsf.`, so N is not wholly excluded. The second letter of `E.L.` has a small foot and could be the h recorded as `E.h` on hcp-1387; L and h cannot be separated here.
3. **Letters under the overlay.** The z of `zpv.` lies under the printed R and the band. It is read as z from its shape: the two strokes of its top and foot are visible. Separately, the sense "you" would need that letter. The z of `pomz` lies on the band but is clear.
4. **`Xjti`.** Stems of j and t are clear and the t has the same detached bar as the t of `bt.`; the i is a low hump. A small heavy mark above the i stands where its dot belongs and is probably that dot.
5. **Dots** are transcribed as seen and sit mid-sentence ("bt." before "Xfmm"), as usual in this hand. The X of `Xjti`, `Xfsf`, `Xfmm` is a capital, not a kiss mark; it is detached from the next letter in all three. The first letter of `Ifsf` is a capital I with a loop, joined to the next letter.
6. **"G. H."** at the end of row 1 is read from flourished plain writing and matches the heading on the sister cards. G and C cannot be separated here.

## Why it is correct
- One fixed shift turns all 40 enciphered letters into ordinary English, with no exceptions. Sense was used only to choose among shapes already seen, and only `zpv` lies under the overlay; its shape supports z without the sense argument.
- Key and groups agree with independently closed sister cards: `pomz` = ONLY (hcp-1383), `Gspn`, `Zpvs`, `Pxo`, `Hjsm` (hcp-1386). These were hypotheses here and each was read on this card's pixels.
- `Xjti zpv Xfsf Ifsf bt Xfmm` was not expected in advance: it emerged from letter shapes, and the repeated f-s-f pattern in row 5 and the double m in row 6 agree with it.
- The plain opening and the cipher continue one sentence ("I am enjoying myself … only wish you were here as well"), which fits a holiday card from Bournemouth.
- 24 Sep 1907 was a Tuesday, matching "Tues." and the postmark date.

## Response to review 1
Review verdict ACCEPT. All five findings were re-examined on the scan (reviewer crops `z_N.png`, `r5b.png`, `z_addr.png`, `z_picmark.png`) and accepted. No deciphered letter changed; the count stays 40. `python3 -I ciphers/hcp-1382/work/decode.py` was re-run after the changes.

1. **`N-L.` is `M-L.` — fixed.** The sign has three feet: a long diagonal, a second foot after the arch, and a separate short third stroke. The feet are clear of the f descender that tangles its top. Changed in `work/decode.py`, the table, the English and Slovak lines and uncertainty 2 (the appeal to hcp-1402 is removed).
2. **Dot after `Ifsf` — fixed.** A clear dot stands on the line before `bt.`. Row 5 is now `Xfsf Ifsf. bt.` in the table and in `work/decode.py`. The editorial English punctuation does not change, since dots in this hand fall mid-sentence (uncertainty 5).
3. **Address "S." — fixed.** The large stroke before `Devon` is an S; the address now reads S. Devon. It has no effect on the reading.
4. **Picture-side mark — fixed.** It was seen and is set aside under Source and context as probable postmark set-off, not message text. Its origin is not proved.
5. **Wording — fixed.** The shape evidence for the z of `zpv` is now separated from the sense argument in uncertainty 3 and under "Why it is correct". Uncertainty 2 now says it is open whether `M-L.` and `E.L.` are enciphered at all, and gives the shifted forms.

In addition, uncertainty 4 now follows the review's reading of the mark above the i of `Xjti` as probably its dot, and uncertainty 6 records that G and C cannot be separated in the heading.
