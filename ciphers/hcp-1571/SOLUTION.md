# HCP1571 / pc252 — source-wide solver candidate

Manual known-key transfer gives a connected Czech letter across **13 physical rows: upper9 and lower4**, with **475 active cipher units, 7 marked CH units and 482 base letters (after review 1)**. All22 supplied key labels occur. Three localized class readings remain bounded QA points (R03 MNE/MME, R10 ANTILKEM/ANDILKEM, R11 ROZEZVUCELA/ROZEZVECELA). The literal block is the selected candidate, not an accepted or wholly unambiguous transcription. No opaque span was assigned a guessed reading or length.

## Source and prior work

Root inspected all three rendered tabs and both full-image modals at https://crypto.hcportal.eu/dashboard/cryptograms/1571 on2026-10-28. Portal: Not solved, Czech,1902-12-20, private collection, recipient Anna Tichá, unknown sender; no individual target transcription or solution attachment. Immutable source provenance is in `SOURCES.md` and `source/metadata.md`. Originals are byte-identical to the earlier triage copies; their three fixed hashes agree with this target's entries in the immutable nine-entry `batches/easy-2026-10-28/cz246-251-252-source-sha256.json`.

Both complete originals/all margins were inspected. Clockwise90° rotation makes the picture writing upright (674×1024). Its upper block contains nine rows, with R05 beginning beside the printed **Veselé vánoce!**; the lower block contains four rows. The intervening **20/XII.1902** is an ordinary handwritten date, separately read and consistent with the portal date. The illustration and watermark contain no observed extra handwritten cipher. Address side: ordinary *Velectěná Slečna / slečna Anna Tichá / učitelka v Žirovnici / u Počátek*, printed multilingual postal headings, stamp and cancellations. No cipher continuation was observed there; exact postmark dates were not needed or asserted.

The fixed family key `ciphers/hcp-1520/work/key.json` was supplied before this reading. Maxim Egorov / Cipher-Atelier's public partial study https://maxim-egorov.dev/research/anna-ticha-postcards/ and archived `batches/easy-2026-10-28/published-anna-ticha-key.txt`, plus the photographed pc199 reference/provenance, were already known. Expanded public work on other cards is credited, including publicly registered1520–1524/1542; those six explicit exclusions remain outside new-discovery/repeat-submission counts. This is manual target reading with a transferred key, not independent key recovery, OCR, blind review or global priority. No target-specific plaintext seed, transcript or phrase search was used.

Root's fresh rendered register observation covers337 contributions/303 unique HCIDs; this target is absent from the full bounded source-ID set. Evidence is the root register snapshot and `triage-pc246-252/selection.json` cited in SOURCES. Register absence is not worldwide novelty proof. The closing PEPOUS does not establish a civil sender identity.

## Fixed key and source-linked record

The neutral glyph labels are the supplied22-label key, with plaintext capitalized. `H` denotes one marked r-like CH unit; `y` denotes J. They are shape labels, not plaintext accents or assumptions about the intended handwritten alphabet.

| Label | 1 | 2 | 3 | 4 | 5 | 6 | 8 | q | g | f | h |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Plain | Y | U | O | I | E | A | L | Z | K | V | R |

| Label | t | r | c | s | n | m | p | b | d | y | H |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Plain | D | H | S | C | M | N | B | P | T | J | CH |

`work/transcription.json` holds exact cipher strings, literal rows, boxes and physical inventory; `work/positions.csv` indexes every active unit globally and within its row. Counts by row are41,37,36,38,26,40,42,38,41,36,38,36,26. Boxes use the clockwise working rotation and may include neighboring slanted strokes; no individual glyph pixel segmentation is invented. `indexed-rows.png` and `rows-A/B/C-indexed.png` expose all13 rows; the24 same-card controls in `source-controls.json` include native and nearest-neighbor crops with source boxes. Marked CH occurs in ABYCH, VLASTNICH, SVYCH, MYCH, DLOUHYCH, VRELYCH and VASNIVYCH; R02 BYH has a plain, unmarked r (writer omission), read editorially as *bych*.

## Literal Czech base letters — selected candidate

No Czech diacritic layer is claimed. Capitalization is uniform; spacing and punctuation are manual layout transcription. TESIC, ANTILKEM and JSI TI remain unnormalized. R11 now reads ROZEZVUCELA after focused source comparison. The ordinary greeting/date/address are outside this block and count.

