# HCP 1359 (pc_hcp_40): an English love card to Mr W. Abbott, 9 May 1907

Human solver: Tomáš Pavuk

**Status: whole message read (52 of 52 enciphered letters); the short closing group M. & L. and a trailing t are kept literal and unexpanded. Independent review 1 verdict ACCEPT; no decoded letter changed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1359 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1359), portal name pc_hcp_40, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-05-09, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (the catalogue's spelling of Abbott), with no transcription or solution attached.

The picture side is a printed view, **The Promenade and Beach, Morecambe**, with no handwriting. Everything handwritten is on the address side, which is scanned sideways; the message is read after turning the scan 90° counter-clockwise. The printed line reads E.S. London No. 468. The address, in plain writing, is to **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**. The card has a halfpenny Edward VII stamp. Its postmark shows only "…ORNE", 10 PM and 9 on this scan. The same writer's hcp-1392, of the same day, is postmarked [WI]MBORNE 10 PM MY 9 07, so the office is probably Wimborne, but that name, the month and the year come from the sister card and not from this scan.

The plain heading reads **G. H. Thursday.** and the plain date **May 9th 07**. 9 May 1907 was a Thursday, and the date agrees with the portal. The grey A–Z disc and building logo on the scan are a scanning overlay, not part of the card.

The card belongs to the correspondence of a woman who signs as his girl with W. Abbott in 1907–08, already read on hcp-1386…1407. No published solution of this card was found or used, and no earlier work on this number exists in this repository. The AI Decipherment Register was checked on 2026-10-30 and has no record for it.

![Picture side: The Promenade and Beach, Morecambe (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned, sideways (source/address-large.jpg)](../source/address-large.jpg)

![Message area turned upright: heading, six cipher rows, and the plain date at lower left (work/crops/reading.png)](../work/crops/reading.png)

## Method

The transcription is manual. The solver turned the un-converted scan upright and read every word from 3–5× enlargements. The key was tested as a hypothesis taken from the sister cards, then applied to every token without any per-word adjustment. The strongest evidence comes from words outside the usual formulae: ABOUT, THE, OF, THIS and STOCK.

Early attempts gave no word and were corrected by rereading the shapes, never by changing the key: `befpvu` became `bcpvu` = ABOUT, and `nijl` became `uijt` = THIS, with the uncrossed t this writer also uses on hcp-1387. For the capital of `Foe`, V (UND, no word) and P (ONE, rejected on form) were tested and F (END) was kept.

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet; decrypt by subtracting one. The heading and date are in plain writing.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

| Ciphertext | Literal plaintext |
|---|---|
| *(plain)* G. H. Thursday. | G. H. Thursday. |
| Nz. Pxo. Efbsftu | MY. OWN. DEAREST |
| J. bn. bcpvu. uif | I. AM. ABOUT. THE |
| Foe. pg. uijt | END. OF. THIS |
| tupdl. M. & L. t | STOCK. [M. & L.] [t] |
| Gspn. Zpvs. Pxo | FROM. YOUR. OWN |
| Hjsm. | GIRL. |
| *(plain)* May 9th 07 | May 9th 07 |

52 cipher letters are decoded with the one key; 3 letters (M, L, t) are kept literal.

English (the plaintext language; the portal lists Unknown): **G. H., Thursday. My own dearest, I am about [at] the end of this stock. M. & L. [t]. From your own girl. May 9th 07.**

Slovak: **G. H., štvrtok. Môj najdrahší, som asi na konci týchto zásob. M. & L. [t]. Od tvojho vlastného dievčaťa. 9. mája 1907.**

The likely sense is that she is nearly out of this stock of postcards. That is an inference: the card does not say what the stock is. She was sending cards almost daily, and hcp-1392 of the same day says she is sending a card instead of a letter.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1359/work/decode.py
```

The script checks the SHA-256 hashes of the four image files, decodes every cipher token of work/transcription.json, checks the inverse round trip, and prints the plaintext, the counts and the alternative for the uncertain sign. It does not read the image: the transcription step is manual and was confirmed independently in review.

## Uncertainties

1. **Capital of `Foe` = END (weakest letter).** The sign is a large left curl running into a stem, plus a long rising stroke, and its outline is V-like; read as V the word is UND, not a word. It lacks the arch and crossbar of the writer's plain F. It is unlike his capital V of `Vtvbm` on hcp-1373, which has no left curl. The enciphered F of `Fbsmz` = EARLY on hcp-1355 has the same construction, with the rising stroke leaving higher. hcp-1355 is not closed, so this is a parallel, not an accepted control. F rests on that parallel and on sense.
2. **Third letter of `Foe`.** A small sign with a filled eye, read e; c would give ENB. No other lowercase e on this card is available for comparison.
3. **`bcpvu` = ABOUT.** The letters are crowded and can be misread as `befpvu`, which gives no word.
4. **`Efbsftu`.** The s is c-shaped and the final letters are pale. The word is a formula also found on hcp-1392.
5. **`uijt`.** The last letter is an uncrossed t. A third dot nearby sits level with the top of the t, so it may be a detached crossbar and not a period. This is not certain and has no effect on the reading.
6. **`M. & L.`** The group is kept literal and unexpanded. The capital has one more stroke than the one-legged N of `Nz`, so it is transcribed M; the extra stroke is short, so N is not fully excluded, and hcp-1392 reports `N & L`. Shifted, the group gives L. & K. Finished cards treat it either as enciphered (hcp-1368, L. & K.S; hcp-1395, L. & K.; both read as probably "love and kisses") or as literal (hcp-1361, hcp-1407). "Love and kisses" is a family hypothesis and is not claimed here.
7. **Trailing t.** A curved stroke with a detached short dash, read as t by parallel with hcp-1368 and with hcp-1366 (not closed). hcp-1392 of the same day has none. It may instead be a mark, and it is not counted as a decoded letter.
8. **Stroke before `Hjsm`.** A long, dry, pale curve with a dark foot stands just after the date. It is treated as a pen stroke, not a letter. Some sister cards have a closing group before "girl", so a lost abbreviation is not excluded; nothing readable is there.
9. **"About the end".** The phrase lacks "at"; the reading is literal.
10. **Not established:** the meaning of the closing group, what the stock is, and the identity of G. H. and of the writer. Month and year cannot be read from the postmark on this scan.

![Capital F of Fbsmz on hcp-1355 (left) and the capital of Foe on this card (right) (review/work/cmp_F_1355_vs_1359.png)](../review/work/cmp_F_1355_vs_1359.png)

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, decoded its own token list with its own script (same six rows, same 52 letters), made its own crops and read every word sign by sign, checked the key's coverage, and computed the weekday. It tried to break the reading through the capital of `Foe` and found it better supported than the solver had claimed. It did not run a separate web search for a published solution. Its four findings were all minor and are reflected here:

- **Sister capital F.** The solver had said no enciphered capital F survives; `Fbsmz` on hcp-1355 is one. Uncertainty 1 is corrected.
- **Status of sister cards.** The t parallels are now stated with their status. hcp-1368 was closed after the review; hcp-1366 is still open.
- **Third dot near `uijt`.** It is not in a period's position, and the note is adjusted.
- **Postmark.** Wimborne is added, labelled as coming from hcp-1392.

**One change after the review, not re-reviewed.** hcp-1368, closed after this review, rejects N for the closing group by counting downstrokes. The same test on this card gives M, so the literal group changed from `N. & L.` to `M. & L.` The review had noted that M is not excluded. No decoded letter changed.

Transcription, decipherment, review response and this report are by Claude Opus 5.5.

## Sources

- HC Portal record 1359, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1359 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4137/pc_hcp_40_pic.JPG (work/hires/) and its conversion (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/4138/pc_hcp_40_adr.JPG (work/hires/) and its conversion (source/address-large.jpg).
- Sister cards in this repository: hcp-1392, 1368, 1395, 1361, 1407 (closed); hcp-1355, 1366 (not closed); hcp-1373, 1387.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
