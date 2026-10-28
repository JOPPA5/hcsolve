# HCP 1527 — pc_hcp_208

Solver correction after separate-provider **Review 1: REVISE** (Claude Opus 5.5). This response addresses the findings; it does not claim reviewer acceptance or FINAL. The complete visible cipher is read as Czech by applying the existing Anna Tichá family key. This is **known key transfer**, not a new key discovery or a claim of historical priority.

## Source and context

Source: https://crypto.hcportal.eu/dashboard/cryptograms/1527 . Root inspected rendered General, Description and Attachments on 2026-10-28. The portal showed **Not solved**, Czech, Substitution, private collection, date 1903-12-19, unknown sender, recipient Anna Tichá. Both original postcard sides and immutable rendered metadata are in `source/`; exact observed image URLs are in `SOURCES.md`. No individual transcription or solution was attached. The ordinary address calls Anna Tichá a teacher in Žirovnice near Počátky. The picture is a romantic portrait with birds; all cipher writing lies below the portrait after rotating the image 90° counterclockwise. The handwritten ordinary date is `19.XII.1903`. The cipher signature is PEPOUS; expanding this nickname to a civil identity is unsupported.

Root checked the newer rendered AI register: 158 contribution rows, 124 HC Portal IDs, target absent. This bounded check does not establish worldwide novelty. Maxim Egorov / Cipher-Atelier's previously published generic partial family key and eleven partial card readings are acknowledged in `SOURCES.md`, with the public key and exact provenance in `batches/easy-2026-10-28/`. No published target plaintext was supplied. The supplied HCP 1520–1525 family key was available before this reading began; no independent recovery is claimed.

## Cipher, key and exact procedure

Monoalphabetic substitution using handwritten digits and Latin-looking forms, with one special glyph encoding the Czech digraph CH. Labels are conventional shape labels; printed characters below are not diplomatic font reproductions. Distinct `m` and `n` labels retain the family convention: `m` means N, `n` means M.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 7 | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | ř (special family glyph) | CH | | | | |

Procedure: verify the three source hashes, rotate picture.jpg by a lossless 90° counterclockwise transpose, manually transcribe the twelve visible rows into `work/transcription.json` using the indexed row boxes, and replace each shape label through `work/key.json`. Preserve line breaks, the SEDLAC-/KOVA split, and the source's separate/adjacent word spacing without treating spaces as cipher units. The apparent spacing within CASTECNE is joined as one word; VPOLEDNE is left joined in the base reading. Punctuation is visually transcribed and excluded from letter counts. `ř` is a neutral label for the special CH glyph; it does not mean the plaintext letter Ř.

Single reproduction command, from repository root:

```sh
python3 ciphers/hcp-1527/work/decode.py
```

This command is read-only by default and uses Python's standard library. It verifies source hashes and record hashes, decodes all rows, checks the 415 indexed positions, explicit class counts, the unchanged fixed key, tokenwise and actual whole-row inverse, and saved/SOLUTION literal equality, and prints the full base text. Manual image transcription is a documented input, not automatic OCR; the round trip proves internal consistency rather than independently validating glyph readings. `work/indexed.png`, twelve `work/Rxx.png` row crops and `work/focused-controls.png` allow image checking. Review-specific original-derived controls are in `work/review1-controls.png`, with native boxes/transforms in `work/review1-controls.json` and nine individual panels. Row coordinates are for the upright 674×1024 working image; CSV character indices do not falsely claim individual pixel boxes. `build-record.py` and `make-controls.py` are explicit record/crop generators, not the default command.

## Literal base plaintext

No inferred missing letter or grammatical correction is inserted. Accents are not included in this base-letter transcription. The word PRED in row 7 is underlined in the source.

```text
VRELY DIK ZA DRAHE PSANKO. OBSAHEM JEHO BYL
JSEM CASTECNE VELMI PREKVAPEN. CLECNA SEDLAC-
KOVA SE ASI MNOHO PRESLECHLA; NEMAM O TETO NME
URCOVANE NEVESTE ANI TUSENI. NENALEZIM TEZ
K TEM, KDOZ DAJI SI SNAD URCOVATI SVOJI NEVESTU
JINYMI.
PRANI SVEHO SRDECKA SPLNIM A ODPOVIM MU PRED
CTVRT ROKEM. JSEM NYNI CELE DNY V URADE A TAKE
SE DOLE STRAVUJI; JEN NAHODOU ZASEL JSEM DNES
VPOLEDNE DOMU. TISIC VRELYCH PUS A POZDRAVU POSILA
TI TVUJ PEPOUS, KTERY SVEMU CRDECKU PREJE, ABY
STRAVILO HODNE HEZKE SVATKY. BUDU VZPOMINATI.
```

## Editorial Czech reading

Accents, ordinary capitalization, and the space in *v poledne* are editorial. SEDLAC-/KOVA is joined as Sedláčková. Literal CLECNA, NME and CRDECKU are normalised only here to slečna, mně and srdéčku; the literal layer preserves these writer's slips. The unusual *před čtvrt rokem* is retained, not silently changed to a more conventional seasonal greeting.

