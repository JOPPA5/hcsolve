# Notes — HCP 1393

2026-10-26: Read README fully. User's persistent override prohibits starting watchers/reviewers. Assigned exactly one cipher. Root read all three rendered tabs and captured originals before this solve.

Personally inspected `source/address.jpg` and `source/picture.jpg`. Picture contains the printed title Church Parade. Southsea., no additional handwriting. Rotated address scan 270° into work only, then cropped/enlarged without altering originals. Read simple Caesar−1 from the repeated English groups EFBSFTU / MFUUFST / GSPN ZPVS PXO. Cipher-only transcription and decoder saved with source SHA-256.

61 positions appear in the partial manual transcription; some are provisional and no full-coverage claim is made. The uncommitted group after THERE IS may be OP or POF; source syntax remains unsatisfactory with tentative GLAD. Re-reading has not established which alternative is correct. The fourth-line right continuation and lowest/oval text remain open. IVSSBI → HURRAH is only a hypothesis. It must not be called a sender's name or definite decoded word.

No completed candidate or DONE1. Root may independently revisit these unresolved groups. No reviewer, watcher, PDF or register entry started.

## 2026-10-29 — Claude Opus 5.5 (solver)

- Hashes of source/ re-verified (unchanged). Re-read every line on enlarged contrast crops (work/crops/).
- Line 2: `hmbe. uifsf. jt. pof.` → GLAD THERE IS ONE (pof is clear: p, o, f; the j of jt has a g-like
  entry curve and no visible dot; g would give no word).
- Line 3: the earlier `mfuufst` was wrong — the ink is `mfuufs.` (z_letter.png) → LETTER, so the sentence is
  "I am glad there is one more letter for me this week!".
- Line 4 tail: `xffl!` then a cross below the line (kiss), then shorthand `M & L` with raised mark and
  underline — same family as hcp-1403 "N. & L." and hcp-1390 "M ××"; kept literal.
- Line 6: `Mᵘ.` + "Hjsm" (GIRL) — same closing as hcp-1390 "Mu. Hjsm". Line 7 in a drawn cloud:
  "Ivssbi" → HURRAH (all six letters clear in oval.png).
- 73 enciphered letters, all under Caesar −1. Postmark WIMBORNE 10 PM AP 29 07; 1907-04-29 = Monday.
- New command: `python3 -I ciphers/hcp-1393/work/decode2.py`. SOLUTION.md rewritten; DONE1 created.

## 2026-10-30 — Claude Opus 5.5 (solver, after review 1)

- Review 1 verdict ACCEPT, four minor findings, all accepted after checking review/work/m_r6b.png,
  m_r4r.png, m_r2mid.png: the raised sign after M (line 6) is h-like, not u → `M[h]`, unread; the
  hcp-1390 "Mu." citation withdrawn; line-4 group now `M ? L` (middle sign r/&/+-like); `jt` j read by
  context only; faint u-i of `uifsf` disclosed. transcription2.json notes updated; decode2.py re-run (73
  letters, plaintext unchanged). Report written and rendered; register entry written; FINAL created.
