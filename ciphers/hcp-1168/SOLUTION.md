# hcp-1168 solution (round 1, corrected after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal shows Not solved with nothing attached. I found no published solution in the repo or on the portal; the HistoCrypt article the portal links was not checked for this card. The transcription is my own, from `work/hires/`. The key starts from the FINAL sister cards hcp-1174, 1178 and 1179 (Claude Opus 5.5); five values are new here (`2`, `6`, `6.`, `4.`, `.1`) and one tentative value, `4`, is confirmed.

## Card

Picture postcard, portrait of a young woman, from Mezőkövesd to Sziber Margitka, Szomolya. Open note on the picture side: `Mezőkövesd, 1916, I 30,` Address side, open: `Őnsg. / Szépreményű / Sziber Margitka / urleánynak / Szomolya / (Borsod m.) u. p. Bogács`. Postmark: `JAN` is legible and the place fits Mezőkövesd; the day and year are not clearly struck. The boxed `1916, I/30` is open text too.

Unlike its sisters, almost the whole message is enciphered: 365 signs. Only three lines of a four-line verse are mainly open.

## Cipher type and key

Hungarian, monoalphabetic substitution with a figure-plus-mark alphabet (register label: MASC). A letter is a digit plus an optional mark, and the mark changes the letter. There are no word divisions on the card. Hungarian digraphs have one sign. Long and short vowels are mostly not separated, except a/á and e/é (`1:` e, `2.` é).

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| `0` | o, ó | `2` | **c** (new) | `5` | h |
| `0,` | ö, ő | `2,` | cs | `5,` `5.` | l |
| `1` | i, í | `2.` | é | `6` | **j** (new) |
| `1,` | b | `3` | d | `6,` | n |
| `1.` | a | `3,` | r | `6.` | **ny** (new) |
| `1:` | e | `3.` | v | `7` | k |
| `1'` (high dot) | á | `4` | f | `7,` | s |
| `.1` (dot on the left) | **u** (new) | `4,` | g | `7.` | sz |
| `:1` (dots on the left) | ü | `4.` | **gy** (new) | `8` | m |
| `9` | p (and see point 1 below) | `9,` | z | `8,` | t |

`4` = f was only tentative on hcp-1175 and is confirmed here (`fizetik`, `fizettem`). `5.` for l is known from hcp-1178. Key work: the family table gave most of the text at once (`Édes Margitkám`, `bocsás meg`, `ritkán írok`). The new values came from words the table left with one gap: `anyagi viszonyok`, `nyolc`, `jobban`, `hogy`, `egy`, `kilenc`, `krajcár`, `Anyukád`, `hozzájutni`. Each new sign recurs: `6.` five times in `inyen, anyagi, viszonyok, Anyukád, nyolc`; `6` in `jobban, krájcár, krajcár, hozzájutni, megcsókoljam, ajkadat`; `4.` in `hogy` (twice) and `egy` (twice); `2` in `kilenc, nyolc, cipőre, krájcár, krajcár`; `.1` in `hozzájutni, Anyukád`.

## Plaintext (Hungarian; [ ] = enciphered on the card; spelling as written, normal form after =)

Mezőkövesd, 1916, I 30,

[Édes Margitkám!]

[Bocsás (= Bocsáss) meg, hogy inyen (= ilyen) ritkán írok, de most az anyagi viszonyok nem fizetik ki jobban, nem tehetünk rólla (= róla), hogy ahoz (= ahhoz) a pár krájcárhoz olan (= olyan; see `inyen`, `olan` under Uncertainties) nehezen lehet hozzájutni, amit keves (see `keves` under Uncertainties) Anyukád ide adot (= adott), kilenc koronát már nincs belőle mert nyolc korona kellet (= kellett) a cipőre az mán (= már) az egy koronából az adóságomat (= adósságomat) fizettem még most is tartozok egy pár krajcárral]

) ([Árpád]) 1916, I/30

