# hcp-1138 solution (after review 2)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal lists it as Not solved with no transcription or solution attached. I did not check the HistoCrypt article linked by the portal for this card, and no published solution was seen. The key family comes from FINAL cards hcp-1174, 1178, 1179 and, for `8.`, 1142, 1146, 1164, all my model's work; the new signs below are from this card. Round 1 was wrong in several places; the independent review found them, and `## Response to review 1` says what it changed.

## Card

Picture postcard (printed roses, C. Klein signature, no writing on the picture side), Mezőkövesd, 17 March 1916, to Sziber Margitka, Szomolya, u. p. Bogács, Borsod megye. 5-fillér stamp; the postmark is partly under the stamp and agrees with the written date as far as it can be read (the reviewer reads `MEZŐ...` and a 17; I see only part of that, so this is a weak check). Signed in cipher Árpád, as on hcp-1174. Almost the whole message is enciphered, 409 signs in 84 words. Open text: `Kívánom:`, `Mezőkövesd, 1916. III/17` and the address.

## Cipher and key

Register type: MASC. Hungarian, monoalphabetic, one sign per letter or digraph. A sign is a digit plus a mark; no word divisions in the digits are reliable. A comma is a long stroke running down-left from under the digit, often into the next row.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| `0` | o, ó | `2.` | é | `6` | j (new) |
| `0,` | ö, ő | `2` | c (new, once) | `6,` | n |
| `1` | i, í | `3` | d | `6.` | ny (new) |
| `1.` | a | `3,` | r | `7` | k |
| `1:` | e | `3.` | v | `7,` | s |
| `1'` (high dot) | á | `4` | f | `7.` | sz |
| `.1` (dot to the left) | u, ú (new) | `4,` | g | `8` | m |
| `:1` (dots to the left) | ü | `4.` | gy (new) | `8,` | t |
| `1,` | b | `5` | h | `8.` | ty (once here) |
| `2,` | cs | `5,` | l | `9` | p; z without a comma, see below |
| | | | | `9,` | z |

The dotted forms are digraphs of the comma letter: `4,` g and `4.` gy, `6,` n and `6.` ny, `7,` s and `7.` sz, `8,` t and `8.` ty.

Key recovery: `Édes Margitkám!` opens the card with the same 13 signs as hcp-1174, and the family table then gives most words. The new signs came from words and each recurs: `6` in szedjétek, hagyjatok, jó, jól, teljen, május, tolmácsolja; `6.` in nyugott, hernyót; `4.` in hogy, úgy, vagyok, ángyika, hagyjatok; `.1` in úgy, rosszul, nyugott, május, kapuba. `8.` occurs once here, in `kártyámon`; on this card it rests on that one word and the pattern above, and FINAL sister cards hcp-1142 (`kártyán`), 1146 (`kártya`) and 1164 (`kártyát`) read the same value.

## Plaintext (Hungarian, spelling as on the card; [ ] = enciphered)

[Édes Margitkám!]

[Értesítlek hogy májusba fognak sorozni de csak azokat akik még nem voltak sor alatt tehát most már nyugott lehec édes de most már ne szedjétek le a hernyót hagyjatok úgy mindent) aztán úgy volna jó ke(d)vesem ha már mostanába lejönne ángyika házat nézni hogy akkorra lenne) de most többet nem írok mert rosszul vagyok úgy veszem észre ott a kapuba alaposan megfáztam)]

[Kártyámon e kis virág tolmácsolja érzelmem]

Kívánom: [minden órád a távolban jól teljen!]

[Most üdvözöl és számtalanszor csókol szerető kedvesed (Árpád)]

Mezőkövesd, 1916. III/17.

Address: Őnagysága. / Rózsareményű / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács / Borsod m.

Normal spelling of the odd forms: nyugott = nyugodt, lehec = lehetsz, ke(d)vesem = kedvesem (the d is not written), mostanába = mostanában, kapuba = kapuban (same dropped n as mostanába).

## English translation

Sweet Margitka! I inform you that they will recruit in May, but only those who have not yet been in the ranks, so now you can be at ease, sweet. But now do not pick off the caterpillars any more, leave everything as it is. Then it would be good, my darling, if ángyika (an aunt, or a sister-in-law by marriage) came down soon to look at a house, so that by then there would be one(?, the subject is unstated). But now I will not write more, because I am unwell; as I notice, I caught a bad cold there at the gate.

On my card this little flower interprets my feelings.

I wish: may every hour of yours go well in the distance!

Now your loving sweetheart greets you and kisses you countless times (Árpád)

Mezőkövesd, 17 March 1916.

## Slovak translation

