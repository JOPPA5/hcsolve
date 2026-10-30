# HCP 1315 (cpc_1914--_HU__HU_Jasz Arokszalas_jolanka-119): Feri to Jolánka Tóth, a rainy Sunday apart

Human solver: Tomáš Pavuk

**Status: deciphered in full (392 written signs in 21 main rows and 8 stamp-corner rows, with a few weak or restored signs listed below); independent review 1 verdict REVISE, all findings addressed, one wrongly entered sign removed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1315 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1315), part of Tobias Schrödel's collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, date and language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution was met.

It is a tinted photographic greeting card headed **A szerelem hőmérője** ("The thermometer of love"), showing a couple in a heart-shaped frame and a printed thermometer. The printed verse says roughly that when she cast her lovely eyes on him, it at once turned warm by a number of degrees.

The address side is in plain writing: Szépreményű (spelled Szepremenjü, "Of fair hope", a fond form of address), then **Tóth Jolánka**, one hard-to-read word, **Budapest, István út 5**, and further figures. The postmark shows BUD… and a year ending 914, so 1914 is the likely date; no full date could be read. The portal's file name says Jász-Árokszállás, while this card is addressed to Budapest, and the card does not explain why.

The rest of the address side is filled with cipher: 19 rows at the left, two rows along the bottom edge, and eight tiny rows in the corner under the stamp, which has been torn off. Hiding a closing message under the stamp is a habit of this family of cards.

The card belongs to the "Jolánka" family of cipher postcards, love letters from Feri to Jolánka Tóth, in Hungarian, in the same hand and the same cipher. The key was taken from finished sister cards (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301) and not invented here. No earlier work on this number exists in this repository.

