# HCP 1535 - corrected decipherment report

Human solver: Tomáš Pavuk

Review1 by Claude Opus5.5 returned REVISE. All numbered findings have been addressed and checked by root. The review author explicitly permits closure after these corrections without a further round. No new ACCEPT verdict is claimed.

This is a manual transcription and known-key decryption of all visible active ciphertext on both sides of the postcard. The picture contains 16 main rows and three marginal rows. A canceled span after B09 PRACI is only partly legible: at least three apparent sign positions, with an f/V form in the middle and an uncertain looped final ascender. The whole word and exact original unit count remain unknown; the span is excluded from the active text. The address side has ordinary writing only.

This is **known-key transfer**, not independent key discovery. The Anna Tichá public partial study and the local shape-key from HCP1520 were available before transcription; no target plaintext was supplied. The public study is [Anna Tichá postcards](https://maxim-egorov.dev/research/anna-ticha-postcards/) with its archived partial-key text recorded in SOURCES.md. The additional published pc199 photograph supports shallow-v/F, an assignment not exercised on this card. Sources and reference hashes are recorded in work/reference-sha256.json. Root/collaborator source checks are solver collaboration, not independent review. A subsequent separate-provider Review 1 by Claude Opus 5.5 returned **REVISE**. This revision addresses all five findings, checked by root against the original pixels; the review verdict remains REVISE and is not relabelled ACCEPT. No watcher or reviewer was launched by this correction collaborator.

## Context and method

The rendered portal was checked in General, Description and Attachments by the root solver: Not solved, Czech, substitution, date 1903-10-13, recipient Anna Tichá, private collection; no attached transcription/solution. The 173-contribution register snapshot did not include this target. This is a bounded register check, not a worldwide novelty claim. The source image bears 13./X.1903; the address reads, with editorial accents, “Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.” The sender is not otherwise identified; the encrypted closing says Pepouš.

Each glyph was manually read from the original picture, not OCR. Whole-row crops in work/ accompany the transcription. The main frame is a lossless 90-degree counterclockwise rotation of source/picture.jpg; the margin frame is a 180-degree rotation. Neutral labels represent handwriting shapes, not ordinary Latin meaning. Small upper marks do not automatically supply modern accents; H represents the established special CH shape as one complete unit, including its upper mark.

| Cipher label | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | b | c | d | f |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Base plaintext | Y | U | O | I | E | A | J | L | P | S | T | V |

| Cipher label | g | h | m | n | p | q | r | s | t | H | v |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Base plaintext | K | R | N | M | B | Z | H | C | D | CH | F |

The v/F class is transferred but absent here. The supplied corpus uses y or 7 for the J-shaped unit; this transcription consistently uses 7. No target-specific new letter assignment was needed.

## Literal base-letter plaintext

The following retains source I/Y and source spelling. It supplies no Czech accents. The full ciphertext is in work/transcription.txt, the row geometry and literal output in work/transcription.json, and each active glyph in work/indexed-units.csv.

```text
B01 VRELY DIK ZA DRAHY LISTEK! ZARMOU-
B02 TIL MNE VSAK. ANUNKA MI URCITE
B03 SLIBILA, ZE V RIJNU PRIJEDE
B04 DO PRAHY! KDIZ SAMA NEVERI,
B05 ZE SE MI PO NI STYSKA A ZA
B06 SE NA NI VELICE TESIM, NEMA
B07 MNE SAMA RADA! - DOPIS ZASLU,
B08 JAKMILE SE MI TROCHU UVOLNI
B09 V NAHROMADENE PRACI.
B10 CTVRT ROKU NEB DALE, JAKO
B11 JA JSEM MUSEL CEKATI NA
B12 DOPIS, TO JISTE TRVATI
B13 NEBUDE! TISIC VRELYCH, DLOU-
B14 HYCH VASNIVYCH PUS OD PEPOUSE.
B15 SKODA, ZE MI POSLALA JAHODY BEZ VYZNAMU!
B16 BYL BYCH ZADAL, ABY HODNE BRZO PRIJELA DO PRAHY!
M01 KDYZ VSAK NEMAJI MITI JAHODI
M02 PRO MNE SVEHO VYZNAMU, NEVIM,
M03 MOHU-LI SE ODVAZITI, TOHO ZADATI..
```

The canceled B09 observations and the distinct excluded M03 u-like mark are described in Remaining limits and in the manual record; they are not silently counted as active text.

B01-B13 run downward in the main right block; B14 is immediately below, starting farther left, and HYCH continues B13 DLOU-. B15/B16 span the bottom. M01-M03 form a separate rotated marginal block. A right-edge arrow near B13 points upward; another arrow points into M01. The exact attachment point is uncertain because main lines continue below that right-edge arrow. Reading the marginal addition after B16 is an editorial order, not a proven unique arrow-based sequence. All physical rows are separately retained.

## Editorial Czech

Accents, capitalization and joined words are editorial. ANUNKA is kept. The source's B04 KDIZ is normalised to když, and marginal JAHODI to jahody, only here. The literal I/Y differences are retained above. The older wording “neb dále”, “čekati”, “trvati”, “míti” and “žádati” is preserved. The canceled span is not reconstructed.

Vřelý dík za drahý lístek! Zarmoutil mne však. Anunka mi určitě slíbila, že v říjnu přijede do Prahy! Když sama nevěří, že se mi po ní stýská a zase na ni velice těším, nemá mne sama ráda! - Dopis zašlu, jakmile se mi trochu uvolní v nahromaděné práci. [Přeškrtnutý nečitelný úsek.] Čtvrt roku neb dále, jako já jsem musel čekati na dopis, to jistě trvati nebude! Tisíc vřelých, dlouhých vášnivých pus od Pepouše. Škoda, že mi poslala jahody bez významu! Byl bych žádal, aby hodně brzo přijela do Prahy!

Když však nemají míti jahody pro mne svého významu, nevím, mohu-li se odvážiti, toho žádati…

## Slovak translation

Vrúcna vďaka za drahý lístok! Predsa ma však zarmútil. Anunka mi určite sľúbila, že v októbri príde do Prahy! Keď sama neverí, že sa mi po nej cnie a opäť sa na ňu veľmi teším, sama ma nemá rada! - List pošlem, len čo sa mi trochu uvoľní čas pri nahromadenej práci. [Prečiarknutý nečitateľný úsek.] Štvrť roka alebo aj dlhšie, ako som ja musel čakať na list, to určite trvať nebude! Tisíc vrúcnych, dlhých vášnivých bozkov od Pepouša. Škoda, že mi poslala jahody bez významu! Bol by som žiadal, aby veľmi skoro prišla do Prahy!

Keď však jahody pre mňa nemajú mať svoj význam, neviem, či sa smiem odvážiť o to žiadať…

## Reproduction and checks

From the repository root:

```sh
python3 ciphers/hcp-1535/work/decode.py
```

The command reads, never writes. It verifies hashes of both original images and source metadata, the manual record and row crops, the supplied reference files, every indexed unit, unchanged fixed-key identity, tokenwise and actual full-row inverse agreement, class counts, and equality of the JSON/CSV/text/SOLUTION literal records; it prints all literal plaintext. It uses the supplied manual image transcription as an input: it does **not** automatically extract letters from the photograph or independently prove transcription accuracy.

Result: **19 active rows, 437 active indexed cipher units, all assigned; 442 base letters; five CH units; 22 observed assigned classes; 0 unassigned active units.** I/4 has **39** occurrences and Y/1 **15** (before correction: 38 and 16). The count excludes spaces/punctuation/ordinary date/address and the canceled span. No denominator for all original uncanceled-plus-canceled glyphs is claimed. All rows produce continuous Czech using the same substitution; the letter, affectionate closing and ordinary address agree in context.

## Remaining limits

- B09 has at least three apparent canceled positions: a solid blot, an f-form/V whose upper loop and descender remain visible, and a looped ascender compatible with h/R or 8/L but uncertain. The full word and exact original count are unknown; the whole canceled span stays outside the 437 active units. Partial legibility does not reconstruct its original wording.
- B04 reads KDIZ versus M01 KDYZ; M01 reads JAHODI versus B15 JAHODY. Both I/Y differences are retained literally and normalised only editorially. M01 terminal I is faint: the current reading is 4/I, while 1/Y cannot be excluded completely at this source resolution. Root's earlier I/Y and ANUNKA source controls were solver collaboration. Review 1 subsequently identified the missed B04 I/4.
- Czech accents, exact space segmentation, and marginal-block insertion point are editorial. B04 PRAHY! has a visible upper stroke above its dot. M03 has two dots followed, slightly above the line, by a distinct upright u-like mark in the same ink. The mark differs from the key 2/U form, has unknown meaning, and is excluded from the cipher-unit index; it is not silently decoded as U.
- The meaning of the strawberries is not established by this text; no symbolic interpretation is added.
- Review 1 is a real separate-provider review with verdict REVISE. This correction response does not change that verdict or assert acceptance. FINAL status, PDF and register entry remain outside this collaborator's scope.

## Root verification - 2026-10-28

Root inspected both originals, all19 row panels, the full main/bottom/marginal regions, ANUNKA and I/Y controls, and the widened M01 crop. M01 terminal4/I is faint but its angular foot agrees with the local I class; literal JAHODI is retained separately from B15 JAHODY. The M01 crop was widened to include that terminal sign and its surround; coordinate/index/record hashes regenerated together. Arrow attachment of the marginal block remains uncertain, with all physical rows preserved separately.

Read-only decoder passed3 source hashes, record/crop/reference hashes, all437 indexed active units→442 base letters(five CH), literal equality and tokenwise key roundtrip. The canceled B09 span stays excluded with unknown exact original count (now visually bounded below by at least three apparent positions). These checks support a complete active-text candidate, not recovery of canceled wording or certainty about every faded stroke. Root's source-derived comparisons and crop correction are solver collaboration, not independent provider review.


## Response to review 1

Review read: `REVIEWED1` and `review/REVIEW1.md`, verdict **REVISE**, Claude Opus 5.5. The original source pixels were re-examined after reading the findings. New source-derived controls are in `work/review1-source-controls.png` and its five individual panels. This is the solver's correction response, not a new acceptance or FINAL assertion.

1. **B04 KDIZ - accepted and corrected.** In the 90° counterclockwise original frame, the disputed third sign of `gt4q` has two arms, curved left stroke and a foot like the I/4 in B01 DIK. M01 KDYZ and B04 PRAHY instead show the single flagged Y/1 stem. Changed `gt1q` to `gt4q`, literal KDYZ to **KDIZ**. Global active ordinal **83**, B04 unit **10**, changed 1/Y→4/I. I/4 rises **38→39** and Y/1 falls **16→15**; all 437 active positions and five CH units remain. KDIZ and JAHODI are disclosed together; only editorial Czech gives když/jahody, and the Slovak translation follows that interpretation. No key assignment changed.
2. **B04 PRAHY! - accepted and corrected.** The original-derived panel shows a separate vertical stroke above the punctuation dot. Changed `t3 bh6r1.` to `t3 bh6r1!`, producing **DO PRAHY! KDIZ**. Editorial Czech and Slovak preserve this sentence punctuation too; cipher counts are unchanged.
3. **B09 partial cancellation - accepted and clarified.** Original pixels show at least three apparent sign positions: first a solid blot, second the tall-loop f/V form with its descender, and third an uncertain looped ascender with bounded alternatives h/R or 8/L. Recorded these observations in `excluded_spans`; retained unknown whole word and exact original count. No guessed word, replacement unit, or all-original-glyph denominator was added. The span remains excluded from active counts.
4. **M03 distinct u-like sign - accepted and clarified.** After the two dots, slightly above the baseline, a separate upright u-like sign is visible in the same ink. It differs from this hand's cipher 2/U. Its meaning remains unknown; recorded as an excluded mark with source-frame box, outside the cipher-unit index, with no automatic U assignment.
5. **Portable reproducer - accepted and corrected.** The documented single command is now `python3 ciphers/hcp-1535/work/decode.py`; the decoder uses only the Python standard library and performs no writes. The authoring helper was inspected before execution and updated consistently, so future regeneration preserves the correction. Manual rows, indexed units, literal files, class counts and hashes were regenerated together. Source and fixed-key hashes remained unchanged. Final verification includes actual full-row inverse and exact literal/index/SOLUTION equality.


## Root closure checks after review1

Root inspected the reviewer's comparison strips and the fresh source-derived controls. B04's footed two-arm4/I differs from the flagged1/Y in M01 KDYZ and PRAHY; the active record correctly retains DO PRAHY! KDIZ. The B09 f/V and uncertain final loop remain partially visible under cancellation, without reconstruction of the word or exact original count. M03's distinct u-like mark remains excluded with unknown meaning. All five numbered findings are addressed; the fixed key, active scope and meaning are unchanged. The reviewer explicitly permits closure after these local corrections without another round.

The portable command passes the unchanged fixed-key/source/reference hashes, regenerated records, all437active indices, actual whole-row inversion and SOLUTION literal equality. These checks do not resolve the faint M01I/Y alternative or the marginal attachment point; both limits remain explicit. Source/review/old marker hashes are preserved in the closure-pass protected manifest. Root/helper source QA is solver collaboration, distinct from the existing Claude Opus5.5 independent review.

The latest complete337-contribution/303-HC-ID register does not contain this target. Expanded public work on other family cards is acknowledged in SOURCES.md; no global novelty claim is made. The final report and local register entry are prepared before FINAL; no external submission occurs. Solver name is TODO because no name was supplied for these entries.


## Original source photographs

![Original picture side, preserved unchanged.](../source/picture.jpg)

![Original address side, preserved unchanged.](../source/address.jpg)

## Source record and attribution

## Sources - HCP 1535

- Rendered portal: https://crypto.hcportal.eu/dashboard/cryptograms/1535; all three tabs inspected 2026-10-28. Original metadata in source/metadata.md. Not solved; no transcription or solution attached.
- source/picture.jpg: https://api.hcportal.eu/media/4665/conversions/pc_hcp_216_pic-large.jpg ; exact full URL observed after opening the picture modal, downloaded 2026-10-28.
- source/address.jpg: https://api.hcportal.eu/media/4666/conversions/pc_hcp_216_adr-large.jpg ; exact full URL observed after opening the address modal, downloaded 2026-10-28.
- AI register https://ai.hcportal.eu/register/ rendered Show all: 173 contributions,139 HC Portal source IDs; this target absent. Snapshot batches/easy-2026-10-28/register-snapshot-173.json. Bounded check, no worldwide novelty claim.
- Public family/key reference known before transcription: https://maxim-egorov.dev/research/anna-ticha-postcards/ ; generic key https://maxim-egorov.dev/downloads/anna-ticha-postcards/anna-ticha-partial-key-and-rules.txt archived in batches/easy-2026-10-28/published-anna-ticha-key.txt. Transfer, not independent key discovery.
- Photographic reference for shallow v/F: published pc199/HCP1518 image https://api.hcportal.eu/media/4614/pc_hcp_199_pic.JPG archived in batches/easy-2026-10-28/public-reference-199/picture.jpg, provenance.json. Reference proposed RUDOLFINA corroborates this shape. Available before this target transcription; prior study remains partial. No target plaintext supplied.

Source files immutable after acquisition. Manual image transcription is not OCR. Root/subagent work is solver collaboration, not independent provider review. No watcher or reviewer authorized.

Fresh rendered family-index check: eleven partial target pages, none for pc216-218; batches/easy-2026-10-28/family-index-pc216-218.json. This is bounded prior-publication evidence, not a global novelty claim.


### Updated register observation before closure

The complete rendered register was rechecked on2026-10-28:337contributions and303distinct HC Portal IDs, with HCP1535 absent. The full ID set matches register-snapshot-337.json; current browser evidence is register-check-pc235-continuation.json in batches/easy-2026-10-28/. Public documentation for additional other family cards is now known; the earlier eleven-page index is a historical bounded check. No current target-specific published plaintext was consulted. The public generic key and family research remain credited; no worldwide novelty or priority is established.
