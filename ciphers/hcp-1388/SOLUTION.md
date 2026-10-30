# HCP 1388 / pc_hcp_69 — solution (round 1)

**Status (2026-10-30, after review 1):** complete reading of all 51 cipher letters on the card. One residual: two dark non-alphabetic marks on line 3, reported literally. Review 1 verdict ACCEPT (four minor findings, addressed below in "Response to review 1"; no cipher letter changed).

## Source and context

HC Portal cryptogram 1388 ("pc_hcp_69"). Status on the portal: Not solved. No transcription or solution is attached (see SOURCES.md, source/metadata.md). The postcard is a Frith's Series view captioned "Nottingham Castle"; the picture side has no handwriting. The address side carries a halfpenny Edward VII stamp postmarked "…MBORNE / 10 PM / AP 15 / [0]7" (year digits faint). The plain address reads Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (portal recipient field: "W. Abboú"). The plain heading reads "G. H. Monday" (C. H. not excluded; the first initial has an open top and an inward bar, like the G preferred on the sister card hcp-1397). The plain date is "April 15th 1907", which agrees with the portal date 1907-04-15 (a Monday). The four lines between the heading and the date are enciphered.

This is one card in the run of postcards to W. Abbott (hcp-1386 … 1407, 1907–08) that use the same cipher. The accepted sister card hcp-1397 has the same key and the same closing, "Love from your own girl".

## Cipher and key

Monoalphabetic Caesar shift. Each plaintext letter is written as the **next** letter of the alphabet (encryption +1). To decrypt, subtract one:

