# HCP 1526 - corrected Czech postcard report

Human solver: Tomáš Pavuk

Independent Review1 by Claude Opus5.5 returned REVISE. The local findings have been addressed and checked against the source. The reviewer explicitly permits closure after these corrections without a further round. The original review verdict is preserved; no new ACCEPT verdict is invented.


Round-1 solver corrections checked by root; the existing independent review is **REVISE**. The complete visible message is included: **16 physical rows, 497 active cipher units, 504 output base letters, seven CH units**. One singleton assignment, the shallow v-shaped sign to F in DOUFAM, remains a target-specific contextual inference. Thus this is a complete transcription and candidate reading, not a claim that every assignment has independent visual confirmation.

## Origin and reading order

HC Portal describes a Czech substitution postcard dated 1903-12-12, recipient Anna Tichá, private collection, status Not solved. Root inspected rendered General, Description and Attachments and both original image sides. No individual transcription or solution was attached. The ordinary picture-side date reads `12./XII.1903.`. The ordinary address sends the card to Anna Tichá, a teacher in Žirovnice near Počátky. The writer signs PEPOUS in cipher; his civil identity is not established. A woman with swallows is depicted.

The picture-side cipher reads after a lossless 90° counterclockwise rotation, producing the 674×1024 working image. The first six rows have short left fragments and long right continuations separated by the picture/blank area. Read **across each physical row**, left fragment then right continuation. Reading the entire left column first would scramble the message. The remaining ten rows run across the width. Both image sides were inspected; the address side contains ordinary writing, not additional cipher rows.

## Method, transferred key and prior publication

This is key transfer and source transcription, not independent discovery of a new key or cipher family. The mixed digit/Latin key used on HCP 1520-1525 was available from the start. No target plaintext was supplied during the initial transcription. This correction pass uses the existing Review1 findings and fresh original-pixel comparisons; it is not blind. Maxim Egorov / Cipher-Atelier had already published a generic partial key and eleven partial Anna Tichá card readings at https://maxim-egorov.dev/research/anna-ticha-postcards/ . Root's bounded index inspection listed pc198, 440, 250, 453, 329, 199, 458, 441, 338, 339 and 200, not pc207. The public key and exact provenance are preserved in `batches/easy-2026-10-28/published-anna-ticha-key.txt` and the adjoining provenance JSON. Root also checked the rendered AI register: this ID was absent from 158 contributions / 124 HC Portal IDs. Those are dated capture-time observations, not a refreshed census or worldwide priority claim. The current local register-exclusions file has no 1526 entry; that does not establish novelty or authorize a submission.

The public text includes a rare neutral class `G16 → f`, but contains no glyph photographs. It does **not** establish that our target's shallow v-shaped sign is G16. Its tentative assignment to F is inferred from the target singleton `t32v6n` and its Czech context, with the source shape separately preserved. It is clearly different from the tall looped f-shaped V used repeatedly elsewhere. A future visual comparison to original family scans could strengthen or refute this assignment; none is claimed here.

The ASCII labels below name shapes, not ordinary literal ciphertext letters. `ř` labels the capped h-like special unit CH. Other small r- and h-like forms remain separate. Attached marks are retained in the images, while this candidate addresses the base-letter layer. Restored Czech accents are editorial, not a proven encoded diacritic layer.

| Cipher labels | Plaintext |
| --- | --- |
| `1 2 3 4 5 6 7 8` | `Y U O I E A J L` |
| `b c d f g h` | `P S T V K R` |
| `m n p q r s t` | `N M B Z H C D` |
| `ř` special capped form | `CH` |
| `v` shallow open form, tentative singleton | `F` |

All 23 listed labels occur. `work/transcription.json` records every physical row, its cipher labels, candidate plaintext, unit count and bounding rectangle. `work/positions.json` indexes each active unit by global position (1-497), row-local ordinal and text column; none of those indices is an individual photographic glyph coordinate. Four `indexed-rows-*.png` panels align source rows and transcripts. Row rectangles overlap because ascenders and descenders overlap adjacent rows.

## Literal base-letter candidate

Punctuation, spaces and capitalization are manually represented. R03 retains **SECONA** and **PRNEM**, and the nine newly corrected literal slips below are retained consistently. Intended Czech forms belong only to the editorial layer. R04's F is tentative as described above; the mechanical decoder prints F using the explicitly provisional key.

