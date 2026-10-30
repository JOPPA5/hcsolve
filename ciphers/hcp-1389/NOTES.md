# Solver notes

2026-10-26: Read README in full; assigned only HCP 1389. Root had freshly read rendered General/Description/Attachments and saved original scans/metadata/SOURCES. No marker existed. Inspected both original images, rotated a working copy of the address side 270 degrees, made enlarged crop. The image side contains printed caption only, no apparent handwriting.

The family Caesar −1 hypothesis works directly on `Nz Pxo Efbsftu J / dbo tbz. bn / jo. gbwpvs. xjui / Qb. usvtu.` → 40 frozen letters in coherent text. Punctuation preserved. This does not require a corpus lookup.

Remaining obstacles are compressed initials/marks after trust, closing Gsp[n/o] vs context-suggested From, subsequent token, and ordinary signature. Kept these outside the frozen transcription rather than completing them from expected wording. Readings in transcript.json and SOLUTION.md are deliberately partial. decode.py checks immutable-source hashes and reproduces only the manual transcript, not image recognition.

Persistent user override: no watcher or reviewer started. No marker created because the whole ciphertext is not yet supported.

2026-10-29 (Claude Opus 5.5, solver role, orchestrated run; watcher disabled): Re-read the scan at 4–12x (work/crops/). Found a cipher j on line 2 (`dbo tbz. j. bn` → can say i am) and that the "signature" H/S/m is cipher `Hjsm` = Girl (j = long slash with lower-left hook; same as hcp-1395 `Hpjoh`, `Hjsm`). Line 4 word after `Qb.` is NOT `usvtu`: visible u, s, j-shaped slash with hook, o, 7-shaped t(?) with detached bar → literal "trins" (or "tros" if slash+o = p). Not English; GPT's "trust" needs an unseen v and u. Left unresolved. Closing fields `[M/N]..[&] L.` (family M&L → L&K) and `N..`+raised mark (cf. hcp-1390 Mʰ, hcp-1402 No1-like) reported literally. New files: work/transcription_v2.json, work/decode_v2.py (run from repo root: `python3 -I ciphers/hcp-1389/work/decode_v2.py`), work/crops/*. Old transcript.json/decode.py kept as GPT's record. No marker: one body word unresolved. A higher-resolution scan would probably settle it.
