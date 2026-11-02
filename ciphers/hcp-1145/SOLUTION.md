# hcp-1145 solution (round 1, with the response to review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal lists it as Not solved and attaches no solution or transcription. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses this card. The transcription is mine, made from `work/hires/`.

## Card

Picture postcard (a man at a window handing roses to a girl; no writing on that side), to Sziber Margitka, Szomolya. Date in clear `Mezőkövesd, 1916, II/12.`; the postmark agrees (FEB 12). The whole message is enciphered, unlike sisters hcp-1174 and 1178. The date and the address are in clear.

## Cipher type and key

MASC (register label). The family key of hcp-1174, 1178 and 1179: each letter is one digit plus an optional mark. Word gaps on the card are not reliable. Hungarian digraphs have one sign. Long and short vowels share a sign, except a/á and e/é.

| sign | letter | | sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `1,` | b | | `3.` | v | | `6` | j |
| `0,` | ö, ő | | `2,` | cs | | `4` | f | | `6,` | n |
| `1` | i, í | | `2.` | é | | `4,` | g | | `6.` | ny |
| `1.` | a | | `3` | d | | `4.` | gy | | `7` | k |
| `1:` | e | | `3,` | r | | `5` | h | | `7,` | s |
| `1'` (high dot) | á | | `9` | p | | `5,` | l | | `7.` | sz |
| `:1` (dots at left) | ü, u | | `9,` | z | | `8` | m | | `8,` | t |

Taken over from the sister cards and confirmed here: all signs of the hcp-1174 table. New from this card: `4` = f (felmegyünk), `4.` = gy (hogy, nagyobb, gyötrelem), `6` = j (jöjjön, ajtón, majd), `6.` = ny (anyám). `1,` = b comes from hcp-1179 and is confirmed by legalább, többet, ébren, eszemben. This key does not match the provisional values in the partial notes of hcp-1175 (`4.` = l, `1` = é there).

## Plaintext (Hungarian)

Punctuation and capitals are mine, except the writer's `!`, `)` and `.`, which are in `work/transcription.txt`, and his one semicolon after `többet`, which a comment line there describes (in the token lines `;` only separates words). Spelling is his; [ ] shows letters he wrote single.

Mezőkövesd, 1916, II/12.

Édes Margitkám!

Értesítlek, hogy hacsak lehet, vasárnap felmegyünk Pistával. Szerettem volna, ha még addig ot[t] let[t] volna édes anyám, nem is gondoltam, hogy haza jöjjön. Legalább nagyot nézet[t] volna, mikor betoppantam volna az ajtón. No de ezt most hadjuk [= hagyjuk], majd szóval többet;

Titkon írok csak levelet,
Titkon szeretlek tégedet.
Nincsen nagyobb gyötrelem,
Mint a titkolt szerelem.

I → Akár alva, akár ébren,
Mindig te vagy az eszemben.

Sokszor ölelve és csókolva maradok hűséges, kedvesem, és imádód (Árpád)

Address (clear): Őnsg. / Szépreményű Sziber Margitka kisasszonynak, / Borsod m. / Szomolya, / u. p. (Bogács)

## English translation

Mezőkövesd, 12 Feb 1916. Sweet Margitka of mine! I let you know that, if at all possible, we are coming up on Sunday with Pista. I would have liked my mother to have stayed there until then; I did not even think she would come home. At least she would have been quite astonished when I walked in at the door. But let us leave this now, more by word of mouth;

Only in secret I write a letter, / in secret I love you. / There is no greater torment / than a hidden love.

I → Whether asleep or awake, / you are always on my mind.

Embracing and kissing you many times, I remain faithful, my sweetheart, and your adorer (Árpád)

## Slovak translation

Mezőkövesd, 12. 2. 1916. Moja sladká Margitka! Oznamujem ti, že ak to len pôjde, v nedeľu prídeme hore s Pištom. Bol by som rád, keby tam moja mama ešte dovtedy zostala, ani som si nemyslel, že pôjde domov. Aspoň by sa bola poriadne začudovala, keby som vkročil do dverí. Ale nechajme to teraz, viac osobne;

Len tajne píšem list, / tajne ťa ľúbim. / Niet väčšieho trápenia / než utajená láska.

I → Či v spánku, či bdiac, / stále si mi na mysli.

