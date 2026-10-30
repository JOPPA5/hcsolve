# HCP 1297 (cpc_1912-07-07_HU__HU_Jasz Arokszalas_jolanka-29): a Hungarian love letter from Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: whole card deciphered (460 of 460 signs transcribed; two marks have no letter value, one sign only a tentative one); some phrases stay open in sense. Independent review 1 verdict REVISE, all findings addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1297 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1297), part of Tobias Schrödel's collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, date 1912-07-07, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution was met.

The picture side is a tinted photograph of a young couple with swallows overhead. The printed caption and verse are in Hungarian ("Fecském hova szállsz?") and are not cipher. The address side is in plain writing to **Tóth Jolánka** at **Jászárokszállás**. The whole cipher text is in red ink on the address side: 21 rows at the left, four rows across the bottom edge, and a five-line block written over the stamp area at the top right. The first line of that block is washed out. The date comes from the portal; the postmark is not fully legible.

The card belongs to the group addressed to Jolánka Tóth, with the same cipher and closing formulas (see HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). The sender signs "Feri" twice. Identity with the Feri of HCP 1216 is likely but not claimed.

![Picture side, printed text only (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side, with the cipher rows at the left and bottom and the block over the stamp area (source/address-large.jpg)](../source/address-large.jpg)

## Method

The key was **transferred**, not recovered here. It is the Jolánka family key, established on earlier cards by the OpenAI GPT solver and completed by Claude Opus 5.5. All work on this number was done by Claude Opus 5.5 on 2026-10-30.

The transcription is **manual**. The solver read each sign from enlarged crops of the un-converted original scan (work/hires/), recording one token per written sign in work/ledger-opus.txt. The portal gives no transcription and no OCR was used. A script (work/decode_opus.py) checks the scan hashes and decodes the ledger:

```text
python3 -I ciphers/hcp-1297/work/decode_opus.py
```

The reviewer read all rows from its own crops and decoded them with its own script, which shares no code with the solver's. After the fixes described below, the two outputs differ only in how no-value marks are displayed and in how the lines under the stamp are split.

## Key

Hungarian, monoalphabetic substitution with invented graphic signs. Letter names are conventional descriptions of handwritten shapes.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| two bars | a | section mark / S-loop | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left + right bowl | cs | three short strokes | m | gamma/corner | t |
| short + long stroke | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short tick | h / p (one sign) | dotted crossed curve | i |
| open loop with descender | g | inverted T | j | cross with hook | z |
| joined loop + descender | gy | | | | |

Two dots over o or u give ö or ü. Other accents are faint and are supplied in normalization. Because h and p share a sign, the choice between them rests on word sense. So does a versus e where a third dash is doubtful.

## Plaintext

Literal decipherment, row by row (s1–s5 are the lines over the stamp; {|} is a mark with no letter value, {/} a single slash of uncertain value):

```text
01 kedvesjolankam             14 mindenbajtol{|}ede
02 becsessoraitmegkap         15 semaligvaromazt
03 tammejetangyon             16 azidöthogyjolan
04 köszönokkedvesjo           17 kavalujrmulathas
05 önnagyonroszul             18 sakharomhetmulva
06 erteteteszedemet           19 leszegynepszava
07 haazgondoljahogy           20 ünepejmajerölszoval
08 szüleimtalanmaga           21 bövebbenjomulatast
09 ragszonakeztaigy           22 kivanovasarnapabela{/}ak
10 gondoljaamiaz              23 vasarna{|}pirokistenvele-
11 utazstiletiatol               tisztelemakedvesmamajat
12 nemfelekmermeg             24 atavolbolimadojaferi
13 vedamagaszeleme            25 sajnalomhogynemjötbe
s1 csokolom | s2 szamta | s3 lanszor | s4 hükedve | s5 senferi
```

Normalized Hungarian. Square brackets mark letters not on the card; braces mark open points.

Kedves Jolánkám! Becses sorait megkaptam, melyet [n]agyon köszönök, kedves jó! Ön nagyon rosszul értette [be]szédemet, ha az[t] gondolja, hogy szüleim talán magá[ra ha]ragszanak; ezt a így gondolja {sense unresolved}. Ami az utaz[á]st illeti, attól nem félek, mer[t] megvéd a maga szelleme minden bajtól. Édesem, alig várom azt az időt, hogy Jolánkával újr[a] mulathassak. Három hét múlva lesz egy Népszava-ünnepély; majer[r]ől szóval bővebben. Jó mulatást kívánó[k] vasárnap[r]a {Béladak?}. Vasárnap írok. Isten vele. Tisztelem a kedves mamáját. A távolból imádója Feri. Sajnálom, hogy nem jött be.

Under the stamp: Csókolom számtalanszor. Hű kedvese[n?] Feri.

**English.** Dear Jolánka! I received your esteemed lines, for which I thank you very much, my dear good one! You understood my words very badly if you think that my parents may perhaps be angry with you; [rows 9–10 unresolved: literally "this ... thus you think", the expected sense is probably "do not think of it this way", but no negation is on the card]. As for the journey, I am not afraid of it, because your spirit protects me from every harm. My sweet, I can hardly wait for the time when I can have fun with Jolánka again. In three weeks there will be a Népszava festival; about *majer* more by word of mouth. I wish good fun for Sunday {Béladak?}. I shall write on Sunday. God be with you. My respects to your dear mother. From afar, your adorer, Feri. I am sorry that you did not come in.

Under the stamp: I kiss you countless times. Faithfully and lovingly [?], Feri.

**Slovak.** Milá Jolánka! Vaše vážené riadky som dostal, za čo veľmi ďakujem, moja milá dobrá! Veľmi zle ste pochopili moje slová, ak si myslíte, že moji rodičia sa na Vás azda hnevajú; [riadky 9–10 nevyriešené: doslova „toto ... takto si myslíte“, očakávaný zmysel je asi „tak to neberte“, no zápor na lístku nie je]. Čo sa týka cesty, tej sa nebojím, lebo Váš duch ma ochráni pred každým zlom. Moja sladká, sotva sa dočkám času, keď sa budem môcť znova zabávať s Jolánkou. O tri týždne bude slávnosť Népszavy; o *majeri* viac ústne. Želám dobrú zábavu na nedeľu {Béladak?}. V nedeľu napíšem. S Bohom. Pozdravujem Vašu milú mamu. Z diaľky Váš ctiteľ Feri. Ľutujem, že ste neprišli dnu.

Pod známkou: Bozkávam Vás nespočetnekrát. Verne a láskyplne [?] Feri.

## Uncertainties

- **Row 22 *bela/ak*.** The signs b e l a, a single slash, a k are clear, but no secure word results. It may be a name or a family form of Béla. An alternative, *vasárnap a Bélának* ("on Sunday, to Béla"), would take the slash as a reduced n, though it is a single stroke, unlike n elsewhere.
- **Row 20 *majer*.** The signs are clear, the meaning is not: a form of *major* (farmstead), a place name or the surname Majer. Left untranslated.
- **Rows 9–10.** The signs *ezt a így gondolja* are confirmed, but the clause gives no good sense as written.
- **Row 25 *jött be*.** The first sign is read j on shape plus sense, not shape alone: the bar is low on the stem, as on inverted T, but a tiny foot shows below it. The subject is not written; "you" follows the formal address.
- **Row 6 *[be]szédemet*.** The literal text is *erteteteszedemet*; the restoration assumes a repeated *-te-* or a dropped *be*. The last sign lies on the postmark, so t rather than r is by sense.
- **Rows 8–9 *magá[ra ha]ragszanak*.** The writer seems to have skipped from one *ra* to the next. The supplied letters are a restoration; the accent tick on the last a of *maga* supports it.
- **Row 3 *angyon*** is normalized *nagyon* (transposed letters), by sense.
- **Row 19 *Népszava*.** The p is by sense. Népszava was the Social Democratic daily; a festival of that name is an inference and was not checked against any source. *nép szava* ("voice of the people") would be the same letters.
- **Rows 20 and 24.** In *ünnepély* and *imádója* the j lies over a t-like top, apparently a correction. Row 24 also has a blot on the d.
- **Row 23 and row 14.** Blots and a smudged stroke; *vasárnap* is by sense there, and two marks have no letter value.
- **Under the stamp.** Only *csokol* is firm on the washed-out first line, and the *sz* of *számta-* is a restoration. *hű kedvesen* or a slip for *hű kedvese* cannot be decided. Where this block belongs in the letter is not known.
- **Spelling as written.** Double letters are often single (*roszul*, *ileti*, *atol*, *szeleme*, *jöt*), letters are dropped (*utazst*, *mer*, *ujr*), and ly appears as j (*mejet*, *ünepej*). Acute accents are supplied.
- **Not verified.** The identity of Feri and the postmark date.

## Review and what changed

An independent Claude Opus 5.5 reviewer reran the decoder, read all rows from its own crops and returned **REVISE**: the card, key and overall reading stand, with two signs to correct and five smaller points. All seven findings were accepted.

![Row 25: j, o with two marks, t. The low bar on the first sign is what changed the reading (review/work/crops/fot.png)](../review/work/crops/fot.png)

![Row 20: the final wave l that the first transcription missed (review/work/crops/r20w.png)](../review/work/crops/r20w.png)

- **Row 25 (major).** The first sign is j, not f. The closing sentence is now *nem jött be* ("you did not come in"), replacing the forced *nem fért be* ("it did not fit").
- **Row 20 (major).** A final wave had fallen outside the solver's crop. The row now ends *szoval*, and the count goes from 459 to 460 signs.
- **Row 20 normalization.** An article and an r that are not on the card were removed or bracketed.
- **Row 22.** The *vasárnap a Bélának* alternative was added.
- **Rows 4–5.** Punctuation is now *kedves jó! Ön nagyon…*, with no letter change.
- **Rows 9–10.** The clause is marked unresolved instead of smoothed over.
- **Ledger.** The block over the stamp was split into its five lines, and the legend was completed.

The reviewer could not verify the Népszava festival, the meaning of *majer*, Feri's identity, the postmark date, or the washed-out first line sign by sign.
