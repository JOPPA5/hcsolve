# HCP 1101 (cpc_1898-02-11_CH_Basel_CH_Basel_): a love verse hidden under a red lattice, Basel 1898

Human solver: Tomáš Pavuk

**Status: read in full; the hidden message is a six-line German verse concealed under a red overlay (steganography, no cipher). Independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1101 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1101), portal name cpc_1898-02-11_CH_Basel_CH_Basel_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Marie Müller, with no transcription or solution attached. The portal links the HistoCrypt paper on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166).

The address side is a pre-printed German form, "Deutsche Reichspost / Postkarte", but it was franked with a Swiss Helvetia 5-centime stamp and cancelled BASEL 11 II (1898). It is addressed in plain writing to **Fräulein Marie Müller, Basel, Dornacherstrasse 2?4** (the house number is partly covered by the round collection stamp of the HC Portal / Schrödel collection). The picture side is a view card published by Vogel, Leipzig (No. 180), photograph credited "R. Loës ph.".

![Address side: Fräulein Marie Müller, Basel; Swiss 5 c stamp, Basel postmark 11 II (source/address-large.jpg)](../source/address-large.jpg)

On the picture side, in the free space beside the view, the writer put the open date **11/II/98** and the remark **"das isch suber"**, then a block of handwriting covered by a dense red lattice, and below it the open closing **"Mit freundl. Gruss"** and the initials **H. B.** in a hand-drawn oval.

![Picture side as delivered: the red lattice over the hidden block, with the open date, remark, closing and initials (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The block is not enciphered; it is concealed. The message was written in black ink in ordinary Latin cursive, and then covered with red: thick horizontal and vertical red bars, red diagonal crosses, and red loops and scribbles that imitate handwriting, so that to the naked eye the block looks like an illegible tangle. The black strokes visibly run under the red bars, so the red was added afterwards.

The intended way to read such a card is through red glass or red cellophane: red lines then become as pale as the paper, while black ink stays dark. The digital equivalent is the red colour channel of the scan. The solver took the un-converted high-resolution scan of the picture side (3468 x 2298 pixels), cropped the block and kept only the red channel (work/redfilter.png, written by the reproduction script). In that image the red lattice almost disappears and the six lines read continuously. The reviewer made its own filter independently (a different crop and a hard threshold on the red channel, review/work/rf_all.png and 3x enlargements), read every line before looking at the solver's text, and agreed word for word.

![The hidden block seen through the "red glass": red channel of the high-resolution scan (work/redfilter.png)](../work/redfilter.png)

Both sides were searched for further hidden text: the picture border and edges, the margins of the address side, and the edges of the stamp. Nothing else was found.

## Key

There is no letter key. The "key" is the reading method: look through a red filter. Register type: **Steganography**. The label MASC + Steganography would be wrong here, because no part of the card is enciphered.

## Plaintext

Open text and hidden block, as written (ñ is the writer's n with a nasal bar, standing for nn):

```text
[open]    11/II/98        das isch suber
[hidden]  Weñ der früche Morgen lächelt
          Weñ des Abends Kühle fächelt
          Immer-immer denk ich dein
          In der Mitternächte Hülle
          Selbst in meiner Träume Stille
          Mischt dein schönes Bild sich ein.
[open]    Mit freundl. Gruss      H. B.
```

Normalised German:

**Wenn der frühe Morgen lächelt, / wenn des Abends Kühle fächelt, / immer, immer denk ich dein. / In der Mitternächte Hülle, / selbst in meiner Träume Stille / mischt dein schönes Bild sich ein.**

"das isch suber" is Swiss German (standard German "das ist sauber"), roughly "that's neat" or "that's clever", a comment on the hiding trick.

English translation:

**11 Feb. '98. That's a neat one.**
**When the early morning smiles, / when the evening's coolness fans, / always, always I think of you. / In the shroud of the midnights, / even in the stillness of my dreams / your lovely image mingles in.**
**With kind regards, H. B.**

Slovak translation:

**11. 2. 98. To je šikovné.**
**Keď sa usmieva skoré ráno, / keď ovieva večerný chlad, / stále, stále myslím na teba. / V závoji polnocí, / aj v tichu mojich snov / sa vmiesi tvoj krásny obraz.**
**S priateľským pozdravom, H. B.**

The verse is regular trochaic metre with the rhymes lächelt / fächelt, Hülle / Stille and dein / ein, in the manner of a period album or love poem. Its literary source, if it has one, was not found.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1101/work/decode.py
```

A Python with Pillow is needed to write the filtered image (on the solver's machine, the Python under ~/.cache/codex-runtimes). The script checks the SHA-256 hashes of the four scans, writes work/redfilter.png (the red channel of the hidden block) and prints the transcription and the normalised text. The transcription itself is a reading of the filtered pixels, not computed by the program; the filtered image is the evidence, and it was read independently by the reviewer.

## Uncertainties

- **"früche"**: the card has f-r-ü-c-h-e. Read as "frühe" (early). It is either a slip of the pen or a spelling coloured by Swiss German "früech"; the meaning is the same either way. The normalisation to "frühe" rests on word sense.
- **"Weñ"** (twice) is "Wenn" written with a nasal bar over the n.
- **Pen marks**: the hyphen in "Immer-immer" is kept as written; a short stray slash after "Hülle" is a pen stroke, not a letter, and is left out.
- **"Mit freundl. Gruss"**: the first word has an overwritten letter (an extra t or f stroke); read "Mit".
- **Writing under the stamp** cannot be excluded, since the stamp cannot be lifted from a scan; nothing is visible at its edges.
- **Identities**: the sender is known only as H. B.; the recipient's house number on Dornacherstrasse is partly covered (2?4).
- **Source of the verse**: not identified by solver or reviewer.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer re-ran the reproduction command and checked the hashes with shasum; built its own red-channel filter with a different crop and threshold; read all six hidden lines on its own and agreed with the solver word for word; confirmed the open text, the date against the Basel postmark, and the Swiss German remark; and found no published source or solution for the card. Its three minor findings are reflected in this report:

- **German form**: the address side is a German "Deutsche Reichspost" form, the card published by Vogel, Leipzig, and posted in Switzerland; now stated under Origin and context.
- **"früche"**: the Swiss German "früech" explanation is now given as an alternative to a slip of the pen.
- **Pen marks**: the stray slash after "Hülle" is now mentioned, alongside the kept hyphen.

No word of the reading changed because of the review. At the human's request the stamp area was checked again for stamp-box steganography (reported on the Jolánka series); nothing was found, and the type remains Steganography because nothing is enciphered.

All work on this card (capture, filtering, reading, translation, this report) was done by Claude Opus 5.5 (Anthropic); there was no earlier work on this number.

## Sources

- HC Portal record 1101, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1101 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3363/conversions/cpc_1898-02-11_CH_Basel_CH_Basel__pic-large.jpg (source/picture-large.jpg); high-resolution original https://api.hcportal.eu/media/3363/cpc_1898-02-11_CH_Basel_CH_Basel__pic.jpg (work/hires/).
- Address side: https://api.hcportal.eu/media/3364/conversions/cpc_1898-02-11_CH_Basel_CH_Basel__adr-large.jpg (source/address-large.jpg); high-resolution original https://api.hcportal.eu/media/3364/cpc_1898-02-11_CH_Basel_CH_Basel__adr.jpg (work/hires/).
- HistoCrypt paper linked from the portal record: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no record for this card.
