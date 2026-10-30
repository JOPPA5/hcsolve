ACCEPT

# Review 1 of hcp-1383 (pc_hcp_64) — Claude Opus 5.5, reviewer, 2026-10-30

The reading stands: Caesar −1, 19 enciphered words, 73 letters, all confirmed on the pixels. There are three minor findings. None changes a letter. Finding 1 changes how one sentence should be understood, so the solver should address it before FINAL.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1383/work/decode.py` ran. Source hashes OK (also recomputed with `shasum -a 256`, all four match SOURCES.md). The output equals the plaintext table in SOLUTION.md. 73 shifted letters and 6 literal letters.
- **Independent decode.** `review/work/own_decode.py` uses its own arithmetic and word list, typed from my reading of the scan, not from transcription.json. Output: MY OWN BOY JUST COME BACK I FOUND LETTERS WAITING HERE FOR ONE WEEK ONLY FROM YOUR OWN GIRL (19 words, 73 letters). It agrees with the solver.
- **Transcription.** I rotated `work/hires/pc_hcp_64_adr.JPG` 90° CCW (`review/work/rot.py`) and made 2x segments and 3–6x zooms (`review/work/zoom.py`, `zoom2.py`, outputs `seg*.png`, `z_*.png`). Every word was read on the card. Nothing was skipped because the card is short.
  - Clear with no doubt: Nz, Cpz, kvtu, dpnf, cbdl, gpvoe, ifsf, gps, pof, xffl, pomz, gspn, zpvs.
  - `Xbjujoh`: X, then b, j, u, j, o, h. The o is an inked-in blob and the h has a filled arch, but the letter count and the two long j slashes are clear.
  - `mfuufst`: the last sign is a stem curving like a c with a top stroke, as the solver discloses. It stands apart from the s. Four minims make uu.
  - `Pxo` (twice): the arc over the stem is confirmed. The thin connection is a dry-pen stroke. The sign is P, not i + flourish.
  - `Hjsm`: H with crossbar; a long slash with hooked foot, descending below the line; s of the same form as in `ifsf`; a hairline joining to a three-stroke m. It is GIRL, not a time.
  - `M-L.` against `Nz`: three feet against two in the zooms (`z_ml.png`, `z_nz.png`). The solver's M is right. The m of `mfuufst` has the same construction. The join is a plain dash, not an ampersand.
  - `E. L.` and `E-L.`: the E is certain. The L is a slash with a heavily inked base and is less clean than the L of `M-L.`. The last one has a dry ascender. L is the best reading and matches the sister formula. It is disclosed, and no meaning depends on it.
- **Plain parts.** Heading "1 Cleveland Rd" and "Monday Sep 23rd 07" are as stated. Postmark BOURNEMOUTH 8 PM SP 23 07, Royal Series, Bournemouth Series 1089, address and recipient are confirmed. 23 Sep 1907 was a Monday (decode.py assertion). The picture side has no writing.
- **Key coverage.** One shift, no exceptions. Only the two abbreviation types (6 letters) stay outside it, and they are bracketed and disclosed.
- **Restorations.** None. There are no completion or restored letters, and "No restoration was used" is correct. The only reading chosen by word sense is the c-like t, and it is disclosed.
- **Language and context.** Natural period English in the couple's formula. Salutation and closing are parallel on hcp-1386, 1403 and 1370. hcp-1381 and 1382 are further Bournemouth cards of the same week.
- **Sources.** Portal status Not solved and no attachment, per SOURCES.md and metadata. No use of a published solution is visible. The number is not in skip.txt or register-exclusions.json.

## Findings

1. **minor — probable mis-phrasing of the sentence "for one week only" (SOLUTION.md translation and uncertainty 6).** The translation runs "I found letters waiting here for one week only" and calls its point unexplained. The writer puts a dot after every word, so the dots do not settle the sentence division. The sister cards suggest a better division: "I found letters waiting here. For one week only", or "…waiting. Here for one week only", meaning her own stay. Monday 23 Sep is posted from Bournemouth (this card), then 24 Sep (hcp-1382) and 26 Sep (hcp-1381), and by Monday 30 Sep she writes from G. H. with a WIMBORNE postmark (hcp-1370). That is one week exactly. hcp-1370 is itself DONE1 only, so this is supporting evidence, not proof. The letters do not change. Fix: give the parsing that fits the dates, keep the literal alternative in the uncertainty, and update the Slovak.
2. **minor — wrong count in "Why this is correct".** The text says "all 16 enciphered words". There are 19 (73 letters, which is correct). Fix the number.
3. **minor — citation in uncertainty 3.** It cites hcp-1398 for the hooked-slash j, but that SOLUTION.md has no such description. The sister that records it is hcp-1386 (uncertainty 1 there). Cite that card.

## Could not verify

- `E. L.` and `M-L.`: their meaning, and whether they are enciphered. The solver leaves both open, which I agree with.
- I did not compare the capital J (a loop with a diagonal stem) sign by sign against a sister card. It is a one-letter word, it reads as a period capital J, and I = "I found" is the only sensible value.
- "1 Cleveland Rd" as a real Bournemouth address was not looked up. It is plain text and does not affect the reading.