Saját kis versembe zárni
Szeretném én [magamat]
Hogy mikor ajkad elszavalja,
[Megcsókoljam - ajkadat]

[Sokszor üdvözölve és csókolva - maradok szerető kedvesed a sírig]

## English translation

Sweet Margitka! Forgive me for writing so rarely, but just now money matters do not pay any better; we cannot help it that those few kreuzers are so hard to come by. Of what your [dear? or: the little that your; see `keves` under Uncertainties] mother gave here, nine crowns, there is nothing left, because eight crowns were needed for the shoes, and with the one crown left I paid my debt, and even now I still owe a few kreuzers. (Árpád) 1916, I/30

I would like to shut myself up in my own little verse, so that when your lips recite it I may kiss your lips.

Greeting and kissing you many times, I remain your loving sweetheart until the grave.

## Slovak translation

Sladká Margitka! Odpusť, že píšem tak zriedka, ale teraz finančné pomery nevyplácajú lepšie; nemôžeme za to, že k tým pár grajciarom sa tak ťažko dá dostať. Z toho, čo tvoja [drahá? alebo: to málo, čo tvoja; pozri `keves` v Uncertainties] mama sem dala, deväť korún, už nič nezostalo, lebo osem korún bolo treba na topánky a tou jednou korunou som zaplatil svoj dlh, a ešte aj teraz dlhujem pár grajciarov. (Árpád) 1916, I/30

Rád by som sa uzavrel do vlastného veršíka, aby som, keď ho tvoje pery zarecitujú, pobozkal tvoje pery.

Mnohokrát ťa pozdravujem a bozkávam a zostávam tvoj milujúci milý až do hrobu.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1168/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign of `work/transcription.txt`, stops if the letters differ from the stated reading (whole text, across line breaks), and prints the text. The open text and punctuation are hard-coded in the script. It reports 365 signs: 358 by the table as written, 7 by word sense.

## Uncertainties

Signs resting on word sense (tagged `~` in the transcription):

1. `üdvözölve` (three signs). The ö signs are transcribed `9~ö` because they first looked like plain `9` (p). Enlarged (review/work/cmp_oe.png) they are not plain: the tail of the true `9` in `pár` flows straight out of the ring, while these two have a separate squared head at the start of the tail, notched against the ring. That is most likely `0,` with its comma touching, so the table value ö is probably what is written, and the conflict with p is weak. The tags stay as a caution. The first sign has a lower left dot and a thick blob at the end of the serif, which may be the upper dot of `:1`; a plain `.1` = u cannot be fully excluded, but the word needs ü.
2. `sírig`: the first sign is a plain `7` (k) with no comma visible; the collector's stamp crosses this place but the paper below the sign looks clean. The table gives `kirig`, not a word. `s` is by sense; `kedvesed a sírig` is a stock ending.
3. `csókolva`: the first sign is a filled ink blot with a clear comma. Its tail fits 2, so `2,` is partly by sense.
4. `koronából`: the sign before `ól` has a comma and a cramped body. Enlarged, it is a serifed 1 and the hairline is not a crossbar, so `1,` (b) is the likely reading; `7,` (s) would give `koronásól`, no word here. Tagged out of caution.
5. `adóságomat`: the sign after `7,` is a 1 with one dot, sitting lower than the usual `1'` (about 35% down the sign, not about 23%), and the line-end hyphen lies at its foot, where the lower dot of `1:` would be. `1:` cannot be fully excluded on the pixels; `á` is confirmed by the word. Tagged `1'~`.

Readings that are not sign doubts:

