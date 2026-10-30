# HCP 1530 solver notes — 2026-10-28

Assigned HCP1530/pc_hcp_211 only. Read repository README in full. Root specifically retains watcher/marker/review/PDF/register duties; this collaborator writes only this cipher and its batch summary. Source files were supplied immutable and not downloaded or modified here. No published target plaintext was supplied.

## Procedure and retained evidence

1. Viewed both originals. Rotating picture.jpg 90° counterclockwise gives an upright 674×1024 body; the five top margin rows are still upside down. Crop [28,35,642,195], then rotate this crop 180°, to read the five top rows. The main nine rows lie at upright y675–991. Read T01–T05 followed by B01–B09: TAKE JA continues VZPOMINAM. The date is ordinary 14.XI.1903. Address has no cipher body.
2. Applied the key supplied at start from HCP1520/HCP1527; no independent key discovery. Manual visual transcription is in work/transcription.json. Indexed row controls and positively read ordinal inventory are retained. No OCR, blind held-out test or independent provider review was used.
3. Generated unfiltered pixel crops with work/make-controls.py. Their exact original-picture boxes and transforms are in work/focused-controls.json. Enlarged composites are for convenience; raw *-original.png files preserve the source crop pixels after lossless transpose. An early T01 contrast image was tried but did not establish hidden strokes. Enhanced contrast is not used as proof.
4. Root provided collaborative pixel QA of the uncertain areas. Root agreed PSANKO and NYNEJSI were not secure in the dark print, agreed ordinary Issajův was a plausible reading, and cautioned about URADE. This is second solver inspection, not independent review or a published target plaintext seed.

## Failed and corrected drafts

- Initial quick visual notes misread ZDE as KDE and ZDRZEL as KDYZEL. Closer comparison of the q/Z form corrected these before the record was finalized. No such false forms remain in the plaintext.
- Context suggests top PSANKO, B04 NYNEJSI, final JEDINEMU and B08 URADE. They were tempting full-word drafts, but the relevant dark strokes do not warrant complete transcription. Final record retains U1/U2/U3/U4 and does not count the unknown span lengths. JE and final MU are read on the two sides of U3; URA is read before U4.
- B07 has a shallow v-like singleton in RUDOL?INE. The previously tentative v/F from HCP1526 is not a generic validated mapping. F is linguistically attractive here, but is withheld as UF. Tall f/V elsewhere on this card is a different visible form. No F key entry was added at that stage; see the later reference transfer below.
- Ordinary title could be associated contextually with a musician, but no primary external historical evidence was consulted and no identification is claimed. Literal tentative paleography Issajův is retained outside cipher counts.
- The source reads KTERE ... PRISLO ... NEVHOD. No KTERA, PRISLA or NEVHODNE repairs were inserted. NEVHOD is six known cipher units and is retained even if unusual.

## Verification and limits

The read-only default command verifies three immutable target source hashes, two reference hashes, three record hashes, 14 indexed rows, 445 known cipher units, six CH units/451 known base letters, known-key inverse round trip and exact preservation of four unresolved dark spans. The complete count/coverage percentage is unknown because span lengths are not defensible. The round trip validates consistency of the manual record and does not independently validate source readings. Ordinary writing, punctuation and word spacing are not counted as cipher units. No extra canceled-unit inventory is claimed where retracing cannot be separated.

No markers, watcher, reviewer launch, PDF, register entry, git operation, submission or external message was made by this collaborator. Root performs final source/manifests checks and handover.

## Root initial check — before later F transfer

Root inspected both originals, the complete upright top and bottom blocks, all five focused unknown regions and local CH/V/title controls on 2026-10-28. Dark PSANKO/NYNEJSI/URADE completions were not accepted as literal readings; U1, U2 and U4 remain. The shallow v in RUDOL[UF]INE is a contextual F candidate, with the uncertainty preserved. Ordinary Issajův remains a tentative cursive reading without historical performer identification. The updated read-only command passed three original hashes, three record hashes, all 444 assigned units, six CH expansions and tokenwise checks. Full denominator remains unknown. This is a second solver check of a partial manual record, not independent provider review. No marker created.

## Later targeted reference comparison (same date)

Root supplied exact card199/HCP1518 original source photo cited by the published partial study. Viewed both that original and the four-way unfiltered comparison. The short open v form in reference h2t38v4m6/proposed RUDOLFINA visually matches the target h2t38v4m5. Adopted v/F as later known published-reference transfer, explicitly after initial contextual F inference; no independent key discovery or expert validation claim. Work key/record/positions/decoder now include one v/F. Counts become 445 assigned units, six CH expansions, 451 known letters; U1/U2/U3/U4 unchanged. Original UF crop name remains as historical trace. The reference photo and published key text are hashed in work/reference-sha256.json and checked by read-only decoder. Other cipher directories and shared reference files were only read, not modified.

Root verified later photographed-reference F transfer and updated read-only decoder:445 assigned units/451 letters, four dark spans unchanged. All target/reference/record hashes pass. Still PARTIAL without markers.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
x5 crops: U1 8..5g -> LISTEK (not PSANKO); U2 m1m57c4 NYNEJSI; U3 JEDINEMU;
U4 2h6t5 URADE. Flagged DRAHE vs th6r1 (DRAHY) for reviewer. Register
re-checked (357, 1530 absent). Watcher + DONE1.
