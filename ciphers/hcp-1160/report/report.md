# HCP 1160 (cpc_1915-11-11_HU_Mezokovesd_HU_Szomolya_szomolya-05): a suitor's verse in digit cipher on a Hungarian postcard

Human solver: Tomáš Pavuk

**Status: all 351 cipher signs are deciphered (349 by the key as written, 2 partly by word sense); independent review 1 verdict REVISE, findings addressed, sense of the message unchanged.** One short word cancelled by the writer is not read. Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1160 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1160), portal name cpc_1915-11-11_HU_Mezokovesd_HU_Szomolya_szomolya-05, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), which was not consulted, so it is not known whether it discusses this card.

It is a picture postcard of a young couple holding roses, sent in wartime, dated by the writer 1915. XI/11. (11 November 1915) and signed Sz. A. The file name gives Mezőkövesd as the place of sending; the postmark ring shows KÖVES, but its date could not be fixed. The open address reads: **Szépreménnyü / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács. / Borsod m.** ("To the promising young lady Margitka Sziber, Szomolya, post office Bogács, Borsod county"). The language is Hungarian.

Almost the whole message side is enciphered in ink. One note at the foot and the words "Mindnyájatokat csókollak" are open. A separate enciphered note in violet pencil stands across the top of the address half, set off by a ruled line, and runs on to the card edge above the stamp. The picture side has no writing.

The card belongs to a family of postcards to Margitka Sziber in the same cipher (hcp-1135 to 1179), several of them already deciphered in this repository.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual: Claude Opus 5.5 read every row from enlarged crops of the un-converted original scan, then enlarged each doubtful sign. There was no earlier work on this number. The key was carried over from the finished sister cards hcp-1174, 1178 and 1179 and the cards hcp-1170 and 1172, and it gave Hungarian at once. The few signs missing from those tables were fixed from words on this card. It is therefore a transferred key with small extensions, not a fresh key recovery.

A script (work/decode.py) checks the hashes of the scans, decodes the transcription with the table and compares each row with the stated reading. Run from the repository root:

```text
python3 -I ciphers/hcp-1160/work/decode.py
```

The reviewer retyped the ciphertext from its own crops and rebuilt the key separately (review/work/decode_review.py). After the corrections described below, its 351 signs agree with the solver's everywhere, apart from how the two doubtful signs are labelled.

## Key

Monoalphabetic substitution: one sign per Hungarian letter, a digit alone or a digit plus a mark, with no word division. The signs do not separate o/ó, i/í or u/ú. All 32 signs occur on this card.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| 0 | o, ó | 3 | d | 6. | ny |
| 0, | ö, ő | 3, | r | 7 | k |
| 1 | i, í | 3. | v | 7, | s |
| 1. | a | 4 | f | 7. | sz |
| 1: | e | 4, | g | 8 | m |
| 1' (high dot) | á | 4. | gy | 8, | t |
| 1, | b | 5 | h | 8. | ty |
| :1 (two dots left) | ü | 5, | l | 9 | p |
| .1 (one dot left) | u, ú | 5. | ly | 9, | z |
| 2, | cs | 6 | j | 9. | zs |
| 2. | é | 6, | n | | |

For n, g, t and l the comma gives the plain letter and the dot the palatal. This came out of the words and was not assumed. Three signs occur once each here: 5. (melynek), 8. (hattyúdalom) and 9. (rózsáról). They agree with sister cards, for example FINAL hcp-1164 and hcp-1166 for ty. The one family disagreement is 5.: ly here and on hcp-1151, 1142 and 1164, but l on hcp-1178 and 1179, and l with ly open on hcp-1166. This card cannot settle that for the family.

## Plaintext

Ciphertext as transcribed; | separates the words as printed (the card has no word division). `~` marks the two doubtful signs. Labels: L = prose, P = verse, F = cipher at the foot, V = violet note.

