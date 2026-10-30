# HCP1288 — Feri to Jolánka Tóth: thanks for a letter, money worries, a hard parting

**Status: complete reading with small disclosed residuals; review 1 (REVISE) addressed.** Claude Opus 5.5, 2026-10-30.

Credit: solved here by Claude Opus 5.5; no earlier work on this number. The key comes from the finished Jolánka family cards (hcp-1216 and sisters, whose earlier passes were by the OpenAI GPT solver and Claude Opus 5.5). The portal shows *Not solved* with no attached solution or transcription, and no published solution was used or seen. This card was not checked by web search.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs, the Jolánka postcard family. The key of hcp-1216 was taken over unchanged; no new sign value was needed (see the table in `ciphers/hcp-1216/SOLUTION.md`). Dots over o/u give ö/ü. On this card g and y are written as two separate signs in *gy* (hogy, egyetlen). Ciphertext is 26 main rows (rows 23-26 run across the full card width) plus 7 rows in the space under the stamp, 784 written signs in the ledger. The address and the printed poem on the picture side are in clear.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1288/work/decode.py
```

It checks the SHA-256 of all four scans, decodes `work/ledger.txt` and prints the literal rows and `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the hi-res address scan (`work/crop.py`, `work/crops/`), not OCR.

## Literal decipherment

```
01 szeretetedesegyetlenremenyem        14 remélemhogymegviradmégenrám
02 varvavartsoraitmegkaptam            15 istalanéshelyrepotolhatom
03 mitkoszönokszépenigazan             16 mitedigmentettemigazanörü
04 örülökhogyszerencsesenmeg           17 lökhogybelattaedesemhogy
05 erkezettcsakaztsajnalom             18 levagyogkotelezvedebiztas
06 hogyénnemerkezhettem                19 saazatudathogygondolatom
07 magmagavaledesemked                 20 mindigmaganalvanédesemés
08 vesjolankaménmagatolnem             21 remjükazistentölhogymég
09 sajnaloksemmiköltségetami           22 öszehöozehozasorskezemitaligvarok
10 tölemtelikszivesenaldozom           23 édesjolankamaztaparboldognapotbizonyénisnehezenfelej
11 magárabárigazhogyedigmég            24 temdesajnosamiboldogviszontlatasunknakmindignehezel
12 edeskevesetköltöttemdeazt           25 valásavegekedvesemalelembekérdéseimrelegyenszives
13 vegyeroszanyagihejzetemnek          26 valaszolnimertnagyonerdekelistenveleédesemferi
under stamp: istenvele / edem{|}cso / kolom / szamta / lanszor / hükedves / seferi
```

## Hungarian (normalized)

Szeretett édes egyetlen reményem! Várva várt sorait megkaptam, mit köszönök szépen. Igazán örülök, hogy szerencsésen megérkezett. Csak azt sajnálom, hogy én nem érkezhettem magával, édesem. Kedves Jolánkám! Én magától nem sajnálok semmi költséget, a mi tőlem telik, szívesen áldozom magára. Bár igaz, hogy eddig még, édes, keveset költöttem, de azt vegye rossz anyagi helyzetemnek. Remélem, hogy megvirrad még énrám is. Talán és helyre pótolhatom, mit eddig nem tettem(?) [literally: mentettem]. Igazán örülök, hogy belátta, édesem, hogy le vagyok kötelezve, de biztassa az a tudat, hogy gondolatom mindig magánál van, édesem, és reméljük az Istentől, hogy még összehoz a sors keze, mit alig várok. Édes Jolánkám! Azt a pár boldog napot bizony én is nehezen felejtem, de sajnos a mi boldog viszontlátásunknak mindig nehéz elválás a vége. Kedvesem, a le[ve]lembe[li] kérdéseimre legyen szíves válaszolni, mert nagyon érdekel. Isten vele, édesem. Feri.

Under the stamp: Isten vele. Éd[es]em(?), csókolom számtalanszor. Hű kedvese, Feri.

## English

My beloved sweet only hope! I have received your long-awaited lines, for which I thank you very much. I am truly glad that you arrived safely. I only regret that I could not arrive with you, my sweet. Dear Jolánka! I grudge you no expense; whatever I can afford I gladly spend on you. It is true that so far, my sweet, I have spent little, but put that down to my poor financial situation. I hope the day will still dawn for me too. Perhaps I can also make good what I have not done so far (reading proposed; see uncertainty 1). I am truly glad that you have understood, my darling, that I am bound by obligation, but let the knowledge encourage you that my thoughts are always with you, my darling, and let us hope to God that the hand of fate will yet bring us together, which I can hardly wait for. Sweet Jolánka! Those few happy days I too will surely find hard to forget, but unfortunately our happy reunion always ends in a hard parting. My dear, please answer the questions in my letter, because they interest me very much. God be with you, my darling. Feri.