```
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Case is kept. Dots, the dash and the [**] marks are passed through unchanged.

## Transcription and plaintext

| Cipher (manual transcription) | Plaintext |
|---|---|
| `Nz. Efbsftu. uibolt -` | My. Dearest. thanks - |
| `gps. mfuufs ju. Xbt` | for. letter it. Was |
| `gjof [**] N yy gspn` | fine [**] M xx from |
| `Zpvs. pxo. Hjsm` | Your. own. Girl |

51 cipher letters in total. One key covers all of them, with no exceptions.

**Reading (English):** "My dearest, thanks for letter, it was fine. [**] M xx from your own girl." Here xx stands for kisses.

**Slovak:** „Môj najdrahší, ďakujem za list, bol pekný. [**] M xx (bozky) od tvojho vlastného dievčaťa.“

Punctuation and capitals in the readings are editorial. The literal dots are in the table above.

## Reproduce

From the repository root:

```sh
python3 -I ciphers/hcp-1388/work/decode_full.py
```

The script checks the SHA-256 hashes of source/address.jpg, source/picture.jpg and source/metadata.md. It then decrypts `work/transcript_full.json` with the key and asserts the expected plaintext line by line. The transcription is manual, made from enlarged crops. The script does not read the image itself. The crops used are in `work/c-*.png`.

## Key readings checked on the pixels (2026-10-29)

- **Line 3, `gjof` → fine** (`work/c-l3-gjof.png`). The four letters are g, j, o and f. The j has its dot, a heavy dot above the line. This completes "it Was fine".
- **Line 3, `N yy` → M xx** (`work/c-l3-nyy-and-j-descender.png`, `work/c-l3-yy-10x.png`). The earlier "{L3-B}" group is not a word: most of its ink belongs to line 2. The long diagonal and the oval loop on its left are the descender and descender loop of the tall j of `ju` on line 2. Once that stroke is set aside, three signs are left:
  - a capital N, formed like the N of `Nz` on line 1 (a stem with a top loop and one hump);
  - a y whose top is a large open curl and whose stem runs along (and merges with) the j descender;
  - a second y, with a small top hook, a long diagonal and a foot.
  Cipher `yy` = plain **xx**, i.e. kisses. On the sister card hcp-1390 a capital followed by two y/× marks also stands before "From your own Girl". That card supports the reading **yy = xx (kisses)**; it does not by itself settle the capital, which hcp-1390 leaves undecided (enciphered or plain M). Here the capital has the same build as the cipher N of `Nz`, so cipher N → plain M is read; the parallel is consistent with this reading, not a proof of it.
- **Line 4, `Hjsm` → Girl** (`work/c-l4-hjsm.png`). The H is a slanted stroke with a crossbar plus a second short stroke, as on hcp-1390's H.
- Every other word was checked on enlarged crops: Nz, Efbsftu, uibolt, gps, mfuufs, ju, Xbt, gspn, Zpvs, pxo.

## Uncertainties

1. **[**] on line 3.** Between `gjof` and `N` there are two small, dense, star-shaped marks, in ink darker than the message. They have no letter form. They may be heavily inked crosses (kisses), blotted or cancelled letters, or later stains. They are not read and not decrypted. The earlier transcript called them "CANCELLED". That is possible, but it is not established.
2. **"M".** Cipher N = plain M. It stands alone before the kisses, as it does on hcp-1390. Its meaning is not established. It may be an initial or pet name of the writer, or an abbreviation. It is not expanded.
3. **y no. 1 in `N yy`, and the oval.** Its stem merges with the j descender from line 2. The reading y rests on its top curl, on the parallel kisses on hcp-1390, and on the meaning "xx". A closed oval at line-3 x-height, left of the long diagonal and joined to it (review/work/l3group-8x.png), is taken as the descender loop of the line-2 `j`; it could instead be a separate line-3 sign (it resembles the writer's 9-shaped g), which would make the group four signs (N ? y y). Neither the key nor the reading "M … xx" changes either way, but the exact sign count of this group is not certain. The reading c or e (`Ncy`/`Ney` → "Mbx"/"Mdx") gives no sense.
4. The plain heading initials (G. H., C. H. not excluded) and the farm name are outside the cipher. They are not claimed beyond "Stokelake Farm", the reading also given on hcp-1397.

## Why this is believed correct

- One fixed shift, the same one as on the accepted sister card hcp-1397, turns all 51 letters into English words that are natural for a 1907 lover's postcard. The text runs through its long words: Dearest, thanks, letter, fine, from, Your own Girl.
- The closing formula matches the sister cards from the same writer to the same recipient.
- The date in the message agrees with the postmark (AP 15; year faint) and with the portal date.
- No published solution was found or used. The portal status is Not solved.

## Credit

The first partial work (2026-10-26) was done by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol). It downloaded the sources, identified the shift −1, made the rotation and crops, and read lines 1, 2 and 4 plus `gspn`. Claude Opus 5.5 (2026-10-29) completed the reading: it read `gjof` → fine, separated the line-2 j descender from line 3 and read `N yy` → M xx. It also rewrote the transcription and the command. The old `work/decode.py` / `work/transcript.json` are kept as the record of the partial state.

## Response to review 1

Review 1 (Claude Opus 5.5, 2026-10-30): verdict **ACCEPT**, four minor findings, no blocker or major ones. All addressed; no cipher letter and no decrypted letter changed.

1. **hcp-1390 parallel overstated – agreed, fixed.** The current hcp-1390 SOLUTION reads the group after "to day" as a capital (plain M or enciphered → L, undecided) followed by ×× / y y. The wording under "Key readings" now says that hcp-1390 supports yy = xx (kisses) and is *consistent with*, not a confirmation of, cipher N → M. On this card N → M rests on the capital's shape, which matches the N of `Nz` (top loop, stem, one hump; review/work/l1Nz-8x.png). The report describes the two cards in these terms.
2. **Oval in the "N yy" group – agreed, added to uncertainty 3.** At 8x (review/work/l3group-8x.png) the oval sits at line-3 x-height and joins the long diagonal above its lower end; it resembles the writer's 9-shaped g. I keep it as the line-2 `j` loop, because the diagonal runs unbroken from `ju` on line 2, but a four-sign group (N ? y y) is now stated as possible. If it were a cipher g (→ f) it gives no word, so the reading "M … xx" stands.
3. **Heading initial – agreed, fixed.** On work/address-rotated.jpg the first initial has an open top and an inward bar; it is now given as "G. H." (C. H. not excluded), as on hcp-1397. Outside the cipher; not expanded.
4. **Literal "M" – no change needed** (the reviewer asks for none); it stays unexpanded and disclosed in uncertainty 2.

Reproduction re-run after these edits (only SOLUTION.md text changed; transcription and script untouched): `python3 -I ciphers/hcp-1388/work/decode_full.py` → "source hashes OK", the same four lines, "cipher letters decrypted: 51".
