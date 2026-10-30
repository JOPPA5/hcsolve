# HCP1554 / pc_hcp_235 — Pepouš to Anna Tichá, 22 May 1903

**Current position (after review 1, 2026-10-29):** the card is read in full. One word, U6 (*mne*), is a weaker reading and is marked as such. This section and "Response to review 1" below state the current solution. Everything under "History (superseded)" is the earlier text: an initial partial candidate by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol), and Claude Opus 5.5's completion note before review. It is kept for the record only. Where it disagrees with this section (for example "partial", "no G", "no marker", `k hradce`, `⟦U4⟧`/`⟦U6⟧`), this section wins.

## Cipher and key

The cipher is a monoalphabetic substitution with a special unit for Czech CH. It uses the known Anna Tichá family key: `work/key.json` = `ciphers/hcp-1520/work/key.json` plus shallow-v → F. Round 2 adds the family's k-shaped **G** sign, label `G`, as established on HCP1541, 1553 and 1570. The current key file is `work/key-v2.json` and has 24 classes.

| Cipher labels | Plaintext |
|---|---|
| `1 2 3 4 5 6 8` | `y u o i e a l` |
| `q g f h t r c s` | `z k v r d h s c` |
| `n m p b d y H v G` | `m n b p t j ch f g` |

The key was transferred from earlier family cards and from Maxim Egorov's published partial study (https://maxim-egorov.dev/research/anna-ticha-postcards/). It was not discovered on this card. No plaintext of this card was published or consulted.

## Reproduction (single command)

From the repository root:

```sh
python3 -I ciphers/hcp-1554/work/decode2.py
```

The script uses only the standard library. It checks the source hashes and checks that `key-v2.json` is `key.json` plus G. It then decodes `work/transcription-v2.tsv` and checks the result against `work/literal-v2.txt`.

It prints the literal below, plus the counts:

- 21 rows;
- 570 read cipher units, 3 of them marked uncertain;
- 575 letters;
- 5 CH units and 1 G unit;
- 2 signs presumed abandoned by the writer;
- 23 of the 24 classes used (only `v`/F unused).

The older `work/decode.py` still audits the pre-review transcription and is superseded.

Notation:

- `{x}` marks a sign whose class is uncertain.
- `⟨…⟩` marks signs that were read but are presumed abandoned and inked over by the writer.
- `[9:40]` is ordinary numerals.

## Literal reading (output of the command)

```text
M01: vrely dik, anunko moje jedina, za drahou vzpo-
M02: minku z hradce. tazes se, kda se tesim na
M03: schuzku? - tesim se nevyslovne! vzdit opet
M04: budu po tak dlouhem case k sobe privinouti
I04: moci
M05: roztomilou divenku, jez stala se mi tak drahou!
M06: navrhuji, drahousku, abychom si oba navzajem
M07: zaslali jeste v pondeli listky, tak aby-
M08: chom je kazdy z nas v utery obdrzeli a
M09: pripadne snad nove okolnosti nasi schuzky
M10: se t{i}kajici si sdelili, ano anunko?!
M11: kdo by snad z nas proti nadani ujednanym
I12: ve stredu
M12: vlakem prijesti nemohl, zasle telegram
M13: restante do vesel{y}. sjedeme se za
M14: kazdeho pocasi. prijedu rychlikem v [9:40]
M15: rano a srdecko ⟨mo⟩mn{e} bude jiz ocekavati
M16: vid?!
L01: tisic pus zasila a na stredu se
L02: nesmirne tesi stale vzpominajici
L03: a vecne tvuj pepous
```

- I04 (*moci*) is written above the end of M04.
- I12 (*ve středu*) is written above the start of M12.
- L01–L03 run up the left margin.
- The date `22/V.1903` and the address (Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.) are plain writing.

## Editorial Czech

The accents and punctuation are editorial. The insertions are placed where the writer marked them. Four words keep the writer's forms, normalised as follows:

- *kda* = kdy;
- *vzdit* = vždyť;
- *t?kajici* = týkající;
- *prijesti* = přijeti.

