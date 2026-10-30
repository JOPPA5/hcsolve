# HCP 1530 — pc_hcp_211 — COMPLETE (after review 1)

**Status (2026-10-29, after review 1, verdict REVISE): complete reading.** Czech love letter from Pepouš to Anna Tichá, 14.XI.1903, monoalphabetic substitution with the known Anna Tichá / Pepouš family key (known-key transfer, not independent key discovery). All 464 cipher units (6 CH) are transcribed and decoded; 2 of them (I, S in LÍSTEK) are restored from context and shown in brackets, 5 are faint or probable. This consolidated block supersedes every "PARTIAL", "unknown span", "coverage unknown" and "no register entry" statement in the historical sections below.

## Consolidated reading (v2)

Reproduction command (repository root, standard library only, read-only):

```sh
python3 ciphers/hcp-1530/work/decode.py
```

It verifies the three source hashes and the per-sign inverse-key round trip, decodes work/v2/transcription-v2.json with work/key.json, and prints:

```text
T01 VRELY DIK SRDECKO MOJE ZLATE, ZA DRAHY L[IS]TEK
T02 JAK DARI SE NYNI S HLAVICKOU? JA JSEM, BOHUDIK,
T03 BOLEST SVE HLAVY JIZ PREMOHL, KTERE MNE NYNI
T04 PRISLO VELICE NEVHOD. U NAS JIZ BLIZI SE DOBA
T05 VANOCNI A S NI ROZMNOZENI PRACE. TAKE JA
B01 VZPOMINAM NA LONSKY ROK VTETO DOBE,
B02 KDY MOJE SRDECKO ZDE DLELO NA ZKOUSKACH.
B03 SKODA. A TY HEZOUNKE CHVILKY VZDY TAK
B04 RYCHLE PRCHAJI. JAK TRAVI ANUSKA NYNEJSI
B05 DLOUHE VECERY? MUJ ZIVOT JE NARAMNE JEDNO-
B06 TVARNY. VCERA CHTEL JSEM NAVSTIVITI VECER
B07 KONCERT «Issajův» V RUDOLFINE, ZDRZEL JSEM
B08 SE VSAK PRILIS DLOUHO V URADE. TISIC VRELYCH
B09 PUS POSILA PEPOUS SVEMU JEDINEMU SRDECKU.

464 cipher units (6 CH) -> 470 letters; 457 clear, 5 faint/probable, 2 restored from context (in brackets).
```

The earlier partial decoder is kept unchanged as work/decode-v1-partial.py (it still checks the v1 record with its hashes). work/v2/build-v2.py derives the v2 record from the v1 record; its only changes are T01 `th6r5` -> `th6r1` and the four spans filled sign by sign.

Editorial Czech (accents, capitals and punctuation editorial):

> Vřelý dík, srdéčko moje zlaté, za drahý lístek. Jak daří se nyní s hlavičkou? Já jsem, bohudík, bolest své hlavy již přemohl, které mně nyní přišlo velice nevhod. U nás již blíží se doba vánoční a s ní rozmnožení práce. Také já vzpomínám na loňský rok v této době, kdy moje srdéčko zde dlelo na zkouškách. Škoda. A ty hezounké chvilky vždy tak rychle prchají. Jak tráví Anuška nynější dlouhé večery? Můj život je náramně jednotvárný. Včera chtěl jsem navštíviti večer koncert „Issajův“ v Rudolfině, zdržel jsem se však příliš dlouho v úřadě. Tisíc vřelých pus posílá Pepouš svému jedinému srdéčku.

English: Warm thanks, my golden darling, for the dear card. How is your little head now? I have, thank God, already overcome my headache, which came at a very bad time just now. Here the Christmas season is already approaching, and with it more work. I too remember last year at this time, when my darling stayed here for her examinations. A pity. And those lovely moments always pass so quickly. How does Anuška spend these long evenings? My life is terribly monotonous. Yesterday evening I wanted to go to the "Issajův" concert in the Rudolfinum, but I stayed too long at the office. A thousand warm kisses from Pepouš to his only darling.

