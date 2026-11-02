# hcp-1159 solution (round 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work exists on this number and the portal attaches no solution or transcription; the transcription is my own, from `work/hires/`. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it. The key was not reconstructed here: it is the family key of the Mezőkövesd cards (FINAL hcp-1174, 1178, 1179, and the tables of hcp-1163, 1164, 1166, 1168, 1169).

## Card

Picture postcard (couple with roses) to Sziber Margitka, Szomolya, u. p. Bogács, Borsod m., in the portal name dated 1915-11. The postmark is too faint for a date: only "ME..." and a digit or two can be seen. All writing is on the address side: a heading in digits, four open lines, a dashed rule, the digit block, then an open close.

## Cipher type and key

Hungarian with a monoalphabetic digit cipher (register label: MASC). Each letter is one digit with or without a mark; the mark is part of the sign. No word division.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o | | `2.` | é | | `6,` | n |
| `0,` | ö, ő | | `3` | d | | `7` | k |
| `1` | i, í | | `3,` | r | | `7,` | s |
| `1.` | a | | `3.` | v | | `7.` | sz |
| `1:` | e | | `4,` | g | | `8` | m |
| `1'` (high dot) | á | | `4.` | gy | | `8,` | t |
| `1,` | b | | `5` | h | | `9` | p |
| | | | `5,` | l | | `9,` | z |

Only the 23 signs attested on this card are listed: 125 signs decode by this table as written, and 1 blotted sign is left undecoded. The 5 carries a short flag over it in this hand, as on hcp-1166.

## Plaintext (Hungarian; [ ] = enciphered on the card)

[Édes Margitkám]

Kérlek írd meg, hogy megkaptad-e a levelet, mert küldtem benne a számbetűket is.

[Vedd tőlem e képes lapot
s véle tiszta szívemet
érted lá(n)gol, érted ég az,
míg a sír el nem temet.
Távolban a vágyam nekem,
ha te is itt volnál velem.]

Mindnyájatokat csókollak. Sz. Á.
Írjál.

Address: Tek. / Rózsareményű Sziber Margitka kisasszonynak / Szomolya / u. p. Bogács / Borsod m.

Line breaks and punctuation of the verse are mine. The card runs the signs on without division. (n) = a letter not on the card, see point 1.

## English translation

[Sweet Margitka]

Please write and tell me whether you got the letter, because I also sent the number-letters in it.

[Take this picture card from me, / and with it my pure heart; / it flames for you, it burns for you, / until the grave buries it. / Far away is my longing; / if only you too were here with me.]

I kiss you all. Sz. Á.
Write.

Address: To the honourable / "Rose-hoped" Miss Margitka Sziber / Szomolya / post office Bogács / Borsod county. `Rózsareményű` is a playful honorific, literally "of rose hope", apparently formed like `szépreményű` ("of fair hope"). This gloss is my reading; I know no printed parallel for the word.

## Slovak translation

[Moja sladká Margitka]

Prosím, napíš mi, či si dostala list, lebo som v ňom poslal aj číselné písmená.

[Prijmi odo mňa túto pohľadnicu / a s ňou moje čisté srdce; / pre teba plane, pre teba horí, / kým ho hrob nepochová. / V diaľke je moja túžba; / keby si aj ty bola tu so mnou.]

Bozkávam vás všetkých. Sz. Á.
Napíš.

Adresa: Ctenej / „ružovonádejnej“ slečne Margitke Sziberovej / Szomolya / pošta Bogács / župa Borsod. Masculine `poslal` assumes a male writer, which fits the family's signature but is not shown on this card.

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1159/work/decode.py

It checks the SHA-256 of all four scans, decodes every sign, asserts each decoded verse line against the stated reading, prints the sign counts and the whole card. The open text is hard-coded in the script, so the command proves only the decoding of the cipher signs.

## Uncertainties

