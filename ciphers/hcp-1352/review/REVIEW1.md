ACCEPT

# Review 1 of hcp-1352 / pc_hcp_33 (reviewer: Claude Opus 5.5, 2026-10-30)

Verdict: the reading and the key stand. All findings are minor. They concern how signs are described, not what the message says.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1352/work/decode.py` ran. The hashes were OK and it reported 97 enciphered letters. Its output matches the plaintext column of SOLUTION.md and `work/plaintext.txt` in wording. I also recomputed the SHA-256 of all four image files with `shasum`, and they match SOURCES.md.
2. **Independent decryption.** `review/work/indep.py` holds my own typed transcription and a separate −1 shift. It gives TAKE CARE I HAVE MADE / NO MISTAKES I AM VERY / MUCH AMUSED WITH OUR / NEW PLAN MY LOVE / ON A POST CARD HOW / NICE THIS IS SECRET LOO, 97 letters. Shifts +1, +2, +3 and +13 applied to the same text give no English.
3. **Transcription against pixels.** I rotated `work/hires/pc_hcp_33_adr.JPG` 90 degrees CCW and enlarged it 3 to 6 times (`review/work/r1..r6b.jpg`, `c1..c4.jpg`, `z_*.jpg`, `cmp_g_j.jpg`). I read all six rows sign by sign. No enciphered word is missing, and every row runs to the card edge with nothing after it. The grey wheel is the portal watermark.
4. **Normalised signs, checked individually.**
   - a-shaped b in `Ualf`, `dasf`, `a`, `dase`: the signs really are a-shaped, with no ascender of their own, except that `Ualf` is ambiguous as disclosed. The same writer's b elsewhere (`bn`, `bnvtfe`, `nbef`, `qmbo`) has a tall stem. Correctly disclosed.
   - Last sign of `ofx`: a long flat bar crossing a stem with a blob foot. It is unlike the x of `xjui` and closer to the bar-type t. Disclosed, and NEW is the only word that fits.
   - `uift`: the third sign has the same outline as the final f of `ojdf`. The dot over the preceding i is real. Literal THES is correctly disclosed as a correction by sense.
   - `nvdg`: see finding 2.
   - Final capital: see finding 1.
5. **Key coverage.** One key covers the whole text, with no literal group and no leftover signs. The solver's count of normalisations (8) is consistent with its table, subject to findings 1 and 2.
6. **Language and context.** The result is natural English of the period. 1 Feb 1907 was a Friday (computed), which matches the plain heading and the postmark WIMBORNE FE 1 07 as far as I can see on the card. The addressee and the Wimborne origin agree with the sister cards. `Mpp` occurs on hcp-1398 (FINAL), and on hcp-1350, 1353 and 1354.
7. **Picture side.** Printed "Ludlow Castle", Valentine's Series, with no handwriting, as stated.
8. **Sources.** `source/metadata.md` records no attached solution or transcription. I found no sign of a published solution being used. hcp-1352 is not in `skip.txt` or `register-exclusions.json`.

## Findings

1. **minor: the final capital is described as N, but the pixels show M.** Uncertainty 7 says "two humps, which is N as it stands" and lists `N.p.p. -> M.p.p.` as a normalisation. Two humps means three downstrokes, and that is what `review/work/z_M.jpg` shows: hooked stroke, arched second stroke, and a third stroke ending in the tail. The N of `Nz` on this card has one downstroke fewer (`review/work/c4.jpg`), and the m of `mpwf` also has three. The sign can be taken as `M.p.p.` as seen, so LOO needs no correction here. The two-humps wording in point 7 also misdescribes the sister evidence: hcp-1350 argues for three downstrokes, and only hcp-1353 speaks of "closer to two humps". hcp-1350, 1353 and 1354 are still under review, so hcp-1398 is the only accepted parallel. Fix: as-seen `M.p.p.`, then 7 normalised words and 90 of 97 letters as written, and correct the sister statement.

2. **minor: the same sign shape is treated two ways.** `review/work/cmp_g_j.jpg` puts the last sign of `nvdg` beside the first sign of `jt`. Both have a closed top bowl and a long descender with a return loop. The solver calls the first g, and so a correction, but transcribes the second as plain `j` with no normalisation. The real j of `xjui`, by contrast, is y-shaped. So either `jt` is a further g-shaped sign needing disclosure, or the `nvdg` sign is this writer's looped j (or an i with a tail). The second option gives a simpler account of MUCH than the solver's backward-shift guess: the writer's i and j signs overlap, and the word is one sign away from `nvdi`. Plaintext is not affected. Fix: add `jt` to the disclosed signs and reword uncertainty 2.

3. **minor: "G. H." is not addressed.** SOLUTION.md states the heading is not shifted, and that holds for "Friday". It says nothing about what G. H. means, and if shifted it would be F. G. The Slovak carries it without comment. Fix: one line stating that its meaning is unknown.

4. **minor: the "as written" figure is softer than it reads.** "89 of the 97 letters decode as written" also includes `Qptu`, `Tfdsfu`, the y-shaped j and the n/u of `bn`, which the solver lists under uncertainties 5 and 6 as choices made by sense. The disclosure is there, but the number should carry that qualification.

## What I could not verify

- Who "Loo" is, and what "our new plan" means. The solver marks both as conjecture.
- Whether the a-shaped signs are a short b or an unshifted A. The card does not decide this and the plaintext is the same.
- I did not re-read the sister cards' images. Statements about them rest on their SOLUTION.md files and on hcp-1398's review.
- I did not independently re-check the portal page; the status comes from `source/metadata.md`.
