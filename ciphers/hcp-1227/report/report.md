# HCP 1227 (cpc_-09-26_HU__HU_Jasz Arokszalas_jolanka-95): Feri to Jolánka Tóth, how to find him on the train

Human solver: Tomáš Pavuk

**Status: main text deciphered in full (24 rows); closing under the stamp read as the family formula with 8 signs restored. Independent review 1 verdict REVISE; all findings addressed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1227 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1227), portal name cpc_-09-26_HU__HU_Jasz Arokszalas_jolanka-95, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card turned up, and the AI Decipherment Register had no entry for it.

The address side is plain Hungarian: **Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás** ("To the promising young lady Jolánka Tóth, Jászárokszállás"). The message itself is on the same side, in green ink in invented signs: 24 rows, the last three running along the bottom edge under the address, and seven short lines hidden under where the stamp was. The cancels are a Rákospalota-Újpest station box and a circular date on which only the day 26 can be read. The month IX comes only from the portal file name; the year is not legible.

The picture side has only printed gold captions and no cipher: Szerelmi üzenet / Hozzád sietek angyalom! / Égek a vágytól, hogy viszontlássalak ("Love message / I hurry to you, my angel! / I burn with desire to see you again"). A further worn gold line at the right edge is probably print too; it could not be read.

The card belongs to the family of Hungarian cipher postcards to Jolánka Tóth, several of them signed Feri (for example HCP 1211, 1213, 1216). That this Feri is the same man is suggested by the name and the Rákospalota link, not proved.

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, printed captions only (source/picture-large.jpg)](../source/picture-large.jpg)

![Enlargement of the block under the stamp, with the torn patch at left and the printed green triangle over the signs (review/work/st.png)](../review/work/st.png)

## Method

The key was **transferred, not recovered**: it comes unchanged from the finished family cards HCP 1216, 1301 and 1243, whose earlier work is credited to OpenAI GPT-6 Astra / GPT-6.1 Sol and Claude Opus 5.5. This card itself had no earlier work; Claude Opus 5.5 transcribed it by hand, sign by sign, from enlarged crops of the un-converted original scan, using a green-minus-red ink map where the black cancels and grey portal stamp overlie the ink. Each written sign is one token in work/ledger.txt, and a script decodes the ledger. The difficult places were settled in this order: the shape first, the word sense only where two signs are close, and every such call is listed under Uncertainties.

## Key

Cipher type: **MASC + Steganography** (updated 2026-11-03). This is a simple monoalphabetic substitution with invented graphic signs, and its closing is hidden in the stamp box under the stamp (the stamp is now lifted). Digits stand as plain digits (as on HCP 1301). Dots over o and u give ö and ü.

| Sign | Plain | Sign | Plain |
|---|---|---|---|
| two bars | a | two short strokes | n |
| 6-shape | b | cursive loop | o |
| opposed bowls | cs | tall stroke + tick | h / p |
| long stroke + tick | d | F-shape | r |
| three bars | e | right bowl | s |
| cross | f | gamma | t |
| open loop with descender (4-like) | g | x-cross | u |
| dotted crossed curve | i | chevron | v |
| inverted T | j | low descender | y |
| section mark or S-curve | k | crossed diagonal | z |
| wave | l | three short strokes | m |

h and p share one near-homograph shape, so each call comes from the word. On this card u and z are also close.

## Plaintext

Literal decipherment. Square brackets mark restored signs, {|} a stray stroke without value.

```text
01 szeretettedesjolankam          13 amelikazonavonalon
02 becsessoraitmegkaptammit       14 vanénanyugatioldalon
03 nagyörömmelfogadok             15 vagyokesarrakeremhogy
04 eskoszönöksorainnem            16 anemdohanyzoszakasz
05 tudokeligazodnihogy            17 bautazzonhogyeset
06 szombatongyönevagy             18 legkonyenmmegtalal
07 28ánmerezketöén                19 jamesedesemmerfel
08 hatehetamszombaton             20 atulvasutasruhatol
09 varomvalaholdehogy             21 anyirahogylatniseakar
10 holaztennemtudummeg            22 benn{|}epedigazelsotalalkozasomabalesz
11 jegyzemaztishogyen             23 merthasikerüavonatontalkoznicsakis
12 nemazonarakosonvagyok          24 abbaleszek
stamp: isten / veleede / [s][e][m]abol / [d][o]gvi / s[z][o][n]t / latasig / feri
```

After vonaton in row 23 the writer goes on at a higher level (talkozni csakis), and abbaleszek is squeezed below it; the order comes from the sense, and the other order gives no text.

**Hungarian (normalized):** Szeretett édes Jolánkám! Becses sorait megkaptam, mit nagy örömmel fogadok és köszönök. Sorain nem tudok eligazodni, hogy szombaton jön-e vagy 28-án, mer[t] ez kettő. Én hát e héten szombaton várom valahol, de hogy hol, azt én nem tudom. Megjegyzem azt is, hogy én nem azon a Rákoson vagyok, amelyik azon a vonalon van, én a Nyugati oldalon vagyok, és arra kérem, hogy a nem dohányzó szakaszba utazzon, hogy esetleg könnyen megtaláljam. És édesem, mért fél a túl vasutas ruhától annyira, hogy látni se akar benne, pedig az első találkozásom abba[n] lesz, mert ha sikerü[l] a vonaton talá[l]kozni, csakis abba[n] leszek.

