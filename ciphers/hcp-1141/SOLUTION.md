# hcp-1141 solution (round 1, corrected after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal attaches no solution or transcription, and none was found (see SOURCES.md). The transcription is my own, from `work/hires/`.

## Card

Picture postcard, a couple at a fence, no writing on the picture side. Message side: all 24 lines are enciphered; only the place and date are open. Address, open: Őnagysága / Szépreményű Sziber Margitka kisasszonynak / Szomolya / u. p. (Bogács) (Borsod m.). The writer signs in cipher as Árpád, as on hcp-1174.

## Cipher type and key

Register label: MASC. Hungarian, one sign per letter, Hungarian digraphs one sign. A sign is a digit plus an optional mark, and the mark changes the letter. This is the Mezőkövesd family key (hcp-1174, 1178, 1179). Word gaps exist but are not consistent; the word divisions in `work/transcription.txt` are mine.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2,` | cs | | `5,` | l |
| `0,` | ö, ő | | `2.` | é | | `6` | j |
| `1` | i, í | | `3` | d | | `6,` | n |
| `1.` | a | | `3,` | r | | `6.` | ny |
| `1:` | e | | `3.` | v | | `7` | k |
| `1'` (high dot) | á | | `4` | f | | `7,` | s |
| `1,` | b | | `4,` | g | | `7.` | sz |
| `:1` (dots at left) | u, ú, ü, ű | | `4.` | gy | | `8` | m |
| `2` | c | | `5` | h | | `8,` | t |
| `9` | p | | `9,` | z | | | |

All 29 signs are used on this card. `:1` does not separate u from ü here (rosszul, kunn, nélkül, üdvözletemet). `2` = c occurs in harctéri and Galiciába. `1,`, `4`, `4.`, `6`, `6.` were not in the hcp-1174 table; they were fixed on this card and agree with the values filed on hcp-1145, 1147, 1153, 1163, 1165 (`4` = f also on hcp-1175, `1,` = b on hcp-1179).

## Plaintext (Hungarian)

Sentence punctuation is partly editorial; the writer's own marks are `!`, `( )`, the `:` after az, and commas after the verse words.

    Édes Margitkám!

    A napok nállad nélkül nagyon rosszul telnek, de szeretnék legalább esténkint
    együtt lenni vélled.

    (Harctéri tudósítás) Galiciába megint támadnak az oroszok minden vonalon, de az
    nem baj. Jelenleg többet nem írok. Majd írd meg, hogy megkaptad-e a lapokat.

    Ott kunn a hó tornyosulhat,
    jég is hullhat, szél is dúlhat,
    megzörrentve ablakom)
    soha nem panaszkodom,
    mert szívemben itt van az:
    édes kép, a friss tavasz.

    Téged látlak mindég álmomban,
    álmom után minden dolgomban,
    ha sóhajtok érted a panasz,
    ha víg vagyok érted vagyok az.

    Sok csókomat és üdvözletemet küldve maradok hű imádód a sírig (Árpád)

    Mezőkövesd, 1916, II/29 (open)

`nállad`, `vélled` (for nálad, véled) are spelled with two l signs by the writer. `mindég` is a normal variant of mindig.

## English translation

Sweet Margitka!

The days go very badly without you, but I would like to be together with you at least in the evenings.

(War report) The Russians are attacking into Galicia again on every line, but that does not matter. For now I write no more. Later write and tell me whether you received the cards.

Out there the snow may pile up, / ice may fall, wind may rage, / rattling my window; / I never complain, / for in my heart there is this: / a sweet image, the fresh spring.

You I see always in my dreams, / after my dream, in everything I do; / if I sigh, the lament is for you, / if I am merry, it is for you I am.

Sending many kisses and my greetings, I remain your faithful adorer unto the grave (Árpád)

Mezőkövesd, 29 February 1916.

## Slovak translation

Moja sladká Margitka!

Dni bez teba ubiehajú veľmi zle, ale chcel by som byť s tebou aspoň po večeroch.

(Správa z bojiska) Rusi znova útočia do Haliča na celej línii, ale to nevadí. Teraz viac nepíšem. Potom mi napíš, či si dostala pohľadnice.

Vonku sa môže kopiť sneh, / môže padať ľad, môže zúriť vietor, / nech mi rachotí oknom; / nikdy sa nesťažujem, / lebo v srdci mám toto: / sladký obraz, svieža jar.

Teba vidím stále vo svojich snoch, / po sne vo všetkom, čo robím; / ak vzdychám, je to žiaľ za tebou, / ak som veselý, som ním pre teba.

Posielam veľa bozkov a pozdravov a zostávam tvoj verný ctiteľ až do hrobu (Árpád)

Mezőkövesd, 29. február 1916.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1141/work/decode.py

It checks the SHA-256 of the four scans, decodes every sign of `work/transcription.txt` with the key, stops if any word differs from the stated reading, and prints the raw decode, the counts and the plaintext. The verse layout and punctuation in its output are fixed text; the check covers the letters. Output: 480 signs, 96 words, 477 by the table, 3 read by sense.

## Uncertainties

Three signs are marked `~` in `work/transcription.txt`. The bare table would give a non-word at each:

1. `nállad`: second 5 has a long flat foot and no separate comma, table gives h (`nálhad`). Read l. The foot may be a merged comma, and `vélled` has the same double l with both commas clear.
2. `nagyon`: last 6 has no comma, table gives j (`nagyoj`). Read n by word sense.
3. `látlak`: first 5 has no comma, table gives h (`hátlak`). Read l by word sense and the verse.

Other points:

- `tudósítás`: the s is now transcribed `7,` (changed in review, it was `~s`). A stroke of comma width starts under the foot of the 7 and touches the top of the 1 on the next line; the kink where they meet shows two strokes. Because they touch, this comma is less clean than the others.
- `tavasz`: the last sign (line 17) has a malformed foot, a blob with a short upright under the crossbar, and no free dot. I read `7.` with the dot merged; the rhyme az / tavasz supports sz. Bare 7 would give `tavak`, which fails the rhyme.
- Two free dots stand after `panaszkodom` (line 15): one to the right of the final 8 (near x 1100, y 1202 on the hires scan), one lower, directly above the 1 of `van` on line 16, which also has its normal low dot. I take them as that line's full stop and a stray. Neither is part of a sign: `8.` is not in the key, and a 1 with a dot above and below makes no word in `van`.
- `kép`: the comma after `7 2. 9` stands well to the right of the 9, unlike every real `9,` on this card, so I take it as punctuation. If it were part of the sign the word would be `kéz` (hand), which fits the sense worse. This is the one word whose letter rests on mark position plus sense.
- `imádód`: the á rests on a high dot, next to the line-end hyphen. A second dot cannot be wholly excluded under the hyphen, but `imédód` is no word, and imádód closes hcp-1145, 1147, 1153, 1163 and 1165.
- `megzörrentve ablakom)`: a closing bracket with a short rule after it and no opening bracket. I read it as a mark, not a sign, and its purpose is unexplained.
- `a lapokat`: there are two strokes here. The section divider runs separately beneath the words; a second stroke leaves the left end of the divider, rises through `a lapokat` and stops at the 7 of `lapokat`, with a heavier spot there. It has the grey-blue tone of the faded ink around it. It may be a flourish or a partial strike of the phrase; I cannot tell which, and a deletion is not excluded. The words read either way and are kept in the plaintext.
- `megkaptad-e`: no hyphen on the card; the final `1:` stands at the green margin line.
- Galiciába is illative (into Galicia) as written. I did not test whether the report matches events in February 1916; the bracketed heading may be a joke.
- Postmark: not read beyond isolated letters, so the date rests on the open line. 29 February exists in 1916. The green `1031. 2.` near the bottom left and the circular stamp are collection marks, not message.
- The verses are taken as the writer's or popular verse. I did not find a printed source and did not search for one.
- The Schrödel article was text-searched only (see SOURCES.md).

## Why I believe it is correct

- The key was taken from other cards and from this card's opening, then 477 of 480 signs decode as written into continuous Hungarian with no unread word.
- There are 96 words and 29 signs, far too long and too rich for a forced fit: rhyme falls where it should (hullhat / dúlhat, ablakom / panaszkodom, az / tavasz, álmomban / dolgomban, panasz / az).
- Rare words come out unforced: tornyosulhat with `6.` = ny, megzörrentve with `9, 0, 3, 3,`, harctéri with `2` = c.
- Names and context fit: Édes Margitkám, the signature Árpád, the closing `hű imádód` as on sister cards, Galicia and the Russians in wartime 1916, and asking whether cards arrived.

## Response to review 1

Verdict ACCEPT, seven minor findings. No letter of the plaintext changed. I rechecked each point on the reviewer's enlargements and, for finding 4, on a new 4x crop of the hires scan.

1. `után`: agreed, fixed. The dot stands high on the stem, level with the `1'` of `látlak` directly above it; a real `1.` dot sits at the foot. `work/transcription.txt` now has `1'` with no override.
2. `tudósítás`: agreed, fixed. The stroke under the 7 has comma width, and the kink where it meets the 1 below shows two strokes. Now `7,` with no override; the contact is noted under Uncertainties. Counts are now 477 by the table, 3 by sense (`nállad`, `nagyon`, `látlak`).
3. `tavasz`: agreed, disclosed under Uncertainties. The sign stays `7.`.
4. Free dots near `van`: agreed, disclosed under Uncertainties. Both dots are visible on the crop. Neither changes a letter.
5. Rule over `a lapokat`: agreed, description corrected here and in NOTES.md. The stroke is separate from the divider beneath the words and stops at the 7, so "divider, not a deletion" is withdrawn and a partial strike is left open. "Pencil" is withdrawn.
6. Stale header: fixed. `work/transcription.txt` no longer mentions `ODD`.
7. Wording: fixed. The open date is now `1916, II/29`, in SOLUTION.md and in the output of `work/decode.py`. `de` is now "but" in English and "ale" in Slovak.

Reproduction rerun after the changes: `python3 -I ciphers/hcp-1141/work/decode.py` reports hashes OK (4 files), 480 signs, 96 words, 477 by the table, 3 read by sense, 29 distinct signs, and every word check passes.
