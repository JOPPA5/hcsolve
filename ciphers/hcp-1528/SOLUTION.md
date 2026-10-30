# HCP 1528 — pc_hcp_209 — Pepouš to Anna Tichá, 5 December 1903

Status: **complete reading (round 3, after review 2)**, with three small marked gaps. This file
replaces the round-1 text. The round-1 text is archived in `work/v1/SOLUTION-round1.md`.

## Source and context

- Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1528, name `pc_hcp_209`.
  Status "Not solved". No transcription or solution was attached. Language Czech, date
  1903-12-05, private collection, recipient Anna Tichá.
- Picture side (`source/picture.jpg`): an engraved mountain landscape with 18 rows of
  cipher in the writer's hand. Below them is the plain date `5./XII.1903.`.
- Address side (`source/address.jpg`), in plain cursive: Anna Tichá, a teacher staying
  at that time in **Trhové Sviny** (south Bohemia, near České Budějovice), care of the
  teacher Karla Janková.
- The card belongs to the Anna Tichá / Pepouš family of HC Portal postcards, all in one
  key.

## Cipher type and key

The cipher is a simple monoalphabetic substitution (MASC) with invented signs. It has
no word-space masking, and one extra sign stands for the digraph CH. The key is the
Anna Tichá family key, taken over unchanged from the family cards (HCP 1520–1525,
1545). Maxim Egorov / Cipher-Atelier published a generic partial key for this family
earlier. **No new key discovery is claimed.** The labels below are the working labels
used in the transcription.

| Label | `1 2 3 4 5 6 7 8` | `b c d f g h m n` | `p q r s t ř` |
|---|---|---|---|
| Plain | `Y U O I E A J L` | `P S T V K R N M` | `B Z H C D CH` |

`ř` is a neutral label for the capped/hooked CH sign. Accent marks are not part of the
key, so all diacritics in the text below are editorial.

## Reproduction (single command)

From the repository root:

```sh
python3 -I ciphers/hcp-1528/work/decode.py
```

The command checks the SHA-256 of the three source files and of the record files
(`key.json`, `transcription.json`, `positions.csv`, `plaintext.txt`). It decodes all 18
rows from the manual transcription with the key and round-trips each sign through the
inverse key. It then prints the plaintext below and lists the three gaps. Result:
**562 cipher signs → 570 base letters**, 7 of them CH signs. The record was generated
by `work/build-record-v2.py`.

## Literal base plaintext (row breaks as on the card)

`[Q1]` marks a visible sign that is not secured. `[H1]` and `[H2]` mark ink hidden
under the printed foliage.

```text
VRELY DIK ZA DRAHY LISTEK. POSLECHL JSEM SVE SRDECKO A ZUSTAL JSEM
JESTE DOMA. JE MI JIZ O HODNE LEPE, AVSAK DOSUD PLICE A KRK[Q1] NE-
JSOU UPLNE V PORADKU. V PONDELI ZEPTAM SE LEKARE, ZDA MI DOVOLI
JIZ JITI DO URADU. JO MI NYNI NEMOC VERUSE NEVHOD. ABY ME SRDECKO
STONALO KE MNE, BYCH ZA ZADNOU CENU NECHTEL. I BYL BYCH SI VSAK PRAL
KDYZ MNE TAK HLAVA BOLELA, ABY MNE [H1] BYLO ME SRDECKO ASPON
NA CHVILI BYLO, POLOZILO SVOU RUCKU
NA HLAVU, BYLA BY MNE JISTE BOLESTI
PRESTALA. HEZKY SE VE SVINECH BAV[H2]
A VYRID, PROSIM, SLECNA JANKOVA
ME UCTIVE PORUCENI. NEPOSLI
MI VSAK ZE SVIN OPET TAKOVY
LISTEK, JAKO POSLEDNE, KTERY MNE
ZARMOUTIL. SRDECNY POZDRAVA
TISIC DLOUHYCH, VASNIVYCH PUS
POSILA TI TVUJ PEPOUS,
KTERY STALE VRELE
VZPOMINA.
```