```text
TISICKRAT DIK. ANICKO MOJE PREDRAHA, ZA ROZTOMILY
LISTEK. MEL BYH VSAK JA SAM PRIJETI S METLOU NA
ANDELKU, KTERA SICE MNE PILNE NAPOMINA, ABYCH
SE SETRIL. AVSAK SAMA VLASTNICH SVYCH RAD NEDBA A
DLE MYCH SE NERIDI. TESIC SE MNOHO
NA SVATKY? JA TRAVITI JE BUDU JAK OBYCEJNE V PRAZE.
MAME OPET V URADE HODNY SHON A BUDU RAD, AZ SE VSE OPET
UKLIDNI. NA TEBE, DUSICKO MOJE VZPOMINAM DENNE
RANO, VECER I CELY DEN. KDY MI POSLES SLIBENE PSANKO?
TAKOVYMTO ANTILKEM, DEVENKO MOJE PREDRAHA,
JSI TI A LASKA TVOJE ROZEZVUCELA MI SKVOSTNOU
HUDBU V DUSI!! - TISIC DLOUHYCH, VRELYCH, VASNIVYCH
PUS POSILA TI VECNE TVUJ PEPOUS.
```

## Editorial Czech reading

Diacritics, joined rows and sentence punctuation below are editorial. Explicit repairs are TESIC→*těšíš* (C→S), ANTILKEM→*andílkem* (T→D; source class alternative also retained), and TI→*ty* (I→Y). Selected ROZEZVUCELA becomes *rozezvučela* by adding diacritics only; no U→E repair is made. The prior ROZEKVUTELA and *rozekvětela?* draft are explicitly rejected after source comparisons changed word units5 and8, not improved by grammar. PSANKO is retained as *psánko*. No such repair changes the literal key record.

> Tisíckrát dík, Aničko moje předrahá, za roztomilý lístek. Měl bych však já sám přijeti s metlou na Andělku, která sice mne pilně napomíná, abych se šetřil. Avšak sama vlastních svých rad nedbá a dle mých se neřídí. Těšíš se mnoho na svátky? Já tráviti je budu jak obyčejně v Praze. Máme opět v úřadě hodný shon a budu rád, až se vše opět uklidní. Na tebe, dušičko moje, vzpomínám denně ráno, večer i celý den. Kdy mi pošleš slíbené psánko? Takovýmto andílkem, děvenko moje předrahá, jsi ty a láska tvoje rozezvučela mi skvostnou hudbu v duši!! Tisíc dlouhých, vřelých, vášnivých pus posílá ti věčně tvůj Pepouš.

## Slovak translation of the editorial reading

> Tisíckrát ďakujem, moja predrahá Anička, za milý lístok. Mal by som však ja sám prísť s metlou na Andělku, ktorá ma síce usilovne napomína, aby som sa šetril. Sama však na vlastné rady nedbá a mojimi sa neriadi. Veľmi sa tešíš na sviatky? Ja ich strávim ako obyčajne v Prahe. V úrade máme opäť poriadny zhon a budem rád, keď sa všetko zasa upokojí. Na teba, moja dušička, myslím denne ráno, večer aj celý deň. Kedy mi pošleš sľúbený lístok? Takýmto anjelikom, moja predrahá dievčina, si ty a tvoja láska mi rozozvučala nádhernú hudbu v duši!! Tisíc dlhých, vrúcnych, vášnivých bozkov ti posiela naveky tvoj Pepouš.

This translation follows the selected source branch ROZEZVUCELA; its remaining unit7 class alternative is disclosed below. Andělka is the name/addressed pet form as read here; no historical identity is inferred.

## Source controls and uncertainties