```text
VRELY DIK, ZLATO MOJE, ZA DRAHY LISTEK.
JSEM ODE STREDY OPET V URADE, KDE JEST
VANOCNI SECONA JIZ V PRNEM PROUDU. MAM
SICE JESTE TROCHU RYMU, AVSAK DOUFAM, ZE JSEM
CHRIPKU JIZ PREMOHL. VZPOMINAM VSAK NA
SVE CRDECKO, KDERE NYNI ZACE MISTO
MNE CHRIPKA TRAPI. NACHLADILA SE BEZPOCHYBY
BEHEM JIZDY PO DRAZE. MUSI SE ME SRDECKO
HODNE SETRIDI, JAKO MNE DO MA ANDULICKA
SAMA TAK DUTKLIVA RADILA. PROSIM JI O TO.
TAZE SE, ZDA JSEM NA NI VZPOMINAL, KDYZ
MNE HLAVA BOLELA. ZAJISTE, DRAHOUSKU,
VZDIT JSEM BYL TEMER STALE SAM. VZPOMINAL
JSEM MNOHO A VRELE. TISIC DLOUHYCH, VASNIVYCH
PUS POSILA TI TVUJ PEPOUS, KDERY SE VELICE
TESI NA SLIBENE PSANKO.
```

## Editorial Czech reading

Accents and paragraphing are editorial. Bracketed uppercase forms explicitly record every anomalous literal base form; they are not new cipher text. DOUFAM remains dependent on the tentative F assignment. The corrected source name is ANDULICKA, editorial **Andulička**, not the earlier incomplete Andulka.

Vřelý dík, zlato moje, za drahý lístek. Jsem ode středy opět v úřadě, kde jest vánoční **secona [patrně: sezona]** již v plném **[doslova PRNEM]** proudu. Mám sice ještě trochu rýmu, avšak doufám, že jsem chřipku již přemohl. Vzpomínám však na své srdéčko **[CRDECKO]**, které **[KDERE]** nyní zase **[ZACE]** místo mne chřipka trápí. Nachladila se bezpochyby během jízdy po dráze. Musí se mé srdéčko hodně šetřiti **[SETRIDI]**, jako mně to **[DO]** má Andulička sama tak důtklivě **[DUTKLIVA]** radila. Prosím ji o to.

Táže se, zda jsem na ni vzpomínal, když mne hlava bolela. Zajisté, drahoušku, vždyť **[VZDIT]** jsem byl téměř stále sám. Vzpomínal jsem mnoho a vřele. Tisíc dlouhých, vášnivých pus posílá ti tvůj Pepouš, který **[KDERY]** se velice těší na slíbené psánko.

## Slovak translation

Srdečná vďaka, zlato moje, za drahý lístok. Od stredy som opäť v úrade, kde je vianočná **[pravdepodobne: sezóna; doslova SECONA]** už v plnom prúde. Mám síce ešte trochu nádchu, ale **dúfam [závisí od predbežného F]**, že som už premohol chrípku. Myslím však na svoje srdiečko, ktoré teraz zase namiesto mňa trápi chrípka. Bezpochyby prechladla počas jazdy vlakom. Moje srdiečko sa musí veľmi šetriť, ako mi to moja Andulička sama tak dôrazne radila. Prosím ju o to.

Pýta sa, či som na ňu myslel, keď ma bolela hlava. Iste, drahúšik, veď som bol takmer stále sám. Myslel som na teba veľa a vrúcne. Tisíc dlhých, vášnivých bozkov ti posiela tvoj Pepouš, ktorý sa veľmi teší na sľúbený listík.

The translation identifies the addressed `srdečko` with Anna/Andulička from the feminine Czech clauses. This is linguistic interpretation, not an additional encoded name. `Po dráze` is interpreted as railway travel in context.

## Reproduction and limits

From the repository root, run this single read-only command:

```bash
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I
  ciphers/hcp-1526/work/decode.py
```

The command is read-only and uses the bundled Python/Pillow runtime. It checks the three immutable originals against this target's three entries in the frozen batch guard, eight immutable inputs (including original source/provenance and existing review/markers), two published-reference hashes and 40 canonical record hashes. It verifies all 497 global/row/column indices, exact 16 row totals, 504 output letters, seven CH expansions, all 23 used labels and the one tentative F. It checks the saved literal, the native lossless rotation, 12 raw nearest-neighbor source controls and four refreshed indexed row panels. Finally it inverse-encodes the **entire plaintext** under the full fixed inverse key, greedily taking CH as one unit. It does not construct the inverse by looking up each saved source token. The current target's exclusion flags are checked dynamically; the shared exclusion file is not rebaselined or modified. The command writes nothing.

`make-record.py`, `make-controls.py` and `make-review1-controls.py` are separate mutators. Each was inspected before use. The source pins are checked before regeneration and are no longer silently re-created from current source bytes. Only the command above is the final reproduction command. `work/record-sha256.json` enumerates the 40 canonical current records, including this solution and notes; historical scratch crops outside it are not new claims.

