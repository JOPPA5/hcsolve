# hcp-1150 solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal attaches no solution. No published solution turned up; the HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. The transcription is my own, from `work/hires/`.

## Card

Picture side: forget-me-nots, no writing. Address side: open place and date (Kisterenne, 1916 VI/..), open address (Őnagyságn. Sziber Margitka Kisasszonynak, Szomolya, Borsod m., u. p. Bogács). All the message, about 420 signs in 20 rows, is in digits. Rows run across the divider up to the stamp. Three horizontal pencil rules separate the prose, the flower verse, the star verse and the close. The card was sent from Kisterenye, not Mezőkövesd as the sister cards, though the portal file name says Mezokovesd.

## Cipher type and key

MASC (the family key of hcp-1174, 1178, 1179, here extended). A letter is one digit plus an optional mark. No word divisions. Hungarian digraphs have one sign. A large `)` stands after sentences in rows 8, 9 and 18 and is not a letter.

| sign | letter | sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | `1'` (high dot) | á | `4` | f | `6.` | ny |
| `0,` | ö, ő | `:1` (dots left) | ü, u, ú, ű | `4,` | g | `7` | k |
| `1` | i, í | `2,` | cs | `4.` | gy | `7,` | s |
| `1.` | a (also unmarked á) | `2.` | é | `5` | h | `7.` | sz |
| `1:` | e | `3` | d | `5,` | l | `8` | m |
| `1,` | b | `3,` | r | `6` | j | `8,` | t |
| `9` | p | `3.` | v | `6,` | n | `9,` | z |

New against hcp-1174: `1,` b (stated in the hcp-1179 table), `4` f (the hcp-1179 note reads `4 0, 1, ...` on hcp-1175 as `főb lövöm`), `4.` gy, `6` j, `6.` ny. They were found here in words such as `hogy`, `hétfőn`, `éjjel`, `lányka`, `nefelejcs`. A crossed 7 is 7; an uncrossed 7-shape is a flagged 1. A `0,` with a long comma can look like a 9 (`jött`, `földön`), as hcp-1174 also noted.

## Plaintext (Hungarian; all enciphered except place and date and the address)

Kisterenne, 1916 VI/..

Drága Margitkám!

értesítlek hogy inet [= innét] hétfőn éjjel elutazom hazafelé. Az ünnepek itt nagyon lassan teltek, jobban szerettem volna veled tölteni, no de nem soká ott leszek. Egyéb újságot nem tudok írni. Gerzon hazajött hát hadi szabadságra. Majd szóval többet.

Van egy kis szende virág,
úgy hívják hogy nefelejcs.
Ez a virág tolmácsolom lányka,
engem ne felejts!

Nem bámulok a fényeségre [= fényességre],
ragyognak bár a csillagok,
mert itt a földön reád nézve
egy szebb csillagot láthatok.

Soraimat zárva számtalanszor ölel, csókol és üdvözöl hű imádód (Árpád)

Punctuation, capitals and verse lines are mine. `Ez a virág tolmácsolom` is printed as written; correct grammar would want `Ezt a virágot` or `tolmácsolja`.

## English translation

Dear Margitka! I inform you that on Monday night I leave here for home. The holidays here passed very slowly; I would rather have spent them with you, but I will be there before long. I can write no other news. Gerzon has come home, then, on military leave. More by word of mouth later.

There is a small modest flower, they call it forget-me-not. This flower, I interpret it, girl: do not forget me!

I do not gaze at the brightness, though the stars are shining, for here on earth, looking at you, I can see a lovelier star.

Closing my lines, your faithful adorer embraces, kisses and greets you countless times (Árpád)

## Slovak translation

Drahá Margitka! Oznamujem ti, že odtiaľto v pondelok v noci odchádzam domov. Sviatky tu ubiehali veľmi pomaly, radšej by som ich bol strávil s tebou, ale onedlho tam budem. Iné novinky ti napísať neviem. Gerzon teda prišiel domov na vojenskú dovolenku. Viac potom ústne.

Je jeden malý skromný kvietok, volá sa nezábudka. Tento kvet, tlmočím ho, dievča: nezabudni na mňa!

Nehľadím na jas, hoci hviezdy žiaria, lebo tu na zemi, keď hľadím na teba, môžem vidieť krajšiu hviezdu.

Zakončujúc svoje riadky ťa nespočetnekrát objíma, bozkáva a pozdravuje tvoj verný ctiteľ (Árpád)

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1150/work/decode.py

It checks the SHA-256 of the four scans, decodes each word from its signs, asserts the result against the stated reading, and prints the text. The open place, date and address are hard-coded. It counts 420 signs: 414 by the table, 6 marked `~` in the script.

## Uncertainties

Signs not by the table (the 6 in the script); each rests on word sense:

1. `Az`: the first sign shows a plain `1` under a postmark edge; a low dot may be hidden.
2. `ünnepek`: first sign shows no dots to the left.
3. `nagyon`: the first 6 shows no comma; the head of the sign below it could be hiding one. By the table it is j.
4. `Egyéb`: the third sign is under the black figure 1 of the postmark date; a dash and dot are visible. `é` is a restoration from the word.
5. `szabadságra`: the second a is a plain `1`, no dot seen.
6. `Soraimat`: the second a has the shape of `4.`, a curled `1.`. `4.` gives `soraimgyt`, which is nothing.

Signs read through postmarks or print, kept in the table count but less firm: the `5,` of `éjjel` and `1:` before it (edge of the stamp postmark); the signs of `hazafelé` and `Az` under the sector of the postmark; `6` of `jobban`; `6,` and final `1` of `írni` (under the KISTERENYE ring); `3 7,` of `szabadságra`; `6,` of `nefelejcs`; the opening `1'` of `(Árpád)`, which sits on a stroke I take as `(`.

