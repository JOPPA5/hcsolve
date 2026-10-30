# HCP 1293 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-76): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (33 written rows, 523 signs, all mapped); independent review 1 verdict REVISE, all findings addressed.** A few words and one sentence remain open and are listed under Uncertainties. Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1293 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1293), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-76, part of Tobias Schrödel's collection of cryptographic postcards (see the HistoCrypt proceedings, https://ecp.ep.liu.se/index.php/histocrypt). When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language unknown, recipient Tóth Jolánka, with no transcription or solution attached. The language turns out to be Hungarian. A check of the AI Decipherment Register the same day found no record for this card.

The picture side is a printed tinted photograph of a young man and a young woman speaking by telephone, with printed gilt captions in Hungarian (they include *Mit kívánsz édesem?*, "What do you wish, my sweet?"). It carries no cipher text.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address side carries the plain address, read approximately as *Szépreményű Tóth Jolánka úrleánynak, Budapest, Petőfi u. 16*, with a faint last line beginning *ház-* (perhaps *házfelügyelő*). This address was not needed for the decipherment and is not claimed exactly. Budapest differs from Jászárokszállás, the place in the portal's file name. The stamp is torn off and the postmark is cut, so the card has no legible date.

![Address side with the cipher text in violet pencil (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards to Jolánka Tóth, several of which are finished in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key, so this card was read with a **known, transferred key**, not by a new key recovery. It is signed Feri, like HCP 1216.

## Method

The key was taken from the finished sister cards, in the sign classes of HCP 1216. No value had to be changed for this card.

All work was done by Claude Opus 5.5 on 2026-10-30; there was no earlier work on this number. The solver read every row on enlarged crops of the un-converted address scan and recorded one token per written sign in a ledger (`work/ledger.txt`). The transcription is manual, with no OCR. The writing under the green printed triangle in the stamp square was read on a blue-minus-green image, which separates pencil from print.

The reading path had to be traced on the card, and it is forced by the sense:

1. 23 rows on the message half, the last running along the bottom of the whole card.
2. Round the corner and up the right edge (E1).
3. An arrow at the top right leads to the top margin, written upside down, right to left (T1).
4. That ends at a ruled box with two short rows, turned 90° (B1, B2).
5. A signature block of six short rows stands in the stamp square (S1–S6), upright.

A separate Claude Opus 5.5 agent reviewed the work. It made its own crops, wrote its own transcription by sign class, and decoded it with a key typed from the HCP 1216 table.

## Key

Hungarian simple monoalphabetic substitution with invented signs. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S-shape) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma / corner | t |
| long stroke + short tick | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short tick | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | opposed bowls | cs | | |

On this card:

- **gy** is written as two signs, g + y, not as the joined digraph of HCP 1216.
- **o** (plain loop) and **i** (loop with a crossing stroke and a tick above) are close, and the mark decides.
- **ö** has two dots.
- The writer's **j** stands for *ly* (*ojan*, *ijen*).
- **h** has its short tick on the right of the tall stroke and **d** on the left. That rule has three exceptions, listed under Uncertainties.

## Plaintext

Literal decipherment, row by row, as printed by the reproduction command:

```text
01 szeretetedesegyetlen            13 mentemszolgalatba
02 remenyemneharagudjonram         14 esepenbeleptemmarszo
03 hogyojansokavarakoz             15 litottakisanevem
04 tattamdeijensokameg             16 esrögtöneluttam
05 sohasemtartottavezen            17 mitnemiskelmonda
06 lesmintmostmikorvege            18 nomdragacsillagom
07 voltelmentemenedesem            19 aligvaromhogy
08 magatkerestemdenemta            20 viszszajöjeklegjobb
09 laltamesaztgondol               21 szeretnekedesemezalatta
10 tamedesemhogyhaza               22 arövididoalatmindig
11 mentekdesenishazamen            23 maletalenikerjekibocsanatomathogyelsembu
12 tematöltöztemes                 E1 csuztamviszontlatasramikora
T1 mikorigerthavalamil   B1 közbe   B2 nemjön
S1-6 csoko lom szam talan szor feri
```

Normalized Hungarian (editorial; square brackets mark letters not on the card):

**Szeretett édes egyetlen reményem! Ne haragudjon rám, hogy olyan soká várakoztattam, de ilyen soká még soha sem tartott a vezén[y]lés, mint most. Mikor vége volt, elmentem én, édesem, magát kerestem, de nem találtam, és azt gondoltam, édesem, hogy hazamentek, de [s] én is hazamentem, átöltöztem és mentem szolgálatba, és éppen beléptem, már szólítottak is a nevem[en], és rögtön el[f]uttam. Mit nem is kell mondanom, drága csillagom, alig várom, hogy visszajöjjék. Legjobb[an] szeretnék, édesem, ez alatt a rövid idő alatt mindig mellette le[n]ni. Kérje ki bocsánatomat, hogy el sem búcsúztam. Viszontlátásra, mikor[ra] – mikor ígért, ha valami[l] közbe nem jön.**

**Csókolom számtalanszor. Feri**

English translation: **Beloved sweet, my only hope! Do not be angry with me for keeping you waiting so long, but the duty assignment has never lasted as long as it did now. When it was over I went off, my darling, and looked for you, but did not find you, and I thought, my darling, that you had gone home, so I too went home, changed and went on duty, and just as I walked in they were already calling my name, and I ran off at once. I need hardly tell you, dear star of mine, that I can scarcely wait for you to come back. Most of all, my darling, I would like to be beside you all the time during this short while. Please ask pardon for me that I did not even say goodbye. Until we meet again, when you promised, if nothing comes up.**

**I kiss you countless times. Feri**

Slovak translation: **Milovaná sladká, moja jediná nádej! Nehnevajte sa na mňa, že som Vás nechal tak dlho čakať, ale ešte nikdy netrvala služba tak dlho ako teraz. Keď sa skončila, odišiel som, drahá, hľadal som Vás, ale nenašiel som Vás, a myslel som si, drahá, že ste odišli domov, nuž aj ja som šiel domov, prezliekol som sa a šiel do služby, a práve keď som vošiel, už ma volali po mene, a hneď som odbehol. Ani Vám nemusím hovoriť, drahá hviezdička moja, že sa sotva dočkám, kým sa vrátite. Najradšej by som bol, drahá, počas tohto krátkeho času stále pri Vás. Poproste za mňa o odpustenie, že som sa ani nerozlúčil. Dovidenia, kedy ste sľúbili, ak do toho nič nepríde.**

**Bozkávam Vás nespočetnekrát. Feri**

The writer addresses her formally (*maga*, third-person verbs), as in the other cards of the family. The content, a long duty and a roll call, suggests a man in service; nothing on the card says what service.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1293/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the four image files, decodes the manual ledger `work/ledger.txt`, and prints the literal rows and the normalized text. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

**Signs read by sense against their shape.** There are three.

- Both p of row 14 (*épen*, *beléptem*) have the d shape, with the tick on the left. Taken literally they give *eden*, *beledtem*.
- The d of row 4 *de* has the h shape, with the tick on the right. The same slip occurs on HCP 1216 row 5.

The ledger marks these three signs.

![Row 14 with the two d-shaped p signs (review/work/crops/p14.png)](../review/work/crops/p14.png)

**Sentence with an open reading.** Row 23 reads k-e-r-j-e-k-i. The preferred division is *kérje ki bocsánatomat*: he asks her to apologise for him, presumably to those who went home with her, since *hazamentek* is plural. It leaves no stray sign and explains the possessive *-omat*, but *kikér* with *bocsánat* is not the usual phrase and needs a native reader's judgment. The alternative is *kérjek [i] bocsánatomat*, "let me ask your forgiveness", with one stray i and a strange *-omat*.

**Other sense readings and damaged places:**

- Row 11 *de s én is*: literal *desenis*, an odd pleonasm. The blot before it is the most damaged sign of the card. If it is a cancelled sign, *hazament, édes, én is hazamentem* is possible. The signs do not decide.
- Row 6 *mikor*: the k has a closed lower bowl, near the b sign.
- Row 8 *kerestem*: the second e has its bars joined into a loop.
- Row 8 *magát* and the k of row 11 *mentek* lie in moisture stains.
- Row 21 end: rubbed. The *tt* of *alatta* cannot be counted and is a sense reading. The final a repeats the a of row 22 and is dropped.
- Row 22 *idő*: the ő is overwritten by bar-like strokes.
- Row 23 *maleta*: normalized *mellette*. The a-signs stand where standard spelling has e.
- S3–S5 lie partly under the green triangle.

**Letters supplied or dropped in normalization:**

- *vezén[y]lés*
- *nevem[en]*
- *el[f]uttam*, colloquial for *elfutottam*
- *legjobb[an]*
- *le[n]ni*
- Row 20 *visszajöjjék* ("that you come back") could also be *visszajöjjek* ("that I come back"), because accents are not visible. The former fits the promised meeting.
- E1 ends *mikora* and T1 starts *mikor* again: a restart or *mikorra*.
- A wave after *valami* (*valamil*, touching the box line) makes no word; it may be a slip or a flourish.
- Most acute accents are not visible and are supplied.

**Not established:** the date, the sender's full identity, the exact address. No search for a prior publication was made beyond the portal status and the AI Decipherment Register.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. It ran the command, read all rows from its own crops and decoded them with its own script: 523 signs in 33 rows, all mapped, differing from the solver's ledger in four rows only. It confirmed the family key, the reading path and that the plaintext is natural colloquial Hungarian, and it agreed on most of the hard spots. Its six findings, all addressed:

1. **Row 23 had one n too many in the ledger** (major). The card has *leni*, so the second n is now supplied in brackets, and the claim that no sign was restored was withdrawn.
2. **B1 *közbe* has its ö dots** (minor). The solver had missed them.
3. **The h/p/d statement was wrong** (minor). The solver had said the p of row 14 looked like h, but it has the d shape. The readings stand, with the correct basis stated.
4. **Row 23 word division** (major). The solver's *kérjek i bocsánatomat* is replaced by *kérje ki bocsánatomat* as preferred reading, which removed a "meaningless sign".
5. **Row 11** (minor). The alternative *hazament, édes* is now disclosed.
6. **vezén[y]lés** (minor). The y is now bracketed.

In all, one letter was removed from the literal text, one sign gained its dots, and one sentence was re-divided and retranslated. After the corrections `work/decode.py` still runs and its hashes check out. The reviewer could not verify the accents, the date, or the native idiom of *kérje ki bocsánatomat* and *a nevem*.

## Sources

- HC Portal record 1293, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1293 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3939/conversions/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-76_pic-large.jpg, original https://api.hcportal.eu/media/3939/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-76_pic.jpg.
- Address side: https://api.hcportal.eu/media/3940/conversions/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-76_adr-large.jpg, original https://api.hcportal.eu/media/3940/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-76_adr.jpg.
- Family key: ciphers/hcp-1216 and sister cards in this repository.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