> Vřelý dík, Anunko moje jediná, za drahou vzpomínku z Hradce. Tážeš se, kdy se těším na schůzku? – Těším se nevýslovně! Vždyť opět budu moci po tak dlouhém čase k sobě přivinouti roztomilou dívenku, jež stala se mi tak drahou! Navrhuji, drahoušku, abychom si oba navzájem zaslali ještě v pondělí lístky, tak abychom je každý z nás v úterý obdrželi a případně snad nové okolnosti naší schůzky se týkající si sdělili, ano, Anunko?! Kdo by snad z nás proti nadání ujednaným ve středu vlakem přijeti nemohl, zašle telegram restante do Veselí. Sjedeme se za každého počasí. Přijedu rychlíkem v 9:40 ráno a srdéčko [mne?] bude již očekávati, viď?! Tisíc pus zasílá a na středu se nesmírně těší stále vzpomínající a věčně tvůj Pepouš.

**English.** Warm thanks, my one and only Anunka, for the dear souvenir from Hradec. You ask when I look forward to our meeting? – I look forward to it unspeakably! For after such a long time I shall again be able to hold close the charming girl who has become so dear to me! I suggest, darling, that we both still send each other cards on Monday, so that each of us receives them on Tuesday, and that we tell each other any new circumstances concerning our meeting, yes, Anunka?! Should either of us unexpectedly be unable to come by the train agreed for Wednesday, he will send a telegram poste restante to Veselí. We shall meet whatever the weather. I shall arrive by the express at 9:40 in the morning and my sweetheart will already be waiting for [me?], won't she?! Sending a thousand kisses and looking forward immensely to Wednesday, ever remembering and eternally your Pepouš.

**Slovensky.** Vrúcna vďaka, Anunka moja jediná, za drahú pamiatku z Hradca. Pýtaš sa, kedy sa teším na stretnutie? – Teším sa nevýslovne! Veď opäť budem môcť po takom dlhom čase privinúť k sebe roztomilé dievčatko, ktoré sa mi stalo takým drahým! Navrhujem, drahúšik, aby sme si obaja navzájom poslali ešte v pondelok lístky tak, aby sme ich každý z nás v utorok dostali, a prípadné nové okolnosti týkajúce sa nášho stretnutia si oznámili, áno, Anunka?! Kto by z nás azda proti očakávaniu nemohol prísť dohodnutým vlakom v stredu, pošle telegram poste restante do Veselí. Stretneme sa za každého počasia. Prídem rýchlikom o 9:40 ráno a srdiečko [ma?] už bude očakávať, však?! Tisíc bozkov posiela a na stredu sa nesmierne teší stále spomínajúci a večne tvoj Pepouš.

## Uncertainties

- **U6, M15 *[mne?]* (weakest point).** The overinked group reads:
  1. a heavy `n`;
  2. a `3` with a loop above it;
  3. a lighter `n`;
  4. an `m`;
  5. a heavy final sign, read as `5`/E, though `6`/A is possible.

  Read straight, that gives *momn-e/a*, which is not a word. The reading *mne* assumes the writer abandoned *mo-* and inked it over. Alternatives:
  - *mna*: not a word;
  - the abandoned start of *moje* or a pet name.

  Crops: `work/r1/u6-context-x5.png`; reviewer `review/work/u6x10.png`.
- **U4, M12 *tele{G}ram*.** There is exactly one sign between `d585` and `h6n`. It is the family's k-shaped G, written over an earlier stroke whose form cannot be recovered. TELEGRAM is certain from context. Crops: `work/r1/u4-context-x6.png`; reviewer `review/work/u4x7.png`.
- **TIKAJICI, M10.** The second sign is an ink blob over a 4-like stem. It may be a correction to `1`/Y, which would give *týkající*. It is marked `{4}`.
- **VESELI, M13.** The final sign is a stem with a flag and a flat foot, without the crossbar that `4`/I has in ZASLALI and PONDELI. It is closer to `1`/Y, as in VRELY. It is now transcribed `{1}`, giving the literal *vesel{y}*. The place is Veselí (nad Lužnicí), and the I/Y slip does not affect the reading. Panel: `work/r1/y-vs-i-panel.png`; reviewer `review/work/veseli3.png`.
- **Writer's forms kept literally:**
  - KDA (M02), a clear `6`/A;
  - VZDIT (M03);
  - PRIJESTI (M12), with a visible `c` before `d4`.
- **Insertions.** The placement of I04 and I12 is editorial. The connecting strokes are not read as cancellations.
- **Resolution.** The scan is 1024 px wide, so the glyphs are only 10–20 px high.
- **Sender.** "Pepouš" (a pet form of Josef) is not identified. Hradec is presumably Jindřichův Hradec; Veselí is a railway junction near Žirovnice.