## Czech with editorial accents

> Vřelý dík za drahý lístek. Poslechl jsem své srdéčko a zůstal jsem ještě doma. Je mi
> již o hodně lépe, avšak dosud plíce a krk[u] nejsou úplně v pořádku. V pondělí zeptám se
> lékaře, zda mi dovolí již jíti do úřadu. Jo [= Je] mi nyní nemoc věru se nevhod. Aby mé
> srdéčko stonalo ke mně [= kvůli mně], bych za žádnou cenu nechtěl. I byl bych si však
> přál, když mne tak hlava bolela, aby mne bylo mé srdéčko aspoň na chvíli bylo [sic, *bylo* repeated],
> položilo svou ručku na hlavu, byla by mne jistě bolest přestala. Hezky se ve Svinech
> bav[ila?] A vyřiď, prosím, slečna Janková [= slečně Jankové] mé uctivé poroučení.
> Nepošli mi však ze Svin opět takový lístek jako posledně, který mne zarmoutil.
> Srdečný pozdrav a tisíc dlouhých, vášnivých pus posílá ti tvůj Pepouš, který stále
> vřele vzpomíná.

## English translation

> Warm thanks for the dear card. I listened to my sweetheart and stayed at home a little
> longer. I am already much better, but my lungs and throat are still not quite right.
> On Monday I will ask the doctor whether he will let me go back to the office. Illness
> really comes at a bad time for me just now. I would not for any price want my
> sweetheart to fall ill because of me. And yet, when my head ached so, I would have
> wished that my sweetheart had been with me at least for a moment and laid her little
> hand on my head; the pain would surely have stopped. Have a nice time in Sviny! And
> please give Miss Janková my respectful regards. But do not send me from Sviny another
> card like the last one, which made me sad. A heartfelt greeting and a thousand long,
> passionate kisses are sent to you by your Pepouš, who always remembers you warmly.

## Slovak translation

> Vrelá vďaka za drahý lístok. Poslúchol som svoje srdiečko a zostal som ešte doma. Je
> mi už oveľa lepšie, ale pľúca a hrdlo ešte nie sú celkom v poriadku. V pondelok sa
> spýtam lekára, či mi už dovolí ísť do úradu. Choroba mi teraz naozaj prichádza
> nevhod. Za nič na svete by som nechcel, aby moje srdiečko kvôli mne ochorelo. Predsa
> by som si však bol prial, keď ma tak bolela hlava, aby moje srdiečko aspoň na chvíľu
> bolo pri mne a položilo mi rúčku na hlavu; bolesť by iste bola prestala. Pekne sa vo
> Svinoch zabávaj! A vyrieď, prosím, slečne Jankovej moju úctivú poklonu. Ale
> nepošli mi zo Svín znova taký lístok ako naposledy, ktorý ma zarmútil. Srdečný
> pozdrav a tisíc dlhých, vášnivých bozkov ti posiela tvoj Pepouš, ktorý stále vrelo
> spomína.

## What remains uncertain

