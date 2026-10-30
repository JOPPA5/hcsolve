# HCP 1016 (cpc_1898-11-16_DE_Berlin_DE_Berlin_mariechen-02): a Pigpen goodnight card to Mariechen in Berlin

Human solver: Tomáš Pavuk

**Status: all 94 cipher glyphs deciphered (93 read from the scan, one restored from context under the watermark); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1016 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1016), portal name cpc_1898-11-16_DE_Berlin_DE_Berlin_mariechen-02, from Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, Pigpen, category Substitution / Monoalphabetic, date 1898-11-16, language Unknown, location Europe, sender Unknown, recipient Mariechen Kühnast, with no transcription or solution attached. The collection is described in Schrödel's HistoCrypt 2021 paper (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166); a check of that paper found no individual solution of this card.

The picture side is a lithographed view card **"Gruss aus Rüdesheim"** (Rochuskapelle, a view of Rüdesheim above the Rhine with vineyards, and the Mäuseturm), printed by Louis Glaser, Leipzig. Below the title the writer added five rows of Pigpen, then a small four-sign word and a four-sign signature at the bottom right.

The address side is in plain writing: **Fräulein Mariechen Kühnast, Berlin S., Kottbuser Damm.** The 5-pfennig stamp is cancelled **BERLIN S.** with the day 16, and the Berlin delivery stamp reads **Bestellt vom Postamte 59, 16/11 98**. The card was therefore a Rüdesheim picture card **posted locally in Berlin** and delivered the same day, 16 November 1898, in agreement with the portal date; it was not sent from Rüdesheim. The pencil notes **"Hessen 1898"** and **"9"** at the top left of the address side are a later collector's or dealer's note, not part of the message. The address side carries no cipher.

Two other cards to the same recipient in this repository, HCP 995 (Bonn → Berlin, 1900) and HCP 905, use the identical Pigpen key.

![Picture side: "Gruss aus Rüdesheim", five Pigpen rows below the title, the small word DEIN and the signature THEO at the bottom (source/picture.jpg)](../source/picture.jpg)

