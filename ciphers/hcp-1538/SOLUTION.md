# HCP 1538 / pc_hcp_219 — complete reading (round 2 record, after review 1)

**Status: complete reading of the Czech love letter from Pepouš to Anna Tichá, 22 Sep 1903.**
503 cipher signs: 498 read on the scan, 1 partly visible (the `d` in M07), 4 restored by the editor
at the edge of the printed stem/flower (`[3]` in M06, `[3c]` in M07, `[6]` in S01). The printed bouquet
stem was on the card before the writing; the writer left it blank, so the former spans G01–G05, G08
and G09 hide no letters. Initial transcription and partial decipherment by OpenAI GPT (GPT-6 Astra /
GPT-6.1 Sol) on 2026-10-28; completion by Claude Opus 5.5 on 2026-10-29; review round 1 by a separate
Claude Opus 5.5 agent (verdict REVISE), addressed below.

## Cipher and key

Monoalphabetic substitution of the Anna Tichá family (key transferred from earlier family cards and the
published partial study by Maxim Egorov; not recovered blind here). Diacritics are not encoded.

| Cipher | 1 | 2 | 3 | 4 | 5 | 6 | 8 | b | c | d | f | g | h | m | n | p | q | r | s | t | y / 7 | ř (H) | shallow v |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Plain | y | u | o | i | e | a | l | p | s | t | v | k | r | n | m | b | z | h | c | d | j | ch | f |

Full table: `work/key.json`. Shallow v (F) does not occur on this card.

