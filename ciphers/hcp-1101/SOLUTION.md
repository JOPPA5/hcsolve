# hcp-1101 — Solution (round 1)

Postcard, T. Schrödel collection, HC Portal cryptogram 1101 (`cpc_1898-02-11_CH_Basel_CH_Basel_`).
Picture postcard (Postkarten-Verlag Vogel, Leipzig, No. 180), Swiss 5 c stamp, postmarked Basel 11 II 98,
to Fräulein Marie Müller, Dornacherstrasse 2?4 (house number partly covered by the collection stamp), Basel. Sender signs "H. B.".
Portal status: Not solved, no attached transcription or solution. A short web search found no published reading.
All work on this card by Claude Opus 5.5 (2026-11-03); there was no earlier work on this number.

## Cipher type and key

**Concealment (steganography), no cipher.** A six-line message in plain German (Latin cursive, black ink) on the picture side
is hidden under a dense red overlay: a grid of thick red horizontal/vertical bars plus red diagonal crosses and red
loop-scribbles that imitate handwriting. The red was drawn over the black ink (black strokes visibly run under the red bars).
The "key" is a red filter: seen through red glass (here: the red channel of the scan) the red overlay vanishes and the black
writing stands out. No letter substitution is involved. Register type label: `Steganography`.

The remark written openly above the block, "das isch suber" (Swiss German: "that is neat/clever"), comments on the trick.

## Plaintext (German, as written)

Open: `11/II/98` — `das isch suber`

Hidden under the red lattice:

    Weñ der früche Morgen lächelt
    Weñ des Abends Kühle fächelt
    Immer-immer denk ich dein
    In der Mitternächte Hülle
    Selbst in meiner Träume Stille
    Mischt dein schönes Bild sich ein.

Open: `Mit freundl. Gruss` — `H. B.`

Normalised: Wenn der frühe Morgen lächelt, / wenn des Abends Kühle fächelt, / immer, immer denk ich dein. /
In der Mitternächte Hülle, / selbst in meiner Träume Stille / mischt dein schönes Bild sich ein.

## English translation

11 Feb '98 — "That's a neat one."
When the early morning smiles, / when the evening's coolness fans, / always, always I think of you. /
In the shroud of midnights, / even in the stillness of my dreams / your lovely image mingles in.
With kind regards, H. B.

## Slovak translation

11. 2. 98 — „To je šikovné.“
Keď sa usmieva skoré ráno, / keď ovieva večerný chlad, / stále, stále myslím na teba. /
V závoji polnocí, / aj v tichu mojich snov / sa vmiesi tvoj krásny obraz.
S priateľským pozdravom, H. B.

## Command (run from repo root)

    /Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1101/work/decode.py

It checks the SHA-256 of all four scans, writes `work/redfilter.png` (red channel of the hi-res picture side, the
"red glass" view), and prints the transcription read from that image plus the normalised text.
The transcription itself is a reading of the pixels, not something a program computes; the filtered image is the evidence.

## Uncertainties

- "früche": the pen clearly has f-r-ü plus a c-like stroke before "he"; read literally as "früche", meaning "frühe".
  Whether the c-stroke is a slip or part of the ü/h join rests on word sense; the meaning is not affected.
- "Weñ" (twice) is written with a nasal bar over n = "Wenn".
- "Mit freundl. Gruss": the first word has an overwritten/blotted letter (looks like "Mitt" with an f started over it); read "Mit".
- "H. B." are initials only; the sender is not identified. The house number on the address side is partly covered
  by the collection stamp (2?4); not part of the message.
- The stamp (address side) could not be lifted; nothing visible suggests writing under it. No other marks were found on
  the picture border or edges.
- Source of the verse not identified (web search for the opening lines gave nothing); it reads as a period album/love verse
  with regular trochaic metre and rhyme lächelt/fächelt, Hülle/Stille, dein/ein.

## Why it is correct

Every word of the hidden block is legible in the red-channel image without guessing (one spelling oddity noted);
the six lines form a rhymed, metrical German love verse; the open words (date matching the Basel postmark 11 II 98,
Swiss German "isch suber", Basel address, Swiss stamp) fit a Basel writer in 1898. The overlay is entirely red and the
writing entirely black, so the red-filter reading is exactly what the concealment intended.

## Response to review 1

Review 1 verdict: ACCEPT, three minor findings. No reading changed. The reproduction command was re-run on 2026-11-03 after this response: all four hashes OK, `work/redfilter.png` rewritten, output identical to the text above.

1. **German printed form (minor) — accepted, context added.** The address side is a pre-printed "Deutsche Reichspost / Postkarte" form (publisher Vogel, Leipzig; view credited "R. Loës ph."), franked with a Swiss Helvetia 5 c stamp and posted in Basel on 11 II 98. A German-printed picture card bought and used in Switzerland is not unusual; it does not affect the reading. Recorded here and in the report.
2. **"früche" (minor) — accepted as an alternative.** The letters f-r-ü-c-h-e stand on the card (both solver and reviewer read them). Two explanations: a slip for standard "frühe", or a dialect-coloured spelling influenced by Swiss German "früech" (early). The meaning "early" is the same either way; the literal transcription keeps "früche".
3. **Pen marks (minor) — accepted.** The hyphen in "Immer-immer" is kept as written. The short stray slash after "Hülle" (line 4) is a pen stroke, not a letter or punctuation of the verse, and is left out of the transcription; this is now stated here and in the report.

Human remark on stamp-box steganography (passed on for the Jolánka series): checked again on this card. The hi-res address side shows the 5 c stamp with clean edges and nothing written around or beside it; the stamp cannot be lifted from a scan, so writing under it cannot be excluded. The type stays `Steganography`, not `MASC + Steganography`: the hidden verse is plain German, nothing on the card is enciphered.
