# hcp-1164 solution (round 1, with response to review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal status is Not solved and it attaches no solution or transcription. I found no published solution, but I did not check the HistoCrypt article the portal links, so I cannot say whether it discusses this card. The transcription is mine, made from `work/hires/`.

## Card

Picture postcard, Mezőkövesd to Szomolya, in Hungarian (the portal says language Unknown). Almost the whole message is in cipher, on both sides: 556 cipher signs. In clear are only the address, the date line, and a few words and letters mixed into verse 3.

Address, in clear: Őnsg. / Szépreményű Sziber Margitka Kisasszonynak / Szomolya / (Borsodm.) u. p. Bogács. Postmark Mezőkövesd, 1 APR; the year on the postmark is not clearly legible.

## Cipher type and key

Type: MASC (register label). Each letter is one sign, a digit plus an optional mark (none, dot, comma, colon, high dot). The mark is part of the sign, so `8` is m and `8,` is t. Hungarian digraphs have their own signs. Spaces fall between words. Vowel length is mostly not marked for o, i, u, and ü's sign also serves u, ú and ű; ö's sign also serves ő.

| digit | none | dot `.` | comma `,` | other |
|---|---|---|---|---|
| 0 | o, ó | | ö, ő | |
| 1 | i, í | a | b | `1:` e; `1'` (high dot) á; `:1` (dots left) ü, ű, u, ú |
| 2 | | é | cs | |
| 3 | d | v | r | |
| 4 | f | gy | g | |
| 5 | h | ly | l | |
| 6 | j | ny | n | |
| 7 | k | sz | s | |
| 8 | m | ty | t | |
| 9 | p | zs | z | |

All 31 signs occur on this card. The key comes from hcp-1174, 1178 and 1179 (FINAL cards). This card adds or settles: `4` f, `4.` gy, `5.` ly, `6` j, `6.` ny, `8.` ty, `9.` zs, `1,` b. The pattern is regular: a dot on 4, 5, 6, 8, 9 gives the palatal or zs digraph. The sister cards have no such table, and it was not known before this card.

Conflict with sister cards: `5.` is ly here (3 times: `milyen`, `olyankor`, `oly`), and no l reading gives those words. On hcp-1178 and hcp-1179 the same sign is filed as l (`a legszeb`, `csókollak`), and hcp-1178 says the mark on 5 distinguishes no letter. So the table holds for this card; it does not settle those two cards.

Thin attestation: `9.` zs occurs once (`rózsák`) and `8.` ty twice, both in the word `kártyát`. Both rest on the word and on the dot pattern, with little repetition.

## Plaintext (Hungarian, spelling as on the card)

Punctuation is mostly the writer's; line breaks in the prose and some full stops and capitals are mine. The `)` marks are on the card.

Address side:

    Édes Margitkám!
    Vasárnap nem igen mehetek fel mert it [= itt] van egy kis dolgom pedig
    édes anyámmal is akarnék már beszélni) hacsak lehet azért felmegyek)
    most pedig irok egy kis verset

    Margitkának hívnak téged
    Aranyos vagy igazán —
    Vedd e kártyát üdvözletül
    S gondolj drága néha rám!

    Fogadd ezt a kártyát s vele
    üdvözletem Margitka.
    Nyíljanak ki ablakodban
    Piros rózsák hajnalra.

    Hogy mit jelent az M betű?
    Csak Margitot jelenthet!
    Be szép e név! S kit hívnak így?
    Egy kis babát egy szentet!

    Zárva soraimat üdvözlettel és sok csókkal maradok
    Imádó kedvesed) Árpád) Mezőkövesd, 1916 IIII 1

Left margin, written sideways, with the small dashed box at the right of the verses:

    Nincs e valami bajod mert álmodtam felőled és oly szomorú voltál.

Boxed in the top right corner: Írjál!

Picture side, along the long edge:

    Látod milyen szép a páros élet.
    Olyankor érzem magam boldognak mikor
    így veled lehetek te jó szívű babus.

## English translation

Sweet Margitka! On Sunday I can hardly come up, because I have a little business here, and I would also like to speak with my mother at last; if it is at all possible I will come up anyway. And now I am writing a little verse.

They call you Margitka, / you are truly a darling. / Take this card as a greeting, / and think of me sometimes, dear!

Accept this card, and with it / my greeting, Margitka. / May red roses open / in your window by dawn.

What does the letter M mean? / It can only mean Margit! / How lovely this name is! And whom do they call so? / A little babe, a saint!

Closing my lines with greetings and many kisses, I remain your adoring sweetheart Árpád. Mezőkövesd, 1 April 1916.

Margin: Is something wrong with you? Because I dreamed about you and you were so sad.

Corner: Write!

Picture side: You see how beautiful life as a couple is. I feel happy at such times, when I can be with you like this, you good-hearted darling.

## Slovak translation

Moja sladká Margitka! V nedeľu asi nebudem môcť prísť hore, lebo tu mám nejakú robotu a aj s mamou by som sa už chcel porozprávať; ak to len trochu pôjde, predsa len prídem. A teraz ti píšem malý veršík.

Volajú ťa Margitka, / naozaj si zlatá. / Prijmi túto pohľadnicu ako pozdrav / a mysli na mňa, drahá, niekedy!

Prijmi túto pohľadnicu a s ňou / môj pozdrav, Margitka. / Nech ti v okne rozkvitnú / červené ruže do rána.

Čo znamená písmeno M? / Môže znamenať len Margitu! / Aké krásne je to meno! A koho tak volajú? / Malé dievčatko, svätú!

