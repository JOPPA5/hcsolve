# HCP 1016 — German Pigpen postcard to Mariechen Kühnast (Rüdesheim picture card, posted in Berlin, 1898)

**Status: complete reading; review 1 verdict ACCEPT (see Response to review 1).** All 94 cipher glyphs on the card are decoded with one fixed key; 93 are read from the pixels and one (the R of KRAEFTIGON, under the watermark) is restored from context. Two writer-level anomalies (MEINES, KRAEFTIGON) are kept literally and disclosed below.

## Provenance and credit

- Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1016, name `cpc_1898-11-16_DE_Berlin_DE_Berlin_mariechen-02`, status **Not solved**, tags Postcard / T. Schrödel Collection / Pigpen, no attached transcription or solution (see `source/metadata.md`, `SOURCES.md`).
- Picture side: lithographed "Gruss aus Rüdesheim" (Rochuskapelle, Rüdesheim, Mäuseturm). Address side: "Fräulein Mariechen Kühnast, Berlin S., Kottbuser Damm"; Berlin postmark and the Berlin delivery stamp "Bestellt vom Postamte 59, 16/11 98". The address side carries no cipher.
- The linked Schrödel (HistoCrypt 2021) collection paper was checked earlier (copy at `../hcp-1081/source/schrodel-2021.pdf`) and gives no individual solution of this card. No published solution was used.
- Earlier work: the key, the 90-glyph transcription of the five rows and signature, and the pixel audits in `work/` (`decode.py`, `transcript.json`, `opening-audit.md`, `compare-boxes.py`) were produced by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26/27, which left the card partial. Claude Opus 5.5 (2026-10-29/30) re-read every glyph on its own enlarged crops, read the four small glyphs before the signature as **DEIN** (previously taken as the date "1898"), identified the drinking idiom that explains KOMME, and wrote `work/decode_full.py`.
- Sister cards to the same recipient, HCP 995 and HCP 905 (both FINAL in this repo), use the identical key.

## Cipher type and key

Pigpen (monoalphabetic substitution), German convention with I/J sharing one cell, so the dotted grid runs K–S. Shape names give the strokes drawn: SE=┘, S=⊔, SW=└, E=⊐, O=□, W=⊏, NE=┐, N=⊓, NW=┌; a trailing `.` means an interior dot.

| Shape | ┘ | ⊔ | └ | ⊐ | □ | ⊏ | ┐ | ⊓ | ┌ |
|---|---|---|---|---|---|---|---|---|---|
| plain | A | B | C | D | E | F | G | H | I/J |
| dotted | K | L | M | N | O | (P) | (Q) | R | S |

Extra signs: vertical stroke | = T, V/check = U, dotted upward wedge ∧· = Z. P, Q and the V/W/X/Y signs are not attested on this card. A short dash is the word separator.

## Plaintext

Literal decoded text (line breaks as on the card):

```
MEINES - LIEBE -
HERZIGEN - MAEUSCHEN
KOMME - ICH - EINEN - KRAEFTIGON -
SCHLUCK - UND - EINEN - SUESSEN -
GUTENACHTKUSS
                 DEIN  THEO
```

Normalised German: *Meinem lieben herzigen Mäuschen komme ich einen kräftigen Schluck und einen süßen Gutenachtkuss. Dein Theo.*

"Einem einen (Schluck) kommen" is the 19th-century student/drinking-custom phrase for drinking to someone's health (cf. "ich komme dir einen Halben"); it suits the wine-town picture ("Gruss aus Rüdesheim") on a card that was itself posted locally in Berlin (BERLIN S. departure postmark, Berlin delivery stamp 16/11 98), and explains the earlier "unresolved" KOMME.

English: "To my dear, sweet little mouse I drink a hearty gulp, and [send] a sweet goodnight kiss. Your Theo."

Slovak: „Na zdravie môjho milého, zlatého myšiačika si dávam poriadny dúšok a [posielam] sladký bozk na dobrú noc. Tvoj Theo."

## Command

From the repository root:

```
python3 -I ciphers/hcp-1016/work/decode_full.py
```

It checks the SHA-256 of `source/picture.jpg` and `source/address.jpg`, decodes all 94 manually transcribed shape tokens (rows, small closing word, signature) with the single key above, and prints the literal plaintext and the normalisation. The transcription is manual (not OCR); approximate original-image coordinates are given per row in the script and per glyph for the first 90 glyphs in `work/transcript.json`.