## Reproduction (single command, from the repository root)

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1538/work/decode_final.py
```

It checks the SHA-256 of both scans, decodes the final manual transcription `work/transcript-final.txt`
with `work/key.json`, stops on any unmapped glyph, counts read / partly visible / restored signs
separately, checks the output against the saved `work/decoded-final.txt`, and prints:

```text
COMPLETE literal reading: 498 signs read, 1 partly visible, 4 restored; 503 cipher signs total; no unmapped glyphs.
M01 tisicery dik za drahy listek dnesni! take
M02 mne se anicko ma jedina, velice styska
M03 po tobe. dovolene me se, drahousku, bati nemu-
M04 sic, vzdit vis, ze jen tebe a pro vzdy mam rad.
M05 zaujala jsi moji dusi celou a neni tam jiz
M06 mista pro nikoho jineh[o] dovolenou svoji stravim
M07 asi celou ve spolecn[os](t)i pana dekana, s kte-
M08 rym budeme prohlizeti pametni knihu dekan-
M09 skou, jak jsem si to jiz zamlouval pri
M10 cecilskem koncerte. den, kdy odjedu dosud
M11 nevim, myslim vsak, ze bud ve ctvrtek vecer neb
S01 v patek rano. zalezi n[a] tom, kdy budu s uctem
S02 kvartalnim hotov. tisic uprimnych pus ti posila
S03 vecne tvuj pepous, ktery se na slibene psanko
S04 nesmirne tesi.
```

In `work/transcript-final.txt` `||` marks the blank printed stem, `[..]` restored signs and `(..)` a partly
visible sign. The round-1 record (`work/transcript.json`, `work/decode.py`, `decoded-literal.txt`,
`indexed-units.tsv`) is kept unchanged as history and is superseded.

Literal spellings kept: `nemu-|sic` (the writer's NEMUSIC for *nemusíš*, cf. `d5c4s` TESIC on sister
cards), `vzdit` (cipher `fqt4d`, 4 = I, not 1 = Y; normalised editorially to *vždyť*), `pus`
(genitive plural of *pusa*, correct).

## Editorial Czech

Tisícerý dík za drahý lístek dnešní! Také mně se, Aničko má jediná, velice stýská po tobě. Dovolené mé
se, drahoušku, báti nemusíš, vždyť víš, že jen tebe a pro vždy mám rád. Zaujala jsi moji duši celou a
není tam již místa pro nikoho jiného. Dovolenou svoji strávím asi celou ve společnosti pana děkana, s
kterým budeme prohlížeti pamětní knihu děkanskou, jak jsem si to již zamlouval při cecilském koncertě.
Den, kdy odjedu, dosud nevím, myslím však, že buď ve čtvrtek večer neb v pátek ráno. Záleží na tom, kdy
budu s účtem kvartálním hotov. Tisíc upřímných pus ti posílá věčně tvůj Pepouš, který se na slíbené
psánko nesmírně těší.

## English translation

A thousand thanks for your dear card today! I too miss you very much, my only Anička. You need not fear
my holiday, darling; you know that I love only you, and for ever. You have taken my whole soul and there
is no room left in it for anyone else. I shall probably spend my whole holiday in the company of the
dean, with whom we are to look through the deanery's memorial book, as I already arranged at the
Cecilian concert. I do not yet know the day I leave, but I think either Thursday evening or Friday
morning. It depends on when I finish the quarterly accounts. A thousand sincere kisses are sent to you
by your ever-faithful Pepouš, who is immensely looking forward to the promised little letter.

## Slovak translation

Tisícoraká vďaka za drahý dnešný lístok! Aj mne sa, Anička moja jediná, veľmi cnie za tebou. Mojej
dovolenky sa, miláčik, báť nemusíš, veď vieš, že len teba a navždy mám rád. Zaujala si celú moju dušu a
nie je tam už miesto pre nikoho iného. Dovolenku strávim asi celú v spoločnosti pána dekana, s ktorým
budeme prezerať dekanskú pamätnú knihu, ako som si to už dohodol pri cecilskom koncerte. Deň odchodu
ešte neviem, myslím však, že buď vo štvrtok večer, alebo v piatok ráno. Záleží na tom, kedy budem hotový
so štvrťročným účtom. Tisíc úprimných bozkov ti posiela naveky tvoj Pepouš, ktorý sa nesmierne teší na
sľúbený list.

## Uncertainties (current)

- **Restorations, not readings:** JINEH[O] (M06), SPOLEČN[OS]TI (M07) and N[A] TOM (S01). Each lies at
  the edge of the printed stem or the yellow flower; the letters rest on edge traces and Czech grammar.
  The Czech of all three is certain from context, the signs are not read.
- **M07 `d`:** only a rising stroke (ascender) is visible right of the stem; read as `d` (T) because of
  the word *společnosti*.
- **S01 `m`:** the visible sign before the flower has the m-form (N); the reading *na tom* is supported
  by the form and by context together.
- **M03 `n5` (MÉ):** one-hump n, same form as `n6` (MÁ) in M02, different from the two-hump m in
  `t3f385m5`; confirmed by the reviewer. The round-1 `m5` (NE) was a transcription error.
- **M08 `r84`:** readable under heavier ink; no cancellation. PROHLÍŽETI.
- Writer's spellings: NEMUSIC for *nemusíš*, VZDIT for *vždyť*. Accents, capitals and punctuation of the
  editorial Czech are editorial.
- Only the scan exists: whether any letter is physically under the stem in M06, M07 or S01 cannot be
  checked.

## Response to review 1

1. **major — record does not match the reading. Fixed.** New final transcription
   `work/transcript-final.txt` and decoder `work/decode_final.py` (saved output `work/decoded-final.txt`).
   M03 `m5` → `n5`; C01 → `r84`; U01 settled as `m`; G01–G05, G08, G09 → `||` (blank stem, no letters);
   G06, G07, G10 encoded as bracketed restorations `[3]`, `[3c]`, `[6]`, kept separate from read signs
   and counted separately (498 read / 1 partly visible / 4 restored = 503). The header and the
   Uncertainties section above now match the complete reading. The command was re-run and passes.
   The round-1 files are kept unchanged as history.
2. **major — missing `s` in M04. Fixed.** I checked `review/work/m04a.png`: three signs `c`, `4` and a
   raised `s` stand before the comma. M04 now begins `c4s,` and the literal reads `nemu-|sic`
   (NEMUSIC = *nemusíš*, the writer's habit, cf. TESIC on sister cards). Counted in the 503.
3. **minor — word division in M07. Fixed.** The record now has `f5 cb385sm…` and the literal reads
   `ve spolecn[os](t)i`.
4. **minor — wording of restorations. Fixed.** The uncertainties now say that `m` = N in S01 rests on
   form and context together, and that the M07 `d` is only partly visible (marked `(d)` in the record).
5. **minor — `vzdit`. Agreed.** Kept literal (`fqt4d`, 4 = I); the editorial *vždyť* is stated as a
   normalisation here and in the report.

No decoded word changed except the corrections the reviewer itself verified (MÉ, the added S of
NEMUSIC); the reading equals the completion text that was reviewed.

---

# History: round-1 record (superseded; kept for the record)


This is a **partial manual transcription and known-key decipherment**, not a complete solution. All picture-side rows and both sides/margins were inspected. Ten dark spans, one uncertain overink span and one ambiguous visible glyph remain. No independent provider review or final state is claimed.

## Origin and source boundary

The rendered portal identifies this as Czech substitution postcard dated 1903-09-22, recipient Anna Tichá, private collection; status Not solved. No individual transcription or solution attachment was displayed. Source URLs, download records, prior public study and family-key sources are in SOURCES.md; source files were preserved unchanged. The fresh register snapshot omitted this target, a bounded check only.

The family key was available before target transcription from earlier local cards and the disclosed public Anna Tichá partial study. The proposed RUDOLFINA pc199 photograph was available as a comparative F reference, not independent expert ground truth; no new F inference is required by this transcript. This is key transfer and application after prior public partial study, not independent key discovery or a blind test. No initial target plaintext was supplied. Transcript is manual, not OCR.

Address side reads: **Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.** The picture date is **22./IX.1903**. No encrypted address text was observed.

## Cipher and key

Monoalphabetic letter substitution, Czech diacritics mostly omitted. ASCII glyph labels are manual surrogates, not claims about font identities; `ř` labels the handwritten CH-like symbol.

| Cipher | 1 | 2 | 3 | 4 | 5 | 6 | 8 | b | c | d | f | g | h | m | n | p | q | r | s | t | y / 7 | H / ř | shallow v |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Plain | y | u | o | i | e | a | l | p | s | t | v | k | r | n | m | b | z | h | c | d | j | ch | f |

The complete transferred table is `work/key.json`. Unused transferred mappings do not constitute evidence from this target.

## Reproduction

From the repository root, a single read-only command checks original/reference/record hashes, every indexed position and token-wise roundtrip, then emits the full recorded partial plaintext:

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1538/work/decode.py
```

