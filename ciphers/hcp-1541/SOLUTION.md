# HCP 1541 / pc_hcp_222 — Pepouš to Anna Tichá, 19 August 1903

Status: **complete reading with two letters restored under the printed picture and one visible sign of uncertain shape; all three marked.** Current state after review 1 (Claude Opus 5.5 as solver, 2026-10-29). The round-0 candidate by the earlier solver (OpenAI GPT-6 Astra / GPT-6.1 Sol, 2026-10-28) and the completion that went to review are kept below under "History"; where they differ from this top part, this top part is current.

Czech picture postcard dated 19. VIII. 1903, addressed to Anna Tichá, teacher temporarily in Pelhřimov. The writer thanks her for a card, mentions Hradec and the deanery memorial book in Ústí, and explains that he must postpone his holiday because his superior is taking leave to accompany his sick brother-in-law to a spa. It is signed with the nickname PEPOUŠ.

This is **key transfer**, not a new key discovery: the Anna Tichá / Pepouš family key (earlier family cards in this repository, ciphers/hcp-1545/work/key.json; partial public study by Maxim Egorov, https://maxim-egorov.dev/research/anna-ticha-postcards/) was known before transcription. The portal attaches no transcription or solution. See SOURCES.md.

## Cipher type and key

Simple monoalphabetic substitution (MASC) with letter- and digit-shaped signs and one sign for the digraph CH. Labels name the shape of each cipher sign:

```
1→y 2→u 3→o 4→i 5→e 6→a 7→j 8→l
b→p c→s d→t f→v g→k h→r m→n n→m p→b q→z r→h s→c t→d
k→g   (k-shaped sign: ascender, loop, kicked leg; distinct from looped g = K)
H→ch  (capped h-shape)
```

S/Š share the sign `c`, C/Č share `s`, and so on; the cipher does not mark diacritics. File: work/key-final.json (23 signs). The round-0 record labelled the J sign `y`; it is the 7-shaped sign and is now labelled `7` as in the family key (hcp-1545). The mapping is unchanged.

## Single reproduction command

From the repository root:

```bash
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1541/work/decode_final.py
```

(any python3 ≥ 3.8 works; no third-party modules). It verifies the 11 source/reference/record hashes, checks that the final transcription work/transcription-final.txt differs from the audited round-0 record work/transcription.txt only by the documented relabels (`y`→`7`, `[U01]`→`k`, `[U02]`→`(5)`, `[U03]`→`(d)5<s>4`), applies work/key-final.json, checks that every key sign is used, and prints the full literal plaintext. Markup: `(x)` = sign hidden under the printed picture, restored from context; `<x>` = visible sign of uncertain shape, decoded as its best match. Output: 19 rows; 550 visible cipher signs decoded (1 of uncertain shape); 2 hidden signs restored; all 23 key signs used.

The older audit work/decode.py still runs and prints the round-0 literal with the U01–U03 placeholders; it is kept as the record of that state.

## Literal plaintext (output of the command)

```
vrely dik, holubicko moje, za drahy listek, jenz
se s nim krizoval. dostala jsi jeste muj listek
v hradci? - tesi mne, ze je srdecko moje opet zdra-
vo jako diblik. mel jsem velkou starost. vzpo-
minam, zlato moje, stale. chtel jsem nastoupiti
dovolenou svoji koncem tohoto mesice, abych
se mohl podivati jeste do ustecke pametni
knihy dekanske, avsak zhatil se muj plan.
nas vrchni spravec, ktery nechtel jiti na dovole-
nou, nastoupi ji nasledkem choroby sveho
svagra, ktereho bude provazeti
do lazni, presto zitra, nasled-
kem cehoz musim odloziti ja
svoji dovolenou az na druhy
mesic. tisic dlouhych, vrelych
pus posila ti vecn(e)tvuj
pepous, ktery se (t)e<c>i na
opetnou brzkou zpravu
od sveho srdecka.
```

## Editorial Czech reading

Accents, capitals and word joins restored; restorations in square brackets.

> Vřelý dík, holubičko moje, za drahý lístek, jenž se s ním křižoval. Dostala jsi ještě můj lístek v Hradci? — Těší mne, že je srdéčko moje opět zdrávo jako diblík. Měl jsem velkou starost. Vzpomínám, zlato moje, stále. Chtěl jsem nastoupiti dovolenou svoji koncem tohoto měsíce, abych se mohl podívati ještě do ústecké pamětní knihy děkanské, avšak zhatil se můj plán. Náš vrchní správce [literally *spravec*], který nechtěl jíti na dovolenou, nastoupí ji následkem choroby svého švagra, kterého bude provázeti do lázní, přesto zítra, následkem čehož musím odložiti já svoji dovolenou až na druhý měsíc. Tisíc dlouhých, vřelých pus posílá ti věčn[ě] tvůj Pepouš, který se [t]ě[š]í na opětnou brzkou zprávu od svého srdéčka.

## English translation

> Warm thanks, my little dove, for the dear card, which crossed with mine. Did you still get my card in Hradec? — I am glad that my little heart is well again, as lively as a little imp. I was very worried. I think of you all the time, my treasure. I wanted to take my holiday at the end of this month, so that I could also look into the deanery memorial book in Ústí, but my plan has fallen through. Our chief administrator, who did not want to go on leave, is taking it after all, tomorrow, because of the illness of his brother-in-law, whom he will accompany to a spa; as a result I must put my holiday off until next month. A thousand long, warm kisses are sent to you by your forever [*věčně*, restored] Pepouš, who is looking forward [*těší se*, partly restored] to a new, early message from his little heart.

## Slovak translation

> Vrelá vďaka, holubička moja, za drahý lístok, ktorý sa minul s mojím. Dostala si ešte môj lístok v Hradci? Teší ma, že je moje srdiečko opäť zdravé ako diablik. Mal som veľkú starosť. Stále na teba spomínam, zlato moje. Chcel som nastúpiť na dovolenku koncom tohto mesiaca, aby som sa mohol ešte pozrieť do ústeckej dekanskej pamätnej knihy, môj plán sa však zmaril. Náš vrchný správca, ktorý nechcel ísť na dovolenku, na ňu predsa zajtra nastúpi pre chorobu svojho švagra, ktorého bude sprevádzať do kúpeľov, a preto musím svoju dovolenku odložiť až na budúci mesiac. Tisíc dlhých, vrelých bozkov ti posiela navždy [restored] tvoj Pepouš, ktorý sa teší [partly restored] na opätovnú skorú správu od svojho srdiečka.

## Uncertainties

1. **SVAGRA (row 11).** The k-shaped sign is not in the published partial family key. It is read as G because only G gives a word (*švagra*, "brother-in-law"), and the same sign stands where only G fits on HCP 1570 (SVAGROVA and KOLEGY; that card's independent review identified the sign in both words), and on HCP 1553/1554 (TELEGRAM-). On this card it occurs once, and it is clearly distinct from the looped `g` (K) in KTEREHO on the same row (work/svagra.png).
2. **VĚČN[Ě] TVŮJ (row 16).** A printed green patch covers about one sign between `f5sm` (VECN) and `df27` (TVUJ); no ink of it can be identified. E (věčně tvůj, "forever yours") is restored from the family's closing formula (also on HCP 1552, 1554). VĚČNÝ TVŮJ is equally possible from the pixels; the meaning is the same.
3. **[T]Ě[Š]Í (row 17).** After `c5` (SE) the patch hides one sign (a bowl visible inside the patch is compatible with `d` = T but not identifiable). Then three signs are visible: an E-like sign (`5`; its top bar makes it 5 rather than 3), a **tall slanted stroke with a small foot**, and `4` (I). The tall stroke is not the round `c` that this writer uses for S/Š everywhere else; it best matches the angular `s` (= C), less well `1` (= Y). The literal decode is therefore `(t)e<c>i`. The sentence requires TĚŠÍ ("který se těší na …", "who looks forward to …"); no other Czech word fits *se ?e?i na*. So the reading TĚŠÍ assumes either a writer's slip — writing `s` instead of `c`, i.e. the plain letter of a swapped key pair, the same kind of slip as the T-for-D in TIK = *dík* on HCP 1556 — or an unrecorded variant. TĚŠÍ is an **editorial, context-based reading** for the hidden T and the Š; only E and I are read from visible signs. Crops: work/review1/u03_7x.png, u03_7x_contrast.png.
4. **SPRAVEC (row 9)** is literal (`cbh6f5s`); *správce* is an editorial repair of the writer's spelling (E and C transposed), not a key change.
5. Accents, punctuation and word division of the editorial text are editorial; the cipher does not encode diacritics.
6. "Hradec", "Ústí", the superior and the identity of Pepouš are not identified further. Nothing hidden completely under the printed picture can be recovered from a 674×1024 scan beyond the two restorations above.

## Why the reading is believed correct

The family key, unchanged except for adding the k-shaped G already established on sister cards, turns all 550 visible signs into grammatical Czech of around 1900 (nastoupiti, následkem čehož, pamětní kniha děkanská) without leftovers; the only irregular places are the literal SPRAVEC, the row-17 stroke and the two signs under the paint. The content (a postponed holiday, the closing nickname Pepouš, *holubičko*, *srdéčko*) matches the rest of the Anna Tichá family, and the date 19./VIII.1903 and the Pelhřimov address agree with the portal metadata. An independent reviewer decoded the transcription with their own table and got the same text letter for letter.

## Unencrypted writing

Picture side: date `19./VIII.1903.` Address side: `Velectěná Slečna / Anna Tichá / učitelka t.č. / v Pelhřimově / Vlastnoručně / dodati.` (honoured Miss Anna Tichá, teacher at present in Pelhřimov; to be delivered into her own hands). Postal print, stamp, postmarks, publisher's mark and the portal watermark are not cipher.

## Response to review 1

Review 1 (Claude Opus 5.5, verdict REVISE) had five findings. All are addressed; the reading of the letter is unchanged except that the row-17 word is now presented honestly as partly editorial.

1. **[major] U03: "EŠÍ still visible" contradicted by the scan — agreed, fixed.** I re-cropped the passage myself from source/picture.jpg (upright, 7x, also with auto-contrast: work/review1/u03_7x.png, work/review1/u03_7x_contrast.png). The reviewer is right: the sign between the E-like sign and `4` is a tall slanted stroke with a foot, not the round `c` of TĚŠÍ in row 3 or of PUS/POSILA in row 16. The E-like sign has a top bar to the left, which fits `5`. The transcription now records the visible signs as they are: `c5 (d)5<s>4 m6`, with the hidden first sign marked `( )` and the uncertain stroke marked `< >`; the literal output is `se (t)e<c>i na`. SOLUTION.md (Uncertainties 3) now calls TĚŠÍ an editorial reading, states the C/Š discrepancy, and gives the two possible explanations (a slip of the same type as TIK on HCP 1556, or a variant). The earlier sentence "`5 c 4` (EŠÍ) are still visible" is withdrawn.
2. **[major] the command did not print the final text — fixed.** New read-only command `work/decode_final.py` (above) with work/transcription-final.txt and work/key-final.json. It prints SVAGRA, `vecn(e)tvuj` and `se (t)e<c>i na`, and asserts that the final transcription differs from the audited round-0 record only by the four documented relabels, so no other sign was changed silently. Rerun on 2026-10-29: all 11 hashes verified, 550 visible signs decoded, 2 restored, all 23 key signs used, output identical to the "Literal plaintext" block above. The literal, editorial, English and Slovak sections at the top of this file were rewritten to agree with it; the older, conflicting sections are now under "History" and marked superseded.
3. **[minor] U02 = E is a pure restoration — agreed.** The editorial text now shows věčn[ě], and Uncertainties 2 says VĚČNÝ is equally possible from the pixels.
4. **[minor] J labelled `y` though it is 7-shaped — fixed.** The final transcription and key use `7`, as in the family key (hcp-1545). The mapping is unchanged; the decoder checks the relabel against the round-0 record.
5. **[minor] cross-references to unaccepted cards — agreed.** The G argument now rests first on HCP 1570, whose independent review identified the k-shaped sign in two places where only G fits (SVAGROVA, KOLEGY). HCP 1553/1554 are cited as further occurrences, not as accepted proof. On this card itself G is the only letter that makes a word.

What the reviewer could not verify (the signs fully under the paint, the nature of the row-17 stroke) cannot be settled from this scan either; both are disclosed above as restorations / editorial readings.

# History

## Round-0 candidate (GPT solver collaboration, 2026-10-28) — superseded, kept for the record

Czech postcard dated 19. VIII. 1903, addressed to Anna Tichá, teacher temporarily in Pelhřimov. Its writer thanks her for a letter, refers to Hradec and a deanery memorial book in Ústí, and explains postponing his holiday because his superior will take leave. The closing nickname is literally PEPOUS. The present claim leaves one unassigned visible glyph and two dark spans of unknown length unresolved.

This is **key transfer**, not a new independent key discovery. The family key and public partial Anna Tichá study were available before manual transcription. The public pc199/RUDOLFINA photograph is a disclosed glyph reference, not expert ground truth; no rare shallow-v/F reading is claimed on this target. No initial target plaintext was supplied. Root inspected the rendered portal tabs and register; there was no attached target transcription or solution. See SOURCES.md. Solver collaboration is not independent-provider review.

### Key and manual record

The cipher is monoalphabetic substitution, using letter-shaped and numeral-shaped symbols. `H` labels one special h/caron-shaped class mapping to the digraph CH; it is one cipher unit. Other labels describe glyph classes, not ordinary Latin writing.

```
1→y 2→u 3→o 4→i 5→e 6→a 8→l
q→z g→k f→v h→r t→d r→h c→s s→c
n→m m→n p→b b→p d→t y→j H→ch
```

Work/transcription.txt and inventory.json record all 19 visible cipher rows, with row crops, crop bounds, global and row glyph indices, token positions and literal output. There are **547 indexed visible units: 546 assigned through this key and one unassigned visible glyph U01**. Two additional dark spans, U02 and U03, have unknown glyph counts and are excluded from that count. A dark span is not replaced with one invented glyph. No canceled handwritten cipher writing was identified; the painting's trees are not counted as cancellations. Crop bounds are diagnostic regions, sometimes including neighbors, not precise automatic glyph segmentation.

Both complete postcard sides and all remaining margins were inspected. The address and date are unciphered. No additional visible cipher writing was found outside the 19 recorded rows. A digital image cannot establish whether completely invisible writing exists under the dark painted design.

### Literal Czech output

Line divisions, hyphens and the apparent original SPRAVEC spelling are preserved. Accents have not been restored. Unknown labels are retained exactly.

```
vrely dik, holubicko moje, za drahy listek, jenz
se s nim krizoval. dostala jsi jeste muj listek
v hradci? - tesi mne, ze je srdecko moje opet zdra-
vo jako diblik. mel jsem velkou starost. vzpo-
minam, zlato moje, stale. chtel jsem nastoupiti
dovolenou svoji koncem tohoto mesice, abych
se mohl podivati jeste do ustecke pametni
knihy dekanske, avsak zhatil se muj plan.
nas vrchni spravec, ktery nechtel jiti na dovole-
nou, nastoupi ji nasledkem choroby sveho
sva[U01]ra, ktereho bude provazeti
do lazni, presto zitra, nasled-
kem cehoz musim odloziti ja
svoji dovolenou az na druhy
mesic. tisic dlouhych, vrelych
pus posila ti vecn[U02]tvuj
pepous, ktery se [U03] na
opetnou brzkou zpravu
od sveho srdecka.
```

### Editorial Czech reading

This restores accents and capitalization and joins words divided by line breaks. It explicitly repairs SPRAVEC to *správce*. U01 is shown as a linguistic G conjecture; the supplied key does not contain a G assignment and no G mapping has been added. The dark spans remain gaps of unknown length. No target secondary accent rule has been applied.

> Vřelý dík, holubičko moje, za drahý lístek, jenž se s ním křižoval. Dostala jsi ještě můj lístek v Hradci? — Těší mne, že je srdéčko moje opět zdrávo jako diblík. Měl jsem velkou starost. Vzpomínám, zlato moje, stále. Chtěl jsem nastoupiti dovolenou svoji koncem tohoto měsíce, abych se mohl podívati ještě do ústecké pamětní knihy děkanské, avšak zhatil se můj plán. Náš vrchní správce, který nechtěl jíti na dovolenou, nastoupí ji následkem choroby svého šva[g?]ra, kterého bude provázeti do lázní, přesto zítra, následkem čehož musím odložiti já svoji dovolenou až na druhý měsíc. Tisíc dlouhých, vřelých pus posílá ti věčn[U02: nečitelné, délka neznámá]tvůj Pepouš, který se [U03: nečitelné, délka neznámá] na opětnou brzkou zprávu od svého srdéčka.

The punctuation and “přesto zítra” remain close to the literal source, even though modern editorial punctuation could make the sentence smoother. “Hradec” and “Ústí” have not been expanded to specific modern towns without evidence. No writer or historical-person identification is established by the nickname.

### Slovak translation of the editorial reading

> Vrelá vďaka, holubička moja, za drahý lístok, ktorý sa s ním minul na ceste. Dostala si ešte môj lístok v Hradci? Teší ma, že je moje srdiečko opäť zdravé ako diablik. Mal som veľkú starosť. Stále na teba myslím, zlato moje. Chcel som nastúpiť na dovolenku koncom tohto mesiaca, aby som sa mohol ešte pozrieť do ústeckej dekanskej pamätnej knihy, môj plán sa však zmaril. Náš vrchný správca, ktorý nechcel ísť na dovolenku, na ňu pre chorobu svojho šva[g?]ra, ktorého bude sprevádzať do kúpeľov, predsa nastúpi zajtra. Preto musím svoju dovolenku odložiť až na ďalší mesiac. Tisíc dlhých, vrelých bozkov ti posiela večn[U02: nečitateľné, neznáma dĺžka]tvoj Pepouš, ktorý sa [U03: nečitateľné, neznáma dĺžka] na opätovnú skorú správu od svojho srdiečka.

“Minul na ceste” interprets the crossed-mail idiom, rather than adding a cipher reading. The proposed G remains uncertain in the translation as well. The missing endings/words are not supplied from grammatical expectation.

### Unencrypted writing and coverage

Picture-side bottom: `19./VIII.1903.` This agrees with the portal date. The rest of the picture has painted scenery, a printed artist/publisher mark, and the portal watermark; these are excluded from the cipher inventory. Whole-side upright.png retains all borders and the date.

Address-side handwriting: `Velectěná Slečna / Anna Tichá / učitelka t.č. / v Pelhřimově / Vlastnoručně / dodati.` This is a postal address and delivery instruction, not substitution output. Postal headings, stamp, postmarks, watermark and printed rules are excluded from cipher counts. No complete postmark transcription or new historical inference is claimed. Address-control.png includes every margin.

### Uncertainties and corrections

- **U01, P11:** one distinct k-like cipher glyph in `sva[U01]ra`. It is not in the supplied key. The Czech word suggests *švagra*, but linguistic fit does not establish the glyph assignment. The unassigned class is retained, with a dedicated svagra.png crop.
- **U02, P16:** dark painting overlaps the writing between readable `f5sm` → VECN and readable `df2y` → TVUJ. The number and identity of hidden glyphs are unknown. No final vowel, conjunction or word space is inserted from expected “věčně/věčný tvůj”.
- **U03, P17:** dark painting overlaps writing between readable `c5` → SE and final `m6` → NA. No “těší” is inserted on the strength of grammar alone; the span length is unknown.
- Literal **SPRAVEC** is preserved as `cbh6f5s`; editorial *správce* changes the order of C/E explicitly. It is not hidden inside the key.
- Initial working guesses PANVE/ZNAMY were rejected by the visible glyphs. The actual sequence `b6n5dm4 / gm4r1 t5g6mcg5` gives PAMETNI / KNIHY DEKANSKE. Focused controls are retained. P18 `qbh6f2` gives ZPRAVU, with no added K or invented *schůzku*.

### Single read-only reproduction command

From the repository root:

```bash
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1541/work/decode.py
```

This verifies 11 immutable-source/reference/key/manual-record hashes, row and glyph indices, exact token positions, actual key application and re-encoding through the **inverse of the fixed substitution key**. Unknown labels are preserved separately and are not claimed to pass decryption or acquire glyph counts. The inverse is not manufactured from individual token/reading pairs. The command prints the complete literal text above and does not write files.

Source images are read for their hashes. Manual transcription is the explicit bridge between pixels and tokens; the command is not OCR and a passing round trip is not visual proof. Optional build-record.py regenerates working records/crops and is therefore not the read-only verification command. Coherent same-key Czech and whole-card coverage support the candidate, but the three unresolved regions prevent an unqualified full-solution claim. No independent review, watcher, marker, PDF or register entry was created by this collaborator.


### Root source verification — 2026-10-28

Root inspected both originals, all nineteen main and closing rows, and focused PAMETNI, KNIHY, SPRAVEC, ZPRAVU and U01–U03 crops. Visible PAMETNI KNIHY replaces early guesses; SPRAVEC stays literal. The ornate unit in SVA[U01]RA has no supported G mapping in the disclosed generic key. Švagra is an explicitly marked linguistic conjecture. Two dark spans remain unknown in length; no vowel or TĚŠÍ is supplied.

Read-only reproduction passed eleven source, reference, key and manual-record hashes and all 547 indexed visible positions. There are 546 assigned units producing 553 base letters (seven CH), one unassigned visible unit and two uncounted dark spans. The actual fixed-key inverse checks known units. Unknown labels are preserved, not decrypted. Crops are diagnostic regions, not precise glyph segmentation. The candidate remains partial. Root and helper work is solver collaboration. No marker or independent provider review.

### Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading, handed to review (DONE1).**

1. **U01, SVA?RA (work/svagra.png).** The word is `c f 6 k h 6`. The
   unmapped sign is a **k-shaped** sign: an ascender with a loop and a kicked
   leg. It is distinct from the looped `g` (K) used in KTEREHO on the same
   row. Only G gives a word: **SVAGRA** (*švagra*, “brother-in-law”). The
   family key thus has a **G sign of k shape**. The same single unmapped sign
   stands where only G fits on HCP1570 (KOLE?I = kolegy; described there as
   resembling h/R) and on HCP1554 (TELE?RAM). The three cards support one
   another, and the reviewer may compare the three crops.
2. **U02, `vecn[■]tvuj` (work/tail16-19.png, line 2).** After `f5sm` (VECN)
   a dark printed patch covers about one sign. `d f 2 7` (TVUJ) follows. Read
   **VECNE TVUJ** (*věčně tvůj*, “forever yours”). The covered sign is E,
   restored from context. The closing phrase is the same as on HCP1552 and
   HCP1554.
3. **U03, `se [■] na` (line 3).** After `c5` (SE) the patch hides the first
   sign; `5 c 4` (EŠÍ) are still visible after it. Read **TESI**: “který se
   těší na opětnou brzkou zprávu” (“who looks forward to…”). The hidden first
   sign is T, the only Czech completion.

Editorial Czech of the changed passages: “…následkem choroby svého švagra,
kterého bude provázeti do lázní… Tisíc dlouhých, vřelých pus posílá ti věčně
tvůj Pepouš, který se těší na opětnou brzkou zprávu od svého srdéčka.”

Reproduce with the command given earlier in this file. The family key is
credited to earlier family cards and the published partial study by Maxim Egorov.

(The completion above was superseded by "Response to review 1": its U03 description "5 c 4 (EŠÍ) still visible" is withdrawn.)