Other points:

- `Gerzon`: the name is the least firm reading on the card. It is taken as the given name Gerzson with `zs` written as `9,`, which is itself an inference. The first sign is only touched by the postmark ring. Its bar meets the main stroke at mid-height and crosses it, with a short upstroke at the left, the open form of `4`, and its comma ends in a hook like the `4,` of `Drága`, so `4,` g. The alternative `1,` b (`Berzon`) cannot be fully excluded, because the curled `1.` of `Soraimat` has a similar form. The `0` may be `0,`, and the last sign is partly hidden. Nothing outside this card confirms the name, and I do not know who he was.
- `hát hadi szabadságra`: the signs are clearly `5 1. 8,`. `1.` also stands for an unmarked á on this card (`számtalanszor`), so `hát` (`so, then`) is grammatical and needs no missing unit. The alternative `hat` (`six`) would need a unit such as `heti`. The choice rests on sense.
- `Ez a virág tolmácsolom lányka`: printed as written. It can stand as a parenthesis (`this flower, I interpret it, girl`), which is how I translate it, but the syntax is not fully resolved.
- `reád`: the middle mark is a high dot; I read `1'`.
- `veled`: the second `1:` has one extra high dot beside its colon, taken as a stray.
- `inet` is written with one n and `8,`, `fényeségre` with one s; both kept as written.
- The date ends under the stamp postmark. `VI/` is clear; after it a further `1` and a round digit show at the stamp edge, but I cannot fix the digit. That would fit the 12 June the portal gives. Computed, not checked in a source: Pentecost 1916 fell on 11 June and 12 June 1916 was a Monday, Whit Monday itself. That fits `Az ünnepek`. `hétfőn éjjel` may then mean that same night or a later Monday; the text does not say.
- `Őnagyságn.` in the address is abbreviated as written. I did not fully read the postmark dates.
- The two verses were not found in a published source, and I did not search widely. Copying errors in them would not show.

## Why I believe it is correct

- One table turns 414 of 420 signs into continuous Hungarian with no gaps, and the other 6 are disclosed above. `4`, `4.`, `6` and `6.` each recur in several unrelated words. Most of the table was found on other cards before this one.
- The new values are independently repeated: `4.` in `hogy`, `nagyon`, `egy`, `ragyognak`; `6` in `éjjel`, `jobban`, `hívják`, `majd`, `újságot`, `nefelejcs`, `felejts`.
- The verses rhyme where a rhyme is expected: `nefelejcs` / `felejts` and `csillagok` / `láthatok`. The second stanza rhymes in lines 2 and 4 only; `fényeségre` / `nézve` is at most assonance.
- `nefelejcs` matches the picture side, which shows forget-me-nots, and the card was not used to build that word from any outside hint.
- `(Árpád)` and the closing `számtalanszor ... üdvözöl`, `csókol` match the signature and formula on hcp-1174. Both were decoded from digits.
- `Soraimat zárva` is this writer's closing formula elsewhere: hcp-1135 has the same two words, hcp-1167 `Soraimat bezárva`, hcp-1164 `Zárva soraimat` (these three are not FINAL, so this is support only; the pixels carry the reading).
- The writer on hcp-1174 and here is the same suitor writing to the same addressee, in the same key and copying pencil.

## Response to review 1

Verdict REVISE. All eight findings were checked against the reviewer's enlargements of the hires scan and accepted, with one correction to finding 6. The reproduction command was re-run after the changes (see below).

1. **`várva` to `zárva`: fixed.** In `review/work/z_zv.png` the sign is a loop with a tail running down-left plus a separate parallel comma to the right, so `9,` by the table. I had taken the stem through the pencil rule as part of the sign and missed the comma. Token, plaintext and both translations changed, and the uncertainty entries were removed. The sign 8 in `Soraimat` stands (`z_m.png`), and the former puzzle about `my lines` is gone.
2. **`[B]erzon` to `Gerzon`: fixed, flagged.** In `z_g.png` the sign is touched by the ring, not hidden, and shows the open `4` with a hooked comma. My old argument was also wrong: a comma cannot separate `1,` from `4,`. `Berzon` stays as the alternative, and the reading stays flagged in Uncertainties.
3. **`hat hadi szabadságra`: fixed.** Text and translations now use `hát`, with `hat` as the disclosed alternative. The signs are unchanged; the choice rests on sense.
4. **`leszek`: fixed.** `z_l.png` shows the comma below the 5, crossed by the ring. Token is now `5,`, and the entry was deleted.
5. **`Soraimat`: fixed.** The second a is now token `4.~a` and listed as read by sense. New count: 414 by the table, 6 against it (7, minus `leszek` and `zárva`, plus `Soraimat`). The total stays 420.
6. **Overclaims: fixed, with one correction.** The rhyme claim is restricted to the true rhymes, and `várva` is no longer an exception. The reference for `4` now points to the hcp-1179 note on hcp-1175, because hcp-1175 has no SOLUTION.md. The reviewer could not find `1,` on hcp-1179, but it is in that card's key table (SOLUTION.md there, line 18), so the citation stays.
7. **`Ez a virág tolmácsolom lányka`: fixed.** It is now translated as a parenthesis, and the unresolved syntax is stated. The plaintext is kept as written.
8. **Date: fixed.** The extra `1` and round digit are noted, and Whit Monday is stated as computed, with the open question of which night `hétfőn éjjel` means.

Not resolved, as in the review: whether the first 6 of `nagyon` has a comma, and the postmark date in full. The verses' source and the HistoCrypt article were not checked.
