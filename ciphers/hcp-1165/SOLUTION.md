# hcp-1165 solution (round 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal shows Not solved and attaches no solution or transcription. The HistoCrypt article the portal links was not checked for this card. Key family taken from FINAL cards hcp-1174, 1178, 1179; the transcription is my own, from `work/hires/`.

## Cipher type and key

Hungarian letter and verses to Margitka Sziber, Szomolya, from the Mezőkövesd writer. The heading and the whole letter part are enciphered; the verses and closing are in clear with key words enciphered. Register label: MASC. One sign is a digit, or a digit with a mark; the mark is part of the sign. Word spaces are mostly kept. Parentheses are punctuation.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2.` | é | | `6.` | ny |
| `0,` | ö, ő | | `3` | d | | `7` | k |
| `1` | i, í | | `3,` | r | | `7,` | s |
| `1,` | b | | `3.` | v | | `7.` | sz |
| `1.` | a | | `4` | f | | `8` | m |
| `1:` | e | | `4,` | g | | `8,` | t |
| `1'` (high dot) | á | | `4.` | gy | | `9` | p |
| `.1` (one dot left) | u, ú | | `5` | h | | `9,` | z |
| `:1` (two dots left) | ü, ű | | `5,` | l | | | |
| `2,` | cs | | `6` | j | | | |
| | | | `6,` | n | | | |

Most values are on the table of hcp-1174 (`4` = f is only tentative on hcp-1175 and is confirmed here by `fiú`). `4.` = gy, `6` = j, `6.` = ny and `.1` = u are not on that table, but they are not new to the family: they recur on sister cards such as hcp-1137, 1144 and 1153. This card confirms them on its own: `5 0 4.` hogy, `6 1. 4. 0 6,` nagyon; `6 0` jó, `6 0, 6, 6, 1` jönni, `6 0, 8, 8, 1: 8` jöttem; `6. 1 8, 3. 1.` nyitva; `.1 8, 0 5, 2. 3, 8,` utolért. One dot (u, ú) and two dots (ü, ű) are distinct signs here, and the letters follow them exactly.

## Plaintext (Hungarian; [ ] = enciphered on the card)

[Édes Margitkám]!

[értesítlek hogy szerencsésen hazaértem nagyon jó idő volt szinte passzió volt jönni hét órára értem a városba mert lassan jöttem a szalóki fiú is utolért a szőllők közt mire az üzletház értünk már nyitva volt de nem szólt semit az öreg Lubi]

Más különös ujság nincs.

Kicsiny kezed körül csapongva
Egy tarka pille röppen,
Mintegy [bűbájtól vonzva] vonva
Mind szűkebb körökben
Míg végül össze vonva szárnyait
Pihenni száll a kézre
Fehér [kezedet], a parányit
Ő liliomnak nézte.

Ha a szőlő nedvtül árad,
A fecske is ott terem,
Mikor a szem könnybe lábad
Héba [szívben szerelem].

Üdvözölve és [sokszor csókolva] maradok [hű imádód] és [igaz] sz[ív]ű [kedvesed] ([Árpád])
csókolom angyikát és Mariskát is

Address: Őnsg. / Szépreményű Sziber Margitka kisasszonynak / Szomolya / u. p. (Borsod megye) / u. p. Bogács. The postmark shows Mezőkövesd (ZŐK legible); its date is not legible. The portal file name gives 1915.

Normal spellings: semit = semmit, üzletház = üzletházhoz (the card has no ending), szőllők = szőlők, nedvtül = nedvtől, Héba = hiába (see below).

## English translation

Sweet Margitka! I let you know that I got home safely. The weather was very good, it was almost a pleasure to travel. I reached the town by seven o'clock, because I went slowly; the Szalóki boy (or: the boy from Szalók) also caught up with me among the vineyards. By the time we reached the shop building it was already open, but old Lubi said nothing. There is no other special news.