Under the stamp: Isten vele, éde[sem], a bol[do]g visz[on]tlátásig. Feri.

**English:** My beloved sweet Jolánka! I received your esteemed lines, which I welcome with great joy and for which I thank you. I cannot make out from your lines whether you are coming on Saturday or on the 28th, because these are two [different things]. So I will wait for you this week on Saturday somewhere, but where, that I do not know. I also note that I am not on the Rákos that lies on that line; I am on the Nyugati [Western station] side, and I ask you to travel in the non-smoking section, so that I may perhaps find you easily. And, my sweet, why do you fear the all-too-railwayman clothes so much that you do not even want to see [me] in them? Yet my first meeting [with you] will be in them, because if we manage to meet on the train, I will be in nothing but those.

Under the stamp: God be with you, my sweet, until the happy reunion. Feri.

**Slovak:** Moja milovaná, sladká Jolánka! Vaše vzácne riadky som dostal, čo s veľkou radosťou prijímam a ďakujem za ne. Z Vašich riadkov sa neviem vyznať, či prídete v sobotu alebo 28-ho, lebo to sú dve [rôzne veci]. Budem Vás teda čakať tento týždeň v sobotu niekde, ale kde, to neviem. Podotýkam tiež, že nie som na tom Rákosi, ktorý je na tej trati, som na strane Západnej stanice, a prosím Vás, aby ste cestovali v nefajčiarskom oddelení, aby som Vás prípadne ľahko našiel. A, drahá, prečo sa tak bojíte toho príliš železničiarskeho oblečenia, že ma v ňom ani nechcete vidieť? Veď moje prvé stretnutie [s Vami] bude práve v ňom, lebo ak sa nám podarí stretnúť sa vo vlaku, budem jedine v ňom.

Pod známkou: S Bohom, moja sladká, do šťastného zvidenia. Feri.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1227/work/decode.py
```

The script checks the SHA-256 of the four image files, decodes the ledger and prints the literal rows and the normalized text: 515 tokens, 8 of them restored.

## Uncertainties

- **Closing under the stamp, the largest point.** The stamp tore the paper there, and the black box and a printed green triangle overlie the ink. Visible: S3 ends a b o l, S4 ends g v i. The signs s, e, m and d, o are **restored from the family closing** (HCP 1205: "Isten vele, édesem, a boldog viszontlátásra"), not read, and their number is estimated. z, o, n in S5 cannot be separated from the triangle's printed letters and are restored by the word. The sense is complete and every visible sign fits.
- **e héten (row 8).** The card has hetam: the a and the m both differ from the expected héten, so this is an emendation of two signs. e hét ám ("this week, mind you") needs no change but is less idiomatic. The meaning "this week on Saturday" holds either way.
- **28-án (row 7).** The first two signs are taken as plain digits, which rests on sense: 2 has no match in the key, the a has a visible accent, and "mer ez kettő" follows naturally. Row 13 has a similar 8-like sign read as k. The word kető in the same row is overwritten and blotted.
- **Row 19 first sign** is blotted; j rests on megtaláljam. **Row 15 arra** has two touching, overwritten r signs. **S7 Feri** has faded e and r and a tilted first sign, and rests partly on the family signature.
- **h/p and d calls.** hat, hetam as h, pedig, kaptam as p, and the d of de (row 9) all come from word sense.
- **Writer's slips,** kept literally and normalized: extra stroke in row 18 (konyen m meg), stray stroke in row 22, sikerü[l], talkozni for találkozni, abba for abban, mer for mert, gyöne for jön-e, tudum for tudom, amelik.
- **Interpretive readings.** túl vasutas ruha as "all-too-railwayman clothes", a railway uniform, is an inference. mér is taken as mért ("why"), since mert leaves the sentence without a main clause. találkozásom is literally "my meeting".
- **Plain word Szép-** in the address is partly under the black box. **Dating:** only the day 26 is legible, so the 28th cannot be tested against a calendar.
- Accents are mostly unwritten and were supplied in normalization.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. It ran the command, made its own crops, wrote its own sign-class transcription of rows 1 to 24 (not blind, since it had read the ledger first) and decoded it with values taken only from a sister card. It confirmed the key, the type and the reading as a whole, and the disclosed hard spots. What changed because of it:

- **Row 3:** two signs in the ledger were not on the card. elfogadok ("accept") became fogadok ("receive, welcome").
- **Row 8:** the sign before m is a, not e, so the literal is hetam; the emendation to héten is now stated as two signs.
- **Row 9:** vale became vala, the literal agreeing with valahol.
- **Closing:** the solver's division "…ból / …g" with an unexplained gap was wrong; the visible signs fit the family formula a boldog viszontlátásig, now given as a labelled restoration.
- **Smaller points:** the month comes from the file name, not the cancel; the edge line is probably print; the translation of találkozásom is marked.

After the corrections the reviewer's decoder agrees with the ledger on all 477 letters of rows 1 to 24. The reviewer could not confirm the restored signs, the uniform reading, or the month and year of the cancel; neither could the solver.

## Sources

- HC Portal record 1227, all three tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1227 (source/metadata.md).
- Scans: https://api.hcportal.eu/media/3741/ and https://api.hcportal.eu/media/3742/, converted copies in source/, originals in work/hires/ (listed with hashes in SOURCES.md).
- Family key and closing formula: finished cards ciphers/hcp-1216, hcp-1301, hcp-1243 and hcp-1205 in this repository.