This is not OCR. The image-to-glyph transcription remains manual. Hashes establish source identity; round trips establish consistency between the key and transcription. Neither independently proves a visual reading. No blind held-out test or statistical accuracy percentage is claimed. The entire target was available while applying the transferred key.

Focused source controls are in `work/source-controls.png` and the additional `work/sezona-controls.png`. Exact rectangles and transformations are recorded in their JSON/generator files:

- The separated left fragments belong to their corresponding right rows. R02 is JSEM ODE STREDY OPET, not an isolated margin message or an invented STEDRY OBED.
- R03 `c5s3m6` contains the short angular s-shaped C sign, matching angular C in VANOCNI and the corrected literal CRDECKO. It lacks the long q-shaped Z descender seen in ZLATO and TAZE. Literal SECONA is preserved; SEZONA is an editorial interpretation.
- R04 `t32v6n` contains a shallow v-shaped singleton. It is not the tall f-shaped V seen in VZPOMINAM and VSAK. F is a contextual candidate, not a separately established shape-to-letter transfer from the public neutral G16 label.
- R07 NACHLADILA and BEZPOCHYBY have capped CH units. R08 BEHEM has the uncapped H unit. The comparison is supplied, without claiming every ancillary mark has been decoded.
- R11 `d6q5` is TAZE, not TAKE: its third unit has the q-shaped Z descender; K in nearby KDYZ is a separate g-shaped form.

## Apparent writer slips and correction controls

At this scan resolution the writer repeatedly appears to use paired signs where the intended Czech word needs the other value; the literal layer now records every such case consistently. This is a statement about the visible classification, not proof of what a higher-resolution physical-card inspection would show.

| Row | Literal retained | Editorial interpretation | Source distinction |
|---|---|---|---|
| R03 | SECONA | sezona | angular s/C, not descending q/Z |
| R03 | PRNEM | plném | tall looped h/R, like adjacent PROUDU, not digit 8/L |
| R06 | CRDECKO | srdéčko | angular initial s/C, like its fifth C; R08 correctly has round c/S |
| R06 | KDERE | které | crossed t/D, not looped d/T |
| R06 | ZACE | zase | angular s/C, not round c/S |
| R09 | SETRIDI | šetřiti | second expected T is crossed t/D; first remains looped d/T |
| R09 | DO | to | crossed t/D, not looped d/T |
| R10 | DUTKLIVA | důtklivě | terminal closed 6/A, not 5/E |
| R13 | VZDIT | vždyť | underbarred 4/I, not footed 1/Y; compare BYL |
| R15 | KDERY | který | crossed t/D, like KDERE |

`work/review1-panel-1.png` through `review1-panel-3.png` show 12 fresh native-source nearest-neighbor controls. Every exact context box, transformation and crop file is in `review1-controls.json`; they are context boxes, not individual glyph segmentation. `review1-corrections.json` records ten changed word sites: nine one-label replacements and the insertion of two formerly missed labels `4s` in `6mt284sg6` (ANDULICKA). This adds I and C to the name, not a new key entry. ANDULICKA occupies global positions 275-283; the newly included I/C are positions 280-281. The row-9 count rises from 30 to 32; later global indices shift by two.

All visible message rows and marginal fragments are represented. No extra canceled unit is asserted: heavy ink and background marks are not counted as additional historical letters. One F assignment remains tentative; accents, exact postmark readings, writer identity and historical glyphs beneath any retracing remain outside the established claim. No new reviewer, PDF, register entry or finalization is produced by this correction. The existing independent Review1 remains REVISE; root has checked all findings and corrections.


## Response to review 1

The existing `review/REVIEW1.md` and `REVIEWED1` are unchanged. All eight findings were checked against native original pixels after lossless counterclockwise rotation. This is a solver correction checked by root, not a new independent acceptance.