| Place | Issue |
|---|---|
| Q1, R02 `ghg?` | The last sign is g-like with a trailing hook, not a clear 2/U loop. The reading is KRK or KRKU; the meaning ("throat") is not affected. |
| H1, R06 | A printed foliage blot sits after ABY MNE. Only `p183` (BYLO) is visible after it. It cannot be shown whether the blot hides a sign. |
| H2, R09 | BAV… : the visible ink ends with `p6f`, and the rest is under the tree at the card edge. The ending (bavila / bavíš / bav se …) is a **restoration**. |
| R09 HEZKY | The two middle signs `qg` sit on dark engraving. They are plausible but not certain. |
| R07 POLOZILO, sign 2 | The second sign of `b?839483` is smudged by ink/engraving. It looks like 3/O, and POLOZILO is safe in context, but the sign is read partly from context (probable). |
| R06–R07 *bylo … bylo* | The writer repeats *bylo* ("aby mne [H1] bylo mé srdéčko aspoň na chvíli bylo"). It is kept literal, not repaired. |
| R05 `4` before BYL | The sign is small and partly in foliage. Its shape fits 4/I better than the long-descender 7/J, so it is read as I (probable). |
| R04 JO | Literal JO, as written (expected JE; the sign is 7/J, not d/T). |
| R10 SLECNA JANKOVA | The writer's nominative, where the dative "slečně Jankové" is expected. Kept literal. |
| Diacritics | Not transcribed. All accents in the editorial text are supplied. |

## Why I believe it is correct

- One fixed family key decodes every one of the 562 signs into continuous Czech of
  about 1900. No sign needs a new assignment.
- The content fits the context. The addressee is staying in Trhové Sviny (address
  side), so we get "ve Svinech" and "ze Svin". Slečna Janková is named both in the
  cipher and on the address side. The writer is ill and off work, the card is signed
  Pepouš, and it is dated 5 Dec 1903, all in line with the rest of the family.
- In review 2 the reviewer re-transcribed the whole card independently from fresh crops
  with a hand-typed key (562 signs). After the R07 correction the decoder output is
  identical to the reviewer's `review/work/review2_decode_output.txt`, apart from how the
  three gaps are written (checked with `diff`).

## Credits and history

- The first, partial transcription (492 signs, eight gaps U1–U8) was made on
  2026-10-28 by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol). Its record is
  archived in `work/v1/`.
- The middle passages were completed by Claude Opus 5.5 on 2026-10-29 (DONE1).
- After review 1, Claude Opus 5.5 re-transcribed rows R12–R14 and R16 and rebuilt the
  record and the decoder (round 2).
- After review 2, Claude Opus 5.5 corrected R07 (PRISLO → BYLO), re-checked rows R01–R09
  on the pixels and rebuilt the record (562 signs).
- Family key: earlier family cards, and the published generic partial key of
  M. Egorov / Cipher-Atelier. No published plaintext of pc_hcp_209 was used.

## Response to review 1

Verdict REJECT. All nine findings are accepted and fixed. Each correction was checked
on fresh 3–4x crops in `work/claude/r2/` (r12, r13, r14, r16, r02end, r09, r10_11).

1. **R12 (blocker), fixed.** The crop `work/claude/r2/r12.png` clearly shows
   `n4 fc6g q5 cf4m 3b5d d6g3f1`, which reads MI VSAK ZE SVIN OPET TAKOVY. The round-1
   "SVYM ZLATUCKOVI" was a misreading, and the "zlatoučkovi" interpretation is
   withdrawn.
2. **R13/R14 (blocker), fixed.** In r13.png the row is `84cd5g, 76g3 b3c85tm5, gd5h1 nm5`,
   which reads LISTEK, JAKO POSLEDNE, KTERY MNE. In r14.png the first word is
   `q6hn32d48` (ZARMOUTIL): the last sign is the 8/L loop, not c/S. The grammar-forced
   "kde bys mne zarmoutíš" is withdrawn.
3. **U8 (major), fixed.** The open-topped sign before `5` is q/Z, so the word is ZE
   ("ze Svin"). U6 is q/Z as well (ZARMOUTIL).
4. **Reproduction (major), fixed.** `work/build-record-v2.py` regenerated
   `transcription.json`, `positions.csv`, `plaintext.txt` and the hashes with all
   completions encoded. `decode.py` was rewritten and prints the full final reading.
   I ran it as `python3 -I ciphers/hcp-1528/work/decode.py`; it exits 0 with 564 signs,
   572 letters and 3 gaps. Its 18 lines differ from `review/work/review_decode_output.txt`
   only in gap notation (`[Q1]`/`[H1]`/`[H2]` against `?`/`[..]`).
