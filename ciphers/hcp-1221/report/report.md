# HCP 1221 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-66): Feri (?) to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 20 left rows and the 7 rows under the stamp); independent review 1 verdict REVISE, one clause and two small details corrected. One sign rests on word sense, and two words of the unenciphered sender line remain unresolved.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1221 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1221), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-66, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166, which was not consulted for this reading). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was found.

The picture side is a printed photograph with publisher number 1012 and no writing. All the writing is on the address side, in red ink: 20 cipher rows at the left and 7 short rows in the place of the lost stamp.

The plain parts of the address side read **Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás** ("to the promising young lady Jolánka Tóth, Jászárokszállás"). The sender line, also in plain Latin script, reads Rákos Szent Mihály, then two unresolved words, then Bocskai utcza 3. The card is undated: the only legible part of the postmark is "C 12".

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the area of the lost stamp and the sender line (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth in Jászárokszállás, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key, reconstructed on those cards by earlier work of an OpenAI GPT solver, completed by Claude Opus 5.5. This card was therefore read with a **known, transferred key**, not by a new key recovery.

The card has no signature. "Feri" is inferred, not written: the hand and key match the family, and HCP 1309 has Holes Feri, formerly at Szentmihály, while this card is sent from Rákosszentmihály.

## Method

The transcription is **manual**: each sign was read from enlarged crops of the portal's un-converted scan and recorded as one token in a sign ledger. No OCR was used. The ledger is then decoded by a script with the family key, which also checks the SHA-256 hashes of the scans. The key was not changed to fit this card, and no new sign value was needed. The opening, "Szeretett édes Jolánkám! Ne haragudjon, hogy oly ritkán írok", settled the sign classes at once.

To reproduce, run from the repository root:

```text
python3 -I ciphers/hcp-1221/work/decode.py
```

## Key

Type: **MASC + Steganography** (updated 2026-11-03). Simple monoalphabetic substitution with invented graphic signs; word divisions are not marked. The steganographic part is the 7-row enciphered message written in the stamp box and hidden under the stamp (now lifted); it is fully read below ("Under the stamp") and was re-checked on enlarged crops of the original on 2026-11-03. The names below are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark / 8 / open S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma / corner | t |
| long stroke + tick left | d | two strokes | n | plain bold X | u |
| three bars | e | crossed curve, no dot | o | chevron | v |
| upright cross | f | long stroke + tick right | h / p (one sign) | low descender | y |
| open hook with descender | g | crossed curve, dot | i | X with tail / crossed diagonal | z |
| inverted T | j | | | | |

Accents are small ticks over the sign (á, é, í, ó); two ticks give ö, ő or ü. This writer spells gy as separate g + y. Every choice between h and p rests on word sense, since they are one sign.

## Plaintext

Literal decipherment, row by row (square brackets mark letters restored under an overwrite or blot; the leading 8 of row 06 is the digit):

```text
01 szeretetedesjolan
02 kamneharagudjonhogy
03 ojritkanirókmert
04 nagyonelvagyok
05 foglalvameeste
06 8oraigdolgozok
07 mertaholdolgo
08 zoksürgősamun
09 kaésojkésőidegen
10 haznalnemle
11 hetojkesőnfel
12 lennimegmostnem
13 tud[o]kírnisemi
14 ujsakotmertcsak
15 szombatonegyezek
16 amesterrelhat
17 jolakaéknalmiuj
18 ságvasár[na]pbemegyek
19 pestremegnezemlatogatomapesti
20 eket
S1 istenve
S2 leavi
S3 szont
S4 latas
S5 igmely
S6 barso
S7 kalesz
```

Normalized Hungarian (word division, punctuation, most accents and spelling are editorial):

Szeretett édes Jolánkám! Ne haragudjon, hogy oly ritkán írok, mert nagyon el vagyok foglalva. Még este 8 óráig dolgozok, mert ahol dolgozok sürgős a munka, és oly késő; idegen háznál nem lehet oly későn fel lenni. Még most nem tudok írni semmi újságot, mert csak szombaton egyezek a mesterrel. Hát Jolá[n]káéknál mi újság? Vasárnap bemegyek Pestre, megnézem, látogatom a pestieket.

Under the stamp: Isten vele a viszontlátásig, mely bár soká lesz.

**English.** My beloved sweet Jolánka! Do not be angry that I write so rarely, for I am very busy. I work until 8 in the evening, because where I work the job is urgent, and it is so late; in a stranger's house one cannot stay up so late. I cannot yet write any news, because only on Saturday do I come to terms with the master. So what is new at Jolánka's family? On Sunday I am going in to Pest; I will look up and visit the people from Pest.

Under the stamp: God be with you until we meet again, though that will be long.

**Slovak.** Moja milovaná, sladká Jolánka! Nehnevajte sa, že píšem tak zriedka, ale som veľmi zaneprázdnený. Pracujem až do 8 hodiny večer, lebo tam, kde pracujem, je práca súrna, a je tak neskoro; v cudzom dome nemožno byť tak neskoro hore. Zatiaľ Vám neviem napísať nijaké novinky, lebo až v sobotu sa dohodnem s majstrom. Tak čo je nové u Jolánkiných? V nedeľu idem do Pešti, pozriem si a navštívim Peštianov.

Pod známkou: Boh s Vami, do videnia, hoci to bude ešte dlho.

## Uncertainties

1. **Rows 7–8, the d of "dolgozok".** It has its tick on the right, like h/p, while the five other d on the card have it on the left. d is a word-sense call for this one sign; the same anomaly occurs on HCP 1216 ("de"). The word itself is safe: it repeats "dolgozok" of row 6 and the clause is plain grammar.
2. **Row 6.** The first sign is a tall 8 with a long tail, shaped like the k sign but read as the digit from sense. The i of "óráig" shows no dot.
3. **Row 5, "me este".** Normalized "még este"; the g is not on the card (the same omission occurs on HCP 1216).
4. **Row 10.** A blot between z and n: deleted ("háznál", chosen) or a hidden á ("házánál"). The meaning is the same. The n of "nem" has a kinked first stroke, read by sense.
5. **Row 13, "tud[o]k".** The sign is overwritten; no o shape is visible. This is a true restoration from word sense.
6. **Row 18, "vasár[na]p".** A dark blot whose strokes fit an overwritten n + a; "vasárnap" makes the restoration safe.
7. **Writer's spellings normalized.** Row 14 "ujsakot" has k for g ("újságot"); row 17 "jolakaéknal" lacks the n ("Jolá[n]káéknál"; "Jolánkáék" occurs on HCP 1296). Also "szeretet", "oj", "semi", "nezem".
8. **"egyezek".** Taken as "I come to terms" with the master, presumably over pay or a post. The card does not say about what.
9. **"mely bár soká lesz".** The signs are clear, but "bár" leaves the sentence slightly hanging. The translation takes it as concessive; a wish sense, or a dropped "nem" ("which I wish would not be long"), is also possible.
10. **Sender line (plain script).** After Rákos Szent Mihály comes a word read only as "Emocn", then an overwritten word best fitting "Telep". Neither is resolved, and it is not clear whether they name a locality or a person. They belong to the address, not the message.
11. **Date and writer.** The card is undated, and "Feri" is an inference (see above).

## Review and what changed

An independent Claude Opus 5.5 reviewer ran the command, transcribed all 27 rows (337 tokens) from its own crops after seeing the solver's text, and decoded them with its own table; the two readings differed in one row. It confirmed that every sign fits the family classes and found no forced passage. Its verdict was **REVISE**. All findings were rechecked on the scan and addressed:

- **Rows 7–8 (major).** The first version read "[dol-] dolgozók [?]", a false start with an invented accent and no syntax. It is now "ahol dolgozok", needing the tick anomaly once instead of twice.
- **Row 16 (major).** The sign after r r has three bars, not two: a red-pixel profile shows three bands. The word is "mesterrel", and the claimed writer's slip does not exist.
- **Minor.** The false accent was removed, the acute on "ság" in row 18 was added to the ledger, and a miscount of the d signs was corrected. The sender line is now reported without guessed readings, and the alternative sense of "bár" is noted.

The rest of the reading did not change. The reviewer could not verify the date, the writer's identity, what lies under the blots in rows 10 and 13, or the two sender words.
