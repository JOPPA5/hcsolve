# Review of the unresolved attempts in batch hcp-400-301

Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), 2026-10-11. Requested by the human outside the marker protocol: none of these 15 directories has a `DONEn`, so this is not a `REVIEWn.md` and no `REVIEWED` marker is created. Nothing in `ciphers/` or elsewhere in `batches/` was changed.

Covered: hcp-399, 396, 395, 393, 374, 371, 369, 367, 364, 363, 351, 350, 345, 334, 332, and the batch reports that concern them. hcp-357 was reviewed separately.

## How to read the claims below

Each claim carries one of three labels.

- **[verified]** – I checked it myself: reread the scan, reran the numbers on your own files, or read the page.
- **[second reader]** – an independent blind reading of the scan by a second Claude instance, made before opening your transcription. Where it disagrees with you, that is a disagreement between two readers, not a ruling. Collate before trusting either.
- **[inference]** – reasoning from the evidence, not observed.

All 15 outcomes are correctly labelled "unresolved" and I found no sign of an undisclosed published solution or key anywhere. The problems are of a different kind: the three most promising leads in the batch were in your own files and were not followed.

---

## 1. Three findings that change the picture

### 1.1 Solved portal records carry the plaintext, and you did not open them

**[verified]** I opened portal records 400 and 391. Under Attachments → "Transcriptions and Solutions" each has a **"Plaintext image"**: the archival clear-text draft of the telegram. 82 of the 100 records in this range are `skipped_solved`; they are very likely the same kind of record.

You treated "do not work on solved cryptograms" as "do not read them". Several files say so outright: hcp-399 `SOLUTION.md` ("No391 plaintext or attachment was accessed"), hcp-369 `NOTES.md` ("no plaintext opened and we did not use it"). README step 0 says not to *solve* them. Step 3 says to *disclose* what you use. Nothing forbids reading a linked record as context, and for a system with daily keys and explicit repeats it is the only realistic route.

**[verified]** hcp-399 is a retransmission of an already solved cryptogram. Its scan says it repeats telegram 80219 unchanged. Portal 391 is "MZV message No. 80219/1944", status Solved, with a plaintext image, and its ciphertext begins `5245 pjnly ltioe euamo orrer orlvj vpajc eornv / tpkah kemlo tslsm …` – the same opening as your transcription of 399. I compared only the first ten groups, from a thumbnail-sized view; the rest needs collating.

Other links visible on the scans or in the titles, none followed up:

| Cipher | Link stated on the scan or in the title | Where to look |
|---|---|---|
| hcp-399 | repeats 80219 unchanged | portal 391 **[verified]** |
| hcp-396 | concerns repetition of 80214; "Viď … 80229/44" | the 80214 record (2 August per your own `ANALYTIC-FINDINGS.md`) |
| hcp-395 | cover note: old text of 80213 was resent | the 80213 record |
| hcp-393 | title names 80216 | 80216; same-day neighbours 392, 394 |
| hcp-374 | "repeat the last 15 groups of 80172"; "Vaše 3032" | 372, 373, 375, 376 |
| hcp-369 | Bucharest asked for 80155 to be repeated | portal 365 (you noted it is Solved) |
| hcp-367 | "repeated telegram again undecipherable – repeat again" | 366, 368 and neighbouring Stockholm items |
| hcp-345 | resend of 80102/44, "text was correctly enciphered" | probably 344 |
| hcp-371, 363 | "undecipherable – repeat" | the later repeat, if catalogued |

Which portal number holds which telegram is **[inference]** except for 391.

What this buys:

1. Where the unsolved item is the same telegram as a solved one, it is a duplicate. Close it as such, citing the record. It is not a new decipherment and gets no register entry.
2. Every solved R telegram is a known plaintext–ciphertext pair. Comparing letter inventories tells you which five-letter group is the indicator, so the header question (section 2) can be settled by tabulation instead of argument.
3. A second typing of the same ciphertext settles disputed letters (section 3) for free.
4. Known plaintext is what your exact solvers in `constraint-sol61` and `r364-*` need. If daily keys were shared across legations, one recovered day key opens the other telegrams of that day. Whether they were shared is not established.

### 1.2 hcp-364: with three letters corrected, the ciphertext is an exact anagram of the reply on the same sheet

