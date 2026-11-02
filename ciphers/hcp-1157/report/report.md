# HCP 1157 (cpc_1915-12-03_HU_Mezokovesd_HU_Szomolya_szomolya-08): a cipher salutation and a coal-gas poisoning

Human solver: Tomáš Pavuk

**Status: all 24 cipher signs are deciphered with a transferred key, and the open Hungarian text is read in full; independent review 1 verdict REVISE, findings addressed, one accent in the cipher reading changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1157 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1157), portal name cpc_1915-12-03_HU_Mezokovesd_HU_Szomolya_szomolya-08, from Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), which was not opened for this card, so it is not known whether the article discusses it.

The card went from Mezőkövesd to Szomolya in north-east Hungary, in wartime. The address reads "Tek. / Szépreményü / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács." (to the honourable, fair-hoped Miss Margitka Sziber, post office Bogács). The postmark reads MEZŐKÖVESD 915 DEC 3, N, C; a mark stands before the 3, so 13 cannot be fully excluded. The picture side, a couple at a rustic fence, has no writing.

The card belongs to the Mezőkövesd correspondence to Margitka Sziber, 1915 to 1916, of which other cards are deciphered in this repository (for example HCP 1165, 1174, 1178 and 1179). The writer is the suitor who signs Sz. A. on sister cards and, in cipher, Árpád on HCP 1174. This card itself only gives the initials.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, from the un-converted high-resolution scan enlarged 2 to 3 times. No OCR was used. Only the top two rows of the message are enciphered; the rest of the card is open Hungarian.

No key was recovered here. The monoalphabetic key of the family, in which one letter is one digit together with its mark (comma, dot, colon or raised dot), was reconstructed on the finished card HCP 1174. It was applied to the 24 signs of this card. Fourteen of the 15 distinct signs are on the HCP 1174 table. The fifteenth, `4.` = gy, is fixed on the finished card HCP 1165 by `hogy` and `nagyon`. A short script checks the hashes of the scans, decodes the signs and asserts each word:

    python3 -I ciphers/hcp-1157/work/decode.py

The open text is typed into that script, so the command reproduces only the decoding of the cipher.

![The two cipher rows; the word Édes at the end of row 2 starts the open text (work/crops/report_cipher.png)](../work/crops/report_cipher.png)

## Key

Only the signs that occur on this card are listed.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| `1` | i | `2.` | é | `6,` | n |
| `1.` | a | `3` | d | `7` | k |
| `1:` | e | `3,` | r | `7,` | s |
| `1'` | á | `3.` | v | `8` | m |
| `4,` | g | `4.` | gy | `8,` | t |

## Ciphertext and decoding

`/` is a single slanted stroke at each row end, read as an exclamation stroke.

    7 1: 3 3. 1: 7,   8 1. 3, 4, 1 8, 7 1' 8 /
    2. 7,   1' 6, 4. 1 7 1' 8 /

    kedves  margitkám  /  és  ángyikám  /

## Plaintext

Square brackets mark the enciphered part. Spelling and word division are as on the card; words broken at a line end are joined.

[Kedves Margitkám! És ángyikám!]

Édes anyám már elment csütörtökön Róza itt maradt nem tudom medig lesz itt. En a régi kvártélyon háltam pénteken este demajd az életembe került még most is nagyon rosszul vagyok a dolog úgy történt hogy a szoba nagyon hideg volt és vittem szenet és fát magam voltam egyik inassem hált ott felvoltam 12 óráig mert rendezgettem egyet mást aztán betüzeltem a kályhába jól meg raktam szénnel a cső egyhelyen lyukas én lefeküdtem és egyóra múlva felébredtem borzasztó hányinger fogot elő aligbírtam felkelni már nem volt erőm az ajtót nagy nehezen kinyitottam és ki szaladtam az udvarra ) a szén gáz akart megölni

Sz. A.

mindnyájatokat csókollak.

## English translation

Dear Margitka of mine! And my ángyika (sister-in-law or aunt by marriage)! [cipher ends]

