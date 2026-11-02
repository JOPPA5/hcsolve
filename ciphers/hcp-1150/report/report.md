# HCP 1150 (cpc_1916-06-12_HU_Mezokovesd_HU_Szomolya_szomolya-40): a Whitsun love letter in digits

Human solver: Tomáš Pavuk

**Status: all 420 cipher signs are deciphered into continuous Hungarian (414 by the key as written, 6 by word sense); independent review 1 verdict REVISE, findings addressed, with word-level corrections only.** One name (Gerzon) remains a flagged reading. Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1150 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1150), portal name cpc_1916-06-12_HU_Mezokovesd_HU_Szomolya_szomolya-40, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber. No transcription or solution was attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166); it was not checked for this card. No published solution turned up.

The picture side shows forget-me-nots and carries no writing. On the address side the place and date are in clear: "Kisterenne, 1916 VI/..". So is the address: "Őnagyságn. Sziber Margitka Kisasszonynak, Szomolya, (Borsod m.), u. p. Bogács". The postmark reads KISTERENYE. The card was therefore sent from Kisterenye, although the portal file name says Mezőkövesd, where the sister cards come from.

The whole message is in digits: about 420 signs in 20 rows, running across the divider up to the stamp. Three pencil rules separate the prose, the first verse, the second verse and the closing.

The card belongs to the wartime correspondence of a suitor who signs (Árpád) with Margitka Sziber of Szomolya, in north-east Hungary. Hcp-1174, 1178 and 1179 in the same group were finished earlier, with a key built from their digit passages.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: forget-me-nots, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, from the un-converted high-resolution scan, enlarged 2 to 7 times. No OCR was used. The purple-pencil writing was separated from the postmark ink with a colour mask where the two cross.

The work started from the family key of hcp-1174, 1178 and 1179. `Drága Margitkám`, `értesítlek hogy` and `elutazom` confirmed it at once. Five values were added or taken over from the sister cards in words such as `hétfőn`, `éjjel`, `jobban`, `lányka` and `nefelejcs`. A letter is one digit plus an optional mark. There are no word divisions, and a Hungarian digraph has one sign. A large `)` stands after sentences in rows 8, 9 and 18 and is not a letter.

The decoding can be reproduced from the repository root with `python3 -I ciphers/hcp-1150/work/decode.py`. It checks the scan hashes, decodes every word from its signs, asserts that the result matches the stated word, and prints the text. The open place, date and address are hard-coded there.

## Key

Monoalphabetic substitution (MASC). Accents are only partly distinguished.

| sign | letter | sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | `1'` (high dot) | á | `4` | f | `6.` | ny |
| `0,` | ö, ő | `:1` (dots left) | ü, u, ú, ű | `4,` | g | `7` | k |
| `1` | i, í | `2,` | cs | `4.` | gy | `7,` | s |
| `1.` | a (also unmarked á) | `2.` | é | `5` | h | `7.` | sz |
| `1:` | e | `3` | d | `5,` | l | `8` | m |
| `1,` | b | `3,` | r | `6` | j | `8,` | t |
| `9` | p | `3.` | v | `6,` | n | `9,` | z |

Compared with hcp-1174, the new signs are `1,` b (already in the hcp-1179 table), `4` f (a value noted from hcp-1175 on hcp-1179), and `4.` gy, `6` j and `6.` ny. Each of `4`, `4.`, `6` and `6.` recurs in several unrelated words.

## Plaintext

Punctuation, capitals and verse lines are editorial. Spelling is as on the card: `inet` stands for `innét` and `fényeségre` for `fényességre`, both with a single consonant, as this writer often does. `Ez a virág tolmácsolom` is printed as written, although correct grammar would want another form.

Kisterenne, 1916 VI/..

Drága Margitkám!

értesítlek hogy inet hétfőn éjjel elutazom hazafelé. Az ünnepek itt nagyon lassan teltek, jobban szerettem volna veled tölteni, no de nem soká ott leszek. Egyéb újságot nem tudok írni. Gerzon hazajött hát hadi szabadságra. Majd szóval többet.

