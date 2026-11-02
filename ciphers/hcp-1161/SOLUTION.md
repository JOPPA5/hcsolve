# hcp-1161 solution (round 1, corrected after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal shows Not solved and attaches no solution or transcription. The transcription is my own, read from `work/hires/`. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. The key is transferred from sister cards, not built here, except as noted.

## Cipher type and key

Hungarian open text with the tender and private passages replaced by a digit cipher (register label: MASC). The card's digits are the Mezőkövesd family key (hcp-1174, 1178, 1179, 1170). Each letter is one sign: a digit, or a digit with a mark. A comma or dot is part of the sign. Spaces on the card divide words.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2,` | cs | | `5,` | l |
| `0,` | ö | | `2.` | é | | `6,` | n |
| `1` | i, í | | `3` | d | | `6.` | ny |
| `1.` | a | | `3,` | r | | `7` | k |
| `1:` | e | | `3.` | v | | `7,` | s |
| `1'` (single high dot) | á | | `4,` | g | | `7.` | sz |
| `.1` (dot left) | u | | `4.` | gy | | `8` | m |
| `-1` (dash or dot left) | ú | | `5` | h | | `8,` | t |
| `1,` | b | | `9,` | z | | | |

The card has 217 cipher signs in 50 words: 213 decode by this table as written, 4 are read by sense (see Uncertainties).

Where the signs come from: nearly all are on hcp-1174. `1,` = b comes from hcp-1179 (legszeb), `4.` = gy, `6.` = ny and `-1` = ú from hcp-1170, where each had thin support. This card confirms them: `4.` in hogy, `6.` in anyám, `-1` in úgy. `.1` = u is confirmed here with three clean occurrences (tudom, kábulva, elutasítanál); it was already listed on hcp-1135 and hcp-1160, citing hcp-1172. `9,` = z now has a word of its own support (Róza).

## Plaintext (Hungarian; [ ] = enciphered on the card)

[Kedves Márgitkám]!

Lapodat megkaptam melynek nagyon örvendek nem tudom micsoda borzasztóságot írsz, hogy volt aba a levélbe [én aszt sem tudom hogy mit írtam akkor úgy el voltam kábulva no] de az se-mi én azt bár mikor meg[tenném érted ha hidegen elutasítanál] mer én azt nem tudnám [elviselni hisz így sincs senki hát úgy meg ki volna ha te se volnál már most is édes anyám is meg Róza is írtak másnak] és én még már két lapot írtam nekik és ma se kapok választ.

[számtalanszor ölellek és csókollak] ([Árpád])

Open pencil date at the foot: 1915. XII/18 Mezőkövesd.

Address: Tek. / Szépreményű / Sziber Margitka / kisasszonynak / (Borsod m.) Szomolya / u. p. Bogács. Postmark: only a day-like 5 and scattered letters are legible, so it adds nothing. The picture side has only a printed photograph, publisher's mark and the number 3398/4; no writing.