My dear mother already left on Thursday; Róza stayed here, I don't know how long she will be here. I slept at the old lodgings on Friday evening, but it nearly cost me my life, I am still very unwell. It happened like this: the room was very cold and I carried in coal and wood. I was alone, neither of the apprentices slept there. I was up until 12 because I was tidying one thing and another, then I lit the stove and loaded it well with coal. The pipe has a hole in one place. I lay down and an hour later I woke up; a terrible nausea seized me, I could hardly get up, I had no strength left, with great difficulty I opened the door and ran out into the yard. ) The coal gas tried to kill me.

Sz. A.

I kiss you all.

## Slovak translation

Drahá moja Margitka! A moja ángyika (švagriná alebo teta)! [koniec šifry]

Moja drahá matka už odišla vo štvrtok; Róza tu ostala, neviem, dokedy tu bude. V piatok večer som spal v starom podnájme, ale takmer ma to stálo život, ešte aj teraz mi je veľmi zle. Stalo sa to takto: izba bola veľmi studená a nanosil som uhlie a drevo. Bol som sám, ani jeden z učňov tam nespal. Bol som hore do 12, lebo som upratoval všeličo, potom som zakúril do pece a dobre som ju naložil uhlím. Rúra je na jednom mieste deravá. Ľahol som si a o hodinu som sa zobudil; prepadla ma strašná nevoľnosť, sotva som vládal vstať, už som nemal síl, s veľkými ťažkosťami som otvoril dvere a vybehol som na dvor. ) Uhoľný plyn ma chcel zabiť.

Sz. A.

Bozkávam vás všetkých.

## What remains uncertain

Cipher:

- `ángyikám`, first sign. The dots of the first and last `1` of this word stand at the same height, so the writer made one sign twice, and the last is á, as in `Margitkám`. Both dots are lower than the `1'` of row 1, so this rests on the match and the context, not on the dot alone. Read as `angyikám` it would be the same word with a dropped accent.
- Meaning of `ángyika`. The word stands in clear on HCP 1144 and HCP 1165, and HCP 1175 opens `Kedves Ángyika!`. It means a woman related by marriage, but the exact relation, and who she is here, are not given. A personal name cannot be excluded. `mindnyájatokat` (you all) fits more than one person in the house.
- `4.` = gy occurs once here. Its value comes from HCP 1165 and from the word.
- The second `7` of row 1 has a looped top unlike the other 7s, but it has the cross bar, and k is what the name needs.
- The row-end strokes have no dot. They are taken as punctuation.

Open text:

- The weakest words are `hányinger` (the h is partly under the printed Serie Nr. 2963), the second `hált` (publisher marks overlap it), and `már` and `ki` (under the printed FOTOTAGLIO box, and blotted). All are legible on enlargement.
- The closing parenthesis before `a szén gáz` has no opening partner, and its role is unexplained.
- `mindnyájatokat csókollak.` and `Sz. A.` stand on the address side. They are printed last here, but they may have been written earlier, before the writer ran out of room.
- `Sz. A.` is taken as written. That he is the Árpád of HCP 1174 is not proven by this card.
- Who Róza is is not stated.
- Date of the event. 3 December 1915 was itself a Friday, so "pénteken este" would be a week before; a postmark of 13 December, a Monday, would suit "still very unwell" better. This is unresolved and does not touch the text.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-ran the script, decoded the card with its own script, read every cipher sign and every open row from the high-resolution scan, measured the dot heights and read sister cards. It agreed with the open text word for word, apart from word division, and gave the verdict REVISE.

- Major: the first sign of the last enciphered word is `1'`, not `1.`, so the word is `ángyikám`, a kin word, not `angyikám` with a possible "little angel" sense. Fixed in the key note, script and translations.
- Minor: `4.` = gy was wrongly called new; it is credited to HCP 1165.
- Minor: word division is now kept as on the card (`demajd`, `inassem`, `meg raktam`, `egyóra`, `En`).
- Minor: the row-end marks are described as strokes.
- Minor: the looped `7` is noted as a variant form in the counts.

The solver accepted all five findings. Nothing else in the reading changed.

The reviewer could not verify the HistoCrypt article, the postmark day beyond the above, or the identities of the ángyika, Róza and Sz. A. Sister card readings were taken from their solution files, not from their pixels.
