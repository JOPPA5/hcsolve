# Work log

2026-10-12: Selected through the Jolanka name filter in the rendered catalog, status Not solved. All three tabs read, both scans archived unchanged. Testing the alphabet established on HCP1301/1243 against these independent cards.

2026-10-12: Applied the HCP1301/1243 graphic key to the main text and inspected the stamp and both source sides. Saved the partial Hungarian reading and English translation in SOLUTION.md and work/reading.json. The phrase after the question, the venue/name after “mulatság”, the middle anecdote (including possible literal digits), and most of the stamp text remain unresolved. A tentative “33 times married” reading was rejected as insufficiently grounded. The small annotation near the address also remains unread. This is a selected continuous reading with gaps, not a complete diplomatic transcript.

2026-10-12 second source-reading pass: The small address annotation is now read as szeretettel. The anecdote really has a sequence resembling literal 33 followed by szor and nősültem; its literal reading is retained as a qualified, possibly joking statement, not rejected solely for odd meaning. The number, the venue after mulatság, and an adjacent clause still need confirmation. The stamp remains unresolved: applying the key yields apparently contradictory fragments. The English explicitly does not invent a coherent love poem to hide that contradiction. No complete decipherment claim.

2026-10-13: The opening question resolves to mulatott tegnap. The following source rows yield remé-lemint rendesen most; the normalized mint supplies m across the word boundary, with that restoration marked. This is a direct reading from top.png, not a quotation.

2026-10-13: The old unresolved venue after mulatság was a mistaken expectation: middle-detail.png reads és pedig szüreti de még. Szüreti describes a harvest dance; it is not a place name. The adjacent fogot… phrase and stamp verse remain unresolved.

2026-10-13: Fourth pass: all seven stamp rows now have a direct shape ledger. The connector in S5 is deliberately UNKNOWN UNKNOWN: de and ha remain competing readings. A conditional rhetorical-question interpretation would remove the former semantic contradiction, but coherence alone does not decide the glyphs. The raw szivelelek is only tentatively related to szívellek; no silently repaired love poem is claimed. A focused web search found no matching source verse. The main-text middle fragment and stamp wording still prevent a complete decipherment claim.

2026-10-13 fifth pass: stamp-connector-pass5.png isolates red ink at two thresholds. The connector still cannot be safely chosen as ha instead of de. The third apparent bar may be genuine; do not select ha solely to repair the meaning. No new solved claim.

2026-10-14, sixth pass: Material breakthrough under the stamp. A search for "kit szeretnék" "téged" found Petőfi's Honfidal; the entire short poem was read at MagyarÍrók.hu and its first stanza corroborated in an indexed MEK edition (direct MEK retrieval failed). This is an external literary parallel, not a published card solution. The unchanged S01–S03 sequence is tiedvagy/okesziv/elelek, hence Tiéd vagyok, e szív, e lélek. The old és [s]zívelelek / szívellek hypothesis was an incorrect segmentation, now withdrawn. The preferred whole stamp is an adapted stanza, with ha still graphically qualified and sze[re]tnélek explicitly restoring two absent characters. Reinspection changed S07 from the earlier mistaken F T sequence to T N, yielding szetnelek. A crop of S05 shows two substantial red bars and a small lower mark, so a/e uncertainty remains rather than being removed by the poem.

2026-10-14: Added the full 22-row main ledger, seven stamp rows and one annotation row. Old excerpts and pre-pass JSON retained. A15/A16 currently yields ...csake{h|p}enufogy{i|o?}t / meazt... . Earlier unqualified úgy cannot be justified by the observed character sequence and has been removed from the editorial reading. Tested fogott meg, fogyott and fojt meg; each needs unsupported sign changes or additions. The gap remains. Source-spelling differences (egésségban, ilet, rosz(u), tanczolni, azal) are now visible in the literal ledger instead of hidden by fluent editorial prose. Still partial; no completion marker or register entry.

2026-10-14 annotation audit: the old szeretet[t]el display underreported restoration. Literal N01 is sze{r|t?}etel, so szeretettel requires additional letters as well as doubling. The claim now labels the whole word an editorial restoration and prints its literal reading. A T reading would share the missing re pattern of the stamp, but that possible error pattern is not treated as independent confirmation.

