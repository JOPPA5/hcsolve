# hcp-1146 solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. The portal shows Not solved and attaches no solution or transcription. The transcription is my own, from `work/hires/`. The HistoCrypt article the portal links was not checked, so I cannot say whether it discusses this card.

## Card

Picture postcard (a couple in a garden; nothing written on the picture side), sent to Margitka Sziber, Szomolya. The whole message is on the address side in blue copying pencil. It is mostly digits, with some words in clear. The last line of the message, below the signature, gives place and date in open script: `Mezőkövesd. 1916. IV/14`. This agrees with the collection file name. The postmark date is not legible. The date fits the text: 14 April 1916 was a Friday, nine days before Western Easter (23 April).

## Cipher type and key

Type: MASC (register label). Same digit-plus-mark alphabet as hcp-1174, 1178, 1179. One letter is a digit with an optional mark; words are not always separated, and Hungarian digraphs have one sign.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2,` | cs | | `6.` | ny (new) |
| `0,` | ö, ő | | `2.` | é | | `7` | k |
| `1` | i, í | | `3` | d | | `7,` | s |
| `1.` | a | | `3,` | r | | `7.` | sz |
| `1:` | e | | `3.` | v | | `8` | m |
| `1'` (high dot) | á | | `4` | f | | `8,` | t |
| `1,` | b | | `4,` | g | | `8.` | ty (new) |
| `:1` (dots left) | ü | | `4.` | gy (new) | | `9` | p |
| `.1` (dot left) | u, ú, ű (new) | | `5` | h | | `9,` | z |
| | | | `5,` | l | | `6` / `6,` | j (new) / n |

Key work: I started from the hcp-1174 table. It read the opening at once (`Édes Margitkám! Értesítlek ...`). The new signs each came from one or more words: `.1` from húsvétkor, mulattatlak, hű; `6` from majd (twice), járok; `6.` from lányka; `4.` from hogy, megyek, egyebet, elhagyott, vagy, vagyok; `8.` from kártya; `4` from fel. The dot on 4, 6 and 8 gives the palatal partner (gy, ny, ty), which is a system and was not assumed. The word kártya was decoded by the script after I had typed it wrongly as `kárta`: the sign forced the y. In `hogy` the mark on the 4 is a short low dash, taken as the dot.

The 311 cipher signs use 30 table signs. 306 decode cleanly by the table, 3 are by sense and 2 are read through a stroke overlap (see Uncertainties 1 to 4). All 311 are accounted for.

## Plaintext (Hungarian; [ ] = enciphered on the card)

Spelling is as the signs give it; the card does not mark ó, ő, í, ú, ű, so these accents are mine. The parentheses are marks on the card, written as two curved strokes.

[Édes Margitkám]!

[Értesítlek hogy vasárnap nem megyek fel majd csak húsvétkor már hála istennek nem messze van] ([most egyebet nem írok majd szóval többet]) [adig is versecskékkel mulattatlak]

[Itt e városban járok],
De [nincs itt a lelkem],
Ott maradt az [nálad],
Én [szerelmem szentem].

Ezer ember jár az utcán,
Vagy több is tán e városban,
S én [elhagyott vagyok mégis],
Mert hisz nem [vagy velem mostan].

Sz[eretlek szívemből],
Érted [élek lányk]a,
Elmondottam [százszor] is,
S [ismétli e kártya].

[üdvözöl sokszor ölel és csókol hű kedvesed] ([Árpád])

Mezőkövesd. 1916. IV/14

Address (open): Őnagysága / Szépreményü / Sziber Margitka / kis-asszonynak / Szomolya / u. p. Bogács. / (Borsod m.)

`adig` is a one-d spelling of addig. `Sz` and the final `a` of lányka are open letters inside enciphered words, as written.

## English translation

Sweet Margitka! I let you know that I am not coming up on Sunday, only at Easter, which, thank God, is not far off now (I write nothing else now, more later by word of mouth). Until then I will entertain you with little verses.

Here in this town I walk, / but my soul is not here, / it stayed there with you, / my love, my saint.

A thousand people walk the street, / perhaps more in this town, / and yet I am forsaken, / for you are not with me now.

I love you from my heart, / for you I live, girl, / I have said it a hundred times, / and this card repeats it.

Greets you many times, embraces and kisses you your faithful sweetheart (Árpád)

Mezőkövesd, 14 April 1916

Note: the card says literally "now I write nothing else, later in words more", where `szóval` (by word of mouth) may also be the filler "so"; I take it as "by word".

## Slovak translation

Sladká Margitka! Oznamujem ti, že v nedeľu neprídem hore, až na Veľkú noc, ktorá, vďaka Bohu, už nie je ďaleko (teraz nepíšem nič iné, neskôr poviem ústne viac). Dovtedy ťa budem zabávať veršíkmi.

Tu v tomto meste chodím, / ale moja duša tu nie je, / zostala tam u teba, / moja láska, moja svätá.

