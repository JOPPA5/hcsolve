# Notes hcp-1205

2026-11-02: captured by Claude Opus 5.5 (orchestrator).

2026-11-02 (Claude Opus 5.5, solver): identified as the Jolánka family key (HCP1216, 1267), reverse direction, Jolánka to Feri Holecz. Key transferred unchanged. Work log:
- First tile pass misread the upper right as one more upright block. It is written with the card turned 180 degrees (U1-U8); `work/croprot.py` handles it. Crops across the divider mix the two orientations: for example `9=2 ...` at the end of row 06 is the upside-down end of U2 (*inkáb*), not a *csak* in row 06. That false *csak* cost a detour.
- Hand-specific finding: tall + short serves h, p and n; double slash serves d and sometimes h; the crossed curve with a short hook is o, without it i.
- Zigzag sign: first taken as punctuation; *pletyka* and *megyek* (row 27) showed it is y.
- Reading solved by word sense in places (see SOLUTION.md uncertainties); rows 25-26 remain the weakest. HistoCrypt article linked on the portal not read.

2026-11-02 (Claude Opus 5.5, solver, after review 1): all findings checked on crops, ledger corrected. New in rows 25-26, beyond the review: m in `mene` is three strokes (free + joined pair, as row 05); `nagyon` replaces `egYin`; `egy hét is` from the review's proposal; `ott, ahonnan` replaces `ott a hon ő/én`, so maga = you. Row 20 `látom, mivel`: six strokes are m + m. Dead ends this round: `ö` of `jö` has no dots, so `jó`; `jöneNek` stays open between nénék / jönnének / jönne nek. Re-review needed because rows 25-26 changed: DONE2. work/crop2.py writes crops2/ (a stray shared scratchpad script was overwritten by another agent, so crops are kept here).

2026-11-02 (Claude Opus 5.5, solver, after review 2): all six findings accepted. Row 25 is `jó népek` (N to P); rows 04 and 14 N to plain n, on crops r04a, r04b and k4, so `N` is one token (row 06). *Egy hét is pedig a rokonnál leszek* is a sentence. Going to report and FINAL.