![Address side: Fräulein Mariechen Kühnast, Berlin S., Kottbuser Damm; BERLIN S. cancellation and the delivery stamp "Bestellt vom Postamte 59, 16/11 98"; pencil collector's note "Hessen 1898 9" at top left (source/address.jpg)](../source/address.jpg)

## Method

The transcription is **manual** (no OCR; the portal supplied none). The scan is small and light, so each row was read sign by sign from 3–7× enlarged crops of the original image. Every sign is recorded as a shape token (which sides of the cell are drawn, and whether it has an interior dot).

Conventional English Pigpen (dotted cells J–R) gave nonsense. The German convention, in which I and J share one cell so that the dotted grid runs K–S, immediately produced ICH, EINEN and HERZIGEN, and then, without further change, the long independent words of the lower rows: SCHLUCK, SUESSEN, GUTENACHTKUSS and the signature THEO. Doubtful places were checked against controls from the same card: undotted and dotted boxes were compared at the same scale without contrast enhancement (to decide E against O), and the end of row 5 was segmented as a separate upright stroke T followed by a dotted corner K, not one malformed cup.

The earlier solver took the four small signs before the signature for a date "1898". On enlargement they are Pigpen signs ⊐ □ ┌ ⊐·, which read **DEIN**, giving the ordinary closing "Dein Theo".

In review a separate agent made its own crops, read all 94 glyphs itself, generated the key from the German 25-letter grid with its own script, and obtained the identical plaintext in every position.

## Key

Pigpen (monoalphabetic substitution), German grid with I/J in one cell. ┘ means a cell drawn with its right and bottom sides, and so on; · marks an interior dot.

| Sign | ┘ | ⊔ | └ | ⊐ | □ | ⊏ | ┐ | ⊓ | ┌ |
|---|---|---|---|---|---|---|---|---|---|
| Undotted | A | B | C | D | E | F | G | H | I/J |
| Dotted | K | L | M | N | O | (P) | (Q) | R | S |

| Sign | upright stroke | check-like v | dotted wedge ^· |
|---|---|---|---|
| Letter | T | U | Z |

A short dash on the card separates words. P, Q, V, W, X and Y do not occur; their signs are not attested on this card. Umlauts are written out as AE and UE, ß as SS.

## Plaintext

Ciphertext in the sign notation of the key table (/ = word dash):

```text
└· □ ┌ ⊐· □ ┌· / ⊔· ┌ □ ⊔ □ /
⊓ □ ⊓· ^· ┌ ┐ □ ⊐· / └· ┘ □ v ┌· └ ⊓ □ ⊐·
┘· □· └· └· □ / ┌ └ ⊓ / □ ┌ ⊐· □ ⊐· / ┘· ⊓· ┘ □ ⊏ | ┌ ┐ □· ⊐· /
┌· └ ⊓ ⊔· v └ ┘· / v ⊐· ⊐ / □ ┌ ⊐· □ ⊐· / ┌· v □ ┌· ┌· □ ⊐· /
┐ v | □ ⊐· ┘ └ ⊓ | ┘· v ┌· ┌·
                          ⊐ □ ┌ ⊐·
                                    | ⊓ □ □·
```

Literal German as decoded (94 letters):

```text
MEINES - LIEBE -
HERZIGEN - MAEUSCHEN
KOMME - ICH - EINEN - KRAEFTIGON -
SCHLUCK - UND - EINEN - SUESSEN -
GUTENACHTKUSS
                 DEIN  THEO
```

Normalised German (case, umlauts, ß, punctuation and the corrections MEINES → Meinem, LIEBE → lieben, KRAEFTIGON → kräftigen are editorial):

**Meinem lieben herzigen Mäuschen komme ich einen kräftigen Schluck und einen süßen Gutenachtkuss. Dein Theo.**

English translation: **To my dear, sweet little mouse I drink a hearty gulp, and [send] a sweet goodnight kiss. Your Theo.**

Slovak translation: **Na zdravie môjho milého, zlatého myšiačika si dávam poriadny dúšok a [posielam] sladký bozk na dobrú noc. Tvoj Theo.**

Notes on the reading (editorial interpretation):

- **komme ich einen … Schluck.** "Einem einen (Schluck) kommen" is a 19th-century student and drinking-custom phrase meaning to drink to someone's health ("ich komme dir einen Halben"); cf. Grimm, *Deutsches Wörterbuch*, s.v. *kommen* (given as a pointer; the entry was not re-consulted for this report). It explains the otherwise odd KOMME and requires a dative, which is why the first word is normalised to *Meinem*. The picture of the Rhine wine town suits the toast, but the card itself was posted in Berlin.
- **einen süßen Gutenachtkuss** depends only loosely on *komme*; the bracketed [send]/[posielam] in the translations is editorial.
- **herzig** ("sweet, darling") and **Mäuschen** ("little mouse") are ordinary terms of endearment of the period.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1016/work/decode_full.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of source/picture.jpg and source/address.jpg, decodes all 94 manually transcribed shape tokens (five rows, the word DEIN and the signature) with the single key above, asserts the glyph count, and prints the literal rows, the literal plaintext and the normalised reading. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **MEINES** (row 1, last sign): clearly ┌ with a dot = S. The dative needed by *komme* would be MEINEM (└· = M). Kept literally; most likely a slip or loose grammar.
- **KRAEFTIGON** (row 3): the penultimate box has a distinct central dot (O), checked against undotted E boxes from the same card. Intended *kräftigen*; the literal O is kept.
- **LIEBE** (row 1): no final N; *lieben*, or a compound *liebeherzigen*, is editorial.
- **R of KRAEFTIGON is restored, not read.** This sign lies under the grey watermark letters of "HISTORICAL"; strokes compatible with ⊓ are visible but cannot be separated from the watermark, and no dot is distinguishable. R is supplied by the surrounding K-A-E-F-T-I-G. The S of MAEUSCHEN and the second S of SUESSEN are also crossed by watermark strokes, but their top bar and dot are visible.
- **DEIN**: small, lighter signs; the I (┌) has a short overshoot at its top-left corner, and the dot in the final N is small but visible. Earlier read as a date "1898"; the shapes are Pigpen.
- The curved stroke under the printed title is part of the printed flourish, not cipher.
- The drinking-idiom interpretation and the bracketed [send] are editorial.
- The writer is known only as "Theo"; his identity and relation to the writers of HCP 995 and 905 (same key, same recipient) are not established.
- The key was first established on this card (by the earlier solver) and later reused on HCP 995 and 905; it was not tested blind on another card first.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), made its own enlarged crops, read every glyph itself and decoded its transcription with an independently generated key; its reading agreed with the solver's in all 94 positions. It checked the contested signs on the pixels (the S of MEINES, the E/O boxes of KOMME and KRAEFTIGON, the T + K segmentation in GUTENACHTKUSS, DEIN and THEO) and confirmed that no published solution exists. Its four findings were minor and are reflected here:

- **R under the watermark** is now listed as restored from context rather than read; the status line says 93 + 1.
- **Place of sending** corrected: a Rüdesheim picture card posted locally in Berlin, not sent from Rüdesheim.
- **Idiom** given a reference pointer and marked editorial, together with the bracketed [send].
- **Pencil notes** "Hessen 1898 9" on the address side identified as a later collector's note.

No decoded letter changed as a result of the review.

## Credit

The German Pigpen key, the first transcription of the five rows and the pixel audits were produced by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) on 2026-10-26/27, which left the card partial. Claude Opus 5.5 (2026-10-29/30) re-read every glyph, read the four small signs as DEIN, identified the drinking idiom that explains KOMME, wrote the full decoder, and prepared the response to review and this report. The review was done by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1016, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1016 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3108/conversions/cpc_1898-11-16_DE_Berlin_DE_Berlin_mariechen-02_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/3109/conversions/cpc_1898-11-16_DE_Berlin_DE_Berlin_mariechen-02_adr-large.jpg (source/address.jpg).
- Tobias Schrödel, Cryptographic postcards, HistoCrypt 2021: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- Sister cards to the same recipient in this repository: ciphers/hcp-995, ciphers/hcp-905.
