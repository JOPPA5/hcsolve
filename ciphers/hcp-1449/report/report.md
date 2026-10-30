# HCP 1449 (pc_hcp_130): an English holiday message in Greek letters from Menai Bridge

Human solver: Tomáš Pavuk

**Status: deciphered in full (49 of 49 cipher signs read, every sign covered by the key); independent review 1 verdict ACCEPT, no change to the decoded letters. One two-letter word, ⟨mg⟩, is read letter for letter but its meaning (initials or "my") is open.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1449 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1449), portal name pc_hcp_130, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date and language Unknown, location Europe, sender Unknown, recipient L. Thompson, with no transcription or solution attached.

The picture side is a Photochrom Co. card of the interior (nave) of Bangor Cathedral in North Wales; it carries no handwriting. The address side, scanned sideways, has the printed headings "POST CARD", "ADDRESS ONLY", "THIS SPACE FOR COMMUNICATION" and the publisher's line "Published by the Photochrom Co. Ltd., London and Detroit, U.S.A. Printed in England". In plain handwriting it is addressed to **Miss L. Thompson, 85 Upper Highgate St, Birmingham**, and the communication space is headed in plain writing **Menai Bridge / Sat evening**. Below that heading stand three short lines in Greek-looking letters, followed by a monogram signature. The stamp has been removed and the remaining postmark is illegible, so the year is not known. The card format (divided back, "This space for communication") and the Photochrom imprint point to the Edwardian period, roughly 1902–1915.

Writing English in Greek letters was a common light-hearted "cipher" on Edwardian postcards, used by people who had learned the Greek alphabet at school to keep a short message from casual readers.

![Address side turned upright: address to Miss L. Thompson, Birmingham; plain heading "Menai Bridge / Sat evening"; the three Greek-letter lines and the monogram below (work/address-rotated.jpg)](../work/address-rotated.jpg)

![The cipher passage enlarged (work/message.jpg, crop of the address side)](../work/message.jpg)

![Picture side: Bangor Cathedral, nave (source/picture.jpg)](../source/picture.jpg)

Other marks on the card, none of them cipher: the address, the place-and-day heading, the printed headings and publisher's line, the postmark remnant, the monogram signature and the HCPortal watermark (a large lettered ring) on both sides.

## Method

Earlier source capture and triage (2026-10-26) were done by an OpenAI GPT solver (GPT-6 Astra). It saved the scans, rotated and cropped the passage, tried a mirror image and a 180° rotation, and recorded that it could not yet identify the system; it established no reading.

On 2026-10-30 Claude Opus 5.5 recognised the letterforms as Greek used for English. The passage was transcribed **manually**, sign by sign, from 5–8× enlargements of the crop (no OCR; the portal supplied no transcription). Each sign was written as the nearest Greek letter, keeping the two Latin letters the writer used (j, and the final w of "tomorrow"). A short script then replaces each Greek letter by its English value. Because the shapes are handwritten, decisions were checked against repeats on the card: the same w-like μ ends "him" and stands in "tomorrow"; the same y/ʒ-shaped γ stands in "regards"; ω is used for every o.

In review a second, separate Claude Opus 5.5 agent rotated and cropped the scan itself, made 4–8× and thresholded enlargements, transcribed all three lines under its own glyph labels and decoded them with its own key and script. Its result was identical: 49 glyphs, 22 distinct glyph forms, all mapped.

## Key

A letter-for-letter transliteration (monoalphabetic substitution of Latin letters by Greek letterforms):

