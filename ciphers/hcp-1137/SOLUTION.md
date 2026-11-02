# hcp-1137 solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. The transcription is my own, read from `work/hires/`. The portal says Not solved and attaches no solution or transcription. The article it links (Schrödel, "Cryptographic postcards", HistoCrypt 2021) has, on its landing page, no decipherments and no mention of Hungarian cards; I saw only that page, not the full text.

## Card

Picture side: printed roses with a faint printed signature at the left edge, no handwriting. Address side: open place and date `Kis Terenne, 1916 VI 10` (as written; the modern name is Kisterenye) and one open word start `Érte`; everything else on the message side is digits, in 21 rows (two rows at the bottom right run beside the address). Three pencil rules divide prose, verse and close. Open address: `Őnagysága. / Sziber Margitka Kisasszonynak / Szomolya / (Borsod m.) u. p. Bogács.` The postmark reads KISTERENYE and is consistent with 1916 and JUN 10. The portal file name says Mezokovesd, but the card was written and posted at Kisterenye.

## Cipher and key

Register label: MASC. Hungarian, one sign per letter or digraph. A sign is a digit with an optional mark; the mark is part of the sign. Accent length is not marked except a/á and e/é. It is the key of hcp-1174, 1178 and 1179 (`1,` = b from hcp-1179, `4` = f from hcp-1175). The five signs marked * are not on those cards. They were established independently from this card's own words and also occur, with the same values, on unreviewed sister cards of this run: `4.`, `6`, `6.` on hcp-1150 among others, `.1` and `9.` on hcp-1135, 1138, 1150, 1160, 1164.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2,` | cs | | `6,` | n |
| `0,` | ö, ő | | `2.` | é | | `6.` | ny * |
| `1` | i, í | | `3` | d | | `7` | k |
| `1.` | a | | `3,` | r | | `7,` | s |
| `1:` | e | | `3.` | v | | `7.` | sz |
| `1'` (high dot) | á | | `4` | f | | `8` | m |
| `1,` | b | | `4,` | g | | `8,` | t |
| `.1` (dot left) | u, ú * | | `4.` | gy * | | `9` | p |
| `:1` (dots left) | ü, ű | | `5` | h | | `9,` | z |
| | | | `5,` | l | | `9.` | zs * |
| | | | `6` | j * | | | |

Every 7 is crossed, every 5 has a flag, and these strokes mean nothing. A few long hooks after a word are ordinary commas (after `írni`, `kúthoz is`, `imádód`), as words like `írni` and `is` make clear. The final 3 of `Árpád` also carries a long hook, taken as the same flourish; as a comma on the 3 it would give r, `Árpádr`, which is no name. Hyphens at row ends inside a word (`Tere-nyén`, `találkoz-tam`, `Szent-kúthoz`) are ordinary word-break marks; the one after `ápolom` ends a word and a verse line, so it is a dash. A short tick before the first sign of the heading is taken as meaningless.

373 cipher signs, 30 distinct, the 30 of the table: 370 give their letter as written; 3 lack their mark and are corrected by sense, and one word has a letter omitted (below).

## Plaintext (Hungarian; [ ] = enciphered on the card)

Kis Terenne, 1916 VI 10

[Édes Margitkám]!

Érte[sítlek hogy már itt vagyok Terenyén, még Rózával nem találkoztam, lehet hogy elmegyek a Szent-kúthoz is, egyeb újságot nem tudok írni, szervusz]

[Elhervad a rózsaszál is, / Ha megcsípte már a dér, / Elhervad a leány is, hogyha / Nem for[r] benne már a vér.]

[Üde az én rózsaszálam, / Meleg ágyban ápolom, / Forr a vére a babámnak, / Mert hisz gyakran csókolom.]

[Azért, hogy eljöttem, szeress csak továbbra, / Mert még visszatérek ismét hozzád, lányka.]

[Számtalanszor ölel és csókol a távolból hű imádód, Árpád]

Writer's forms are kept: `egyeb` (normal `egyéb`), `for` with one r (normal `forr`), `Értesítlek` without the linking vowel (normal `értesítelek`; the same writer uses this form on hcp-1138, 1143, 1146, 1150, 1153), `Terenyén` in cipher against `Terenne` in clear. Commas in the verse and the sentence breaks are editorial.

## English translation

My sweet Margitka! I let you know that I am already here in Terenye; I have not yet met Róza; perhaps I will also go to the Szentkút (the Holy Well); I can write no other news; bye.

The rose too withers once the frost has nipped it; the girl too withers if the blood no longer boils in her.

Fresh is my rose; I tend her in a warm bed; my sweetheart's blood boils, for I kiss her often.

(`Meleg ágyban` also suggests `melegágy`, a garden hotbed, which suits the rose image.)

Though I have gone away, go on loving me, for I will yet come back to you again, girl.

Countless times your faithful adorer embraces and kisses you from afar, Árpád

## Slovak translation

Moja sladká Margitka! Oznamujem ti, že už som tu v Terenyi; s Rózou som sa ešte nestretol; možno pôjdem aj k Svätej studni (Szentkút); iné novinky ti napísať neviem; servus.

Aj ruža zvädne, keď ju zasiahne mráz; aj dievča zvädne, ak v ňom už nevrie krv.

Svieža je moja ruža, opatrujem ju v teplej posteli; mojej milej vrie krv, veď ju často bozkávam.

Hoci som odišiel, ľúb ma ďalej, lebo sa k tebe ešte vrátim, dievčatko.