`work/transcript.json` contains every recorded cipher unit, physical row and unknown-span annotation. `work/indexed-units.tsv` lists all 494 visible positions: 493 mapped units plus U01 (494 base output letters because CH is two letters). `work/row-index.json` locates every main and margin row crop; originals are picture.jpg and address.jpg in source/. The decoder does not perform OCR or extract letters automatically from pixels. It verifies the supplied images are the recorded originals and then verifies the human/AI manual record against the transferred key. The inverse is constructed from the entire key: 479 target units have singleton inverse classes and are recovered exactly; 14 units belong to alias classes j=y/7 or ch=H/ř and retain their original labels as necessary side information. Those aliases cannot be recovered uniquely from plaintext alone. Unknown placeholders roundtrip as placeholders, not recovered source glyphs. Default verification also compares both saved literal and indexed TSV outputs for exact equality; --emit-only skips only these saved-output comparisons during artifact authoring. Successful internal checks cannot establish correct manual readings or full coverage.

## Literal original-language output

The following retains physical row breaks, spellings and spaces, including `vzdit` and `pus`. G markers represent unknown-length dark spans; C01 is uncertain overink; U01 is one ambiguous m/n cipher glyph (plain n/m). No grammatical completion is embedded.

```text
M01 tisicery dik za drahy [G01: unreadable span] listek dnesni! take
M02 mne se anicko ma [G02: unreadable span] jedina, velice styska
M03 po tobe. dovolene ne [G03: unreadable span] se, drahousku, bati nemu-
M04 si, vzdit vis, ze jen [G04: unreadable span] tebe a pro vzdy mam rad.
M05 zaujala jsi moji dusi [G05: unreadable span] celou a neni tam jiz
M06 mista pro nikoho jineh [G06: unreadable span] dovolenou svoji stravim
M07 asi celou vespolec n[G07: unreadable span]i pana dekana, s kte-
M08 rym budeme pro[C01: uncertain overink]zeti[G08: unreadable span] pametni knihu dekan-
M09 skou, jak jsem si [G09: unreadable span]to jiz zamlouval pri
M10 cecilskem koncerte. den, kdy odjedu dosud
M11 nevim, myslim vsak, ze bud ve ctvrtek vecer neb
S01 v patek rano. zalezi [U01: n/m][G10: unreadable span]tom, kdy budu s uctem
S02 kvartalnim hotov. tisic uprimnych pus ti posila
S03 vecne tvuj pepous, ktery se na slibene psanko
S04 nesmirne tesi.
```

## Editorial Czech, with accents

This separate reading adds accents and sentence-initial capitals. It does not fill G/C/U spans. Original row-end splits remain. `vzdiť` and `pus` retain the recorded letters. `Pus` is valid Czech genitive plural in “tisíc upřímných pus”. Accents on personal names and ordinary words are editorial, not encoded distinctions.

