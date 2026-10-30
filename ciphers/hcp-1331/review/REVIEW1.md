ACCEPT

# Review 1 of hcp-1331 (pc_hcp_12)

Reviewer: Claude Opus 5.5, 2026-10-30. The solver was also Claude Opus 5.5, so this is not the two-provider check the README expects. All sign calls below were made on my own crops of the un-converted original.

## Result

The reading stands: a plain-English card with the private words written with dots in place of letters. All 8 dotted words, the 13 dots and the clear lines hold up on the pixels. I found no error in the plaintext. Six minor findings follow; none changes the text. Findings 1 and 2 add to the uncertainty list, and the rest correct small claims.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1331/work/decode.py` ran: hashes OK, 13 dotted letters, 9 lines of output, as claimed in SOLUTION.md.
- **Independent script.** `review/work/verify.py` holds my own transcription and a whole-word expansion table, written from my crops. Output: `identical dots 13 letters 140`, meaning identical to decode.py. This shows agreement only: on a card with no key, both are expansions by sense.
- **Word-list counts.** I compared the counts in the SOLUTION.md uncertainties with `work/candidates.txt`. They match: y.u 1, l..t 19, n.g.t 2, n.c.t 0, n.r.t 0, de...e 51, da...e 31.
- **Scans.** `work/hires/pc_hcp_12_adr.JPG` rotated 90 degrees and enlarged 3 to 12 times (`review/work/crops.py`, `crops2.py`, `blobs.py`; PNGs in `review/work/`).
  - Line 1: D . . 2-shaped r / O . looped d / B . y, underlined. Confirmed.
  - Line 3: 9-54 with a full stop, Did, M . s s, y . u. The 4 is a clear 4, not a 1. Confirmed.
  - Line 4: l . . t / n . hook . t / d, blotted sign with a white counter, three dots, e. Confirmed, with exactly three dots in the last word. See findings 1 and 2.
  - Lines 2 and 5 to 9: read in clear. Rehearsal, "did not have", Pole, last night, "rather silly I think", "yours with love Ada" all stand.
  - "Pole": I tested Role, since this writer's capital R looks P-like. In Rehearsal the R's bowl ends in a bar and a leg running into the e; here the bowl closes with no leg, and the o is a separate letter. So P, as claimed.
  - Dots near lines 6 to 8 (at about x 364, 671 and 739, y 1402 to 1449 in my rotated 1600-pixel frame) sit over the i of silly, think and night, displaced rightwards like this writer's other i-dots. They are i-dots, not concealment.
  - Watermark: the l..t dots lie under the grey ring and stay black, so the ring does not hide ink of that weight.
- **Thresholded blob counts** (`blobs.py`) were not decisive, because the threshold fragments strokes. The dot count of 13 therefore rests on my eye, not on that script.
- **Picture side.** Printed caption MISS MADGE CRICHTON, RAPID PHOTO E.C., 3623, no handwriting. Confirmed.
- **Postmark.** HORSHAM, 8 PM, AU 4, numeral 381. Only a fragment shows where the year would be; it is illegible, as the solver says.
- **Context.** Sender Ada and addressee F. Stuniger on the portal fit the card. Midhurst appears in both the address and the message.
- **Sources.** A grep of all `*/source/metadata.md` and `*/SOLUTION.md` finds the surname only in this directory. The card has no sister with this addressee.

## Findings

1. **minor: first sign of `l..t` could be taken for t, and this is not disclosed.** The sign has a stroke running across its stem, and it resembles the crossed t at the end of the same word. That would allow `t..t` = "that night" (31 word-list hits for t..t). I still read l. The upper stem is thick and doubled, which fits a closed loop, and the cross stroke does not continue right of the stem as the t's bar does; it is an entry stroke. "last night" also recurs in clear. The solver should add this to the uncertainties, since "last" is defended only against other `l` words. Crop: `review/work/first_l.png`.
2. **minor: the n.g.t hook has more evidence than SOLUTION.md gives.** Item 3 says the sign is a flat hook that looks like a tiny c or r, resting on word sense. Under it, in the grey ring, there is a thin, broken diagonal mark running down-left, the direction of this writer's g and y descenders. It may be an ink-starved tail, which would make the hook a real g, or it may be a speck. It is not a settled reading, but it should be mentioned. Crop: `review/work/hook_tail2.png`. If the hook were instead a misshapen dot, the word is still night but the dot count would be 14.
3. **minor: "the i is undotted" in Stringer (item 7) looks wrong.** A small black tick sits above and to the right of the middle of the name (`review/work/name.png`), which fits this writer's displaced i-dots. That favours Stringer over Strunger. It does not affect the message.
4. **minor: NOTES.md says hcp-1463 "shares the sender name Ada".** Its metadata gives Sender Unknown, recipient Miss Nicholls, and an ordinary address reading Miss Ada Nicholls. So Ada is the addressee there. The conclusion that it was not used stands, but the note should be corrected.
5. **minor: wording about what decode.py and the card check prove.** decode.py hard-codes both transcription and expansion, so "checks that every written sign agrees" is an internal consistency test, not a check against the image. "Every sign on the card is accounted for" is also not literally shown, as the i-dots are not mentioned. Add a line saying the other dots on the card are i-dots.
6. **minor: Easebourne as context.** The address has it in quotation marks, which suggests a house name rather than the village. The "adjacent places" argument in the last section is therefore weak; the word is better treated as unresolved.

## What I could not verify

- Why the writer chose those letters, or the meaning of "the Pole". Both remain open, and the solver says so.
- The year of the card. The Edward VII stamp is the only dating evidence the card itself gives.
- The Horsham assignment of numeral 381 from any outside source; I only see it struck beside the Horsham datestamp.
- That no solution exists elsewhere. I did not re-fetch the portal or search the web; the solver's capture and the orchestrator's register check are what I have.
- Whether 13 is the absolute number of dots, since an ink-free or wholly hidden dot cannot be excluded in theory.
