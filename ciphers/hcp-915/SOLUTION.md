# hcp-915 — Solution (round 1)

Solver: Claude Opus 5.5, 2026-11-03. No earlier work on this number; no published solution found or attached on the portal (status Not solved). The transcription is my own (portal attaches none).

## The card
Irish comic postcard, "Lawrence, Publisher, Dublin", printed caption in Gaelic type "Arrah na pogue" / "Give me a kiss" (the title of Dion Boucicault's 1864 Irish play; the scene shows a man kissing a girl). Address side is blank: no address, no stamp, empty stamp box, no writing along the edges. All writing is in pencil on the picture side, left of the image, written with the card turned 90 degrees:
1. an Ogham line on a drawn stem line (the cipher);
2. beside it (above it when the card is turned so that the lines read left to right), the same text in Irish written in Gaelic (insular) script, unenciphered.

## Cipher type and key
Ogham alphabet (Irish), i.e. a simple monoalphabetic substitution by a fixed script — register label MASC. Standard table, horizontal stem read left to right:
- B-aicme, strokes below the stem only: 1 b, 2 l, 3 f, 4 s, 5 n
- H-aicme, strokes above the stem only: 1 h, 2 d, 3 t, 4 c, 5 q
- M-aicme, slanted strokes across: 1 m, 2 g, 3 ng, 4 z, 5 r
- vowels, perpendicular strokes across: 1 a, 2 o, 3 u, 4 e, 5 i
- a horizontal bar above the stem = p (peith); dot above = lenition (séimhiú); acute above = fada; two dots (:) = word separator.

Transcription (work/transcription.txt, read from 3–5x enlargements of work/hires/cpc_--_IE_____pic.jpg):
`H2 X1 B1^ X1 X5 M5 : H2 X2 M1 : P X2' M2 .`

## Plaintext
- Ogham, letter for letter: `dabair dom pog.`; with its marks (dot over b, acute over o): `dabhair dom póg.`
- Plain Gaelic-script line under it: `Taḃair ḋom póᵹ` = `Tabhair dom póg`
- Irish: **Tabhair dom póg.**
- English: Give me a kiss.
- Slovak: Daj mi bozk. (Pobozkaj ma.)

It is the Irish rendering of the printed English caption "Give me a kiss".

## Command
From the repo root: `python3 -I ciphers/hcp-915/work/decode.py` (checks SHA-256 of all four images, decodes the transcription with the table above, prints the reading).

## Uncertainties
1. First Ogham letter: clearly two strokes above the stem (verified at 4x; no third stroke, no trace), which in the standard table is D, not T. The plain-script line has T and the phrase is "tabhair", so this is a writer's slip (2 instead of 3 strokes) or a dialect-like voicing; the letter-for-letter reading `dabhair` is reported as is, and the T rests on the parallel plain line and word sense.
2. The lenition dot in word 1: in the Ogham it stands after the b-stroke, not directly over it (slightly right of the second a-stroke, above the a/i area); in the Gaelic-script line it sits between b and a. I assign it to b (bh) from the spelling "tabhair", not from its position. (Corrected after review 1, finding 3.)
3. The Ogham "dom" carries no lenition dot, while the script line has ḋ (ḋom, the old spelling of dhom/dom). Both are acceptable Irish.
4. The horizontal bar for P: the standard Ogham forfeda give no fixed universal form for p; a bar above the stem is used here, and only p fits "póg". Rests on word sense.
5. The final dot below the stem is read as a full stop.
6. No date, sender, recipient or stamp; dating (c. 1900–1910, Lawrence of Dublin undivided-style card) is only from the printed card. No hidden writing found in the stamp box or the picture at the available resolution.

## Why I believe it is correct
Every mark on the card is accounted for (15 Ogham tokens: 12 letter groups, 2 word separators and 1 final dot, plus 2 diacritics, the lenition dot and the acute; 3 words; count corrected after review 1, finding 4); the Ogham decodes under the standard table to a grammatical Irish sentence, it is duplicated by the plain Gaelic-script line under it, and it translates exactly the printed caption "Give me a kiss". The fada over o and the dot of lenition are placed where Irish orthography needs them.

## Response to review 1

Verdict ACCEPT, six minor findings / notes. The reading is unchanged.

1. D vs T (minor) – agreed, nothing to fix. Re-checked on work/strip_upright.jpg (new upright crop of the hires scan): the first group has two strokes above the stem only. The letter-for-letter reading stays `dabair`; T rests on the parallel plain line and word sense.
2. P as a bar (minor) – agreed, already disclosed as uncertainty 4; nothing to fix.
3. Dot position (minor) – fixed. Uncertainty 2 now says the Ogham dot stands after the b-stroke (slightly right of the second a-stroke), not directly over b or the b/a gap; in the script line it is between b and a. The assignment to b is from spelling. Visible on work/strip_upright.jpg.
4. "17 groups" (minor) – fixed. The count now reads 15 Ogham tokens (12 letter groups, 2 separators, 1 final dot) plus 2 diacritics. decode.py now also prints the counts it decodes (`12 letters, 2 separators, 1 final dot`).
5. Script line hard-coded (minor) – fixed in work/decode.py: the line is now labelled "manual reading, plain writing, not computed" with a comment; the report says the same. Re-ran `python3 -I ciphers/hcp-915/work/decode.py`: all four hashes pass and the output is unchanged (`dabair dom pog.` / `dabhair dom póg.`).
6. Register type (note) – agreed. The card has no stamp (the printed STAMP box is empty and there is no trace of a removed stamp), the address side is blank and nothing is hidden along the edges or in the picture, so the human's remark about hidden messages under stamps (Arokszállás/Jolánka series) does not apply here. Type stays MASC (Ogham as a fixed-script letter substitution); no "+ Steganography".

Also corrected: the script line stands beside / above the Ogham in the upright view (it was described as "below it").
