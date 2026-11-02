# HCP 1165 (cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-42): a report from the road and a verse for Margitka

Human solver: Tomáš Pavuk

**Status: deciphered in full (276 of 276 cipher signs, 268 by the key as written, 8 by word sense); independent review 1 verdict REVISE, findings addressed, reading kept with small corrections.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1165 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1165), portal name cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-42, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was **not checked** for this card. The whole reading here was made from the card, with the key taken from sister cards in this repository.

The card is addressed in clear to **Őnsg. Szépreményű Sziber Margitka kisasszonynak, Szomolya, u. p. (Borsod megye), u. p. Bogács**, "To the promising young lady Margitka Sziber". Part of the place name of the Mezőkövesd postmark can be read (ZŐK). Its date cannot, so the year 1915 rests on the portal file name alone. The picture side has no writing, only the portal stamp.

The card belongs to the Mezőkövesd correspondence (hcp-1135 to 1179), in which a suitor writes to Margitka in Szomolya in Hungarian, often enciphering only the tender words. Here he goes further: the heading and the whole letter are enciphered, while the verses and the closing are in clear with key words in digits. He signs Árpád, as on hcp-1174, and greets ángyika and Mariska, who also occur on hcp-1178.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, from the un-converted high-resolution scan (work/hires/) enlarged 3 to 5 times. No OCR was used. The key was not recovered from this card: the digit-plus-mark table of the finished cards hcp-1174, 1178 and 1179 was applied, and each sign was read from the pixels. A digit with a comma, dot, colon or high dot is one sign, and the mark is part of it. Word spaces are mostly kept. Dashes at the ends of the cipher lines fill the space. Parentheses are punctuation.

The signs missing from the hcp-1174 table (`4.` gy, `6` j, `6.` ny, `.1` u) are attested on sister cards such as hcp-1137, 1144 and 1153, and this card confirms them with clean words: hogy, nagyon, jó, jönni, jöttem, nyitva, fiú, utolért.

The decoding can be reproduced from the repository root with `python3 -I ciphers/hcp-1165/work/decode.py`. It checks the scan hashes, decodes every sign, asserts each word against the stated reading and prints the text. The clear text is hard-coded there, so the command tests the cipher part only.

## Key

Monoalphabetic substitution, register label MASC. Unmarked accents are normal: `0` covers o and ó, `0,` ö and ő, `1` i and í.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| 0 | o, ó | 3 | d | 6 | j |
| 0, | ö, ő | 3, | r | 6, | n |
| 1 | i, í | 3. | v | 6. | ny |
| 1, | b | 4 | f | 7 | k |
| 1. | a | 4, | g | 7, | s |
| 1: | e | 4. | gy | 7. | sz |
| 1' (high dot) | á | 5 | h | 8 | m |
| .1 (one dot left) | u, ú | 5, | l | 8, | t |
| :1 (two dots left) | ü, ű | 2, | cs | 9 | p |
| 2. | é | | | 9, | z |

## Ciphertext

All 276 signs, grouped by passage (heading, letter, then the enciphered words of the verses and closing). A bar separates the words. Marks are as seen on the card, with the two commas that touch other ink included. The `g` is the letter-like sign of `igaz`.

```text
2. 3 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8
2. 3, 8, 1: 7, 1 8, 5, 1: 7 | 5 0 4. | 7. 1: 3, 1: 6, 2, 2. 7, 1: 6, |
5 1. 9, 1. 2. 3, 8, 1: 8 | 6, 1. 4. 0 6,
6 0 | 1 3 0, | 3. 0 5, 8, | 7. 1 6, 8, 1: | 9 1. 7, 7. 1 0 | 3. 0 5, 8, |
6 0, 6, 6, 1 | 5 2. 8, | 0 3, 1' 3, 1.
2. 3, 8, 1: 8 | 1 | 3. 1' 3, 0 7, 1, 1. | 8 1: 3, 8, | 5 1. 7, 7, 1. 6, |
6 0, 8, 8, 1: 8 | 1 | 7. 1. 5, 0 7 1
4 1 .1 | 1 7, | .1 8, 0 5, 2. 3, 8, | 1 | 7. 0, 5, 5, 0, 7 | 7 0, 9, 8, | 8 1 3, 1: |
1. 9, | :1 9 5, 1: 8 5 1. 9,
2. 3, 8, :1 6, 7 | 8 1' 3, | 6. 1 8, 3. 1. | 3. 0 5, 8, | 3 1:
6, 1: 8 | 7. 0 5, 8, | 7, 1: 8 1 8, | 1. 9, | 0, 3, 1: 4, | 5, .1 1, 1
1 :1 1, 1' 6 8, 0 5, | 3. 0 6, 9, 3. 1.
7 1: 9, 1: 3 1: 8,
7. 1 3. 1, 1: 6, | 7. 1: 3, 1: 5, 1: 8
7, 0 7 7. 0 3, | 2, 0 7 0 5, 3. 1.
5 :1 | 1 8 1' 3 0 3 | 1 g 1. 9,
1 3. | 7 1: 3 3. 1: 7, 1: 3 | 1' 3, 9 1' 3
```

## Plaintext

Square brackets mark what is enciphered on the card. The spelling is the writer's.

