# HCP 1284 (jolanka-74): Feri writes to Jolánka Tóth from Szentjakab

Human solver: Tomáš Pavuk

**Status: deciphered with one small unresolved residue in row 17 (a letter i and a stroke); independent review 1 verdict REVISE, findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1284 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1284), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-74, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution was seen.

The picture side shows a young woman with a book and, in a vignette, an embracing couple. It has a printed four-line Hungarian verse, Magácskánál mulat / Minden gondolatom . . . / Mennyire szeretem, / Azt ki sem mondhatom ("With you my every thought lingers; how much I love you I cannot even say"), and a publisher's mark with the number 2523. The verse is printed and is not part of the message.

The address side is in plain writing: Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás ("To Miss Jolánka Tóth, of fair promise, Jászárokszállás"). At the lower right, partly under the HC Portal collection stamp, is a plain note Kelt 2 1 ?ra este ("written ... in the evening"), whose number and following word are not settled. The cipher text fills the left half in eighteen rows, in red ink, with four more rows in the box meant for the stamp. The word kocsin ("by cart") is inserted above row 14 in ordinary Latin script. The postmarks are faint: the left one shows only fragments (at least ÁSZ and a numeral 2), so the card is undated here.

The card belongs to the family of cipher postcards from Feri to Jolánka Tóth, several of which are finished in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). The family key was transferred unchanged from HCP 1216. This is therefore a reading with a **known, transferred key**, not a new key recovery. No plaintext was taken from the sister cards.

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, turned sideways in the scan, with the printed verse (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is **manual**. The solver read every sign from enlargements of the high-resolution address scan, and recorded each row in a ledger (work/ledger.txt), one token per written sign. No OCR was used. The key was then used as a known table. The command below verifies the hashes of the images and prints the ledger and the normalized text; it does not read pixels.

```sh
python3 -I ciphers/hcp-1284/work/decode.py
```

The family has known near-homographs, chiefly h/p and d/n. Where these were decided by the word and not by the shape, the uncertainties below say so.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs, with the closing hidden in the stamp box under the stamp (register label MASC + Steganography; updated 2026-11-03, was MASC):

| Plain | Sign | Plain | Sign |
|---|---|---|---|
| a | two bars | l | wave |
| b | six | m | three strokes, the first often ticked |
| c, cs | bowls | n | two strokes |
| d | long and short stroke, here also short and long | o | cursive loop |
| e | three bars | r | F-like |
| f | upright or tilted cross | s | right bowl |
| g | loop with descender | t | gamma |
| gy | joined loop | u | plain cross |
| h, p | tall stroke with short stroke | v | chevron |
| i | dotted crossed curve | z | crossed diagonal with curled top |
| j | inverted T | ö, ü | o, u with dots |
| k | S-shape | | |

Accents are mostly unmarked. The figures "4 ½" in row 13 are clear numerals.

## Plaintext

Literal decipherment, row by row. `{#}` is a heavy cancelled sign; `{p:d}` a d shape read p; `{R}` a gamma read r; `{m?}` three strokes with an arc; `{s?}` an overwritten loop read s; `{|}` an isolated stroke; `{n-}` n under a thin bar; `{-}` a hyphen.

```text
01 szeretetedesjolan            10 etanyafalutol
02 kambecsessorait              11 feloraja{R}asnyira
03 megka{p:d}tamigazan          12 esgyöngyöstol
04 örülökhogymeg                13 {#}pedig41/2orajara{s?}{-}
05 {#}egyszerolvashat           14 ra[kocsin]vanezazelet
06 tamsoraitahoszu              15 nemojonminöne
07 tavolletalat                 16 edesjolankama
08 mamarszentjakab              17 tanyani{|}{n-}emeszünk
09 roiromsorai{m?}              18 föteteltistenveleedesem
stamp box: csokolom / szamta / lanszo / feri + r
```

**Hungarian (normalized):** Szeretet[t] édes Jolánkám! Becses sorait megkaptam. Igazán örülök, hogy még egyszer olvashattam sorait a hosszú távollét alat[t]. Ma már Szentjakabró[l] írom soraim. E tanya falutól félórajárásnyira és Gyöngyöstől pedig 4½ órajárásra kocsin van. Ez az élet nem ojon, min[t] öné, édes Jolánkám. A tanyán {i + stroke, unresolved} nem eszünk főt[t] ételt. Isten vele, édesem. Under the stamp: Csókolom számtalanszor. Feri.

**English:** My dear sweet Jolánka! I have received your esteemed lines. I am truly glad that I could read your lines once more during the long absence. Today I am already writing my lines from Szentjakab. This farmstead is half an hour's walk from the village and 4½ hours by cart from Gyöngyös. This life is not like yours, my sweet Jolánka. On the farmstead we do not eat cooked food. Farewell, my darling. Under the stamp: I kiss you countless times. Feri.

**Slovak:** Moja drahá sladká Jolánka! Vaše vzácne riadky som dostal. Naozaj sa teším, že som si počas dlhej neprítomnosti mohol ešte raz prečítať Vaše riadky. Dnes už píšem svoje riadky zo Szentjakabu. Tento salaš je pol hodiny chôdze od dediny a od Gyöngyösu 4½ hodiny vozom. Tento život nie je taký ako Váš, moja sladká Jolánka. Na salaši nejeme varené jedlo. Zbohom, moja drahá. Pod známkou: Bozkávam Vás nesčíselne veľakrát. Feri.

## What remains uncertain

![Row 17, middle: dotted i, stroke, pair under a thin bar, e, three strokes with a ticked first stroke, then the e of eszünk (review/work/crops/r17mid.png)](../review/work/crops/r17mid.png)

1. **Row 17.** After tanyán stand a dotted i and a stroke with no established value, and a thin bar over the next pair is unexplained. The pair, e and the three strokes give nem. If stroke and pair were instead one m, the text would be imem eszünk, which is no word; the pixels alone do not exclude that division, so the negation rests partly on word sense. It does fit the sentence before it.
2. **Values fixed by word sense.** Row 13 sign before the hyphen, shaped like a retraced o with no s form visible, read s for órajárás-ra. Row 11, a gamma read r in járás, and a very Z-like final sign read a. Row 3, a d shape read p in megkaptam. Other h/p calls (hogy, olvashat, hoszu, pedig) likewise.
3. **Cancelled signs.** The first signs of rows 5 and 13 are heavy retraced crosses, treated as false starts of no value.
4. **Row 9, last sign:** three strokes with an arc, read m (soraim), possibly corrected from or to t.
5. **Row 18, first word:** a tilted cross read f; the ő's long arm could be a separate s (főst), which makes no sense.
6. **Writer's spellings.** ojon for olyan, min for mint, ro for ról, hoszu, alat, főt, szeretet. The second l in távollét is close to the chevron.
7. **Stamp box.** The final o of -szo is a doodled loop and the r a tilted F at the end of the name row; számtalanszor rests on sense and the family's closing formula.
8. **Szentjakab** is taken as a place name. A Szentjakab in Heves county appears in the Hungaricana urbarial listing (https://archives.hungaricana.hu/en/urberi/heves-szentjakab), but it has not been established that this is the same place. The date is unknown.

## Why the reading is credible

The key was not fitted to this card. It turns every row into Hungarian with the family's formulas (Isten vele, Csókolom számtalanszor, signature Feri), and also gives new content that no sister card supplied: Szentjakab, félórajárásnyira, Gyöngyöstől and the numerals 4½, with the writer's own Latin insertion kocsin falling exactly where the sentence needs it.

## Review summary

An independent Claude Opus 5.5 reviewer ran the command, made its own sign-class transcription of 292 tokens from 3x to 5x crops (having already seen the solver's ledger, so not blind) and decoded it with the family table. 18 of 22 rows were identical, and every sign mapped through the key with no new values. The verdict was REVISE, with five findings:

1. **Row 17 (major).** The solver had left the word before eszünk unread, so the polarity was unknown. The last group is an ordinary m, giving **nem eszünk**. Adopted.
2. **Row 10 (major).** E tanyafalutól was wrongly divided. **E tanya falutól** gives the sentence its subject and reverses the earlier English. Adopted; the letters did not change.
3. **Row 3 (minor).** The sign in megkaptam is literally a d shape. Now stated in the ledger.
4. **Word-sense claims (minor).** A statement that one reading was the only restoration was too strong; corrected.
5. **Side material (minor).** The verse, the publisher's mark and the postmark attempt were added.

The reviewer could not verify the date, the identity of Szentjakab, the meaning of the bar in row 17 or the residue i + stroke.

## Credits

Source capture, transcription, key transfer and decipherment: Claude Opus 5.5. The key comes from the finished Jolánka family cards, on which earlier work was done by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) and Claude Opus 5.5. Independent review: a separate Claude Opus 5.5 agent.

## Sources

Portal record: https://crypto.hcportal.eu/dashboard/cryptograms/1284. Image URLs and hashes are in SOURCES.md. Key: ciphers/hcp-1216/SOLUTION.md.