## Response to review 1

Claude Opus 5.5 (as solver), 2026-10-29. The review's verdict was REVISE. Every finding is addressed below. The decoded letters change in only two places: one sign in M02 (k → z) and one in M13 (i → y, marked uncertain). U4 and U6 are now produced by the command rather than only proposed. The reading is not substantially changed.

1. **[major] M02 `g` → `q` (z Hradce). Fixed.**
   - I compared the standalone sign with the card's controls in `review/work/m02-standalone.png` and `gq-panel.png`. It is a compact "9" with a short open leftward hook and no returning loop. That matches ZA (M01, M07), JEZ, U2 and U3. It does not match KDO or KAZDY.
   - `transcription-v2.tsv` M02 now reads `n4mg2 q rh6ts5`, so the literal is `z hradce`.
   - Counts: q +1, g −1. The literal, editorial, English and Slovak texts are all updated.
2. **[major] U4/U6 not reproducible; SOLUTION.md contradictory. Fixed.**
   - The key now has the k-shaped G (`work/key-v2.json` = `key.json` + `G`), citing HCP1541, 1553 and 1570.
   - U4 is transcribed `G`.
   - U6 is transcribed `⟨n3⟩nm{5}`, with the abandoned signs and the uncertain final sign marked.
   - The new single command, `python3 -I ciphers/hcp-1554/work/decode2.py`, prints `telegram` and `⟨mo⟩mn{e}`. I re-ran it, and the output is as listed above.
   - The counts are restated: 570 units, 575 letters, 5 CH, 1 G, 23/24 classes.
   - SOLUTION.md now opens with one current position. The earlier texts are kept below under "History (superseded)".
3. **[minor] U4 overwritten. Disclosed.** See Uncertainties: the earlier stroke under the G cannot be recovered.
4. **[minor] U6 is a guess. Done.**
   - The text is bracketed `[mne?]` in the editorial, English and Slovak texts.
   - The literal keeps `⟨mo⟩` and `{e}`.
   - The alternatives are listed under Uncertainties.
5. **[minor] TIKAJICI overinking. Disclosed and marked.** The sign is transcribed `{4}`, with the possible correction to `1`/Y noted.
6. **[minor] Stale administrative text, and the VESELI final sign. Fixed.**
   - The statements "human override: never watchers/reviewers", "no marker" and "partial" are superseded, as recorded here and in SOURCES.md, where a status note was appended.
   - The register count is 357 as of 2026-10-29, with HCP1554 / pc_hcp_235 absent. SOURCES.md's 337 was the count on 2026-10-28.
   - VESELI: I built a 1/4 panel (`work/r1/y-vs-i-panel.png`, with `work/r1/m07.png` and `work/r1/m13-start.png`). The final sign lacks the crossbar of 4/I in ZASLALI and PONDELI and is closer to the 1/Y of VRELY and LISTKY. It is now transcribed `{1}` (literal *vesel{y}*), and the editorial reading remains Veselí.

## History (superseded)

_Earlier texts, kept unchanged except that their headings are demoted. They do not state the current solution._

### HCP1554 / pc_hcp_235 — partial known-key transfer

This is a manually transcribed, substantially readable Czech postcard with two unresolved overink spans. It is **not a complete glyph-verified solution**. The portal's captured status is `Not solved`. No watcher, reviewer, marker, report, register entry or submission is part of this handoff.

The sources and both original faces were inspected. The image bears the ordinary date `22/V.1903`; the address reads `Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.` Neither the date nor address is cipher text. The signature's decoded `pepous` is reported as writing, not an identification of a historical sender. Postal marks and printed postcard decoration are not cipher text.

### Method and attribution

This is monoalphabetic substitution, with a distinct cipher unit for Czech `ch`. The generic family key in `ciphers/hcp-1520/work/key.json`, the public partial Anna Tichá study preserved in `batches/easy-2026-10-28/published-anna-ticha-key.txt`, and the pc199 photographic reference were known before target transcription. See `SOURCES.md`. The study is AI-associated partial research, not expert ground truth. This is key transfer, not independent key discovery or blind review. No target-specific plaintext was supplied or consulted.

