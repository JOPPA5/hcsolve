# Notes hcp-1315

2026-10-30: captured by Claude Opus 5.5 (orchestrator).

2026-10-30 (Claude Opus 5.5, solver): Identified the Jolánka key from HCP1216 etc. Read all rows on 2.5x-8x crops in work/crops/ (scripts work/crop*.py; run with the codex runtime python). Dead ends and turns:
- Row 8 first looked like unknown signs before it was seen as digits ½ 9 + -kor.
- Row 20 end + row 21 start joined as ma|radok only after the tail of row 20 was resolved (three strokes with a joining bar = m, then a).
- Green-minus-red filter (crop2.py) failed: JPEG chroma blocks. Red-channel stretch (crop6.py) separated the bottom rows and stamp better.
- Stamp rows s6-s8 first gave nonsense (v-a-e-r-a, "váratik", "anjárz"). The t1/t3 views showed that the first signs of s6 are z + e, and the "z" at the end of s8 lacks its loop only because of the tear. The layout then matched HCP1212 (számta / lanszor / csókol / szeretet / tel Feri). s6-s8 are the weakest part; see SOLUTION.md item 10.
- Row 12 has g where d is expected (slip).
No marker existed before DONE1. Output of decode_opus.py checked.

2026-10-30 (Claude Opus 5.5, solver, after review 1): verdict REVISE. Rechecked r14b and deleted the phantom a of row 14 (392 signs). Added ? to the weak signs named by the reviewer; d/h-p stroke order, TT and the barred n of row 2 now in the key section; normalization marks unified ([x] added, ⟨x⟩ removed); counts and citations corrected. Reviewer's r11tt.png shows row 12; row 11 checked on work/crops/r11_full.png. See SOLUTION.md "Response to review 1".
