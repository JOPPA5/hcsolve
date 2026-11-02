# hcp-1149 solution (round 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. The portal shows Not solved and attaches no solution or transcription; the transcription is my own, from `work/hires/`. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it.

## Card

Picture postcard, Mezőkövesd, dated on the card 1916. IV/26, signed in cipher (Árpád), to Szépreményű Sziber Margitka kisasszonynak, Szomolya, u. p. Bogács. Unlike most of the family, almost the whole message is enciphered: a letter, three boxed verses and a vertical verse. Open words sit only in the first and second boxes, plus the place and date. The address is open.

## Cipher type and key

Register label: MASC. Hungarian, one sign per letter or digraph: a digit plus a mark (none, low dot or short dash, two dots, comma, single high dot, or dots to the left). The mark is part of the sign. Word spaces are only partial. The key is the family key of hcp-1174, 1178, 1179, extended by this card.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2.` | é | | `5,` `5.` | l (`5.` perhaps ly, see uncertainty 3) |
| `0,` | ö, ő | | `3` | d | | `6` | j (new) |
| `1` | i, í | | `3,` | r | | `6,` | n |
| `1.` | a | | `3.` | v | | `6.` | ny (new) |
| `1:` | e | | `4` | f | | `7` | k |
| `1'` | á | | `4,` | g | | `7,` | s |
| `1,` | b | | `4.` | gy (new) | | `7.` | sz |
| `:1` | ü, ű, and u, ú (u is new) | | `5` | h | | `8` | m |
| `2` | c (new) | | | | | `8,` | t |
| `2,` | cs | | | | | `9` | p |
| | | | | | | `9,` | z |

The family values are confirmed on a much larger text, and j, ny, gy, c, plus u under `:1`, are added from this card's words. The tentative value `4` = f (hcp-1179) is confirmed here (félegyre, felmegyek, fogsz, fehér, fakaszt).

## Plaintext

Normalised punctuation and spelling for reading; the literal letters are in the command output. [ ] marks the only open words among the cipher in the boxes; everything else in the boxes that is not in [ ] is cipher. The first two lines of box 1 are wholly open.

Édes Margitkám!

Értesítlek, hogy szerencsésen haza értünk félegyre. Nagyon sötét volt, meg nagy borulás, dörgött, villámlott, de nem esett. Szerencse, hogy a lámpát elhoztam: még ilyen hasznát nem vettem, mint most, anélkül sehogy se tudtunk volna jönni, így is csak így bukdostunk.) Erről most többet nem irok, majd ha felmegyek elmondom, hogy hogy értünk le, legalább fogsz rajta kacagni.)

Box 1:
[Nem kérdi senki, hogy a réten / Virág miért terem?]
[Ne] kérd, lányka, [hogy] szívemben
[Miért nyil a] szerelem[?]

Box 2:
A nap sugára süt a rétre,
[S] fakaszt [ott] életet.
[Reám sütött] szemed sugára,
Azóta szeretlek.

Box 3:
Számtalanszor ölel, csókol és üdvözöl hűséges kedvesed (Árpád)
[Mezőkövesd, 1916. IV/26]

Vertical verse, right of the boxes, read bottom to top:
Én fehér madonnám,
szép liliom lányom,
te vagy a világom,
te vagy a bálványom,
üdvöm, boldogságom)

Address (open): Őnsg. / Szépreményű Sziber Margitka kisasszonynak / Szomolya / u. p. Bogács.

## English translation

Sweet Margitka of mine! I let you know that we got home safely by half past twelve. It was very dark and heavily overcast, it thundered and lightened, but it did not rain. Lucky that I took the lamp along: it has never been of such use to me as now; without it we could not have come at all, and even so we only stumbled along.) I will not write more about this now; when I come up I will tell you how we got down, at least you will laugh at it.)

No one asks why on the meadow the flower grows. Do not ask, girl, why love blooms in my heart.

The sun's ray shines on the meadow and brings forth life there. The ray of your eyes shone on me; since then I love you.