Končím svoje riadky s pozdravom a mnohými bozkami a zostávam tvoj zbožňujúci milý Árpád. Mezőkövesd, 1. apríla 1916.

Okraj: Nie je ti niečo? Lebo sa mi o tebe snívalo a bola si taká smutná.

Roh: Napíš!

Obrázková strana: Vidíš, aké krásne je žiť vo dvojici. Vtedy sa cítim šťastný, keď môžem byť takto s tebou, ty dobrosrdečná moja milá.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1164/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign of `work/transcription.txt` by the fixed table, stops on any mismatch with the stated word, and prints the full text. Output: 556 signs, 31 distinct. The transcription holds a reading beside each word, used as an assert; the signs alone produce the text. The comparison ignores accents the cipher does not mark.

## Uncertainties

No word is unread. These points rest partly on word sense:

1. `bajod` (margin): the first sign is a blot with a tapering top, shaped like a stem, with a clear comma under it. I read `1,` = b by sense.
2. `mert` (margin): the last sign is a blot with a comma under it; read `8,` by sense. It sits on the crossing of the margin frame.
3. `kedvesed` (closing): the third sign is heavy and could be taken for 8 at a glance; read `3`. `8` gives no word. See `work/crops/j2.png`.
4. `babus` (picture side): I see one dot left of the 1, on the halftone, where `:1` has two; the lower dot may be lost in the comma of the sign before it. Read `:1`, with ü's sign used for u as in `szomorú`. See `work/crops/j3.png`.
5. `nincs e` (margin): the two dots of `1:` stand on green printer's text and are visible at 5x (`work/crops/h2.png`). Written as two words on the card; normal form `nincs-e`.
6. `látod` (picture side): the 0 is filled with ink, so it is a black oval.
7. `it` is one `8,` on the card (`work/crops/k1.png`), with normal form `itt`. I give it as written.
8. `rózsák`: the last 7 has no comma; the star under it is the flourish on the arrow line (`work/crops/j1.png`). With a comma the word would be `rózsás`.
9. Reading order of the margin is by sense. Inner row first, then outer row, then the small dashed box between the verses and the address. The opposite row order gives no sentence. The box and margin share a dashed frame.
10. Corner box: `1 3, 6 1' 5,` = írjál. The second sign is pale with a large upper lobe; the comma is clear. Its top lobe resembles 9, but `9,` gives no word.
11. Translation: `édes anyámmal` is taken as `édesanyámmal`, "with my mother", the writer's mother. It could be meant as "my dear mother" or (less likely) about Margitka's mother, with no change in the sense of the plan. `hacsak lehet azért felmegyek` is colloquial: "if at all possible I will come up anyway".
12. The written month is four strokes, IIII, and the day is 1, matching the postmark 1 APR and the portal's file name 1916-04-01. It is not III. The strokes stand between an over-line and an under-line. There is no slash: the diagonal to the right is the frame and the flag of the 1. The speck after 1916 is the head of the under-line, so no full stop is transcribed.
13. The feathered double line under verse 1 is a drawn ornament, not text, as far as can be seen; the small green `1315` and the green line near the left margin are printer's marks.

## Why I believe it is correct

- The whole card decodes with one fixed table, with no unknown sign and no word left over.
- Verse 1 rhymes igazán / rám; verse 2 Margitka / hajnalra; verse 3 jelenthet / szentet; and the verses scan.
- Most of the key was reached before this card, on hcp-1174, 1178, 1179. New values come from words that repeat: `felmegyek`, `kártyát`, `üdvözlet-`, `milyen`, `olyankor`. Each new sign recurs or fits the pattern above; `9.` and `8.` are the thinnest (see the key section).
- The writer's own clear letters confirm the cipher reading in mixed words: `jelenthe` plus a clear `t`, `szente` plus a clear `t`, and `M betű` is answered by `Margitot`.
- Names fit: Margitka is the addressee, Árpád is the signature on hcp-1174. The date agrees with the postmark. The picture of a couple fits `páros élet`.

## Credit

Key origin: Claude Opus 5.5 on hcp-1174, 1178, 1179. No GPT work was used. Sister-card note: `8.` = ty here may bear on the open point `kar[t?]im` on hcp-1179. For `5.` the cards disagree (see the key section). I have not changed those cards.

## Response to review 1

Verdict ACCEPT. No word of the plaintext changed. All three findings are minor and are addressed.

1. **`5.` filed differently on sister cards: fixed.** The key section now states the conflict. The sign is ly here, by `milyen`, `olyankor` and `oly`, and l on hcp-1178 and 1179.
2. **`9.` and `8.` thinly attested: fixed.** Counted from `work/transcription.txt`: `9.` once, `8.` twice. The key section and "Why I believe it is correct" now name them.
3. **Date line details: fixed.** I checked `review/work/crops/date.png` and `date2.png` and agree. There is no slash, and the dot after 1916 is the head of the under-line. `work/transcription.txt` line 112 and the plaintext now give `1916 IIII 1`, and uncertainty 12 explains it. English and Slovak keep 1 April 1916 as the meaning.

The reviewer's Saturday observation stands: 1 April 1916 was a Saturday (checked with Python), which suits a card about the coming Sunday. It is context only, not evidence for the key.

Re-run after the edit: `python3 -I ciphers/hcp-1164/work/decode.py` gives hashes OK, 556 signs, 31 distinct, no unused key sign.

Still unverified: whether the HistoCrypt article treats this card, whether the verses are borrowed from print, and the postmark year.
