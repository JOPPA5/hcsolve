# HCP 1259 (cpc_1912-04-04_HU__HU_Jasz Arokszalas_jolanka-14): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: enciphered text read in full (18 rows); one illegible word-length line in the plain stamp-box text stays unread. Independent review 1 verdict REVISE; all findings addressed, no change to the sense of the text. Type MASC + Steganography.** Report dated 2026-11-01, stamp-box section added 2026-11-03.

## Origin and context

The cryptogram is record 1259 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1259), portal name cpc_1912-04-04_HU__HU_Jasz Arokszalas_jolanka-14, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the catalogue listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language unknown, recipient Tóth Jolánka, with no transcription or solution attached. The portal's detail page timed out during capture, so that statement rests on the catalogue row. No published solution was found and no earlier work on this number exists in this repository.

The picture side shows a couple with a mandolin, with a printed verse headed Szerenád. Ábránd. and series number 2317. It carries no cipher. The whole message is on the address side, in red ink: 18 rows of invented signs on the left half, with a few syllables in ordinary cursive inside them. The closing in the stamp box and the address are plain cursive.

The clear postmark reads …ÁROKSZÁ… / 91 ÁPR 4, with no 2 printed in the year. A second cancel over the stamp box shows 912 ÁP, but only a final S of its place name is legible. Together with the portal file name, this gives 4 April 1912.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the plain address and the stamp box (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards from Feri to Jolánka Tóth in Jászárokszállás, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery.

## Method

The transcription is **manual**, made sign by sign on enlarged crops of the un-converted high-resolution scan (work/hires/), with no OCR. It was not blind, because the key was known beforehand. Each written sign is one token in the ledger work/ledger.txt, and each token that rests on word sense rather than on the sign alone is flagged. The command `python3 -I ciphers/hcp-1259/work/decode.py` checks the hashes of the four image files, decodes the ledger with the key and prints the literal and normalized text.

In review a separate agent made its own crops, its own 18-row transcription in its own notation and its own sign table (review/work/my_decode.py). Over 267 letters it found one difference, in the form of one sign in row 11 (see below).

## Key

**Cipher type: MASC + Steganography** (updated 2026-11-03). Simple monoalphabetic substitution with invented graphic signs. The labels are conventional names for handwritten shapes. The plain closing is hidden in the stamp box, under the stamp.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark or S shape | k | F-like | r |
| six | b | wave | l | right bowl | s |
| short + long stroke | d | three short strokes | m | gamma | t |
| three bars | e | two short strokes | n | plain cross | u |
| open loop with descender | g | cursive loop | o | chevron | v |
| tall stroke + tick | h / p | dotted crossed curve | i | crossed curve, no dot | y |
| inverted T | j | joined cursive gy | gy | crossed diagonal with tail | z |

The h/p sign is a near-homograph family feature: one sign serves both letters. The sequence sz is written right bowl + z. In legyen and nagyon the writer drops into ordinary cursive for the rest of the syllable. Letters c and f do not occur. A dot beneath k on rows 1, 3 and 13 seems to belong to the sign.

Two local variants differ from the family legend. The y here is the crossed curve without a dot, not a low descender, so it may be an i with the dot left off. The h in láthat has the d shape.

## Plaintext

Literal decipherment. UPPERCASE is ordinary cursive; {x} is a blotted, overlapped, pale or off-form sign whose value rests on word sense; {i/o} is a hidden sign, either letter; [..] is struck through by the writer; h stands for the h/p sign.

```text
01 kedvesjolankam
02 remélemhogyelég
03 joltelnekórái
04 edesemlegyENel
05 nézesel[nezese]ilo
06 naylonaira{n}dena
07 gyONsokdolgavan
08 {h}igyeelédesem
09 {i/o}jzavarosirás
10 {m}intitvanamit
11 lat{h}atsoraimza
12 varosirásábol
13 {m}erszetakartamteh
14 {n}i.edesemir{j}onhon
15 {h}ogymiujsag{h}ogy
16 {r}{a}{g}odnakrajtamarosz
17 {n}y{e}lvek.istenvela
18 viszontlatasra
```

**Hungarian (normalized):** Kedves Jolánkám! Remélem, hogy elég jól telnek órái. Édesem, legyen elnézéssel Ilona irán[t], de nagyon sok dolga van, higgye el, édesem. [I/O]ly zavaros írás, mint itt van, amit láthat soraim zavaros írásából, mer[t] szét akartam tépni. Édesem, írjon hon[n], hogy mi újság, hogy rágódnak rajtam a rossz nyelvek. Isten vel[e], a viszontlátásra.

Stamp box (plain): [one illegible line, unread] Csókolo[m] számtalanszor. Sírig hű kedves[e], Feri.

Address (plain): Szépremény[ű] Tóth Jolánka úrleánynak, Jászárokszállás.

**English:** Dear Jolánka! I hope your hours are passing quite well. My darling, be indulgent towards Ilona, but she has a great deal to do, believe me, my darling. Such muddled writing as there is here, which you can see from the muddled writing of my lines, because I meant to tear it up. My darling, write from home what the news is, how the evil tongues are chewing on me. Farewell, until we meet again.

Stamp box: [one illegible line, unread] I kiss you countless times. Your sweetheart, faithful unto the grave, Feri.

Address: To the promising Miss Jolánka Tóth, Jászárokszállás.

**Slovak:** Milá Jolánka! Dúfam, že Vaše hodiny plynú celkom dobre. Drahá, buďte zhovievavá voči Ilone, ale má veľmi veľa práce, verte mi, drahá. Také zmätené písmo, ako je tu, čo môžete vidieť zo zmäteného písma mojich riadkov, lebo som to chcel roztrhať. Drahá, napíšte z domu, čo je nové, ako ma ohovárajú zlé jazyky. S Bohom, dovidenia.

V poli pre známku: [jeden nečitateľný riadok, neprečítaný] Bozkávam Vás nespočetnekrát. Váš do hrobu verný milý, Feri.

Adresa: Nádejnej slečne Jolánke Tóthovej, Jászárokszállás.

### Stamp-box message

Added 2026-11-03 after a stamp-box audit. The closing lines lie inside the dotted frame of the stamp box, on bare paper beside the printed P.R.A. wreath. The second cancel stops at the frame, so the stamp was on the card when it was cancelled and these lines were hidden under it; the stamp has since been lifted. The lines are plain Hungarian cursive, not cipher: "[illegible line] / csokolo / számta / lanszor / sirig hű / kedves / Feri", that is **Csókolo[m] számtalanszor. Sírig hű kedves[e], Feri** ("I kiss you countless times. Your sweetheart, faithful unto the grave, Feri"; Slovak "Bozkávam Vás nespočetnekrát. Váš do hrobu verný milý, Feri"). The top line, about one word, stays unread. This hidden placing is why the card is typed MASC + Steganography.

![The stamp box at 2x, with the plain closing under the lifted stamp (work/stamp-2026-11-03/stamp_box_2x.jpg)](../work/stamp-2026-11-03/stamp_box_2x.jpg)

## What remains uncertain

- **Stamp box, top line.** About one word long, an illegible pink mass partly outside the box, not read. Whether it was deleted on purpose or smeared cannot be told. Below it, final letters of csókolo[m] and kedves[e] are not visible.
- **Row 9, first sign.** A blot hides it. Ily and oly ("such") are both open, with the same meaning. A mark above the blot may be an i dot, but it is about twice the usual size.
- **Rows 5–6, ilo|na ylona.** The writer struck a repeated nézése, wrote ilo, broke the row, and wrote na and ylona. This is read as a repeated Ilona. Who she is cannot be said from this card; the name also occurs on other cards of the family.
- **Row 6, irán[t].** The two pale strokes are read as n by word sense, and no t is visible. A slip for írna ("[Ilona] would write") is another possibility and would change that clause.
- **Row 13–14, tépni.** The sign is taken as p, and the blotted first sign of row 14 as n, on word sense alone.
- **Blotted signs read by the word:** mint (row 10 m), mer (row 13 m), írjon (row 14 j), both hogy of row 15, nyelvek (row 17 n and e). The g of rágódnak (row 16) could be k by shape; this word rests on sense more than the others do.
- **Off-form h.** In láthat (row 11) the sign has the d shape, and the first sign of row 8 is not a clean h. Both rest on the word.
- **Row 17 end.** The last sign is literally a. It is read as the article of the family's closing Isten vele, a viszontlátásra, with the e of vele left out by the writer.
- **Row 14, hon.** Normalized hon[n]; "from home" is by sense.
- **Sense.** Rows 9–13 are clumsy as a sentence, though the remark matches a card with a struck line and many blots. Rágódnak rajtam is taken as gossip about the writer; the exact shade is an interpretation.
- **Accents.** Marks between rows are mostly real accents or i dots of the row below. Written ones are shown in the literal text; the others are supplied. The dot after nyelvek may be a full stop or part of the k.
- **Portal capture.** The detail page was not read tab by tab. The address word Szépremény[ű] ends at paper damage, and the ű is restored.

## Review and what changed

Independent review 1 tried to refute the reading and could not: the reproduction command and hashes passed, the independent transcription agreed, and the language and closing formulas fit the family. The verdict was REVISE, with nine minor findings. All were accepted after rechecking on the pixels:

1. The end of row 17 changed from a forced vele to vel[e], a, keeping the sign as written.
2. The first letter of row 9 changed from a restored oly to open ily/oly, and the mark above the blot is now reported.
3. The d-shaped h in láthat and the off-form sign of row 8 are now disclosed.
4. The word-sense flag was applied consistently across the ledger, adding rows 6, 8, 10, 11, 13, 14, 15, 16 and 17.
5. The description of accents and dots was corrected, and accents were added to the ledger.
6. The address word became Szépremény[ű].
7. The postmark statement was corrected.
8. The top stamp line is now called illegible, not scribbled over.
9. The y variant and the picture side are now stated.

No words of the English or Slovak translation changed except the description of that stamp line.
