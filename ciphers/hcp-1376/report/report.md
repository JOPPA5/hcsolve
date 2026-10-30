# HCP 1376 (pc_hcp_57): a Caesar-shifted English love postcard, 9 November 1907

Human solver: Tomáš Pavuk

**Status: whole message read (54 cipher letters read, 1 restored under a blot, 9 letters of abbreviations kept literal); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1376 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1376), portal name pc_hcp_57, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-11-09, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue misreading of Abbott), with no transcription or solution attached.

The picture side is a printed view, "Glastonbury Abbey looking West", with no handwriting. The address side carries a halfpenny Edward VII stamp with the postmark WIMBO[RNE] / 10 [PM?] / NO 9 / 07. It is addressed to **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**. The date agrees with the portal, and 9 November 1907 was a Saturday, which matches the plain heading "G. H. Saturday". The circular disc and building logo on the scans are a scanning overlay, not part of the card.

The message is written on the address side, sideways; it reads upright when the scan is turned 90° counter-clockwise. The language is English. The card belongs to a group of cipher postcards addressed to W. Abbott, among them HCP 1386–1407, which the repository attributes to one couple in 1907–08. This card has the same key, hand and formulae as those. It was read with a key already known from them, and no reading of this particular card was supplied or consulted.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![The message, turned upright (work/crops/msg.png)](../work/crops/msg.png)

## Method

The transcription is **manual**. The solver read the un-converted original scan (work/hires/pc_hcp_57_adr.JPG) after rotating it, sign by sign from enlarged crops, and recorded each token in work/transcription.json. The groups `xbt qptufe`, `Cfgpsf` and `Nztufsz` gave WAS POSTED, BEFORE and MYSTERY under a shift of one at once, and that single shift then held for every enciphered word.

Several first impressions were corrected on the enlargements by rereading the shapes, never by changing the key:

- What looked like "Fr" in row 1 is the big-bowled P of `Px[o]`, the same form as on HCP 1386.
- What looked like a slash and a caret in row 4 is one sign, the j of `dmfbsjoh`, with a very long descender and a V-shaped foot.
- CLEARED fails on the count of signs; `dmfbsjoh` = CLEARING fits all eight.
- The loop in row 6 is the descender of the f of `Nztufsz`, not a letter of `Zpvs`.

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet, and one subtracts one to decrypt.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "No. 3. G. H. Saturday" is ordinary writing. `2 hrs.` is left plain by the writer. `E-L.` and `N. & L.` are abbreviations kept literal, as on the sister cards.

## Plaintext

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Px[o] E-L. | MY. OWN [E-L.] |
| Jt. xbt. qptufe | IS. WAS. POSTED |
| 2 hrs. Cfgpsf. | 2 hrs. BEFORE. |
| dmfbsjoh. | CLEARING. |
| "Ju't. b. Nztufsz" | "IT'S. A. MYSTERY" |
| Nz. N. & L. gspn. Zpvs. | MY. [N. & L.] FROM. YOUR. |
| E-L. Hjsm. | [E-L.] GIRL. |

Reading (the writer's own English; square brackets mark the one emendation, of the literal IS to "It"):

**My own E-L. [It] was posted 2 hrs before clearing. "It's a mystery." My N. & L. from your E-L. girl.**

Slovak translation: **Môj vlastný E-L. [Bolo to] podané 2 hodiny pred vyberaním schránky. „Je to záhada." Moje N. & L. od tvojho E-L. dievčaťa.**

"Clearing" is taken as the emptying of a post box, good period usage. The sentence evidently answers a complaint that an earlier card arrived late, but that context is inferred; it is not on the card.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1376/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the two scans in source/ and the two originals in work/hires/, decodes every token of work/transcription.json, checks the inverse round trip, and prints the literal plaintext with the line `54 letters read and decoded, 1 restored under a blot, 9 kept literal; hashes OK.` It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **`Jt` = IS, where the sense needs IT.** The second sign is certainly the t form of `xbt`, so the letters give IS. The first sign has a large closed loop, which the plain J of `Ju't` lacks, and that favours a plain capital I: the word may be "It" left unshifted like `2 hrs.` A slip for `Ju`, or a half-shifted slip, are also possible. All three come to the same sense, and the card cannot decide between them.
- **`Px[o]`.** In the place of the o stands a solid blot, about 30 x 22 px on the original where this writer's stops are about 10 x 7 px. It stands on the baseline. The reading OWN is a restoration from the formula `Nz Pxo E L`; the pixels alone do not show an o. If the blot is only a heavy stop, the group is an abbreviated `Px.` = OW.
- **`hrs.`** is read as plain h, r, s. Shifted, it would give GQR.
- **`Zpvs`.** The Z and the p stem are clear; p, v, s are pale and partly hidden by the loop of the f above, and v and u cannot be told apart here. The sign count and shapes fit, and YOUR is not in doubt.
- **`dmfbsjoh`.** The first sign, left loop plus tall stroke, is read as d; a U-like reading gives no word.
- **Abbreviations.** `E-L.`, `N. & L.` and `G. H.` are not expanded; nothing on the card proves a meaning.
- **Other marks.** A long horizontal line with an arrowhead runs under row 4; its purpose is unknown. The heavy dot above the top of the `J` of `Ju't` probably belongs to that J. A short tick follows `clearing`. None of them affects the plaintext.
- **Heading number** after "No." reads 3, with 2 or 7 not excluded; it is not ciphertext.
- **Postmark.** A 10 stands above NO. Sister cards report WIMBORNE 10 PM, but the letters after 10 cannot be read here.
- **Scans only.** Faint ink in rows 6–7 could hold detail a scan loses.
- The key and formulae were compared with sister cards, not recovered blind, though one shift decodes every enciphered word here, including MYSTERY, which was not taken from any sister card. No prior publication of this card was found, but no exhaustive search was made.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. Solver and reviewer are the same model on this card, so this was not an inter-vendor check. The reviewer ran the reproduction command, recounted the figures by hand, checked all hashes, decoded its own tokens with its own script, read every sign of rows 1–7 from its own 3x crops and 5–7x crops of the disputed places, and compared the forms with HCP 1386. It could not refute the reading. Its six findings were minor and are reflected here:

- **Wording.** `Jt` is now called the only *fully legible* token that does not decode as expected.
- **Plain "It".** The difference between the looped sign of `Jt` and the plain J of `Ju't` is now stated, with the half-shifted slip as a third explanation.
- **Emendation.** The English and Slovak lines now mark "[It]".
- **Heavy dot.** Now assigned, as probable, to the J of `Ju't`.
- **`Zpvs`.** Now described as confirmed in outline.
- **Postmark.** The 10 above NO is now recorded, with PM left unconfirmed.

No decoded letter changed as a result of the review. All work on this card was done by Claude Opus 5.5.

## Sources

- HC Portal record 1376, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1376 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4188/conversions/pc_hcp_57_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4188/pc_hcp_57_pic.JPG (work/hires/).
- Address side: https://api.hcportal.eu/media/4189/conversions/pc_hcp_57_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4189/pc_hcp_57_adr.JPG (work/hires/).
- Sister cards in this repository, HCP 1386–1407 and in particular ciphers/hcp-1386/.