Under the stamp: God be with you. My darling(?), I kiss you countless times. Your faithful sweetheart, Feri.

## Slovak

Moja milovaná, sladká, jediná nádej! Dostal som Vaše dlho očakávané riadky, za ktoré pekne ďakujem. Naozaj sa teším, že ste šťastne docestovali. Len to ľutujem, že som nemohol prísť s Vami, drahá. Milá Jolánka! Ja Vám neľutujem nijaké výdavky, čo mi prostriedky dovolia, to na Vás rád obetujem. Je pravda, že doteraz, sladká, som minul málo, ale pripíšte to mojej zlej finančnej situácii. Dúfam, že aj mne ešte svitne. Možno aj napravím, čo som doteraz neurobil (navrhované čítanie, pozri neistotu 1). Naozaj sa teším, že ste pochopili, drahá, že som viazaný povinnosťou, ale nech Vás povzbudí vedomie, že moje myšlienky sú stále pri Vás, drahá, a dúfajme v Boha, že ruka osudu nás ešte zvedie dokopy, na čo sa už neviem dočkať. Sladká Jolánka! Tých pár šťastných dní aj ja veru ťažko zabudnem, ale žiaľ, naše šťastné stretnutie sa vždy končí ťažkou rozlúčkou. Moja milá, buďte taká dobrá a odpovedzte na otázky v mojom liste, lebo ma veľmi zaujímajú. S Bohom, drahá. Feri.

Pod známkou: S Bohom. Drahá(?), bozkávam Vás nespočetnekrát. Váš verný milý, Feri.

## Uncertainties

Signs read on word sense or with a contextual call:

1. **Row 16 `mentettem`**: literal signs m-e-n-t-e-t-t-e-m. The first sign is a heavy, overwritten joined form, read as m (the same shape as the heavy m-form of S2), but n is not excluded; h/p is unlikely. The third sign is plainly two strokes, n. Taken at face value *mentettem* ("I saved") does not fit after *pótolhatom* ("make good"). Proposed by the solver after review 1, and not seen by the reviewer: *nem tettem* ("I have not done"), which fits the clause exactly. It would be either a phonetic spelling, since *nem* before t is pronounced [nen] and this writer spells by ear (*hejzetemnek*, *remjük*), with the heavy sign taken as n; or a swap of m and n, which the overwriting of the first sign could reflect. The literal letters stay `mentettem`; the normalized word is an interpretation and is marked (?).
2. **Row 22 restart**: literal `öszehö` + `ozehoz`. The sign after `ö` is a heavy cursive loop of the o class at the ink stain, read as o, directly followed by z, e, h, o, z. Taken as a false start *öszehö…* restarted as *(ö)zehoz*, normalized *összehoz*. This remains an interpretation of a sign in the stain; the following *a sors keze* supports it.
3. **Stamp row S2 `edem{|}cso`**: after *ede* comes a heavy joined m-form plus a separate stroke, then a V-shaped pair read as cs, then o. Normalized *Éd[es]em(?)* and *cs|ókolom*. *kolom* is clear; cs rests on word sense, and the m-form plus stroke has no certain value (it may be a correction of s). The dot of the first i in S1 is not visible.
4. **Row 24**: withdrawn after review 1. The earlier `amibol hog` was a misreading; see the response below.
5. **Row 25 `alelembe`**: the sign before `e m` is a shortened wave with a separate tick, read as l but not clearly so; v is not excluded (*levembe*). Normalized *a le[ve]lembe[li]* with the writer's omission restored, one supplied suffix. This is an interpretation of a writer's slip; the sense "the questions in my letter" stands either way.
6. **Stamp overlap (portal stamp over the ciphertext)**: row 23 `s` of *is* and `l` of *felej-*, row 24 `dig` of *mindig*, and row 25 `gy` of *legyen* lie under the portal's violet stamp and are partly hidden. They are read from what shows, and the words confirm them.
7. **Row 19 and 22**: the h/p class and r/t: *várok* (row 22) has an r sign with a weak middle stroke, close to t. *alig várok* decides it. Row 5 *érkezett*: the first t has a spurious short mid-stroke, like r. Row 2, first sign: heavy overwritten v.
8. **h/p and d/n calls resting on word sense**: *pótolhatom* (15), *pár*, *napot* (23), *megkaptam* (2) have p against h; *gondolatom* has d. They are chosen by the word. *szépen* has a clear p shape. *boldog* (rows 23, 24) is decided by the sign: the tick stands on the left of the long stroke.
9. **Row 15 `és`**: *talán és helyre* is kept literally; *és* may stand for *is*. Rows 24-25 divide directly as *nehéz el|válás a vége*, with nothing supplied.
10. **Writer's spellings normalized**: *szeretet*→szeretett, *koszönok*→köszönök (dots absent on two o), *mag magával* (false start *mag*), *edig*→eddig, *rosz*→rossz, *hejzetemnek*→helyzetemnek, *megvirad*→megvirrad, *remjük*→reméljük, *vagyog*→vagyok (clear g sign), *kötelezve* (o without dots), *biztas|sa* (s repeated at the row break), *öszehoz*, *kedves|se* (s repeated at the row break, stamp block). Row 16-17 *örü|lök* breaks across rows. Most accents are invisible and are supplied. Row 17: the second t of *belátta* has a heavy horizontal smear under it; the reading is unaffected.
11. Sender "Feri" is the signature; the same name signs hcp-1216, but identity is not proved. The postmarks do not give a date: the boxed mark reads RÁKOSPALOTA-ÚJP., and a second, round cancellation has rim letters reading (…)SZ ÁRO(…), compatible with Jász-Árokszállás, with a date line of which only partial characters survive, not enough to claim a date. A separate large numeral 13 stands beside it, meaning unknown. 1913 comes only from the file name.
12. Clear text on the address side, in green ink and the writer's hand: *Szépreményű / Tóth Jolánka / úrleánynak / Jász-Árokszalás* (so spelled, for Jászárokszállás). The first word runs through the cancellation, its opening *Sz* tangled with the postmark; the same address form appears on hcp-1212 and hcp-1290.

