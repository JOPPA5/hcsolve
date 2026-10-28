# HCP 1537 / pc_hcp_218

Claim: complete manual transcription and decoding of the 13-row encrypted picture-side message (289 cipher shapes). This is a whole-message solver candidate awaiting independent provider review. No watcher, reviewer, state marker, PDF or register entry has been created by this collaborator.

## Source and attribution

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1537 . The root inspected all three rendered tabs on 2026-10-28: Not solved, Czech, private postcard collection, 1903-09-17, recipient Anna Tichá. There was no attached transcription or solution. Both original sides and all margins were inspected; originals are immutable. See SOURCES.md and work/source-sha256.json.

The Anna Tichá family key was known at the start from earlier cards and public partial work (https://maxim-egorov.dev/research/anna-ticha-postcards/). The public partial-key file and pc199/RUDOLFINA photographic comparison were already available, including the shallow-v/F correspondence. The work here is transferring that key, reading this target manually, and checking the result; it is not an independent discovery of the substitution key. No target plaintext was supplied.

## Cipher and key

Monoalphabetic shape substitution, without plaintext accents or encoded case. Digit/letter labels describe handwritten shapes and do not retain their ordinary values. All observed shapes use this table (H/CH is part of the transferred family key but is unused here):

| Shape | 1 | 2 | 3 | 4 | 5 | 6 | 8 | b | c | d | f | g | h | m | n | p | q | r | s | t | y | F | H |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Base plaintext | y | u | o | i | e | a | l | p | s | t | v | k | r | n | m | b | z | h | c | d | j | f | ch |

`F` specifically labels the shallow-v-shaped glyph, contrasting with looped f-shaped V; `y` labels the J shape. The one letter becoming F occurs in DEFINITIVNE. Key is work/key.json. Exact manual records and glyph indices are work/manual-records.json and work/indexed-transcription.tsv. work/transcription-index.md displays every row crop with its ordered cipher and glyph indices. Focused controls and corrected false starts are in work/controls.md.

## Literal Czech base letters

Line endings and written line hyphens preserved; no grammatical correction or inserted base letters:

```text
srdecny dik za drahy
listek. myslil jsem
jiz, ze jsi uplne
na mne zapomnela.
kdy zacinali jste
novy skolni rok?
v klastere zacinal rok asi
dnes. neprijde-li nic neoce-
kavaneho do toho, pojedu asi kon-
cem pristiho tydne na dovolenou.
ucinkovani pri vecirku ve vamberce jsem
jiz definitivne odrekl. tisic pus posila
ti tvuj pepous a tesi se opet na brzky listek.
```

## Editorial Czech

Accents, capitalization and joined line splits are editorial additions. The base letters, word order, MYSLIL, VAMBERCE and BRZKY remain unchanged:

> Srdečný dík za drahý lístek. Myslil jsem již, že jsi úplně na mne zapomněla. Kdy začínali jste nový školní rok? V klášteře začínal rok asi dnes. Nepřijde-li nic neočekávaného do toho, pojedu asi koncem příštího týdne na dovolenou. Účinkování při večírku ve Vamberce jsem již definitivně odřekl. Tisíc pus posílá ti tvůj Pepouš a těší se opět na brzký lístek.

## Slovak translation

> Srdečná vďaka za drahý lístok. Myslel som si už, že si na mňa úplne zabudla. Kedy ste začínali nový školský rok? V kláštore sa rok začínal asi dnes. Ak do toho nepríde nič neočakávané, pôjdem asi koncom budúceho týždňa na dovolenku. Účinkovanie na večierku vo Vamberce som už definitívne odmietol. Tisíc bozkov ti posiela tvoj Pepouš a opäť sa teší na skorý lístok.

## Unencrypted content and margins

Picture-side date: `17/IX1903.` (17 September 1903), matching portal metadata. There are no further encrypted rows outside the 13 recorded message rows. Publisher/series text and printed ornament were inspected, not counted as message glyphs.

Address-side handwritten text, with visual layout retained:

```text
Velectěná Slečna
slečna Anna Tichá.
učitelka v
Žirovnici
u Počátek.
```

The unencrypted Czech address identifies Anna Tichá as a teacher in Žirovnice near Počátky. Stamp, cancellation and printed postcard headings contain no further encrypted message.

## Reproduction and limits

From the repository root, this single command verifies the exact original image/metadata bytes, checks indexed manual records, and prints all literal plaintext:

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1537/work/decode.py
```

Default execution writes nothing. Optional `--write-derived` regenerates crops and derived displays. The program verifies 3 original hashes, 13 ordered rows, 289 indexed glyphs and an exact tokenwise key roundtrip. This pipeline starts from verified source bytes plus manual image records; it does not automatically extract glyphs from pixels. Reproducibility proves record/key consistency, not the truth of image reading.

No undeciphered span remains in the current manual reading. VAMBERCE is an eight-glyph literal reading, retained without replacing it by a modern place form; its precise historical referent has not been established. Pepouš is a readable nickname, not an identification of the sender. Editorial accents/case are not independently encoded. Date and school/holiday context support the message, while the controlling evidence is complete row coverage and repeated same-card shape consistency. Root visual verification and its limits are recorded below.

## Root verification — 2026-10-28

Root inspected both original sides, the complete upright13-row text panel, the ordered glyph records and focused PRI/PRISTIHO/VAMBERCE/BRZKY controls. The five-glyph BRZKY and eight-glyph VAMBERCE are supported by the visible forms; earlier familiar-word guesses are superseded. The short lower-left fragments belong to the full-width last three rows and are included. No additional cipher region found. Root's later image-derived questions/control requests are solver collaboration, not blind transcription or independent provider review.

Read-only reproduction passed3 source hashes,3 record hashes,2 credited reference hashes,13 ordered rows,289 cipher units→289 base letters,zero CH units, exact indexed TSV, literal-display equality and tokenwise key roundtrip. This verifies consistency; manual source transcription accuracy remains subject to independent review. The card199 reference itself is a prior proposed reading, not expert ground truth.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-28). The reviewer ran the reproduction command (exit 0, output byte-identical to work/plaintext-literal.txt), decoded the solver's cipher rows with its own independently written table (review/work/decode_review.py, identical output), and read all 13 rows (289 signs) itself from its own clockwise-rotated 4–5× crops before comparing (review/work/reading_review.txt). Its reading agrees with the solver's sign for sign except at one position, the last sign of OPET in row 13. It confirmed VAMBERCE (eight signs `f6np5hs5`), BRZKY (five signs, open-hooked q = Z then closed-loop g = K), the angular 4 = I in PRI and PRISTIHO, the shallow-v F in DEFINITIVNE against the looped f = V in the same word, the q/g (Z/K) split everywhere on the card, and that neither side carries further cipher text.

1. OPET is literally OPED on the card (minor). Accepted; this is a correction of the literal reading. On the reviewer's enlargement (review/work/z_opet.png), which I re-inspected for this closing pass, the last sign of row-13 word 8 is a plain stem with a separate top bar and no bowl: the t-shape, which this key reads as D (the same shape as DO in row 9). It is not the left-bowl d-shape that the key reads as T, as in TOHO (row 9) and TI, TVUJ, TESI (row 13). The corrected cipher for row 13 is `d4 df2y b5b32c 6 d5c4 c5 3b5t m6 phqg1 84cd5g.` and the corrected literal row 13 is `ti tvuj pepous a tesi se oped na brzky listek.` The editorial Czech keeps *opět*, now marked as an editorial correction of the writer's slip OPED. A likely cause, offered as a plausible explanation only: this cipher deliberately gives the t-shape to D and the d-shape to T, so writing the t-shape for T is an easy slip (and Czech word-final D and T are both pronounced [t]). The solver itself made the same t/d label confusion once in a draft of TVUJ (work/controls.md). The meaning does not change. The files in work/ (manual-records.json, indexed-transcription.tsv, plaintext-literal.txt) and the printed output of work/decode.py still show `3b5d` / `opet` as at DONE1, because this closing pass does not change work/; this section and report/report.md carry the corrected literal reading. Corrected sign counts: t 13, d 12 (the total stays 289).
2. Uncertainty list should name the close calls (minor). Accepted. The report's uncertainty section now names: the writer's slip OPED (one of 289 signs, so the cipher text is not flawless); the close calls checked on the scan by both solver and reviewer (4 = I against 1 = Y in PRI and PRISTIHO; the eight signs of VAMBERCE, including the descending p = B and tall h = R; the five signs of BRZKY with the q = Z / g = K split; the shallow-v F against the looped f = V in DEFINITIVNE); and the solver's own corrected false starts (FAMILCE → VAMBERCE, BRZY → BRZKY, the t/d label in TVUJ).
3. VAMBERCE identifiable as Vamberk (minor). Accepted as an inference. *Ve Vamberce* is the older Czech locative of Vamberk, a town in East Bohemia (Rychnov nad Kněžnou district), on the same pattern as Žamberk → *v Žamberce*. The literal text stays VAMBERCE and the normalized Czech keeps *ve Vamberce*; the English and Slovak translations render the place as Vamberk. That the writer meant this town is an inference from the form, not something the card states; it does support the reading, since an eight-sign string decoded with the fixed key gives the regular locative of a real Czech town.
4. Machine-specific interpreter in the command (minor). Accepted. The script uses only the Python standard library. I ran `python3 ciphers/hcp-1537/work/decode.py` from the repository root with the system Python: exit 0, `VERIFIED: 3 originals; 13 ordered rows; 289 indexed glyphs; exact tokenwise roundtrip.`, and the same 13 lines. The report gives this portable command; the codex-runtime interpreter named above works the same.

Status: the statements earlier in this file that no reviewer, PDF or register entry exists, and that the transcription awaits independent review, describe the state at DONE1 and are left in place as a record; this section supersedes them. Independent review 1 by Claude Opus 5.5 returned ACCEPT; report/report.pdf and register-entry.txt exist.

Additional notes from the closing pass: 17 September 1903 was a Thursday. The address side carries an Austrian 5-heller stamp with a cancellation at the top right whose place name is only partly legible, and an arrival-type stamp ŽIROVNICE / SEROWITZ whose day and month are only partly legible (year 03). The register type is recorded as MASC (monoalphabetic substitution, known family key; the CH sign of the family key does not occur on this card).

Remaining uncertainties carried into the report: the editorial accents, punctuation and word joins; the writer's slip OPED (editorial *opět*); Vamberk as the intended place (inference); the civil identity of Pepouš and what the *klášter* (monastery or convent) is; the key is a transferred family key, with the published partial key by Maxim Egorov acknowledged in SOURCES.md; novelty rests on the bounded checks in SOURCES.md (portal status Not solved, AI Decipherment Register snapshot of 173 contributions without this card, Egorov family index without pc216–218), which the reviewer did not repeat.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-28.