```text
Van egy kis szende virág,
úgy hívják hogy nefelejcs.
Ez a virág tolmácsolom lányka,
engem ne felejts!

Nem bámulok a fényeségre,
ragyognak bár a csillagok,
mert itt a földön reád nézve
egy szebb csillagot láthatok.
```

Soraimat zárva számtalanszor ölel, csókol és üdvözöl hű imádód (Árpád)

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

## What remains uncertain

Six signs do not follow the table and rest on word sense:

1. `Az`: the first sign shows a plain `1` under a postmark edge; a low dot may be hidden.
2. `ünnepek`: the first sign shows no dots to the left.
3. `nagyon`: the first 6 shows no comma, which by the table would be j. The head of the sign below may hide one, and the reviewer could not settle this.
4. `Egyéb`: the third sign lies under the black figure of the postmark date; `é` is a restoration from the word.
5. `szabadságra`: the second a is a plain `1`, with no dot seen.
6. `Soraimat`: the second a has the shape of `4.`, taken as a curled `1.`; `gy` gives nothing.

Several other signs are read through postmarks and are less firm, though they count as by the table. They are in `éjjel`, `hazafelé`, `jobban`, `írni`, `szabadságra`, `nefelejcs`, and the opening of `(Árpád)`.

Readings that depend on interpretation:

- **Gerzon** is the least firm word. It is taken as the given name Gerzson, with zs written as z, which is an inference. The first sign looks like `4,` g, but `1,` b (Berzon) cannot be fully excluded. Nothing outside the card confirms the name, and it is not known who he was.
- **hát** ("so, then") is chosen by sense, because `1.` also stands for an unmarked á. The alternative `hat` ("six") would need a missing unit such as `heti`.
- **Ez a virág tolmácsolom lányka** has unresolved syntax; the translation treats "I interpret it" as a parenthesis.
- **reád** and **veled**: the middle mark of `reád` is read as a high dot, and an extra dot in `veled` is taken as a stray.

The day of the date is not fully read. After `VI/` a further 1 and a round digit are visible at the stamp edge, which would fit the portal's 12 June. By calculation, not from a source, Pentecost 1916 fell on 11 June and 12 June was a Monday, Whit Monday. That fits "the holidays", but the text does not say which Monday night is meant. The postmark date was not fully read either. The two verses were not found in a published source, though the search was not wide, so copying errors in them would not show.

## Why the reading is believed correct

One table gives continuous Hungarian across the whole card, with 414 of 420 signs by the key, and most of the table comes from other cards. `nefelejcs` ("forget-me-not") agrees with the picture side, and `nefelejcs` / `felejts` and `csillagok` / `láthatok` rhyme. The formula `Soraimat zárva` and the signature (Árpád) recur in the same correspondence. The date fits a card about holidays just over.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-ran the command, built its own sign stream with the key taken from sister cards, and reread the card from the hires scan. It worked with the solver's text available, so this shows agreement, not independent discovery. The verdict was REVISE, with eight findings, all addressed:

- **`várva` became `zárva`.** The sign is `9,`, with a tail and a separate comma that the solver had missed. This also corrects the sense of the closing, from "awaiting my lines" to "closing my lines".
- **`[B]erzon` became `Gerzon`**, still flagged, with Berzon as the alternative.
- **`hat` became `hát`**, replacing the nonsense "on six military leave". The signs are the same.
- **`leszek`** is now by the table, because the comma is visible under the postmark ring.
- **`Soraimat`** is now disclosed as a sense reading, so the count moved from 413 + 7 to 414 + 6.
- Overclaims about rhyme and sources were corrected, the flower line was translated more faithfully, and the date note was improved.

The changes are limited to single words, so no second review round was needed.

The transcription, key extension and decipherment are by Claude Opus 5.5, with no earlier work on this number.