2026-10-14 seventh pass: fresh same-scale source comparison supports A15 f and joined gy; final loop i/o still uncertain. Ten manually proposed phrases were audited for character changes with compare-gap.py; none accepted. This is negative evidence, not a new decipherment. Portal rechecked in rendered UI: Not solved. Opened address viewer reports natural size 1024x657 and the same media/3715/...adr-large.jpg already archived. No higher-resolution control visible. Searches for the card label produced no relevant transcription. Linked HistoCrypt article abstract read; PDF retrieval failed twice. Working text remains unchanged and partial. No source modification, completion marker, external submission, commit or push.

2026-10-14 after 1213/1217 reviews: reconsidered the main A15/A16 gap in light of missed line-ending signs found on 1213. The saved comparison includes the full overflow to x526 and the next-row prefix; no additional omitted edge signs were identified in this check. The f and joined gy shapes remain supported by same-card controls. No new plaintext or completed-solution claim.

2026-10-14: Completed the first-review package and five-page English report, preserving Hungarian text and all stated uncertainties. Full source image, 30-row manual ledger, same-card shape comparisons and rejected conjectures are available. This is explicitly a partial-decipherment handoff, not a claim that A15/A16 is solved. Review priorities: whole-card transcription, A15/A16, S05/S07, N01, A17 digits. PDF rendered and inspected, source hashes unchanged, literal decoder output matched. No FINAL/register entry, watcher, external submission, commit or push. DONE1 is the last write for handoff.


## Review 1 response, 2026-10-14

Reviewer: Claude Opus 5.5; verdict REVISE, 2026-10-14. The reviewer first supplied the successful A15 reading; the solver then inspected the review crops against the archived scan. This is a substantive correction, so the complete claim is submitted as DONE2, not FINAL.

1. A15 accepted: two bars after csak are A, and the diagonal cross has the extra bar of Z. The pale ending supports O GY O T. The corrected literal sequence is csaka{h|p}enzfogyot, interpreted as csak a pénz fogyot[t]. Earlier segmentation and pass-7 conjectures were wrong; they remain only in historical notes and snapshots.
2. A16 accepted: visible me is retained in the ledger; Me[g] is an explicitly restored connective, not a particle joined to the preceding verb.
3. A17 accepted: both shapes are numeral 3. The ledger now preserves 33 literally. The English quotation marks around “married” signal the unusual statement; no particular harvest-ball custom is asserted as established history.
4. S05 accepted as two bars, hence ha te-. S07 remains literal szetnelek; the editorial sze[re]tnélek discloses the missing letters.
5. N01 corrected by adding the overlooked E T group. Literal sze{r|t?}etetel supports szeretet[t]el if the uncertain sign is r. The earlier claim that more than a doubled t must be restored is withdrawn. Watermark interference and the approximate sign count remain disclosed.
6. A03 corrected to egésségben; A21 corrected to ezel, editorial Ez[z]el. Both changes follow the bar counts in the source strips.
7. “First Sunday” is retained literally. The reason it occupied the writer is unknown; a duty-day interpretation suggested by the reviewer is possible but not established by this card.
8. The English report has been rebuilt for the corrected claim. The standing user instruction not to start watchers remains in force. All archived source files, review files and previous markers are preserved.

The prior pass-7 candidate audit used a misclassified Z and wrong segmentation. Its rankings are obsolete evidence of failed attempts, not remaining live alternatives. Snapshot: work/done1-snapshot.


## Response to review 2

Review 2 by Claude Opus 5.5, dated 2026-10-14, returned ACCEPT. All eight findings from review 1 are addressed; no blocking issues remain. The accepted plaintext and literal ledger are unchanged in this final edition.

1. Attribution: the solver established the key transfer and main transcription; the reviewer first supplied A15, “csak a pénz fogyott”. The solver’s subsequent inspection was informed by that reading, not a second independent discovery. This division of work is stated in the register entry.
2. The number 33 remains a literal reading. The English quotation marks around “married” and the explicit uncertainty about the event are retained. No harvest-ball explanation has been promoted to fact.
3. The small N01 annotation remains qualified because of its r/t ambiguity and uncertain sign count under the watermark. Accents and the postmark day remain subject to the already stated limits.

The English PDF has been updated to record acceptance. A local register entry is prepared with solver TODO because no personal name was supplied. Neither the register entry nor the report has been published by this finalization. FINAL records completion of this repository’s review workflow; it does not claim that the portal status has changed.