- **g/q:** C01 shows the closed/different head and descender forms in JAK and PRAZE; the fixed K/Z assignments were not selected by vocabulary alone.
- **t/d:** C02/C03 compare R10's d-like third sign in `6md48g5n` with T in TAKOVYMTO and D in ANDELKU. Selected ANTILKEM is retained; ANDILKEM remains the bounded t/D alternative retained after root photographic QA.
- **b/p:** C04/C05/C16 compare low/descending p/B in BYCH with tall b/P in PILNE and both OPET words. An early draft's OBET and UPADE were corrected after source comparison; selected URADE has h/R.
- **m/n:** C06/C07/C09 compare hump counts in MNE, PILNE, MAME, VZPOMINAM and DENNE. R03 `nm5`→MNE (row17–19/global95–97) is selected; `nn5`→MME remains a localized alternative at the second label, without adding a missing sign.
- **c/s:** C08 shows TESIC `d5c4s` (row15–19/global167–171), whose last angular s/C differs from round c/S in the following SE. DUSICKO and the closing VECNE are also preserved in their source contexts. The source's TESIC is not silently changed to TESIS.
- **4/1 and underline:** C10/C14 compare I/Y forms. Underlined R11 `d4` is retained as TI (row4–5/global379–380), interpreted editorially as TY; underline alone is not cancellation. No baseline unit is deleted.
- **CH:** C11/C12/C17 show the marked r-like units, counted once and expanded to two base letters. Their marks are not counted as Czech diacritics.
- **R11 focused correction:** C13/C18–C21 contain `h3q5qf2s586` (row17–27/global392–402). Word unit5/global396 now uses q/Z, matching the word-internal unit3 q reference and differing from the same-row g/K in SKVOSTNOU. Unit8/global399 now uses the short angular s/C seen in TESIC, rather than the tall/top-barred rounded d/T. These replace the earlier g/K and d/T; ROZEKVUTELA and its rozekvětela draft are rejected. Existing unit7/global398 remains selected2/U, giving ROZEZVUCELA; the bounded5/E alternative gives ROZEZVECELA. Source comparison supports the corrections, not merely a recognizable Czech verb. Root inspected qa-gq/qa-sd panels and agreed with selected q/Z and s/C. qa-td (C22–C24) leaves R10 d/T selected with crossed t/D alternative; R03 MNE remains bounded. The inverse validates the selected branch, not any visual class choice.
- **Closing:** C15 records `f5sm5 df2y b5b32c`→VECNE TVUJ PEPOUS. The tiny2 is kept; the three/four-unit distinction was checked against pixels, not a familiar formula.

No opaque run is currently asserted; locally dark/filled loops are not used to invent earlier writing or an exact canceled count. Bounded class alternatives keep the same visible units/count. Candidate full-coverage counts do not turn these readings into accepted glyph truth.

## One read-only reproduction command

Run from the repository root:

```bash
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1571/work/decode.py
```

It verifies three original hashes against this target's fixed entries of the unchanged nine-entry batch, reference/record/canonical hashes, supplied-key equality, all13 rows/475 positions, counts, saved literals and exact SOLUTION literal equality. It scans and inversely encodes the **entire literal plaintext** with the complete fixed key, greedy CH as one unit, comparing whole cipher strings; this is not a per-token inverse tautology. It checks the clockwise original rotation,13 row crops and24 native/NN controls pixel-for-pixel and verifies indexed uncertainty ranges. It writes nothing. PIL is available in the documented runtime. The other authoring scripts are mutators and were inspected before use.

Hashes, inverse equality and crop consistency establish provenance/internal consistency, not the truth of manual glyph classification. Root collaboration/QA is a solver check, not independent provider review. No watcher/reviewer, marker, final acceptance, PDF, external submission or register entry was created by this collaborator.

## Root source QA and candidate handover

Root inspected both original sides/all margins, all13 physical row crops, all24 native/NEAREST class controls and the three extra q/g,s/d,t/d comparison panels. The bounded follow-up caught two wrong class labels in R11 before handover: global396 g/K→q/Z and399 d/T→s/C. Internal same-word q, same-row K and angular C references support the corrected ROZEZVUCELA; the earlier ROZEKVUTELA/rozekvětela branch is rejected. No key value or unit count was changed.

MNE/MME at the second label of globals95–97, ANTILKEM/ANDILKEM at global351 and2/U versus5/E at global398 remain explicit bounded alternatives. Selected TI and TESIC are kept literally, with intended TY/TESIS editorial only. All eight CH units and the VECNE TVUJ PEPOUS closing are represented. There is no opaque missing-length run in the proposed13-row segmentation; that is not a claim that every class is visually certain.

