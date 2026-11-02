# HCP 1135 (cpc_1916-04-22_HU_Mezokovesd_HU_Szomolya_szomolya-30): Árpád's Easter card to Margitka Sziber, 1916

Human solver: Tomáš Pavuk

**Status: deciphered in full (301 of 301 cipher signs, 294 by the key as written, 7 by word sense); independent review 1 verdict ACCEPT, no word of the reading changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1135 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1135), portal name cpc_1916-04-22_HU_Mezokovesd_HU_Szomolya_szomolya-30, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was not checked for this card, so it cannot be said whether it discusses it.

The card was sent in wartime from Mezőkövesd to the village of Szomolya in north-east Hungary. It is dated in clear at the foot: Mezőkövesd. 1916. IV/22. That is Holy Saturday, the day before Easter Sunday (23 April 1916). The postmark shows MEZŐ... and 22; its month and year are not legible. The picture side is an Easter scene, a couple with eggs and catkins, and carries no cipher text.

The address is in clear: Őnsg. / Szépreményű Sziber Margitka Kisasszonynak / Szomolya / u. p. (Bogács), "To the promising young lady Margitka Sziber, Szomolya, post office Bogács". Őnsg. is an abbreviated title, read as written.

The card belongs to the same correspondence as hcp-1174, 1178 and 1179 in this repository, on which a digit cipher was reconstructed. Those cards have only key words in digits inside open Hungarian. This one enciphers almost the whole message, with word spaces mostly kept. Only the first word of each verse line, a few single letters, the date and the address stand in clear. The sender signs as Árpád, as on hcp-1174.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, sign by sign, from the un-converted high-resolution scan (3468 by 2298 pixels) enlarged 3 to 5 times. No OCR was used, and the portal supplied no transcription.

The key was transferred from hcp-1174, 1178 and 1179, not recovered from nothing. The first line of this card is the salutation of hcp-1174, Édes Margitkám. All signs known from those cards were applied unchanged. Four signs are new on this card and came from the words around them: `.1` (u) from húsvét, `4.` (gy) from hogy and vágyik, `6` (j) from majd and jobbat, `6.` (ny) from szárnyán and lánykám.

The decoding can be reproduced from the repository root:

```sh
python3 -I ciphers/hcp-1135/work/decode.py
```

The script checks the hashes of the four scans, decodes every sign of work/transcription.txt, asserts each decoded line against the stated reading, and prints the sign counts and the date of Easter 1916 by the computus. It does not read the image. The accents and the seven readings by sense come from the transcription and the reading list, not from the key.

## Key

Monoalphabetic substitution (MASC). Each letter is a digit with an optional mark, and the mark is part of the sign. cs, sz, gy and ny have one sign each. The key has 29 distinct signs and does not separate short and long o, u and i, or ö from ő, or ü from ű.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o, ó | `2.` | é | `6,` | n |
| `0,` | ö, ő | `3` | d | `6` | j (new) |
| `1` | i, í | `3,` | r | `6.` | ny (new) |
| `1.` | a | `3.` | v | `7` | k |
| `1:` | e | `4,` | g | `7,` | s |
| `1'` (high dot) | á | `4.` | gy (new) | `7.` | sz |
| `1,` | b | `5` | h | `8` | m |
| `:1` (dots left) | ü, ű | `5,` | l | `8,` | t |
| `.1` (one dot left) | u, ú (new) | `5.` | l | `9` | p |
| `2,` | cs | | | `9,` | z |

## Plaintext

Transcription as signs. Words are separated by a bar, =X marks a letter or word in clear, and SIGN~letter is a sign read by sense.

