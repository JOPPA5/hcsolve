# hcp-1148 solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal lists the card as Not solved and attaches no solution or transcription. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it.

## Cipher type and key

Register label: MASC. The whole message is in the digit cipher of the Mezőkövesd cards. Only the place and date are open. Each letter is one digit plus an optional mark; there are no word divisions. The key comes from FINAL cards hcp-1174, 1178 and 1179 and was extended on this card.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| `1` | i, í | `2,` | cs | `6` | j (new) |
| `1.` | a | `2.` | é | `6,` | n |
| `1:` | e | `3` | d | `6.` | ny (new) |
| `1'` (high dot) | á | `3,` | r | `7` | k |
| `:1` (two dots left) | ü | `3.` | v | `7,` | s |
| `.1` (one dot left) | u, ú; also ü, ű (new) | `4` | f | `7.` | sz |
| `1,` | b | `4,` | g | `8` | m |
| `0` | o, ó | `4.` | gy (new) | `8,` | t |
| `0,` | ö, ő | `5` | h | `9` | p |
| `2` | c (new) | `5,` | l | `9,` | z |

New values: `.1` u, `4.` gy, `6` j, `6.` ny and plain `2` c are not on the three sister cards. Each is set by words on this card: indultunk, tudom; egy, nagy, hogy; rajta, jól; annyi; cipőnk, arcod. `.1` also stands on hcp-1135, 1137, 1138 and 1139. `4` = f was only tentative in the family (hcp-1175); here it is `félhatra`.

On this card the writer often marks the crossed 7 and the plain 1 differently: a 7-shaped sign with no bar is `1`, and only the barred one is `7`.

## Plaintext (Hungarian, punctuation and word division mine)

Édes Margitkám!

Szerencsésen hazaértünk. Háromórakor indultunk és félhatra értünk le. Nagyon sötét volt és nagy sár. A nadrágunk térdig lett vizes, a cipőnk meg egész elázott. Most egyébb nem történt, csak annyi, hogy egy helen [= helyen] át akartam ugrani az árkot és keresztül estem rajta. Már egyebet nem irok. Bocsás [= bocsáss] meg, édes, ha valamit vétettem, mert tudom hogy nem jól cselekedtem.

Mikor együtt voltál velem,
öröm volt a szerelem;
s most hogy arcod nem láthatom,
szerelem lett bú-bánatom.

Üdvözöl számtalanszor, ölel és csókol hű kedvesed (Árpád)

Open on the card: Mezőkövesd 1916. V/9
Address (open): Tek. Sziber Margitka Kisasszonynak, Borsodm., Szomolya, u.p. Bogács

## English translation

Sweet Margitka of mine!

We got home safely. We set out at three o'clock and got down by half past five. It was very dark and very muddy. Our trousers got wet to the knee, and our shoes were completely soaked. Nothing else happened, except that at one spot I tried to jump over the ditch and fell across it. I will not write anything more now. Forgive me, sweet, if I did anything wrong, for I know I did not act well.

When you were together with me,
love was a joy;
and now that I cannot see your face,
love has become my grief and sorrow.

Your faithful sweetheart greets you countless times, embraces and kisses you (Árpád)

Mezőkövesd, 9 May 1916. Address: To the esteemed Miss Margitka Sziber, Borsod county, Szomolya, post office Bogács.

## Slovak translation

Moja sladká Margitka!

Šťastne sme prišli domov. Vyrazili sme o tretej a dole sme boli o pol šiestej. Bola veľká tma a veľké blato. Nohavice sme mali mokré po kolená a topánky úplne premočené. Inak sa nič nestalo, len toľko, že som na jednom mieste chcel preskočiť priekopu a spadol som cez ňu. Viac už nepíšem. Odpusť mi, milá, ak som sa niečím previnil, lebo viem, že som nekonal dobre.

Keď si bola so mnou,
radosťou bola láska;
a teraz, keď nemôžem vidieť tvoju tvár,
láska sa stala mojím žiaľom a smútkom.

Nespočetnekrát ťa pozdravuje, objíma a bozkáva tvoj verný milý (Árpád)

Mezőkövesd, 9. mája 1916. Adresa: Vážená slečna Margitka Sziberová, Boršodská župa, Szomolya, pošta Bogács.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1148/work/decode.py

It checks the SHA-256 of all four scans, decodes `work/transcription.txt` sign by sign through the key, stops on any word whose signs do not give the stated reading, and prints the text and the sign counts. The open lines (place, date, address) are hard-coded in the script. The word divisions in the transcription are mine.

## Uncertainties

The script reports 415 cipher signs: 412 decode by the table and 3 are set by word sense.

1. `valamit` (L12, third sign, `8,~t`; crop `work/crops/y1.png`): a tailed sign that looks partly like a 9. I take the tail as the comma of a joined `8,`. Sense wants t.
2. `ölel` (first sign, `9~ö`; crop `work/crops/a8.png`): 9-shaped with a long tail, not a clear `0,`. hcp-1174 has the same 9-shaped ö. This rests on word sense, since 9 alone is p.
3. `szerelem` in verse line 2 (`1.~e`; crop `work/crops/d2.png`): only the low dot is visible. The 1 touches the following blotted 8, so a high dot could be hidden. The same word in verse line 4 has a clean `1:`.