Around your tiny hand, fluttering, / a bright butterfly takes wing, / as though drawn, pulled by a spell, / in ever narrower circles, / until, folding its wings together, / it settles on the hand to rest: / your white hand, the tiny thing, / it took for a lily.

When the grape swells with juice, / the swallow too appears there; / when the eye fills with tears, / in vain the love in the heart.

Greeting you and kissing you many times, I remain your faithful adorer and true-hearted sweetheart (Árpád). I kiss ángyika (sister-in-law or aunt by marriage) and Mariska too.

## Slovak translation

Moja sladká Margitka! Oznamujem ti, že som šťastne došiel domov. Bolo veľmi pekné počasie, cesta bola takmer potešením. O siedmej som bol v meste, lebo som išiel pomaly; medzi viničami ma dostihol aj chlapec Szalókiovcov (alebo: chlapec zo Szalóku). Kým sme došli k obchodnému domu, už bolo otvorené, ale starý Lubi nič nepovedal. Iná zvláštna novinka nie je.

Okolo tvojej drobnej ruky poletujúc / vzlietne pestrý motýľ, / akoby čarom priťahovaný, ťahaný, / v čoraz užších kruhoch, / až napokon, zložiac krídla, / sadne si na ruku odpočinúť: / tvoju bielu ruku, tú drobnú, / pokladal za ľaliu.

Keď sa hrozno naleje šťavou, / aj lastovička je hneď tam; / keď sa oko zaleje slzami, / márna je láska v srdci.

Pozdravujúc ťa a mnohokrát bozkávajúc ostávam tvoj verný ctiteľ a tvoj milý verného srdca (Árpád). Bozkávam aj ángyiku a Marišku.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1165/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign word by word, asserts each decoded word against the stated reading, prints the sign counts and the full text with the address. The clear text is hard-coded in the script, so only the cipher part is computed. Result: 276 signs, 268 by the table, 8 read by sense. The check folds only the accents the writer leaves unmarked (o/ó, ö/ő, i/í, u/ú, ü/ű); it keeps u and ü apart.

## Uncertainties

Cipher signs, the 8 in `ODD` in `work/decode.py` (the table alone gives other letters or the mark is missing):

1. Article `a`, three times (`a városba`, `a szalóki`, `a szőllők`): a plain `1` with no dot; the table gives i. Pixels are clear at 3x; the writer seems to use it for the article, and `1.` in other words. Word sense.
2. `lassan`: plain `5`, no comma seen (the flag of the 5 runs into the next 1). The table gives h. Word sense.
3. `üzlet`: `9` clearly has no comma (table p), and the `8` has a hook under it where the comma would be. Two signs, read by sense.
4. `bűbájtól`: the first sign is `1`; a stroke to its lower right, beside the double dots of `szűkebb` in the line below, is taken as its comma, though it sits further right than usual. Without it the word is `iűbájtól`. Word sense; no other Hungarian word fits `?űbájtól`.
5. `igaz`: the second sign looks like a written letter g with a closed loop, not `4,`. Possibly a clear g, or a lapse. Word sense.

Other points:

- `Lubi` is a name or nickname reported literally (`5, .1 1, 1`). The sign has one dot; the stroke beside it is the separate flag of the 5. The writer leaves accents unmarked, so Lúbi is also possible. I do not know who this is.
- Two signs count as table readings but touch other ink: in `szólt` the comma of `8,` merges into a stroke of the clear line below (the u there has no such stem), and in `kedvesed` the comma of `7,` crosses the ruled line. Each stroke sits where the comma falls, and neither changes the reading.
- `szalóki`: place adjective or surname; not identified. The translation gives both.
- `üzletház` has no ending in the signs. The last two signs `1. 9,` are partly under the postmark ring and an ink blot, still legible. I did not supply `-hoz`.
- `szív` + `ű` in `sz[ív]ű`: `sz` and `ű` are clear letters; only `1 3.` is cipher. The second letter of the `ü` is written over a green mark `142` under the ink, not part of the message.
- `Más` in clear: the first word of the line is blotted, and the accent is lost in the blot. The pixels look like `Mois`, which is this writer's `Más`: his a looks like `oi` throughout (vonva, árad, szárnyait). The same habit explains the a of `ujság`.
- `Héba`: clear, taken as dialect or a slip for `hiába`. Sense only.
- `lábad` is squeezed in small at the right, read also by the rhyme with `árad`. `árad` has one tall stem only, the d of `kezed` and `lábad`; there is no t.
- `angyikát` has no accent visible. The translations supply the normal form ángyika, a relative by marriage; a personal name Angyika is not excluded.
- `[kezedet],`: the comma is the comma of the sign `8,`; no separate punctuation comma is visible.
- A faint pencil `)` in line 4 of the cipher, before `mire`, has no partner. It seems to be a stray.
- The dashes at the ends of cipher lines fill the space, except that the mark after `3 1:` could be a hyphen; the sign after `6, 1. 4. 0` has a comma under it, so it is `6,`.
- The verses were not found in print; I made no search beyond the sister cards.

## Why I believe it is correct

- A key built on other cards decodes 268 of 276 signs as written into connected Hungarian prose, a long and ordinary travel report, with names and context that fit (Margitka as addressee, ángyika and Mariska as on hcp-1178, signature Árpád as on hcp-1174).
- The signs missing from the hcp-1174 table are attested on sister cards, and each appears here in clean words.
- `szerelem` rhymes with `terem`, and `bűbájtól vonzva` gives the verse its sense; `kezedet` agrees with the clear `Fehér ... a parányit`.
- The sign pair `1:` / `1'` holds: where `szerelem` first looked like `1'`, enlargement (`work/crops/C3.png`) showed the second dot of the colon.

## Response to review 1

Verdict REVISE. All five findings were checked on the reviewer's crops and on my own new crops from the high-resolution scan, and all are accepted. No word of the reading changes except the name and `árad`; the letter, the verses and the sign count (276) stand.

1. `.1` against `:1` (major): fixed. One clear dot in fiú, utolért and the name; two clear dots in értünk, üzlet, bűbájtól and hű. I re-cropped hű, because the reviewer's crop stops just above the dots, and it has two. `.1` = u, ú is now in the table and in KEY; the three tokens are changed; the name is Lubi in all three languages; the uncertainty note is rewritten. `decode.py` no longer folds u into ü, so a mix-up of the two signs now stops the script.
2. `áradt` to `árad` (minor): fixed in the plaintext, `decode.py` and the note. One stem only, and the word rhymes exactly with `lábad`. The translations do not change.
3. `Önsg.` to `Őnsg.` (minor): fixed in `SOLUTION.md` and `decode.py`. Two long strokes stand above the O.
4. Commas in `szólt` and `kedvesed` (minor): accepted. Both strokes sit where the comma falls. Both are now `8,` and `7,` by table, still flagged as touching other ink. The count of signs read by sense drops from 10 to 8.
5. Wording (minor): fixed. "Mezőkövesd to Szomolya walkers" is removed, the Slovak now has `chlapec Szalókiovcov`, the ángyika form is noted as supplied, and the comma of `[kezedet],` is explained.

Also taken from the review: `Más` loses its question mark, because the writer's a looks like `oi` throughout; my crop shows `Mois` under the blot. `4.`, `6`, `6.` are no longer called new. The reviewer's upheld points (article `a`, `lassan`, `üzletház`, `bűbájtól`, `igaz`, `Héba`) stay disclosed as before. The postmark date stays unread; the year rests on the portal file name.

After the fixes: `python3 -I ciphers/hcp-1165/work/decode.py` gives hashes OK, 276 signs, 268 by table, 8 by sense, and the text above. The reviewer's independent `review/work/verify.py`, run read-only, shows only the differences of the sense readings listed under Uncertainties.