```text
2. 3 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8
7 1 3. 1' 6, 0 8 | 1~a | 5, 1: 4, | 1, 0 5, 3 0 4, 1. 1, 1, | 5 .1 7, 3. 2. 8, 1
:1 6, 1: 9 1: 7 1: 8, | 6, 1: 7 1: 3 | 1~a | 5, 1: 4, | 8, 1 7. 8, 1' 1, 1,
7. 1 3. 1, 0, 5, | 1. 9, | 1 4, 1. 9, | 5 0 4. | 1: 9, | 6, 1: 8 | 3. 1. 5, 1. 8 1
1, 0 5, 3 0 4, | 5 .1 7, 3. 2. 8, | 6, 0 | 3 1: | 8 1. 6 3 | 1. 3 | 8 2. 4,
1. 9, | 1 7, 8, 1: 6, | 6 0 1, 1, 1. 8, | 1 7,
=Te | 8, 1: 7, 8, 8, 2. | 3. 1' 5, 8, | 8, :1 6, 3 2. 3, 3, 1: 4, 1:
=Te | =b 1' 6.~j 6.~j 1' | 5, 1: 8, 8, | 3. 1 3, 1' =g
=U 8, 1' 6, 1. 3 | 3. 1' 4. 1 7 | 2, 1. 7 | 7. 1 3. 1: 8
=Be 2, .1~ü 5, | 7. 1: 3, 1: 8, | 1 8 1' 3
=A | 7. 1: 3, 1: 5, 1: 8 | 7. 1' 3, 6. 1' 6, | 7 :1 5, 3 0, 8
=Te | 5 0 9, 9, 1' 3 | 1. | 5, 1: 5, 7 1: =m
=Fogadd | 5, 1' 6. 7 1' =m | 7.~sz 1: 3, 1: 5, 1: 8 8 1: =l
=S | 7 :1 5, 3 | 5 1: 5. 1: 8, 8, 1: | 5, 1: 5, 7 1: =d
7, 0 3, 1. 1 8 1. 8, | 9, 1' 3, 3. 1. | :1 3 3. 0, 9, 0~ö 5, | 2. 7, | 7, 0 7 7. 0 3,
2, 0 7 0 5, | 5 :1 | 7 1: 3 3. 1: 7, 1: 3 | 1' 3, 9 1' 3
```

The prose rows above are rewrapped for the page. The verse rows follow the card.

**Hungarian.** Spelling as on the card. The punctuation is editorial, because commas on the card belong to signs; only the exclamation mark, the closing bracket after "is", the brackets around Árpád, the point after lelked and the date are written.

**Édes Margitkám!**

**Kívánom a leg boldogabb húsvéti ünepeket neked a leg tisztább szívből, az igaz hogy ez nem valami boldog húsvét, no de majd ad még az isten jobbat is)**

**Te testté vált tündérrege, / Te bájjá lett virág, / Utánad vágyik csak szívem, / Becsül, szeret, imád.**

**A szerelem szárnyán küldöm / Te hozzád a lelkem, / Fogadd lánykám szerelemmel / S küld helette lelked.**

**Soraimat zárva üdvözöl és sokszor csókol hű kedvesed (Árpád)**

**Mezőkövesd. 1916. IV/22.**

Normal forms: ünepeket = ünnepeket, helette = helyette, küld = küldd, Te hozzád = tehozzád.

**English.** Sweet Margitka of mine! I wish you the happiest Easter holidays from the purest heart; true, this is not much of a happy Easter, but God will yet give a better one too)

You fairy tale become flesh, / you flower become charm, / my heart longs only for you, / it esteems, loves, adores.

On the wings of love I send / my soul to you; / accept it, my girl, with love, / and send your soul in its place.

Closing my lines, your faithful sweetheart greets you and kisses you many times (Árpád)

Mezőkövesd, 22 April 1916.

**Slovak.** Moja sladká Margitka! Želám ti najšťastnejšie veľkonočné sviatky z najčistejšieho srdca; pravda, toto nie je bohvieaká šťastná Veľká noc, ale Boh ešte dá aj lepšiu)

Ty rozprávka, čo sa stala telom, / ty kvet, čo sa stal pôvabom, / len za tebou túži moje srdce, / váži si ťa, miluje, zbožňuje.

Na krídlach lásky posielam / k tebe svoju dušu; / prijmi ju, dievčatko moje, s láskou / a pošli namiesto nej svoju dušu.

Na záver mojich riadkov ťa pozdravuje a mnohokrát bozkáva tvoj verný milý (Árpád)

Mezőkövesd, 22. apríla 1916.

## Why the reading is believed

