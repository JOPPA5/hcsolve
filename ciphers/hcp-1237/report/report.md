# HCP 1237: Feri to Jolánka Tóth, on the word "not interested", the cards and the end of mourning

Human solver: Tomáš Pavuk

**Status: complete reading. 426 of 427 written signs read; the last sign of the card is a blot. Independent review 1 verdict ACCEPT, with no change to any letter.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1237 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1237), portal name cpc_1912-06-30_HU__HU_Jasz Arokszalas_jolanka-26, from Tobias Schrödel's cryptographic postcard collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The portal links an article in the HistoCrypt proceedings as its reference. That article was not read, so this report cannot say whether it discusses this card. No published solution of this card was found or used.

The address is written in plain script: **Szép reményű Tóth Jolánka úrleánynak, Jász-Árokszállás** ("To Miss Jolánka Tóth, of fair hopes"). The last word is partly under the collection stamp. The date 1912-06-30 comes only from the portal file name, because the postmarks are not legible enough to confirm it.

The card belongs to the Hungarian postcards sent by a man who signs himself Feri to Jolánka Tóth. Several are deciphered in this repository (for example HCP 1216, 1212, 1213, 1217, 1218, 1243 and 1301). The picture side has only a printed poem, "Fecském hova szállsz?", and no handwriting. All the ciphertext is on the address side, in red ink: a block on the left, a long line along the whole bottom edge, and five short rows in the stamp area at the top right. Only a torn remnant of a stamp stays at the top of that box: the stamp was lifted, and the five rows were written in the box where it would have covered them, a hidden message in the cipher signs (re-checked 2026-11-03).

