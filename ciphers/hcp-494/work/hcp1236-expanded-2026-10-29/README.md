# Additional HStAM4d1236 images exposed by HCP,2026-10-29

All22 supplied hero images from records267–288 were downloaded and visually inspected. **No unchanged255 alphabet or matching target nomenclator was identified. No new HCP494 plaintext is established.**

## Provenance and inspection scope

Root opened each record in the normal rendered HCP interface and copied its visible attachment `src`. This helper fetched only those exact22 URLs. No HCP data API was queried and no unobserved neighboring URL was inferred. The [manifest](manifest.json) gives exact public URLs, local filenames, dimensions, byte counts and SHA256 hashes; all22 hashes were checked after saving. Every image is1024 pixels wide.

The assessment covers the supplied hero page, not all attachments of every record. All22 were viewed as full images. Dense dictionary cells were not exhaustively transcribed; fine readings at this resolution remain limited. Readings below are visual working readings.

## Comparisons

| HCP / scan | Content and observed values | Assessment |
|---|---|---|
| [267 / 0030](267-0030.jpg) | Numeric word list, no alphabet on supplied image. Dennemarck236/339; Holstein239/342; king of Denmark235/338/583. | Different country entries; alphabet remains unseen. |
| [268 / 0039](268-0039.jpg) | Alphabet and syllables/word list. a20, ae/umlaut-a21, b22, c23, d24; Dennemarck155 (working reading). | Isolated a20/b22 is not unchanged255: c23 differs from targetc24. |
| [269 / 0041](269-0041.jpg) | Alphabet and dense French dictionary. a11,b10,c9,d8; second homophones33,34,35,36. | Alphabet differs; small word entries not exhaustively transcribed. |
| [270 / 0044](270-0044.jpg) | Alphabet and syllables. a2557/2558, b2559/2561; four-digit sequence. | Alphabet differs. |
| [271 / 0051](271-0051.jpg) | Large French syllable table with names. A10; B26; Holstein388. | Syllabic numbering differs; resembles288. |
| [272 / 0054](272-0054.jpg) | Pour Mons. le Baron de Dalwig: dictionary. Alliance249; Dennemarck367. | Target country code differs; no alphabet shown. |
| [273 / 0059](273-0059.jpg) | Encoding and decoding alphabet. a45..48,b37..40,c29..32,d53..56; n1..4. | Alphabet differs. |
| [274 / 0064](274-0064.jpg) | Alphabet and German dictionary. A10..15,B16..21,C22..27;20 thereforeb. | Alphabet differs; dense word cells not all transcribed. |
| [275 / 0066](275-0066.jpg) | Inverse alphabet1..199. 1=e,10=a,20=q,21=b,22=t,24=c. | Same visible family as277/284; not255. |
| [276 / 0067](276-0067.jpg) | Small numerical nomenclator, Hand von Klaute. Denmark22; King of Denmark46; Alliance54. | Different country numbering; no alphabet shown. |
| [277 / 0069](277-0069.jpg) | Inverse alphabet1..199. 1=e,10=a,20=q,21=b,22=t,24=c. | Same visible family as275/284; not255. |
| [278 / 0073](278-0073.jpg) | Inverse alphabet1..213. 1=z,20=f,21=e,22=d,23=c,24=b,25=a. | Alphabet differs. |
| [279 / 0076](279-0076.jpg) | Alphabet and French dictionary. A36/63/90/99; B35/62/89; alphabet reverses. | Alphabet differs. |
| [280 / 0079](280-0079.jpg) | Nomenclator with multiple codes per word. Armee597..600; Alliance583/584; Dänemark532/533; King of Denmark534/535. | Different country numbering; no alphabet shown. |
| [281 / 0088](281-0088.jpg) | Chiffre pour M. C. M. B. de Kettler: alphabet and names. a17,b18,c19,d20; Dennemarck463/464/465. | Alphabet and country codes differ; same family as282. |
| [282 / 0091](282-0091.jpg) | Kettler encoding/decoding alphabet. a17,b18,c19,d20; extended homophone table. | Same family as281, differs from255. |
| [283 / 0095](283-0095.jpg) | Chiffre de M. Kl.: multi-code nomenclator. Dennemarck209/423; Schweden202/416; Alliance236/440. | Different country numbering; no alphabet shown. |
| [284 / 0097](284-0097.jpg) | Inverse alphabet1..199. 1=e,10=a,20=q,21=b,22=t,24=c. | Same visible family as275/277; not255. |
| [285 / 0099](285-0099.jpg) | Postscript adding words and correcting a letter-code error. Versailles608/619, Marly609/620, Fontainebleau610/621; note k should have3 rather than13. | The correction gives3=k, incompatible with unchanged255 (3 is null; k29/39/49/59/69/MM). Arbitrary reuse of word entries remains untested. |
| [286 / 0100](286-0100.jpg) | Postscript about duplicated code assignments. King of Denmark547; king of Sweden542; Roman emperor544. | Different country numbering. No alphabet shown. |
| [287 / 0104](287-0104.jpg) | Chiffre pour M. D. M.: multi-code nomenclator. Alliance222/373; king in Prussia200/351/500. | No target country anchors or alphabet on supplied page; no positive255 feature. |
| [288 / 0114](288-0114.jpg) | Fragment of large French syllable/name table. Holstein388; partial syllables and dictionary; no full alphabet. | Same visible family/layout content as271; not a targetHolstein634 match. |

## Bounded check of the285 addendum

The original note clearly corrects the value of **k from13 to3**: the relevant phrase reads `buchstaben K ... nicht13 sondern3 stehen soll`. See the [original-pixel comparison sheet](285-k-correction-comparison.png). This supplies a direct alphabet comparison even though no base table is attached: unchanged255 has **3=null**, while **k=29/39/49/59/69/MM** (checked against the existing target mapping in `../reproduce_current.py`). The addendum therefore does not belong to an unchanged255 alphabet.

The supplied tables275/277/284 visibly also have3=k. That shared mapping is compatible with their family, but does not establish that285 belongs to it without provenance. Nothing here excludes arbitrary later reuse of some word-list entries; it excludes the unchanged alphabet only. The note is not evidence for PP/BB or II/55 corrections in494.

Root additionally inspected285 in the live UI: no date, users unknown, categoryOther, structureVfn, Description empty, oneAttachment0099, HasInstructionsNo. These metadata were relayed by root, not independently observed by this helper. There is no second gallery page to inspect for this record.

Record287 also lacks the alphabet and target-country entries on its supplied page, but has no positive255 feature and belongs to a nomenclator naming a king in Prussia. Its chronology is not inferred as confirmed metadata here. No continuation request is justified solely by its three-digit codes.

Tables275/277/284 visibly share a numerical-letter mapping;281/282 share the Kettler alphabet;271/288 share syllable/name content. These22 records must not be counted as22 independent keys. No physical-sheet deduplication against Daniel’s previous collection has been performed.

The601Denmark/634Holstein/768Sweden meanings remain fallible annotation-derived screening anchors. Alphabet mismatch is recorded independently. No source images, shared SOLUTION/NOTES, markers or goal status were modified.
