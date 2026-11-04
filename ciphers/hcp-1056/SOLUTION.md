# hcp-1056 – PARTIAL solution (no DONE marker)

Solver: Claude Opus 5.5, 2026-11-03. No earlier work on this number; no published solution found.

## Cipher type and key
Partial monoalphabetic digit substitution inside plain German Kurrent text (MASC): only some letters are replaced by digits, the rest stay plain.

| digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| letter | a | e | i | o | u | l | n | m | r | s |

Same key on sister card hcp-910 (same sender): "eine klaine bitte", "in Urlaub komme", "noch".

## Command
`python3 -I ciphers/hcp-1056/work/decode.py` (checks source hashes, prints each cipher group and its decoding).

## Reading (partial)
German: Ulm, den 9.(?) 17. Liebe Eltern! Das mir von Euch zugesandte [noun not read] m[it] [1–2 words under postmark] Freude(?) erhalten, wofür ich mich bestens bedanke. Habe diser Tage um [korchus?] Urlaub eingegeben und werde es Euch gleich mitteilen, wann ich fahren kann. Noch 1000 Grüße sowie auch nochmals besten Dank für die Gabe. Schließe nun im besten Hoffen auf baldiges frohes Wiedersehen, sendet Euer dankschuldiger Sohn M. Zwick. Ich war diser Tage auf dem Minster, mind. 778 Stufen.

Enciphered parts: korchus(?) urlaub eingegeben / war diser Tage auf dem miinster / mind.

English: Dear parents! The [...] you sent me I received [...] with joy(?), for which I thank you very much. These days I have applied for [?] leave and will let you know at once when I can travel. Another 1000 greetings and once more many thanks for the gift. I close in the best hope of a soon happy reunion, your grateful son M. Zwick. These days I was up the Minster, at least 778 steps.

Slovak: Milí rodičia! [...], ktorý ste mi poslali, som dostal [...] s radosťou(?), za čo sa vám veľmi pekne ďakujem. V týchto dňoch som podal žiadosť o [?] dovolenku a hneď vám dám vedieť, kedy budem môcť prísť. Ešte 1000 pozdravov a ešte raz veľká vďaka za dar. Končím v najlepšej nádeji na skoré radostné zvidenie, váš vďačný syn M. Zwick. V týchto dňoch som bol na Münsteri (Ulmský dóm), najmenej 778 schodov.

## Uncertainties (why partial)
- The leave type before "Urlaub" decodes k-o-r-?-u-s with an unidentified double sign (read as Kurrent ch): not understood.
- Plain line 2 is under the postmark: the noun after "zugesandte" and the words after "mit" are not read.
- "miinster" has two 3s as read; 778 kept as written; day of date uncertain.
