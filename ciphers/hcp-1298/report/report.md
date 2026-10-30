# HCP 1298 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-77): Feri to Jolánka Tóth, pencil instead of ink

Human solver: Tomáš Pavuk

**Status: complete reading, with one tentative verb (row 11). All 622 sign tokens are transcribed and decode with the family key. Independent reviews 1 and 2 returned REVISE; their findings are addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1298 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1298), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-77, part of Tobias Schrödel's collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, category Substitution, date and language Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution was found or used.

The plain address, in violet, reads Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás. The upside-down rectangular cancel ends -TA-ÚJPEST P.U., the Rákospalota-Újpest station cancel known from HCP1288 (the start of the name is restored). The round cancel shows an 8; its month, year and place could not be read. The picture side has printed Hungarian verse only and no cipher. The message itself shows that it was written just after New Year and Epiphany.

The card belongs to the "Jolánka" family of postcards in this repository (HCP1216 and sisters). The signature "Feri" and the closing formula match HCP1216; beyond that the writer's identity is not established. The key comes from those finished cards, whose earlier passes were made by an OpenAI GPT solver and by Claude Opus 5.5. It is a transferred key, not a new recovery. All work on this card itself was done by Claude Opus 5.5.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is manual, from enlarged crops of the high-resolution address side, sign by sign into a ledger (ciphers/hcp-1298/work/sign-ledger.txt). No OCR was used. The ledger holds 622 tokens; the two digraph signs, gy and cs, each count as one token for two written elements. Numerals are in clear.

The writing runs round the card: 26 rows in the left block, then the bottom margin left to right, the right edge upward, the top margin with the card turned 180°, and six short rows in the stamp place. Those six lay under the stamp, whose remains are still on the card. The top margin is not a continuation of row 1: its faint signs read only when rotated, and it joins magok|nál across the corner.

A script checks the hashes of the images and decodes the ledger with the key:

```sh
python3 -I ciphers/hcp-1298/work/decode.py
```

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs, unchanged from the family.

| Sign | Letter | Sign | Letter |
|---|---|---|---|
| two bars | a | section mark S | k |
| six | b | wave | l |
| left bowl ( | c | three strokes | m |
| () | cs | two strokes | n |
| short stroke left of a long stroke | d | cursive loop | o |
| three bars | e | long stroke with tick on the right | h / p |
| cross + | f | F shape | r |
| hooked ς | g | right bowl ) | s |
| ς + y-shaped sign | gy | Γ | t |
| dotted crossed curve | i | plain X | u (with double mark ű) |
| inverted T | j | chevron Λ | v |
| | | tailed crossed x | z |

h and p are one sign, separated only by word sense. Accents are mostly not written and are supplied in the normalized text.

## Plaintext

Literal decipherment. `h` stands for the h/p sign, `?` means the value rests on word sense, and `·` is a mark with no letter value.

```text
01 kedvesjolankamnagyon
02 kivanomhogyalegjobbegesz?
03 segbentalaljasoraim·
04 kedvesemszivesenelmenek
05 ahesztorinehoznemme
06 hetekelmertugyelvagyok
07 foglalvakedvesemami
08 engemilletcsakmegvagyok
09 esegesegesvagyokazuj
10 evilahjatedesemeloszo?r
11 3ikanbeozat?t?aahostasesen
12 5ikenkahtamkezhezesaz
13 ertnemvalaszanedesemugy
14 hamarabbigaz
15 elvagyokr?oglalvahogy
16 nemtunikefelmaganek
17 edesemhogymindigcsak
18 cz?eruzavalirokdeazt
19 csakanakkovetkeztesse
20 edesemhogyotiromso?ra
21 i?maholnemlehetten
22 tetszereznikedvesemkah
23 tamatothilonkatolegyla
24 hotujevremasnakneisju
25 tottameszibekedvesem
26 hogymulatotvasarnah
B1 megavizkesztnahjanvolte
R1 valaholmulatsagbanmostmagok
T1 nalmindigcsakennemmulathat?·
S1-6 csokol / jaszam / sirig / hűked / vesse / feri
```

### Hungarian (normalized)

Kedves Jolánkám! Nagyon kívánom, hogy a legjobb egészségben találja soraim. Kedvesem, szívesen elmennék a Pesztorinéhoz, [de] nem mehetek el, mert úgy el vagyok foglalva, kedvesem. Ami engem illet, csak megvagyok és egésséges vagyok. Az újévi lapját, édesem, először 3-ikán behozta? a postás, és én 5-ikén kaptam kézhez, és azért nem válasz[oltam], édesem, úgy hamarabb. Igaz, el vagyok foglalva. Hogy nem tűnik-e fel magának, édesem, hogy mindig csak ceruzával írok, de azt csak annak következtesse, édesem, hogy ott írom soraim, ahol nem lehet tentet szerezni. Kedvesem, kaptam a Tóth Ilonkától egy lapot újévre, másnak ne is jutottam eszébe. Kedvesem, hogy mulatott vasárnap, meg a vízke[re]szt napján? Volt-e valahol mulatságban most maguknál? Mindig csak én nem mulathat[ok].