- A key built on other cards turns 294 of 301 signs as written into continuous Hungarian of the period, with normal period spellings.
- The verse is parallel (testté / bájjá) and rhymes: virág / imád, lelkem / lelked.
- The date gives an outside check. The card is dated the day before Easter 1916 and wishes a happy Easter, the picture is an Easter scene, and "nem valami boldog húsvét" fits wartime.
- Sender, salutation, addressee and closing match hcp-1174.

## Uncertainties

Seven signs are read by word sense. The key as written gives something else, or the sign is damaged:

- **a before leg, twice.** Both are a plain `1` with no dot, so the key gives i. "a lelkem" on the same card has a clear `1.`.
- **Becsül.** One low blot stands left of the 1, so literally `.1` = u. It may be `:1` with the dots merged; the left flag of that 1 is heavy where the upper dot would sit. "becsul" is not a word.
- **üdvözöl, second ö.** The line is cramped against the margin. The 0 has no comma of its own, because the comma of the 9 runs under it.
- **szerelemmel, first sign.** Transcribed `7.`, but no detached dot stands under it. The end of the crossbar curls into a blob, probably the dot tied in by the pen.
- **bájjá, twice.** Both are a clear `6.`, which is ny elsewhere on the card. Plain `6` is j in majd and jobbat. "Te bájjá lett virág" is the only sense, so this is a homophone or a slip.

Other points:

- `.1` = u rests on one word, húsvét, written twice. The other three new signs stand in two words each.
- `5.` occurs once, in helette, and is plain l as in the family. It happens to stand where normal spelling has ly.
- The `5` of hozzád is closed at the bottom like a 6, but carries the detached top bar of this hand's 5.
- In zárva a blot lies on the dot of `3.`; plain `3` would give zárda (convent), which makes no sense here.
- Clear letters stand inside cipher words: b (bájjá), g (virág), m (lelkem, lánykám), d (lelked), l (szerelemmel). A comma-shaped tick follows the l and the g. It is either punctuation or the comma of the sign, in which case those two are badly formed `5,` and `4,`. Either way the letters are the same. They are not counted in the 301.
- The `)` after "is" has no opening bracket on the card, so the start of the aside is unknown; "az igaz" is the natural start.
- It is not known whether the verse is printed or the writer's own. A web search for the lines found nothing.
- The faint red marks at the right edge of the picture side are specks, not writing.
- The solver's and reviewer's sign lists agree, but the reviewer's was typed with the solver's in view and then checked on the pixels, so it is not a blind second transcription.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, wrote its own key table from hcp-1174, 1178 and 1179 and decoded all 301 signs with no unkeyed sign, checked every row of the scan at 1.2 to 2 times and every disputed sign at 3 to 6 times, and judged the Hungarian and both translations. It found no wrong word and no forced passage. Its six findings were minor, and all are reflected here:

- The claim of "no free choices" was narrowed. The decoder no longer chooses ny or j by looking at the expected reading; the two j of bájjá are now marked as readings by sense.
- The first sign of szerelemmel was added to the readings by sense.
- The tick after the clear l and g was reported.
- The punctuation is now stated to be editorial.
- `5.` is now given as plain l.
- The á of lánykám moved from a reading by sense to a table reading `1'`, because its dot matches the other `1'` of the card.

The count therefore changed from 296 + 5 to 294 + 7. No word of the reading changed.

Solver and reviewer: Claude Opus 5.5 (Anthropic). There was no earlier work on this number.

## Sources

- HC Portal record 1135, General, Description and Attachments tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1135 (source/metadata.md).
- Message side: https://api.hcportal.eu/media/3466/conversions/cpc_1916-04-22_HU_Mezokovesd_HU_Szomolya_szomolya-30_adr-large.jpg (source/address-large.jpg), and the un-converted original in work/hires/.
- Picture side: https://api.hcportal.eu/media/3465/conversions/cpc_1916-04-22_HU_Mezokovesd_HU_Szomolya_szomolya-30_pic-large.jpg (source/picture-large.jpg), and the un-converted original in work/hires/.
- Family key: ciphers/hcp-1174, ciphers/hcp-1178 and ciphers/hcp-1179 in this repository.