Countless times your faithful sweetheart (Árpád) embraces, kisses and greets you. Mezőkövesd, 26 April 1916.

My white madonna, my lovely lily girl, you are my world, you are my idol, my salvation, my happiness.

## Slovak translation

Moja sladká Margitka! Oznamujem ti, že sme šťastne dorazili domov o pol jednej. Bola veľká tma a silne zamračené, hrmelo a blýskalo sa, ale nepršalo. Šťastie, že som si vzal lampu: ešte nikdy mi tak neposlúžila ako teraz, bez nej by sme vôbec nemohli prísť, aj tak sme sa len tackali.) Viac o tom teraz nepíšem, keď prídem hore, porozprávam ti, ako sme sa dostali dolu, aspoň sa na tom zasmeješ.)

Nikto sa nepýta, prečo na lúke rastie kvet. Nepýtaj sa, dievča, prečo v mojom srdci kvitne láska.

Slnečný lúč svieti na lúku a kriesi tam život. Na mňa svietil lúč tvojich očí; odvtedy ťa ľúbim.

Nespočetnekrát ťa objíma, bozkáva a pozdravuje tvoj verný milý (Árpád). Mezőkövesd, 26. apríla 1916.

Moja biela madona, moje krásne ľaliové dievča, ty si môj svet, ty si moja modla, moja spása, moje šťastie.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1149/work/decode.py

It checks the SHA-256 of the four scans, decodes `work/transcription.txt` sign by sign, stops if any line differs from the stated reading (accents the key does not mark are folded), and prints the full text. Open words are in the transcription file as open text; the script decodes only the cipher signs.

## Uncertainties

No word is unread. The points below are small:

1. Sense-assisted sign calls. These signs are read with help from the word, because the mark is fused or hard to separate: the comma of `4,` in `hűséges` and `világom` is joined to the stem or to the digit of the next row (`work/crops/s3.png`, `s1.png`); the `7,` in `boldogságom` has the comma merged into a hooked tail (`work/crops/r7.png`); `0,` in `sötét` has its comma joined so that it looks like a 9, as noted for this writer on hcp-1174; in `dörgött` and `vettem` the first `8,` has a comma running out of the body. The final `7` of the first `értünk` has a small tick at its foot, read as part of the digit since `értüns` is no word. The first sign of `hűséges` is a closed S-shape close to an 8, with its overbar detached to the right, over the following `:1` (`review/work/crops/Y3.png`); I first read it as 8. It is a barred `5`, because `mű-` gives no word and an 8 in this hand is compact with no bar. In `legalább` the sign `1'` before `1, 1,` carries its high dot and also a small separate dot at the foot (`review/work/crops/Z1.png`), which by my convention would be `1:` and give `legalebb`. A true `1'` has no lower dot. I take the low dot as a speck or slip, on word sense; the transcription keeps `1'`.
2. Faint upper dots. In `1:` a few upper dots are faint or brownish (`szerencsésen`, `vettem`), and in `3. 1. 7,` of `kedvesed` the dots sit over the card's faint printed text. Read as `1:` because the lower and upper marks are both seen; word sense agrees.
3. `5.` in `ilyen`. This is the only `5.` on the card, and it stands where standard spelling has `ly`. Two readings are open. For ly: the key's series pairs a base and a palatal (`4,`/`4.` g/gy, `6,`/`6.` n/ny), so `5,`/`5.` l/ly is the expected value, and `ilyen` is the exact place it would be used. For plain l: FINAL hcp-1178 and 1179 use `5.` for l (`csókollak`, `legszeb`), and this writer also spells `melnek` on hcp-1160. One occurrence cannot settle it. I print `ilyen` in the normalised text; the script keeps the literal `ilen` because its table holds `5.` = l. The word and the meaning do not change.
4. `S` in box 2 is a single looped sign that I read as an open cursive capital S (`work/crops/r2.png`). It is not in the key, and `S fakaszt` is good sense.
5. `Reám` in box 2 (open): the a is formed by a round bowl and a short stem, so it can look like `Reoim` (`work/crops/r1.png`). The accent stroke and the sense fix it.
6. Writer's spellings kept by the cipher: `eset` for esett, `kérd` for kérdd (`ilyen` only if `5.` is l, see item 3). The sign `:1` is the same for u and ü, so `tudtunk`, `bukdostunk`, `sugára`, `borulás` are spelled with it; I print them with u by sense, and the script's check folds u to ü. Also ó, í, ő, ú, ű are not marked by the key.
7. Marks without a letter value: the `!` after the salutation (printed in the plaintext, not in the transcription), a pair of short strokes below the end of `elhoztam`, a dash after `mint`, a dash after `raj` at the row end (in effect a hyphen in `raj-ta`), a dash after the second `sugára`, the two `)` that close `bukdostunk` and `kacagni` without an opening bracket, the `)` after `boldogságom`, and a row of short dashes along the top of the vertical verse (`work/crops/e4.png`, `w4.png`). I treat them as punctuation or decoration; their exact meaning is not known.
8. The reading order of the vertical verse (bottom to top, rows left to right) comes from the orientation of the digits and from the rhyme. Its place in the whole message after the signature is an assumption.
9. `félegyre` is taken as the clock time "half past twelve" (literally "by half of one"). `lányka` and the verses are not identified with a published poem; I did not search for one.
10. I did not read the postmark, which is inked over the stamps. The date used is the written one, 1916. IV/26, which agrees with the date in the portal's file name.
11. The picture side is a printed couple with lilacs and carries no writing. The speckled patch at its top left is surface damage, not script. So the address side holds all the writing on the card.