- `keves`: signs are clearly `7 1: 3. 1: 7,`. Both readings need a slip. `kedves` ("your dear mother") drops a d (compare `kedvesed` in the last line, which has it). `kevés` ("little", `amit kevés`, the little that) needs `1:` for é, whereas this writer writes é with `2.` in `Édes`, `és` and `még`. The sense favours `kedves`, but it is not settled, and it changes one word of the translation only. The translation marks it. I print the signs as written.
- `inyen`: `6.` is ny, as clear as in the other four words, but the sense is `ilyen`. It is either a slip or dialect, and I print it as written.
- `olan`: this may be no oddity at all. The dotted row of the alphabet gives digraphs (`4,` g / `4.` gy, `6,` n / `6.` ny, `7,` s / `7.` sz), so by that pattern `5.` could be ly and `0 5. 1. 6,` simply `olyan`. But `5.` = l comes from hcp-1178 and 1179 (`a legszeb`, `csókollak`), so the writer also uses it for plain l, and this is its only occurrence here. Unproved either way; I keep `5.` = l and print `olan`.
- `az mán`: `mán` is the colloquial form of `már`. The sentence has little punctuation (none is enciphered), so my clause division in the money passage is an interpretation. The sums fit it: 9 crowns = 8 for shoes + 1 for the debt.
- `krájcár` and `krajcár` both occur, the first with `1'`.
- `adóságomat`: for the spelling, the single s against normal `adósságomat`; the sign itself is point 5 above.
- `elszavalja` is open text. The l and j share one long stroke, and the stroke over the line is a comma from the cipher line above, not an accent. Sense and the rhyme scheme (`magamat` / `ajkadat`) support it.
- A closing bracket `)` stands after `krajcárral` with no opening one. It is plain punctuation; I cannot explain it. A dot stands above the `5,` of `csókolva`, also unexplained. A fine line runs through part of the last row and has no effect on the reading.
- The poem may be quoted or may be the writer's own; it does say `saját` ("my own"). I found no printed source, and did not search for one outside the repo.

## Why I believe it is correct

- One table decodes all 365 signs into continuous Hungarian with only 7 signs by sense, and those stand in words the other signs fix.
- The text is specific and self-checking: 9 crowns from the mother, 8 for shoes, 1 for a debt.
- The open verse confirms the cipher: `Szeretném én [magamat]` and `[Megcsókoljam - ajkadat]` complete a rhyme with `magamat` / `ajkadat`, and `ajkadat` repeats the open `ajkad`.
- Sister cards agree: same recipient, town and date range, and the same signature `Árpád` as hcp-1174 (found here from the digits). The fuller alphabet here extends their key with no conflict; `csókol-` and `szerető kedvesed` recur as on hcp-1174.

## Response to review 1

Verdict ACCEPT, six minor findings. No letter of the reading changed. The reproduction command was re-run after the fixes and passes, now reporting 358 signs by table and 7 by sense.

1. Broken cross-reference: fixed. The plaintext and both translations now name `keves` under Uncertainties instead of "point 3".
2. e/é statement: agreed and fixed. The cipher section now says a/á and e/é are both separated. The `keves` note is rewritten: both `kedves` and `kevés` need a slip, and sense favours `kedves`. Still open. The translations give both options.
3. `olan`: agreed. It has its own note beside `inyen`, with the `5.` = ly alternative. I do not change the value, because `5.` = l is attested on hcp-1178 and 1179 and there is only one `5.` here.
4. `üdvözölve`: agreed after looking at review/work/cmp_oe.png. The notched tail is visibly unlike the `9` of `pár`. Point 1 is rewritten, the "9-for-ö habit" is removed from the evidence section, and the claim about hcp-1174 no longer serves as support. Tags stay.
5. Count of new values: fixed. Five are new, `4` is confirmed, and the opening sentence now agrees with the table and NOTES.md.
6. `adóságomat`: agreed after looking at review/work/z_adosa.png. The dot is low and the hyphen stands where a lower dot would be. The sign is now tagged `1'~` in work/transcription.txt and listed as point 5, which makes 7 sense-read signs.

The reviewer's trivial note on the picture side is also fixed: on review/work/pic_note.png the open date reads `Mezőkövesd, 1916, I 30,` with commas, so SOLUTION.md and work/decode.py now print that.

Not verifiable and left open, as the review says: the HistoCrypt article linked from the portal, the postmark year (the written dates give 1916), and a printed source of the verse.
