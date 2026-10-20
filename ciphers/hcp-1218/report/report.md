# HCP1218 - Sunday and a masons’ dance

**Status: accepted in independent review 2; complete main-message decipherment. Final edition, 2026-10-14.** Local glyph and editorial uncertainties remain disclosed below.

## Source and method

The [HC Portal record](https://crypto.hcportal.eu/dashboard/cryptograms/1218), jolanka106, is dated September 1912 and addressed to Tóth Jolánka at Jászárokszállás. It displayed Not solved at capture on 2026-10-12 and on reinspection on 2026-10-14. Both postcard sides and metadata are archived unchanged. No published solution was located in the recorded searches; this is not proof that none exists.

The cipher is a Hungarian graphic monoalphabetic substitution. The key transferred from HCP1301/HCP1243 was tested across all 22 main rows, seven stamp rows and the address annotation. Transcription is manual, with earlier hypotheses known, not blind transcription or OCR. Independent review 1 resolved the last unread clause as “csak a pénz fogyott” (“only the money ran out”). The solver adopted this after inspecting the actual signs.

Spacing, punctuation and most accents are editorial. Brackets show significant supplied letters. Source spellings such as egésségben and tánczolni are retained. The literal ledger takes precedence for exact character claims; Hungarian normalization and English translation are interpretive editions.

## Hungarian editorial reading

Kedves édes Jolánkám! Kívánom, hogy a legjob[b] kedvében és egésségben találja soraim. Édesem, hogy mulatott tegnap? Remélem, [m]int rendesen, most is jól telt el a vasárnap. Ami engem il[l]et, én el voltam foglalva, mert első vasárnap volt, este pedig a kőműves mulatság volt, és pedig szüreti, de még ilyen ro[s]szu[l] nem mulattam soha, csak a pénz fogyot[t]. Me[g] azt az egyet megjegyzem, hogy 33-szor nősültem meg négy leán[n]yal. Tánczolni egyáltalán nem tánczoltam. Mikor megy Berénybe? Ez[z]el bezárom soraim, sorait várva.

Small annotation by the address: szeretet[t]el? (r/t and precise sign count uncertain; literal sze{r|t?}etetel).

Under the stamp, source-assisted editorial reading: Tiéd vagyok, e szív, e lélek; kit szeretnék, ha téged nem sze[re]tnélek?

## English translation

My dear, sweet Jolánka! I hope my lines find you in the best of spirits and in good health. My darling, how did you enjoy yourself yesterday? I hope that, as usual, Sunday went well again. As for me, I was busy, because it was the first Sunday; in the evening there was a masons’ dance, specifically a harvest dance, but I have never enjoyed myself so little, only the money ran out. And one more thing I note: I “married” 33 times with four girls. I did not dance at all. When are you going to Berény? With that I close my lines, awaiting yours.

Small annotation by the address: [with love?].

Under the stamp, source-assisted translation: I am yours, this heart, this soul; whom would I love if I did not love you?

## Identification of the stamp verse

After decoding the phrases, the solver identified Sándor Petőfi’s Honfidal through its [published text](https://www.magyarirok.hu/petofi-sandor/h/honfidal). The public-domain poem opens: “Tied vagyok, tied, hazám! / E szív, e lélek; / Kit szeretnék, ha tégedet / Nem szeretnélek?” This literary source assisted interpretation; it is not a published solution of this postcard.

The card adapts the stanza to a personal addressee, omitting tied, hazám and using téged instead of tégedet. The unchanged S02/S03 letters divide as the end of vagyok followed by e szív, e lélek. S05 now reads ha by its two-bar sign as well as by context. S07 has no visible re: sze[re]tnélek restores the intended verb, with a copying or enciphering slip as an interpretation. The card is not silently replaced by the printed poem.

## Remaining uncertainty and historical interpretation

No unread main-text clause remains. A02 retains a blot restored contextually to m. Most accents, word boundaries and punctuation are editorial. Missing consonants and A16 Me[g] are bracketed in the Hungarian edition. Shared h/p shapes are resolved by context. N01 has uncertain r/t and a sign count uncertain by about one; preferred szeretet[t]el (with love) remains qualified. Stamp S07 literally reads szetnelek: sze[re]tnélek supplies re using the identified Honfidal parallel. The written number is 33; whether the marriages are literal is not established. The day of the postmark is unread. Round 2 accepted the solution with these disclosed limitations.

Berény is interpreted as Jászberény, consistent with the related correspondence. The postmark month agrees with September, but its day cannot be read. The postcard describes yesterday as Sunday and calls it the first Sunday. September 1, 1912 was a Sunday, making September 2 a plausible writing date; this is a calendar inference, not a recovered postmark date. The report makes no factual claim about the reason for the writer’s first-Sunday duties or the nature of the 33 “marriages”.

## Working key


At this scan resolution h/p are near-homographs and sometimes require linguistic context; d/n can also differ only by stroke length. The shape names below describe tendencies, not a guaranteed visual classifier. This qualification follows the independent HCP1301 review that arrived during this batch.

| Named graphic class | Letter |
|---|---|
| two-bars | a |
| six | b |
| left-bowl | c |
| joined-two-strokes | d |
| three-bars | e |
| cross | f |
| open-loop-descender | g |
| two-tall-strokes | h |
| dotted-crossed-curve | i |
| inverted-T | j |
| section-mark | k |
| wave | l |
| three-short-strokes | m |
| two-short-strokes | n |
| cursive-loop | o |
| tall-short-stroke | p |
| F | r |
| right-bowl | s |
| gamma | t |
| x | u |
| chevron | v |
| low-descender | y |
| crossed-diagonal | z |
| two-bars:acute | á |
| three-bars:acute | é |
| dotted-crossed-curve:acute | í |
| cursive-loop:acute | ó |
| cursive-loop:diaeresis | ö |
| cursive-loop:double-acute | ő |
| x:acute | ú |
| x:diaeresis | ü |
| x:double-acute | ű |



Numerals are copied as numerals: DIGIT3 maps to 3. CS and GY denote joined signs for cs and gy. The literal H class deliberately preserves h/p ambiguity; contextual readings do not manufacture distinct glyphs.

## Reproduction and evidence boundary

Run from the repository root:

```sh
python3 batches/jolanka-next-five-2026-10-12/visual-ledgers/decode.py 1218
```

This single command verifies the archived address-image hash and decodes the complete manually observed ledger to literal row text. It does not perform OCR or independently prove the transcription. The ledger, its provenance and output are work/as-seen.txt, work/as-seen-provenance.json and work/as-seen-decoded.txt. The editorial Hungarian and English readings are also stored in work/reading.json. The source-bound check_readings.py 1218 command checks all three archived hashes and prints that editorial claim.

Review 1 independently read the full card. Its corrected A15 sequence fits the unchanged key, the source marks and the sentence context. The successful reading replaces the previous open clause without introducing an unobserved word. All 30 spatial rows are represented; complete message recovery does not eliminate the local uncertainties above. The reviewed partial edition is preserved in work/done1-snapshot, with earlier unsuccessful attempts in NOTES.md and numbered work files.

## Response to review 1

Reviewer: Claude Opus 5.5; verdict REVISE, 2026-10-14. The reviewer first supplied the successful A15 reading; the solver then inspected the review crops against the archived scan. This is a substantive correction, so the complete claim is submitted as DONE2, not FINAL.

1. A15 accepted: two bars after csak are A, and the diagonal cross has the extra bar of Z. The pale ending supports O GY O T. The corrected literal sequence is csaka{h|p}enzfogyot, interpreted as csak a pénz fogyot[t]. Earlier segmentation and pass-7 conjectures were wrong; they remain only in historical notes and snapshots.
2. A16 accepted: visible me is retained in the ledger; Me[g] is an explicitly restored connective, not a particle joined to the preceding verb.
3. A17 accepted: both shapes are numeral 3. The ledger now preserves 33 literally. The English quotation marks around “married” signal the unusual statement; no particular harvest-ball custom is asserted as established history.
4. S05 accepted as two bars, hence ha te-. S07 remains literal szetnelek; the editorial sze[re]tnélek discloses the missing letters.
5. N01 corrected by adding the overlooked E T group. Literal sze{r|t?}etetel supports szeretet[t]el if the uncertain sign is r. The earlier claim that more than a doubled t must be restored is withdrawn. Watermark interference and the approximate sign count remain disclosed.
6. A03 corrected to egésségben; A21 corrected to ezel, editorial Ez[z]el. Both changes follow the bar counts in the source strips.
7. “First Sunday” is retained literally. The reason it occupied the writer is unknown; a duty-day interpretation suggested by the reviewer is possible but not established by this card.
8. The English report has been rebuilt for the corrected claim. The standing user instruction not to start watchers remains in force. All archived source files, review files and previous markers are preserved.

## Response to review 2

Review 2 by Claude Opus 5.5, dated 2026-10-14, returned ACCEPT. All eight findings from review 1 are addressed; no blocking issues remain. The accepted plaintext and literal ledger are unchanged in this final edition.

1. Attribution: the solver established the key transfer and main transcription; the reviewer first supplied A15, “csak a pénz fogyott”. The solver’s subsequent inspection was informed by that reading, not a second independent discovery. This division of work is stated in the register entry.
2. The number 33 remains a literal reading. The English quotation marks around “married” and the explicit uncertainty about the event are retained. No harvest-ball explanation has been promoted to fact.
3. The small N01 annotation remains qualified because of its r/t ambiguity and uncertain sign count under the watermark. Accents and the postmark day remain subject to the already stated limits.

The English PDF has been updated to record acceptance. The register entry names Tomáš Pavuk as the solver. Neither the register entry nor the report has been published by this finalization. FINAL records completion of this repository’s review workflow; it does not claim that the portal status has changed.

## Archived source provenance

# HCP1218 sources

Captured 2026-10-12 through the rendered portal General, Description and Attachments tabs. Status: **Not solved**.

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1218

- picture.jpg: https://api.hcportal.eu/media/3714/conversions/cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-106_pic-large.jpg ; SHA256 b410f5ba3bbbc8635c03cb95a62b814db97d124cc4173ead659e6e87dfc72083
- address.jpg: https://api.hcportal.eu/media/3715/conversions/cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-106_adr-large.jpg ; SHA256 eb2a636aacf1484429f3fb50d2381c9aa4d1df230bdc3e82c4b70e13632eb0df

## Literary parallel discovered 2026-10-14

- Sándor Petőfi, **Honfidal** (Debrecen, January–February 1844), rendered poem: https://www.magyarirok.hu/petofi-sandor/h/honfidal . Read on 2026-10-14, specifically the first stanza. Search discovery query: `"kit szeretnék" "téged"`. The source explains the stamp's word boundaries and supplies a preferred conditional reconstruction. This is a published poem, **not a published solution of HCP1218**. The adapted card omits words and has uncertain/dropped letters; SOLUTION.md distinguishes them.
- Corroborating library search result: *Petőfi Sándor összes költeményei*, https://mek.oszk.hu/09400/09496/html/ . Search indexed the same stanza under Honfidal; direct page retrieval returned 502, so the successfully opened poem above is the cited reading source.

Original files in source/ were not altered or extended during this pass. New literary evidence is recorded here and in the solver documents.

## Follow-up checks, 2026-10-14

Rendered HC Portal General/Attachments and the full address viewer were revisited: status Not solved; the displayed address media URL is unchanged and its natural dimensions are 1024 × 657. No higher-resolution download control was visible. The linked article abstract at https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 was read; the linked PDF https://ecp.ep.liu.se/index.php/histocrypt/article/download/166/122/65 failed to load in the web reader. No plaintext or card-specific detail was taken from that abstract.