```text
L1 7 1: 3 3. 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8
L2 1. | 5, 1. 9 0 3 1. 8, | 8 1: 4, 7 1. 9 8, 1. 8 |
   8 1: 5. 6, 1: 7 | 6, 1. 4. 0 6, |
   8 1: 4, 0, 3, :1 5, 8, 1: 8
L3 7 1: 3 3. 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8 |
   8, .1 3 5 1. 8, 0 3 | 5 0 4. | 5 1. | 2, 1. 7 |
   5, 1: 5 1: 8, | 4 1: 5, | 8 1: 4. 1: 7 | 3 1: | 5 1. |
   6, 1. 4. 0 6, | 3, 0 7. | :1~ 3 0, | 5, 1: 7. |
   6, 1: 8 | 8 1: 5 1: 8, 1: 7
P1 1: 5, 5 1: 3, 3. 1. 3 0 7 | 9 0 3, 1, 1. |
   5 .1 5, 5, 0 7 | 8 1 6, 8, | 3, 0 9. 1' 3, 0 5, |
   1. | 7. 1 3, 0 8
P2 6, 1: 8 | 1: 6 8, | 7 0, 6, 6~ 1: 8, | 7, 1: 6, 7 1 |
   2. 3, 8, 1: 8 | 9 .1 7. 8, 1' 6, | 1' 5, 5, |
   8 1. 6 3 | 1. | 7, 1 3, 0 8
P3 1. 9, | 1: 3, 3 1: 1 | 7 1 7, | 3 1. 5, 0 7, 0 7 |
   9, 1: 6, 4, 1 7 | 1: 5, | 5 1. 8, 8. .1 3 1. 5, 0 8
P4 1: 4. | 1, 0 5 0 | 7. 1: 4, 2. 6. | 4 1 .1 3. 1. 5, |
   7 1: 3. 1: 7, 1: 1, 1, | 5, 1: 7. | 8 0 6, 3 5 1. 8, 0 8
F1 1, 0 2, 1' 7, | 8 1: 4,
F2 7. 1' 8 8, 1. 5, 1. 6, 7. 0 3, | 2, 0 7 0 5, 5, 1. 7
V1 1. | 4 2. 6. 7 2. 9 | 7 2. 7. 1: 3. 1. 6, |
   9 2. 6, 7. 8, | 7 :1 5, 4. 2. 5, | 5, 1: | 8 1. 6 3 |
   7 1 3. 1' 5, 8, 0 8 | 2. 7, | 4 1: 3. 1 7. 1: 8
```

Hungarian text. Square brackets mark the enciphered parts. Punctuation, capitals and word division in the cipher passages are editorial, and lengths on ó, í, ú are supplied. The writer's spelling is kept.

```text
[Kedves Margitkám]! [A lapodat megkaptam, melynek nagyon
megörültem. Kedves Margitkám, tudhatod hogy ha csak lehet
fel megyek, de ha nagyon rosz üdő lesz nem mehetek.]

I
[Elhervadok, porba hullok,
mint rózsáról a szirom,
nem ejt könnyet senki értem,
pusztán áll majd a sírom.]

II
[Az erdei kis dalosok
zengik el hattyúdalom ...
Egy bohó szegény fiúval
kevesebb lesz, mondhatom.]

ha esetleg rosz üdő lenne és nem mehetnék [bocsás meg] )
[számtalanszor csókollak] ) Mindnyájatokat csókollak.

1915. XI/11. Sz. A.

Violet pencil, top of the address half:
[a fénykép készevan, pénszt külgyél le, majd kiváltom
és feviszem]
```

Normal spellings: Szépreménnyü = Szépreményű, rosz = rossz, üdő = idő, bocsás = bocsáss, pénszt = pénzt, külgyél = küldjél, készevan = készen van, feviszem = felviszem. The two brackets ) are on the card and act as dividers.

**English translation**

Dear Margitka! I received your card, which made me very glad. Dear Margitka, you may know that if it is at all possible I will come up, but if the weather is very bad I cannot come.

I. I wither, I fall into the dust, like the petal from a rose; no one sheds a tear for me, my grave will stand desolate.

II. The little songsters of the forest sing my swan song out... With one foolish poor boy there will be fewer, I can say.

