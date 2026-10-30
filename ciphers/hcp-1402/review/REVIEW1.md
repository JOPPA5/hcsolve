ACCEPT

# Review 1 — hcp-1402 (pc_hcp_83), Caesar +1 love postcard, 28 Jan 1908

Reviewer: Claude Opus 5.5, 2026-10-30. Role: reviewer, round 1.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1402/work/v2/decode.py` (from repo root) runs, reports
   "hashes OK", and prints exactly the plaintext table of SOLUTION.md:
   MY. OWN. [N. L.] BOY. / LETTER THIS. / MORNING WAS. / FINE. MANY THANKS / MY. [N. & L.] FROM. /
   YOUR OWN [N. L.] / GIRL. — "59 enciphered letters decoded + 6 abbreviation letters kept literal".
2. **Independent decryption.** `review/work/indep.py` (my own token list typed from the scan, own −1 shift
   function) gives the same seven lines and the same count, 59 enciphered letters. Every enciphered token
   decodes to an English word; no letter is left over or forced.
3. **Transcription vs. scan.** Rotated `source/address.jpg` 90° CCW myself (`review/work/rot.png`) and
   cut 3x/5x crops of every line (`review/work/r1.png`…`r5.png`, `nl1.png`, `nl2.png`). Sign by sign:
   - `Nz. Pxo. N-L Cpz.` (r1): Nz, Pxo (P with long lead-in loop, x, o) and Cpz clear. The group after
     Pxo is a two-arch N, a short dash/lead-in, and an L-like stroke (nl1.png) — consistent with the
     solver's "N. L."; it is not expanded, which is correct.
   - `Mfuufs uijt.` (r2): M, looped f, u, u, f, s; u, i, long-descender j, t. Supported.
   - `npsojoh xbt.` (r3): all seven + three signs visible. Supported.
   - `GJOF. Nboz uibolt` (r3/r4): copybook G, slash J, then a small o sitting on a long looped f (O+F);
     Nboz clear; uibolt clear except the final t at the card edge, which looks more like an e/looped t —
     context forces t (THANKS), and the solver disclosed this (uncertainty 4).
   - `Nz. N. & L. gspn.` (r4): Nz (same form as line 2), N, ampersand, L, gspn clear. Supported.
   - `zpvs Pxo N-L.` (r5): zpvs, Pxo clear; the closing group is N + dash + a stroke that is less L-like
     than on line 1 (could be read as 1/l), but treated as the same abbreviation, kept literal, and disclosed.
   - `Hjsm.` (r5): H, slash j, s, m. Supported.
   No restoration or added word was found; the "completion" by the second solver session (the
   second `Nz` on line 5, the N. L. / N. & L. reading) is visible on the pixels, not forced from context.
4. **Key / coverage.** One fixed shift covers all enciphered text; heading "G. H. Tuesday." is plain, as on
   the sister cards. The key is the one used across hcp-1386…1407 (e.g. hcp-1397 FINAL).
5. **Context.** Postmark WIMBORNE 10 PM JA 28 08 visible on my rotated scan; 28 Jan 1908 was a Tuesday,
   matching the heading. Address Mr Abbott, Stokelake Farm, Chudleigh, S. Devon — same recipient as the
   sister cards. Plaintext is natural 1908 sweetheart English with the couple's formulae.
6. **Honesty.** SOURCES.md records portal status Not solved and no attached solution; no published
   solution is claimed or used. Credits split truthfully between the GPT solver (partial, 2026-10-26) and
   Claude Opus 5.5 (completion, 2026-10-29). The partial status of the abbreviation groups is stated.

## Findings

1. **minor** — Closing `N. L.`: the second sign of the closing group is a short slanted stroke with only a
   faint foot (r5.png); it is less clearly an L than in the salutation. SOLUTION.md treats both groups as
   identical with some confidence ("the same L as in N. & L."). Suggest wording that the closing group is
   read as N. L. by analogy with the salutation, with 1/l not excluded. Does not affect the enciphered text.
2. **minor** — Final `t` of `uibolt` at the card edge is visually closer to an e/loop than a crossed t;
   reading t depends on context (THANKS). Disclosed, but the report should say plainly that this one letter
   rests on context.
3. **minor** — NOTES.md 2026-10-26 entry is written without spaces between words (e.g.
   "ReadREADMEfull."), which makes it hard to read; the PDF/report should not copy it. Cosmetic.
4. **minor** — Plain English rendering "letter this morning was FINE" is the literal word order; fine,
   but the report could note it means "(your) letter this morning was fine".

No blocker or major findings.

## What I could not verify

- The meaning of the abbreviations N. L. and N. & L. (not claimed by the solver either).
- Identity of the sender "G. H." (not claimed).
- Portal pages were not re-opened by me; I relied on source/metadata.md and SOURCES.md. Source hashes
  checked by the solver's decoder passed.
