# Notes hcp-903

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 — Claude Opus 5.5, solver attempt (PARTIAL, no marker)

What the card shows (read from work/hires/ originals, enlarged 2–3x; crops L*/z*/w* in work/):
- Address side: plain "Herrn H. Johannessohn, S.W. 29, Fürbringer Str. 20 II", Berlin postmark 29.11.02. Nothing else visible; the stamp box cannot be inspected underneath.
- Picture side: plain "Berlin, d. 29. 11. 02." then about 11 lines of invented signs, words divided by "/", one detached "?", one hyphen at a line end (line 3 into line 4), one sign with an overbar (H with bar, probably a Kurrent-style doubling mark), and a darker-ink group at the bottom right.
- About 22 working sign classes (labels in work/transcription-draft.txt): + o H d x 6 7 J Z C b L P y F G q D M W S ... Several are uncertain splits/merges: H vs N-shaped H (lines 7, 9), J (2/3 with descender) vs Z (2 with loop) vs C (open hook), D (big loop) vs d (alpha with upright) vs the D+H ligature written like a cursive M, L (club-headed stem) vs S.
- Line 10 middle and end are partly overprinted by the HCPortal collection stamp (one word reads b P d ? ? with an unclear sign and a dot); the bottom-right darker group (before "/ + J F 7 H + G") is not transcribed reliably. These parts are left out of the draft.

Cryptanalysis tried:
- Word-pattern search against the German frami/UD word list (work/pattern.py): strong isolated hits are L+L+x = "gegen", x P F = "nur", L H b = "gut/gab", y+Gq+(7) = "weiter/leider/beide(r)", DH+dx = "klein/Stein". These do not combine: e.g. "nur" (F=r) makes the thrice-repeated 2-letter word G F = "?r", which only "er" fits, clashing with + = e.
- Bijective MASC annealing (work/anneal_masc.py, German 4-grams + word bonus) and annealing with up to two signs per letter (work/anneal_homophonic.py): no run produced coherent German; best strings are word salad (e.g. "seine ... gegen ... gemessen" fragments only). Reversed word order inside words was also tried: nothing.
- Line 1 word 2 (11 signs, 6 H d H o J + d x + 7) has no German dictionary isomorph under any of the tried class splits, so it is either a compound/name or the sign classes are wrong.

Why it stops: the sign inventory itself is not stable (the classes above), and every key tried leaves most words unread. No letter of the plaintext is established, so there is no partial plaintext to report and no SOLUTION.md, no marker and no register entry. Next steps for a later attempt: build a glyph contact sheet of every token to settle the class splits (especially H/N, J/Z/C, D/d/M), then retry pattern work starting from "gegen" and "nur"; consider that + may not be e, or that the card is homophonic.
No published solution of this card was searched for or found.