The final documented read-only command passes all source/reference/record/canonical hashes, positions/counts, SOLUTION equality, original crop pixels and actual whole-plaintext fixed-key inverse. Full before/after directory hashes confirm no execution writes. Root/helper checks are solver collaboration, not independent-provider review. DONE1 hands over this qualified candidate; no PDF, register entry, acceptance or FINAL is claimed. No watcher/reviewer was launched under the human override.

## Response to review 1

Written by Claude Opus 5.5 (solver role, 2026-10-29). All corrections were made in `work/build-record.py` (row strings) and the record was rebuilt with it; `work/rev1/transcription-before-review1.json` keeps the pre-review record, and `work/rev1/R08-tobe-6x.png`, `R08-tobe-10x.png`, `R08-mid-5x.png` are my new source crops. `work/decode.py` now asserts the corrected rows and counts (7 marked CH, 482 base letters), `work/refresh-hashes.py` resealed the record/canonical hashes, and the reproduction command passes again.

1. **[major] R09 ZDA → KDY – fixed, agreed.** In `review/work/R09zda_hi.png` and `gq_compare.png` the first sign has the open head and long looped descender of g/K (as in JAK, PSANKO, AVSAK), not the closed "9" of q/Z, and the last sign is a plain `1` (Y) like the final sign of CELY on the same row. The cipher string is now `gt1` = KDY: *Kdy mi pošleš slíbené psánko?* Slovak: *Kedy mi pošleš sľúbený lístok?* The active-unit count is unchanged (R09 stays 41 units), so all global positions are unchanged.
2. **[minor] R02 BYCH has no CH mark – fixed, agreed.** `review/work/R02bych.png` shows a plain r-sign. The cipher string is now `p1r`, literal **BYH**; *bych* is an editorial CH (writer omitted the mark). Marked CH units are now 7 (ABYCH, VLASTNICH, SVYCH, MYCH, DLOUHYCH, VRELYCH, VASNIVYCH) and base letters 482; active units stay 475.
3. **Additional correction found on the requested R08–R09 re-check.** R08 `d3p5` (TOBE) was wrong: at 6× and 10× (`work/rev1/R08-tobe-*.png`) the second sign has the flat top bar of `5` (compare the final `5` of the same word and of `n3y5`), not the rounded top of `3` (as in `n3y5`, `fqb3n4m6n`). The row is now `d5p5` = **TEBE**: *Na tebe, dušičko moje, vzpomínám* – which is also the grammatical case after *vzpomínat na* (accusative), so the earlier *na tobě* was a transcription slip. The rest of R08 and R09 was re-read sign by sign against the 3× row crops and agrees.
4. **[minor] Over-hedged alternatives – agreed.** ROZEZVECELA (U/E at global 398) and MME (global 96) are not supported by the pixels (clear `2`; a narrow one-hump n followed by a two-hump m). They are kept in `work/uncertainties.json` only as rejected checks; the reading is ROZEZVUCELA and MNE. ANTILKEM (literal) vs *andílkem* (intended) remains an editorial repair, not a visual doubt.
5. **[minor] Attribution – clarified.** Download, transcription, key transfer and the DONE1 reading (`work/`, NOTES entries by "root"/"collaborator") were done by the earlier OpenAI GPT solver session on 2026-10-28 (its DONE1 marker names "OpenAI GPT-6 Codex"); the review-1 corrections above and the report were done by Claude Opus 5.5; the review was done by a separate Claude Opus 5.5 agent.

Remaining uncertainties after review: editorial repairs TESIC→*těšíš*, ANTILKEM→*andílkem*, TI→*ty*, BYH→*bych* (all writer slips, disclosed); the key is the known Anna Tichá family key, not recovered independently here.

English translation of the corrected editorial reading:

> A thousand thanks, my dearest Anička, for the lovely card. I myself, though, ought to come with a rod for Andělka, who diligently admonishes me to take care of myself, yet she heeds her own advice no more than she follows mine. Are you looking forward to the holidays very much? I will spend them as usual in Prague. At the office we are again quite busy and I will be glad when everything calms down again. I think of you, my darling, every day – morning, evening and the whole day. When will you send me the promised letter? Such a little angel you are, my dearest girl, and your love has made splendid music sound in my soul!! A thousand long, warm, passionate kisses are sent to you for ever by your Pepouš.