> Vřelý dík za drahé psánko. Obsahem jeho byl jsem částečně velmi překvapen. Slečna Sedláčková se asi mnoho přeslechla; nemám o této mně určované nevěstě ani tušení. Nenáležím též k těm, kdož dají si snad určovati svoji nevěstu jinými.
>
> Přání svého srdéčka splním a odpovím mu **před** čtvrt rokem. Jsem nyní celé dny v úřadě a také se dole stravuji; jen náhodou zašel jsem dnes v poledne domů. Tisíc vřelých pus a pozdravů posílá ti tvůj Pepouš, který svému srdéčku přeje, aby strávilo hodně hezké svátky. Budu vzpomínati.

R10 literally reads POSILA with the underbarred I/4 sign. The earlier *posýlá* claim was a transcription error and has been removed.

## Slovak translation

> Vrelá vďaka za drahý lístok. Jeho obsah ma čiastočne veľmi prekvapil. Slečna Sedláčková sa asi poriadne prepočula; o tejto neveste, ktorú mi určujú, nemám ani tušenie. Nepatrím ani k tým, ktorí si nechajú svoju nevestu určovať inými.
>
> Želanie svojho srdiečka splním a odpoviem mu „pred štvrť rokom“ [doslovné nezvyčajné znenie]. Teraz som celé dni v úrade a tiež sa dole stravujem; iba náhodou som dnes na poludnie zašiel domov. Tisíc vrúcnych bozkov a pozdravov ti posiela tvoj Pepouš, ktorý svojmu srdiečku želá, aby prežilo pekné sviatky. Budem spomínať.

The quoted temporal phrase is deliberately not resolved by guessing an intended different text. It may be playful about reply delay, but that is interpretation, not decipherment.

## Coverage and remaining uncertainties

- Twelve rows contain **415 active cipher units**, including **2 CH units**, producing **417 base letters**. All have preferred assignments under the unchanged transferred key; no active unit is unassigned. One retraced R06 position remains less certain with a bounded alternative. No canceled cipher unit was identified. Date, address, punctuation and underline are outside this denominator.
- R01 PSANKO is the six-unit `bc6mg3`; the penultimate shape matches K in DIK rather than Z in ZA. The diminutive is retained.
- R04 NENALEZIM TEZ retains the visible multi-hump `m` = N family shape. No replacement from a language model is used.
- R07–08 visibly says PRED / CTVRT ROKEM. R08 opening is `sdfhd`, i.e. C-T-V-R-T. Final T (`d`) has the looped body, whereas D (`t`) at the end of PRED has a straighter crossed stem. Both are shown in focused controls. No word or cipher glyph is supplied from an expected greeting.
- R10 has a separate small caron associated with the final portion of VRELYCH. It is documented as a diacritic mark, not counted as an extra cipher base unit. Base-letter coverage is not a claim to recover every encoded accent. The accented reading throughout is editorial.
- R02 has a clear angular `s`/C after A in `c5t86s-`, giving SEDLAC-/KOVA. The editorial surname is Sedláčková; her identity is not established.
- Literal writer's slips are R02 CLECNA (initial angular C sign instead of round S), R03 NME (`mn5`, N-M-E rather than M-N-E), and R11 CRDECKU (initial C, against the round S of R07 SRDECKA). These are not repaired by changing the key. The repeated C-for-S slip is a tendency visible twice on this card; Review 1 also notes parallels on HCP1526, which this correction did not re-examine.
- R06 JINYMI's fourth sign (global position187 / row position4) is retraced, with a closed 2-like upper loop. Its height and foot favour 1/Y, retained as the preferred literal; 2/U is a bounded visual alternative (JINUMI). `uncertain_positions` records both without treating either as a new key assignment. Thus 0 unassigned active positions does not mean 0 visually uncertain positions.
- Word boundaries, punctuation and accents are less mechanically constrained than the substitution letters. Sender identity and historical implications of the proposed bride are not established.

The evidence is a consistent full-card key application and readable correspondence, with anomalous wording preserved. There is no held-out test, blind key recovery or publication claim. Separate-provider Review 1 returned REVISE; this correction response does not change that verdict to acceptance. No DONE/FINAL marker, PDF or register entry is created by this solver collaborator; root has inspected the source controls before closure.


## Root verification before handover — historical, before Review 1

Root inspected both original sides, the full enlarged twelve-row body and focused source controls on 2026-10-28. The looped final d/T in CTVRT differs from the crossed t/D in underlined PRED. The source-specific phrase PRED CTVRT ROKEM remains unresolved in meaning without altering its letters. PSANKO, NENALEZIM TEZ and POSYLA are retained as read. Root ran the documented command: all original and record hashes, 414 indexed units, two CH expansions and tokenwise round trip passed. Sources matched the wave manifest. This is a second solver check using the known key, not independent provider review.