## Uncertainties and anomalies

1. **MEINES** (row 1, glyph 6 at ≈594,438): clearly ┌ with a dot = S. Dative grammar needs MEINEM (└· = M, a vertically flipped sign). Kept literally; most likely a writer's slip or loose grammar.
2. **KRAEFTIGON** (row 3, ≈944,518): the penultimate box has a distinct central dot (O), checked against undotted E controls in `work/box-controls-unenhanced.png`. Intended "kräftigen"; literal O kept.
3. **LIEBE** (row 1): no final N; "lieben" or a compound "liebeherzigen" is editorial.
4. **DEIN** (≈519–604, 592): small, lighter glyphs ⊐ □ ┌ ⊐·. The third sign has a short leftward overshoot at its top-left corner; read as ┌ = I. The dot in the fourth is small but visible near the top inside the bracket. Earlier work treated this group as a date "1898"; the shapes are Pigpen signs, and "Dein Theo" is the standard closing.
5. The verb object "einen süßen Gutenachtkuss" depends loosely on "komme"; the bracketed [send] in the translations is editorial.
6. The curved stroke under the printed title (≈760,420) is part of the printed lettering/flourish, not cipher.
7. **R of KRAEFTIGON (row 3, sign 3.15, ≈739,518) is restored from context.** The sign lies under the grey watermark letters of "HISTORICAL"; a vertical and a top stroke compatible with ⊓ are visible, but they cannot be separated from the watermark and no dot is distinguishable. R is supplied by the surrounding K-A-E-F-T-I-G. The S of MAEUSCHEN (2.13) and the second S of SUESSEN (4.20) are also crossed by watermark strokes, but their top bar and dot are visible.
8. The pencil notes "Hessen 1898 9" at the top left of the address side are a later collector's/dealer's note, not part of the message.
9. Same-family key transfer: the key was first established on this card by the earlier solver and later reused on 995/905; no blind test.

## Why it is correct

- One fixed key decodes all 94 glyphs (93 legible, one restored under the watermark, see uncertainty 7) into continuous German with no unmapped sign; only two single-glyph anomalies remain, both kept literally.
- Independent long words (HERZIGEN, MAEUSCHEN, SCHLUCK, SUESSEN, GUTENACHTKUSS) each confirm several key cells, including the dotted K/L/M/N/O/R/S cells and the I/J merge.
- The content fits the context: a Rüdesheim wine-town picture card posted in Berlin, a goodnight-kiss love note to Mariechen, signed "Dein Theo", same key as the other cards to Mariechen Kühnast (HCP 995, 905).

## Response to review 1

Review 1 (Claude Opus 5.5, verdict ACCEPT) confirmed the reproduction command and agreed with the reading in all 94 positions using an independent transcription and decoder. Responses, finding by finding (Claude Opus 5.5, 2026-10-30):

1. **R of KRAEFTIGON restored, not read (minor) – fixed.** Agreed. On `review/work/r3stamp_color.png` the sign at ≈739,518 is overlaid by the watermark letters A/L/C; only strokes compatible with ⊓ are visible and no dot can be seen. Added as uncertainty 7; the status line and "Why it is correct" now say 93 glyphs are read and one restored from context. The watermark-crossed S signs of MAEUSCHEN and SUESSEN are noted there as legible. No change to the decoded text.
2. **Place of sending (minor) – fixed.** Agreed: `source/address.jpg` shows a BERLIN S. departure postmark and the delivery stamp "Bestellt vom Postamte 59, 16/11 98"; the card is a Rüdesheim picture card posted locally in Berlin. Title and the idiom paragraph corrected; the report states this.
3. **Idiom reference and editorial marking (minor) – fixed.** The reading "einem einen (Schluck) kommen" = to drink to someone is the student drinking usage recorded under *kommen* in Grimm's Deutsches Wörterbuch (the entry was not re-consulted online in this session, so it is given as a pointer). The report marks the idiom interpretation, the bracketed [send], and the dependence of "einen süßen Gutenachtkuss" on "komme" as editorial.
4. **Pencil notes on the address side (minor) – fixed.** Confirmed on `source/address.jpg`: "Hessen 1898" and "9" in pencil at top left, a later collector's/dealer's note. Added as uncertainty 8 and described in the report.

The reproduction command was re-run after these edits (unchanged script): both hashes OK, 94 glyphs decoded, same literal plaintext. The reading is unchanged, so the card proceeds to FINAL.