```text
[Édes Margitkám]!

[értesítlek hogy szerencsésen hazaértem nagyon jó idő volt
szinte passzió volt jönni hét órára értem a városba mert
lassan jöttem a szalóki fiú is utolért a szőllők közt mire
az üzletház értünk már nyitva volt de nem szólt semit az
öreg Lubi]

Más különös ujság nincs.

Kicsiny kezed körül csapongva
Egy tarka pille röppen,
Mintegy [bűbájtól vonzva] vonva
Mind szűkebb körökben
Míg végül össze vonva szárnyait
Pihenni száll a kézre
Fehér [kezedet], a parányit
Ő liliomnak nézte.

Ha a szőlő nedvtül árad,
A fecske is ott terem,
Mikor a szem könnybe lábad
Héba [szívben szerelem].

Üdvözölve és [sokszor csókolva] maradok [hű imádód] és
[igaz] sz[ív]ű [kedvesed] ([Árpád])
csókolom angyikát és Mariskát is
```

Normal spellings: semit = semmit, üzletház = üzletházhoz (the card has no ending), szőllők = szőlők, nedvtül = nedvtől, Héba = hiába.

## English translation

Sweet Margitka! I let you know that I got home safely. The weather was very good, it was almost a pleasure to travel. I reached the town by seven o'clock, because I went slowly; the Szalóki boy (or: the boy from Szalók) also caught up with me among the vineyards. By the time we reached the shop building it was already open, but old Lubi said nothing. There is no other special news.

Around your tiny hand, fluttering, / a bright butterfly takes wing, / as though drawn, pulled by a spell, / in ever narrower circles, / until, folding its wings together, / it settles on the hand to rest: / your white hand, the tiny thing, / it took for a lily.

When the grape swells with juice, / the swallow too appears there; / when the eye fills with tears, / in vain the love in the heart.

Greeting you and kissing you many times, I remain your faithful adorer and true-hearted sweetheart (Árpád). I kiss ángyika (sister-in-law or aunt by marriage) and Mariska too.

## Slovak translation

Moja sladká Margitka! Oznamujem ti, že som šťastne došiel domov. Bolo veľmi pekné počasie, cesta bola takmer potešením. O siedmej som bol v meste, lebo som išiel pomaly; medzi viničami ma dostihol aj chlapec Szalókiovcov (alebo: chlapec zo Szalóku). Kým sme došli k obchodnému domu, už bolo otvorené, ale starý Lubi nič nepovedal. Iná zvláštna novinka nie je.

Okolo tvojej drobnej ruky poletujúc / vzlietne pestrý motýľ, / akoby čarom priťahovaný, ťahaný, / v čoraz užších kruhoch, / až napokon, zložiac krídla, / sadne si na ruku odpočinúť: / tvoju bielu ruku, tú drobnú, / pokladal za ľaliu.

Keď sa hrozno naleje šťavou, / aj lastovička je hneď tam; / keď sa oko zaleje slzami, / márna je láska v srdci.

Pozdravujúc ťa a mnohokrát bozkávajúc ostávam tvoj verný ctiteľ a tvoj milý verného srdca (Árpád). Bozkávam aj ángyiku a Marišku.

## What remains uncertain

Eight signs are read by word sense, because the table alone gives another letter or a mark is missing:

- The article `a`, three times (a városba, a szalóki, a szőllők), is a plain `1` with no dot; the table gives i. Elsewhere `1.` is used for a.
- `lassan` begins with a plain 5 and no comma; the table gives h, and `hassan` is no word.
- `üzletház` has a 9 with no comma (table p) and an 8 with a hook below in place of the comma (table m). That is two signs.
- `bűbájtól` starts with a 1 whose comma stands further right than usual. The verse needs a b here, and no other word fits.
- `igaz` has a written letter g, not the sign `4,`: a clear letter or a lapse.

Two more signs are counted by the table but touch other ink: the comma of `8,` in `szólt` runs into a stroke of the line below, and the comma of `7,` in `kedvesed` crosses the ruled line. Neither changes the reading.

Other points:

- **Lubi** is a name or nickname reported literally. Lúbi is equally possible, since accents go unmarked. It is not known who this is.
- **szalóki** may be a surname or a place adjective; the translations give both.
- **Héba** is in clear and is taken as a variant or slip for hiába on sense alone. It is the softest word of the verses.
- **Más** is blotted and its accent is lost. The pixels show `Mois`, which is this writer's form of Más: his a looks like `oi` throughout.
- **angyikát** has no visible accent. The translations supply ángyika; a personal name Angyika is not excluded.
- **üzletház** has no ending, and none is supplied. The last two signs stand partly under the postmark ring and a blot, but are legible.
- A faint pencil `)` in the fourth row of the letter has no partner and looks like a stray mark.
- The postmark date is unread, and the source of the verses was not found. No search was made beyond the sister cards.

## Review and what changed

An independent reviewer, a separate Claude Opus 5.5 agent, re-ran the command, made its own row-by-row transcription and its own decoder (review/work/verify.py), and viewed every doubtful sign at 5× enlargement. It reached the same 276 signs, the same key and the same connected Hungarian, and judged the text real Hungarian of the period, with no published solution used. Verdict REVISE, with five findings:

1. **Major:** one dot and two dots to the left are distinct signs, u/ú and ü/ű, and the first version had merged them. The name changed from Lübi to **Lubi**, and the check script no longer folds u into ü.
2. `áradt` corrected to **árad**: one stem only, and an exact rhyme with `lábad`. The translation is unchanged.
3. `Önsg.` corrected to **Őnsg.** in the address.
4. Two commas first called unseen were found in `szólt` and `kedvesed`, so the signs read by sense dropped from 10 to 8.
5. Wording: an unfounded remark that the writer walked was removed, one Slovak phrase was corrected, and the supplied form ángyika was noted.

The solver checked each finding on the crops and on its own new crops, and accepted all five. It also dropped the question mark on `Más`. The rest of the reading did not change. The reviewer upheld the other disclosed sense readings and found no unread clause, enciphered or clear.