Spellings as written: `Márgitkám` (normal Margitkám; 1' is clear in the heading), `aszt` (azt), `se-mi` across a line break (semmi), `mer` (mert), `bár mikor` (bármikor), `tud nám` written as two parts (tudnám), `aba` (abba, colloquial for abban, "in that"). The open `meg` joins the cipher `tenném`. `Róza` has no accent sign, as this key does not separate o and ó.

## English translation

[Dear Margitka]! I received your card, which I am very glad of. I do not know what dreadful thing you are writing about, that was in that letter; [I do not even know what I wrote, I was so dazed then, well,] but that is nothing, I would do it [for you] any time [if you coldly rejected me], because I could not [bear it. After all, even so there is no one, so who would there be if you were no longer there. Now too my dear mother and Róza have written to others,] and I have even written them two cards already, and even today I get no reply.

[Countless times I embrace you and kiss you] ([Árpád])

1915, 18 December, Mezőkövesd.

## Slovak translation

[Drahá Margitka]! Dostal som tvoj lístok, ktorému sa veľmi teším. Neviem, akú hroznú vec píšeš, že bola v tom liste; [ja ani neviem, čo som napísal, tak som bol vtedy omámený, no] ale to nič, ja by som to [pre teba] kedykoľvek [urobil, keby si ma chladne odmietla], lebo ja by som to nedokázal [zniesť. Veď aj tak nikoho nemám, kto by teda bol, keby si už nebola ani ty. Aj teraz moja drahá matka aj Róza písali iným,] a ja som im dokonca už napísal dva lístky a ani dnes nedostávam odpoveď.

[Nespočetnekrát ťa objímam a bozkávam] ([Árpád])

1915, 18. december, Mezőkövesd.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1161/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign, asserts that each decoded word equals the stated reading, and prints the full text with the address and the 213/4 count. The open text is hard-coded in the script, so the command reproduces only the decoding of the cipher signs.

## Uncertainties

Four cipher signs are not clean; they are in `ODD` in `work/decode.py`:

1. `így`: the mark after the 4 is a short tick, nearer a comma than a dot, so the table alone gives g (`ig`). `hisz így sincs senki` fixes gy. The short tick on `2.` in `érted` is close in form and counted as clean, so this is a cautious listing.
2. `úgy` (second one, before `meg ki volna`): an ink blot with a tail running lower left covers the mark of the 4. The mark itself is unreadable: it may be a dot or a comma. `gy` rests purely on word sense, since `úg` is not a word.
3. `voltam` (first one): an ink blot of the same kind covers the mark of the 3. Again the mark is unreadable and `v` rests purely on word sense, since `roltam` gives nothing; `3.` occurs clean in `volna`.
4. `Árpád`: the 9 has a clear comma, so the table alone gives `Árzád`. Plain `9` = p on hcp-1174 and 1173, signed the same. I take it as the writer's slip, and the name as certain. It is a signature read from sisters on this one sign.

`kábulva`, listed here in round 1, is no longer an uncertainty: the second sign is a clean `1'` = á, because the low dot is the i-dot of the open `mi` in the next row (`review/work/kab.png`). The third sign has no cross bar and the shape of this writer's 1 with a lead-in stroke, so it is `1,` = b; read as `7,` the letters would give `kesulva`, no word.

Smaller points:

- The left mark of the 1 in both `úgy`, read as `-1`: in the first it looks like a dot and a dash together, in the second a dash and a dot at the lead-in. `így` would also make sense in the second, but the mark is there, so I read ú.
- `Márgitkám`: the single high dot is clear. It may be a slip for `1.`; it changes nothing.
- `Róza` is read as a name from `meg Róza is`, joined on the card only by close spacing. Who she is, is not known. `3, 0 9, 1.` is otherwise clean.
- `meg ... írtak másnak`: the sense "wrote to others (not to me)" is my understanding of the context; the words themselves are clean.
- `azt` in `én azt bár mikor megtenném` has no stated object on this card. What he would do remains unexplained; the suicidal line on hcp-1175 (`lövöm magam`, unconfirmed there) may be related, but this is only a suspicion and is not part of the reading.
- `no` is the Hungarian interjection, as enciphered; it is two signs, `6, 0`, closing the cipher group before open `de`.
- Open text is pencil, not struck through, and reads well. `borzasztóságot` is broken over two lines, and `mikor` ends in a long tail.
- The date in pencil at the foot agrees with the portal file name (1915-12-18), though the card's own date is in a smaller hand at the edge, and a line was drawn around it. It may be the writer's or a later note.
- Published Hungarian text: none is involved here; this is a private letter.

## Why I believe it is correct

- A key established on other cards decodes 213 of 217 signs as written, into 50 Hungarian words in a continuous, grammatical passage with no gaps. The sentence runs across the changes between open and cipher, for example open `meg` + cipher `tenném`, open `nem tudnám` + cipher `elviselni`. A forced key could not join open text like that.
- Long clean words with no freedom: `elutasítanál`, `számtalanszor`, `elviselni`, `hidegen`, `csókollak`.
- The content fits the correspondence: Árpád to Margitka Sziber, private matters hidden, mother and the tender close enciphered. Closing words match hcp-1174 (`számtalanszor`, `csókollak`, `Árpád`).
- Everything else on the card, the open text included, is read: there is no unread word. (Round 1 made this claim while omitting the open word `aba`; I have since read every open row against enlargements, and the rest stands as transcribed.)

## Response to review 1

Verdict REVISE. All five findings are accepted. The cipher reading and the 217 signs do not change. The decoded letters are identical; one open word was added and notes and translations were corrected.

1. **major, `aba` omitted: fixed.** I checked `review/work/o6b.png` and `o5.png`: the sixth line ends `hogy volt aba` right at the margin rule, and the next line starts `a levélbe`. It is three letters, a-b-a, the colloquial `abba(n)`. Added to the plaintext, to the hard-coded line in `work/decode.py`, to both translations ("in that letter", "v tom liste") and to "Spellings as written". Because the claim that nothing was unread proved false, I re-read all open rows myself on the reviewer's enlargements (`o2`, `o3`, `o4`, `o5`, `o7`, `o10`, `o12`, `o14`, `o15`, `o21`, `o22`, `o23`) and on the whole card. I found no other omission.
2. **minor, low dot in kábulva: fixed.** `review/work/kab.png` shows the dot directly over the i of the open `mi` below, which has no other dot. The sign is a clean `1'`. The token is now plain in `work/decode.py`, the `1'~low` entry is removed from `ODD`, and the count is 213 by table, 4 by sense.
3. **minor, blot wording: fixed.** `review/work/r08b.png` and `r16c.png` show a tail running lower left on both blots. Uncertainties 2 and 3 and the comments in `ODD` now say that the mark is unreadable and that the letters rest purely on word sense.
4. **minor, `még` in translation: fixed.** English now has "have even written them two cards already", Slovak "dokonca už napísal".
5. **minor, `.1` not new: fixed.** Now stated as confirmed here, with hcp-1135, hcp-1160 and hcp-1172 credited. The likeness of the `így` tick to the `2.` tick in `érted` is noted; `így` stays in the sense list.

Re-run: `python3 -I ciphers/hcp-1161/work/decode.py` passes the hash checks and every word assertion, and prints 217 signs, 213 by table, 4 by sense, with `aba` in place.