Sladká Margitka! Oznamujem ti, že v máji budú odvádzať, ale len tých, čo ešte neboli na vojne, takže teraz už môžeš byť pokojná, sladká. Ale teraz už nezbierajte húsenice, nechajte všetko tak. Potom by bolo dobre, moja milá, keby už v týchto dňoch prišla dolu ángyika (teta alebo švagriná cez manželstvo) pozrieť dom, aby dovtedy nejaký bol(?, podmet nie je uvedený). Ale teraz už viac nepíšem, lebo mi je zle; ako pozorujem, tam pri bráne som sa poriadne prechladil.

Na mojej pohľadnici tento kvietok tlmočí moje city.

Želám si: nech ti každá hodina v diaľke plynie dobre!

Teraz ťa pozdravuje a nespočetnekrát bozkáva tvoj milujúci milý (Árpád)

Mezőkövesd, 17. marca 1916.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1138/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign of `work/transcription.txt`, asserts each word against the reading column, and prints the text from those words. The `@open` lines of the transcription and the address are text in clear, read and not decoded. Capitals, punctuation and `(d)` are mine, in the reading column. Word breaks in the transcription are mine. For the upright view use `work/crops/full51.png` (made by `work/rot_full.py`), not `rot48.png` or anything cut from it: that one is truncated.

## Uncertainties

1. Plain 9 as z, by word sense only, three times: `azokat`, `aztán`, `házat`. I looked for a comma on enlarged crops and saw none at any of them. At `házat` the stroke over the 9 belongs to the `7,` of the row above. The table gives `apokat`, `aptán`, `hápat`, which are not words. On the same card 9 = p in `alaposan`, `kapuba` and `Árpád`, and the comma form is written in sorozni, nézni, üdvözöl, érzelmem, megfáztam. The writer seems to have dropped the comma.
2. `akkorra lenne`: the words are clear, "by then would be". The card does not state the subject. The house is the likely one, and that alone is marked (?) in the translations. "By then" probably means May, which is an inference.
3. `lehec` rests on one `2` with no mark; I read it as a phonetic spelling of `lehetsz`. If a comma was dropped it would be `lehecs`, the same word.
4. `ke(d)vesem`: the signs are `7 1: 3. 1: 7, 1: 8`, so the d is missing on the card. `kedvesed` is spelt fully in the signature. The word is taken as a slip.
5. Blot after `8 1'` at the end of row 2, heavy and pen-made, a thick stroke running right. `május` reads through it (`8 1'` then `6 .1 7,` at the start of the next row). It is most likely the row-end dash of `má-jusba`, drawn heavily; rows 7, 10 and 11 end in a thin dash of the same shape. Nothing is restored. If a sign is hidden there, the word is not `május`. Rows 7 and 10 show the writer used the dash loosely, since `hagyjatok` and `nem` are complete at theirs, and row 9 has none.
6. `már` in row 6 has a stray dot low left of the 1. Taken as a slip. The `7,` in `alaposan` is blotted with a blue overstroke; its comma is clear.
7. `ángyika`: the gloss is the usual meaning of the word. Who she is on this card is not known.
8. `ott a kapuba`: the words read; why he stood at a gate is not stated. Guard duty would fit but is not on the card, and I do not claim it.
9. Stray marks not decoded: `)` closes phrases with no opening bracket, and a small `:` with a curved rule and a dot follows `megfáztam)`. A violet pencil mark near row 12 is a later addition.
10. `Rózsareményű` in the open address is a playful title; hcp-1174 has `Szépreményű`.
11. Grey dot below right of the first 7 of `akkorra`, with a thin grey trail down to the 7 of row 11 (`review/work/r2/Z1.png`). It sits where the dot of `7.` sits. Read strictly that gives `aszkorra`, no word. It is paler than the writer's dots and the trail suggests a smear or pen drag, so I read plain 7. This call rests on word sense. Whether the dot is the writer's ink or a later smear cannot be settled from the scan.

## Why I believe it is correct

- A key taken from other cards decodes `Édes Margitkám`, `csókol`, `szerető kedvesed`, `Árpád` here without adjustment.
- All 409 signs in 84 words read as continuous Hungarian with one fixed table and no unread word. The exception to a strict table reading is item 1, three plain 9s read as z.
- The reviewer's independent row reading (`review/work/own_decode.py`) now agrees with `work/transcription.txt` in all 409 signs. It was reached with knowledge of my round 1 text except at the row ends, so it is not fully blind. Its second pass (`review/work/r2/own.py`), own table and own word divisions, also agrees in all 409 signs and was likewise not blind.
- The new values were each forced by words and each recur in other words, except `8.`, which rests on one word, the pattern and sister cards.
- The sense fits March 1916: a call-up in May for men not yet served, a young man reassuring his girl, and a card with a printed rose as the `kis virág`.
- `alaposan megfáztam` and `rosszul vagyok` agree with `többet nem írok`; `Kívánom:` in clear introduces a complete wish in cipher.

