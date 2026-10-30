# HCP 1357 (pc_hcp_38): a Caesar-shift love postcard to W. Abbott, 22 March 1907

Human solver: Tomáš Pavuk

**Status: whole message read (54 of 54 enciphered letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** One letter is a restoration under an ink blot, and a few others are settled by sense; see Uncertainties. Report dated 2026-10-30.

> **My own dearest boy, this will make the pair for album. From your girl.**

## Origin and context

The cryptogram is record 1357 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1357), portal name pc_hcp_38, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-03-22, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached. "Abboú" is a catalogue misreading of Abbott.

The picture side is a Raphael Tuck "Glosso" *Illustrated Hymns* card, Postcard Series 5534, with a printed verse of "The day is past and over" credited to J. M. Neale as translator. It carries no handwriting.

The address side is addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. It has a halfpenny Edward VII stamp and a WIMBORNE postmark in which PM, MR and 07 are legible; the day is only partly legible and is compatible with 22. The message stands on the left half of this side and is read with the card turned 90° counter-clockwise. The date **March 22nd 07** is written in clear below it.

The card belongs to a series of Caesar-shift postcards in English sent to W. Abbott from a young woman who signs as "girl" (see, for example, HCP 1386–1407 in this repository). The hand, the phrasing and the groups `Nz`, `pxo`, `Efbsftu`, `Cpz`, `gspn` and `Hjsm` recur on those cards. An album is also mentioned on sister card HCP 1398.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![The message turned 90° counter-clockwise and enlarged 2×; the clear date stands below it (work/crops/reading-2x.png)](../work/crops/reading-2x.png)

## Method

The shift was first established on the sister cards of this correspondence, so here it was a hypothesis to test, not a new key recovery. The solver read the un-converted original scan (work/hires/pc_hcp_38_adr.JPG) turned counter-clockwise and enlarged 4–9×, and transcribed it by hand. No OCR was used. The transcription is in work/transcription.json. All 54 letters decode under one shift, with no per-word change.

The one real choice in reading was the first word of line 3, which could be `gbjs` (FAIR) or `qbjs` (PAIR). On this card g has a short hooked tail, while the first letter of `qbjs` has a long descender closing in a loop. That loop is the writer's q in `qptu` on HCP 1395, so the word is PAIR.

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the next letter of the alphabet. Decrypt by subtracting one.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

Ciphertext as transcribed, line by line, with its decoding. Dots are as on the card.

| Ciphertext | Plaintext |
|---|---|
| Nz. pxo. Efbsftu Cpz. | MY. OWN. DEAREST BOY. |
| uijt Xjmm. nblf. uif | THIS WILL. MAKE. THE |
| qbjs gps bmcvn | PAIR FOR ALBUM |
| gspn. Zpvs. Hjsm | FROM. YOUR. GIRL |
| (clear) March 22nd 07 | March 22nd 07 |

English (the original language; word divisions follow the handwriting, sentence punctuation is editorial): **My own dearest boy, this will make the pair for album. From your girl. March 22nd 07.**

Slovak translation: **Môj vlastný najdrahší chlapec, toto doplní pár do albumu. Od tvojho dievčaťa. 22. marca 1907.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1357/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of all four captured images, decodes the manual transcription in work/transcription.json and prints each line with its plaintext. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **`Zpvs`, last letter.** This is a restoration, not a pixel reading. The sign is an unreadable brown mass, and S is the only letter making a word in "from you? girl". The writer's usual `Zpvs` on sister cards supports it.
- **`Zpvs`, the v.** It is damaged by the same smudging: only a low stroke and a stroke rising to the right can be seen.
- **`Xjmm`, the j.** The sign has no dot, unlike the j's of `uijt` and `qbjs`, and it is nearly the same shape as the g of `gps`. Taken literally the word would give WFLL. WILL rests on sense and on the word on HCP 1351. The strokes after it number about six, which fits `mm`, but they cannot be separated one by one.
- **Other letter forms settled by sense.** The second f of `Efbsftu` has a closed round head and no ascender or lower loop. The c of `bmcvn` has a closed e-like top, and the v of that word runs into the n stroke. The j of `Hjsm` has no visible dot. DEARPST, ALDUM and GORL are not words.
- **`qbjs`, first letter.** Head shape alone does not separate g, j, q and f in this hand, so q rests on the descender loop and on sense.
- **`uijt`, first letter.** It looks like h, but it is this writer's tall word-initial u, as on HCP 1358 and HCP 1362. Taken as h the word would give GIHS.
- **Dash after `uijt`.** It is transcribed as nothing: either the bar of the t carried to the right, or a hyphen. No letter depends on it.
- **Dots.** Dots are kept as read, but some may be accidental. No letter depends on them.
- **"The pair".** The words are clear, but what they refer to is not stated. Probably this card matches another one for his album; which one is unknown.
- **Writer's identity.** The sender is known only as "girl". The portal lists the sender as Unknown.
- **Published solutions.** None turned up in the portal or this repository, and the AI Decipherment Register was checked on 2026-10-30. No wider web search was made.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command and got identical output. It made its own crops, transcribed the card independently and decoded it with its own script; its letters were the same as the solver's, and it differed only in punctuation. It also compared every other shift, confirmed the q by its descender loop, and checked the address, postmark and picture side. Its four findings were all minor and are reflected here:

- **The j of `Xjmm`.** The anomalous sign is now disclosed, and the claim that only the blot rests on a restoration was softened.
- **Two dots.** The dots after `gspn` and `Zpvs` were added to the transcription.
- **Other letter forms.** The f, c, v and dotless j above are now disclosed, with the consequence for q.
- **Capital U.** The first word is now transcribed `uijt`, not `Uijt`, because nothing shows it is a capital.

While closing the review the solver also reduced the postmark description to what the reviewer could confirm. No decoded letter changed.

Transcription, decipherment, report and closing are by Claude Opus 5.5. There is no earlier work on this number; the shift was first established on the sister cards of the correspondence.

## Sources

- HC Portal record 1357, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1357 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4131/conversions/pc_hcp_38_pic-large.jpg and the original https://api.hcportal.eu/media/4131/pc_hcp_38_pic.JPG.
- Address side: https://api.hcportal.eu/media/4132/conversions/pc_hcp_38_adr-large.jpg and the original https://api.hcportal.eu/media/4132/pc_hcp_38_adr.JPG.
- Sister cards in this repository: ciphers/hcp-1351, hcp-1358, hcp-1362, hcp-1395 and hcp-1398.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