Manual shape labels are convenient identifiers; they are not claims that each handwritten sign is a literal Latin letter or numeral. `H` denotes the special capped/marked h-family unit mapping to `ch`; the ordinary labels `h` and `r` must not be interchanged. The shallow-v label `v` maps to `f`; tall-looped `f` maps to `v`. The rare shallow-v class is in the fixed key but has **no confidently transcribed occurrence here**. Nothing is assigned a new `g` plaintext value to repair the word resembling a telegram.

| Cipher labels | Plaintext units |
|---|---|
| `1 2 3 4 5 6 8` | `y u o i e a l` |
| `q g f h t r c s` | `z k v r d h s c` |
| `n m p b d y H v` | `m n b p t j ch f` |

The main text has 16 baseline rows, two interlinear insertions and three marginal rows. The latter are read after rotating the left strip by 270° counterclockwise. Every cipher row has a saved crop, orientation, source/rotated bounding box, token column positions and globally indexed known glyphs in `work/inventory.json`. Text columns are offsets in the saved transcription, not individual photographic glyph boxes. `work/uncertainties.json` gives separate approximate image boxes for uncertain spans. Small accent-like marks are not generally stripped and decoded as modern accents: the literal reading retains the base classes and the five accepted CH units; Czech accents below are editorial.

The marginal row locators were corrected after root visual QA found that the earlier L02 rectangle also contained L03 and the earlier L03 crop missed its writing. Current boxes, in the 492×135 rotated strip, are L01 `[15,6,458,44]`, L02 `[10,34,474,80]`, L03 `[10,55,322,95]`. Slanted writing makes rectangular L02 and L03 envelopes overlap. Their `L01.png`/`L02.png`/`L03.png` locator crops therefore use documented polygon masks: original pixels inside the polygon, white outside, nearest-neighbor 3x. Separate `L01-context-rawNN.png` etc. preserve each complete raw rectangle. `marginal-row-ownership-rawNN.png` displays both, and `marginal-locators.json` stores exact bounds/polygons. These masks locate the intended rows; they do not prove separation of touching ink, especially near rotated x288–305/y65–77. The transcription is unchanged by this framing correction.

### Exact literal reading

This is the output of the fixed key, with original row division. The insertion rows remain separate: `I04` is above the end of `case` in M04 and is tentatively placed after that word in the reading text; `I12` lies above the start of M12 and is tentatively placed before `vlakem`. The baseline words `case` and `vlakem` are retained. Connecting strokes, underlining and ink overlap do not by themselves establish cancellation.

```text
M01: vrely dik, anunko moje jedina, za drahou vzpo-
M02: minku k hradce. tazes se, kda se tesim na
M03: schuzku? - tesim se nevyslovne! vzdit opet
M04: budu po tak dlouhem case k sobe privinouti
I04: moci
M05: roztomilou divenku, jez stala se mi tak drahou!
M06: navrhuji, drahousku, abychom si oba navzajem
M07: zaslali jeste v pondeli listky, tak aby-
M08: chom je kazdy z nas v utery obdrzeli a
M09: pripadne snad nove okolnosti nasi schuzky
M10: se tikajici si sdelili, ano anunko?!
M11: kdo by snad z nas proti nadani ujednanym
I12: ve stredu
M12: vlakem prijesti nemohl, zasle tele⟦U4⟧ram
M13: restante do veseli. sjedeme se za
M14: kazdeho pocasi. prijedu rychlikem v [9:40]
M15: rano a srdecko ⟦U6⟧ bude jiz ocekavati
M16: vid?!
L01: tisic pus zasila a na stredu se
L02: nesmirne tesi stale vzpominajici
L03: a vecne tvuj pepous
```

`[9:40]` transcribes ordinary numerals (written as 9 with raised 40), not five cipher units. The date and address are ordinary writing outside the cipher inventory.

### Uncertainties and limitations

| ID | Literal position | What the image currently supports |
|---|---|---|
| U4 | M12 `tele⟦U4⟧ram` | Ink overlap after `d585`, before `h6n`. Glyph sequence and unit count are unknown. `telegram` is a linguistic expectation, not decoded evidence or a new G assignment. |
| U6 | M15 `srdecko ⟦U6⟧ bude` | Overinked word. Some humps and an o-like form are visible, but the base sequence and unit count remain unasserted. No name or pet name is inferred. |

