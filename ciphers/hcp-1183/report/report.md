# HCP 1183: an enciphered US postal card from Santa Clara to San José

Human solver: Tomáš Pavuk

**Status: deciphered in full (163 of 163 cipher signs); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1183 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1183), portal name "cpc_-06-25_USA_Santa Clara, California_USA_San Jose, California_", part of Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient "Fannie E. Brimblecone", with no transcription or solution attached.

The card is a United States one-cent postal card with the printed Liberty-head indicium of the type issued 1873–1881. It is postmarked SANTA CLARA CAL. JUN 25 (no year in the postmark) and addressed in ink "To Miss Fannie E. Brimblecom[?], San José, Cal." The handwritten surname looks like "Brimblecom"; the portal has "Brimblecone". A small pencil "51" at the lower left of the address side is probably a dealer or collection number.

The message side holds nine short lines in pencil, written entirely in invented geometric signs: six lines of text, three initials, and two short groups at the bottom left and bottom right. The HC Portal watermark is printed over the lower right corner and partly covers the initials and the last group.

![Message side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Santa Clara postmark, one-cent indicium, address to San José (source/address-large.jpg)](../source/address-large.jpg)

## Method

All work on this card was done by Claude Opus 5.5 (Anthropic) on 2026-11-03; there was no earlier work on this number. The message side was read sign by sign from 3–6x enlarged crops of the un-converted high-resolution scan (3468 x 2298 pixels) and recorded as named sign tokens (work/transcription.txt). The cipher was broken from word patterns: a two-sign word occurring three times gave TO, a lone sign gave I, a seven-sign word with a repeated sign in positions 4 and 6 gave MORNING, and an eight-sign word with three equal signs gave RECEIVED. These fixed enough letters to read YOUR POSTAL CARD, THIS, HEARD OF IT, HURRIED, GRANDMA'S, MOUNTAINS, AUNT LUCY and GOODNIGHT, after which every sign of the card was assigned.

The writer separates L (a cross with one bar) and N (a vertical with two bars) only by the number of bars; every one of these signs was checked on an enhanced montage. Where the watermark overlies pencil, pencil strokes were separated from the watermark by their colour fringe (the watermark is a digital overlay with none).

Both sides were searched for hidden writing (steganography). The card is a pre-printed postal card with an imprinted indicium, so there is no adhesive stamp under which a message could be hidden; the address side shows only printed text, the postmark and killer, the address, the pencil "51" and a few faint pencil strokes at the lower left that form no letters. Nothing else is written on the message side.

A short web search found no published solution of this card.

## Key

Simple monoalphabetic substitution (MASC) with invented symbols; English; word spaces and punctuation (full stop, comma, apostrophe) written in clear. The alphabet is built systematically from shape families: slashes for A/B, the X family for C/D/E, the circle family for F/G/H/I, crosses for L/M/N, corners for O/P/R, boxes for S/T/U, arches for V/W.

| Sign | Letter | Sign | Letter |
|---|---|---|---|
| / slash | A | vertical with two bars | N |
| \ backslash | B | hook (rounded 7) | O |
| X | C | top-left corner | P |
| X with horizontal bar | D | bottom-right corner | R |
| X with vertical bar | E | open-top box | S |
| plain circle (small tick at top) | F | square | T |
| circle with dot | G | square with dot | U |
| circle with horizontal bar | H | arch with feet | V |
| circle with vertical bar | I | arch with feet and dot inside | W |
| cross with one bar (+) | L | arrow up | Y |
| # | M | | |

Twenty-one letters occur; J, K, Q, X and Z do not. Frequencies on the card (163 signs): A12 B1 C5 D10 E14 F2 G8 H8 I15 L4 M3 N12 O13 P2 R12 S8 T19 U6 V3 W2 Y4.

## Plaintext

As decoded, line by line:

