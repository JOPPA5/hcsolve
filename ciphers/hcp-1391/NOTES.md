# HCP 1391 solver notes — 2026-10-26

Root captured all three rendered tabs and the original scans. I read README in full, verified there is no DONE/FINAL marker and no exact `1391` line in skip.txt, and personally inspected both source images. Original files were not changed. The picture caption reads “River Stour & Bridge, Blandford.” Address-side message needs a 270-degree clockwise rotation. The postal address appears to begin Mr W. Abbott, consistent with the collection context, but the full address is not a cryptanalytic claim.

The supplied Caesar −1 prior was checked against visible ink: `Nz Pxo Efbsftu / Nboz uibolt gps` gives `My Own Dearest / Many thanks for`. These two lines contain 25 letters, not a complete message. Five lower lines are faded and crossed by the watermark. Tempting contextual expansions (a sweet postcard, an affectionate closing) are not frozen as observations.

Tried rotated original, a 3× crop, and independent red/green/blue channel autocontrast/contrast/sharpness copies. They improve contrast but do not recover erased or covered strokes. The lower first word may be `Txffu` (SWEET), a later row may begin `Ibwf` (HAVE), and the last row seems to start `Pxo` (OWN); all three remain hypotheses, excluded from verified counts. Several lower apparent letters are only fragments, so I have not represented them as a complete fixed-length transcript.

The date header includes May and 07; portal metadata gives 1907-05-11. No date-based repair of encrypted letters is made. The terminal hatch/monogram is retained only in the source image, not interpreted as letters.

No watcher/reviewer was started, per persistent user override. No DONE marker: this is a partial reading and requires further image-supported transcription.

## 2026-10-29 — Claude Opus 5.5 (solver), continuation of GPT work above

Re-inspected `work/message-large.jpg` with new autocontrast crops at 2-3x (`work/crops/l1..l8*.png`, `sig.png`, `l7m.png`). Compared with the sister cards of the same C. H. -> W. Abbott family (hcp-1386, 1390, 1397, 1398, 1399, 1403; Caesar -1). Message has seven lines under the date line "Cg. H. May 11 .. 07" (plain).

Newly frozen (clear on pixels, all decode under Caesar -1): line 3 last word `pomz` = ONLY; line 4 first word `Ibwf` = HAVE; line 6 `gspn Zpvs` = FROM YOUR; line 7 first word `Pxo` = OWN. Total frozen 44 letters.

Still unread (why it stops): the scan is only 1024 px wide, so each letter is ~10 px; lines 3-5 lie under the grey postmark ring/watermark and the right half of lines 4-7 is faded ink.
- Line 3 start: `dvs?:` / `dbs?:` (CARD? CUR?) — third/fourth letter not decidable; then a two-letter group `?p.` and a stroke that may be `J` (I) before `pomz`. "...I only / have ..." is suggested (cf. hcp-1398 "I only have this view in my album") but not read.
- Line 4 after `Ibwf`: `uij?` (THI?, perhaps `uijt` THIS), then a group with p + o/5-like + long descender (`pof` ONE?), faint tail. Hypotheses only.
- Line 5: `?oe.` (first letter t/U/b-like; `boe` AND fits but the first sign is not b-shaped on pixels) and `Ibs?` (HAR?); faint tail with dots.
- Line 6 start: M + x/y-like + Z/c-like marks before `gspn` — the same unresolved "M ××" closing group as hcp-1390.
- Line 7: `M` + raised h-like letter + dot (as on hcp-1390 signature), then a faint word (crossbar, slanted stroke, loop + tail) that could be `Hjsm` = GIRL as on hcp-1390, but the pixels do not show it reliably; then hatched-circle ornament.

No marker created: the reading is not complete; forcing CARD/THIS ONE/AND/GIRL would be context-guessing, not reading.