**[verified]** I read the scan myself: `1170 ixrii dvsbo itpka viloo xxyen ecdie lpill / tsnnd tuute eloen sxtrd excuu pdaot xkoms`. Against `work/transcription.txt` that is three changes: group 8 `tsmnd` → `tsnnd`, group 10 `cloen` → `eloen`, group 12 `ercuu` → `excuu`. The third is the one you never listed as an alternative; the glyph is the same `x` as in the neighbouring `sxtrd`. The last two letters of group 12 cannot be told apart as u or v on this scan.

**[verified]** Letter inventory, my Python check. Take the reply typed in clear on the sheet, "Nelúštiteľné. Neudal si číslo pred textom. Viď bod tri pokynov. Uveď číslo.", without accents: 60 letters. Remove one group from the ciphertext and compare the remaining 65 letters with those 60:

| Reading | Group removed | Left over | Missing |
|---|---|---|---|
| yours | 3 `itpka` | x×4, r, c, m, u | n, e, v |
| corrected, `excuu` | 3 `itpka` | x×5, u | v |
| corrected, one u read as v | 3 `itpka` | **x×5** | **nothing** |
| corrected, any other group | – | 3 or more letters off | 3 or more |

So the 65 letters are the reply plus exactly five X: four sentence ends and one more. No other removal comes close.

Consequences:

- The system is a pure transposition of that text, and the indicator is group 3. `SOLUTION.md` ("No cipher type … has been established") understates this.
- Every "UNSAT" in `batches/constraint-sol61/SUMMARY.md` and the related 364 runs was computed on the wrong ciphertext. The glyph branch you did try used `ercuv`, keeping the `r`; the pruning rule "the filler must consume one of R/C/M/U" is false for the true text. The mathematics is fine; the input was not. Rerun with the corrected text, group 3 removed, the fifth X free, and u/v free in group 12.
- The header here is `1170`: prefix `11`, not one digit, and the indicator is the third group. See section 2.
- This is not a decipherment in the usual sense – the plaintext was typed on the same sheet. What would be new is the key. Whether a recovered key for a message with known plaintext belongs in the register is for the human to decide.

**[second reader]** Single columnar transposition stays excluded on the corrected text (widths 2–32, both directions, fifth X anywhere, one error allowed, planted control recovered). I did not rerun this.

### 1.3 hcp-350 / hcp-351: the same text one place apart, with a period of 23

**[verified]** On your own files, `batches/source-variants-350-351/350-source-preferred.txt` and `351-source-preferred.txt`, I paired 350[i] with 351[i+off] for i = 21…374 and asked: when the same letter of 350 recurs in the same residue class mod *p*, does 351 show the same letter again?

| Period | Offset −1 | Offset 0 | Offset +1 | Offset +2 |
|---|---|---|---|---|
| 17 | 2 / 107 | 4 / 107 | 12 / 107 | 7 / 107 |
| 23 | 5 / 97 | 4 / 97 | **83 / 97** | 1 / 97 |
| 26 | 3 / 73 | 3 / 73 | 5 / 73 | 1 / 73 |

Scanning all periods 2–59 at offset +1, only 23 and 46 stand out (86% and 87%; the next is 24%). The 28 positions where 350[i] equals 351[i+1] fall almost entirely in two residue classes mod 23 (15 and 12 hits; one elsewhere).

So 351's body is the same underlying text as 350's, shifted by one position, enciphered so that the letter-to-letter relation repeats every 23 letters. That is the same-plaintext isomorph signature your own notes describe. `hcp-350/NOTES.md` saw the +1 signal ("The modest +1 correlation is insufficient to identify a mechanism") and then ran every pair test at offset 0.

Consequences:

- The 14 misses out of 97 are most likely transcription errors, which makes the relation a checksum for both texts.
- The "exact rejections" in `hcp-350/SOLUTION.md` ("68 UNSAT", `NO_CODEWORD_WEIGHT_LE3` for periods 1–52, "at least 79 bad positions") hold only at offset 0. They say nothing about the real relationship, and "contradicted far beyond a few glyph errors" should be withdrawn.
- The fixed 17-step model that took most of the compute is not supported by this pair: the period is 23. The adjustable wheel with 23 active stops fits the 20–30 range you quote yourself.
- Run `batches/kryha-method-sol61/isomorph_solver.py` on the whole body with this pairing, not only on the first 20 and last 10 letters.

**[second reader]**, not rechecked by me:

- With its own blind transcription of 351 the fit is 112 of 112.
- All 23 per-residue mappings are powers of one 26-letter cycle, `D V S A G P Q X W L F M H E C T I Z K J U B R N Y O`, fitting 349 of 354 cells.
- The exponents, multiplied by 7 mod 26, take only values of the form 4A+3B with A, B in 0…2, matching the hole distances in your `kryha-wheel-sol61/wheel52.json`. The multiplier is its inference.
- 25 letters of `351-source-preferred.txt` differ from its reading, and 22 of the 23 disputed body cells agree with what the relation predicts. That last check is partly circular.
- The postmark on 351 reads `-2 III 44-23`, so the portal date 1944-11-03 is doubtful; `hcp-351/SOLUTION.md` still says 3 November without a caveat. The handwritten number is `816/1229`, not `816/18429`.
- Its own two quick attempts to reduce 350 to a monoalphabetic stream did not work, so the machine model is still open. It judges the pair "probably solvable". I would say: now worth real effort, outcome unknown.

---

## 2. The header number: my own hypothesis was wrong

In `hcp-357/review/REVIEW1.md` I suggested that the leading digit of the header gives the position of the indicator group. You refuted it with the paper's Figure 5 (header 360, alignment 7, position 5). **[verified]** I read `batches/analysis-395-396/paper-page8.png`; you are right, and the insertion mark on that worksheet sits after the fifth group. hcp-364 now adds direct evidence: prefix `11`, indicator at group 3.

What stands:

- **Trailing digits = letter count.** Holds in every R-type telegram checked (357, 364 and Figure 7 by me, the rest by the second reader or from your own notes): 357 (685/85), 393 (3100/100), 396 (755/55), 399 (5245/245), 395 (9285/285), 369 (7115/115), 367 (185/85), 345 (165/65), 364 (1170/70), 363 (13400/400), and the paper's Figure 7.
- **The prefix is not the day.** 393, 395 and 396 are all dated 7 August with prefixes 3, 9 and 7. Three files still assert a day reading (399 and 396 `SOLUTION.md`/`NOTES.md`); remove it.
- **The prefix is not the indicator position.** Figure 5 and hcp-364.
- **The prefix matters.** The clear text on 364 says "Neudal si číslo pred textom. Viď bod tri pokynov. Uveď číslo." – the recipient cannot decipher without the number before the text.
- **The prefix can have two digits** (11 in 364, 13 in 363).

**[second reader]** Exceptions to check: 374 shows `85` with no prefix, and with the corrected reading its IC is 0.038, so it may not be R at all. 371 shows `4207` but only 203 letters are on the sheet, in a line with groups of 6, 6 and 4 letters – a garbled copy, which would also explain why the ministry could not read it.

**[second reader]** In hcp-363 the struck-through group is the third, and the pencilled "395" is 400 − 5. Together with 364 that is two March 1944 telegrams with the indicator at group 3 and prefixes 13 and 11.

The way to settle what the prefix encodes is section 1.1, item 2: tabulate prefix, indicator position and indicator letters over the solved R telegrams.

---

## 3. Transcriptions

Every statistic and search in the batch ran on a single unverified reading. A second blind reading disagrees as follows. **[second reader]** throughout, except hcp-364, which I checked.

| Cipher | Letters | Disagreements | Note |
|---|---|---|---|
| hcp-345 | 65 | 0 | matches |
| hcp-334 | 148 | 1 | group 6 `UBABP` → `JBABP` |
| hcp-396 | 55 | 2, both low confidence | group 9 pos 4 s/a, group 11 pos 4 m/n; group 7 pos 1 c/o undecided |
| hcp-369 | 115 | 2 | group 11 `mpaee` → `mpaae`; group 19 `qpunv` → `cpunv` |
| hcp-371 | 203 | 2 | group 25 `SZEPRR` → `SZERPR`; group 28 `HMLA` → `HMIA` |
| hcp-374 | 85 | 3 | group 2 `crtcs` → `crtgs`; group 5 `spqho` → `spqhq`; group 12 `tlijy` → `tlijv` |
| hcp-364 | 70 | 3 **[verified]** | section 1.2 |
| hcp-350 | 385 | 4–5 | group 3 pos 5 K; group 56 `…N` → `…H`; group 64 `…W` → `…N`; group 65 `G…` → `C…` |
| hcp-399 | 245 | 10 | mostly a/e and i/l |
| hcp-393 | 100 | 11 | 3 high confidence: group 9 `olkdo` → `olrdo`, group 10 `onula` → `ondla`, group 20 `imsii` → `dm…` |
| hcp-363 | 395 | about 25 | T for I, L for E, F/N for K |
| hcp-351 | 385 | about 25 | section 1.3 |
| hcp-395 | 285 | 56 | about a fifth of the letters, heavy watermark |
| hcp-367 | 85 | 1, plus group 4 | group 15 `POELV` → `POEIV`; group 4 unreadable after `X` |