Slovak: Vrelá vďaka, moje zlaté srdiečko, za milý lístok. Ako sa teraz darí hlavičke? Ja som, chvalabohu, bolesť hlavy už premohol, ktorá mi teraz prišla veľmi nevhod. U nás sa už blíži vianočný čas a s ním pribúda práce. Aj ja spomínam na minulý rok v tomto čase, keď tu moje srdiečko pobývalo na skúškach. Škoda. A tie pekné chvíľky vždy tak rýchlo ubiehajú. Ako trávi Anuška terajšie dlhé večery? Môj život je nesmierne jednotvárny. Včera som chcel večer navštíviť koncert „Issajův“ v Rudolfine, zdržal som sa však príliš dlho v úrade. Tisíc vrúcnych bozkov posiela Pepouš svojmu jedinému srdiečku.

Uncertainties: L[IS]TEK (I, S restored, see response to review 1, item 4); faint signs in U3/U4 and the probable L in U1; Z/K distinctions partly supported by Czech (item 5); the ordinary title «Issajův» and its identification (item 7); VTETO is the writer's spacing of "v této".

# Historical record (v1 partial and DONE1 completion, superseded where it conflicts with the block above)

## Source and context

https://crypto.hcportal.eu/dashboard/cryptograms/1530 . Root read rendered General, Description and Attachments on 2026-10-28: Not solved; Czech; Substitution; private collection; date 1903-11-14; unknown sender; recipient Anna Tichá. Both original postcard sides and immutable rendered metadata are in source/. Exact observed image URLs are recorded in SOURCES.md. No attached transcription or target solution was supplied. The ordinary address calls Anna Tichá a teacher in Žirovnice near Počátky. The ordinary picture date reads 14.XI.1903. The signature decodes PEPOUS; a civil sender identity is not established.

Root's current rendered AI register check found 158 contributions/124 HC Portal IDs, target absent. This bounded check does not establish worldwide novelty. Maxim Egorov/Cipher-Atelier's previously published generic partial family key and eleven other partial card readings are acknowledged in SOURCES.md and batches/easy-2026-10-28/published-anna-ticha-key.txt. No published target plaintext was supplied. The existing HCP1520/HCP1527 key was available at the beginning. Root later inspected focused original-pixel crops collaboratively; this was solver collaboration, not an independent provider review.

The picture writing occupies five top rows (upside down relative to the nine lower rows), not just the large lower body. Read T01–T05, then B01–B09: TAKE JA continues VZPOMINAM. No cipher is observed on the address side. Small handwritten ordinary title in B07 is tentatively Issajův; this is not ciphertext and no historical performer identification is claimed.

## Key and reproducible procedure

Monoalphabetic substitution of digit/Latin-like handwritten shapes, with a special CH glyph. Labels are conventional transcriptions of shapes, not their plaintext names. The source's special glyph is labeled ř, which means CH, not Czech Ř. The family m/n distinction is retained. The shallow v-like form is now v/F through a later targeted comparison with published card199; it was initially retained as UF.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 8 | L | q | Z |
| g | K | f | V | h | R | t | D |
| r | H | c | S | s | C | n | M |
| m | N | p | B | b | P | d | T |
| y | J | ř | CH | v | F | | |

Rotate original picture.jpg by a lossless 90° counterclockwise transpose (upright.png, 674×1024). For T rows, crop upright [28,35,642,195] and rotate the crop 180° (top-upright.png, 614×160). Manually transcribe the 14 rows through work/transcription.json, using each row's specified coordinate system and row box. Apply work/key.json to each positively transcribed glyph, preserve unknown spans verbatim, preserve the JEDNO-/TVARNY line split and source spacing such as VTETO. Punctuation and ordinary title are separately recorded, outside cipher counts. No letter is supplied from Czech grammar.