![Address side: cipher block on the left, the line along the bottom edge, five rows in the stamp area (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, printed poem only (source/picture-large.jpg)](../source/picture-large.jpg)

![The five rows in the stamp area; the last sign of the bottom row is the blot (work/crops/stamp.png)](../work/crops/stamp.png)

## Method

The key was **transferred unchanged** from the finished Jolánka cards, chiefly HCP 1216 and 1243. It is not a new key recovery, and no value was adapted to this card.

The transcription is **manual**, not OCR. The solver read all 28 rows sign by sign from enlarged crops of the high-resolution original scan and recorded one token per written sign, 427 in all (work/ledger.txt). A single command checks the SHA-256 of the images, decodes the ledger and prints the literal rows and the normalized text:

```text
python3 -I ciphers/hcp-1237/work/decode.py
```

Several first readings were corrected on the enlargements by rereading the shapes, never by changing the key: "szí" to "szó", "isze" to "össze-", "e" to the two-bar "a" in "a gyász", and "hoz" to "mozdu-" (three separate strokes). The word then continues on the next row as "-latja".

## Key

Monoalphabetic substitution with invented graphic signs; register type **MASC + Steganography** (2026-11-03), because part of the message (the five rows in the stamp area) was hidden under the stamp, which has since been lifted. The names below are conventional labels for handwritten shapes. Accents stand above the signs when they are written at all.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section / S mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three strokes | m | gamma | t |
| short + long stroke | d | two strokes | n | plain X | u, ü |
| three bars | e | hump loop, down tail | o, ö, ő | chevron | v |
| upright cross | f | long + short stroke | h / p | low curve | y |
| open loop, descender | g | crossed curve, long bar | i | crossed diagonal, tall stem | z |
| joined loop + descender | gy | inverted T | j | | |

On this card the stroke order separates d (short then long) from h/p (long then short). The letters h and p share one sign.

## Plaintext

Literal decipherment, row by row. An apostrophe marks an accent or dot seen on the card; [?] is the blot.

```text
01 kedvesjolankameso
02 rokkalege'szitemkiso
03 raime'desehigyjeelhogy
04 nagyonroszu'lesetez
05 aszo'neme'rdekli
06 pedighigyeeledesem
07 maganakmindenmozdu
08 latjaerdekelami
09 lapokatiletiaranem
10 lehetpanaszamerthet
11 elejenku'ldo'kketto't
12 esaharmadikatvalasz
13 ke'ntszoktamkuldeni
14 e'shakesonkapomso
15 raitnkoregykicsito'sze
16 jo'ne'smiti'rjakoly
17 su'ru'nanakigazano'rulo'k
18 hogyletelikagyasz
19 igazanmilygyorsan
20 elteltezido'mint
21 hamostletvolnaezelbezaromsoraim
22 maradosirihukedvesse
23 feri
stamp area: u'dvoz | loma | tavol | bolhu | kedve[?]
```

**Hungarian (normalized):**

Kedves Jolánkám! E sorokkal egészítem ki soraim, édese[m]. Higgye el, hogy nagyon rosszul esett ez a szó: „nem érdekli”, pedig higgye el, édesem, magának minden mozdulatja érdekel. Ami lapokat illeti, arra nem lehet panasza, mert hét elején küldök kettőt, és a harmadikat válaszként szoktam küldeni, és ha későn kapom sorait, [a]‹n›kor egy kicsit összejön, és mit írjak oly sűrűn. Annak igazán örülök, hogy letelik a gyász. Igazán, mily gyorsan eltelt ez idő, mintha most lett volna. Ezzel bezárom soraim, maradok sírig hű kedvese, Feri.

In the stamp area: Üdvözlöm a távolból. Hű kedves[e].

Square brackets are supplied letters; ‹n› means the card has n where "akkor" needs k.

**English:**

Dear Jolánka! With these lines I complete my lines, my sweet. Believe me, this word hurt me very much: "does not interest you", when, believe me, my darling, your every movement interests me. As for the cards, you can have no complaint on that score, because at the start of the week I send two, and the third I usually send as a reply, and if I get your lines late, then they pile up a little, and what should I write so often? I am truly glad that the mourning is coming to an end. Truly, how quickly this time has passed, as if it were only now. With this I close my lines; I remain, faithful to the grave, your sweetheart, Feri.

In the stamp area: I greet you from afar. Your faithful sweetheart.

**Slovak:**

Milá Jolánka! Týmito riadkami dopĺňam svoje riadky, drahá. Verte mi, že veľmi ma zabolelo toto slovo: „nezaujíma Vás”, a pritom mi verte, moja milá, že ma zaujíma každý Váš pohyb. Čo sa týka pohľadníc, na to sa nemôžete sťažovať, lebo na začiatku týždňa posielam dve a tretiu zvyčajne posielam ako odpoveď, a keď Vaše riadky dostanem neskoro, tak sa to trochu nazbiera, a čo mám písať tak často? Naozaj sa teším, že sa končí smútok. Naozaj, ako rýchlo prešiel tento čas, akoby to bolo len teraz. Týmto končím svoje riadky, ostávam až do hrobu Váš verný milý, Feri.

V mieste známky: Pozdravujem Vás z diaľky. Váš verný milý.

## What remains uncertain

Two places are genuinely unclear, each a single word, and the clause around each reads.

1. **Row 15, "nkor".** The signs are two strokes (set under the arm of the preceding gamma), k, o, r. It is normalized as "akkor": the a is not on the card and the writer has n for the first k. This is the weakest word of the text. The sentence needs "then", and no other word fits.
2. **Stamp area, last sign.** "kedve" is clear. The last sign is a pale smeared X-like form where s is expected, and "kedves[e]" is a restoration from the same phrase in row 22.

Letters that rest on word sense rather than on the sign alone:

3. **h/p.** p is chosen by sense in "pedig" (row 6), "lapokat" (9), "panasza" (10) and "kapom" (14).
4. **Blotted signs.** The final u of "mozdu-" (row 7), the j of "elején" (11), the k of "kapom" (14), the y part of "gyorsan" (19) and the z of "ez" (20) are over-inked. The remaining shape in each case is compatible and the word decides.
5. **Row 15–16, "osze jon".** This is normalized "összejön" ("piles up") with a single s written. The marks over both o signs support ö. The meaning in context is an interpretation of a loose colloquial sentence.
6. **Row 5.** "Nem érdekli" is taken as a quotation from her letter, but the card has no punctuation. The letters are clear; who was "not interested" in what is inferred.
7. **Mourning.** "Gyász" reads clearly, but the card does not say whose mourning is meant.
8. **Writer's spellings normalized.** roszul, eset (esett), ilet, ara, anak, marado siri (maradok sírig, k and g omitted), hu (hű), kedvesse (kedvese), ezel (ezzel), letvolna (lett volna), sürün (sűrűn), higyjeel and higyeel (higgye el; the spurious j is also on HCP 1216), édese (final m supplied). Most accents are not written and are supplied.

## Why the reading is believed

The key, taken unchanged from other cards, turns every sign in all rows into continuous Hungarian in the formal "maga" register. Repeated forms decode identically (hogy, igazán twice, higgye el twice, soraim, édesem, küld- twice). The text answers a specific complaint in her letter, and the closing "sírig hű kedvese, Feri" is the formula of HCP 1216.

## Review and what changed

An independent Claude Opus 5.5 reviewer tried to refute the reading. It made its own crops and its own transcription of all 28 rows in shape symbols (not blind, since the claimed text was known), and decoded them with its own script. The result differs from the ledger only in the four disclosed h/p calls. It checked the difficult signs on 3–4x enlargements, the whole card including the picture side, and the language. Verdict: **ACCEPT**.

Four minor findings were fixed, with no change to any letter:

1. Three visible accents were missing from the ledger: the marks over the o of "osze" and "jon" and over the e of "es". They were confirmed on new crops and added, and they are direct evidence for the ö of "összejön".
2. The normalization eset to esett was added to the disclosed list.
3. The notation [a]‹n›kor now shows the n to k correction at the word itself.
4. "Over the stamp" became "in the stamp area", because no stamp remains over these rows.

The reviewer could not verify the date, because the postmarks are not legible, and did not read the HistoCrypt article linked from the portal.
