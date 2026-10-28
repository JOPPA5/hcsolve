# HCP 962 (cpc_1903-06-06_DE_Bonn_DE_Aachen_): a Pigpen love note from Bonn to Aachen

Human solver: Tomáš Pavuk

**Status: deciphered in full (117 of 117 cipher glyphs); independent review 1 verdict ACCEPT.** Report dated 2026-10-28.

## Origin and context

The cryptogram is record 962 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/962), portal name cpc_1903-06-06_DE_Bonn_DE_Aachen_, from Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-10-28 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, Pigpen, category Substitution / Monoalphabetic, date 1903-06-06, language Unknown, location Europe, sender Unknown, recipient Maria Peters, with no transcription or solution attached. The collection is described in Schrödel's HistoCrypt paper (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166); a bounded check of that paper found no individual solution for this card.

It is a German picture postcard (Dr. Trenkler Co., Leipzig, no. 12958). The picture side shows the new Rhine bridge at Bonn, captioned "Neue Rheinbrücke". The whole cipher is on the picture side: four short rows in the white inset at the lower right, under a handwritten pencil "Bonn", and two long rows along the bottom edge. The address side is in plain writing: **Fräulein Maria Peters, Aachen, Adalbertsteinweg 46.** The postage stamp is no longer on the card; the lower half of the departure stamp that remains reads "…03. 6-7 V." (morning), and the arrival stamp reads **AACHEN 1 ANKUNFT 6.6.03**. The card was therefore posted on the morning of Saturday 6 June 1903 and delivered in Aachen the same day, in agreement with the portal date.

![Picture side: the Rhine bridge at Bonn; the cipher is in the inset at the lower right and along the bottom edge (source/picture.jpg)](../source/picture.jpg)

![Address side: Fräulein Maria Peters, Aachen; arrival stamp 6.6.03 at the left (source/address.jpg)](../source/address.jpg)

Other marks on the card, none of them cipher: the printed caption and imprint, the HCPortal watermark, the pencil "Bonn", and faint, illegible violet pencil traces at the top right of the picture.

## Method

The transcription is **manual**: the solver read each glyph from enlarged crops of the original scan and recorded its shape, row and word in work/transcript.json. No OCR was used and the portal supplied no transcription.

The signs are Pigpen: corner, U-shaped and square cells of a tic-tac-toe grid, with and without a dot, plus angled signs (v, >, ^). A first attempt with the familiar one-letter-per-cell German Pigpen table did not fit. Reading recurring groups as a monoalphabetic substitution instead showed a regular alphabet in which each grid cell holds a **pair** of consecutive letters (AB, CD, EF, GH, IK, LM, NO, PQ, RS, with J omitted), the dot selecting the second letter; the angled signs carry TU, VW, XY and Z the same way. This single key turns all six rows into connected German. The card has 117 cipher glyphs (11 + 13 + 11 + 13 + 39 + 30), one of them with an umlaut.

In review the reviewer re-read every glyph from its own upscaled crops before comparing, and decoded them with an independently written script. Its reading agrees with the solver's in all 117 positions. It checked in particular the H that begins the anomalous word HORGEN, the Ü of ZURÜCK, the D of DER, the four S's of GRUSS and KUSS, and the undotted squares (I, not K).

## Key

One fixed key for the whole card. Undotted sign = first letter of the pair, dotted sign = second. "Walls" names the lines drawn: t top, b bottom, l left, r right.

| Sign | ┘ | ⊔ | └ | ⊐ | □ | ⊏ | ┐ | ⊓ | ┌ |
|---|---|---|---|---|---|---|---|---|---|
| Walls | br | lbr | bl | tbr | tblr | tbl | tr | tlr | tl |
| Undotted | A | C | E | G | I | L | N | P | R |
| Dotted | B | D | F | H | K | M | O | Q | S |

| Sign | v | > | < | ^ |
|---|---|---|---|---|
| Undotted | T | V | X | Z |
| Dotted | U | W | Y | – |

J is not in the alphabet. P, Q, W, X and Y do not occur on the card; their cells follow from the regular pattern and are not attested. Ü is written as the dotted v with two additional dots above it.

This writer places dots loosely. In KOMME and HORGEN the dot of ┐· (O) sits just above the top bar rather than inside the corner, and in UNTER, GRUSS, UND and KUSS the dot of v· (U) sits above the v (in ZU it is inside). Each of these signs is still clearly dotted.

## Plaintext

Ciphertext as written, in the sign notation of the key table (· = dot, ¨ = umlaut, / = word gap):

```text
⊏ □ └ ┘· └ ┌  /  └ ┐ ⊐ └ ⊏  !
⊔· □ ┌  /  ^ v·  /  ⊐ └ └· ┘ ⊏ ⊏ └ ┐
□· ┐· ⊏· ⊏· └  /  ⊐· ┐· ┌ ⊐ └ ┐
^ v· ┌ v·¨ ⊔ □· .  /  ┘· □ ┌·  /  ┌· ┐· ┐ ┐ =
v ┘ ⊐ / ┐ ┘ ⊔ ⊐· / ⊔· └ ┌ / ⊏· └ ┌· ┌· └ / > └ ┌ ┘· ⊏ └ □ ┘· └ /
  v· ┐ v └ ┌ / ⊐· └ ┌ ^ ⊏ □ ⊔ ⊐· └ ⊏·
⊐ ┌ v· ┌· ┌· / v· ┐ ⊔· / □· v· ┌· ┌· / ⊔· └ □ ┐ / ⊔· □ ⊔ ⊐· /
  ⊏ □ └ ┘· └ ┐ ⊔· └ ┌ / ⊏·
```

