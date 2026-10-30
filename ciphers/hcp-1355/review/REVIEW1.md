ACCEPT

# Review 1 of hcp-1355 / pc_hcp_36 (Claude Opus 5.5, reviewer, 2026-10-30)

I tried to refute the reading and could not. All 81 enciphered letters stand on this card's pixels under one fixed shift. The findings below are small corrections to how the uncertainties are described. None changes the plaintext.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1355/work/solve.py` prints "source hashes OK", the seven lines as in the SOLUTION.md table, and "81 enciphered letters decoded". The output matches the claimed plaintext exactly.
2. **Independent decryption.** `review/work/decode.py` holds my own transcription, typed from my crops, and a separately built key. It reads no solver file. Output is identical in all seven lines, 81 letters. Scoring all 26 shifts by English letter frequency gives shift 1 at 6.09 and the next best at 4.87.
3. **Key coverage.** One fixed shift applies to every letter, with no exceptions and no card-specific adjustment. Cipher letters a, l, q, r and y do not occur, which is normal for 81 letters. No cipher letter was left undeciphered or skipped.
4. **Transcription against the scan.** I rotated `work/hires/pc_hcp_36_adr.JPG` myself (`review/work/rot.png`) and read every line sign by sign at 4x (`c_*.png`), and the doubtful spots at 6x and 8x (`z_*.png`, `y_*.png`). This also covers the stops: the transcription's stops match the card, and there is none after `kvtu`, `tuspmf`, `up`, `Npsjoh`, `Xjui` or `zpvs`. The SHA-256 of the hires scan agrees with `SOURCES.md`.
5. **Each disclosed point, on the pixels:**
   - `Npsjoh`: confirmed. After `s` come the long `j` with its back-curling tail, then `o`, `h`, the same sequence as `hpjoh`. There is no room or stroke for an `o` before the `j`. The hook under `s` is the `j` tail, the same form as in `hpjoh` and `Tfswjdf`. MORING is the literal text, and it does not occur on the sister cards I searched (hcp-1356 has `npsojoh`), so a slip is the right explanation.
   - `tuspmf`: confirmed as one `m`. At 8x I count three downstrokes (a pale high arch, then two dark ones) before the join into `f`. Six would be needed for `mm`, so the solver's doubt is if anything too generous.
   - `gps`: the `g` and `p` are pale but complete. The third sign is a round blob, and a separate small dash follows it. Calling this close to a restoration is fair.
   - `Fbsmz`: confirmed. In `review/work/y_compare.png` the stem runs through and well past the bowl, as in the second `f` of `Cffo`, while the `G` of `Gspn` stops at the bowl.
   - `Xjui`: confirmed as to reading; see finding 2.
6. **Language and context.** The plaintext is natural English of the period and matches the couple's formulae (`Nz. Efbsftu`, `Gspn zpvs Hjsm`). Postmark WIMBORNE 10 PM MR 30 07 and address Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon are visible on the card. Computed: 30 March 1907 was a Saturday and Easter fell on 31 March 1907. Picture caption read as "English Lakes. Honister Cray" as printed, as disclosed. `Efbsftu`, `Gspn`, `Hjsm` and `npsojoh` recur in the sister solutions, but I judged this card on its own strokes.
7. **Sources.** The solver states no published solution was known or used, and that no web search was made. Nothing in the directory contradicts this. The sister-card dependence (`Xjui`) is disclosed.

## Findings

1. **minor: the `w` of `Mpwf` is a weaker sign than item 7 of the uncertainties says.** Item 7 says the letter shapes stay visible except at `gps`. At 8x (`review/work/z_love.png`) this sign is a pale grey smudge and one short dark stroke running on to `f`, so a `w` form cannot be read in full as it can in `Tfswjdf`. LOVE is safe, since M, p and f are clear and the formula fits, but this letter is read partly from fit. Add it next to the `s` of `gps` as a sign-level weak point.
2. **minor: uncertainty 6 misdescribes the `X`.** The "large hook" is not part of the `X`. It is the tail of the following `j`: a long stroke rising from the hook to the top right, the same form as in `hpjoh`, `Tfswjdf` and `Npsjoh`. Taken that way the `X` is just the crossed sign and the word has its four letters without any unusual form. If the hook were part of the `X`, no `j` stroke would be left. Correct the description. The uncertainty can be reduced accordingly.
3. **minor: "faint" is the wrong description of the heading's last word (uncertainty 5).** On the hires scan it is dark but cramped (`review/work/y_even.png`). Its first strokes rise high and the later letters run together, so "evening" is a probable reading rather than a clear one, supported by the 10 PM postmark. It is clear text outside the 81 letters. The note should say cramped and probable.
4. **minor: line number mismatch.** `work/transcription.json` says "Line 7 starts in the far left margin", while SOLUTION.md correctly says line 6 (`Xjui Mpwf…`). Fix the note in the JSON. This changes neither the decode nor the letter count.

No blocker or major findings.

## What I could not verify

- Whether a published solution exists elsewhere: I made no web search, and rely on the portal capture in `SOURCES.md` and the orchestrator's register check.
- The initial of the heading, C or G. The sign has a low tail and could be either, as disclosed. The heading is clear text and is not expanded.
- The meaning of "C. H." and the writer's identity.
- The `s` of `gps` as a letter form: a blob cannot be proved to be an `s`. Only FOR fits.