## Why I believe it is correct

- One key, taken from reviewed sister cards and extended by only a few values, decodes every cipher sign on the card (the command prints the count) into continuous Hungarian with no gap.
- The text is long (493 signs, 30 distinct) and self-checking. The new signs recur: `4.` in hogy, nagy, vagy, így, felmegyek; `6` in jönni, majd, rajta; `6.` in lányka, lányom, bálványom; `1,` in borulás, többet, bukdostunk, legalább, szívemben, bálványom, boldogságom.
- The story is coherent: a night walk or ride home in the dark, with thunder and a lamp. The verses rhyme: terem / szerelem in box 1 (open word against cipher word), and -om through the vertical verse (lányom, világom, bálványom, boldogságom; madonnám nearly). Box 2 has no clean rhyme: `életet / szeretlek` is at most an imperfect assonance.
- Open words fit the cipher around them: `Ne` + kérd, `hogy` + szívemben, `Miért nyil a` + szerelem answer the open `Nem kérdi senki ... Virág miért terem?`.
- The signature `Árpád` and the salutation match hcp-1174, sign for sign in the salutation. The recipient on the address is the same woman.

## Response to review 1

Verdict ACCEPT. All five findings are minor and concern how signs are reported. No sign, key value or decoded word changed, `work/transcription.txt` and `work/decode.py` are untouched, and the command gives the same output as before (hashes OK, 493 cipher signs, 30 distinct, every line agrees).

1. `legalább`, low dot on `1'`. Agreed; I looked at `review/work/crops/Z1.png` and the small low dot is there. Listed in uncertainty 1 as a sense-assisted call. The transcription keeps `1'`.
2. First sign of `hűséges`. Agreed; `review/work/crops/Y3.png` shows the closed shape and the detached overbar. Added to uncertainty 1.
3. `5.` in `ilyen`. Agreed. Uncertainty 3 now gives both arguments, and uncertainty 6 no longer calls it a misspelling outright. The key table marks `5.` as l or ly. I do not settle it, because one occurrence cannot, and the review's own counter-evidence from hcp-1178 and 1179 stands.
4. Punctuation and picture side. Agreed. Uncertainty 7 now has the `!`, the dash after `raj` and the dash after the second `sugára`. New uncertainty 11 says the picture side has no writing.
5. Box 2 rhyme. Agreed. Reworded to "no clean rhyme".
