# Notes hcp-946

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 — Claude Opus 5.5 (solver) — PARTIAL, no marker

Address side (hires original, crops in work/crops/): place/date "Doberan / 2. April 09", address Fräulein Erna Garbe, Reddelich, postmark Doberan 2.4.09. Picture side: printed portrait of an actress with printed signature (top right, reads like "Edith ..."), publisher number; no handwriting seen there. Stamp still on card; nothing visible around its edges.

Cipher: two lines of Roman numerals separated by dots, word breaks marked ", —":
`I. XII, — XVIII. XIV XIII. XIII / XIX. I. VII, — I. II. V XIII. IV.`
A=1 (with J) gives AL RNMMSAG ... — wrong. The German 25-letter alphabet without J (I/J=9, K=10 …) gives **AM SONNTAG ABEND** ("on Sunday evening"), every token consistent (N=XIII three times, A=I three times). Checked on 3–5x crops: the third token of line 2 is V+II = VII (=G), not VIII; last numeral of line 1 is X plus heavily retraced strokes, read XIII (fits SONN). Under it four question marks "? ? ? ?" in another pencil (literal).
Command: `python3 -I ciphers/hcp-946/work/decode.py` (checks hashes).

Unenciphered notes (Kurrent/Latin cursive, several hands):
- "Gruss, El" (Latin script; signature may be "El" or "Eb", not certain).
- "Besten Gruß" (Kurrent; "Besten" partly on word sense) and a signature below, roughly "Käthe/Kitty …ass." — not read.
- a large, very faint Kurrent line running across the lower half (starts like "w e …", large h-like loop near x≈440/1024, V-shape and "r"-like stroke to the right) — NOT read even with blur/contrast enhancement.
- an underlined word bottom right, roughly "Isa…/Elsa?" — not read.

Why partial: the cipher itself is fully read, but the brief counts the whole card, and one whole faint clause plus two signatures are unread. No DONE marker. Steganography: no hidden writing seen in picture or margins; under the stamp cannot be inspected (stamp in place).
