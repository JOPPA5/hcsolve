# HCP 1152 (cpc_1915-12-05_HU_Mezokovesd_HU_Szomolya_szomolya-09): a lover's complaint in digits on a Hungarian postcard

Human solver: Tomáš Pavuk

**Status: all 118 cipher signs are deciphered (114 by the key as written, 4 by word sense, one of those a restoration under an ink blot); independent review 1 verdict REVISE, findings addressed, cipher reading unchanged.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1152 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1152), portal name cpc_1915-12-05_HU_Mezokovesd_HU_Szomolya_szomolya-09, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was **not checked** for this card, so it is not known whether it treats it. No published solution of this card was found in the repository.

The card was sent in wartime Hungary to the village of Szomolya; the portal's file name gives Mezőkövesd as its origin. It is addressed in clear to "Tek. Szépreménnyü Sziber Margitka kisasszonynak, Szomolya, u. p. Bogács", "To the promising young lady Margitka Sziber, Szomolya, post office Bogács". A pencil note at the foot reads 1915 XII 5, which agrees with the portal's file name. The postmark on the two stamps could not be read as a date.

The message side starts with eight lines of digits with small marks. The sentence then continues in clear in the middle of a line, is signed Sz. A., and is followed by three stanzas of a love poem and a closing line, all in clear. The picture side is a portrait with no writing. The card belongs to the group of Mezőkövesd cards to Margitka Sziber (hcp-1135 to 1179 on the portal). The cipher key was first reconstructed on hcp-1174; the same signature stands on hcp-1175, 1176 and 1179.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The key was **transferred, not rebuilt**, from finished cards of the family (hcp-1174, 1165, 1168, 1170). No value was created for this card. The transcription is manual, from the un-converted high-resolution scan enlarged 2 to 8 times; no OCR was used. A digit and its mark count as one sign, so `3` and `3,` are different letters.

Two rare signs first looked like stray marks: a dot and a dash to the left of a 1. The first stands for u on hcp-1168 and the second for ú on hcp-1170, each with thin support there. They give `ugyan` and `úgyis` at the expected places. An early reading of line 5, `irnel`, was corrected to `írjál` on enlargement.

The decoding can be reproduced from the repository root:

```sh
python3 -I ciphers/hcp-1152/work/decode.py
```

The script checks the SHA-256 of all four scans, decodes every sign, asserts that each decoded word matches the stated reading, and prints the full text. It reports 118 signs, 114 by the table and 4 by sense. The open text is hard-coded in the script, so the command tests the cipher part only.

## Key

Monoalphabetic substitution (MASC), one sign per letter or per digraph (cs, sz, gy). Word spaces are mostly kept. Only the signs on this card are listed.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o | `2.` | é | `6,` | n |
| `1` | i, í | `3` | d | `7` | k |
| `1.` | a | `3,` | r | `7,` | s |
| `1:` | e | `3.` | v | `7.` | sz |
| `1'` (high dot) | á | `4,` | g | `8` | m |
| `.1` (dot on the left) | u | `4.` | gy | `8,` | t |
| `-1` (dash on the left) | ú | `5` | h | `9` | p |
| `2,` | cs | `5,` | l | `6` | j |

## Plaintext

Ciphertext as read, by card line. `4x` is the odd first sign, `[blot]` the ink blot.

```text
1  4x 1: 3 3. 1: 7,  8 1. 4, 1 8, 7 1' 8 !
2  8 1  3. 1. 6,  3. 1: 5, 1: 3  5 0 4.  6, 1: 8
3  1 3, 7.  5 1 7  8, 1. 5, 1' 6,  2, 1. 7  6, 1: 8
4  5 1. 3, 1. 4, 7 0 5,  2, 1. 7  .1 4. 1. 6,  1 3, -
5  6 1' 5,  7 1: 3 3. 1: 7,  7 2. 3, 5, 1: 7
6  7. 2. 9 1: 6,  6, 1:  7 0 8 [blot] 3, 1 2, 3  1.  7. 1 -
7  3. 1: 8 1: 8,  2. 6,  -1 4. 1 7,  1 3, 0 7
8  8 1 6, 3 1 4,  (then clear text)
```

Hungarian text. Square brackets mark what is enciphered on the card; the punctuation inside them is editorial, because the card has none there.

**[Kedves Magitkám]!**

**[Mi van veled, hogy nem írsz? Hisz talán csak nem haragszol csak ugyan, írjál kedves, kérlek szépen, ne komorícsd a szívemet, én úgyis irok mindig] még többet ez után, mert mostanába nem érkeztem. Sz. A.**

```text
Emészt a vágy napról napra,
Mint sorvasztó-kór betegét;
Csókot hintani ajakadra,
Szívni édes leheletét.

II
Emészt a vágy... sivó, kopár,
Tikkadt mező a kebelem,
Perzsel a hő, a napsugár,
Égő vágyam: a szerelem.

III
S te szép leányka kaczagsz tán
Amig én érted epedek...
Oh, kaczagj, csak nem neked fáj
Hogyha én érted szenvedek!

mindnyájatokat csókollak.
```

English translation: **Dear Margitka! What is the matter with you, that you do not write? Surely you are not really angry, are you? Write, dear, I beg you, do not darken my heart; I will write anyway, always, and more from now on, because lately I have not had the time. Sz. A.**

Longing consumes me day by day, / as a wasting disease consumes its patient; / to scatter kisses on your lips, / to breathe in your sweet breath.