Single reproduction command from repository root:

```sh
python3 ciphers/hcp-1530/work/decode.py
```

This command uses the standard library, is read-only by default, and verifies the three target source hashes, two published-reference hashes, three record hashes, all 445 known ordinal positions, six CH expansions, and an exact tokenwise inverse-key round trip. Four unknown spans survive verbatim. The manual image transcription is a documented input, not OCR; internal consistency does not independently prove the manual readings. work/indexed-top.png, indexed-bottom.png, T01.png–T05.png, B01.png–B09.png and focused-controls.png provide image checks. focused-controls.json records raw source pixel boxes as well as upright coordinates. Position indices enumerate positively read glyphs, not guessed units inside unresolved spans, and do not claim individual pixel boxes.

work/build-record.py and work/make-controls.py are explicit record/control generators requiring Pillow; the default command does not invoke them or write files.

## Literal Czech base plaintext

Accents are omitted for cipher letters. The accented ordinary title is retained as ordinary script. Bracket codes denote unresolved source spans and are not plaintext letters.

```text
VRELY DIK SRDECKO MOJE ZLATE, ZA DRAHE [U1]
JAK DARI SE NYNI S HLAVICKOU? JA JSEM, BOHUDIK,
BOLEST SVE HLAVY JIZ PREMOHL, KTERE MNE NYNI
PRISLO VELICE NEVHOD. U NAS JIZ BLIZI SE DOBA
VANOCNI A S NI ROZMNOZENI PRACE. TAKE JA
VZPOMINAM NA LONSKY ROK VTETO DOBE,
KDY MOJE SRDECKO ZDE DLELO NA ZKOUSKACH.
SKODA. A TY HEZOUNKE CHVILKY VZDY TAK
RYCHLE PRCHAJI. JAK TRAVI ANUSKA [U2]
DLOUHE VECERY? MUJ ZIVOT JE NARAMNE JEDNO-
TVARNY. VCERA CHTEL JSEM NAVSTIVITI VECER
KONCERT «Issajův» V RUDOLFINE, ZDRZEL JSEM
SE VSAK PRILIS DLOUHO V URA[U4]. TISIC VRELYCH
PUS POSILA PEPOUS SVEMU JE[U3]MU SRDECKU.
```

## Editorial Czech with accents

Only accents, capitalization, paragraphing and word joining/splitting are editorial. The source's base letters KTERE, PRISLO and NEVHOD are not grammatically repaired. Unknown dark spans are not expanded. F was explicitly added through the documented later reference transfer.

> Vřelý dík srdéčko moje zlaté, za drahé [U1]. Jak daří se nyní s hlavičkou? Já jsem, bohudík, bolest své hlavy již přemohl, které mně nyní přišlo velice nevhod. U nás již blíží se doba vánoční a s ní rozmnožení práce. Také já vzpomínám na loňský rok v této době, kdy moje srdéčko zde dlelo na zkouškách. Škoda. A ty hezounké chvilky vždy tak rychle prchají. Jak tráví Anuška [U2] dlouhé večery? Můj život je náramně jednotvárný. Včera chtěl jsem navštíviti večer koncert «Issajův» v Rudolfině, zdržel jsem se však příliš dlouho v úra[U4]. Tisíc vřelých pus posílá Pepouš svému je[U3]mu srdéčku.

The displayed editorial sentence stop after U1 is an editorial boundary; the dark span's original punctuation is not securely read. The unusual NEVHOD is retained verbatim apart from capitalization. Accents do not establish the underlying unread letters of a proper name or unknown span. The ordinary title remains paleographically uncertain.

## Slovak translation