```text
M01 Tisícerý dík za drahý [G01] lístek dnešní! Také
M02 mně se Aničko má [G02] jediná, velice stýská
M03 po tobě. Dovolené ne [G03] se, drahoušku, báti nemu-
M04 sí, vzdiť víš, že jen [G04] tebe a pro vždy mám rád.
M05 Zaujala jsi moji duši [G05] celou a není tam již
M06 místa pro nikoho jinéh [G06] dovolenou svoji strávím
M07 asi celou vespoleč n[G07]i pana děkana, s kte-
M08 rým budeme pro[C01]zeti[G08] pamětní knihu děkan-
M09 skou, jak jsem si [G09]to již zamlouval při
M10 cecilském koncertě. Den, kdy odjedu dosud
M11 nevím, myslím však, že buď ve čtvrtek večer neb
S01 v pátek ráno. Záleží [U01: n/m][G10]tom, kdy budu s účtem
S02 kvartálním hotov. Tisíc upřímných pus ti posílá
S03 věčně tvůj Pepouš, který se na slíbené psánko
S04 nesmírně těší.
```


## Slovak translation of the recorded partial text

Translation joins only established line-end word splits. Source fragments crossing unreadable regions remain marked. It is a translation of the partial reading, not a reconstruction of the missing wording.

```text
Tisícerá vďaka za drahý [G01] dnešný lístok! Aj
mne sa, Anička moja [G02] jediná, veľmi cnie
za tebou. Dovolené ne [G03] sa, miláčik, báť nemu-
sí, veď vieš, že len [G04] teba a navždy mám rád.
Zaujala si moju dušu [G05] celú a niet tam už
miesta pre nikoho inéh [G06] svoju dovolenku strávim
asi celú [neúplný úsek vespoleč n…i; G07] pána dekana, s kto-
rým budeme [neúplné pro…zeti; C01][G08] pamätnú knihu dekan-
skú, ako som si [G09]to už dohováral pri
cecilskom koncerte. Deň, keď odídem, dosiaľ
neviem, myslím však, že buď vo štvrtok večer, alebo
v piatok ráno. Záleží [U01: n/m][G10]tom, kedy budem s účtom
za štvrťrok hotový. Tisíc úprimných bozkov ti posiela
večne tvoj Pepouš, ktorý sa na sľúbené psánko
nesmierne teší.
```

## Uncertainties and limits

- G01–G09 are unknown-length central stem/dark spans; G10 is behind the yellow flower in S01. Even where a likely phrase is obvious, no letters are supplied. Total ciphertext length and full-message coverage are therefore unknown.
- U01 is one visible glyph before G10: cipher m or n, plain n or m. It occupies one indexed position; no choice is justified by grammar alone.
- C01 is dense overwritten/overinked middle ink in M08, between readable `bh3` and `q5d4` (`pro…zeti`). Possible middle `r84` would give `hli` and the word *prohlizeti*, but this is only a candidate. Horizontal strokes alone do not establish deliberate cancellation. The seven surrounding readable glyphs are provisionally counted as active; the uncertain middle is excluded without assuming its length. No definite canceled segment has been identified. This convention prevents canceled/uncertain ink from quietly inflating active coverage.
- S01 was corrected after native-pixel and same-card b/P versus 6/A controls: `f b6d5g` = *v patek*, with one b/P, not two. The former extra b was a transcription error. Exact control crops and coordinates are in work/control-index.json. `Pus` in S02 is valid Czech genitive plural, not an error. `vzdit` remains literal and is not silently changed to *vzdyt*.
- A preliminary `projekt` interpretation of M08 was rejected after close visual inspection. It is not evidence or plaintext.
- The coherent Czech across nearly all readable units, consistent transferred key, address/date context, and continuous letter content support a genuine partial decryption. They do not validate letters hidden by printed stems or every manually read glyph.
- Root/helper work is solver collaboration, not independent provider review. No watcher, reviewer, marker, PDF, register entry or git operation was made by this collaborator.

## Root source verification — 2026-10-28

Root inspected both original sides, all fifteen physical cipher rows in the complete main and marginal regions, the overink and Friday-word controls. Native pixels show `f b6d5g`, not `f bb6d5g`: literal V PATEK replaces the duplicated-P error. Records, index, hashes and both language renderings were corrected. The old 495-position count is superseded by 494 positions: 493 mapped units produce 494 assigned base letters (one CH); one visible m/n unit remains ambiguous.