The four formerly bounded single-glyph positions were resolved by same-card shape comparisons, without changing the fixed key. The raw nearest-neighbor panels `work/control-gq-rawNN.png` and `work/control-s4-rawNN.png` contain enlarged original pixels and full source-row context, with explicit source boxes in `work/control-panels.json`. `work/resolved-controls.json` preserves the prior alternatives and current decisions:

- U1 → `s`/C: a compact triangular body without the horizontal baseline crossbar seen in `4`/I. It matches `s` in CASE and I04 MOCI; MINKU and LISTKY provide contrasting `4` shapes. The resulting literal word is `hradce`, not editorial `Hradci`.
- U2 and U3 → `q`/Z: compact oval heads and one open, leftward terminal hook match `q` in ZA (M01/M07) and JEZ (M05). They lack the long returning descender loop and entry shoulder of `g` in KDO/KAZDY.
- U5 → `g`/K: its entry/shoulder and long narrow returning descender loop match KDO/KAZDY, rather than the one open hook of the q controls.

There are **566 known cipher units**, producing **571 known plaintext letters**, including **five CH units**. Twenty-two of the fixed key's 23 classes are used. Two overinked spans have unknown unit counts. Consequently the total number of original cipher units and a complete percentage coverage are **unknown**. Unknown spans are not silently counted as one symbol.

Base-letter anomalies are retained: M02 `kda`; M03 `vzdit`; M10 `tikajici`; M12 `prijesti`. Their plausible Czech normalization does not prove that the source glyph assignment is correct. The targeted g/q and M02 angular comparisons are now recorded, while ordinary b/8 distinctions, CH cap ownership, insertion attachment and overink sites still merit root photographic controls. Hash and inverse checks below cannot supply that visual evidence.

### Editorial Czech reading — accents and repairs separate from the literal

The following adds capitalization, modern diacritics and punctuation. Square brackets preserve uncertainty or identify an editorial repair. Insertion placement is provisional; the two insertion texts are not new deciphered material beyond the literal rows above.

> Vřelý dík, Anunko moje jediná, za drahou vzpomínku k hradce. Tážeš se, [kdy; doslova `kda`] se těším na schůzku? — Těším se nevýslovně! [Vždyť; doslova `vzdit`] opět budu po tak dlouhém čase [moci, I04] k sobě přivinouti roztomilou dívenku, jež stala se mi tak drahou! Navrhuji, drahoušku, abychom si oba navzájem zaslali ještě v pondělí lístky, tak abychom je každý z nás v úterý obdrželi a případně snad nové okolnosti naší schůzky se [týkající; doslova `tikajici`] si sdělili, ano Anunko?! Kdo by snad z nás proti nadání ujednaným [ve středu, I12] vlakem [přijeti; doslova `prijesti`] nemohl, zašle tele[nečitelné]ram restante do Veselí. Sjedeme se za každého počasí. Přijedu rychlíkem v 9:40 ráno a srdéčko [nečitelné U6] bude již očekávati, viď?! Tisíc pus zasílá a na středu se nesmírně těší stále vzpomínající a věčně tvůj Pepouš.

### Slovak translation of the editorial reading

> Vrúcna vďaka, Anunka moja jediná, za drahú spomienku k hradce [doslovné znenie]. Pýtaš sa, [kedy; oprava] sa teším na stretnutie? — Teším sa nevýslovne! Veď opäť budem môcť po takom dlhom čase k sebe privinúť roztomilé dievča, ktoré sa mi stalo takým drahým! Navrhujem, drahúšik, aby sme si obaja navzájom poslali ešte v pondelok lístky, aby sme ich každý z nás v utorok dostali a prípadne si oznámili nové okolnosti týkajúce sa nášho stretnutia, áno Anunka?! Kto by azda z nás proti očakávaniu nemohol prísť dohodnutým [v stredu, vložka] vlakom, pošle tele[nečitateľné]ram restante do Veselí. Zídeme sa za každého počasia. Prídem rýchlikom o 9:40 ráno a srdiečko [nečitateľné U6] už bude očakávať, však?! Tisíc bozkov posiela a na stredu sa nesmierne teší stále spomínajúci a večne tvoj Pepouš.

### Reproduction and audit

