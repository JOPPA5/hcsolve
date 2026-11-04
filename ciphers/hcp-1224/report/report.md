# HCP 1224 (cpc_1912-10-12_HU__HU_Jasz Arokszalas_jolanka-32): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (26 main rows and 7 rows under the stamp, 572 written signs); independent review 1 verdict REVISE, all findings addressed, no word of the reading changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1224 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1224), portal name cpc_1912-10-12_HU__HU_Jasz Arokszalas_jolanka-32, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The date 1912-10-12 comes from the portal's file name.

The picture side, scanned sideways, is a tinted photograph of a young man with a candle beside him and a woman appearing in his dream or thoughts. It has no writing. A row of small dots on the woman's garment and two red streaks look like part of the tinted image or staining, not script. This was checked at the resolution of the scan only.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address side is in clear: **Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás** ("To the promising Miss Jolánka Tóth"). The message is on the same side in red ink and invented signs: 25 rows on the left half, a 26th row along the whole bottom edge to the right corner, and seven short rows in the stamp box, uncovered when the stamp came off.

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

The large postmark reads BUDAPE… 912 OK…, so the "here" of the letter is apparently Budapest, although a postmark proves only the place of posting. Its day is not legible. The second postmark reads …ROK… (Jászárokszállás) with OKT and what look like 1 and 2, which agrees with the portal date without being a firm reading of the day.

The card belongs to the "Jolánka" family of Hungarian cipher postcards, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery. No published reading of this card was found or used.

## Method

- **Key test.** The key table of HCP 1216 was applied without change. It read at once: "kedvesjolankam becses".
- **Transcription.** Claude Opus 5.5 read every row from enlarged crops of the high-resolution address scan and recorded it as a sign ledger, one token for each written sign (work/ledger.txt). The ledger is manual; no OCR was used. A script then decodes it and checks the hashes of the scans.
- **Normalization.** The writer spells loosely, with single consonants and a few slips. The literal decipherment is kept as written, and the normalized Hungarian below is editorial.
- **Review.** A separate Claude Opus 5.5 agent made its own transcription by sign class, its own key table and a diff against the ledger. Its pass was not blind, because it had read the solver's text first. See the review summary below.

## Key

Hungarian simple monoalphabetic substitution with invented signs. Register type: **MASC + Steganography** (2026-11-03), because seven rows of the message were hidden under the stamp. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark / s-shape | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma | t |
| long + short stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short | h / p (here also d) | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | joined loop + descender | gy | | |

Marks over o and u give ö/ő and ü/ű. The digraphs are written with two signs: sz = s + z, zs = z + s. In row 11, "43 fil" and the k after it are written in clear. The tall-plus-short sign is a near-homograph of h, p and, on this card, often d, so these values rest on word sense. Only the d of rows 1, 5, 8 and 16 has a distinct joined 4-like form.

## Plaintext