In the stamp place: Csókolja szám. Sírig hű kedvese, Feri.

### English

Dear Jolánka! I wish very much that my lines may find you in the best of health. My dear, I would gladly go to Mrs Pesztori's, [but] I cannot go, because I am so busy, my dear. As for me, I am just getting by and I am healthy. Your New Year's card, my sweet, the postman brought in [verb tentative] first on the 3rd, and I received it on the 5th, and that is why I did not answer, my sweet, any sooner. True, I am busy. Has it not struck you, my sweet, that I always write only in pencil? But conclude from that only, my sweet, that I write my lines there, where no ink can be had. My dear, I got a New Year's card from Ilonka Tóth; nobody else even thought of me. My dear, how did you enjoy yourself on Sunday, and on the day of Epiphany? Were you at some party there at your place just now? Only I never get to have fun.

In the stamp place: My mouth kisses you. Your sweetheart, faithful unto the grave, Feri.

### Slovak

Milá Jolánka! Veľmi si želám, aby Vás moje riadky našli v najlepšom zdraví. Moja milá, rád by som išiel k Pesztoriovej, [ale] nemôžem ísť, lebo som taký zaneprázdnený, moja milá. Čo sa mňa týka, ako tak sa držím a som zdravý. Váš novoročný pohľad, moja sladká, priniesol poštár [sloveso neisté] najprv 3., a ja som ho dostal 5., a preto som neodpovedal, moja sladká, skôr. Pravda, som zaneprázdnený. Nenapadlo Vám, moja sladká, že vždy píšem len ceruzkou? Ale z toho usudzujte len to, moja sladká, že svoje riadky píšem tam, kde sa nedá zohnať atrament. Moja milá, dostal som od Ilonky Tóthovej novoročný pohľad, inému som ani nezišiel na um. Moja milá, ako ste sa zabávali v nedeľu a na deň Troch kráľov? Boli ste teraz u Vás niekde na zábave? Len ja sa nikdy nemôžem zabávať.

Na mieste známky: Bozkávajú Vás moje ústa. Váš do hrobu verný milý, Feri.

## Uncertainties

- **Row 11 verb, the only word-level gap.** The stretch is crowded and retraced. Behozta ("brought in") is printed, with the extra faint strokes taken as a corrected false start; be[h]ozatta ("had brought in") is the alternative. Neither has a visible h. The sense of the clause does not depend on it.
- **Row 11 first sign, 3 or 8.** The shape does not decide. 3 is a choice based on date order: the postman on the 3rd, received on the 5th.
- **Rows 20–21 soraim.** That the two signs are not z and o as first read rests on shape; which of them is o and which is i rests on word sense and on the same word in row 3. No dot is visible on the i, as on feri in S6.
- **Row 2 final z, row 15 first letter (a long-barred F read as f), row 18 second sign (czeruzával), and the last t of the top margin** rest on word sense. The final p of row 26 has an unusual looped form, but vasárnap is secure. Előszőr has a very faded second o.
- **Marks with no value.** The flourish after row 3 and a tick next to the end of row 1.
- **Editorial supplies.** [de] in row 6, válasz[oltam] for literal `valaszan` (the word is cut short), vízke[re]szt for `vizkeszt`, and mulathat[ok].
- **Csókolja szám** ("my mouth kisses you") is literal, but its sense is odd. It could be short for számtalanszor ("countless times"), the closing of HCP1216.
- **Date and persons.** The year and month are not legible, and Feri and Mrs Pesztori are not identified.

## Review and what changed

Two independent review rounds were done by a separate Claude Opus 5.5 agent, who decoded the ledger with a separately typed table and compared signs on enlarged crops.

**Review 1 (REVISE)** corrected eleven points against the pixels. Among them: a sign wrongly inserted in row 26, a false claim of a scribal slip in row 6, row 15 foglalva, the note that the last rows lay under the stamp, and a stray bar in row 12. The status was set to partial. The solver also dissolved the "unknown word" `sesen` into a postás és én by word division, withdrew én édesem in row 10, and printed 3 for the first sign of row 11.

**Review 2 (REVISE)** confirmed a postás és én and found that the remaining "unknown word" `szra|oma` came from two misread signs: it is soraim, as in row 3, giving "that I write my lines there, where no ink can be had". The solver's earlier suggestion that it was a place-name was withdrawn. The review also showed that d is separable from h/p by the side of its tick, removed the doubt from the d of row 10, and advised offering behozta beside be[h]ozatta. All of this was applied, and the status became a complete reading with one tentative verb. The review stated that no third round was needed if only these changes were made.

The reviewer could not verify the row 11 verb, the 3 or 8 call, the cancel dates, or that the dot of the row 21 i is truly absent.
