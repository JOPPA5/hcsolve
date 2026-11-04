# Notes hcp-1034

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

2026-11-03 (Claude Opus 5.5, solver round 1):
- Read the plain Kurrent text on the picture side (Liebe Tilly ... morgen einen Brief bekommst; dated Münster 5/9 1904) and the address side (Frl. Mathilde Meyer, Bremen, Caprivi Str. 6; Münster 5.9.04 / Bremen 6.9.04). There is no cipher on the address side. The stamp cannot be inspected underneath.
- Cipher: five rows of invented symbols plus one lone sign right of the spire. Crops are in work/z/ (3-5x from work/hires).
- Breakthrough: the 8-sign group L D R 8 P TRId OV L has the same sign first and last, which gives "herzlich". That gave "ich", "Indem ich mich" (H2=n and H3=m, by stroke count), "für deine liebe", "verbleibe ich mit", "Gruß und Kuß" (ß = s+z, the Kurrent ſʒ ligature), "dein tr. Fritz", and "merksamkeit".
- Problems still open: the oval that is c in "ich" must be u in "Auf" (one place, word sense). The lone k by the spire is taken as an abandoned "ke". The dark figure at the end of row A looks printed.
- No sister card in the repo has the same recipient (searched for Mathilde/Meyer; hcp-1075 is unrelated).
- Result: a complete reading; see SOLUTION.md. Command: python3 -I ciphers/hcp-1034/work/decode.py

2026-11-03 (Claude Opus 5.5, solver, after REVIEWED1 / ACCEPT):
- Added the joining dash between "herzlich" and "bedan." (review finding 1) to the transcription and decode.py; output re-checked, no letter changed.
- Findings 2 (U1 open-u vs closed-oval evidence) and 3 (stamp cannot be inspected) are stated in the report. Register type stays MASC: nothing visible is steganographic.
- Wrote report/report.md, rendered report.pdf, wrote register-entry.txt, then FINAL.
