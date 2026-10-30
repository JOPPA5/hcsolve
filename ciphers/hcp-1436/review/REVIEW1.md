ACCEPT

# Review 1 – HCP 1436 / pc_hcp_117 (International Morse, Singapore 1912)

Reviewer: Claude Opus 5.5, 2026-10-30. Round 1 (DONE1).

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1436/work/decode_full.py`
   from the repo root prints exactly the text claimed in SOLUTION.md:
   `MY OWN DARLING GIRLIE WoULD YOu LIKE A NICE LOnG WALK ROUND THIS [LONGSTROKE] PART HOW I sHOULD LOVE TO TAKE YOU DARLING EVER [BLOT] EVER YOUR OWN OMAR`
   / `105 letters decoded (4 ...)`. The source hashes match
   (`shasum -a 256 source/*` = `work/source-sha256.json`).

2. **Independent transcription and decoder.** I rotated
   `source/address.jpg` by 270 degrees myself (`sips -r 270` →
   `review/work/up.jpg`), cut every one of the 10 Morse rows into 4x crops
   (`review/work/r1a.png` … `r10b.png`) and 6–10x zooms of every doubtful
   spot (`z_own`, `z_r1l`, `z_r3a/b`, `z_long`, `z_r5mid`, `z_r5end`,
   `z_sh`, `z_part`, `z_ever1`, `z_ever2`, `z_r9full`, `z_r10`, `z_sig`,
   `z_sigend`), and transcribed the card without using the solver's
   JSON. My transcription and a separate decoder with its own Morse table
   are in `review/work/my_decode.py`. Its output, after upper-casing the
   solver's output and renaming the long-stroke tag, is **identical** (`diff` empty):
   105 letters, same word division, same two non-Morse marks.

3. **Sign-by-sign check of every disclosed point on the pixels:**
   - *wOuld (row 3)*: the dark blot sits between dividers after `.--`
     and ends in one clean dash; it is about two marks wide. O is
     the only fill that gives a word. This is a restoration and it is disclosed as one. Agreed.
   - *yoU (row 3)*: the first mark of the last group is a lump with a
     notch, wider than a dot and shorter than the following dash. `..-`
     is plausible and disclosed.
   - *loNg (row 4)*: see finding 1.
   - *sHOULD (row 6)*: the first group is dot, a mark about twice the size of a dot, then dot.
     It is visibly shorter than the three dashes of the O next to it. S is
     the better reading. The solver discloses R/RHOULD as the alternative. Agreed.
   - *Long stroke before PART*: a heavy bar about 4 dashes long,
     followed by `||`. It is not Morse, and it is correctly left undecoded.
   - *PART*: `.--. | .- | .-. | - |||`. The last group is a single clean
     dash. Keeping the literal PART rather than PARK is right.
   - *Blot between EVERs (row 9)*: a looped ink figure between word
     dividers, possibly "&". It is correctly not restored.
   - *OWN (row 10)*: a divider-like stroke crosses at the junction of the
     two dashes of W. Reading it as a stray stroke is reasonable.
   - *OMAR*: `--- | -- | .- | .-.`. The three dashes of O are distinct.
     The A's dot sits just right of the divider. The R ends in a clean dot.

4. **Ordinary rows sampled and confirmed**: MY OWN DARLING (row 1),
   GIRLIE (row 2), ULD YO (row 3), LIKE A NICE LO (row 4), all of row 5
   (WALK ROUND THIS, including `- | .... | .. | ...`), HOW I (row 6), all of
   row 7 (LOVE TO TAKE YOU), DARLING (row 8), both EVERs and YOUR (row 9).
   In this hand V is written with a fat first dot in both EVERs. It is
   still `...-`, not `-..-`.

5. **Key coverage.** It is the standard International Morse alphabet. Every
   group on the card is decoded or explicitly marked as non-Morse, so no
   ad-hoc symbol values are used. The two loop rows along the card edge
   carry no dots or dashes, and treating them as an ornamental border is right.
   I checked the picture side as well: it shows only the printed caption "Botanical Garden,
   Singapore" and no Morse.

6. **Language and context.** The text is fluent Edwardian English endearment
   ("my own darling girlie", "how I should love to take you", "ever …
   ever your own"). It is addressed to M. C. Hutton, 94 Gunterstone Rd,
   West Kensington, London W., and postmarked Singapore 10.30 AM 27 MY
   1912, with a Singapore Botanical Garden view, so "a nice long walk round
   this part" fits. Nothing is forced onto noise.

7. **Sources and honesty.** The portal status is "Not solved", with no
   attached transcription or solution. SOLUTION.md credits the earlier GPT
   excerpt pass and Claude's completion truthfully, and keeps the earlier
   RHOULD reading on record. I know of no published solution.

## Findings

1. **minor – LONG: two marks sit in the smudge, not one.** In
   `review/work/z_long.png` the row-4 group after `---` is: one clean dash,
   then a grey smudge about 1.5 dashes wide crossed by a divider, then a clean
   dash and a dot. The reading `-. | --.` places the N's dot and the
   **first dash of G** inside the smudge. SOLUTION.md (item 3) and the
   transcript mark only the N as a judgment. The G is shown upper-case as if read cleanly.
   LONG is still the only sensible word, but the disclosure should say
   that two marks (`.` and `-`) are inferred from the smudge. The count of
   letters "read directly from clean marks" should be adjusted to match.

2. **minor – OMAR: say how tightly the signature is spaced.** The A's dot touches the
   divider on its right side (`z_sig.png`). The reading OMAR stands, but item 9
   could add that the dot of A sits on the divider. Item 9 should also make
   plain that OMAR may be a pet name and not a real given name. "Who the
   sender was is not established" already covers most of this.

3. **minor – presentation.** The `[LONGSTROKE]` is rendered as "— " in the
   plaintext. That is fine, but the report should state plainly that the stroke has no
   letter value, so a reader does not take it as a dash/T. The early
   NOTES.md entries (2026-10-26) have run-together words such as
   "rotate90forreading". They are hard to read but harmless, and NOTES is the
   solver's log.

No blocker or major findings.

## What I could not verify

- The scan is 1024 px wide (about 2.5 px per dot), and no higher-resolution
  original is available. The few marks under ink (W?ULD, the LONG smudge)
  therefore cannot be resolved by the pixels alone. They rest on the only word that fits.
- The meaning of the long stroke and of the looped blot (a cancellation,
  an "&", or punctuation) cannot be settled from one card.
- I could not identify the sender "Omar" or the recipient M. C. Hutton
  from outside records.