![Picture side as scanned, turned sideways: "A szerelem hőmérője" (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned; the cipher fills the left part and the bottom edge, the plain address is at the right (source/address-large.jpg)](../source/address-large.jpg)

![Stamp corner enlarged: eight cipher rows under the missing stamp, overprinted by the triangle mark](stamp-corner.jpg)

## Method

The transcription is **manual**. The solver read every row from 2.5× to 8× crops of the un-converted original scan, without OCR, and wrote one token per written sign into a ledger. It was read with the key and the sense in view, so it is not a blind transcription. A red-channel stretch separated the ink from the printed triangle in the stamp corner better than other filters. Rows 8 and 20–21 needed care: row 8 begins with the plain time ½ 9, and the word maradok runs over the end of row 20 into row 21.

The key decoded all rows into continuous Hungarian with no unassigned sign; no key value was fitted to this card. A short script checks the hashes of the images, decodes the ledger, and prints the result. From the repository root:

```text
python3 -I ciphers/hcp-1315/work/decode_opus.py
```

The reviewer read the card separately from its own crops, wrote the rows as sign classes and decoded them with its own script. That reading was not blind either, as the reviewer had read the solution first. It agreed in everything except one sign (see Review).

## Key

Simple monoalphabetic substitution with invented graphic signs. The labels are conventional names for handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section sign (S/5-shaped) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| short stroke, then long stroke | d | three short strokes | m | gamma/corner | t |
| three bars | e | two short strokes | n | plain cross x | u |
| upright cross + | f | cursive loop | o | chevron | v |
| left bowl with descender | g | long stroke, then short stroke | h / p | low descender loop | y |
| dotted crossed curve | i | inverted T | j | crossed diagonal with long arm | z |
| opposed bowls joined | cs | | | | |

Dots over the x give ü, and a double stroke over the loop gives ő. On this card gy is written as two signs, g + y. Two card-specific forms: tt in attól (row 11) is one joined sign, gamma linked to gamma; and the n at the end of egyetlen (row 2) has its two strokes joined by a top bar. The digits ½ and 9 are in clear.

## Plaintext

Literal decipherment, row by row. `?` marks a weak sign, `{a|e}` a sign whose bars cannot all be seen, `[s]` a sign hidden on the tear or the triangle and restored.

```text
01 szeretetedesjolank?a?m      12 agong?oktolhogy
02 edesegyetl?enremenyem       13 nemtőlthetem
03 kivanomhogyalegjob          14 magavaleztvasar
04 kedvebentalaljaso           15 napotigazhogy
05 raimhogymulatot             16 nemalegjobbido
06 vasarnapremelem             17 voltdeaszobab{a|e}
07 j?olamieng?emilet           18 nemesikazesső
08 ½9korjotemhaza              19 mostma?rtobbet
09 eslefeküdtemes              20 nemirokezelbezaromsoraimma
10 aludtamazalvas              21 radoksihüimadojaferimajdszerdan
11 megmentetattol

Stamp corner:
s1 istenve      s5 csok?o?l?
s2 l?eedesem    s6 [s]zer{a|e}
s3 [s]zamta     s7 tokedve
s4 lan[s]zor?   s8 s{a|e}nf?eri
```

Normalized Hungarian; [x] = supplied or restored by the editor, ⟨x⟩ = written on the card and removed by the editor:

Szeretet[t] édes Jolánkám! Édes egyetlen reményem! Kívánom, hogy a legjob[b] kedvében találja soraim[at]. Hogy mulat[t]ott vasárnap? Remélem, jól. Ami engem il[l]et, ½9-kor jöt[t]em haza, és lefeküdtem, és aludtam. Az alvás megmentet[t] attól a gon[d]októl, hogy nem tölthetem magával ezt [a] vasárnapot. Igaz, hogy nem a legjob[b] idő volt, de a szobába nem esik az es⟨s⟩ő. Most már többet nem írok, ez[z]el bezárom soraim[at], maradok sí[rig] hű imádója, Feri. Majd szerdán.

Stamp corner: Isten vele, édesem! [S]zámtalan[s]zor csókol [s]zerető kedvese⟨n⟩ Feri.

## English translation

My beloved sweet Jolánka! My sweet, only hope! I wish that my lines may find you in the best of spirits. How did you enjoy yourself on Sunday? Well, I hope. As for me, I came home at half past eight [8:30], went to bed and slept. Sleep saved me from the worries that I cannot spend this Sunday with you. True, it was not the best weather, but in the room it does not rain. I will not write more now; with this I close my lines and remain, faithful unto the grave, your adorer, Feri. Until Wednesday, then.

Stamp corner: God be with you, my darling! Your loving sweetheart kisses you countless times, Feri.

## Slovak translation

Moja milovaná sladká Jolánka! Moja sladká jediná nádej! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Ako ste sa zabavili v nedeľu? Dúfam, že dobre. Čo sa mňa týka, prišiel som domov o pol deviatej, ľahol som si a spal som. Spánok ma uchránil pred starosťami, že túto nedeľu nemôžem stráviť s Vami. Pravda, nebolo najlepšie počasie, ale do izby nezaprší. Teraz už viac nepíšem, týmto končím svoje riadky a zostávam Váš do hrobu verný ctiteľ, Feri. Teda v stredu.

V rohu pod známkou: S Bohom, drahá moja! Nespočetnekrát Vás bozkáva Váš milujúci milý, Feri.

## What remains uncertain

- **h against p** is one sign and rests on word sense only (hogy, haza, tölthetem, hű against vasárnap). d is separate from h/p by stroke order.
- **Row 1 k a, row 2 l:** in a wet smear and a stain; the words decide them.
- **Row 7:** the first sign (j of jól) is overinked and apparently corrected, and the g of engem is retraced. Both are taken from context.
- **Row 12:** the card has the g sign, giving gongoktól, which is no word. It is taken as a slip for gondoktól. Attól a gondoktól is also slightly ungrammatical and is translated by sense.
- **Row 14:** the card has ezt vasárnapot; the article a is supplied by the editor.
- **Row 17 and row 19:** the last sign of szobába has a printed line through it, so a third bar cannot be excluded; the a of már is blotted.
- **Row 21 si hü:** only s, i, h, ü are written. Sí[rig] hű is an expansion from the family formula sírig hű, and "faithful unto the grave" depends on it.
- **Majd szerdán:** elliptic. It could mean "[I will write or come] on Wednesday"; the card does not say which.
- **Stamp corner:** this is the weakest part. The three s in számtalanszor and szerető are restored from the words, and the l of vele, the r of -szor and k, o, l of csókol are blotted or lie on the printed triangle. In s8 two clear strokes n stand before the blot read as f; they may be a slip or the adverb kedvesen, or n + f may be m + f, giving kedvesem, which fits less well after csókol. The final i is only partly visible.
- **Spelling and accents:** the writer's single consonants (legjob, mulatot, ilet, jotem) are normalized as marked above. soraim stands for soraimat, as is usual in this family. tőlthetem is normalized to tölthetem and ido to idő. Accents á, é, í, ó are mostly not visible and are supplied.
- **Date and place:** no full date; only "914" on the postmark. One word of the address remains unread.

## Why the reading is believed correct

The key comes unchanged from reviewed sister cards and turns all the rows into continuous Hungarian. Repeated words decode identically: hogy four times, nem four times, édes three times, vasárnap, soraim, legjob and Feri twice each. The formulas match the family: Remélem, jól. Ami engem illet (HCP 1301, the closest parallel), kedvében találja soraim and Hogy mulatott vasárnap? (HCP 1217), Ezzel bezárom soraim (HCP 1218, 1306, 1308, 1310), szerető kedvese Feri (HCP 1306), számtalanszor csókol … Feri in the stamp corner (HCP 1212). The sense runs from sentence to sentence, and details such as the plain ½ 9 and the joke about the rain in the room are not what forcing words onto noise would produce.

## Review and what changed

One independent review was done by a separate Claude Opus 5.5 agent; verdict **REVISE**. It re-ran the command and confirmed the output, compared its own reading with the ledger, and checked the key against the family tables. There were no blockers.

- **Major:** in row 14 the solver had entered an a between ezt and vasárnapot that is not on the card; it had been supplied from the grammar. The sign was removed (393 → 392 signs), and the article is now shown as an editor's addition. Translations did not change.
- **Minor, description of the key:** d and h/p are now separated by stroke order; only h against p rests on sense. The joined tt and the barred n are described.
- **Minor, disclosure:** weak signs in rows 1 and 2 and in the stamp corner are now marked; the kedvesem alternative in s8 is listed; every deletion and addition in the normalized text is marked.
- **Minor, evidence:** word counts were corrected (hogy ×4, édes ×3), and wrong citations of parallels were replaced by the cards that really have them.

No word of the reading and no translation changed. The reviewer could not prove the three restored s or the h/p choices from the pixels, nor rule out a reading bias shared with the solver, as neither transcription was blind.
