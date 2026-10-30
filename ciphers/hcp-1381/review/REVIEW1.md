REVISE

# Review 1 of hcp-1381 / pc_hcp_62 (reviewer: Claude Opus 5.5, 2026-10-30)

Summary: the key and most of the message stand, but one word in the plaintext is wrong. Line 7 does not contain `Nz` ("MY"). It is the abbreviation `M-L` / `N-L`, which the sister card from the same trip also writes at this place. A short fix is needed before FINAL. No re-review is needed if the fix stays within what is listed here.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1381/work/decode.py` passes the four hash checks and prints the claimed plaintext, with 69 enciphered and 5 literal letters. This only shows that the JSON and the table in SOLUTION.md agree.
2. **Independent decode.** `review/work/indep.py` uses its own table and re-typed tokens. Solver tokens give the same text. My corrected tokens give the same text except line 7 (67 enciphered letters). Caesar -1 covers every token, and there are no leftover signs on the card.
3. **Pixels.** I made my own enlargements from `work/hires/pc_hcp_62_adr.JPG`: `review/work/c2.py`, `c3.py`, `lines.py`; crops `l*.png`, `z*.png`, `y*.png`, `x78.png`, `w2.png`, `w4.png`. "Hires" here means 1785x1175, so the 5-6x crops show JPEG blocks.
4. **Sign-by-sign results:**

| Item | Result |
|---|---|
| `Kvtu` | good; k, v, t and u are visible |
| `Ibe` (solver `ibe`) | good, better than the solver claims. The first sign is the writer's capital I with a loop (hcp-1382 records that form in `Ifsf`). The tall stroke and low bowl of b are visible around the overlay symbol, then e (`y3.png`) |
| `b` end of line 3 | acceptable; stem and hook are clear, and traces of the bowl show inside the overlay O (`y3b.png`) |
| `gjof` | acceptable; same g as `Gspn`, long j, small o, and f with top bar and lower loop (`y4.png`) |
| `xbml` | x and b visible; the m is not legible under the overlay R; final l visible (`y4b.png`, `w4.png`). The solver's restoration note is correct |
| `mpwfmz xfbuifs` | good; `xfbuifs` is clean, including the dot of i (`l5a.png`, `l5b.png`) |
| `J ipqf zpv bsf` | good (`z6.png`, `z6b.png`) |
| `xfmm` | good; x, f and six downstrokes (`l7a.png`) |
| `Nz` line 7 | **refuted**, see finding 1 |
| `Gspn` | good; capital G, not lower case as transcribed (`l7b.png`) |
| `zpvs Pxo E. L. Hjsm` | good; line 8 is more legible than the solver says (`z8a.png`, `z8b.png`, `x78.png`) |
| `Nz Pxo` line 2 | good (`z2.png`) |
| `E. L. Cpz` line 2 | faint. A low bowl fits E, the L is mostly lost near the overlay symbol, and C, p and z show as traces (`w2.png`). Correctly declared weak |

5. **Context.** 26 Sep 1907 was a Thursday (computed). Postmark BOURNEMOUTH 4.30 PM SP 26 07 and address Mr W. Abbott, Stokelake Farm, Chudleigh, Devon are confirmed on the scan. Plain foot `Sep 26th 07` confirmed. The picture side has no handwriting. The message is natural 1907 English and fits the couple's other cards. The portal attaches no solution, and I found no sign that a published one was used.

## Findings

1. **Major: line 7 `Nz L.` should be the abbreviation `M-L` / `N-L`, so "MY" is not on the card.** Evidence (`review/work/z7.png`, `x78.png`):
   - The sign is one capital of three downstrokes: a looped first stroke, an arch, and a short third stroke. The short stroke has none of the baseline foot that every `z` on this card has (`Nz` line 2, `mpwfmz`, `zpv`, `zpvs`, all "2"-shaped).
   - The long descender that seems to continue the third stroke is not part of it. It is the ascender of the L of `E. L.` on line 8, which starts just below with a visible gap and runs to its own foot (`x78.png`).
   - The mark the solver calls "a dot" is a short mid-height dash.
   - The whole group is laid out like hcp-1382, posted from Bournemouth two days earlier, which reads `Xfmm. N-L. Gspn / Zpvs Pxo E.L. Hjsm`. hcp-1402 also has `N-L`; hcp-1383 has `M-L`. The solver cited only hcp-1386 and did not compare 1382. The sister cards support this reading, but it rests on the stroke evidence above.
   - The solver lists this `Nz` under "Clear", which is an overclaim.
   - Fix: transcribe `xfmm M-L Gspn` or `N-L` (three downstrokes favour M, but hcp-1382 calls the same form N; say so), keep it literal, update `transcription.json`, the table, the counts (67 enciphered, 6 literal), English and Slovak ("I hope you are well. M-L. From your own E. L. girl."), and move the point to Uncertainties.

2. **Minor: `E. L.` on line 2 is not the only option from sister cards.** hcp-1364 and 1368 have `N. L. Cpz`; hcp-1347 and 1365 have `M`-initial forms. The low bowl here favours E, but the solver should name the alternatives. On line 8 the group is legible; move that one out of the "very faint" class. The second letter has the small foot noted as `E.h` on hcp-1387, as hcp-1382 also mentions.

3. **Minor: capitals.** `Ibe` and `Gspn` are capitals on the card, as far as the forms show. This does not change the plaintext.

4. **Minor: wording.** SOLUTION.md calls the disc a "printed wheel" and "printed" letters. It is the portal's overlay on the scan, not printing on the card, so the pencil under it may survive on the original. The "Why it is correct" section also counts the opening and closing formula as support, although line 2's `E. L.` rests partly on that formula; keep this circularity in view.

## Not verified

- The m of `xbml` cannot be read under the overlay. WALK is the sense-based restoration; the visible x, b and final l do not exclude every alternative, but no better word fits.
- The E and L of line 2 and the "Hotel" of the plain heading could not be proved from the pixels. "Hotel" is plain writing and not part of the decryption.
- M against N on line 7, and the meaning of `E. L.` and `M-L`.
- I did not see the physical card or a scan without the overlay.