If the weather should perhaps be bad and I could not come, forgive me. Countless times I kiss you. I kiss you all. 11 November 1915. Sz. A.

Top note: The photograph is ready; send down money, then I will redeem it and bring it up.

**Slovak translation**

Milá Margitka! Tvoj lístok som dostal a veľmi ma potešil. Milá Margitka, vieš, že ak to len bude možné, prídem hore, ale ak bude veľmi zlé počasie, nemôžem prísť.

I. Vädnem, padám do prachu ako lupeň z ruže; nikto za mnou nevyroní slzu, môj hrob bude stáť opustený.

II. Malí speváci lesa dospievajú moju labutiu pieseň... O jedného bláznivého chudobného chlapca bude menej, môžem povedať.

Ak by azda bolo zlé počasie a nemohol by som prísť, odpusť mi. Nespočetnekrát ťa bozkávam. Bozkávam vás všetkých. 11. novembra 1915. Sz. A.

Poznámka hore: Fotografia je hotová; pošli dolu peniaze, potom ju vyplatím a prinesiem hore.

## What remains uncertain

- **üdő in the prose.** One dot stands free left of the stem. A bump on the stem sits where the second dot of :1 should fall, so the second dot is likely but not proven. The word stands open in the foot note.
- **könnyet.** The mark on the second 6 lies in an ink blot with the outline of a comma, so the literal reading leans to 6, and a spelling "könnet". The y is a word-sense restoration. The word is the same either way.
- **készevan.** The signs are clear and are printed as they stand. The sense "is ready" rests on "készen van" with the n omitted.
- **The cancelled word.** Before "a fénykép" the writer struck out about five signs, beginning 1. 5, with 3. as the fourth. It is not read and is not part of the message.
- **feviszem, pénszt, külgyél, hattyúdalom.** Spellings as written: no l in "fe(l)viszem", phonetic "pénszt" and "külgyél", and no accusative ending on "hattyúdalom", which verse allows.
- **Reading order.** The place of the violet note in the message is unknown. It is taken as a separate postscript.
- **The numerals.** I and II are small marks above the rows, taken as stanza numbers. The I could be a stray tick; the II is plain.
- **Postmark and verse source.** The postmark date could not be fixed; the date rests on the writer's own 1915. XI/11. The source of the verse was not searched. The HistoCrypt article was not consulted.

## Why the solution is believed correct

A key taken from other cards gives continuous Hungarian over the whole card with no forced words. The verse scans without help (8 and 7 syllables alternating over eight lines) and rhymes: szirom / sírom, hattyúdalom / mondhatom. The open foot note repeats the content of the cipher: "ha esetleg rosz üdő lenne és nem mehetnék" follows "ha nagyon rosz üdő lesz nem mehetek". The opening formula matches hcp-1151 and hcp-1142, and the photograph note fits hcp-1170.

## Review and what changed

An independent Claude Opus 5.5 reviewer tried to refute the reading, read every row from its own crops and decoded with its own script. Its verdict was **REVISE**. It could not refute the message, but it found two misread signs. All findings were addressed:

- **melynek:** the mark after the 5 is a round dot on the ruled line, not a comma. The first reading "melnek" became "melynek", which added 5. = ly to the table and to the palatal pattern.
- **kiváltom:** the dot on that 1 stands high, so the sign is 1' = á. The claim that the writer had slipped was withdrawn.
- **Sister cards:** values wrongly called new in the family now cite the cards that already have them, separating FINAL from unreviewed cards.
- **Counts and sense calls:** the card has 32 real signs. "fiúval" no longer counts as a sense call, "üdő" is now transcribed :1, and "könnyet" is stated as a restoration.
- **készevan:** now printed as the signs give it, not as "kész e van".
- **Cancelled word:** a possible 1: as third sign is recorded, and no reading is printed.

The solver also corrected the open address from "Szépreményű" to "Szépreménnyü" with a doubled n. The translations did not change in substance.

The reviewer could not verify the verse source, the postmark date or the HistoCrypt article, and some sister cards it cites are themselves not yet final.