## Why it is correct

- A key taken over unchanged from finished sister cards turns all 33 rows into connected Hungarian, with no new value and one stroke of no certain value (`{|}` in S2). Two signs (row 16 first sign, row 22 heavy o) are contextual calls.
- The text was not fitted word by word: signs read independently gave long unforeseen phrases such as *költséget*, *rossz anyagi helyzetemnek*, *kérdéseimre legyen szíves válaszolni*.
- It fits the family: the addressee, the signature Feri, the formal *Ön* address and the closing formulas (*Isten vele*, *csókolom számtalanszor*, *hű kedvese*) as on hcp-1216.
- Repeated words decode identically: *hogy*, *édesem*, *igazán örülök*, *Jolánkám*, *Isten vele*.

## Response to review 1

Verdict REVISE. All eight findings are accepted and addressed. Checked on the reviewer's crops of the hi-res scan (`review/work/crops/`) and re-run with the reproduction command: 4 of 4 hashes OK, 784 signs, literal rows as above.

1. **major, row 24: fixed.** `crops/z24.png` shows the heavy long stroke with a separate tick on its left, the d form of *boldog* in row 23. `work/ledger.txt` row 24 now has D for H. Literal, `work/normalized.txt`, Hungarian, English and Slovak are corrected to *de sajnos a mi boldog viszontlátásunknak…*. Uncertainty 4 is withdrawn: my claims that *amiből* could not be improved and that *hog* lacks y were wrong.
2. **minor, rows 24-25: fixed.** `[a]` and *elválása* are removed; the text reads *nehéz elválás a vége* with nothing supplied.
3. **minor, green word: fixed.** It is ink, not pencil, and it reads *Szépreményű* (`crops/green.png`). The full clear address is in uncertainty 12.
4. **minor, second postmark: fixed.** Recorded in uncertainty 11, with no date claimed. I also note the large numeral 13 beside it, which the review did not mention.
5. **minor, row 22: fixed.** The `?` became O in the ledger (`crops/z22.png`); the literal is now `öszehö` + `ozehoz`. *összehoz* is unchanged and the call stays an interpretation (uncertainty 2).
6. **minor, row 25: fixed.** Restoration lightened to *a le[ve]lembe[li]*, and v is named as an alternative for the sign before `e m` (uncertainty 5). The ledger keeps L.
7. **minor, Uncertainty 10 and "one unreadable sign": fixed.** *hög* is deleted, and the "Why it is correct" sentence now agrees with S2 and the contextual calls.
8. **minor, row 17: fixed.** The smear under the second t of *belátta* is disclosed in uncertainty 10.

One addition beyond the review: uncertainty 1 now proposes *nem tettem(?)* for row 16. The ledger sign and the literal `mentettem` are unchanged, and the reviewer upheld the signs and left the sense open. This fills that gap with an interpretation that the reviewer has not assessed, so it is marked (?). The other changes are the reviewer's own one-sign corrections and do not alter the rest of the reading, so no second review round was opened.
