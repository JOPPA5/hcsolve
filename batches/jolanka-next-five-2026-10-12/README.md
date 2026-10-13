# Five additional Jolánka postcards

Date: 2026-10-12. Branch: main. No commit or push.

The user requested English translations, skipping the remaining old cases, and work on at least five further HC Portal records. HCP1301 and HCP1243 now have English translations, preserving Hungarian originals. HCP917 and HCP1000 were explicitly skipped; HCP975 was already publicly solved.

All five records below were selected from the rendered Jolanka catalog and visibly marked **Not solved**. All three detail tabs and both image sides were inspected. Ten original images were archived; metadata and attachment hashes are in each cipher directory. Second-pass outcome: **1217 is a complete semantic solver reading with localized scribal uncertainties; three cards remain partial**. HCP1243’s separate prior review requirements have now been addressed.

| Record | Result | Remaining obstacle |
|---|---|---|
| [1218](../../ciphers/hcp-1218/SOLUTION.md) | Main column transcribed; stamp identified as an adapted Petőfi Honfidal stanza | One main clause; stamp connector/restored letters; small annotation |
| [1217](../../ciphers/hcp-1217/SOLUTION.md) | Complete semantic reading of 19 main rows and eight stamp rows; direct shape ledger and English PDF | Scribal utra / ki / eze forms preserved; full-card independent review not claimed |
| [1216](../../ciphers/hcp-1216/SOLUTION.md) | Expanded travel/passing-Györk passage; complete stamp greeting signed Feri | Wednesday-post clause, preceding Györk wording, footer |
| [1213](../../ciphers/hcp-1213/SOLUTION.md) | Easter, Szentmihály, later sprinkling, walking at night, wanting to be closer; stamp greeting | Easter wording, accommodation word, promise and footer; signature |
| [1212](../../ciphers/hcp-1212/SOLUTION.md) | Thanks for her letter, love verse, dinner; bottom sign-off signed Feri | Verse variants, dinner clause and small address annotation |

## Prior-solution audit

On the work date, the live [AI Decipherment Register](https://ai.hcportal.eu/register/) displayed 37 contributions. Searching all fields for `jolanka` gave “No matching contributions” and “0 contributions shown”. Two exact-name web searches for the five Jolanka suffixes found no relevant solution. Portal attachments contained no transcript or solution. This limited search is not proof of worldwide novelty; no external plaintext was used in the new readings.

## Evidence and reproduction

Each `SOLUTION.md` contains a Hungarian editorial reading, English translation, key and explicit gaps. `work/reading.json` stores the manual claim with source hashes. `work/source-comparison.html` puts it beside the original address-side scan. 1217 additionally has a full direct shape transcript, with its uncertainties retained.

```sh
python3 batches/jolanka-next-five-2026-10-12/check_readings.py
```

This checks source integrity and displays the saved manual text. It does not independently decrypt the scans. The first-pass command still only displays saved readings. HCP1217 and HCP1213 now have solver completion markers; no FINAL or register entry is claimed for the five new cards.

Second pass added `visual-ledgers/decode.py`: direct shape transcripts for all 18 HCP1243 rows and all 27 HCP1217 rows, plus explicitly limited excerpt ledgers for the other four cards. The decoder preserves near-homographs and blots. These ledgers were entered visually after earlier plaintext hypotheses were known; no blind reading or automatic OCR is claimed.

HCP1243: review findings addressed, final English PDF and local register entry prepared. The uncertain cursive signature remains explicitly outside the cipher claim. HCP1217: solver-complete documentary package, without claiming a new full-card independent review. Neither entry has been submitted online, and nothing has been pushed.

Remaining work: HCP1218 stamp and middle anecdote; HCP1216 opening gaps and exact travel wording; HCP1213 remaining Easter phrases and footer; HCP1212 verse clause, dinner question and small address annotation. Source detail crops and earlier readings are retained.

## Third pass — 2026-10-13

HCP1213: the relocation sentence now specifies moving into Pest by the first of May (source Pest, editorial Pest[re]). HCP1216: the waiting-for-the-Messiah simile and overcoming sorrow are now read. HCP1218: tegnap, [m]int rendesen and szüreti clarify the greeting and identify a harvest dance. HCP1212: the witness line refers to the creator of the universe, but literal alkoté remains qualified. Selected source rows were added as direct shape tokens; none of these excerpt ledgers covers its full card. All four stay partial, without DONE or register entries. The portal viewer exposed the same 1024-pixel scan, so zooming yielded no additional source detail. Earlier claims remain archived as reading-pass2.json.

## Fourth pass — 2026-10-13

HCP1213 is now a solver-complete semantic edition: all 27 main rows and seven stamp rows transcribed, closing imádja Feri and promise nekünk édesem resolved, local word-ending/signature ambiguities preserved. DONE1 and a visually checked three-page English PDF exist; independent acceptance is not claimed. HCP1216 now has full spatial transcription including Vámosgyörk and the right-edge farewell, but two opening phrases remain uncertain. HCP1212 has a complete main-text ledger but still lacks its dinner word and tiny annotation. HCP1218 has a full stamp ledger; ha versus de remains an unresolved reading, so a plausible rhetorical question is only a hypothesis. These three retain partial status and no new register entries.

## Fifth pass — 2026-10-13

HCP1212: ad vissza resolves the dinner phrase by correcting the glyph segmentation. Main text now deciphered with disclosed spelling variants; a four-page English working PDF is rendered and inspected. The tiny address annotation remains unresolved, so no DONE/FINAL or register entry. HCP1216: de higyje el is a new candidate for the opening, recorded in work/opening-candidates-pass5.md but not promoted to established text. HCP1218: threshold inspection does not decide de/ha; the rhetorical reading remains hypothetical. Source hashes for all 15 archived files are unchanged. No new review markers for 1213/1217 were present at the beginning of this pass.

## 2026-10-14 — HCP1218 sixth pass

Full spatial transcription now covers 22 main rows, seven stamp rows and the address annotation. An external literary search identified the stamp as an adaptation of Petőfi’s Honfidal: e szív, e lélek resolves the old szívelelek word-boundary error without changing the underlying letters. The connector ha remains graphically qualified and sze[re]tnélek explicitly restores absent letters. One main-text clause remains undeciphered; 1218 stays partial with no DONE/FINAL or register entry. See its updated SOLUTION.md for source attribution and literal evidence.

## 2026-10-14 — returned reviews addressed

HCP1217: corrected rows 9/10/13/17 and both-language reading; reviewer accepted closure without another round after these corrections. Four-page English report checked; local register entry with solver TODO; FINAL prepared. HCP1213: completed row 11, corrected telt el and kis lakás, recorded the row-8 caret and other source details; four-page English report checked; DONE2 prepared for the requested short second round, no FINAL/register entry. HCP1218 remains partial; an edge-sign recheck did not resolve A15/A16. No commit, push, watcher, or external submission.

## 2026-10-14 — 1213 accepted; 1218 partial claim handed off

HCP1213 received ACCEPT in REVIEW2 and is FINAL, with a five-page English final report and a local register entry (solver TODO). HCP1218 has a five-page English first-review report and DONE1 as an explicitly partial-claim handoff: one substantive main-text clause remains unresolved, along with qualified local signs. It is not solved/FINAL and has no register entry. The reviewer is asked to inspect the problematic sequence independently. No push or external submission.