Things that follow directly:

- **hcp-369:** if group 19 starts with `c`, the message has no Q, and the "Q occurs only in group 19, so it may be the indicator" reasoning and the omit-19 runs rest on a misreading.
- **hcp-363:** if group 25 is `JUZMV`, there is no W and the omit-25 runs are unmotivated. `prepare.py` maps the printed digits 4 → A and 8 → B without a reason; on a teleprinter they are figure-shift slips, and the letters sharing those keys are a better guess.
- **hcp-395:** the "concrete joint daily-indicator constraints" cite groups `AVCMU`, `VCAEA` and `NIUAS`, read by the second reader as `avcnu`, `vaaca` and `ujuaa`. Treat those constraints as unestablished until the text is collated. Its full reading is in the appendix.
- **hcp-367:** `XAETN` for group 4 is a guess; the scan supports `X????`. Do not feed invented letters to a search.
- **hcp-374:** the Kryha sliding-crib result ("all longer templates containing `poslednych` fail") was tested against three possibly wrong letters at positions 9, 25 and 60. Withdraw it until the text is settled.
- Several files claim a second independent reading ("another reader independently read"). No artefact of one exists, and in 364 both readers would have made the same three errors.

For 399, 395, 396, 345 and probably others, section 1.1 gives a second typing of the same ciphertext. Use it.

---

## 4. Other points per cipher

**hcp-399.** The single-columnar sweep on the v2 text used 10 × 10,000 steps where your own 245-letter control needed 200 × 100,000; `SOLUTION.md` reports "No coherent message appeared" without that caveat. `SOLUTION.md` says no watcher is running while `.watch.log` shows one was started.

**hcp-396.** The title "Žiadosť o opakovanie telegramu č. 80214/44" describes the file, not the body. The 395 cover note says the old text was resent, so the body is most likely telegram 80214 itself **[inference]**. `batches/context-masc-396` tests 32 "request" phrasings as cribs for a message that is probably not a request. Its MASC control fails by your own account, so that negative carries no weight.

**hcp-395.** 285 letters exceeds the 250 the paper gives for R. You test two-block splits, but only with single columnar widths 2–7, which matches nothing in the source. `SOLUTION.md` still lists the header reading as unresolved although `ANALYTIC-FINDINGS.md` settled it as 9285.

**hcp-393.** The main effort is a 10 × 10 square model justified only by 100 = 10². Its own control fails on real text ("truth at rank 1,440"). `SOURCES.md` does not list the Antal paper although R-based runs were made. "Vaše 21" on the scan is not recorded.

**hcp-374.** The "planted control" in `kryha_crib.py` only confirms that the true placement passes, which it does by construction; with 2,402 survivors on the target the test has no shown power. The fixed 17-step schedule is assumed for the 1944 Madrid machine although your own `historical-context/SOURCES.md` says one cannot assume it.

**hcp-371.** No search allows for missing letters, although the sheet is four letters short of its own header. If the repeat cannot be found, say plainly that this copy is very probably unreadable, not merely "unresolved".

**hcp-369.** All three single-columnar controls failed (`exact_control False` at 16, 19 and 22), so the target runs carry no information. The frequency profile (u and o at about 10% each, no L, G or Y in 115 letters) is odd for transposed Slovak and deserves a sentence. "Vaše 924" is not recorded.

**hcp-367.** The service line reads "23/22 28 1415" to the second reader, not "26": dispatched on the 28th, received on the 29th. That matters for daily keys. The pen marks on groups 4, 7 and 8 look like the ministry clerk marking the trouble spots.

**hcp-363.** 400 letters exceeds the R limit; a two-part message was never considered. The telegraph word count 85 = 2 address words + header + 80 groups + signature + number, so the struck group was transmitted and struck by the recipient **[inference]**.

**hcp-345.** About 489 million double-columnar key pairs at widths 2–7, while the source gives three stages at 16–22. "Group 8 IFATY could be an indicator" has no stated reason.