Tisíc ľudí chodí po ulici, / azda aj viac v tomto meste, / a ja som predsa opustený, / lebo teraz nie si so mnou.

Ľúbim ťa zo srdca, / pre teba žijem, dievča, / povedal som to už stokrát, / a táto pohľadnica to opakuje.

Mnohokrát ťa pozdravuje, objíma a bozkáva tvoj verný milý (Árpád)

Mezőkövesd, 14. apríla 1916

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1146/work/decode.py

It checks the SHA-256 of all four scans, decodes each word of `work/transcription.txt`, asserts each against its reading, and prints the full text. The open words, the date line and the address are hard-coded in the script's print lines, so only the cipher part is computed.

## Uncertainties

Three signs are read by sense (`ODD` in the script). Two more are read through an overlap (`OVERLAP` in the script, point 4):

1. `hála` (row 3): no comma is seen under the second 5, so as written it is h. The sense `hála istennek` is certain. See `work/crops/z2_c.png`.
2. `mulattatlak`, sixth sign: a blurred, k-shaped sign, read as `8,`. See point 4 and `work/crops/s1.png`.
3. `mégis`, last sign: overwritten and blotted, with a mark after it; read as `7,` from the word only. See `work/crops/v1.png`.

Other points:

4. The word `mulattatlak` is squeezed in small above the rule, directly under `adig is versecskékkel`, and the two rows collide. The comma of `3,` and of `7,` in versecskékkel and of `7,` in `is` run down into this row. Taken alone, two of its signs look like `4.` and a barred 4, which give no word. I assign the upper stroke of each to the row above, leaving `1.` and `7`. These two signs are not counted as clean table readings. The commas of `3,` and `7,` in versecskékkel rest on the same reading of the overlap, though they are also what versecskékkel needs. The upper strokes line up with those descending commas, and the reviewer agreed. See `work/crops/x1.png`.
5. `Ezer`: the first letter is blotted and printed text lies under it; `-zer` is visible and `Ezer` is by sense. `Vagy`: the V is likewise over print.
6. `szóval` in the bracket: see the note under the translation. The first bracket mark stands right after `van` and curves the same way as the closing mark, so it could be a long comma; the bracket is my layout.
7. `.1` in `hű` stands for ű, while the family's `:1` is ü. It is one word of a short ending and the sense is sure, but it shows `.1` covers u and ü-type vowels here.
8. The mark after `százszor is` and the short strokes in the right margin near rows 9 to 12 are unexplained, and treated as punctuation or strays.
9. The `kártya` here uses `8.` = ty. hcp-1179 reads a dotted 8 as a variant of t in `kar[t?]im`; this card suggests that dotted 8 is ty, but I have not reworked that card.

## Why I believe it is correct

- A key built on other cards reads the opening with no change, and 306 of 311 signs decode cleanly by the table into Hungarian; the other 5 are restored by sense or through an overlap and are listed above.
- The new signs each recur in unrelated words, and the dotted set gy, ny, ty is regular.
- The verses scan and rhyme: lelkem / szentem, városban / mostan, lányka / kártya. Words were not chosen to fit, since kártya came from the sign.
- The content fits the card's own date line (Mezőkövesd, 14 April 1916, Easter near), the recipient, and the family's writer: the signature `Árpád` decodes as on hcp-1174, and `csókol`, `versecskét`, `Édes Margitkám` recur on the sister cards.

## Response to review 1

Verdict REVISE, reviewer Claude Opus 5.5. I checked each finding on the scan and accept all four.

1. `városian` / `városban` (major): fixed. On the 5x crop (`review/work/varos.png`) a separate comma stands under the 1, the same shape as the comma of the `6,` beside it, so the sign is `1,` = b. My reading missed it. `work/transcription.txt` line V1 is now `3. 1' 3, 0 7, 1, 1. 6,`. Plaintext, English and Slovak are changed, and my former Uncertainty 6 is deleted because it was wrong; the later points are renumbered 6 to 9. The word now matches `e városban` in the open text of the next stanza. The total stays 311 signs, and the distinct-sign count stays 30.
2. Place and date line (major): fixed. The crops `review/work/date.png` and `date2.png` show `Mezőkövesd. 1916.` and `IV/14` in open script, below the signature. My statement that the card has no written date was false. The line is added to the plaintext, both translations and the print lines of `decode.py`, and the Card section and the evidence are corrected. The postmark date remains illegible.
3. Address spelling (minor): fixed. The card has `Szépreményü` with two dots (`review/work/adr_full.png`), and it is now printed as written.
4. Sign count (minor): fixed. The two overlap signs at the end of `mulattatlak` are marked `1.~a` and `7~k` in the transcription and counted apart by `decode.py`. The headline is now 306 clean, 3 by sense and 2 through an overlap, which is the reviewer's split.

Reproduction after the fixes: `python3 -I ciphers/hcp-1146/work/decode.py` exits 0 with all four hashes OK and all 311 signs asserted. The printed text equals the plaintext above. The reading changed by one word and one added open line, so it is not substantially changed and the card closes without a second round.