(The fifth and sixth rows are each one line on the card; they are wrapped here.)

Literal German, as decoded, line for line (the "!", the full stop after ZURÜCK and the "=" hyphen are on the card):

```text
LIEBER ENGEL!
DIR ZU GEFALLEN
KOMME HORGEN
ZURÜCK. BIS SONN=
TAG NACH DER MESSE VERBLEIBE UNTER HERZLICHEM
GRUSS UND KUSS DEIN DICH LIEBENDER M
```

The third row really reads HORGEN: its first sign is ⊐· (open to the left, H), clearly different from the two ⊏· (open to the right, M) of KOMME just before it. This is a writer's slip, mirroring one sign, and is kept in the literal text.

Normalized German (spelling of 1903, punctuation editorial, [morgen] an editorial correction of the literal HORGEN):

**Lieber Engel! Dir zu Gefallen komme [morgen] zurück. Bis Sonntag nach der Messe! Verbleibe unter herzlichem Gruß und Kuß dein dich liebender M.**

English translation: **Dear angel! To please you, I am coming back [tomorrow]. See you on Sunday after Mass! With heartfelt greetings and a kiss I remain your loving M.**

Slovak translation: **Milý anjel! Tebe na potešenie sa [zajtra] vrátim. Do nedele po omši! So srdečným pozdravom a bozkom zostávam tvoj ťa milujúci M.**

Why MORGEN: the card was written on Saturday 6 June 1903 (the departure stamp gives the morning hour and it arrived in Aachen the same day). "Komme morgen zurück" then means Sunday 7 June, exactly the day named in "bis Sonntag nach der Messe". Grammar, context and the dates all point to MORGEN; the cipher itself says HORGEN.

Alternative parse: the card has no punctuation after MESSE, so the sentence can also run on: "Bis Sonntag nach der Messe verbleibe unter herzlichem Gruß und Kuß …" ("Until Sunday after Mass I remain, with heartfelt greetings and a kiss, your loving M."). The farewell parse above is preferred, because "Verbleibe … dein dich liebender" is the standard closing formula of the period.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-962/work/decode.py
```

The script checks the SHA-256 hashes of both scans and the metadata, decodes the manual shape transcription with the key above, prints the six rows, checks that all 117 glyphs decode and re-encode to their transcribed shapes, and lists the unattested cells (P, Q, W, X, Y). It does not read the image; the transcription step is manual (and was confirmed independently in review). It prints the literal text, with HORGEN.

## Uncertainties

- The sender "M" is not identified, nor is the relationship to Maria Peters. The initial is not expanded.
- MORGEN is an editorial correction of the literal HORGEN. It is strongly supported by the dates, but the cipher reads HORGEN.
- "Bis Sonntag nach der Messe" can be read as a separate farewell (preferred) or as part of the closing sentence.
- The departure town and the day on the departure stamp are illegible; the Bonn origin rests on the picture, the pencil "Bonn" and the portal name. The date rests on the arrival stamp 6.6.03 and the portal metadata.
- The violet pencil traces at the top right of the picture are illegible; they are not Pigpen.
- There was no blind held-out test: all rows were visible while the key was found. The key is a regular pattern, not fitted word by word, and it decodes every glyph.
- No search for a prior publication was made beyond the portal status (Not solved), the AI Decipherment Register (158 contributions, this card absent) and a bounded check of Schrödel's paper, all on 2026-10-28.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, read all 117 glyphs from its own crops of the scan before comparing, decoded them with an independently written script, and found no differences. It confirmed that one regular key covers every glyph, that HORGEN is the literal reading and not a misreading, and that the rest of both sides contains no other Pigpen. Its four findings were minor and are reflected here:

- All writing that is not cipher is now listed: the pencil "Bonn", the violet traces, the address and both postmarks.
- The weekday and postmark evidence (Saturday 6 June 1903, delivered the same day) is now used to support MORGEN = Sunday, while MORGEN stays an editorial correction.
- "Bis Sonntag nach der Messe" is now read as a farewell of its own, with the solver's run-on parse kept as an alternative.
- The report says that this writer places dots loosely (above ┐ and v rather than inside).

No change to the decoded letters resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 962, General, Description and Attachments tabs, captured 2026-10-28: https://crypto.hcportal.eu/dashboard/cryptograms/962 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/2946/conversions/cpc_1903-06-06_DE_Bonn_DE_Aachen__pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/2947/conversions/cpc_1903-06-06_DE_Bonn_DE_Aachen__adr-large.jpg (source/address.jpg).
- T. Schrödel, collection paper in HistoCrypt: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 (copy in ciphers/hcp-1081/source/schrodel-2021.pdf).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-28.