Horizontal strokes do not establish authorial cancellation. M08 remains `pro[C01]zeti`, with seven surrounding units provisionally active and the middle span's length unknown. Ten other dark spans remain unresolved. The final audit derives inverse sets from the actual key: 479 mapped units invert uniquely; 14 require retained alias labels. Stored-stream equality is distinct from reversal from plaintext alone. Default reproduction checks 30 hashes, indexed positions, the saved literal output and saved TSV. This proves internal consistency, not image accuracy. Root and helper comparisons are solver collaboration. No marker or independent review.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading, handed to review (DONE1).**

**Main finding: the stem was printed before the text was written, and the
writer left it blank.** In work/claude/stem-a.png and stem-b.png (enlarged
from work/picture-upright.png) every row stops at the left edge of the stem
and resumes at its right edge. No stroke of the hand runs under the stem,
and on each side the signs are complete. So most G spans hide **no letters**:

| Span | Left of stem / right of stem | Hidden | Reading |
|---|---|---|---|
| G01 M01 | `th6r1` / `84cd5g` | nothing | DRAHY LISTEK |
| G02 M02 | `n6` / `75t4m6` | nothing | MA JEDINA |
| G03 M03 | `n5` / `c5` | nothing | **ME SE** (see correction) |
| G04 M04 | `q5 75m` / `d5p5` | nothing | ZE JEN TEBE |
| G05 M05 | `t2c4` / `c5832` | nothing | DUSI CELOU |
| G06 M06 | `74m5r` / `t3f38…` | one sign at the stem's edge | JINEH[O.] DOVOLENOU: the O is restored |
| G07 M07 | `cb385sm` / `…4` | about two signs, with the stem of a `d` just visible on the right | SPOLECN[OS]TI: *ve společnosti pana děkana*; O and S are restored |
| G08 M08 | `bh3r84q5d4` / `b6n5dn4` | nothing | PROHLIZETI PAMETNI |
| G09 M09 | `c4` / `d3` | nothing | SI TO |
| G10 S01 | `m` / `tom` behind the yellow flower | one sign | N[A] TOM: *záleží na tom*; A restored, `m` = N settles U01 |

**Correction to the record (M03).** The sign before G03 is transcribed `m`
(N), giving “ne”. In stem-a.png it is the same one-hump `n` as in `n6` (MÁ),
one row above, so it reads **MÉ**: “Dovolené mé se, drahoušku, báti
nemusíš, vždyť víš, že jen tebe a pro vždy mám rád.” (“You need not fear my
holiday, drahoušku; you know I love only you, for ever.”) The decoder still
prints the recorded `ne`. Please check this sign.

**C01 (M08 `pro…zeti`).** With the rest of the word visible, `bh3r84q5d4`
reads **PROHLIZETI**. The overink falls on `r8`, which is still readable.

Editorial Czech: “Tisícerý dík za drahý lístek dnešní! Také mně se, Aničko má
jediná, velice stýská po tobě. Dovolené mé se, drahoušku, báti nemusíš,
vždyť víš, že jen tebe a pro vždy mám rád. Zaujala jsi moji duši celou a
není tam již místa pro nikoho jiného. Dovolenou svoji strávím asi celou ve
společnosti pana děkana, s kterým budeme prohlížeti pamětní knihu děkanskou,
jak jsem si to již zamlouval při cecilském koncertě. Den, kdy odjedu, dosud
nevím, myslím však, že buď ve čtvrtek večer neb v pátek ráno. Záleží na tom,
kdy budu s účtem kvartálním hotov. Tisíc upřímných pus ti posílá věčně tvůj
Pepouš, který se na slíbené psánko nesmírně těší.”

Slovak: „Tisícoraká vďaka za drahý dnešný lístok! Aj mne sa, Anička moja
jediná, veľmi cnie za tebou. Mojej dovolenky sa, miláčik, báť nemusíš, veď
vieš, že len teba a navždy mám rád. Zaujala si celú moju dušu a nie je tam
už miesto pre nikoho iného. Dovolenku strávim asi celú v spoločnosti pána
dekana, s ktorým budeme prezerať dekanskú pamätnú knihu, ako som si to už
dohodol pri cecilskom koncerte. Deň odchodu ešte neviem, myslím však, že buď
vo štvrtok večer, alebo v piatok ráno. Záleží na tom, kedy budem hotový so
štvrťročným účtom. Tisíc úprimných bozkov ti naveky posiela tvoj Pepouš,
ktorý sa nesmierne teší na sľúbený list.“

Reproduce with the command given earlier in this file. The family key is
credited to earlier family cards and the published partial study by Maxim Egorov.
