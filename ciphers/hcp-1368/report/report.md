# HCP 1368 (pc_hcp_49): a shift-by-one love postcard from Wimborne, 26 July 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (44 of 44 enciphered letters); one short group, `M. h`, is unresolved and left as written; independent review 1 verdict REVISE, findings addressed; no running word changed, the abbreviation groups were re-read.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1368 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1368), portal name pc_hcp_49, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and HCPortal collection, category Substitution, date 1907-07-26, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue spelling), with no transcription or solution attached.

The picture side is a printed Valentine's view, *The Choir, West, Westminster Abbey*, with no handwriting. The address side, read with the card turned 90° anticlockwise, is addressed in plain writing to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. It has a halfpenny Edward VII stamp and a postmark reading BORNE / 10 PM / JY 26 / 07. BORNE is the visible part of the town name; other cards of the correspondence show Wimborne, so the town is inferred, not read in full. The plain date July 26th 07 fell on a Friday, which agrees with the plain heading "G. H. Friday".

The card belongs to a long run of cards to the same recipient on the portal, written by a girl to her sweetheart in the same hand, the same cipher and the same formulae. Finished cards of the run in this repository include hcp-1378, 1395 and 1402. The key was therefore carried over as a hypothesis from those cards and tested on this card's pixels. It is not a new key recovery. Card hcp-1369 was written on the same day.

![Address side turned upright: heading, six cipher lines and date (work/crops/reading.png)](../work/crops/reading.png)

![Picture side: The Choir, West, Westminster Abbey (work/crops/pic_view.jpg)](../work/crops/pic_view.jpg)

## Method

The transcription is **manual**, from the un-converted high-resolution scan rotated 90° anticlockwise and enlarged 3–8× (work/crops/). The portal supplied no transcription and no OCR was used. Doubtful signs were compared with other signs on the same card and with sister cards.

Subtracting one from every enciphered letter gives ordinary English with no exceptions in the running words: Pxo → OWN, qptu → POST, dbset → CARDS, wfsz → VERY, ojdf → NICE, Hjsm → GIRL. POST, CARDS, VERY and NICE are not formula words of the correspondence, so they carry the proof. The frame "my own … boy" and "your own … girl" alone would not.

In review a separate agent typed its own transcription from its own crops and decoded it with its own script, and tried all 26 shifts against the card's vocabulary. Its running words are the same as the solver's.

## Key

A Caesar shift of +1 for encryption (−1 for decryption): each plaintext letter is written as the letter after it.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "G. H. Friday" and the date "July 26th 07" are ordinary writing, not shifted.

## Plaintext and translation

| Ciphertext | Plaintext |
|---|---|
| (plain) G. H. Friday | G. H. Friday |
| Nz. Pxo. M. h Cpz. | MY. OWN. [M. h] BOY. |
| qptu. dbset | POST. CARDS |
| up Ebz. wfsz. | TO DAY. VERY. |
| ojdf. M. & L.t | NICE. L. & K.S |
| zpvs. Pxo. M. h | YOUR. OWN. [M. h] |
| Hjsm. | GIRL. |
| (plain) July 26th 07 | July 26th 07 |

44 enciphered letters, all decoded by the one key: 41 in running words and 3 in the group `M. & L.t`. The 4 letters of the two `M. h` groups are unresolved.

English: **G. H., Friday. My own M. h boy. Post cards to-day. Very nice. L. & K.s [probably "love and kisses"], your own M. h girl. July 26th 07.**

Slovak translation: **G. H., piatok. Môj vlastný M. h chlapec. Pohľadnice dnes. Veľmi pekné. L. & K.s [pravdepodobne „love and kisses" = láska a bozky], tvoje vlastné M. h dievča. 26. júla 1907.**

The bracketed expansion is an editorial inference, not deciphered text. The sentence division is also editorial.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1368/work/decode.py
```

The script checks the SHA-256 hashes of the source files, decodes the manual transcription in work/transcription.json with the shift above, checks the round trip, and prints the lines and letter counts. It shows `M. h` as `[M. h = L. G?]`, that is, the written form and its shifted value. It does not read the image.

## Uncertainties

- **L. & K.s = "love and kisses"** is an inference. The letters `M. & L.t` are firm and shift to L. & K.S. They are the initial, initial and final letters of `Mpwf & Ljttft`; the phrase is spelled out on sister card hcp-1362, and hcp-1395 reads the same slot as L. & K. Nothing on this card states the expansion, and it is not proved that the group is enciphered.
- **`M. h`** is unresolved. The capital has the three-stroke build of the M in `M. & L.t`, not the two-stroke N of `Nz`. The second sign is a stem with a small foot, h-like in the salutation, h- or b-like in the closing, and unlike the L of `& L`. L remains the alternative, because some sister cards report `N. L.` in this slot. Shifted the group is L. G., unshifted M. h; neither gives a word, and whether it is enciphered is unknown.
- **`dbset`** is partly in dry pen over the portal watermark, and at first sight its middle looks like "e c". It has the same s and pointed e ligature as `dbse` on hcp-1378, and the t bar stands detached to the right.
- **`ojdf`** is very pale because the pen ran nearly dry, but all four signs are visible. The dark spot at the top of the f descender is an ink drop.
- **`zpvs`**: the v has a rising end stroke and might be taken as w, which gives no word.
- **`Hjsm`**: the V-shaped stroke and flourish under the word are the j slash and a paraph, not extra letters.
- **Sense.** "Post cards to-day. Very nice." is terse; it is read as comment on cards received, but the card does not say who sent them.
- **Heading.** G is preferred to C because of its descending foot. The writer's identity is not established, and "G. H." may not be her name at all.
- Separator dots follow the manuscript and carry no meaning.
- No search for a prior publication was made beyond the portal status (Not solved), the absence of an attached solution and the AI Decipherment Register (no record, checked 2026-10-30).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, decoded with its own script, checked every sign on the high-resolution original, and confirmed the weekday and the address. It could not break the reading of the running words. It raised five findings, and all were addressed:

- **The trailing t (major).** The first version kept `N. & L.` literal but read the following t as a shifted plural S, which contradicts itself. The group is now one enciphered token.
- **M, not N (major).** The group capitals have one more downstroke than the N of `Nz` on this card, so `N. & L.` became `M. & L.t`, value L. & K.S, with "love and kisses" marked as inference.
- **The second initial (minor).** The review asked that the alternative h be named. On checking the crops the solver went further and transcribes h, naming L as the alternative, so the group is `M. h` rather than the reviewer's `M. L.`.
- **Letter count (minor).** The earlier "42/42" counted the disputed t. The figures are now 41 running letters, 3 group letters and 4 unresolved letters.
- **Citations (minor).** Unfinished sister cards are no longer cited as accepted.

No running word changed as a result of the review. The transcription of the abbreviation groups, the plaintext of the closing group and the translations did.

Credits: portal capture, transcription, decipherment, response to review and this report by Claude Opus 5.5, 2026-10-30; independent review by a separate Claude Opus 5.5 agent. No earlier work on this number.

## Sources

- HC Portal record 1368, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1368 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4164/conversions/pc_hcp_49_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4164/pc_hcp_49_pic.JPG.
- Address side: https://api.hcportal.eu/media/4165/conversions/pc_hcp_49_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4165/pc_hcp_49_adr.JPG.
- Related cards in this repository: ciphers/hcp-1378, hcp-1395, hcp-1402 (finished); hcp-1362, hcp-1369 (reviewed, not finished).
