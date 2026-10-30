ACCEPT

# Review 1 – hcp-1460 (pc_hcp_141), reviewer Claude Opus 5.5, 2026-10-30

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1460/work/decode_full.py` (repo root)
   runs cleanly: source hashes OK, all six round-trips OK, 6 lines / 89 letters,
   output identical to the plaintext in SOLUTION.md
   (`DearSadie / Fatherwasdelight / edwiththeConcert / lastnightandhas /
   askedmetgivyeuo / hiscongratulations`).
2. **Independent decoder.** `review/work/verify.py` (own index-permutation
   implementation of the first/last/second/second-last route, own transcription
   typed from my crops). Run: `python3 -I review/work/verify.py work/transcription.txt`.
   My transcription is identical to the solver's; output identical. Inverse
   checks: `enc("hiscongratulations") = hsogauainsotltrnci` (exact match to the
   card incl. the inserted `s`); without the inserted `s` the line gives
   `hiscongratulation`, so the `s` is exactly the missing plural letter at the
   right position. `enc("askedmetgiveyou") = akdegvyuoeitmes` vs card
   `akdegveouyitmes`: the four letters after `v` are in fully reversed order,
   exactly as SOLUTION.md uncertainty 1 states.
3. **Key coverage.** One uniform route, restarted per line, consumes all 89
   letters; no substitution, no unused or added letters. Five lines decode
   with no deviation; the sixth is a disclosed order slip plus the unwritten
   `o` of "to", rendered `t[o]` editorially. No alternative arrangement of
   line 5 (e.g. `asked me to give yu`) reproduces the card either, so the
   slip explanation is the most economical one.
4. **Transcription vs scan.** Enlarged (5–20x, some contrast-stretched) crops of
   every line in `review/work/L1_0…L7_1.png` plus detail crops
   (`l5_k`, `l5_mid`, `l5_tmes`, `l6_cluster`, `l6_u`, `l6_u2`, `l3_tt`,
   `l3_hh`, `closing`). Every line read sign by sign; letter counts match
   the transcription (9, 16, 16, 15, 15, 17+inserted s). The line-5 middle
   cluster is clearly `v e o u y`; `i t m e s` is clear; the inserted small `s`
   under line 6 sits between `n` and `o` as claimed.
5. **Language/context.** Fluent Edwardian English ("Father was delighted with
   the Concert last night and has asked me to give you his congratulations"),
   addressed "Dear Sadie" to Miss Ovington, South Tottenham, postmarked
   7 Mar 1905 — fits a local note. Picture side has no cipher text (checked).
6. **Sources/honesty.** No published solution claimed or found; portal status
   Not solved. Credit split GPT (route + lines 1–4) / Claude (lines 5–6) is
   consistent with NOTES.md. All restorations are disclosed.

## Findings

1. **minor – line 6, sign read `u` is not cleanly a `u` on the pixels.**
   In `review/work/l6_u2.png` the sign has an entry upstroke and pointed
   tops; it is ambiguous between cursive `u` and `n` (GPT read `n`). The
   SOLUTION's "cups at the bottom, unlike the `n`" overstates the visual
   evidence; `u` is supported mainly by the route (`congrat-u-lations`).
   Suggest wording: "ambiguous u/n; read u as the route requires".
2. **minor – line 5, second sign `k`.** In `l5_k.png` it is an `h`-like
   form with a small knot in the arch; the `h`s of line 3 (`l3_hh.png`) are
   similar. The `k` reading is plausible but largely route-driven; say so.
3. **minor – line 3 "tt written as a crossed double t" is inaccurate.**
   `l3_tt.png` shows a plain `t` followed by a separate hooked/looped sign;
   that second sign stands for one `t` (route position 4 → "wi-t-h t-he").
   The transcription `ewtte…` is correct (16 letters); only the description
   in uncertainty 3 is wrong and the hooked sign's `t` value should be noted
   as context-supported.
4. **minor – analogy in uncertainty 1.** Calling the line-6 inserted `s` "a
   similar slip" is loose: line 6 is an omission the writer corrected, line 5
   is an uncorrected order reversal. Harmless, but rephrase.

## What I could not verify

- The identity of the writer (`Ys H.A.r` – initials uncertain in form) and of
  Sadie Ovington / the concert; no external records searched.
- Only the portal's `-large` JPEG conversion was available; finer stroke
  details (findings 1–3) cannot be settled at this resolution.