5. **TVOJ → TVUJ (minor), fixed.** In r16.png the sign in `df27` has the looped z-like
   form of 2/U, the same as in `b5b32c` (PEPOUS) on the same row. The record now has
   `df27` (TVUJ).
6. **Sviny (minor), fixed.** Sviny is Trhové Sviny, near České Budějovice, as named on
   the address side. The wrong "near Veselí nad Lužnicí" is removed.
7. **Restorations (minor), fixed.** BAV… is recorded as gap H2, and the ending is only a
   restoration. The BYLO blot is gap H1. HEZKY and I are listed as probable in the
   uncertainty table.
8. **KRKU (minor), fixed.** The last sign of `ghg?` is now gap Q1 (KRK / KRKU).
9. **Stale text (minor), fixed.** SOLUTION.md was rewritten. It now has one plaintext,
   one Czech text, an English and a Slovak translation, and one uncertainty table. The
   PARTIAL preamble and the U1–U8 texts were removed (archived in `work/v1/`).
   One more correction came from re-reading R10: PROSIM ends in `n` (M). The round-1
   prose had given it as `m` (N).

The reading was substantially changed (rows R12–R14), so the solution goes back for a
second review (DONE2).

## Response to review 2

Verdict REVISE. All three findings are accepted and fixed. The decoder was re-run as
`python3 -I ciphers/hcp-1528/work/decode.py`: it exits 0, all hashes pass, and it prints
**562 signs → 570 letters**, gaps Q1/H1/H2. With the gap markers removed, its 18 rows are
identical to `review/work/review2_decode_output.txt` (checked with `diff`).

1. **R07 word 3 (major), fixed.** On the reviewer's crops `review/work/r2/k_r07a.png`,
   `n_r07b.png` and `c_r07_09.png`, the word after `řf484` has four signs: the long-stemmed
   p/B, then 1, 8 and 3. This is the same shape as `p183` (BYLO) after the H1 blot in R06
   (`l_r06tree.png`). There is no room for the six-sign `bh4c83`. The k-like hook on the
   first sign could suggest the family's k-shaped G sign, but GYLO is not Czech, and the
   sign is identical to the B of R06 BYLO, so it is B. The GPT record (`work/v1/`) had
   carried PRISLO since round 1. `work/build-record-v2.py` now has
   `m6 řf484 p183, b383q483 cf32 h2sg2`. `transcription.json`, `positions.csv`,
   `plaintext.txt` and `record-sha256.json` were regenerated (R07: 30 → 28 units). The
   literal text now repeats *bylo* ("aby mne [H1] bylo mé srdéčko aspoň na chvíli bylo,
   položilo svou ručku na hlavu"). It is kept as written, not repaired. The English and
   Slovak translations now say "been with me" / "bolo pri mne", not "come". H1 stays a gap.
   The claim that the base text equals the round-1 reviewer's was replaced by the actual
   `diff` comparison with the review-2 output.
2. **R07 POLOZILO sign 2 (minor), fixed.** Added to the uncertainty table as probable
   (a smudged sign that looks like 3/O, read partly from context).
3. **Provenance (minor), fixed.** Round 2 re-read on the pixels only R02 (end), R09,
   R10–R11, R12–R14 and R16. Rows R01, R03–R08, R15, R17 and R18 were taken over from the
   earlier records (the GPT round-1 record and the reviewer's round-1 transcription) without
   a fresh check. That is how the R07 error survived. In this round I re-checked R01–R09
   sign by sign on the reviewer's 3–6x crops `a_r01_03.png`, `b_r04_06.png` and
   `c_r07_09.png`. Apart from R07 they agree with the record. R15, R17 and R18 were checked
   by the reviewer in review 2, and I did not re-read them myself.

The reading changed by one word in one row, and the substance of the letter is
unchanged, so the solution is finalised.