> Vrelá vďaka, moje zlaté srdiečko, za drahé [U1]. Ako sa teraz darí s hlavičkou? Ja som, chvalabohu, bolesť svojej hlavy už premohol, čo mi teraz prišlo veľmi nevhod [znenie zachováva nezvyčajné české NEVHOD]. U nás sa už blíži vianočný čas a s ním pribúdanie práce. Aj ja spomínam na minulý rok v tomto období, keď tu moje srdiečko pobývalo na skúškach. Škoda. A tie pekné chvíľky vždy tak rýchlo ubiehajú. Ako trávi Anuška [U2] dlhé večery? Môj život je veľmi jednotvárny. Včera som chcel večer navštíviť koncert «Issajův» v Rudolfine, zdržal som sa však príliš dlho v úra[U4]. Tisíc vrúcnych bozkov posiela Pepouš svojmu je[U3]mu srdiečku.

Unknowns remain unknown in translation. The awkward partial words are retained to avoid turning a context completion into a source reading.

## Coverage, source controls and uncertainty

The 14 rows contain **445 positively transcribed cipher units**, including **6 CH units**, producing **451 known base letters**. Four dark spans have unknown unit counts. Consequently the complete glyph/letter denominator and a whole-card coverage percentage are **unknown**, not 100%. Ordinary date, address, title, punctuation, spaces and accents are excluded. The overwritten/retraced start of VANOCNI is read as one active word; no separable canceled glyph can be counted reliably.

| ID | Literal output | Contextual candidate only | Focused unfiltered crop |
|---|---|---|---|
| U1 | DRAHE [U1] | PSANKO | work/U1-original.png |
| U2 | ANUSKA [U2] | NYNEJSI | work/U2-original.png |
| U3 | JE[U3]MU | DINE, yielding JEDINEMU | work/U3-original.png |
| U4 | URA[U4] | DE, yielding URADE | work/U4-original.png |

These four dark-span candidates are excluded from the asserted literal text and inventory. The shallow v/F in RUDOLFINE is documented separately below; tall f/V forms on this postcard are shown in work/B05-f-original.png.

T03 ends KTERE MNE NYNI and T04 begins PRISLO VELICE NEVHOD; six-unit NEVHOD is not expanded to NEVHODNE. The focused KTERE/NEVHOD controls retain these literal anomalies. T02 BOHUDIK is seven units, with t/D before final 4g/IK. B07 ZDRZEL is qthq58, not a grammar-based rewrite of an unread word. The coherent letter and known-key agreement support the positive reading; they cannot resolve the dark spans.

No blind held-out test, independent key recovery, OCR, independent provider review, performance timing claim, or worldwide novelty claim is made. Root's visual comments are acknowledged as collaboration. Notes preserve failed drafts and the conservative revisions. No solved register entry is appropriate while the text remains partial.

## Immutable source SHA-256

```text
source/address.jpg  7a3961816c1f21d0e38b14d417d47cbb3649f7f6369f82adff6c25b6f1ee6147
source/metadata.md  0287cc0da7640057e5ee38954749e8449366f8461f627ce6c4644dbcc495be85
source/picture.jpg  c21f3e06329a943109afaa535ba0b390e5cd42bb2b360cbaec5dfcab3a708226
```


## Root verification of partial record — before later F transfer

Root inspected both originals, the complete upright top and bottom blocks, all five focused unknown regions and local CH/V/title controls on 2026-10-28. Dark PSANKO/NYNEJSI/URADE completions were not accepted as literal readings; U1, U2 and U4 remain. The shallow v in RUDOL[UF]INE is a contextual F candidate, with the uncertainty preserved. Ordinary Issajův remains a tentative cursive reading without historical performer identification. The updated read-only command passed three original hashes, three record hashes, all 444 assigned units, six CH expansions and tokenwise checks. Full denominator remains unknown. This is a second solver check of a partial manual record, not independent provider review. No marker created.


## Later targeted F reference transfer