Mnohokrát ťa objímam a bozkávam a zostávam verný, moja milá, a tvoj ctiteľ (Árpád)

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1145/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription.txt` with the key, asserts every word against the stated reading, and prints the counts, the raw decode and the text. The formatted text is hard-coded in the script after the assertion. The date and address are clear text.

## Uncertainties

The script reports 385 signs, 381 by the table and 4 read by sense. Each of the 4 is a `x>y` token in the transcription.

1. `vagy`: the middle sign shows `7.` (crossed 7 with its dot), with an overwriting and a grey smear above it (`work/crops/f.png`). The key alone gives `vszgy`, not a word. I take it as a slip or correction for `1.`. The word is fixed by `Mindig te ... az eszemben` and by the metre.
2. `Pistával`: the sign shows plain `3` with no dot (`work/crops/a.png`), which gives `Pistádal`.
3. `szóval`: also plain `3`, giving `szódal` (`work/crops/s.png`). Here only `szóval` makes sense, so the writer seems to drop the dot of `3.` before `1.` in -val. That is why I read `Pistával` in item 2. `Pistádal` for `Pistáddal` ("with your Pista") is a real alternative in the style of `Angyukádal` on hcp-1178. This changes only whose Pista it is.
4. `Árpád`: the boxed signature shows `1' 3 9 1' 3`, plain `3` with no comma (`work/crops/h.png`), giving `Ádpád`. I read Árpád because hcp-1174 has `1' 3, 9 1' 3`. The box and its brown line may be a later or separate addition.

Other points:

- `kedvesem` is what the card has (`... 1: 8`), not the `kedvesed` of hcp-1174. So I parse `maradok hűséges, kedvesem, és imádód`: "I remain faithful, my sweetheart, and your adorer". That parse and its commas are mine. The other possibility is a slip for `kedvesed`, "your faithful sweetheart", as on hcp-1174. The letters on the card do not change either way. There is also a short dash under its first sign; I read that sign as `7` = k, since the dash does not look like the dot of `7.`.
- `hadjuk`: the `:1` here has its upper dot merged with the flag of the 1 (`work/crops/c.png`). `hadjuk` is a phonetic spelling of `hagyjuk`.
- `:1` serves for u here (`hadjuk`) as well as ü.
- `5,` in `kedvesem` and all other signs are clean. `0,` next to a long comma can look like `9` at low zoom. At 5x the `0` and comma are separate in `többet` and `gyötrelem` (`work/crops/d.png`, `g.png`).
- `ott`, `lett`, `nézett` are written with single t. This is his habit, as in the sister cards, not a restoration.
- `édes anyám` is read as "my mother". The card does not say whose visit is meant or where "there" is, and "up" fits Szomolya as on hcp-1174. The sentence about the mother is the natural reading, but it is thin on context.
- A roman `I` with an arrow stands in the left margin at the couplet (`work/crops/i.png`). Its meaning is unproven. hcp-1174, three days later, marks its couplet with `II`, so it may number a series.
- A broken row of short dashes runs between the last cipher row and the date. I read it as a ruled line, with no cipher value. The red `3526 2` is a printed publisher number.
- The address is clear text read from the card. `Őnsg.` is an abbreviated title, as on hcp-1174.
- I found no printed source for the verses.

## Why I believe it is correct

- A key fixed by other cards decodes 381 of 385 signs as written into continuous, grammatical Hungarian, with no gaps. The four exceptions are single signs in words their neighbours fix.
- Two of the four new signs recur in unrelated words: `4.` 7 times (hogy, nagyobb, gyötrelem) and `6` 6 times (jöjjön, ajtón, majd). The other two occur once each and rest on a single word: `4` = f in felmegyünk and `6.` = ny in anyám. Both words are secure in context.
- The verses rhyme: levelet / tégedet, gyötrelem / szerelem, ébren / eszemben. These were not used to build the key.
- The heading is the same 13 signs as on hcp-1174, the signature agrees with hcp-1174, and the date and postmark match.
- The sense fits the series: the same suitor promises a Sunday visit, and hcp-1174 (15 Feb 1916) apologises for not coming. 12 Feb 1916 was a Saturday and 15 Feb a Tuesday, so the Sunday in question falls between the two cards.

## Response to review 1

Verdict ACCEPT. All three findings are fixed. No letter of the plaintext changed, and `python3 -I ciphers/hcp-1145/work/decode.py` still reports all hashes OK and 385 signs, 28 distinct, 74 words, 4 read by sense.

1. Minor, false claim about recurrence: fixed. My own count over `work/transcription.txt` agrees with the reviewer: `4.` 7, `6` 6, `4` 1, `6.` 1. "Why I believe it is correct" now says that `4` and `6.` rest on one word each.
2. Minor, `kedvesem` translation: fixed. The English and Slovak translations now use the reviewer's parse, the Hungarian has commas around `kedvesem`, the printed text in `work/decode.py` has them too, and the alternative `kedvesed` is stated under Uncertainties.
3. Minor, punctuation claim: fixed. I checked the end of the letter block at 9x of the 1024 view (`work/crops/semi.png`): the dot stands above the comma of the final `8,`, as the reviewer says. `work/transcription.txt` now has a comment line, and the sentence above the plaintext is corrected.

I also added the weekday check from the reviewer's point 7. The alternative `Pistádal` for `Pistáddal` stays disclosed, as the review asked.
