# HCP1306: Feri to Jolánka Tóth, a refused quarrel by postcard (PARTIAL)

**Status: PARTIAL. Every visible sign is transcribed and decoded to letters, but several passages do not yet resolve into words. Not handed to review (no DONE1).** Claude Opus 5.5, 2026-10-30. No earlier work on this number exists; the portal shows Not solved with no attached solution. No external plaintext was used.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented signs: the Jolánka postcard family, same key as finished cards hcp-1216, 1212, 1213, 1217, 1218, 1243, 1301. See the table in `ciphers/hcp-1216/SOLUTION.md` and the token legend at the head of `work/ledger.txt`. Variants on this card: k is a short hook or section mark; a single stroke is a reduced d or h; dots of i often absent.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1306/work/decode.py
```

Checks the SHA-256 of the four images, decodes `work/ledger.txt` (635 signs, a manual reading, not OCR and not blind to the family key), prints the literal letters row by row, then the normalized text.

## Literal decipherment

```
01 szeretetedesjolankam              14 kormegyekmertmeg
02 mosthedigvalaszolok               15 akorsemnettemmosor
03 sorairaireoj{o|ö}romel            16 biztosnakondotam
04 {o|i}r/eknetlahirisegysze         17 arakeremedesemhaigazan
05 rehenegehamarabkime               18 szerethagyjonfelaval
06 rülazirnivalommint                19 atolakodovetejtar
07 meganekedesemhamagamon            20 {o|s}almotremelesmegistette
08 domtcsakszovala{k|g}armeg         21 esnemmeltattavalaszre
09 mon/aniamiojne/ezen               22 soraitamiabözsitileti
10 megymertnagyrabszol               23 igazansajnalomhogyenn{y|i}i
11 gavagyoknemrendel                 24 rejutovajobaratsagezt
12 kezemmagamfelettob                25 nemgondoltamamialitaszkilahjatiletiszeretnem
13 betnemiromhogymo                  26 latniesszeretnemenelinteznhatebizatamelahi
R1 ezelbezeromsoraimharahikok        (inner right edge, reading upward)
R2 szeretikedveseferi                (outer right edge, reading upward)
S1-S7 lhn? / iszont / atasig / udvozli / szere / toked / veseferi   (stamp area)
```

## Hungarian (normalized, partial; square brackets mark unresolved text)

Szeretett édes Jolánkám! Most pedig válaszolok soraira. [ire oj örömel(?) … írdék net lahiris egyszere henege] hamarabb kimerül az írnivalóm, mint magának, édesem, ha magam mondom. Csak szóval akar[om] megmondani, ami oly nehezen megy, mert nagy rabszolga vagyok, nem rendelkezem magam felett. Többet nem írom, hogy m[i]kor megyek, mert még akkor sem [nettem] mos[t?] [or], biztosnak [g]ondo[l]tam. Arra kérem, édesem, ha igazán szeret, hagyjon fel a val[?] a tolakodó vetélytár[s]… álmot remél, és meg is tette, és nem méltatta válaszra sorait. Ami a Bözsit illeti, igazán sajnálom, hogy ennyire jut[ott] a jóbarátság, ezt nem gondoltam. Ami a [litaszki lahjat] illeti, szeretném látni, és szeretném én elintézni, [hate bizatamel ahi] szereti kedvese Feri. Ezzel bezárom soraim. [harahikok] … viszont[l]átásig üdvözli szerető kedvese Feri.

## English (readable parts only)

My beloved sweet Jolánka! Now I answer your lines. [unresolved] my things to write would run out sooner than yours, darling, if I say it myself. I want to tell only by word of mouth what comes so hard, because I am a great slave, I have no say over myself. I will write no more about when I am going, because even then I [unresolved] I thought it certain. I ask you, darling, if you truly love me, give up the [?] intrusive rival [?] hopes for a dream, and he did it too, and did not deem your lines worth an answer. As for Bözsi, I am truly sorry the good friendship has come to this; I did not expect that. As for [unresolved], I would like to see it and I would like to settle it myself, [unresolved] your sweetheart Feri who loves you. With this I close my lines. [unresolved] Until we meet again, greetings from your loving sweetheart Feri.

## Slovak (len čitateľné časti)

Moja milovaná sladká Jolánka! Teraz odpovedám na Vaše riadky. [nevyriešené] skôr sa mi minie, čo mám písať, než Vám, drahá, ak to poviem sám. Len ústne chcem povedať to, čo ide tak ťažko, lebo som veľký otrok, nerozhodujem sám o sebe. Viac nepíšem, kedy idem, lebo ani vtedy [nevyriešené] som to pokladal za isté. Prosím Vás, drahá, ak ma naozaj ľúbite, nechajte [?] dotieravého soka [?] dúfa v sen, a aj to urobil a nepovažoval Vaše riadky za hodné odpovede. Čo sa týka Bözsi, naozaj ľutujem, že dobré priateľstvo došlo až sem; to som si nemyslel. Čo sa týka [nevyriešené], chcel by som to vidieť a chcel by som to sám vybaviť, [nevyriešené] Váš milý Feri, ktorý Vás ľúbi. Týmto končím svoje riadky. [nevyriešené] Do videnia, pozdravuje Váš milujúci milý Feri.

## Uncertainties

1. **Rows 3-5, about 45 signs: unresolved.** Letters are read, the sentence is not. Any of *oly örömmel*, *érdek-*, *két lap*, *lapírás*, *pénteke* would be a guess. The letters rest on an o/i distinction that is weak here, and the first signs of rows 4 and 5 lie under the postmark.
2. **Row 15** *nettem mosor*: unresolved. *Most* would need a t that is not there.
3. **Row 25** *litaszkilahjat*: an accusative before *illeti*, perhaps a name; unresolved.
4. **Row 26** *hatebizatamelahi*: unresolved. The word before it, *elinteznhate*, lacks the i of *elintézni* or holds another form.
5. **Edge R1** tail *harahikok* and **stamp S1**: unresolved; R1 and S1 are faint and S1 borders the stamp remnant.
6. **Reading order** of R1, R2 and the stamp block is inferred, not given on the card. R2 and S7 both end *kedvese Feri*.
7. **Row 19-20**: *a val|a tolakodó*: the *val* and its link are not explained; *vetejtar* is taken as *vetélytár(s)*, j for ly being the family habit, and the s is either the first sign of row 20 (shape between o and s) or absent. The subject of *meg is tette* is unclear.
8. **Word-sense calls**: *akar(om)* (the sign under the postmark line is k or g), *mokor* for *mikor*, *jutova* for *jutott a*, *hagyjon* (the j is an ink blot; shape agrees), *ha magam mondom* with a following stray t.
9. Translations of bracketed stretches are not offered, and the English of the *vetélytárs* sentence is tentative.

## Why the readable parts are believed

The unchanged family key gives long runs of idiomatic Hungarian that could not arise by chance (*nagy rabszolga vagyok, nem rendelkezem magam felett; nem méltatta válaszra; ami a Bözsit illeti, igazán sajnálom*). The address, Budapest cancel and signature Feri fit the family. *Illeti* decodes identically in rows 22 and 25, and *kedvese Feri* in R2 and S7.
