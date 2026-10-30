ACCEPT

# Review 1: hcp-1371 / pc_hcp_52

Reviewer: Claude Opus 5.5, 2026-10-30. I tried to refute the solution. The reading of all 46 enciphered letters stands. Four minor issues remain, all about the literal initial groups or disclosure; none changes the decoded text.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1371/work/decode.py` ran with hashes OK and printed the claimed plaintext, 46 enciphered + 6 literal letters.
- **Independent decode.** `review/work/decode_rev.py` uses my own transcription typed from my own crops and mod-26 arithmetic, with no shared code or table. Result: MY OWN * BOY / LETTER TO-DAY / SPLENDID LOVE / * FROM YOUR / OWN * GIRL, 46 letters. A test of shifts 0 to 25 gives English only at shift 1, on the whole text. The key covers everything except the initial groups.
- **Hashes.** SHA-256 of the images in `source/` and `work/hires/` agree with `SOURCES.md`.
- **Pixels.** I rotated `work/hires/pc_hcp_52_adr.JPG` 90 degrees anticlockwise and read every word at 4x (`review/work/a1,a2,b1,b2,c1,c2,d1,d2,e1,e2.png`), and `oeje` at 8x (`x_oeje.png`):
  - `Nz.`, `Cpz`, `Mfuufs`, `up-Ebz.`, `Gspn.`, `Zpvs`, second `Pxo.`: agreed, no doubtful sign.
  - `tqmfoeje`: t with long bar, q, three-minim m, looped f, o, e, slash j with hooked tail and no loop, e. Agreed. Both e have ink-filled eyes (see finding 3).
  - Line 1 `Pxo`: the o is a solid oval, much larger than the stop after `Nz.`, so it is a filled o and not a stop. Agreed and disclosed. The same form is disclosed on hcp-1376.
  - `Mpwf`: the M here has less of a third stroke than the M of `Mfuufs` and is near the N of `Nz`. It is settled by the word, as uncertainty 6 says.
  - `Hjsm`: pale slash j with V-shaped tail, large s, flattened m that looks like "2u" (z in this hand also looks like 2). Reading is partly forced by the word; this is disclosed in uncertainty 5.
- **Context.**
  - 22 July 1907 was a Monday (computed), matching the heading.
  - Postmark reads ...ORNE, 10 PM, 22 JY 07 (`x_post.png`); the sign before O is partly hidden, so the solver's "...BORNE" is acceptable and rightly labelled as completed from sisters.
  - Address reads Mr. W. Abbott, Stokelake Farm, Chudleigh, Devon.
  - Plain date "July 22nd -07" is legible.
  - Picture side: printed "Crescent Gardens, Harrogate", no handwriting.
- **Language.** Short period endearment in the couple's formula. SPLENDID occurs on no other card in the family's formulae, so it is real independent evidence (a repo search finds it on only one other, unrelated SOLUTION).
- **Sources.** Portal metadata shows no attached solution. Nothing in the solver's files suggests an unstated published source. The user-supplied list of outside work does not include this number.
- **Completions.** This is a first-round card with no later "completion" section. No letter is restored; the only sense-assisted signs are those in uncertainties 3, 5 and 6, each disclosed.

## Findings

1. **minor: `N. h.` omits the closest parallel, and h is probably L.** Uncertainty 1 compares only with `E. L.` / `E.h.` cards, and concludes "h rather than L". hcp-1402 has the same slot with the same group, recorded as `N. L.` and described there as a two-arch N, then an L whose lead-in looks like a dash, slanted stem, small foot. Its crop `hcp-1402/work/v2/crops/nl_salutation.png` is sign for sign what I see in `review/work/a2.png` and `e1/e2.png`: arch N, short dash, slanted stem, small foot. So the "." in `N. h.` may be the lead-in of the second sign and not a stop. Fix: cite hcp-1402, and record the group as `N. L` / `N. h` undecided, or adopt `N. L.` as there. It is literal either way, so the plaintext does not change.
2. **minor: `& Lt..` support is understated, and the "same stroke order" claim is only partial.** The hcp-1386 sign (`work/crops/nl.png`) is a filled drop with a rising stem, and hcp-1399's is a reversed c, so the family's ampersand varies and this open hooked V is not the "same" form; only the direction of the strokes is shared. Stronger support is structural. The first member of the closing slot, `N.` / `M.`, is here apparently replaced by the spelled word `Mpwf` = LOVE, followed by `&` and an L group. hcp-1395 reads `M. & L.` as enciphered, giving L. & K., editorially "love & kisses". Together these favour `& Ks` = "& kisses" more than uncertainty 2 suggests. Fix: add this parallel. Keep it a labelled hypothesis, as now. The third sign is r-like as well as c-like; add r to the alternatives.
3. **minor: final letters of `tqmfoeje`.** The second e of the word has no open eye and looks c-like at 4x; c would give SPLENDIB. The e reading is right, but this sign is not listed. Fix: add one line to uncertainties.
4. **minor: pen marks omitted.** Hand-drawn lines run under `"tqmfoeje"` (ending in a blob, the j tail touches it) and under line 5 (from the date flourish). The first looks like underlining of the quoted word, which matters for the tone of the message. "All ciphertext on the card" is true, but the transcription should note them. There is also no need to treat them as cipher signs.

## What I could not verify

- The meaning and cipher status of the initial groups. No expansion is provable from this card.
- The first letters of the postmark town, which are worn or hidden. WIMBORNE comes from sister cards only.
- The identity of the writers, and any publication outside the portal, the repo and the register check. I did no web search of my own.