Run this single read-only command from the repository root:

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1554/work/decode.py
```

It checks the three immutable original hashes against the **three target entries** in the shared batch guard, four reference hashes, 41 saved-record hashes, all row crops (including marginal polygon masks and separate raw contexts), raw nearest-neighbor glyph/row panel pixels, transcription-to-index positions and the saved literal. It then decodes the complete manual transcription with the fixed key and re-encodes the whole resulting plaintext using the complete inverse key, greedily treating CH as one unit. Unknown tokens and the ordinary time are opaque and are neither guessed nor counted as known glyphs. The inverse operation is not a per-token lookup of saved source glyphs.

Expected audit: 3 original / 4 reference / 41 record hashes OK; 21 rows; 566 known units; 571 known letters; 5 CH units; 22/23 used classes; saved literal and whole-key inverse OK. A successful audit establishes reproducibility and internal consistency of this **manual transcription**, not that the chosen glyph classes match every source stroke. This candidate still needs photographic controls at the stated sites. No independent provider review or historical identity verification is claimed.


### Root solver photographic checks

Root inspected both complete originals, all21 physical text segments and the focused same-card nearest-neighbor controls. The four resolved classes are supported by visible comparisons: angular s/C versus crossbar4/I; q/Z with open terminal hook versus g/K with returning loop. Baseline CASE and VLAKEM remain, with I04/I12 insertions separately recorded; their editorial attachment remains provisional. Ordinary raised40 after9 is recorded as9:40, outside the cipher inventory. U4 and U6 retain unknown length; no G assignment or canceled-text interpretation was invented.

The root row-by-row pass found an artifact locator error: the earlier L02 crop contained two sloping rows and L03 was placed below the actual line. The collaborator corrected all three marginal boxes and supplied both raw rectangular context and explicitly masked locator views. Root checked the final marginal ownership panel: L01 TISIC…; L02 NESMIRNE…; L03 A VECNE TVUJ PEPOUS. Approximate polygon masks near touching ink are presentation aids, not source restoration or independent proof of ownership. The transcript and566known-unit count were unchanged by this locator correction.

The final read-only command verifies the corrected crops, masks, raw contexts,41record hashes and the actual whole-key inverse. This is solver collaboration, not separate-provider review. The candidate remains PARTIAL, with no DONE marker.

### Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading with one weaker word, handed to review (DONE1).**

1. **U4, M12 `tele⟦U4⟧ram` (work/tele.png).** Between `d585` (TELE) and
   `h6n` (RAM) there is room for exactly **one** sign. That sign is heavily
   overwritten: a tall looped form written over an earlier stroke. The phrase
   “zašle tele?ram restante do Veselí” leaves only **TELEGRAM**, so the sign
   stands for G. The family key has no G sign. The same holds on HCP1570
   (KOLE?I = kolegy), where a single unmapped sign also stands where only G fits.
2. **U6, M15 `srdecko ⟦U6⟧ bude` (work/M15.png).** The last three signs of the
   overinked group can be read as `n m 5` (M N E): the hump of n, the double
   hump of m, and a heavily inked final 5/E. The two signs before them, `n3`,
   are blackened, which looks like a start the writer abandoned and inked
   over. Proposed reading: “a srdéčko **mne** bude již očekávati” (“and my
   sweetheart will already be waiting for me”). This is the **weakest point**
   of the card: the cancelled pair and the 5/6 ambiguity of the last sign
   are left for the reviewer.

Editorial Czech (accents editorial; KDA, VZDIT, TIKAJICI, PRIJESTI kept as
written, = kdy, vždyť, týkající, přijeti): “Vřelý dík, Anunko moje jediná,
za drahou vzpomínku z Hradce. Tážeš se, kdy se těším na schůzku? – Těším se
nevýslovně! Vždyť opět budu moci po tak dlouhém čase k sobě přivinouti
roztomilou dívenku, jež stala se mi tak drahou! Navrhuji, drahoušku,
abychom si oba navzájem zaslali ještě v pondělí lístky, tak abychom je
každý z nás v úterý obdrželi a případné snad nové okolnosti naší schůzky se
týkající si sdělili, ano, Anunko?! Kdo by snad z nás proti nadání ve středu
ujednaným vlakem přijeti nemohl, zašle telegram restante do Veselí.
Sjedeme se za každého počasí. Přijedu rychlíkem v 9:40 ráno a srdéčko
[mne] bude již očekávati, viď?! Tisíc pus zasílá a na středu se nesmírně
těší stále vzpomínající a věčně tvůj Pepouš.”

Reproduce with the command given earlier in this file. The family key is
credited to earlier family cards and the published partial study by Maxim Egorov.
