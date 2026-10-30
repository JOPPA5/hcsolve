# Triage
Dense custom symbolic substitution fills message panel and upper margin,
including inverted continuation. Not a short standard numeric/Pigpen case.
No reliable transcript/key/plaintext established. Original scans preserved;
no marker/register entry. Move1468 to seek easier candidate.

## 2026-10-30 — Claude Opus 5.5 (solver): complete reading, handed to review
Earlier triage above (GPT solver, 2026-10-26) had no key. Worked only from source/address-large.jpg.
- Glyph inventory ~22 stroke signs plus dot groups; no sister family in the repo (grep θ/⊥ in
  SOLUTION/NOTES: only unrelated hcp-1212, hcp-1465).
- Rough first transcription (since deleted, superseded by work/transcription.txt). English
  quadgram hill-climb (model built from vim docs + repo English plaintexts, scratch only):
  shapes only -> no English; each dot as its own token -> no English; reversed lines -> none;
  **dot groups as one token by dot count -> English at once** ("my own dearest ... your letter
  this morning came in time for me to read it at breakfast ...").
- Then re-read everything on 5–10x crops (work/lines/, work/crops/). Dots: 1 dot = e, vertical
  pair = i, falling pair = g, rising pair = h. Caret = n and w (no stable difference). k has two
  forms. q = circled dot (quite). p = bracket with top bar (half past, up, present, hope).
- Faint dots checked at 9x and with a connected-component listing (B01). "together" in B13
  has faint third dots (z11.png).
- Text order: body B01–B13, then top margin T1–T7. No inverted text (the earlier triage note
  was wrong). Sender signs "Reg".
- Residual: "dredful" written twice with the caret where r is expected; n/w by context.
- Decoder: python3 -I ciphers/hcp-1469/work/decode.py (hash check + decode). DONE1 created.