```text
RECEIVED YOUR POSTAL CARD
THIS MORNING. I HEARD OF IT
LAST NIGHT, SO I HURRIED TO GET
IT. I WENT RIGHT UP TO GRANDMA'S
AND SENT THE CARD OVER TO THE
MOUNTAINS BY AUNT LUCY. GOODNIGHT.
O. W. L.
GAY AND FESTIVE.
CIDER
```

The last two lines stand apart at the bottom left and bottom right of the card.

English (normalised): **"Received your postal card this morning. I heard of it last night, so I hurried to get it. I went right up to Grandma's and sent the card over to the mountains by Aunt Lucy. Good night. O. W. L." Bottom left: "Gay and festive." Bottom right: "Cider".**

Slovak translation: **"Dostal(a) som tvoj korešpondenčný lístok dnes ráno. Počul(a) som o ňom včera večer, tak som sa ponáhľal(a), aby som ho dostal(a). Išiel (išla) som hneď hore k babičke a poslal(a) som lístok do hôr po tete Lucy. Dobrú noc. O. W. L." Vľavo dole: "Veselý a sviatočný." Vpravo dole: "Cider" (jablčný mušt).**

The text is a natural reply in 19th-century American English: the writer received a postal card, collected it in a hurry, and sent it on "over to the mountains" with Aunt Lucy. It fits the card itself (a postal card posted in Santa Clara to San José).

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1183/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the two source scans and the high-resolution message scan, decodes work/transcription.txt with work/key.json, and prints the nine lines above. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

- **L and N.** Distinguished only by one or two bars. LAST, POSTAL and LUCY have one bar; MORNING, NIGHT, WENT, AND, SENT, MOUNTAINS, AUNT, GOODNIGHT and GRANDMA'S have two. In WENT, SENT and AUNT the second bar is fainter but visible.
- **AND at the bottom left.** The N sign has a faint shorter stroke to its left, which could make it look like # (M); AMD is not a word, so N rests partly on word sense and on stroke weight (the extra stroke looks like a false start).
- **CIDER at the bottom right.** It lies under the watermark. C, I and D are visible; the vertical bar of E is only faintly visible, and the R is partly masked by watermark letters. E and R therefore rest partly on word sense (a plain X would give CIDCR).
- **Meaning of the closing.** "Gay and festive." and "Cider" read letter for letter, but whether they are a joke, a nickname or a postscript is not clear from the card.
- **O. W. L.** Three initials with stops, partly under the watermark but legible. They may be the sender's initials or a playful signature ("owl"); the card does not say.
- **A stray dot** after the H of HURRIED is taken as an accidental mark, not a sign.
- **Date and people.** The postmark has no year; the 1873–1881 range rests on the indicium type and was not checked against a philatelic catalogue. The addressee's surname (Brimblecom or Brimblecone) and the identity of the writer are not established.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), wrote its own decoder with a key typed from its own reading of the scan, and obtained the same plaintext, with 163 signs, 21 sign types, a one-to-one key and no unknown sign. It checked every line against the high-resolution scan in its own crops, including the L/N bars, the D/E distinction, F against G and H, GOODNIGHT and the initials under the watermark, and CIDER. It agreed that no steganography is present and that no published solution exists. Its four findings were minor:

- **Letter count.** The solution said twenty letters occur; the correct number is 21. Corrected here and in SOLUTION.md.
- **CIDER.** E and R rest partly on word sense; kept as an uncertainty above.
- **Closing words.** The meaning of "Gay and festive." / "Cider" is unclear but every letter decodes; stated above.
- **Address side.** Faint pencil strokes at the lower left besides the "51" are now mentioned; they are not letters.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1183, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1183 (source/metadata.md).
- Message side: https://api.hcportal.eu/media/3609/ (converted scan in source/, original in work/hires/).
- Address side: https://api.hcportal.eu/media/3610/ (converted scan in source/, original in work/hires/).
- Collection background: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.