Readings that rest partly on sense, though counted as table signs:

4. `mert` (L12): the first sign has a heavy, flagged top and could be taken for 5 or 6. Only `8` gives a word. The doubled t of `mert tudom` is one t for each word.
5. `láthatom`: the comma of `8,` runs into the base of the next 5, and I assign it to the 8.
6. `voltál`: besides the high dot of the `á`, a small dot stands low on the left of the 1; I take it as a stray.
7. `bú-bánatom`: the signs are `1, .1 1, 1' 6, ...`. I read the first two as `bú` by the set phrase. The hyphen is mine.
8. Vowel marks: the separation of `1.`, `1:` and `1'` depends on small dots and dashes. I read these from the 1.6x to 3x crops, but where a dot is faint the known word helped. The writer also makes the low mark as a short dash. This affects a vowel at most, not a word.

Spellings kept as written, not corrected:

- `egyébb` (standard egyéb), `helen` (helyen, ly not written), `bocsás` (bocsáss, one s), `egész` for egészen.
- `keresztül`, `üdvözöl`, `hű`: these ü, ű words carry the one-dot `.1`, not `:1`. The writer's one-dot form therefore also stands for ü here, or a second dot was left out or lost. The word is the same either way. The two-dot `:1` stands only in ü words (hazaértünk, értünk, együtt), and no u word has two dots.
- `irok`: no accent is marked. The cipher does not mark vowel length for i and o.

Other points:

- A `)` stands after `cselekedtem` at the end of block 1, with no opening bracket. I treat it as a closing mark. It carries no letter.
- A second, clear `)` stands after the signature. A pale slanted stroke before its first sign is probably the opening bracket, so `(Árpád)` is on the card, as on hcp-1143, 1146 and 1162. The stroke is faint, so the opening bracket is only probable.
- Punctuation is mine, except `!` after the salutation, the brackets above and the line-end hyphens on the card.
- The address word `Borsodm.` is read from the normal-size scan and not studied further. The postmark was not read; the date comes from the open line.
- Who "we" were on the journey is not stated.
- I did not search for a printed source of the quatrain; it may be a popular verse.

## Why I believe it is correct

- The 30 signs of the key decode all 415 cipher signs into continuous Hungarian, 412 of them directly by the table. Nothing is left over.
- 25 of the 30 values come from hcp-1174, 1178 and 1179; `4` was tentative there, and `.1`, `2`, `4.`, `6`, `6.` are the five not on those cards. The opening 13 signs repeat hcp-1174's `Édes Margitkám` heading sign for sign.
- The message has a clear story, with concrete detail (three o'clock, half past five, mud, ditch) and a rhymed quatrain (velem / szerelem, láthatom / bánatom).
- Names fit: Margitka is the portal's recipient, and Árpád is the signature decoded independently on hcp-1174. `számtalanszor` also stands on that card.
- New signs recur consistently: `.1` 9 times, `4.` 9 times, `6` twice, `6.` once and plain `2` twice, always in plain words.

## Response to review 1

Verdict REVISE. I checked each finding on the reviewer's crops and the hires scan, and I accept all five. Letters change in only one word (`bocsás`), plus the vowel spelling of `indultunk`. The story, the key values already in use and the sign count are unchanged. `python3 -I ciphers/hcp-1148/work/decode.py` was re-run: hashes OK, 415 signs (412 by table, 3 by sense), 30 distinct signs, `1:` 47, `1'` 15, `.1` 9, `:1` 3.

1. **`bocses` is `bocsás`: fixed.** In `review/work/c/bocs.png` the 1 after `2,` has one high dot and nothing below it, so it is `1'`, not `1:`. Corrected in `work/transcription.txt`, the plaintext and the spellings list. I misread it because I expected an e-spelling.
2. **`ölelés` is `ölel és`: fixed.** Same letters, new word division, which gives the family closing (hcp-1137, 1143, 1146, 1151, 1153, 1162). The transcription has two entries, and the Hungarian, English, Slovak and uncertainty 2 are updated.
3. **`.1` and `:1` are two signs: fixed.** The montage `review/work/c/dotleft.png` shows all 12 places. Two dots: hazaértünk, értünk, együtt. One dot: indultunk (twice), nadrágunk, ugrani, tudom, bú, keresztül, üdvözöl, hű. `.1` is added to the table and `work/decode.py`, `indultunk` is printed, and the three ü words with one dot are disclosed under the spellings. My earlier claim that one sign covers u and ü was wrong and is withdrawn.
4. **Sign count: fixed.** The table had 29 signs. With `.1` it has 30, all used on the card. `work/decode.py` now prints the count. The figure is 25 of 30, with five new signs listed.
5. **Brackets: fixed.** The `)` after Árpád is clear in `review/work/c/arpad.png`, and the pale stroke before the name is reported as a probable opening bracket.

The reviewer's unverified points stay open: the HistoCrypt article was not checked, the postmark is too fragmentary, "we" is unidentified, and the verse has no located printed source.

## Credit

Key family: Claude Opus 5.5 on hcp-1174, 1178, 1179. Transcription, key extension and decipherment of this card: Claude Opus 5.5. No published solution was used.
