# HCP 1549 / pc_hcp_230 — Czech love letter from "P." to Anna Tichá, 2 July 1903

**Status (round 2, after review 1): complete reading.** Every cipher sign on the card is read with the
unchanged Anna Tichá family key, except two ink-blotted signs inside one word (U1, T04), which are
*restored* as D and C to give DOKONCE and are marked as restorations. Five writer's slips are kept
literally and repaired only in the editorial text. This section supersedes everything below
"Archive: round-1 text".

Credit: transcription, record and first reading by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol,
2026-10-28); completion (U1, A1, A2) and the round-2 corrections by Claude Opus 5.5 (2026-10-29).
The key is a **known, transferred family key** (ciphers/hcp-1520/work/key.json; partial public key by
Maxim Egorov, https://maxim-egorov.dev/research/anna-ticha-postcards/). No reading of this card was
published or supplied; the portal lists it as Not solved with no attachment solution.

## Cipher type and key

Monoalphabetic substitution of Czech base letters (no diacritics), digits for vowels, swapped
consonant shapes, plus one sign for the digraph CH (MASC).

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 8 | L | y (7-shape) | J |
| b | P | c | S | d (looped) | T | f | V |
| g | K | h (tall looped) | R | m | N | n | M |
| p | B | q (9-shape) | Z | r (short) | H | s | C |
| t (crossed) | D | H (r with tilde) | CH | | | | |

## Single command

From the repository root:

```sh
python3 -I ciphers/hcp-1549/work/decode-r2.py
```

It reads work/transcription-r2.json (manual glyph record, 24 rows; built from the round-1 record by
work/build-record-r2.py, which applies and logs each review correction) and work/key.json (asserted
identical to the hcp-1520 family key), and prints the literal reading, the editorial base reading and
`CHECKED: 24 rows; 846 plainly read cipher units (7 of them CH); 2 restored units (U1); 0 bounded
alternatives; 5 editorial repairs.` Saved output: work/output-r2.txt. (The round-1 command
work/decode.py still runs and reproduces the superseded round-1 record.)

Reading order: top rows T01–T05, bottom rows B01–B05 (the sentence runs on across the picture),
then the left addition L01–L11 and the right addition R01–R03 (both written sideways; turn the card
90° clockwise).

## Literal reading (base letters; [X] = restored under an ink blot)

```text
JE MI NEVYSLOVNE LITO, ZE SE DOSTALO MEMU DOPISU TAKOVEHO VYKLADU! CHTEL JSEM DOPIS
PREPSATI, PONEVADZ OBAVAL JSEM SE, ZE BUDE NESPRAVNE INTERPRETOVAN. BOHUZEL NEZBY-
VALO MI JIZ K TOMU CASU. - JE MI ZVASTE LITO, ZE ANUNKA POKLADA MNE ZA SCHOPNA,
ABYCH VEDOME URAZEL DIVKU VUBEC A [D]OKON[C]E DIVKU, KTERE SI NADE VSE VAZIM, KTERA
JE MI NADE VSE DRAHA A KTEROU ZBOZNUJI. PRAVE PROTO, PONEVADZ TE MAM NEVYSLOVNE
RAD A PONEVADZ SE O TEBE BOJIM, PSAL JSEM SLOVA TA A TO SICE TIM SPISE, PONEVADZ
ZNAM VOLNE NAZORY MODERNICH PANU O POMERU K DAMAM. HTEL JSEM ZASLATI NOVY DOPIS
AVSAK MYSLIM, JELIKOZ PSANE SLOVO DOPOUSTI TAK RUZNERO VYKLADU, ZE BUDE LEPE PONECHATI
ROZPRAVU DU AZ K OSOBNIMU SETKANI, AC BUDE-LI SE CHTITI NYNI ANUNKA JESTE
SE MNOU SEJITI.
ZE UDELAL PAN BRATR S VYBOR-
NYM PROSPECHEM MATURITU
MNE NEJENOM BAVILO, NYBRZ
I TESILO. PREJI SVEMU JEDI-
NEMU SRDECKU, ABY SO O
PLESU DOBRE BAVILO. TESILO
BY MNE VELICE, KDYBY PRI
TOM NEZAPOMNELO UPLNE NA
SVEHO ZARMOUCENEHO P.,
KTERY MU POSILA VRELOU UPRIMNOU
PUSU.
HNEVAS SE NA MNE OPRAVDU
ANICKO MA? JE MI VELICE
SMUTNO V DUSI!
```

Writer's slips, kept literally and repaired editorially: ZVASTE → zv**l**áště (L omitted);
HTEL → **ch**těl (CH tilde omitted, T01 has a proper CHTEL); RUZNERO → různé**h**o (R-shape for H);
ROZPRAVU DU → rozpravu **t**u (D-shape for T); ABY SO → aby **se** (O for E; a faint mark above the sign).

## Editorial Czech

> Je mi nevýslovně líto, že se dostalo mému dopisu takového výkladu! Chtěl jsem dopis přepsati, poněvadž obával jsem se, že bude nesprávně interpretován. Bohužel nezbývalo mi již k tomu času. — Je mi zvláště líto, že Anunka pokládá mne za schopna, abych vědomě urážel dívku vůbec a [d]okon[c]e dívku, které si nade vše vážím, která je mi nade vše drahá a kterou zbožňuji. Právě proto, poněvadž tě mám nevýslovně rád a poněvadž se o tebe bojím, psal jsem slova ta, a to sice tím spíše, poněvadž znám volné názory moderních pánů o poměru k dámám. Chtěl jsem zaslati nový dopis, avšak myslím, jelikož psané slovo dopouští tak různého výkladu, že bude lépe ponechati rozpravu tu až k osobnímu setkání, ač bude-li se chtíti nyní Anunka ještě se mnou sejíti.
>
> Že udělal pan bratr s výborným prospěchem maturitu, mne nejenom bavilo, nýbrž i těšilo. Přeji svému jedinému srdéčku, aby se o plesu dobře bavilo. Těšilo by mne velice, kdyby při tom nezapomnělo úplně na svého zarmouceného P., který mu posílá vřelou upřímnou pusu.
>
> Hněváš se na mne opravdu, Aničko má? Je mi velice smutno v duši!

## English translation

> I am inexpressibly sorry that my letter was given such an interpretation! I wanted to rewrite the letter, because I was afraid it would be misinterpreted. Unfortunately I no longer had time for it. — I am especially sorry that Anunka thinks me capable of knowingly offending a girl at all, and even a girl whom I esteem above all, who is dearer to me than anything and whom I adore. Precisely because I love you inexpressibly and because I fear for you, I wrote those words, and all the more so because I know the loose views of modern gentlemen on their relations with ladies. I wanted to send a new letter, but I think that, since the written word allows such varied interpretation, it will be better to leave this discussion until we meet in person — if, that is, Anunka still wants to meet me now.
>
> That your brother passed his maturita (school-leaving examination) with distinction not only amused me but also pleased me. I wish my one and only little heart a good time at the ball. It would please me very much if it did not quite forget its saddened P., who sends it a warm, sincere kiss.
>
> Are you really angry with me, my Anička? I am very sad at heart!

## Slovak translation

> Je mi nevýslovne ľúto, že môj list dostal taký výklad! Chcel som list prepísať, pretože som sa obával, že bude nesprávne vyložený. Žiaľ, už mi na to nezostával čas. — Je mi zvlášť ľúto, že ma Anunka pokladá za schopného vedome urážať dievča vôbec, a dokonca dievča, ktoré si nadovšetko vážim, ktoré je mi nadovšetko drahé a ktoré zbožňujem. Práve preto, že ťa mám nevýslovne rád a že sa o teba bojím, napísal som tie slová, a to tým skôr, že poznám voľné názory moderných pánov na vzťah k dámam. Chcel som poslať nový list, ale myslím, keďže písané slovo pripúšťa taký rozličný výklad, že bude lepšie nechať tento rozhovor až na osobné stretnutie, ak sa, pravda, bude chcieť Anunka teraz ešte so mnou stretnúť.
>
> To, že pán brat zmaturoval s výborným prospechom, ma nielen zabávalo, ale aj tešilo. Želám svojmu jedinému srdiečku, aby sa na plese dobre zabavilo. Veľmi by ma tešilo, keby pritom celkom nezabudlo na svojho zarmúteného P., ktorý mu posiela vrúcnu úprimnú pusu.
>
> Naozaj sa na mňa hneváš, Anička moja? Je mi veľmi smutno na duši!

## What remains uncertain

- **U1 (T04) DOKONCE is a restoration, not a reading.** Seven sign positions: blot, overinked O, K, O, N, blot, E. The two blots' outlines are compatible with crossed t (D) and s (C) but do not prove them (the second blot has a descender the normal s lacks). *?okon?e* has no other good Czech completion and "dívku vůbec a dokonce dívku, které…" is idiomatic.
- **Five writer's slips** (list above) are repaired only editorially; the literal keeps them. SO in L05 has a faint mark above the O that may be a correction toward E.
- **"mne nejenom bavilo"** (L03, literally `p6f483` = BAVILO) is read as written; a writer might have meant another verb, but the glyphs are clear.
- Accents, punctuation and word joins in the editorial text are editorial; the cipher writes base letters only.
- The sender is known only as "P."; the "brother" and "Anunka" (= Anna Tichá, a teacher in Žirovnice) are known from the card and the family, not from records.
- Only the 1024-pixel portal image is available.

## Why this is believed correct

The unchanged family key, used on many reviewed cards of the same correspondence, turns all 24 rows into continuous, grammatical period Czech (archaic infinitives in -ti, *ač bude-li*, *poněvadž*, *nýbrž*) with no unused or unmapped sign; the content (a misunderstood earlier letter, a brother's maturita, a ball, "Aničko") fits the Anna Tichá correspondence and the date 2/7 1903 (end of the school year, maturita season). An independent reviewer decoded the record with its own script and matched it, and checked every row against the scan; the round-2 corrections all come from that sign-by-sign comparison.

## Response to review 1

Reviewer verdict REVISE, 12 findings. I (Claude Opus 5.5, solver) re-examined every cited place on the
reviewer's enlargements of source/picture.jpg (review/work/*.png) and on the card; all corrections are
applied in work/build-record-r2.py (each logged in transcription-r2.json, `corrections_r2`) and
reproduced by work/decode-r2.py (output work/output-r2.txt). The key is unchanged.

1. **T03 ZVASTE — fixed (agree).** review/work/t3vaste.png shows `7 5  n 4  9 f 6 c d 5`: a 9-shaped Z
   with a left-curling tail stands before f6cd5, the same shape as the Z of the following `95` (ZE).
   Record now `qf6cd5` = ZVASTE; editorial *zvláště* (L omitted by the writer). The round-1 repair
   *vážně?* is withdrawn.
2. **T04 KTERE — fixed (agree).** t4ktero2.png: `g d 5 h 5`; the last sign has the flagged top of 5,
   not the round 3. *dívku, které si … vážím* is correct Czech. The "KTERO" anomaly is withdrawn.
3. **B01 SICE — fixed (agree).** b01snad.png: `c 4 s 5` (round c, crossed 4, small angular s, 5); no 6
   or t. Round-1 SNAD was a word supplied from expectation. Now *a to sice tím spíše*.
4. **B04 AČ — fixed (agree).** b4as2.png: the second sign of `6s` is the small angular s (C) of VUBEC,
   unlike the round c (S) of the following `c5`. Now *ač bude-li se chtíti*; the *až?* repair withdrawn.
5. **Command/claim mismatch — fixed.** The new single command decode-r2.py prints the complete literal
   reading (no [UNK], no [x|y]) and an editorial base reading in which every restoration ([X]) and
   writer-slip repair (<X>) is marked. The status text and counts above are rewritten consistently:
   846 plainly read units (7 CH) + 2 restored units, 0 bounded alternatives.
6. **B04 DU — fixed (agree).** b4tu2.png: the first sign is the bowl-less crossed t (D). Recorded
   literally `t2` = DU; editorial *tu*, listed as a writer's slip.
7. **B03 RUZNERO — fixed (agree).** b3ruz2.png and review/work/seg_B03.png: in `h2qm5h3` both h are the
   same tall looped R-shape. Literal RUZNERO, editorial *různého*, listed as a writer's slip.
8. **A2 HTEL — fixed (agree).** b2ch.png: `r d 5 8` with a plain short r and no tilde, while CHTEL
   (T01), MODERNICH and CHTITI carry the tilde. Literal HTEL; *chtěl* is presented as an editorial
   repair of an omitted tilde.
9. **A1 ZARMOUCENEHO — fixed (agree).** l09b.png: despite overinking and a crossing stroke the sign has
   the tall looped ascender of h (R), unlike the short r (H) of SVEHO in the same row. Recorded as h on
   the shape evidence.
10. **U1 DOKONCE — fixed (agree).** u1b.png: blot, heavy O, g, 3, m, blot, 5. Recorded as
    `{t}3g3m{s}5`, printed [D]OKON[C]E in literal and editorial text; described as 4 plain + 1
    overinked + 2 restored signs, not "5 of 7 plain".
11. **L05 SO — noted (agree).** l05b.png shows a faint mark above the 3; mentioned in the uncertainties
    as a possible correction toward E; editorial *se*.
12. **Presentation — fixed.** The current claim is now one clean section at the top with one set of
    counts; the round-1 text (helper/root process notes, 836/838 counts) is kept below only as a
    labelled archive. The literal BAVILO in L03 is retained, as the reviewer confirmed.

Effect on the reading: four words change (ZVASTE, KTERE, SICE, AČ, all improving the Czech) and four
literal letters are now recorded as writer's slips; the message, its structure and its translation
are otherwise unchanged. This is a correction of individual signs, not a substantial change of the
reading.

---

## Archive: round-1 text (superseded)

## HCP1549 / pc_hcp_230 — known-key partial reading

This is a bounded solver candidate for the whole postcard. Both immutable sides and all four picture-side cipher regions were inspected. The record contains 838 known cipher units, two bounded single-unit alternatives, and one unknown-length ink region. It is not a complete, independently reviewed decipherment. The supplied Anna Tichá family key and prior public partial research were available before target transcription; this is known-key transfer, not independent key discovery. Root/helper collaboration is solver work, not independent review.

### Context and scope

The root inspected rendered General, Description and Attachments on 2026-10-28. The portal reports Not solved, Czech, Substitution, 1903-07-02, unknown sender, recipient Anna Tichá, private collection; no individual transcription or solution is attached. SOURCES.md records the exact image URLs and prior research provenance. The fresh bounded register check found 193 contributions / 159 HC IDs and no target entry. Neither this check nor a coherent reading establishes worldwide novelty.

The address side reads, in ordinary handwriting: “Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.” Picture-side ordinary date: 2/7 1903. These are outside the cipher-unit count. The address-side printed matter, stamp, postmarks and margins were inspected; no additional cipher line is claimed. The message discusses a misunderstood letter, a future personal meeting, a brother's successful maturita and a ball. It signs with the initial P.; no civil identity is established.

### Key and reproducible procedure

|Shape label|Plain|Shape label|Plain|Shape label|Plain|Shape label|Plain|
|---|---|---|---|---|---|---|---|
|1|Y|2|U|3|O|4|I|
|5|E|6|A|8|L|y|J|
|b|P|c|S|d|T|f|V|
|g|K|h|R|m|N|n|M|
|p|B|q|Z|r|H|s|C|
|t|D|H|CH|||||

These are conventional family shape labels, not printed ciphertext characters. H is a special CH unit, distinct from h/R and r/H. The key is copied unchanged from ciphers/hcp-1520/work/key.json. The generic published key and photographic pc199 reference are hashed in the audit. The latter's rare shallow-v/F is distinct from tall-looped f/V. No rare-F target assignment or newly inferred key is used.

Read top T01–T05, then bottom B01–B05: the sentence continues NEVYSLOVNE / RAD across these regions. Next read the independent left addition L01–L11, then right addition R01–R03. The left and right additions require turning the original picture 90° clockwise. Their relative order after the main message is an editorial presentation order; neither is a continuation across the flower. All four regions are represented, including the short final L11 and R03. There is no omitted flower-area text or invented missing span there.

work/transcription.json is a manual glyph transcription, not OCR. It defines each original crop, its orientation and every row box. The four `*-indexed.png` views and all 24 row crops locate the rows; work/indexed.csv lists the known/uncertain tokens in reading order. “row_token_position” counts recorded tokens, including an unknown-length region as one record item; it does not assert the number of physical glyphs inside that region. The record contains no inferred cancellation.

From repository root:

```sh
python3 ciphers/hcp-1549/work/decode.py
```

This read-only standard-library command verifies original/source-guard, reference and record hashes, the immutable copied key, all indexed positions, exact literal-file equality, and a genuine fixed-key inverse. CH is greedily one unit on inversion; bounded alternatives are each checked against the same fixed key. It does not use a per-word inverse dictionary. Hashes and inverse agreement prove record consistency, not the truth of manual handwriting decisions. Image transcription is still a human/visual step; there is no claim to automatically recover handwriting directly from the JPEG.

### Literal Czech base reading

Line breaks and anomalous base letters are preserved. Square brackets are record uncertainty annotations, absent from the source. No source diacritic is silently restored.

```text
JE MI NEVYSLOVNE LITO, ZE SE DOSTALO MEMU DOPISU TAKOVEHO VYKLADU! CHTEL JSEM DOPIS
PREPSATI, PONEVADZ OBAVAL JSEM SE, ZE BUDE NESPRAVNE INTERPRETOVAN. BOHUZEL NEZBY-
VALO MI JIZ K TOMU CASU. - JE MI VASTE LITO, ZE ANUNKA POKLADA MNE ZA SCHOPNA,
ABYCH VEDOME URAZEL DIVKU VUBEC A [UNK:U1] DIVKU, KTERO SI NADE VSE VAZIM, KTERA
JE MI NADE VSE DRAHA A KTEROU ZBOZNUJI. PRAVE PROTO, PONEVADZ TE MAM NEVYSLOVNE
RAD A PONEVADZ SE O TEBE BOJIM, PSAL JSEM SLOVA TA A TO SNAD TIM SPISE, PONEVADZ
ZNAM VOLNE NAZORY MODERNICH PANU O POMERU K DAMAM. [H|CH]TEL JSEM ZASLATI NOVY DOPIS
AVSAK MYSLIM, JELIKOZ PSANE SLOVO DOPOUSTI TAK RUZNEHO VYKLADU, ZE BUDE LEPE PONECHATI
ROZPRAVU TU AZ K OSOBNIMU SETKANI, AS BUDE-LI SE CHTITI NYNI ANUNKA JESTE
SE MNOU SEJITI.
ZE UDELAL PAN BRATR S VYBOR-
NYM PROSPECHEM MATURITU
MNE NEJENOM BAVILO, NYBRZ
I TESILO. PREJI SVEMU JEDI-
NEMU SRDECKU, ABY SO O
PLESU DOBRE BAVILO. TESILO
BY MNE VELICE, KDYBY PRI
TOM NEZAPOMNELO UPLNE NA
SVEHO ZA[R|H]MOUCENEHO P.,
KTERY MU POSILA VRELOU UPRIMNOU
PUSU.
HNEVAS SE NA MNE OPRAVDU
ANICKO MA? JE MI VELICE
SMUTNO V DUSI!
```

### Editorial accented Czech

This section adds accents, ordinary capitalization and punctuation and joins split words. Repairs that change the literal base reading are bracketed: VASTE → proposed *vážně*, KTERO → proposed *kterou*, SO → proposed *se*, AS → proposed *až*. The B02 word PANU follows the same-card shape controls documented below. BAVILO, Anunka and the initial P. remain as recorded. The unknown word is not reconstructed.

> Je mi nevýslovně líto, že se dostalo mému dopisu takového výkladu! Chtěl jsem dopis přepsati, poněvadž obával jsem se, že bude nesprávně interpretován. Bohužel nezbývalo mi již k tomu času. — Je mi **[vážně?; doslova VASTE]** líto, že Anunka pokládá mne za schopna, abych vědomě urážel dívku vůbec a **[nečitelné slovo U1]** dívku, **[kterou?; doslova KTERO]** si nade vše vážím, která je mi nade vše drahá a kterou zbožňuji. Právě proto, poněvadž tě mám nevýslovně rád a poněvadž se o tebe bojím, psal jsem slova ta, a to snad tím spíše, poněvadž znám volné názory moderních pánů o poměru k dámám. **[H|CH]těl** jsem zaslati nový dopis, avšak myslím, jelikož psané slovo dopouští tak různého výkladu, že bude lépe ponechati rozpravu tu až k osobnímu setkání, **[až?; doslova AS]** bude-li se chtíti nyní Anunka ještě se mnou sejíti.
>
> Že udělal pan bratr s výborným prospěchem maturitu, mne nejenom bavilo, nýbrž i těšilo. Přeji svému jedinému srdéčku, aby **[se?; doslova SO]** o plesu dobře bavilo. Těšilo by mne velice, kdyby při tom nezapomnělo úplně na svého za**[r|h]**mouceného P., který mu posílá vřelou upřímnou pusu.
>
> Hněváš se na mne opravdu, Aničko má? Je mi velice smutno v duši!

### Slovak translation

The translation follows the proposed editorial repairs only where marked and carries the unread region and unresolved glyphs. The incomplete [H|CH]těl is translated as a tentative “chcel”.

> Je mi nevýslovne ľúto, že môj list dostal takýto výklad! Chcel som ho prepísať, pretože som sa obával, že bude nesprávne interpretovaný. Žiaľ, už mi na to nezostával čas. Je mi **[vážne?; doslova VASTE]** ľúto, že ma Anunka pokladá za schopného vedome urážať dievča vôbec a **[nečitateľné slovo U1]** dievča, **[ktoré?; oprava KTERO]** si nadovšetko vážim, ktoré mi je nadovšetko drahé a ktoré zbožňujem. Práve preto, že ťa mám nevýslovne rád a že sa o teba bojím, som napísal tie slová; azda tým skôr, že poznám voľné názory moderných pánov o vzťahu k dámam. **[Chcel?]** som poslať nový list, ale myslím si, že keďže písané slovo pripúšťa taký rozličný výklad, bude lepšie nechať tento rozhovor na osobné stretnutie, **[až?; doslova AS]** ak sa ešte Anunka bude chcieť so mnou stretnúť.
>
> To, že pán brat zmaturoval s výborným prospechom, ma nielen bavilo, ale aj tešilo. Svojmu jedinému srdiečku želám, aby **[sa?; doslova SO]** na plese dobre bavilo. Veľmi by ma potešilo, keby pritom celkom nezabudlo na svojho za**[r|h]**múteného P., ktorý mu posiela vrúcny úprimný bozk.
>
> Naozaj sa na mňa hneváš, moja Anička? Je mi veľmi smutno v duši!

### Coverage and unresolved source controls

- **24 rows: 838 known cipher units, including 7 known CH units = 845 known base letters.** Two additional positions have bounded single-unit alternatives; one may be CH. U1 has unknown length. No exact complete ciphertext denominator or percentage coverage is claimed. Date, address, punctuation and unknown ink are outside the known-unit count.
- **U1, T04:** the retraced word between A and DIVKU is left as an unknown-length ink region. A grammatically attractive completion is not a glyph reading. Its dark strokes establish neither the original number of units nor cancellation. Root should inspect work/t4-mid.png, T04.png and original coordinates approximately x409–512, y105–141.
- **A1, L09:** third glyph of q6…n32s5m5r3 has h/R versus r/H alternatives. The rest is read literally, producing ZA[R|H]MOUCENEHO. A fluent *zarmouceného* does not decide the glyph. See left9.png, L09.png and A1-source-controls.png; the latter compares same-row r/H in SVEHO with h/R in KTERY, VRELOU, PREJI and DRAHA. Heavy overink still prevents choosing the target class confidently.
- **A2, B02:** the opening shape of …d58 is r/H or H/CH; ownership of the cap/mark is uncertain. T01 has a clearer marked CH in CHTEL and B04 another in CHTITI. See b2-mid.png and B02.png.
- **Resolved A3/A4 source controls, B02:** the four-unit word after MODERNICH is b6m2 → PANU. In work/A3-A4-source-controls.png its first glyph has the lower bowl and uncrossed top of b/P in PREPSATI and PONEVADZ, distinct from the conspicuous upper crossbar of t/D in DAMAM. Its third glyph matches m/N in ZNAM and MODERNICH, whereas n/M in DAMAM and MNOU has the other hump geometry. These direct same-card comparisons, rather than an expected Czech word, support selecting the two formerly bounded positions. The panel and exact pixel boxes are preserved in source-control-boxes.json. Root should corroborate the visual decision; it is not expert handwriting ground truth.
- **Literal anomalies:** T03 has f6cd5 → VASTE, T04 gd5h3 → KTERO, L05 c3 → SO, B04 6c → AS. Do not silently change their fixed-key values. Root should adjudicate c/S versus s/C, t/D versus d/T, 3/O versus 2/U/5/E, and any marks against same-card controls. These are candidate shape readings, not established author errors. The left's two BAVILO groups are retained. The nickname ANUNKA has 2/U, whereas ANICKO has 4/I.
- Accents in the editorial text and punctuation interpretation are less constrained than the base substitution. Source underlines are not cancellations. The dense L09 ink likewise is not called canceled. The photographic pc199 reference corroborates a family convention but is AI-associated published partial research, not expert handwriting ground truth.

The message's extended coherence and fixed-key consistency support the family-key identification and much of the transcription. They cannot resolve the listed image ambiguities. Root should check these source controls before any handover or final claim. No watcher, reviewer, marker, PDF, register entry, git action or source modification was performed by this helper.

### Follow-up same-card controls

At root request, source comparison panels were made for the formerly bounded B02 b/t and m/n positions and L09 h/r. PANU is now selected from the direct same-card geometry; A1 remains bounded and A2 remains H/CH. U1 is unchanged. The record, indexed positions, literal file, saved verification and integrity manifest were regenerated. The read-only decoder passes: 838 known units, 7 known CH, 845 known base letters, two bounded single-unit alternatives, one unknown-length region. Source files and their original guard hashes remain unchanged.

### Root source QA - 2026-10-28

Root inspected both originals, all four message regions and all24 physical rows, including the separate right-side three-row addition, then compared the same-card source controls. The lower-loop/uncrossed b/P class in PREPSATI/PONEVADZ versus crossed t/D in DAMAM supports the first PANU unit; m/N comparisons with ZNAM/MODERNICH support the third. PANU is therefore a source-driven selection of the two formerly bounded units. Heavy L09 h/R versus r/H remains unresolved; B02 cap ownership still does not determine H/CH, and T04 U1 remains unknown-length. Literal VASTE, KTERO, SO, AS and BAVILO are preserved as candidate source readings, not established writer errors. ANUNKA retains2/U. The long body and both marginal additions are represented; no omission or cancellation is invented from underlines or retracing. Read-only decoding passes838 known units,7 CH =845 known letters, two bounded alternatives and one unknown-length region. The earlier836-unit count is superseded.

All checks are solver collaboration, not independent provider review. Original sources remain unchanged. The candidate stays PARTIAL without a marker, PDF or register entry. The live193-contribution /159-HC-ID register check is recorded in the batch; this target is absent.

### Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading, handed to review (DONE1).**

1. **U1, T04 (work/t4-mid.png).** The retraced word between `6` (A) and
   `t4fg2` (DIVKU) has seven sign positions: `[■] 3 g 3 m [■] 5`. The middle
   signs are plain: O K O N, and the final one is E. The two blackened signs
   keep their outlines: the first a tall stem with a loop like the looped `t`
   (D), the second a round bowl with a descending tail like `s` (C). Read
   **DOKONCE** (*dokonce*, “even”): “…abych vědomě urazil dívku vůbec, a
   dokonce dívku, kterou si nade vše vážím.” Five of the seven letters are
   plain on the card, and *?okon?e* has no other Czech completion.
2. **`[H|CH]TEL`** → **CHTEL** (*chtěl*). *Htěl* is not Czech, and the same verb
   appears as clear CHTEL in T01.
3. **`ZA[R|H]MOUCENEHO`** → **ZARMOUCENEHO** (*zarmouceného*, “saddened”).
   *Zahmouceného* is not a word.

Literal forms kept: VASTE (= vážně?), KTERO (= kterou), SO (= se).

Slovak (full): see the translation above. With the three points resolved:
„…že ma Anunka pokladá za schopného vedome uraziť dievča vôbec, a dokonca
dievča, ktoré si nadovšetko vážim… Chcel som poslať nový list… na svojho
zarmúteného P.“

Reproduce with the command given earlier in this file. The family key is
credited to earlier family cards and the published partial study by Maxim Egorov.
