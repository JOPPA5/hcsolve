ACCEPT

# Review 1, hcp-1353 / pc_hcp_34 (reviewer: Claude Opus 5.5, 2026-10-30)

The reading "Just a little surprise from Loo." stands. I tried to refute it and could not. Four minor points remain, none of which changes a letter of the plaintext.

## What I verified and how

**Command.** `python3 -I ciphers/hcp-1353/work/solve.py` prints `source hashes OK`, `kvtu. b. mjuumf → JUST. A. LITTLE`, `tvsqsjtf gspn. Mpp → SURPRISE FROM. LOO`, `26 enciphered letters decoded; round trip OK`. This matches SOLUTION.md. I recomputed the SHA-256 of every file in `source/` and `work/hires/` separately with `shasum`; all match `work/source-sha256.json` and `SOURCES.md`.

**Independent decode.** `review/work/dec.py` uses a lookup table and shares no code with solve.py: JUST A LITTLE SURPRISE FROM LOO, 26 of 26 letters. The key is the single shift −1 with no exceptions.

**Transcription against the pixels.** I made my own crops of the original `work/hires/pc_hcp_34_adr.JPG`, rotated 90° CCW, at 3x to 10x (`review/work/a.png`, `b`, `c`, `d`, `e`, `f`, `m`, `date.png`). Every sign was checked, since the card has only 26.

| Group | Result |
|---|---|
| `kvtu.` | Clear. Dot present. The last sign is a `u` with a raised finial. |
| `b.` | The sign looks like a digit 6, but the `b` of "Feb." in the plain date on this same card has the same shape (ascender plus closed low bowl; `date.png`). `6. mjuumf` is also visible on the hcp-1375 scan. So this is her `b`. The solver's reading is right, and this gives stronger evidence than the solver cited. |
| `mjuumf` | Clear: m, long j, minims of `uu`, m, f with heavy junction, descending loop and bar. |
| `tvsq` | `t v s` clear. The `q` tail loops to the right of the stem and runs into the next `s`, whereas the `g` of `gspn` loops to the left. That difference supports `q` rather than `g` on the pixels alone (`c.png`, `d.png`). |
| `sj` | `s` is heavy but clear. The `j` has a long diagonal descender with a looped foot; the top looks like a closed bowl only because the rising stroke from `s` joins it. A `g` here would give SURPRFSE, which is not a word. No dot is visible, as on the `j` of line 1. |
| `tf` | Hardest place (`f.png`). The `t` has a thick rising top, a long stem to the lower left and a hooked foot. It descends below the line, which is unusual for her `t`, and the solver says so. The same hooked long-tailed sign occupies the same position in `Tvsqsjtf` on hcp-1350 (`hcp-1350/work/crops/z_full.png`). That reading is itself unreviewed and cites this card, so it is corroboration of shape only. The `f` is the same form as in `mjuumf`. No letter follows the bar: the plural is excluded. |
| `gspn.` | Clear; the `p` has a heavy junction over the printed ring. |
| `Mpp` | See finding 3. Both `p` have the stem above and below the line, a loop left of the stem and a bowl right of it, as in `gspn`. The ink fades from sign to sign, as the solver says. |

**Sense.** This is a natural, complete English sentence of the period. `tvsqsjtf` is not a formula word and comes out of the fixed shift unaided; with `t v s q s j … f` legible there is no competing English word.

**Rest of the card.** No further ciphertext. Picture side: printed caption "The Minster & Grammar School, Wimborne", no handwriting. Address side: `Feb. 7th 1907` confirmed; pencilled `(1)` confirmed; a ruled pen line separates the date from the message; address confirmed. The postmark shows `WIMBOR…`, `10 PM`, `FE 7`, `07`; the rest of the town name is not on the visible arc but the reading is safe. 7 Feb 1907 was a Thursday, and the card does not state a weekday.

**Sources.** The portal status is Not solved with no attachment, as recorded in `source/metadata.md`. I found no use of a published solution, and the number is in neither `skip.txt` nor `register-exclusions.json`.

**Disclosure.** The three difficult readings (`b`, the `t` of `tvsqsjtf`, the `Mpp` capital) are all disclosed. Nothing is restored beyond the signs on the card. There are no "Completion" or "Response to review" sections, so no later additions needed judging.

## Findings

1. **minor. Word dot after `tvsqsjtf` left out of the transcription.** A faint dot stands between `tvsqsjtf` and `gspn` (`review/work/d.png`, around x=310, y=560; also visible in the solver's `work/reading.png`). The solver's table and `transcription.json` omit it, though every other word boundary has its dot recorded. It should read `tvsqsjtf. gspn. Mpp`. No effect on the plaintext.

2. **minor. "Accepted Abbott cards" is overstated.** "Why it is correct" says the key comes from "the accepted Abbott cards" and that `kvtu`, `b. mjuumf`, `gspn` and `Mpp` recur on those cards. hcp-1370, cited in uncertainty 4, is only at DONE1 with no review. hcp-1375 and hcp-1383 are at REVIEWED1 with verdict ACCEPT but not FINAL. Only hcp-1398 is FINAL. The substance survives, because hcp-1383 supplies `kvtu` and hcp-1375 supplies `b. mjuumf`, both reviewed, but the wording should distinguish reviewed cards from unreviewed ones.

3. **minor. The capital of `Mpp` is undersold, and the alternative is misdescribed.** Uncertainty 3 says the `M` is "closer to two humps than three". At 10x (`review/work/m.png`) I count a looped first stroke plus three feet: left, a short middle one and a right one, which is an M and fits the looped capital on hcp-1398 (`hcp-1398/work/closing.png`). It also says "`Np` / `Npp` give no name", but `Npp` decodes to MOO, which is at least a possible pet name (hcp-1352 records M.O.O as the literal alternative). State the alternative correctly and exclude it on the stroke count and the hcp-1398 signature.

4. **minor. Better evidence available for uncertainty 1.** The solver supports `b` from hcp-1375 only. The `b` of "Feb." on this card is same-hand, same-card evidence and should be cited. The "SURPRISE is singular" argument is then secondary.

## What I could not verify

- The portal page itself: I relied on the captured `source/metadata.md` and on the orchestrator's register check.
- The fact that the writer's `t` really descends in this one word. Its shape is read from a card with a printed ring through it, and the only parallel (hcp-1350) is unreviewed and leans on this card. SURPRISE rests on the seven other signs and on sense as much as on this one sign.
- Who "Loo" was, and what the surprise was. The solver labels both as conjecture.