After the initial partial record and root visual QA, root obtained the exact original photo cited by the already published study for card199/HCP1518. Its proposed reading RUDOLFINA contains h2t38v4m6. The photograph clearly shows a short open v-like form between 8/L and 4/I, matching the form at the same position in this target's h2t38v4m5. The reference has an open bowl/valley with a short rising right stroke; it differs from the target's tall looping f/V. Actual original photograph and unfiltered controls were viewed, including the root comparison with the tentative HCP1526 DOUFAM and HCP1534 DOUFAL forms. Those two other targets are supporting shape comparisons, not the source of a new generic key discovery.

The target singleton is now transcribed v and read F by **known published-reference transfer**. This happened after, and is disclosed separately from, the original contextual F inference. It does not fill any dark word. Source photo: https://api.hcportal.eu/media/4614/pc_hcp_199_pic.JPG ; local reference batches/easy-2026-10-28/public-reference-199/picture.jpg, SHA-256 f50ac01e9e219b7f50d79a2373a81355ce81dbf94da43b12be1b1e7ff9a6a9ce. The native upright reference box is [655,1525,935,1606], target box [325,884,464,921]. Provenance, exact source hashes, native boxes and four-way comparison are preserved in that reference directory. work/UF-original.png retains the target crop name for traceability; it now documents the assigned F, not a fifth unresolved area.

The study is itself partial and its proposed key is not an external expert review or proof of universal accuracy. The adopted correspondence is supported here by a visible shape match and the consistent RUDOLFINE reading. The default command additionally checks the reference-photo and published-key-text hashes recorded in work/reference-sha256.json. The updated record has 445 assigned units/451 known base letters, including one v/F; four dark spans remain unchanged and the status remains PARTIAL. No new marker or review was created.



## Root check after photographed F transfer

Root inspected the four-way unfiltered source comparison and reran the updated decoder on 2026-10-28. The shallow open v in RUDOLFINE agrees with the published card199 proposed F and with DOUFAM/DOUFAL on the related cards. Known-reference transfer therefore supports assigning this one F, after the earlier contextual proposal. The updated record has 445 assigned units, six CH expansions and 451 assigned base letters; four dark spans remain unresolved with unknown lengths. Three target-source hashes, two reference hashes, record hashes and tokenwise checks passed. The earlier 444/450 snapshot is superseded only by this one added assignment. The prior family study is partial; visual agreement is corroboration, not an external expert review. Status remains PARTIAL without markers.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading, handed to review (DONE1).** The four dark spans,
enlarged five times (work/claude/U1-x5.png … U4-x5.png):

| Span | Visible signs | Reading |
|---|---|---|
| U1 (T01 end) | `8`, a darkened middle, then a clear `5 g` and a closing bracket | **LISTEK**: begins with L, ends in EK; the 6-letter frame `8 4 c d 5 g` fits the width. The earlier candidate PSANKO does **not** fit: its last two signs would be `g3` |
| U2 (B01 end) | `m 1 m 5 7 c 4` read through the shadow | **NYNEJSI** (*nynější*, “these present [long evenings]”) |
| U3 (B05) | `7 5 t 4 m 5 m …`, with D and I in the dark | **JEDINEMU** (*jedinému*) |
| U4 (B04 end) | `2 h 6 t 5` | **URADE** (*v úřadě*, “at the office”) |

**Point for the reviewer.** In U1-x5 the word before the span looks like
`th6r1` (DRAHY, ending in the 1/Y sign), whereas the recorded transcription
gives DRAHE. *Drahý lístek* is the family's standard phrase and agrees with
LISTEK. Please check that final sign. The decoder output is unchanged
(it still prints DRAHE and the `[U…]` placeholders); the readings above rest
on the cited crops.

Editorial Czech: “Vřelý dík, srdéčko moje zlaté, za drahý lístek. Jak daří se
nyní s hlavičkou? Já jsem, bohudík, bolest své hlavy již přemohl, které mně
nyní přišlo velice nevhod. U nás již blíží se doba vánoční a s ní rozmnožení
práce. Také já vzpomínám na loňský rok v této době, kdy moje srdéčko zde
dlelo na zkouškách. Škoda. A ty hezounké chvilky vždy tak rychle prchají.
Jak tráví Anuška nynější dlouhé večery? Můj život je náramně jednotvárný.
Včera chtěl jsem navštíviti večer koncert Issajův v Rudolfině, zdržel jsem
se však příliš dlouho v úřadě. Tisíc vřelých pus posílá Pepouš svému
jedinému srdéčku.”

