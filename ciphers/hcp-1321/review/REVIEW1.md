ACCEPT

# Review 1 of hcp-1321 (pc_hcp_2)

Reviewer: Claude Opus 5.5, 2026-10-30. Solver: Claude Opus 5.5. The same model did both roles, so this is not a cross-vendor review.

The reading **SON & HEIR ARRIVED LAST NIGHT** stands. I tried to break it on the pixels and by search and could not. The findings below are minor and need no re-review.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1321/work/decode.py` from the repo root: hashes OK, output `SON & HEIR / ARRIVED LAST / NIGHT`, 23 signs, 13 distinct. This matches the claim.
2. **Key consistency.** Key and transcription are one-to-one, and all 23 signs are keyed. The word gaps in the transcription match the gaps on the card. The 3.3e-05 figure is arithmetically right: 6!/(13!/(2!2!2!3!3!1!)) = 720/21621600.
3. **Transcription, sign by sign.** I made my own contrast-stretched 6x to 12x crops from `work/hires/pc_hcp_2_adr.JPG` (`review/work/crops.py`, `L1a`, `L1amp`, `L1b`, `L2a`, `L2b`, `L2c`, `L3`) and read all 23 signs before comparing:
   - Line 1: diamond with centre dot; angle with blob at the end of the upper arm; angle with blob on the lower arm; scribble; circle with dot upper right; tilted triangle with dot near the apex; circle with dot on the left wall; tilted diamond with dot in the upper-right corner.
   - Line 2: square with dot top left; two diamonds with dot at the top corner; circle with a dot or short bar from the left wall; caret with no dot; triangle with the dot merged into the apex; square with dot bottom right; angle with heavy vertex; parallelogram with dot top left; diamond with centre dot; diamond with heavy bottom.
   - Line 3: angle with blob on the lower arm; circle, left wall; triangle with dot lower right; circle, dot upper right; diamond with heavy bottom.
   - Every sign agrees with `work/transcription.txt`. The three disclosed merges look sound on the pixels. Circle-top in lines 1 and 3 is the same position in both, so that merge is safer than the solver says. In the two line 2 triangles and diamonds the dot is partly fused with the top corner, which the solver's description covers.
4. **Independent decode without the solver's key.** `review/work/independent.py` holds my own sign classes. `review/work/filter.py` searches words against the repeat pattern only. Word lists: web2 plus regular inflections, and a 3,611-word list of words common in this repo's SOLUTION.md files (output in `filter.out`).
   - Merged sign classes, common words: 4 solutions. They are *son heir arrived last/past night* and two nonsense *sol ... light* strings.
   - Large list: 72,048 solutions, almost all nonsense. 15 of them also keep every shape in an unbroken alphabet block, and the only sentence-like ones are the *son heir arrived ... night* family.
   - Merges split one at a time: nothing grammatical. All three split: 17 solutions shown by the list, word salad such as *run obed accepts mary newly*. So the merges are needed for sense, and no rival sentence appears.
   - A first run of my filter found nothing, because web2 has no inflected forms and so no ARRIVED. That was my tool's fault and I fixed it. It does show how hard it is to reach this result by accident: the reading was not found by a loose dictionary fit.
5. **Coverage.** All 23 signs are decoded. There are no restorations, no unkeyed signs and no skipped passages. The scribble is the only non-sign mark in the block.
6. **Language and context.** "Son and heir" is a set phrase of the period, and "arrived" for a birth is normal usage. "All news later" right after it fits. Picture side confirmed: "6073 The Lake. Chislehurst.", no handwriting. Address confirmed: South St. House, Meopham, Kent. The stamp is the Edward VII halfpenny, so the 1902 to 1911 range holds.
7. **Sources.** No attached solution per the capture. The solver states that it made no web search for a published solution. No Fortescue, Meopham or Chislehurst card elsewhere in the repo. The "triangle" hits in other SOLUTION.md files that I sampled (hcp-1293, 1298, 1315) concern a printed triangle in the stamp place, not cipher signs.

## Findings

1. **Minor: the clear text has four brackets, and SOLUTION.md shows two.** The card reads "(it's not altered.)" with a closing bracket at the line end, then a new bracket pair "(Tomorrow Friday evening)". See `review/work/paren.png` and `review/work/tom.png`. The opening bracket of line 3 sits on the printed "only" at the far left and is easy to miss. SOLUTION.md merges them into one aside: "(it's not altered. Tomorrow Friday evening)". The Slovak follows the same error. Fix both. It changes the phrasing a little: two separate asides, one about the 6.40 and one naming the day.
2. **Minor: the value L is a single-use sign and is not disclosed as such.** The vertex angle occurs once. *Arrived past night* satisfies every constraint, including the block rule (N, O, P as the angle block). Only idiom picks LAST. The solver flags the same weakness for caret V but not here. D (ARRIVED), G (NIGHT) and O (SON) are also single-use. O is partly controlled: *sol* is excluded because the same sign is N in NIGHT, and *sol ... light* is nonsense. Add one line to the uncertainties. The reading does not change.
3. **Minor: "This check does not depend on the language" is overstated.** The block check needs the letter values, which come from the English reading, and it was computed after the fact on the key that suggested it. It is still strong evidence, but it should be described as a check on the key given the reading. It also relies on the three merges.
4. **Minor: reproducibility of `work/search2.py`.** It reads `corp.txt` from a session scratchpad, which is not in the repo, so the "searched both ways" claim cannot be rerun from the directory. The script does test all 8 merge combinations, as claimed. My own `filter.py` covers the same ground. The report may cite that or the corpus may be noted as unavailable.
5. **Minor: small inconsistency in the Slovak.** The closing is `V[?] atď.`, while the English has `Y[?] etc.`. Use the same letter, or state that it is a translation guess. My crop (`review/work/sig.png`) shows "Y" plus one more letter, then "etc.", all under a flourish. The solver's caution about this is right.
6. **Minor, optional: addressee initial.** In `review/work/initials.png` the first initial has the same form as the S of "St." on the next line, so S. E. is the better reading against the portal's J. E. SOLUTION.md leaves this open, and it could say which way the evidence leans. Not proven, since no J by this hand in the address is available for comparison.

No blocker or major finding.

## What I could not verify

- The place and date of the postmark. Single letters are visible on the stamp ("A D", "R A"), but I could not get a place from them, so the solver's "not read" is fair. A date would also bear on "Tomorrow Friday".
- The struck-out word before 6.40, the second letter after "Y", and the monogram (J. B., A. B. or S. B.). All three are disclosed.
- The scribble as "&". On `review/work/L1amp.png` it is a looped mark, unlike any shape sign. "&" is plausible, but there is no other "&" by this hand to compare. It is disclosed as resting on word sense, and no enciphered letter depends on it.
- Whether a published solution exists. Neither the solver nor I searched the web.
- The identity of P., the sender and the child.