II. Longing consumes me... barren, bare, / a parched field is my breast; / the heat scorches, the sunshine; / my burning longing: love.

III. And you, pretty girl, are perhaps laughing / while I pine for you... / Oh, laugh, it is not you who hurts / when I suffer for you!

I kiss you all.

Slovak translation: **Milá Margitka! Čo je s tebou, že nepíšeš? Veď sa azda naozaj nehneváš? Píš, milá, prosím ťa pekne, nezatemňuj mi srdce; ja aj tak píšem stále, a odteraz ešte viac, lebo v poslednom čase som nemal čas. Sz. A.**

Túžba ma stravuje deň čo deň, / ako zhubná choroba svojho chorého; / sypať bozky na tvoje pery, / vdychovať tvoj sladký dych.

II. Túžba ma stravuje... pustá, holá, / vyprahnutá lúka je moja hruď; / páli horúčava, slnečný lúč; / moja horúca túžba: láska.

III. A ty, pekné dievča, sa azda smeješ, / kým ja za tebou prahnem... / Ó, smej sa, veď to nebolí teba, / keď ja pre teba trpím!

Bozkávam vás všetkých.

## Uncertainties

Four cipher signs do not decode as written:

- **Kedves, first sign.** An odd closed form with a crossbar and a dark spot in the loop, not a clean 7. As a 4 it would give `fedves`. The word is written cleanly in line 5.
- **hisz and haragszol.** Each has a crossed 7 with no dot, so the table gives `hik` and `haragkol`. Sense wants `7.`. Hcp-1174 has the same missing dot in `szerető`. The division `hisz talán` rests on this reading.
- **komorícsd, the o.** This is a **restoration**. A solid ink blot stands where `0` should be, the same size and tilt as the `0` just before it, with no counter visible. It may be a correction. `komorít` (to make gloomy) is the only word found to fit `komo?rícsd` and `a szívemet`; cs for ts is a phonetic spelling of the imperative `komorítsd`. This word is less sure than the other three.

Other points of the cipher part:

- **Two marks in line 4.** The marks after `1` in `haragszol` (second sign) and `ugyan` (third sign) are elongated ticks, not round dots. Strictly they could be taken for `1,` = b, as on hcp-1168. They are read as `1.` by judgement and sense.
- **Magitkám.** The card has no `3,`. This is the writer's slip for Margitkám, printed as written.
- **írjál.** It is split across a line end with a hyphen at the margin. The `6` has no comma and the `1'` has one high dot, so it is not `írnel`.
- **irok, csak ugyan, ez után.** Spelled as on the card; the normal forms are írok, csakugyan, ezután.

Open text:

- **nem érkeztem.** Taken as "I had no time". This is an interpretation with no period source checked; the words themselves are clear.
- **hintani.** Printed as written, with no dot visible on the final i; the normal form is hinteni. The line has 9 syllables against 8 in the others. The metre expects the short hintni, but the pixels show the longer form.
- **leheletét.** An accent shows only on the last e, and the word is overwritten. The form is third person, "its/her breath", while ajakadra is "your lips". Both translations print "your", which normalises this; the rhyme with betegét may have forced the shift.
- **sorvasztó.** The script is cramped and partly crossed by a stroke from above; read with support from sense.
- **Tikkadt.** The capital looks like a barred T or F; `Fikkadt` is not a word.
- **sivó.** Printed as written, taken as "barren" (compare sivár). This meaning is not independently confirmed.
- **mindnyájatokat.** Pale, along the bottom edge; the accent on á is not certain. The same word stands on hcp-1157 and 1170.

Not established: the postmark date; whether the pencil note is the writer's own (its digits share his forms, which does not prove it); the identity of Sz. A.; whether the poem is printed elsewhere; and whether the HistoCrypt article treats this card.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, read all eight cipher lines sign by sign from its own crops before comparing, and decoded them with the raw key and no sense repair. Its 118 signs agreed with the solver's in every position; the only non-words were the disclosed odd signs and the blot. It also read the open text and address at 2.5x, confirmed the key values against hcp-1168, 1170 and 1174, and counted the metre.

Findings and what changed:

- **keblem (major).** The card has `kebelem`, which gives the stanza 8 syllables per line and a full rhyme with szerelem. Corrected. This is the only word of the text that changed, and the translations stay.
- **hintani and the metre.** The extra syllable is now disclosed; the reading stays.
- **Overclaim on komorícsd.** The restoration is now excepted from "certain".
- **Two tick-like marks in line 4.** Now disclosed.
- **leheletét translated as "your".** Now disclosed.
- **One loose citation.** Hcp-1169 has `mindnyájatoknak`, not `mindnyájatokat`. Corrected.

No cipher sign, key value or decoded cipher word changed, so a second review round was not needed. All work on this card, transcription, key transfer and decipherment, was done by Claude Opus 5.5; there was no earlier work on this number.

## Sources

- HC Portal record 1152, General, Description and Attachments tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1152 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/3517/cpc_1915-12-05_HU_Mezokovesd_HU_Szomolya_szomolya-09_adr.jpg and its large conversion (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/3516/cpc_1915-12-05_HU_Mezokovesd_HU_Szomolya_szomolya-09_pic.jpg and its large conversion (source/picture-large.jpg).
- Family key: ciphers/hcp-1174, 1165, 1168 and 1170 in this repository.