The preceding root check records the pre-review state. Review 1 subsequently identified the missed C and five other issues. The current literal and counts above supersede its historical POSYLA/414-unit reading. Source controls and solver collaboration are distinct from the separate-provider review.

## Response to review 1

Read `REVIEWED1` and `review/REVIEW1.md` (Claude Opus 5.5, **REVISE**). Re-examined both full original sides and the disputed positions using new crops generated directly from the original picture with a lossless counterclockwise transpose. `work/review1-controls.png` and its nine panels retain the evidence; `review1-controls.json` records exact boxes and display scaling. This is a solver correction, not acceptance or FINAL.

1. **Missed C in SEDLAC-/KOVA — corrected.** The original R02 `c5t86s-` contains a distinct angular s/C between A and the hyphen. Added this unit (new R02 position38 / global73), giving **SEDLAC-/KOVA**, editorial **Sedláčková** in Czech and Slovak. Counts increase 414→**415** units and 416→**417** base letters; CH stays2. Identity of the woman remains unestablished.
2. **POSILA, not POSYLA — corrected.** R10 `b3c486` has the underbarred 4/I form, distinct from the flagged/footed 1/Y in BYL. Changed that sign (R10 position39 / new global338) to I. Literal **POSILA**, editorial **posílá**. Removed the incorrect archaic-posýlá assertion. Preferred class totals: I/4 **23→24**, Y/1 **10→9**.
3. **Literal NME — corrected.** R03 final `mn5` has m/N then n/M, opposite the `nm`/MN order in MNOHO in the same row. Recorded **NME** literally; Czech mně and Slovak interpretation remain editorial. New global107–108 / R03 positions34–35 reflect the transposition; m/n class counts do not change.
4. **Literal CLECNA and CRDECKU — corrected.** R02's first and fourth signs in `s85sm6` share the angular s/C form, unlike round c/S in JSEM and CASTECNE. R11 `sht5sg2` likewise starts with angular C, against R07 `cht5sg6` with round S. Retained **CLECNA** and **CRDECKU** literally; normalised only in the editorial layer. The fixed key remains unchanged. With the added C from finding1, C/s totals **10→13** and S/c **32→30**. Repeated C-for-S slips on this card are disclosed.
5. **Retraced JINYMI sign — uncertainty added.** Preferred reading 1/Y is retained, consistent with its height and foot, but the heavy upper loop is 2-like. Added explicit bounded alternative 2/U in `uncertain_positions`, R06 position4 / global187. No automatic normalization, deletion or additional unit; the literal remains JINYMI with this caveat.
6. **Agreements checked and retained.** Original-derived controls and the full rows confirm PSANKO; the hooked q/Z in NENALEZIM TEZ versus looped g/K in K TEM/KDOZ; `sdfhd h3g5n` = CTVRT ROKEM; underlined PRED; and the marked CH of VRELYCH. The meaning of PRED CTVRT ROKEM remains unresolved, with no grammatical filling. No correction to these agreed readings or key was needed.

All manual rows, positions, saved literal/transcription, class totals and source-linked crop/code hashes were regenerated together after inspecting the authoring scripts. The portable documented decoder is read-only and checks immutable source hashes, unchanged key, reference hashes, actual full-row inverse and exact row/index/saved/SOLUTION equality. Final preferred counts: **12 rows;415 units;2 CH;417 base letters;22 observed classes;0 unassigned units;1 explicitly uncertain assigned sign**. No watcher/reviewer was launched; source/review/marker/PDF/register/git writes remain outside this correction.


## Root closure checks after review1

Root inspected the native source-derived comparison panels and the review findings. The angular C after SEDLA is visible before the line-end hyphen, and the resulting surname is SEDLAC-/KOVA, editorial Sedláčková. POSILA has underbarred4/I; the m/n order of NME and angular initials of CLECNA/CRDECKU are retained literally. The retraced JINYMI sign keeps preferredY with the bounded U alternative, rather than being called visually certain. All six findings are addressed; the reviewer explicitly allows closure after the listed local corrections without another round.

The latest complete rendered AI register contains337contributions/303distinct HC Portal IDs, with this target absent. The full IDs matched the previous snapshot; the current evidence is batches/easy-2026-10-28/register-check-review207-208-210-next.json. Expanded public work on other family cards is acknowledged; the earlier eleven-page index is a historical bounded observation. No target-specific public plaintext was consulted for this correction beyond the existing independent review. This check establishes neither worldwide novelty nor historical priority. The six human-directed exclusions in register-exclusions.json remain in force; this target is not one of them.

The final read-only reproducer passes after the correction response; source/review/old markers remain protected by the closure-pass manifest. Root/helper checking is solver collaboration, distinct from the existing independent Claude Opus5.5 review. The report and local register entry are prepared before FINAL. No watcher, new reviewer, external submission, commit or push is performed. Solver name remains TODO because no name was supplied for these entries.