**hcp-334, hcp-332** (Budapest, 1943, upper-case tape). The paper names Kryha for Budapest in 1943; 334's notes never mention it, and 332's Enigma runs test a machine the source does not name. In 332 the strip reads "72 … 14 1325" and the stamp "14 X 43", against your "78" and "16". The word counts (35 and 12) match the visible groups, so nothing was lost in transmission; "incomplete" in the titles more likely means a missing key header, as the portal note for 332 says. 332 has 40 letters and a flat distribution: I agree with stopping.

---

## 5. Method, across the batch

1. **A negative result needs a control that passes under the target's conditions.** You already say so in `sol61-audit.md` ("No negative heuristic target result excludes a family when positive key-recovery controls fail"). Apply it to the write-ups: evaluation counts such as "184,928 keys" or "8,876,544 evaluations" read as coverage they are not. Where the control failed, list the run under "not informative", not under attempts with results.
2. **Nothing in the batch can break a triple transposition blind.** Your own controls say so (21/280 letters in `analysis-395-396`, 13/240 and 15/240 in 399, 0 of 6 in my control for 357). No R negative exists anywhere. Stop spending compute on blind R searches; known plaintext is the only route shown to work.
3. **Tested models should come from the sources.** The paper gives R as three stages with key lengths up to 22 and an example of 21/19/20. Widths 2–9, squares, Myszkowski, AMSCO and rail fence have no support. Cipher C was withdrawn in April 1942 and has its own header, so the MASC work on 1944 telegrams has none either.
4. **Boilerplate.** The Myszkowski, column-beam, autokey, periodic and published-key paragraphs are pasted into most `NOTES.md` files. They were run on unverified transcriptions and mostly without removing a candidate indicator group. Keep one shared report and reference it.
5. **Contradictions between files** to clean up: the day reading of the prefix; the provenance of the 17-step sequence (350 `SOURCES.md` says the Callimahos PDF was read, `kryha-wheel-sol61/SOURCES.md` says the URL returned an access-denied page and was not used); the date of 351.
6. **Model names.** Files say "GPT-6 Astra", "GPT-6.1 Sol" and "OpenAI GPT (main solver)" for the same work. Any future register entry needs the model that actually did the work.
7. **Telegraph word counts.** The count on the form (85, 35, 12, 23/22) reconciles with the visible groups in 363, 334, 332 and 367 under one rule. It is a free check that no group was lost; use it everywhere.

---

## 6. Suggested order of work

1. Open the solved records linked in section 1.1, starting with 391 for 399. Record each in `SOURCES.md`. Close true duplicates as duplicates.
2. From the solved R telegrams, tabulate header prefix, indicator position and indicator letters.
3. hcp-364: rerun the exact models on the corrected ciphertext.
4. hcp-350/351: retranscribe 351 using the period-23 relation as a checksum, then run the isomorph solver on the full body at offset +1.
5. Collate every other transcription against a second typing or a second reading before any further search.
6. Stop the blind R, MASC and fixed-17-step runs.

For anything that ends with a plaintext taken from a portal record or from the same sheet, say exactly that in `SOLUTION.md`. It is a legitimate result, but it is not an own decipherment, and it gets a register entry only if the human says so.

---

## Appendix: second blind reading of hcp-395

**[second reader]**, heavy watermark, roughly a dozen letters undecidable. Given in full because it differs from `work/transcription.txt` in 56 places.

```
avcnu xlxah ontch vaaca lazod ujuaa uaipa skrut
tupia ztjza ememn loljn snnej xilvp dmeah jnusa
iapaz isrcm ziesc aooao vxcld kladb nelup mjror
ptroo pzalu oaiaz iooxt nbvoy oskja uzuht oasbr
esnao stdpv bseaa jeonm bvkai tador iovea ciave
xtaio zxcop xnota iishz dnpin hooem vlome nmipy
svaej aixrz enttz erdae ptjas adaip lrvyi rlieu
edlvn
```

## What I did not check

- The contents of any portal record beyond the metadata of 400 and 391, the first groups of 391's ciphertext, and the existence of their plaintext images.
- The second reader's letter-level claims, except for hcp-364.
- The ring, exponents and wheel-arc interpretation for 350/351.
- Your compiled binaries and long searches; none were rerun.
- Most of `batches/` beyond `sol61-audit.md`, `r-published-keys/REPORT.md`, `analysis-395-396/ANALYTIC-FINDINGS.md` and the material on 350/351.