| Greek sign on the card | English | Remarks |
|---|---|---|
| Η (cursive, U-shaped with a bar) | h | have, him |
| α (written like q) | a | |
| one v-shaped sign (υ / ν) | v and n | v in have; n in seen, kind – one sign, two values, by context |
| η, usually with an over-bar (η̄) | e | over-bar in have, seen |
| ο | u | as in Greek ου; just, out |
| ω | o | look, for, off, tomorrow |
| σ | s | |
| τ | t | |
| μ (w-like) | m | |
| γ (y/ʒ-shaped) | g | regards; in word 4 g, or possibly y |
| φ | f | two forms: a tall looped f in for, a ligature of two barred descending φ in off |
| λ | l | |
| κ | k | |
| ρ | r | |
| ι | i | |
| δ | d | |
| j, w | j, w | Latin letters kept: j in just, final w of tomorrow |

The writer's choices follow pronunciation rather than strict Greek spelling: English *u* is written ο (Greek ου), English *o* is ω, and letters with no Greek equivalent (j, w) are left in Latin.

## Plaintext

Transcription (Greek as written, line by line):

```text
Ηαυη jοστ σηην μγ ωφφ
λωωκ ωοτ φωρ Ηιμ
τωμωρρωw κινδ ρηγαρδσ
```

Mechanical transliteration:

```text
have just seen mg off
look out for him
tomorrow kind regards
```

followed by a monogram signature (two interlaced capitals, not read).

English, as on the card: **Have just seen ⟨M.G.⟩ off. Look out for him tomorrow. Kind regards.**

Meaning: the writer, at Menai Bridge on a Saturday evening, has just seen someone off (by train or boat) and tells Miss Thompson in Birmingham to look out for him the next day.

Slovak translation: **Práve som odprevadil(a) ⟨M.G.⟩. Zajtra ho vyhliadaj (čakaj ho). Srdečné pozdravy.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1449/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the two scans and the metadata in source/, then transliterates the manual transcription in work/transcription.txt with the key in work/key.json, stops if any sign is unmapped, and prints the three lines above. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **Word 4, ⟨μγ⟩ = "mg".** Both signs are clear (the w-like μ and the y/ʒ-shaped γ) and nothing else stands between them and "off". As a word it is not English. It is most likely the initials **M.G.** of the man who was seen off (the "him" of the next line), or **"my"** with γ used for *y* (the letter looks like a y) and a noun left out by the writer ("have just seen my [ … ] off"). The literal letters are certain; the meaning is not. The monogram signature is not evidence either way.
- **The middle sign of "out"** is blotted or overwritten. A round core is visible and is read as ο (u), as in "just"; the reading is guided by context.
- **v/n.** The same v-shaped sign is v in "have" and n in "seen" and "kind"; only context separates them.
- **Resolution.** The scan is about 1024 px across the card and the portal watermark runs over the passage; all decisions were made on 4–8× enlargements.
- **Date and people.** The postmark is illegible, so the year is unknown (Edwardian by the card format); only "Sat evening" is written. The sender (monogram), the recipient beyond "Miss L. Thompson" and the person seen off are not identified.
- No published solution of this card was found: the portal lists it as Not solved with nothing attached, and the AI Decipherment Register had no record for it on 2026-10-29.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), rotated and cropped the scan itself, transcribed all three lines under its own glyph labels and decoded them with its own key; the result was the same, with every one of the 49 glyphs covered. It confirmed sign by sign the readings of have, just, seen, off, look, for, him, tomorrow, kind and regards, that word 4 consists of exactly two signs with no hidden ink in the watermark next to it, and that the earlier GPT triage was credited truthfully. Its four findings were minor and were addressed:

- **Word 4.** One consistent rendering is now used everywhere: literal ⟨mg⟩ / ⟨M.G.⟩, with "my" given as an alternative, and the monogram not equated with it.
- **γ for g and y.** The key now states that γ would serve for both letters if "my" is read.
- **Allographs.** The over-barred η̄ for e and the two forms of f are now recorded in the key and in the transcription notes.
- **v/n.** The key now shows them as one sign with two values.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1449, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1449 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4408/conversions/pc_hcp_130_adr-large.jpg (source/address.jpg).
- Picture side: https://api.hcportal.eu/media/4407/conversions/pc_hcp_130_pic-large.jpg (source/picture.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