1. `lá(n)gol`: the card has `5, 1' 4, 0 5,`, literally `lágol`. There is no `6,` between 1' and 4 (`work/crops/z_lagol.png`), so the n is missing from the card. I read lángol on word sense only, supported by the parallel with `ég`. It is a spelling slip or a dropped sign. The printed `lá(n)gol` is an editorial emendation resting on sense alone; what the card says is `lágol`.
2. Blotted sign after `itt`: `1 8, 8,` is followed by a smeared sign with a clear comma (`work/crops/z_blot.png`, `z_itt.png`). Its body looks like an 8 written over or wiped, so it may be a third `8,`, abandoned. I did not decode it. `itt` is complete without it and the line scans and reads. Read literally as `8,` it would be a dittography, `ittt`.
3. `az` (`1. 9,`): the digit before the last comma could at first sight be an 8. On `work/crops/z_egam.png` it has a closed head and one straight stem with no lower loop, which is a 9, unlike the crossed 8s around it. `9,` = z gives `ég az` ("that burns"; az = the heart). `8,` would give `égat`, no word. So the shape and the sense agree, but the call leans on sense. The sign sits on the card's printed centre line, which touches the dot of the `1.`.
4. `ég` and `az` are divided by me. `égaz` as one word does not exist.
5. `Távolban a vágyam nekem` is rather loose as verse, but every sign is clean. I take a vágyam nekem as "my longing", with the doubled possessive of colloquial speech. Its link with the last line is my punctuation. It may also be a comma-less run-on: "Far away is my longing for me, if only you were here".
6. Unexplained strokes: a horizontal line runs between the 5th and 6th physical cipher rows (`lapot` stands alone as row 2), at about x 480 to 910, y 1300 on the hires scan (`work/crops/z_stray.png`): under `1 3, 1: 5,` of `sír el` and above `1, 1. 6, 1.` of the `Távolban` row. It does not reach `3. 0`, crosses no sign and decodes to nothing. A similar flourish stands above `Mindnyájatokat`. A hyphen stands at the row break inside `ve-lem`.
7. Open text: `a` in `megkaptad-e a levelet` is this hand's a, with the tail of the g above it looking like an accent; `számbetűket` has its accent and double dots partly merged, and the first vowel could be read otherwise, but `szám` + `betű` is the only sense I find. `Sz. Á.`: a stroke stands over the A on the foot crop, so I print Á; the same initials read Sz. A. on hcp-1175, 1176, 1179 as reported on those cards, not re-examined here. hcp-1174 is signed Árpád, which would fit Á., but nothing on this card names him, so that is only a hypothesis. `Rózsareményű` is written in two parts on the card, `Rózsa reményű`; see the gloss in the translations.
8. Date: the portal name's 1915-11 is not confirmed by the postmark.

## Why I believe it is correct

- The key was fixed on other cards and applied without change. 125 of 125 readable signs give continuous Hungarian, with one missing letter (point 1) and no substitute value.
- The text is verse with exact rhyme on `szívemet` / `temet` and `nekem` / `velem`. The heading equals the 13-sign heading of hcp-1174.
- `Vedd tőlem e képes lapot` fits the picture card it is written on. The open line about sending the `számbetűket` ("number-letters") is about the cipher itself, and `írjál` agrees with a message of waiting for a reply.
- Word recognition checks the marks. Each of `3.`/`3,`, `7,`/`7.`, `8`/`8,`, `4,`/`4.` is separated correctly in clean words such as `Vedd`, `véle`, `érted`, `sír`, `szívemet`, `nem temet`, `vágyam`.

## Response to review 1

Verdict ACCEPT. All four findings are minor and none changes the reading. `python3 -I ciphers/hcp-1159/work/decode.py` was re-run after the edits: 4 hashes OK, 125 signs, 23 distinct, 1 blotted sign undecoded, output unchanged.

1. Stray line: fixed in uncertainty 6. I rechecked it on the hires scan (`work/crops/z_stray.png`). My earlier location was wrong; it stands between physical rows 5 and 6. One small addition to the review: at the row below it stands over `1, 1. 6, 1.`, with its left end just over the flag of `5,`. It does not reach `3. 0`.
2. `lá(n)gol`: fixed in uncertainty 1 and the report, now called an emendation, with `lágol` stated as what the card says.
3. Address epithet: fixed. The English and Slovak sections now translate the address and gloss `Rózsareményű`, and the two-part writing stays disclosed in uncertainty 7. The gloss is hedged because I have no parallel for the word.
4. Sz. Á. versus Sz. A.: kept disclosed in uncertainty 7 and the report, with the Árpád link marked as a hypothesis only.

The reviewer's remark on Slovak `poslal` is also noted under the Slovak translation.
