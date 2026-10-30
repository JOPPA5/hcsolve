# HCP 1356 (pc_hcp_37): a shift-by-one love postcard from Wimborne to Chudleigh

Human solver: Tomáš Pavuk

**Status: enciphered message read in full (62 letters, 2 of them restored under ink blots); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1356 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1356), portal name pc_hcp_37, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-03-25, language Unknown, sender Unknown, recipient "W. Abboú" (a catalogue misspelling of Abbott). No transcription or solution was attached. No published solution of this card was found or used.

The picture side is a printed colour view, "Wick Ferry, Christchurch", Valentine's series (J.V. 46288), with no handwriting. The address side has a halfpenny Edward VII stamp, the postmark WIMBORNE 10 PM MR 25 07, and the plain address Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. The farm name has an unclear second letter and is read with the help of the sister cards. The message stands beside the address, under the plain heading "Sunday 24th". In 1907, 24 March was a Sunday, the day before the postmark.

The grey A–Z disc and the building logo on both scans are an overlay added when the card was scanned. They are not part of the card.

The card belongs to a correspondence with the same recipient, town of posting and cipher as the closed cards HCP 1386–1407 in this repository. Those cards served only as parallels. Every word below was read and decoded on this card. The work on this number was done by Claude Opus 5.5, with no earlier attempt.

![Picture side: Wick Ferry, Christchurch (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![The message turned upright, enlarged 2x from the original scan: the plain heading and five enciphered lines (work/crops/message2x.png)](../work/crops/message2x.png)

## Method

The transcription is manual. The un-converted original scan (work/hires/pc_hcp_37_adr.JPG, listed in SOURCES.md) was rotated 90° counter-clockwise and read from crops at 2x to 7x. The letters are ordinary handwriting, and several words were recognisable at once as Caesar-shifted English. A single decryption shift of −1 turns the whole text into English. No per-word adjustment was needed.

One point was tested and not assumed. The first letter of `Mpwf` has three downstrokes, against two in the `N` of `Nz` and `Nboz`, so it is read as M from the sign itself, and M gives LOVE.

In review the reviewer made its own crops at 2x to 8x, typed its own transcription and decoded it with its own script. It obtained the same 60 letters and the same two blots, and only shift 1 of the 26 gave language. It also checked every letter and separator dot of all five lines against the scan.

## Key

Caesar substitution: each plaintext letter is written as the next letter of the alphabet (encrypt +1, decrypt −1). Case and the writer's dots are kept.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

`[x]` marks a letter under a blot.

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

The reading can be reproduced from the repository root with `python3 -I ciphers/hcp-1356/work/decode.py`. The command checks the hashes of the image files, decodes the transcription, tests the round trip and prints the plaintext.

## Uncertainties

1. **Two restored letters.** The `o` of `px[o]` and the `v` of `Zp[v]s` lie under ink blots, and contrast-stretched 8x crops show no letter structure in either. MY OW? DEAREST and YO?R each have one sensible completion, and a one-letter gap fits both. These letters are inferred, not read.
2. **Two partly smeared letters.** The lower half of the `s` of `Zp[v]s` is a blob, and only its top hook is clear. The final `m` of `Hjsm` is clotted. The frames YO?R and GIRL settle both. So 58 letters are clear, 2 are partly smeared and 2 are restored.
3. **`Efbsftu`, end of the word.** The `u` is cramped, a low ripple running on from the barred `t`. It is the weakest clear letter, but DEAREST is secure from the other letters.
4. **`npsojoh`, sixth letter.** This `o` has a tall exit stroke and looks like δ. No word other than MORNING fits.
5. **`Xjui`.** No clear dot stands over the `j`, and one dot stands over the `i`. The letter shapes and WITH agree.
6. **"all this morning".** The sense is elliptical. She thanks him for "all" that came this morning, presumably letters, but the card does not say. Compare HCP 1387, "Thanks very much for all".
7. **Date.** The digit after 2 has an open, 6-like form. A crossing stroke and the calendar support 4, since the 24th was a Sunday and the 26th a Tuesday. The small raised letters after it are read as plain "th". They are worn and could be taken for `ui`, which would be enciphered TH, and that would not change the sense.
8. **Punctuation and case.** Dots are transcribed as seen, and some are faint. Capitals in the English are editorial.
9. **Writer and recipient's identity.** The writer signs only as "Girl". The name of the farm rests partly on the sister cards.

## Why the reading is believed

One fixed shift gives running English for every letter read from the card, with no exceptions. Long words decode independently on this card: Efbsftu→DEAREST, uibolt→THANKS, npsojoh→MORNING. The heading day, the calendar and the postmark agree. The closing also fits the correspondence: HCP 1397 ends with LOVE FROM YOUR OWN GIRL, written in the same cipher.

## Review and what changed

An independent Claude Opus 5.5 agent tried to refute the reading and gave the verdict **ACCEPT**. It reproduced the output of the decoding command, decoded the card from its own transcription, inspected each letter and dot, checked the blots and stray marks, and confirmed the calendar and the postmark. It found no sign of a published solution.

It made two minor findings, both about disclosure, and both were fixed:

1. The partly smeared `s` of `Zp[v]s` and `m` of `Hjsm` had not been named, so "60 read directly" overstated the evidence. They are now disclosed as uncertainty 2 above.
2. The parallel from HCP 1397 had been normalised. The quotation now follows the sister card, with its line break.

No letter of the transcription or the plaintext changed. The reviewer could not verify the letters under the two blots, what "all" refers to, or who the writer was.
