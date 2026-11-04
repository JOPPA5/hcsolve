# HCP1207 — Feri to Jolánka Tóth: ordered onto a train, the visit moved

**Status: complete reading of all ciphertext, with disclosed residual points; reviewed (round 1, verdict REVISE), findings addressed, see the last section.** Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. Portal status Not solved, no attached transcription or solution; no published solution of this card was found or used. The key was reconstructed on sister cards (HCP1216 and its family, credit there: OpenAI GPT solver, with later work by Claude Opus 5.5); the transfer, transcription and reading here are by Claude Opus 5.5.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (register label MASC), the Jolánka postcard family, key unchanged from HCP1216:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three strokes | m | gamma | t |
| long stroke + short tick | d (near h/p) | two strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short (near-homograph) | h / p | low descender | y |
| hooked stroke with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | joined hook + descender | gy | | |

Type update (2026-11-03): register type is now **MASC + Steganography**, because six cipher rows were hidden in the stamp box under the (now lifted) stamp; see "Stamp-box message (2026-11-03)" below.

Dots over o give ö. Row 9 also holds uncoded matter: the digits 7 0 and the plain cursive word "orakor".

Layout: 23 rows in the left half; row 23 runs on along the bottom edge under the address, to the right corner. Six more rows stand in the stamp square.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1207/work/decode_opus.py
```

It checks the SHA-256 of both scans in `source/` and both originals in `work/hires/`, decodes the ledger `work/ledger-opus.txt` (one token per written sign, a manual reading of enlarged crops, not OCR) and prints the literal rows and `work/normalized-opus.txt`.

## Literal decipherment

```
01 szertetedesegyetlen          13 hatommegdecsakkeson
02 remenyemkivanomhogyaleg      14 nemerkezekhazaedesem
03 jobbkedvebentalaljaso        15 irjameghogymikomegyhasz
04 raimsajnalattalkeltu         16 toriektolcsakmararadjo
05 datnomhogyemitöleny          17 nonededesemamedilehet
06 nyirafeltembekövet           18 mulasonjolhamarenem
07 kezetmertojanvonathoz        19 mulathatokmagaval
08 lettemvezenyelveeseste       20 edesemhajolmulatgon
09 7 0 [orakor] jönviszaesregel 21 doljonimdojarki
10 retelikleahihenöm            22 ijsokatgondol{?}kodom
11 esigylegnagyobbsajnala       23 magafelölistenveledesemimadojaferi
12 tomrakedenenestelatoga
stamp square: csoko / lomsza / mtalan / szo{r|h}ű / kedvese / feri
```

## Hungarian (normalized)

Square brackets mark letters that have no sign on the card; other spelling changes (including removed repeated letters) are listed under Uncertainties, item 9. Accents are supplied. The word divisions are editorial.

Szer[e]tet[t] édes egyetlen reményem! Kívánom, hogy a legjobb kedvében találja soraim. Sajnálattal kel[l] tudatnom, hogy [a]mitől ennyire féltem, bekövetkezet[t], mert olyan vonathoz lettem vezényelve, és este 7 0 [sic] órakor jön vis[s]za, és reg[g]elre telik le a pihenőm, és így legnagyobb sajnálatomra ked[d]en én este látoga[t]hatom meg, de csak későn, nem érkezek haza, édesem. Írja meg, hogy miko[r] megy Pásztoriéktól. Csak maradjon ön, édesem, amed[d]i[g] lehet, mulas[s]on jól, ha már én nem mulathatok magával. Édesem, ha jól mulat, gondoljon im[á]dójár[a], ki ily sokat gondolkodom maga felől. Isten vele, édesem. Imádója Feri.

Stamp square: Csókolom számtalanszor, hű kedvese Feri.

## English

My beloved sweet only hope! I wish that my lines find you in the best of moods. I regret to have to tell you that what I so feared has happened, for I have been ordered onto a train that comes back at 7 [written "7 0"] o'clock in the evening, and my rest period is over by morning, and so, to my greatest regret, I can visit you on Tuesday evening, but only late, I will not get home [sooner], my sweet. Write and tell me when you are leaving the Pásztoris'. Just stay, my sweet, as long as you can, have a good time, since I cannot have a good time with you. My sweet, when you are having a good time, think of your admirer, who thinks about you so much. God be with you, my sweet. Your admirer, Feri.

Stamp square: I kiss you countless times, your faithful sweetheart, Feri.

## Slovak

Moja milovaná sladká jediná nádej! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. S ľútosťou Vám musím oznámiť, že to, čoho som sa tak bál, sa stalo, lebo ma pridelili na taký vlak, ktorý sa vracia večer o 7 [napísané „7 0"] hodine, a do rána sa mi skončí oddych, a tak Vás, na moju najväčšiu ľútosť, môžem navštíviť v utorok večer, ale až neskoro, skôr domov neprídem, drahá. Napíšte mi, kedy odchádzate od Pásztoriovcov. Len zostaňte, drahá, kým sa dá, zabavte sa dobre, keď už ja sa s Vami nemôžem zabávať. Drahá, keď sa budete dobre zabávať, myslite na svojho ctiteľa, ktorý na Vás toľko myslí. S Bohom, drahá. Váš ctiteľ Feri.

V štvorci na známku: Bozkávam Vás nespočetnekrát, Váš verný milý Feri.

## Uncertainties

The writer drops and repeats letters; the ledger keeps what is written and the normalization is editorial.

1. **Unread pencil marks in the address (not cipher).** The plain pencil address reads Szépreményű Tóth Jolánka úrleánynak, Budapest, Petőfi … 10 or 16 (street word and number partly under the portal seal). Below it one more short pencil line runs under the seal to the right edge; even after colour separation neither solver nor reviewer can read it (one or two words, ending roughly "-lleg…" or "-hegy"). A small separate pencil mark at the extreme right edge above the end of row 23 (roughly "Hé" or "Hö") is also unread; it may be the end of that line or a further note. Both are address matter in plain writing, not message clauses; they are not read here.
2. **Row 9 "7 0 orakor".** The digit 7 and an open 0 are plain figures, followed by plain cursive *orakor* (órakor). I print them as written. The time is taken as 7 o'clock; why the 0 stands there (for example a false start, or "7 ó") is not known. The subject of *jön vissza* is taken as the train.
3. **Row 15/16 `hasz | toriektol` = *Pásztoriéktól*.** Signs h/p a s z, then t o r i e k t o l, all clear. Taking the h/p near-homograph as p gives the surname straight through, with no emendation: "from the Pásztoris". The name Pásztori occurs in this correspondence on HCP1290 (*a Pásztorinéhoz*). That it is the same household, and that Jolánka was staying with them at the Budapest address, is a hypothesis. The first reading of round 1 (*haza Toriéktól*) is withdrawn: see the response to review 1.
4. **Row 13/14 `de csak keson nem erkezek haza`.** All signs read. The clause order is odd: I read "but only late, I won't get home [sooner]". The alternative is that *nem* is a slip for "csak későn érkezek haza". Either way he comes late. *de* rests on word sense: the first sign is the tick plus long stroke shared by d and h/p.
5. **Near-homographs resting on word sense.** h/p: p in *pihenőm* (row 10, the first of its two h/p signs; literal `hihenöm`) and *Pásztori-* (row 15); h everywhere else. The ledger and the literal rows print h for this sign class throughout. g against d: *regelre* (row 9), the first g of *legnagyobb* (row 11, shaped close to h/d), *ameddi* (row 17). d against h/p: *de* (row 13; the reviewer types this sign as tall + tick, h/p, the solver as d, and only *de* gives a word), first h of *hoz* in *vonathoz* (row 7, a dark, blunt-headed sign). The i of *vissza* (row 9) is a closed loop with a cross stroke and no dot, read i by word sense (o would give *vosza*).
6. **Row 22 stray sign.** Between *gondol* and *kodom* stands a tick plus long stroke with no letter value in *gondolkodom*; printed {?} and dropped as a false start. Literal *gondolhkodom* if taken as h.
7. **Row 21 `imdojarki`.** Same word as the signature *imadoja*, but written without the a after m and without final a: normalized *im[á]dójár[a], ki*. Row 22 `ij` = *ily* (the writer's l-j spelling, as in `ojan` = olyan); the j is slanted.
8. **Stamp square.** Row 4 `szo{r|h}ű`: after *szo* a reduced tall stroke with a foot, then a cross with a heavy mark over it. Either *szor* + *ű* with h omitted, or *szo* with r omitted + *hű*. Normalized *számtalanszor, hű* either way. The k of *csoko* (a loop shape), the t of *mtalan* and the r i of *feri* are cursive variants read by word sense.
9. **Other spellings normalized.** Missing letters (bracketed in the normalized text): `szertet` → szer[e]tet[t]; `kel` → kel[l]; `bekövetkezet` → bekövetkezet[t]; `visza` → vis[s]za; `regelre` → reg[g]elre; `keden` → ked[d]en; `latoga|hatom` → látoga[t]hatom (a t lost at the row break, rows 12/13); `mikomegy` → miko[r] megy; `amedi` → amed[d]i[g]; `mulason` → mulas[s]on. Letters changed or removed (not bracketed): `emitöl` → [a]mitől (written e); `enynyira` → ennyire; `ojan` → olyan; `mararadjo|non` → maradjon ön (repeated *ar*, ö without visible dots); `ededesem` → édesem (repeated *ed*); `veledesem` → vele, édesem (one e sign serves both). Row 12 has a loop written over two strokes in *latoga*, read o. Accents are mostly not visible and are supplied.
10. **Date.** The postmark shows BUD[APEST] and 13 (perhaps the year 1913 or the day); no full date is legible. The printed verse on the picture side is a commercial caption, not part of the message. Sender Feri is the signature; other cards' Feri is the same name, identity not proven.

## Why it is correct

- The key, transferred unchanged, turns every sign of all rows into Hungarian; only one stray sign is left without a value (item 6).
- The opening *Kívánom, hogy a legjobb … találja soraim* and the closing *Isten vele* are the family's formulas (HCP1223). They were not assumed: every sign was read, and the signs give them.
- The text has a specific, unforced story: the writer is ordered onto a train run, his rest ends by morning, the visit shrinks to a late Tuesday evening, and she should stay and enjoy herself. Trains and travel recur in the family (HCP1222, 1223, 1227, 1230).
- Repeated words decode identically: *édesem* ×4 (rows 14, 17, 20, 23, plus *édes* in row 1), *hogy* ×3, *megy/meg*, *mulat-* ×3, *imádó-* ×2.

## Response to review 1

Verdict REVISE; all five findings are addressed. No sign and no key value changed; `work/ledger-opus.txt` has only a new comment line. The command in Reproduction was re-run after the changes: all four hashes OK, literal rows unchanged, new normalized text printed.

1. **Row 15/16 misread (major): fixed, I agree.** I re-read the reviewer's `z_r15end.png` and `z_r16.png`: the signs are as ledgered (h/p, a, s, z; t, o, r, i, e, k, t, o, l). My error was choosing h for the near-homograph and forcing *haza* with an invented Tori. NOTES says "surname" was tested, but Pásztori was not. With p the row reads *Pásztoriéktól* with no emendation, and the writer's plain z in *haza* (row 14) against the two-sign sz here supports it. Hungarian, English, Slovak, normalized file, ledger comment, items 3 and 5 are updated; the name is on HCP1290. The change touches this one phrase, so I do not count it as a substantial change of the reading.
2. **Dropped t and brackets (minor): fixed.** *látoga[t]hatom* is printed and listed. Brackets are now applied consistently for letters with no sign, the rule is stated above the Hungarian, and item 9 separates missing letters from changed ones. That pass also corrected *Szeret[e]tt* to *Szer[e]tet[t]* and *imádójára* to *im[á]dójár[a]*, matching the literal row.
3. **Count claim (minor): fixed.** *édesem* ×4 plus *édes*.
4. **Address disclosure (minor): fixed.** Item 1 now gives both unread items, the last pencil line and the corner mark. I looked at the hires scan and at the reviewer's colour separation and could not read them either. They remain unread and are carried into the report. They are plain address matter of one short line, not a message clause.
5. **Wording (minor): fixed.** Item 5 is rewritten with all h/p calls in one place: p in *pihenőm* and *Pásztori-*, h elsewhere.

## Stamp-box message (2026-11-03)

Stamp-box audit by Claude Opus 5.5 on the hires original `work/hires/cpc_--_HU__HU_Budapest_jolanka-62_adr.jpg` (crops in `work/stamp-2026-11-03/`: `stamp_box_2x.png`, `stamp_half0_3x.png`, `stamp_half1_3x.png`). The printed dotted stamp box at the top right is bare paper: the stamp has been lifted, and the postmark (BUD…, 13) stops at the box's left edge, so a stamp covered the box when the card was cancelled. Under it the sender wrote six short rows **in the cipher signs** (no plain Hungarian in the box). These rows were already in the round-1 reading and ledger (rows S1–S6 of `work/ledger-opus.txt`, decoded by the reproduction command); this audit re-read every sign from the pixels with the card's key and confirms them unchanged.

- Literal: `csoko / lomsza / mtalan / szo{r|h}ű / kedvese / feri`
- Hungarian (normalized): Csókolom számtalanszor, hű kedvese Feri.
- English: I kiss you countless times, your faithful sweetheart, Feri.
- Slovak: Bozkávam Vás nespočetnekrát, Váš verný milý Feri.

Unread: nothing; every sign in the box has a value. The one uncertain sign is still row 4's reduced tall stroke with a foot (r or h, item 8 above); the normalization is the same either way. Cursive variants (k as a loop shape in row 1, t in row 3, r and i in row 6) are read with word sense, as disclosed in item 8.
