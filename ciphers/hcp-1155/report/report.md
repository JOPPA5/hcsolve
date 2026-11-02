# HCP 1155 (cpc_1916-02-22_HU_Mezokovesd_HU_Szomolya_szomolya-19): a walk through the snow, in digits

Human solver: Tomáš Pavuk

**Status: deciphered in full (527 of 527 cipher signs, 7 of them flagged as resting on word sense or needing a note); independent review 1 verdict ACCEPT, disclosure corrected, no letter of the reading changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1155 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1155), portal name cpc_1916-02-22_HU_Mezokovesd_HU_Szomolya_szomolya-19, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article on the collection. That article was not checked for this card, and no published solution was found.

The card was sent in wartime from Mezőkövesd to the village of Szomolya in north-east Hungary, and is dated in clear **Mezőkövesd. 1916. II/22.**, a Tuesday. The partly legible postmark shows FEB 2…, which agrees as far as it can be read. It is addressed in clear to **Őnagysága / Rózsa reményű / Sziber Margitka kisasszonynak / Szomolya / (Borsod m.) u. p. Bogács**. The picture side has a printed red love verse, partly worn, which is not cipher.

The card belongs to the correspondence of Árpád and Margitka Sziber (HCP 1135 to 1179). Most of its cards are open Hungarian with only key words in digits. This one is different: the whole message is enciphered, and only "Sokszor üdvözöl és", the place and date, and the address are in clear. It follows HCP 1174 of 15 February 1916, where Árpád promises to come up the next Sunday. That Sunday was 20 February, two days before this card.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side with the printed verse (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, made from the un-converted high-resolution scan (3468 × 2298 pixels) enlarged 2 to 5 times. No OCR was used. Each letter is one digit with an optional mark, so the digit and mark have to be read together; the card has few word spaces, and the word breaks are the solver's.

The key was transferred from HCP 1174, the fullest table of the family, and 23 of its signs recur here without conflict. `Édes Margitkám`, `hogy` and `szerencsésen` opened the text at once. Eight more values then came from word sense. Two of those are already reported on sister cards (`1,` = b on HCP 1179 and `4` = f from HCP 1175). The other six rest on this card alone.

Close reading corrected several first attempts, all by rereading shapes and none by changing the key. For example, 1' and 1: look alike at low enlargement, and `ha-terba` became `határba`; `Marán` became `talán`; `arzek…` became `arra kérlek`; `neked` became `ne kérd vissza tőllem`.

The result can be reproduced from the repository root with `python3 -I ciphers/hcp-1155/work/decode.py`. It checks the scan hashes, decodes the transcription, asserts each line against the stated reading and prints the text. The normalised paragraph and the open text are fixed strings in the script.

## Key

Monoalphabetic substitution with a digit-plus-mark alphabet. Hungarian digraphs have one sign. Accents are mostly not marked: 0 serves o and ó, 1 serves i and í, and .1 serves u, ú and ű. In the table, 1' has a high dot and :1 and .1 have the marks to the left of the digit.

Signs of the family table (HCP 1174), all confirmed here:

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| 0 | o, ó | 2. | é | 6, | n |
| 0, | ö, ő | 3 | d | 7 | k |
| 1 | i, í | 3, | r | 7, | s |
| 1. | a (rarely á) | 3. | v | 7. | sz |
| 1: | e | 4, | g | 8 | m |
| 1' | á | 5 | h | 8, | t |
| :1 | ü | 5, | l | 9 | p |
| 2, | cs | | | 9, | z |

Signs added from this card (occurrences in brackets):

| Sign | Letter | Fixed by | Also on |
|---|---|---|---|
| 1, | b (10) | jobb, jobban, birtam, boldogságom, üzletbe | HCP 1179 |
| 4 | f (4) | falutól, fagyva, fél, hófúvássok | HCP 1175 |
| 2 | c (1) | nyolckor | this card only |
| 4. | gy (10) | hogy, nagyon, vagyok, egy | this card only |
| 5. | ly (1) | olyan | this card only (HCP 1179 has it as l) |
| 6 | j (7) | jobb, jó, jöt, párjára | this card only |
| 6. | ny (3) | Nyúllápáig, nyolckor, nyakam | this card only |
| .1 | u, ú, ű (9) | út, után, fúvás, haragudott, hű | this card only |

## Transcription

One card line per line; | marks a word break supplied by the solver, and ~ marks the seven signs discussed under Uncertainties.

```
L01: 2. 3 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8
L02: 2. 3, 8, 1: 7, 1 8, 5, 1: 7 | 5 0 4. | 7. 1: 3, 1: 6, 2, 2.
L03: 7, 1: 6, | 5, 1: 2. 3, 8, 1: 8 | 1. 9, | .1 8, | 7, 0 7 7 1. 5,
L04: 6 0 1, 1, | 3. 0 5, 8, | 8 1 6, 8, | 8 1 7 0 3, | 8 1: 6, 8, 1: 8
L05: 2, 1. 7 | 1. | 4 1. 5, .1 8, 0 5, | 1. | 6. .1 5, 5, 1' 9 1' 1 4,
L06: 3, 0 7. | 3. 0 5, 8, | 3 1: | 0 6, 6, 1. 8, | 1. | 8, 1: 5, 1: 9 1 4,
L07: 6, 1. 4. 0 6, | 6 0 | 3. 0 5, 8, | 1. | 7 0, 3. 1: 7, 3 1 | 5 1.
L08: 8, 1' 3, 1, 1. | 6 0 1, 1, 1. 6, | 8 1: 4, | 3. 0 5, 8, | 4 1. 4. 3. 1.
L09: 1. | 7, 1' 3, | 3 1: | 1. | 8, 1: 5, 1: 9 8, 0, 5, | 7 0, 3. 1: 7, 3
L10: 1 4, | 1. 5, 1 4, | 1, 1 3, 8, 1. 8 | 1, 1: 8 1: 6, 6, 1 | 8, 2.~ 3,
L11: 3 1 4, | 2. 3, 0, | 5 0 | 3. 0 5, 8, | 2. 7, | 6, 1. 4. | 5 0
L12: 4 .1 3. 1' 7, 7, 0 7 | 6 0 | 5 0 4. | 6, 1: 8 | 3. 1. 3, 8, 1. 8
L13: 7 0 2, 1 | .1 8, 1' 6, | 8 1: 3, 8, | 6, 1: 8 | 5, 1' 8,~ 8, 1. 8
L14: 5 0 4. | 6 0, 8, | 3. 0 5, 6, 1. | .1 8, 1' 6, 6, 1. 8 | 8,~ 1. 5,~ 1' 6,
L15: 6, 1: 8 | 1 7, | 6 0, 8, | 7 0, 3. 1: 7, 3 3, 1: | 7 0 3. 1' 2, | 1 8 3, 1:
L16: 4 2. 5, | 6. 0 5, 2 7 0 3, | 2. 3, 8, 1: 8 | 1. 9, | :1 9, 5, 1: 8, 1, 1:
L17: 5, .1 1,~ 1 6, | 1. 4. 0 6, | 5 1. 3, 1. 4, .1 3 0 8, 8, | 3 1: | 2. 6, | 1: 4.
L18: 7. 0 8, | 7, 1: 8 | 7. 0 5, 8, 1. 8
III: 5 1. | 7 0, 3, :1 5, | 0, 5, 5, 1: 5, 1: 3 | 6. 1. 7 1. 8
L20: 1, 0 5, 3 0 4, 7, 1' 4, 0 8 | 5 1. 8, 1' 3, 8, 1. 5, 1. 6,
IV : 0 5. 1. 6, | 3. 1. 4. 0 7 | 8 1 6, 8, | 1. | 8 1. 3 1' 3,
L22: 5 1. | 1. | 9 1' 3, 6 1' 3, 1. | 3, 1' 8, 1. 5, 1' 5,
L23: 2, 0 7 0 5, | 5 .1 | 7 1: 3 3. 1: 7, 1: 3
L24: 1' 3, 9 1' 3
BR1: 2. 3 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8 | 1. 3, 3,~ 1. | 7 2. 3, 5,~ 1: 7 | 5 0 4.
BR2: 1. 9, 8, | 1. | 5, 1: 3. 1: 5, 1: 8, | 6, 1: | 7 2. 3, 3 | 3. 1 7, 7. 1. | 8, 0, 5, 5, 1: 8
```

## Plaintext (Hungarian)

Accents, spaces and punctuation are added; spelling is otherwise as written, including `jöt` for jött. All is enciphered except where marked open.

Édes Margitkám!

Értesítlek, hogy szerencsésen leértem. Az út sokkal jobb volt, mint mikor mentem, csak a falutól a Nyúllápáig rosz volt, de onnat a telepig nagyon jó volt. A kövesdi határba jobban meg volt fagyva a sár, de a teleptől Kövesdig alig bírtam bemenni, térdig érő hó volt és nagy hófúvássok. Jó hogy nem vártam kocsi után, mert nem láttam, hogy jöt volna utánnam, talán nem is jöt Kövesdre Kovács Imre. Fél nyolckor értem az üzletbe. Lúbin agyon haragudott, de én egy szót sem szóltam.

III Ha körül ölleled nyakam / boldogságom határtalan.

IV Olyan vagyok, mint a madár, / ha a párjára rátalál.

Sokszor üdvözöl [open] és [open] csókol hű kedvesed (Árpád).

(Édes Margitkám, arra kérlek, hogy azt a levelet ne kérd vissza tőllem.) Mezőkövesd. 1916. II/22. [place and date open]

Open address: Őnagysága / Rózsa reményű / Sziber Margitka kisasszonynak / Szomolya / (Borsod m.) u. p. Bogács.

Printed verse on the picture side (not cipher): Csókolom a kis kezedet / Írtam Neked egy szerelmes levelet / Egy szó nem sok, az is elég / Csak azt mondd meg szeretsz-e még.

## English translation

Sweet Margitka! I let you know that I got down safely. The road was much better than when I went up, only from the village to the Nyúllápa was it bad, but from there to the settlement [telep] it was very good. In the Kövesd fields the mud was frozen harder, but from the settlement to Kövesd I could hardly get in: there was knee-deep snow and big snowdrifts. It is good that I did not wait for the cart, because I did not see it coming after me; perhaps Imre Kovács did not come to Kövesd at all. I reached the shop at half past seven. Lúbin was furious, but I did not say a word.

III When you put your arms round my neck / my happiness has no bounds.

IV I am like the bird / when it finds its mate.

Many greetings and kisses from your faithful sweetheart (Árpád).

(Sweet Margitka, I ask you not to ask for that letter back from me.) Mezőkövesd, 22 February 1916.

Address: Her Ladyship, the rosy-hoped Miss Margitka Sziber, Szomolya, Borsod county, post office Bogács.

## Slovak translation

Sladká Margitka! Oznamujem ti, že som šťastne došiel dolu. Cesta bola oveľa lepšia, než keď som išiel hore, len od dediny po Nyúllápu bola zlá, ale odtiaľ až po osadu [telep] bola veľmi dobrá. V kövesdskom chotári bolo blato lepšie zamrznuté, ale od osady do Kövesdu som sa ledva dostal, bol sneh po kolená a veľké záveje. Dobre, že som nečakal na povoz, lebo som nevidel, že by šiel za mnou, možno ani neprišiel do Kövesdu Imre Kovács. O pol ôsmej som prišiel do obchodu. Lúbin sa strašne hneval, ale ja som nepovedal ani slovo.

III Keď ma objímeš okolo krku, / moje šťastie nemá hraníc.

IV Som ako vták, / keď nájde svoju družku.

Veľa pozdravov a bozkov od tvojho verného milého (Árpád).

(Sladká Margitka, prosím ťa, aby si odo mňa nežiadala ten list späť.) Mezőkövesd, 22. februára 1916.

Adresa: Jej Milosť, Rózsa reményű (ružových nádejí) slečna Margitka Sziberová, Szomolya, župa Borsod, pošta Bogács.

## Uncertainties

Signs flagged in the transcription:

- `Lúbin`, third sign: read as `1,` (b). Its bar resembles 7, so `Lúsin` is not excluded, although the reviewer's crop favours 1 over 7. It is the only unknown name, taken as a person at the shop, perhaps the employer. A search of the sister cards does not find it. The vowel length is unknown, since .1 also stands for u.
- `láttam`, first t: deformed, and could be taken for a 9 with a tail. The low loop with a fused comma favours 8,, and `láttam` is the only reading that makes sense.
- `talán`, first sign: the same deformation of 8,.
- `talán`, third sign: given as 5,, but with a filled closed bowl unlike the open 5 elsewhere. Only its bar and comma support 5,.
- `tér-`, second sign: given as 2., but a ligature runs from the foot of the 2 into the 3 with only a swelling where the dot should be. Strictly it is unmarked. `é` is fixed by `térdig`.
- `arra`, second r: looks at first like 9 with a comma, but the closed top and bottom hook are those of the writer's 3, as in `kövesdre`. Shape and phrase agree.
- `kérlek`, the l: faint, under the mark of the collector's stamp; the bar and comma of 5, are present.

Other points:

- `bemenni`: an ink blot between the two n signs is not counted as a sign.
- `2` = c and `5.` = ly each occur once, in the certain words `nyolckor` and `olyan`. Sister cards write `5.` where the word gives l, so it may be a looser variant.
- `1.` stands for á in `vartam` (vártam), so the split between 1. and 1' is not perfectly strict.
- Spellings kept as written: `rosz`, `onnat`, `jöt`, `hófúvássok`, `utánnam`, `ölleled`, `tőllem`. They look like the writer's habits, not misreadings.
- `Nyúllápa` is read as a local field name and has not been confirmed in a gazetteer. Which `telep` is meant is unknown. The letters are clear.
- `III` and `IV` stand in boxes before the two couplets, with no `I` or `II` on the card. Their purpose is unknown; they may number couplets of a song.
- Underlines, a curved arrow from the `Kovács Imre` line to the `üzletbe` line, and a thin line from the verse to the foot block are copied as marks. The text reads in order, and their purpose is unknown.
- "That letter" in the final sentence has no context on this card.

## Why the reading is believed correct

- All 527 signs decode into continuous Hungarian with no exception list. The signs that recur up to 10 times keep one value through unrelated words.
- Two rhyming couplets come out: `nyakam` / `határtalan` and `madár` / `rátalál`.
- The account is coherent: a walk in snow from Szomolya down to Mezőkövesd, passing village, Nyúllápa, telep and Kövesd, then arrival at work.
- It continues HCP 1174, with the same `Édes Margitkám`, the same signature `Árpád` and a closing formula of the same pattern, and the dates fit.

## Review

An independent reviewer (a separate Claude Opus 5.5 agent) tried to refute the reading and could not; the verdict is **ACCEPT**. It ran the reproduction command, wrote its own decoder with its own key table (no unmapped sign, no conflict with the HCP 1174 table), recomputed the scan hashes, compared every row with enlarged strips of the scan, and examined each hard sign at 3 to 5 times enlargement. Its comparison of the transcription was by eye and not blind. It could not verify the place name Nyúllápa or that Lúbin is a person, did not read the HistoCrypt article, and did no web search for a published solution.

It raised four minor findings, all about disclosure. All were fixed, and no letter of the reading changed:

- The count of signs read by sense was too low. `tér-` and the third sign of `talán` were added, and the solver also flagged the first sign of `talán`, so four became seven.
- "New on this card" overstated: `1,` and `4` were already attested on sister cards. The tables now say so.
- The note on `arra` was too pessimistic about the sign's shape and was corrected.
- The normalised text silently gave `jött`. It now keeps `jöt`, as written.

The brackets of `(Borsod m.)` in the address were also restored after the reviewer's remark.
