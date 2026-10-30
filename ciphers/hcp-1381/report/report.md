# HCP 1381 (pc_hcp_62): an English Caesar sweetheart postcard from Bournemouth, 26 September 1907

Human solver: Tomáš Pavuk

**Status: whole message read (67 enciphered letters, 6 abbreviation letters kept literal); one letter is a restoration and several words are weak because the pencil is very faint. Independent review 1 verdict REVISE; its findings are addressed, and one word of the first reading was corrected.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1381 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1381), portal name pc_hcp_62, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-09-26, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached.

The picture side is a printed view, "Old Harry Rocks near Bournemouth", with no handwriting. The address side has a halfpenny Edward VII stamp and the postmark **BOURNEMOUTH 4.30 PM SP 26 07**. It is addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon**; the portal's "Abboú" is a misreading of Abbott. 26 September 1907 was a Thursday, which agrees with the plain heading "Hotel Thursday" and the plain foot "Sep. 26th 07".

The message is in pencil on the left half of the address side, written sideways. It is very faint, and the portal's cipher-wheel watermark lies over part of it on the scan. The card belongs to a correspondence of Caesar-shifted English cards from one couple in 1907–08, sent to W. Abbott at Stokelake Farm (for example HC Portal 1382, 1383, 1386–1407). HCP 1382 and 1383 come from the same stay in Bournemouth, a few days earlier.

No published solution of this card was found or used.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned: postmark, address and the sideways pencil message (source/address-large.jpg)](../source/address-large.jpg)

![The message turned upright, under the portal's watermark disc (work/crops/full_rot.png)](../work/crops/full_rot.png)

## Method

The transcription is manual. The scan was turned upright, enhanced (red-channel stretch and autocontrast worked best) and read word by word from enlarged crops of the un-converted original, which is itself only 1785 × 1175 pixels. The shift was taken as a hypothesis from the sister cards and tested on this card's own clearest words: `Kvtu` gives JUST, `mpwfmz` LOVELY, `xfbuifs` WEATHER and `zpvs` YOUR. A short script (work/decode.py) then checks the image hashes and decodes every token of work/transcription.json.

In review, a separate Claude Opus 5.5 agent made its own enlargements, examined the card sign by sign and decoded with its own table and re-typed tokens (review/work/indep.py). Caesar −1 covers every token, and no signs are left over.

## Key

Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by moving back one (A→Z).

| Cipher | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z |
|---|---|
| Plain | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y |

The heading ("Hotel Thursday") and the date are plain writing. The groups **E. L.** (twice) and **M-L** are abbreviations and are kept literal. Shifted they would give D. K. and L-K, which explain nothing, so it remains open whether they are enciphered at all.

## Plaintext

| Line | On the card | Reading |
|---|---|---|
| heading | Hotel Thursday | plain writing |
| 2 | Nz Pxo E. L. Cpz | MY OWN [E. L.] BOY |
| 3 | Kvtu Ibe b | JUST HAD A |
| 4 | gjof xbml | FINE WALK |
| 5 | mpwfmz xfbuifs | LOVELY WEATHER |
| 6 | J ipqf zpv bsf | I HOPE YOU ARE |
| 7 | xfmm M-L Gspn | WELL [M-L] FROM |
| 8 | zpvs Pxo E. L. Hjsm | YOUR OWN [E. L.] GIRL |
| foot | Sep. 26th 07 | plain writing |

**English (the original language; punctuation editorial):** *My own E. L. boy, just had a fine walk. Lovely weather. I hope you are well. M-L. From your own E. L. girl.*

**Slovak:** *Môj vlastný E. L. chlapec, práve som sa pekne prešla. Nádherné počasie. Dúfam, že sa máš dobre. M-L. Od tvojho vlastného E. L. dievčaťa.*

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1381/work/decode.py
```

The script checks the SHA-256 of the four image files, decodes the transcription, checks the inverse, and prints the plaintext with the counts (67 enciphered, 6 literal).

## Uncertainties

- **`xbml` (WALK):** the x, b and final l are visible, but the m lies under the overlay letter R and cannot be read. It is a restoration by sense.
- **`Ibe`, the `b` at the end of line 3, and `gjof`:** the shapes fit, but they are faint or partly under the overlay, and the sense helped. The first sign of `Ibe` fits the writer's looped capital I.
- **`E. L.` and `Cpz` on line 2:** very faint, and read with the help of the couple's formula. Sister cards fill this slot with `N. L.` (HCP 1364, 1368), `M. L.` (HCP 1347, 1365) and `E.h` (HCP 1387). A low bowl and the legible group on line 8 favour E. L. here. On line 8 the second letter has a small foot and could be h rather than L.
- **`M-L` on line 7:** three downstrokes favour M over N, and HCP 1382 and 1383 have the same group as M-L. N is not wholly excluded. The dash may be only a stop.
- **Meaning of the abbreviations:** E. L. and M-L are not expanded; their meaning is unknown.
- **"Hotel" in the heading:** plain writing, not provable from the pixels, and not part of the decryption. Sister cards have initials at this place.
- **The physical card:** neither solver nor reviewer saw it or a scan without the overlay. The pencil under the disc may survive on the original.

## Review summary

Review 1 returned **REVISE**. It confirmed the command, the key, the postmark, the date and most of the words, and reported four findings:

- **Major, fixed:** the first reading of line 7 was `Nz L.` (MY L.). This was wrong. The sign is one capital of three downstrokes with no z foot, and the supposed z descender is the ascender of the L on line 8. It now reads `M-L`, and MY is gone from that line (69 enciphered letters became 67, and 5 literal letters became 6).
- **Minor, fixed:** the alternatives for `E. L.` on line 2 are now named, and the line 8 group is rated better.
- **Minor, fixed:** `Ibe` and `Gspn` are capitals on the card; the plaintext does not change.
- **Minor, fixed:** "printed" wheel was corrected to the portal's overlay, and the circular use of the formula as evidence is now stated.

The solver noted one out-of-date detail in the review: HCP 1382 now reads the same group as M-L rather than N-L. The reviewer could not verify the m of `xbml`, the E and L of line 2, "Hotel", M against N on line 7, or the meaning of the abbreviations. These are the uncertainties above.

## Sources

- HC Portal record 1381 and its attached images (source/, work/hires/, listed in SOURCES.md).
- Sister cards in this repository: HCP 1347, 1364, 1365, 1368, 1382, 1383, 1386, 1387, 1402, 1403.
