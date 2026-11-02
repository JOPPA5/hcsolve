# Notes hcp-1141

2026-11-02: captured by Claude Opus 5.5 (orchestrator).

2026-11-02 (Claude Opus 5.5, solver): first and only work on this number.
- The whole message side is in the digit-plus-mark cipher, with no open text except place and date. The picture side has no writing.
- Started from the hcp-1174 table. It read the opening at once (Édes Margitkám!, a napok, nélkül). Remaining signs came from this card and agree with sister cards: `1,` b, `2` c, `4` f, `4.` gy, `6` j, `6.` ny.
- Transcribed all 24 lines from the hires scan with 2.2x crops, then 3-6x on doubtful marks (work/crop.py, work/crops/). Result in work/transcription.txt: 480 signs, 96 words, 29 distinct signs.
- Dead ends and traps: "tudókítás", "nálhad", "hátlak", "nagyoj" by the bare table; these are comma omissions or merges, all listed in SOLUTION.md. `7 2. 9 ,` was first read kéz (`9,`), but the comma stands well clear of the 9, unlike every real `9,`, so it is punctuation: kép.
- Crop a/b overlap is only 40 px and 3.1.4.07 appears twice on line 21: confirmed as two separate groups by their positions (ha víg vagyok érted vagyok az).
- The rule rising through line 11 crosses "a lapokat"; it continues as the divider, so I treat it as a divider, not a deletion. Not provable.

2026-11-02 (Claude Opus 5.5, solver, after review 1, verdict ACCEPT):
- `tudósítás` and `után` are now `7,` and `1'` as written; only 3 `~` remain. No letter changed.
- Correction to the last line above: the rising rule does not continue as the divider. It is a separate stroke from the divider's left end and stops at the 7 of `lapokat`. A partial strike is not excluded. "Pencil" was unproved.
- Added to the uncertainties: the blotted last sign of `tavasz`, and the two free dots after `panaszkodom`.
