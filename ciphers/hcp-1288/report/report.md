# HCP 1288 (cpc_1913--13_HU__HU_Jasz Arokszalas_jolanka-112): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 26 main rows and the 7 rows under the stamp, 784 written signs) with small disclosed residuals; independent review 1 verdict REVISE, one misread clause corrected.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1288 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1288), portal name cpc_1913--13_HU__HU_Jasz Arokszalas_jolanka-112, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt proceedings, https://ecp.ep.liu.se/index.php/histocrypt). When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side shows a young woman in a wide hat holding a letter to her lips. It carries only a printed title and verse in clear, *Kis levélke, drága kis levélke…* ("Little letter, dear little letter…"), and no cipher text.

The whole message is on the address side, in green ink and invented signs: 26 rows, of which rows 23 to 26 run across the full width of the card, and 7 short rows in the space under the stamp, which has since been removed. The clear address, in the same hand, reads *Szépreményű / Tóth Jolánka / úrleánynak / Jász-Árokszalás* (so spelled, for Jászárokszállás): "To the promising young lady Jolánka Tóth". The first word runs through the cancellation.

There are two postal marks. A boxed mark reads RÁKOSPALOTA-ÚJP. A round cancellation has rim letters reading (…)SZ ÁRO(…), compatible with Jász-Árokszállás, and a date line of which only partial characters survive. A separate large numeral 13 stands beside it; its meaning is unknown. No date can be read from the card. The year 1913 comes only from the file name.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the two postal marks and the clear address (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1290, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery. The same signature Feri appears on HCP 1216, but it is not proved that he is the same person.

## Method

- **Transcription and decipherment (2026-10-30), Claude Opus 5.5:** the key of HCP 1216 was applied unchanged; no new sign value was needed. Every row was read on enlarged crops of the high-resolution address scan and recorded as a manual sign ledger, one token per written sign (`work/ledger.txt`). No OCR was used.
- **Review (2026-10-30), a separate Claude Opus 5.5 agent:** re-ran the command, decoded the ledger with its own script and a retyped key, got the same literal output, and compared all 33 rows with its own crops sign by sign. It found one misread clause and seven smaller points.
- **Prior work.** There was none on this number. The family key comes from finished sister cards, whose earlier passes were by an OpenAI GPT solver and Claude Opus 5.5. The portal attaches no solution, and none was used. No web search for a published reading of this card was made; the AI Decipherment Register had no record of it on 2026-10-30.

The writer spells by ear and carelessly: he repeats syllables, drops letters and leaves most acute accents invisible at this scan's quality. The literal decipherment is kept as written; the normalized Hungarian is editorial.

## Key

Hungarian simple monoalphabetic substitution with invented signs. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma / corner | t |
| long stroke + short tick | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short tick | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

The d has its tick on the left of the long stroke, and h/p has it on the right; h and p are told apart only by the word. Dots over o and u give ö and ü. On this card g and y are written as two separate signs in *gy*.

## Plaintext

Literal decipherment, one row per written line. `{|}` is a stroke with no certain value.

```text
01 szeretetedesegyetlenremenyem
02 varvavartsoraitmegkaptam
03 mitkoszönokszépenigazan
04 örülökhogyszerencsesenmeg
05 erkezettcsakaztsajnalom
06 hogyénnemerkezhettem
07 magmagavaledesemked
08 vesjolankaménmagatolnem
09 sajnaloksemmiköltségetami
10 tölemtelikszivesenaldozom
11 magárabárigazhogyedigmég
12 edeskevesetköltöttemdeazt
13 vegyeroszanyagihejzetemnek
14 remélemhogymegviradmégenrám
15 istalanéshelyrepotolhatom
16 mitedigmentettemigazanörü
17 lökhogybelattaedesemhogy
18 levagyogkotelezvedebiztas
19 saazatudathogygondolatom
20 mindigmaganalvanédesemés
21 remjükazistentölhogymég
22 öszehöozehozasorskezemitaligvarok
23 édesjolankamaztaparboldognapotbizonyénisnehezenfelej
24 temdesajnosamiboldogviszontlatasunknakmindignehezel
25 valásavegekedvesemalelembekérdéseimrelegyenszives
26 valaszolnimertnagyonerdekelistenveleédesemferi
S1 istenvele
S2 edem{|}cso
S3 kolom
S4 szamta
S5 lanszor
S6 hükedves
S7 seferi
```

**Hungarian (normalized):** Szeretett édes egyetlen reményem! Várva várt sorait megkaptam, mit köszönök szépen. Igazán örülök, hogy szerencsésen megérkezett. Csak azt sajnálom, hogy én nem érkezhettem magával, édesem. Kedves Jolánkám! Én magától nem sajnálok semmi költséget, a mi tőlem telik, szívesen áldozom magára. Bár igaz, hogy eddig még, édes, keveset költöttem, de azt vegye rossz anyagi helyzetemnek. Remélem, hogy megvirrad még énrám is. Talán és helyre pótolhatom, mit eddig nem tettem(?) [literally: mentettem]. Igazán örülök, hogy belátta, édesem, hogy le vagyok kötelezve, de biztassa az a tudat, hogy gondolatom mindig magánál van, édesem, és reméljük az Istentől, hogy még összehoz a sors keze, mit alig várok. Édes Jolánkám! Azt a pár boldog napot bizony én is nehezen felejtem, de sajnos a mi boldog viszontlátásunknak mindig nehéz elválás a vége. Kedvesem, a le[ve]lembe[li] kérdéseimre legyen szíves válaszolni, mert nagyon érdekel. Isten vele, édesem. Feri.

Under the stamp: Isten vele. Éd[es]em(?), csókolom számtalanszor. Hű kedvese, Feri.

**English:** My beloved sweet only hope! I have received your long-awaited lines, for which I thank you very much. I am truly glad that you arrived safely. I only regret that I could not arrive with you, my sweet. Dear Jolánka! I grudge you no expense; whatever I can afford I gladly spend on you. It is true that so far, my sweet, I have spent little, but put that down to my poor financial situation. I hope the day will still dawn for me too. Perhaps I can also make good what I have not done so far (reading proposed; see Uncertainties). I am truly glad that you have understood, my darling, that I am bound by obligation, but let the knowledge encourage you that my thoughts are always with you, my darling, and let us hope to God that the hand of fate will yet bring us together, which I can hardly wait for. Sweet Jolánka! Those few happy days I too will surely find hard to forget, but unfortunately our happy reunion always ends in a hard parting. My dear, please answer the questions in my letter, because they interest me very much. God be with you, my darling. Feri.

Under the stamp: God be with you. My darling(?), I kiss you countless times. Your faithful sweetheart, Feri.

**Slovak:** Moja milovaná, sladká, jediná nádej! Dostal som Vaše dlho očakávané riadky, za ktoré pekne ďakujem. Naozaj sa teším, že ste šťastne docestovali. Len to ľutujem, že som nemohol prísť s Vami, drahá. Milá Jolánka! Ja Vám neľutujem nijaké výdavky, čo mi prostriedky dovolia, to na Vás rád obetujem. Je pravda, že doteraz, sladká, som minul málo, ale pripíšte to mojej zlej finančnej situácii. Dúfam, že aj mne ešte svitne. Možno aj napravím, čo som doteraz neurobil (navrhované čítanie, pozri neistoty). Naozaj sa teším, že ste pochopili, drahá, že som viazaný povinnosťou, ale nech Vás povzbudí vedomie, že moje myšlienky sú stále pri Vás, drahá, a dúfajme v Boha, že ruka osudu nás ešte zvedie dokopy, na čo sa už neviem dočkať. Sladká Jolánka! Tých pár šťastných dní aj ja veru ťažko zabudnem, ale žiaľ, naše šťastné stretnutie sa vždy končí ťažkou rozlúčkou. Moja milá, buďte taká dobrá a odpovedzte na otázky v mojom liste, lebo ma veľmi zaujímajú. S Bohom, drahá. Feri.

Pod známkou: S Bohom. Drahá(?), bozkávam Vás nespočetnekrát. Váš verný milý, Feri.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1288/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the four scans, decodes the manual sign ledger `work/ledger.txt`, prints the 33 literal rows and 784 as the sign count, and prints the normalized text `work/normalized.txt`. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

- **Row 16, `mentettem`.** The letters are clear except the first sign, a heavy overwritten joined form. It is read as m, with n not excluded. Taken at face value *mentettem* ("I saved") does not fit after *pótolhatom* ("make good"). The text above uses **nem tettem ("I have not done"), a proposal made after the review, which the reviewer has not assessed.** It fits the clause exactly. It would be either a spelling by ear, since *nem* before t is pronounced [nen], with the heavy sign taken as n; or a swap of m and n, which the overwriting could reflect.
- **Row 22, restart.** The literal is `öszehö` + `ozehoz`. The sign after `ö` is a heavy cursive loop at the ink stain, read as o. Taken as a false start and restart, normalized *összehoz*; this is an interpretation, supported by *a sors keze* that follows.
- **Under the stamp, row S2.** After *ede* come a heavy m-form and a separate stroke of no certain value, possibly a correction of s. Normalized *Éd[es]em(?)*. The cs of *csókolom* rests on word sense; *kolom* is clear.
- **Row 25, `alelembe`.** The sign before `e m` is a shortened wave with a separate tick, read as l; v is not excluded. Normalized *a le[ve]lembe[li]*, restoring a writer's slip. The sense is unaffected.
- **Under the portal stamp.** The `s` of *is*, the `l` of *felej-* (row 23), `dig` of *mindig* (row 24) and `gy` of *legyen* (row 25) are partly hidden. They are read from what shows, and the words confirm them.
- **Calls resting on word sense.** *pótolhatom*, *pár*, *napot* and *megkaptam* have p against h; *gondolatom* has d. *várok* (row 22) has an r sign close to t, decided by *alig várok*. Row 5 *érkezett*: the first t has a short mid-stroke like r. Row 2: the first sign is a heavy overwritten v.
- **Row 15, `és`.** *Talán és helyre* is kept literally; *és* may stand for *is*.
- **Writer's spellings normalized.** *szeretet*→szeretett, *koszönok*→köszönök, *mag magával* (false start), *edig*→eddig, *rosz*→rossz, *hejzetemnek*→helyzetemnek, *megvirad*→megvirrad, *remjük*→reméljük, *vagyog*→vagyok (clear g sign), *biztas|sa* and *kedves|se* (s repeated at a row break), *öszehoz*. Most accents are invisible and are supplied. Row 17: a heavy smear lies under the second t of *belátta*; the reading is unaffected.
- **Date and identity.** See "Origin and context". The year is not confirmed by the card, and the sender's identity with the Feri of other cards is not proved.

## Review summary

Review 1 (a separate Claude Opus 5.5 agent) returned **REVISE**. The cipher, the key and almost all of the reading stood. It confirmed the command, the literal text with an independent decoder, and the base signs of all 33 rows; faint accents were not audited individually.

What changed because of it:

- **Major, row 24.** The handover read `amibol hog` and defended it as an awkward word. The fourth sign after *a mi* is d, with its tick on the left, the same form as *boldog* in row 23. The clause is now *de sajnos a mi boldog viszontlátásunknak…*, and the earlier claim that the word could not be improved was withdrawn.

![Row 24: b, o, l, the d with its tick on the left of the heavy stroke, o, g (review/work/crops/z24.png)](../review/work/crops/z24.png)

- **Rows 24-25.** The supplied `[a]` and *elválása* were removed; *nehéz elválás a vége* needs nothing added.
- **Address side.** The green word, first described as a faint pencil word, is the first line of the address, *Szépreményű*. The second cancellation was recorded, with no date claimed.
- **Row 22.** The sign recorded as unreadable became an o-class sign, still an interpretation.
- **Row 25.** The restoration was lightened to *a le[ve]lembe[li]*, and v was named as an alternative.
- **Bookkeeping.** A form that does not exist in the ledger (*hög*) was deleted, the smear in row 17 was disclosed, and the claim about unreadable signs was brought into step with the text.

The row 16 proposal *nem tettem* came after the review and has not been checked by it. The reviewer upheld the signs of that word and left its sense open.

The reviewer could not verify the year, the accents, the identity of Feri or the sense of row 16, and relied on the captured portal metadata.

## Credits

Tomáš Pavuk, human solver. Transcription, decipherment with the transferred family key, and this report by Claude Opus 5.5. Independent review by a separate Claude Opus 5.5 agent. Family key from the finished Jolánka cards (see `ciphers/hcp-1216/`).

## Sources

- HC Portal, cryptogram 1288: https://crypto.hcportal.eu/dashboard/cryptograms/1288 (metadata in `source/metadata.md`).
- Scans: `source/picture-large.jpg`, `source/address-large.jpg`, and the un-converted originals in `work/hires/` (URLs and hashes in `SOURCES.md`).
- Sister cards in this repository, chiefly `ciphers/hcp-1216/`, `ciphers/hcp-1212/` and `ciphers/hcp-1290/`.