Nespočetnekrát ťa z diaľky objíma a bozkáva tvoj verný ctiteľ, Árpád

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1137/work/decode.py

It checks the SHA-256 of all four scans, decodes the whole sign-by-sign transcription exactly as written, asserts each word against the stated reading (the four words below against their table output), and prints the text and the counts. The open text and address are hard-coded.

## Uncertainties

Words corrected by sense (all in `SENSE` in the script; the words are certain, the signs do not give them as written):

1. `csókolom`: the 5 has no comma, so the table gives h, `csókohom`. The area round it is clean and the printed line does not hide a comma (`work/crops/y2.png`). The rhyme with `ápolom` fixes the word.
2. `lányka`: the same, 5 with no comma, so the table gives `hányka` (`work/crops/z2.png`). `hányka` is not a word; the same omission occurs in `csókolom`, `lányka` fits "hozzád", and the writer uses `lányka` in verse on hcp-1150 (as filed there; I did not reread that card). Of the four, this rests most on sense. The stem through the `6.` is the comma of the 8 above running into it.
3. `rózsaszál` (row 7): plain 1 with no dot (`work/crops/z4.png`), so the table gives `rózsiszál`. Row 11 has the same word with `1.`.
4. `számtalanszor`: the m is simply omitted. The card has an ordinary `8,` with a long comma, then `1.`, so the table gives `szátalanszor` (`review/work/crops/szam2.png`). The faint strokes round it do not resolve into a second 8. The word is certain and is the writer's usual closing (hcp-1138, 1144).

Other points:

- `9.` = zs rests on this word alone, twice, on this card; it contrasts with `9,` = z in `Rózával` on the same card.
- `.1` = u/ú: kúthoz, újságot, tudok, szervusz, four words agree. The single dot is left of the stem.
- `Szent-kúthoz`: read as the pilgrimage place Szentkút (Mátraverebély), near Kisterenye. The geography is my knowledge, not on the card.
- `Róza`: a person unknown to me.
- `a távolból` is a short row standing above the last row. I read it after `csókol`, as an insertion. It could instead stand elsewhere in the closing sentence; no word changes.
- `6,` in `ágyban` has a filled, retouched loop; the comma is clear.
- Some marks lie under the Schrödel collection stamp or the postmark ring: the comma after `találkoz` and the end hyphen (stamp postmark ring), and the end of the closing rows (collection stamp); I separated pencil from stamp by colour (`work/ink.py`, crops u1, u2, u3). The `Árpád` signs are read through the stamp but are complete.
- The verses may be a printed or folk rhyme; I did not identify a source and the card's own digits are the only evidence for the wording.

## Why I believe it is correct

- A key built on other cards decodes 370 of 373 signs as written into continuous Hungarian with no fitting of new words.
- The new signs each act consistently over several words, and the gaps fill exact Hungarian (`gy` in hogy, vagyok, egyeb, gyakran; `ny` in Terenyén, leány, lányka).
- The verse rhymes: dér / vér, ápolom / csókolom.
- `Terenyén` agrees in place with the open `Kis Terenne` and the postmark KISTERENYE, though the writer spells it `Terenne` in clear and `Terenyén` (with `6.` = ny) in cipher, and `Szent-kúthoz` with the place. `Margitkám` and `Árpád` agree with hcp-1174, and the hcp-1150 solution describes a card from the same place with the same layout.
- The whole message is enciphered, so there is no open context the key could have been bent to.

No published solution of this card was found. Credit: all reading by Claude Opus 5.5; key from the FINAL cards hcp-1174, 1178, 1179 and the notes of hcp-1175; the five signs marked * established on this card and matching unreviewed sister cards.

## Response to review 1

Verdict REVISE. All six findings addressed; no sign or letter of the cipher reading changed. `python3 -I ciphers/hcp-1137/work/decode.py` was re-run after the fixes: hashes pass, 373 signs, 30 distinct, all words assert. `review/work/decode_review.py` now agrees with the transcription in every token.

1. **Place name (major): fixed.** I looked at `review/work/crops/place.png`: the card has `Kis Terenne`, capital T, double n, no y. SOLUTION.md and decode.py now give the card; the modern form is only a note, and the agreement sentence states the two spellings.
2. **`számtalanszor` (minor): fixed.** The pseudo-sign `8~mt` is gone; decode.py has plain `8,` and the expected table output `szátalanszor`. On `szam2.png` I see the 8, the long comma and then `1.`, as the reviewer says. Described as m omitted.
3. **Count (minor): fixed.** The pseudo-tokens are removed from the transcription altogether (`1`, `5`, `5`, `8,`, what the card has). The script now asserts that the distinct signs are exactly the 30 of the key.
4. **"New" signs and credit (minor): fixed.** Now marked * and described as established independently here and also on unreviewed sister cards. Credit line extended.
5. **Undisclosed small points (minor): fixed.** The hook on the last 3 of `Árpád`, the `Tere-nyén` hyphen, the dash after `ápolom` and `Értesítlek` are all stated in the key section or the spelling note. I checked the sister cards: `Értesítlek` is the writer's habit.
6. **Translations (minor): fixed.** "My sweet Margitka", "Moja sladká Margitka", and a note on `melegágy`.

Additional: the reviewer did not study the picture side. I did: printed roses, the collection stamp, and a faint mark at the left edge in the printed colour (`work/crops/pic_left.png`), a printed signature, not handwriting or cipher.