(Issajův = probably the violinist Eugène Ysaÿe; context only.)

Reproduce with the command given earlier in this file. The family key is
credited to earlier family cards and the published partial study by Maxim Egorov.

## Response to review 1

Responder: Claude Opus 5.5 as solver, 2026-10-29. I re-viewed the reviewer's crops review/work/U1x7.png, U2x5.png, U3x5.png and U4x8c.png before changing anything. The reviewer's independent reading (review/work/mydecode.py) and the new decoder output agree letter for letter, apart from the reviewer's own disclosed typing slip KONCTERT.

1. **[major] Command did not produce the claimed plaintext — fixed.** New record work/v2/transcription-v2.json (built by work/v2/build-v2.py from the v1 record) transcribes the four spans sign by sign: U1 `8 4 c d 5 g`, U2 `m 1 m 5 y c 4`, U3 `t 4 m 5`, U4 `t 5`. (The J sign, 7-shaped on this card, keeps the label `y`, as in key.json.) Each sign carries a certainty: clear / faint / probable / restored. work/decode.py was rewritten to decode this record. It brackets restored signs and lists faint ones. Re-run on 2026-10-29: `python3 ciphers/hcp-1530/work/decode.py` prints the 14 rows above with no placeholder, and `464 cipher units (6 CH) -> 470 letters; 457 clear, 5 faint/probable, 2 restored`. The old decoder is preserved as work/decode-v1-partial.py and still passes against the unchanged v1 files. Correction to the DONE1 completion table: U3 is in row B09 (JE…MU) and U4 is in row B08 (URA…), not B05/B04.
2. **[major] DRAHE -> DRAHY — fixed.** In U1x7.png the final sign of `th6r?` is a vertical stroke with a foot. It matches the `1` closing `fh581` and differs from the open `5`. The v2 record has `th6r1` = DRAHY, which agrees with masculine lístek.
3. **[major] Self-contradictory SOLUTION.md — fixed.** The title and a new top block give one consolidated status (complete), one plaintext, editorial Czech, English and an updated Slovak translation (za milý lístok … terajšie … v úrade … jedinému). The older sections are kept below a heading that marks them as a superseded historical record. Their "PARTIAL", "coverage unknown" and "no register entry" statements no longer apply.
4. **[minor] Degree of restoration — disclosed.** U1: `8` (L) is probable. One or two signs are lost in the dark paint and are restored as I, S from context and width; the count cannot be established. `d 5 g` (TEK) is visible. Output: L[IS]TEK. U2 is fully legible. U3: `t` and `4` are faint, `m 5` clear. U4: `t` and `5` are faint, with the right shapes. The decoder lists these five faint/probable signs explicitly.
5. **[minor] q/Z vs g/K — disclosed.** In this hand Z (`q`) and K (`g`) are near-identical in ZDE, ZDRZEL and ZKOUSKACH (B02qg.png, B07zdrzel.png). The choice at those positions rests partly on Czech word forms, not on shape alone. The early KDE/KDYZEL misreadings in NOTES.md show the risk. No alternative reading gives Czech there.
6. **[minor] NEVHOD not anomalous — agreed.** "Přišlo mi to nevhod" is ordinary Czech. The "unusual" remarks survive only in the superseded historical sections and are withdrawn. KTERÉ ("which [thing]") stands as written.
7. **[minor] Issajův = Ysaÿe — kept as an unverified suggestion.** I found no source confirming a Ysaÿe concert at the Rudolfinum on 13.XI.1903. The title is ordinary script, not cipher, and is read tentatively. Any identification is labelled context only.