Literal decipherment, row by row. {#} is a struck sign and {o|i?} a sign whose class cannot be settled.

```text
01 kedvesjolankambecses          14 abajhogyjönateles
02 soraitmegkaptammely           15 ijenkorkevesamunka
03 etnagyonköszönökami           16 demajdcsakkitelelekva
04 amjobanletünkharajtam         17 lahogykedvesemolvassa
05 fügnemvalunkelsohaede         18 csakelharmadiklapomat
06 semanakhogyjobeitmint         19 marabairtamhogyjozsi
07 gyöngyösönaznekemmin          20 ekaltöltötotemavasarnapot
08 degyvolnacsakakazfaj          21 mostvasarnap{#}emvoltam
09 hogyjolankamolytavol          22 seholköszonomaversetha
10 vantölemamiafize              23 szivbölirtaaszivemmarreg
11 testiletiit[43 fil k]e        24 azöneedesemhogygondol
12 resektöbetnapontamint         25 hatojathogylapjatmutoga
13 gyöngyösöndecsakaz
26 tomvalkinekjoeg{o|i?}segetkivanokistenvaleedesemf
stamp: gondolj / nehaata / volban / epedö / szivre / hüima / dodferi
```

Normalized Hungarian (word division, accents, spelling and most punctuation are editorial):

**Kedves Jolánkám! Becses soráit megkaptam, melyet nagyon köszönök. A mi ám jóban lettünk, ha rajtam függ, nem válunk el soha, édesem. Annak, hogy jobb-e itt, mint Gyöngyösön, az nékem mindegy volna, csak az fáj, hogy Jolánkám oly távol van tőlem. Ami a fizetést illeti, itt 43 fil. keresek többet naponta, mint Gyöngyösön, de csak az a baj, hogy jön a tél, és ilyenkor kevés a munka, de majd csak kitelelek valahogy. Kedvesem, olvassa csak el harmadik lapomat, már abba írtam, hogy Józsiékkal töltöttem a vasárnapot. Most vasárnap nem voltam sehol. Köszönöm a verset, ha szívből írta, a szívem már rég az öné. Édesem, hogy gondolhat olyat, hogy lapját mutogatom valakinek? Jó egészséget kívánok, Isten vele, édesem. [f]**

**Under the stamp: Gondolj néha a távolban epedő szívre. Hű imádód Feri.**

English translation: **Dear Jolánka! I have received your esteemed lines, for which I thank you very much. We have become close, you know, and if it depends on me we shall never part, my sweet. Whether it is better here than in Gyöngyös would be all the same to me; it only hurts that my Jolánka is so far from me. As for the pay, here I earn 43 fillér more per day than in Gyöngyös, but the only trouble is that winter is coming, and at this time there is little work, but I shall get through the winter somehow. My darling, do read my third card; I already wrote in it that I spent Sunday with Józsi and his family. This Sunday I went nowhere. Thank you for the verse, if you wrote it from the heart; my heart has long been yours. My sweet, how can you think such a thing, that I show your card to anyone? I wish you good health; God be with you, my sweet. [f]**

**Under the stamp: Think sometimes of the heart pining in the distance. Your faithful adorer, Feri.**

Slovak translation: **Milá Jolánka! Vaše vzácne riadky som dostal, za ktoré veľmi ďakujem. Veď sme sa zblížili, a ak to bude závisieť odo mňa, nikdy sa nerozídeme, moja sladká. Či je tu lepšie ako v Gyöngyösi, to by mi bolo jedno, bolí ma len to, že moja Jolánka je odo mňa taká ďaleko. Čo sa týka platu, tu zarobím denne o 43 fillérov viac ako v Gyöngyösi, ale problém je len v tom, že prichádza zima a v tomto čase je málo práce, ale nejako tú zimu prečkám. Moja drahá, prečítajte si moju tretiu pohľadnicu, už som v nej písal, že som nedeľu strávil s Józsim a jeho rodinou. Túto nedeľu som nebol nikde. Ďakujem za verš, ak ste ho písali zo srdca; moje srdce je už dávno Vaše. Moja sladká, ako si môžete myslieť niečo také, že Vašu pohľadnicu niekomu ukazujem? Prajem Vám dobré zdravie, s Bohom, moja sladká. [f]**

**Pod známkou: Mysli niekedy na srdce túžiace v diaľke. Tvoj verný ctiteľ Feri.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1224/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of all four scans, decodes the ledger work/ledger.txt with the family key, prints the rows above and prints the normalized text work/normalized.txt. It does not read the image; the transcription step is manual.

## Uncertainties

None of these changes the sense of the letter, except that the first affects the tone of one clause.

- **Rows 3–4, "a mi ám jóban lettünk".** The signs give "ami am joban". Dividing it as "a mi ám jóban" ("we, you know, on good terms"), with ám as the emphatic particle, is an editorial interpretation. The opening "A mi" is awkward, and neither solver nor reviewer found a better division. The final sign of row 3 is the crossed curve with no dot. Single b also allows "jobban", which reads worse.
- **Row 26, "egészséget".** The card has eg, one curved sign, then seget. The curved sign has a closed lower loop and a hooked right end, like an undotted o or i, and it is not the z of this card. No shape settles its class. The normalization comes from the set phrase "jó egészséget kívánok". The word is safe; its spelling is not.

![Row 26: g, the curved sign, right bowl (review/work/z26j.png)](../review/work/z26j.png)

- **Writer's slips, kept in the literal text.** Row 8 "csakakaz" for csak az; row 20 "töltötotem" for töltöttem; row 26 "valkinek" for valakinek (a colloquial contraction) and "vale" for vele (two bars).
- **Row 21.** A two-stroke sign is struck through, followed by e and m. The word is plainly a corrected "nem"; the struck n is a sense call.
- **End of row 26.** A final cross sign with a long bar sits at the corner: literally f. It may be an initial for Feri or a flourish; it is left as [f].
- **h, p and d.** All tall-plus-short signs are assigned by word sense. This covers p in megkaptam, naponta, lapomat, vasárnapot, vasárnap, lapját, epedő; d in de (row 13), harmadik, édesem (rows 24, 26), gondol, gondolj, epedő, imádód; h elsewhere.
- **Blots and crowded signs.** The a of megkaptam (row 2) and jóban (row 4), the n of naponta (row 12), the j of ijenkor (row 15), the k of harmadik (row 18) and the h of hogy (row 24) are blotted and read by word sense. The bars after t or j in rows 19, 20 and 25 are crowded and counted as a. The i of imádód shows no dot.
- **Spelling.** ijenkor, ojat, letünk, füg, aba and töbet are the writer's spelling of ilyenkor, olyat, lettünk, függ, abba and többet. "abba" ("in that one") is the editor's reading of "aba".
- **Accents.** Most acute accents are too faint to audit and are supplied. The ö dots in row 3 are clear; row 22 has none at the matching place. A tick over the o of "dód" confirms ó.
- **"43 fil k".** "fil." is taken as fillér. The k in clear belongs to ke|resek; why he left it in clear is unknown.
- **Address form.** The body uses formal Ön, while "gondolj" and "imádód" under the stamp are familiar. This mix is in the signs and is kept.
- **Persons.** The "third card" and Józsi are not identified, nor is Feri proved to be the Feri of every family card. A workman with a Gyöngyös connection appears on HCP 1303 and 1310, which is agreement of context, not proof.
- **Prior work.** The key was transferred from the family, not recovered blind from this card. No published reading of this card was found. The AI Decipherment Register had no record of it when checked on 2026-11-02.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **REVISE**. It confirmed the command's output, the family key against HCP 1216, the clear address, the reading of every row on the scan at 1:1 and 2x with many enlargements, the language and the absence of any published solution. It concluded that the reading stands but that the ledger was not a true record of the signs in row 26, where the expected text had crept into the transcription.

Findings and what changed:

- **Three major findings, all in row 26.** The first draft ledger held a sign not on the card and the wrong class in "egészséget", an added a in "valakinek", and an e where the card has a in "vele". The ledger now records what is written ("eg{o|i?}seget", "valkinek", "vale"), and the token count fell from 574 to 572.
- **Row 21.** Three bars, not two: the literal is {#}em, so an uncertainty disappeared.
- **Row 3.** The second o of köszönök has dots.
- **Counts.** hogy occurs 7 times, not 8. The solver also found that édesem occurs 3 times, not 4.
- **Row 24.** A real full stop after "öné" moves "édesem" to the next sentence, in the Hungarian and in both translations.
- **Disclosures.** The blotted k in row 18, the tall-plus-short d signs and the tick on "dód" were added. The solver extended the d marking to "édesem" in rows 24 and 26.
- **Context.** The Budapest postmark was added; the solver also added the second postmark.

No word of the normalized text changed because of the review. Only the sentence division in one place and the literal letters above did.

## Credits

- **Claude Opus 5.5, 2026-11-02:** source capture (orchestrator), transcription (sign ledger), transfer of the key, decipherment, response to review and this report.
- **Claude Opus 5.5, separate reviewer agent:** independent review.
- **Earlier family work (OpenAI GPT solver, GPT-6 Astra / GPT-6.1 Sol, and Claude Opus 5.5):** establishment of the Jolánka key on the sister cards. No earlier work existed on this card.