## Response to review 1

Verdict was REVISE. I reread all the cited places myself on the reviewer's crops and on my own new crops (`work/crops/rowends.png`, `row13.png`, from `work/rot_full.py`). All ten findings are correct and all are accepted. No disagreement.

1. Row 11 truncated, `oba` (blocker): fixed. The card continues after `0` with `8, 8, 1. 7 1. 9 .1` and a dash, then `1, 1.`: `ott a kapu-ba`. My "card edge" was the crop edge of `rot48.png`. `{oba}`, its uncertainty item and its place in both translations are gone; `kapuba` as `kapuban` is noted under odd forms.
2. Row 10 truncated, "no `nem`" (blocker): fixed. `8, 6, 1: 8` follows `8, 0, 1, 1, 1:`, giving `többet nem`. The clause now says the opposite of round 1: "I will not write more". Old uncertainty 4 removed.
3. Row 9 truncated, `házi` (major): fixed. The last sign is `1.` with a clear dot and `8,` follows: `házat`, "a house". The speculation about a lost mark is removed; `hogy akkor ra lenne` stays tentative.
4. `hejönne` (major): fixed to `lejönne`. The comma under the 5 is full and separate. I carried a non-word over in round 1 without flagging it; the translations now say "came down".
5. `tolmácsolna` (major): fixed to `tolmácsolja`. The 6 has no comma; the stroke at its upper right belongs to the `6,` of `kártyámon` above. Translations changed to the present.
6. `8.` (major): fixed, `8.` = ty, in the table and `decode.py`. Word is `kártyámon`, spelled correctly. The `kártámon` note is gone. FINAL cards hcp-1142, 1146, 1164 give the same value, which the review did not cite. The `kartim` question on hcp-1179 is for that card; I left it alone.
7. `üdvözölés` (minor): fixed to `üdvözöl és`. The gap is wide on the card. Translations changed. `számtalan szor` in the old transcription is merged to one word, a consequential tidy-up.
8. Hard-coded text in the command (minor): fixed. `decode.py` now prints the enciphered text from the asserted words; the only text not decoded is clear text, and it says so. 409 signs result, as the review predicted.
9. Line-end dashes (minor): fixed. Reported in uncertainty 5, with the row-2 blot as a likely heavy dash. The transcription's `#` for the blot is replaced by `/`, a row break inside the word.
10. Consequential text (minor): fixed. Card sentence, sign and word counts, recurrence list and "why correct" are updated. The plain-9 list stays at three.

A check I added: the sign list of `work/transcription.txt` equals the reviewer's `review/work/own_decode.py`, 409 against 409, with no difference. Reproduction command rerun after the fixes: hashes OK, no mismatch, 409 signs in 85 words.

Decision: the review was REVISE, but I changed the reading substantially, with 12 signs added, one clause reversed and four whole words new, and the review itself asks for a second pass. So this goes to `DONE2`, not `FINAL`. No report or register entry yet.

## Response to review 2

Verdict was REVISE. I reread `review/work/r2/Z1.png` myself. All four findings are correct and accepted, with one note on the reviewer's aside about hcp-1146.

1. `akkor ra` is one word (major): fixed. The signs `1. 7 7 0 3, 3, 1.` run with no gap; the two 3s nearly touch. The break was mine and was wrong. `work/transcription.txt` and the plaintext now have `akkorra`, "by then". English and Slovak are rewritten: "so that by then there would be one", with a marker only on the unstated subject. The old Uncertainty 2 is replaced by a short note on that subject, and `ra = rá` is out of the odd forms. No sign value changed.
2. Dot at the first 7 of `akkorra` (minor): fixed, now Uncertainty 11. On Z1 the dot is grey with a trail to the row below, unlike the writer's black dots. Plain 7 stays in the transcription, as a call by word sense.
3. Slovak `vzdialene` (minor): fixed to `v diaľke`.
4. Counts (minor): fixed. 84 words in the card section and in "Why I believe it is correct", 409 signs unchanged.

Note on hcp-1146: the review did not find `8.` there in its grep. It is there. That card's SOLUTION.md gives `kártya` from `8.` and its `decode.py` has `'8.': 'ty'`. The citation stands, and the key section now names the word on each of the three cards.

Reproduction command rerun after the fixes: 4 hashes OK, no mismatch, 409 signs in 84 words, 3 plain 9 as z, 1 `8.`.

Decision: one word division and one clause of translation changed, no sign or key value. That is not a substantial change, so this goes to the report, the register entry and `FINAL`. With `akkorra` no whole clause is left unread. `ott a kapuba` and `ángyika` are understood as words; only their circumstances are unknown.
