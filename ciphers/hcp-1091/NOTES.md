# Notes hcp-1091

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

2026-11-03 (Claude Opus 5.5, solver):
- Looked at both scans (hires). The address side is plain Kurrent (Herrn August Hradegh, b. Krems). All ciphertext is on the picture side, in the left margin (A), the right margin (B) and three upside-down lines in the sky (C). The C lines run under the stamp.
- The repeated ending ".+8" suggested ich/dich/sich. "0...6..4" (twice) = Lieber, which gave . = i, .. = e and ... = ie. Then also, wirklich, doch/noch, böse and gekränkt fixed the rest of the key.
- Kurrent conventions: 2 = n, 2 with a breve = u, 2 with dots = ü, T = o, T with dots = ö, dash with dots = ä.
- Shared signs: 1 = d/t, 5 = g/k, 9 = f/v, + = c/z. A second s-sign (closed y-shape) appears in "so" and "süsen". The J-sign appears only in "Jaga(s)".
- Problem spots: S-shaped sign in "wirst"; 1-shaped sign in "recht"; 7-shaped sign in "wol"; restorations h (picture), r and n (stamp). All are listed in SOLUTION.md.
- Web search found no published solution. Wrote work/transcription.txt and work/decode.py, with crops in work/crops/.

2026-11-03 (Claude Opus 5.5, solver, after review 1, ACCEPT):
- B3 and B4 r are both coded S (variant of r). The `...ei` token is dropped, so the writer's spelling is "verzien". The stamp area and the address-side annotations are disclosed. decode.py re-run OK. Type stays MASC: there is no evidence of a hidden message under the stamp.