1. **ANDULICKA and missed 4s - fixed.** The full source sequence is `6mt284sg6`: after `6mt28` the underbarred 4/I and angular s/C are visible before g6. `transcription.txt`, the generator/JSON record, literal, global/row/column indices and indexed panels now include both units. Czech and Slovak name forms are Andulička. Exact totals are now 497 units / 504 base letters / seven CH, with row09=32. Native control 06 and the full-row control 05 preserve the evidence.
2. **Four crossed D-for-T forms - retained literally.** Same-card STREDY contains both looped d/T and crossed t/D, providing the control. KDERE (R06), SETRIDI's second expected T (R09), DO (R09) and KDERY (R15) all use the crossed t/D class in the original. No key changes were made. Their intended Czech T is marked editorially; the literal D remains. Controls 01/03/05/09 document them.
3. **Two angular C-for-S forms - retained literally.** R06 begins `sht5sg3` (CRDECKO), with the same angular C class initially and fifth; R08 SRDECKO contrasts the round c/S initial. R06 `q6s5` yields ZACE. Both repairs are explicit only in the editorial reading. Controls 03/04 document the round/angular distinction.
4. **PRNEM - fixed literally.** The second sign of `bhm5n` is tall looped h/R, matching R in adjacent `bh32t2` PROUDU, rather than digit 8/L. PRNEM remains literal; plném is editorial. Control 02 retains both words.
5. **DUTKLIVA - fixed literally.** R10 ends `t2dg84f6` in a closed 6/A. DUTKLIVA is retained and důtklivě is explicitly editorial. Control 07 retains that final glyph without substituting 5/E.
6. **VZDIT - fixed literally.** R13 `fqt4d` contains underbarred 4/I, contrasting with the footed 1/Y in nearby BYL. VZDIT remains literal; vždyť is editorial. The same 4 class occurs in ANDULICKA. Control 08 preserves the comparison.
7. **Agreed disclosures retained.** SECONA remains literal. The shallow open v in DOUFAM is distinct from tall-looped f/V but stays a target-specific contextual F singleton; no asserted photographic equivalence to public G16 is added. ODE/OPET/TAZE, seven capped CH units and uncapped H in BEHEM are unchanged. Controls 10-12 and the original controls retain those distinctions.
8. **Method and paired-sign slips - made explicit.** The table above lists all apparent slips, including the previously retained SECONA, and states the recurring paired-sign pattern at the available resolution. The reproduction command replays a manual transcription. Hashes, indices and inverse consistency cannot detect or validate a missed/wrongly classified source sign by themselves. No OCR, blind test or percentage accuracy claim is made. Native comparisons supply the visual evidence; physical-card/high-resolution limits remain.

The existing reviewer's already-written read-only decoder was inspected and rerun; it now reports **16 rows, 497 units, 504 base letters, CH=7, F=1 and no differences** from the corrected labels. No reviewer agent was launched, and reusing this existing comparison is not a new review. The final read-only audit passes all source/input/reference/40 record guards, saved reading, indexed/control pixels and the whole-plaintext fixed-key inverse. Root has inspected these corrections before closure. No source, SOURCES, existing review, marker, PDF, register or Git state was changed by this collaborator.


## Root closure checks after review1

Root compared all twelve fresh native/nearest-neighbor controls and the review findings. The full source name contains4s, yielding ANDULICKA, with I/C inserted at global280-281. Same-card looped/crossed T/D, angular/round C/S, tall-loop R versus8/L, closed6/A versus5/E and footed1/Y versus underbarred4/I support all nine literal replacements. The apparent writer slips remain literal; only the separate editorial reading repairs them. The shallowv/F singleton remains contextual and is not promoted to independently photographed G16 equivalence. All eight numbered findings are addressed; the reviewer explicitly allows closure after these corrections without another round.

The latest complete rendered AI register contains337contributions/303distinct HC Portal IDs, with this target absent. The full IDs matched the previous snapshot; the current evidence is batches/easy-2026-10-28/register-check-review207-208-210-next.json. Expanded public work on other family cards is acknowledged; the earlier eleven-page index is a historical bounded observation. No target-specific public plaintext was consulted for this correction beyond the existing independent review. This check establishes neither worldwide novelty nor historical priority. The six human-directed exclusions in register-exclusions.json remain in force; this target is not one of them.

The final read-only reproducer passes after the correction response; source/review/old markers remain protected by the closure-pass manifest. Root/helper checking is solver collaboration, distinct from the existing independent Claude Opus5.5 review. The report and local register entry are prepared before FINAL. No watcher, new reviewer, external submission, commit or push is performed. Solver name remains TODO because no name was supplied for these entries.


## Original source photographs

![Original picture side, preserved unchanged.](../source/picture.jpg)

![Original address side, preserved unchanged.](../source/address.jpg)

## Source record and public attribution

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1526 . All three rendered tabs and both source sides were inspected; no individual attached solution or transcription was displayed.

- Original picture image: https://api.hcportal.eu/media/4638/conversions/pc_hcp_207_pic-large.jpg
- Original address image: https://api.hcportal.eu/media/4639/conversions/pc_hcp_207_adr-large.jpg

Prior generic family research and partial key: https://maxim-egorov.dev/research/anna-ticha-postcards/ . This is known-key transfer with manual transcription. Current337-contribution/303-HC-ID register does not list this target. Public work on other family cards and the six explicit local registry exclusions remain acknowledged; no worldwide novelty or historical priority is claimed. Full source history is in SOURCES.md.
