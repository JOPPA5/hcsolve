ACCEPT

# hcp-1191: Review round 1 (Claude Opus 5.5, reviewer, 2026-11-03)

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1191/work/decode.py` from the repo root. The source hashes check out ("source hashes OK"), and the output is byte-identical to `work/plaintext.txt`.
2. **Independent decoder.** `review/work/my_decode.py` has its own code→letter table, which I wrote from my own reading of the scan, not from `key.tsv`. Run as `python3 -I ciphers/hcp-1191/review/work/my_decode.py ciphers/hcp-1191/work/transcription.txt`, its output is identical line for line to the solver's plaintext. Every code in the transcription is covered by the key, with no KeyError. In total there are 269 cipher signs plus the clear date digits "5 1907". All 20 lines decode to English.
3. **Transcription against the pixels.** I rotated the un-converted hi-res message scan 90° CCW (`review/work/up.jpg`) and read it in bands (`band00`…`band09.jpg`, about 1:1). I enlarged the doubtful places 3–4x: `we.jpg` and `we_sep.jpg` (violet-ink separation under the collection stamp), `l7mid.jpg` (TO / ghost stroke), `l6end.jpg`, `roun.jpg`, `gotny.jpg`, `same.jpg`, `line1name.jpg` and `tail.jpg` (curved last line). I checked every row sign by sign against the transcription:
   - Header: square-on-stem, θ, dome = SET, then "5 1907" in clear. Confirmed.
   - Line 1, WELL ?OS I THOUGHT: the Y-shaped sign is unique and distinct from the asterisk of JAKE. Confirmed as written.
   - Line 3, the blot in L?NE: the blotted sign has a dark X-like core and is compatible with I. It is disclosed as a restoration.
   - Line 4, WE under the stamp: after ink separation, a circle with a left stroke and a circle with a bar are visible. The reading is acceptable.
   - Line 7, TO: the T is a faint lens/dome on an abraded patch, followed by a clear ø-type O. A pale ghost stroke stands before 7 (P). The solver's handling is fair and disclosed.
   - Line 10, ROUN: the first sign is overwritten. A cross is visible inside a loop, compatible with + (R). The rest is O, U and N. Disclosed.
   - Line 12, GOT NY ... PAINT: the bowl sign really differs from the dome. NY has a clean ㅂ-shaped N.
   - Lines 14–20 (GUESS ... FROM PETE AND EDNA, including the curved tail): all confirmed. The tail reads A N D E D N A going up the right-hand edge.
4. **Language and context.** This is natural rural American English of 1907 ("a Sunday" = on Sunday, "buggy", "so close", "goodby"). The writer's spellings (HOPEING, SATDAY, ROUN, GOODBY) are typical of a semi-literate family letter, not of words forced onto noise. JAKE fits the recipient J. E. Fortune. The date of Sept. 5 fits the Coshocton postmark of Sep 6, 1907 and the Canal Lewisville receiving mark of Sep 7.
5. **Steganography / other sides.** I viewed the address side at full card size (`review/work/adr_small.jpg`). It is a US one-cent McKinley postal card with an imprinted stamp, so nothing can be hidden under it. It shows the clear address "J E Fortune, Canal Lewisville, O." (the L of Lewisville is overwritten), two postmarks, a small orange mark and the HCPortal stamp. I found no hidden or extra writing. There is no picture side, so the type is plain **MASC**. "MASC + Steganography" does not apply to this card.
6. **Published solution.** None is attached on the portal, and the solver's search found nothing. I have no evidence of undisclosed use.

## Findings

1. **minor – wrong counts in "Why I believe it is correct".** The solver claims WELL 7× and ALL 4×. My count over the decoded text gives WELL 5× (lines 1, 5, 6, 11, 13) and ALL 3× (lines 5, 13, 15). The intro also says "about 330 signs", but the transcription has 269 cipher signs. None of this affects the reading, but the evidence should be stated accurately.
2. **minor – undisclosed mark at the end of line 6.** After "WE" (SANE WELL WE) there is a short curved stroke "(" (`review/work/l6end.jpg`). It is smaller than the crescent D in SUNDAY and AND, and most likely a line-end divider. Nothing in the transcription mentions it. One sentence in the uncertainties should say it is taken as a divider and not as D (WED would make no sense).
3. **minor – the N in SANE is not a clean ㅂ.** In `review/work/same.jpg` the sign has extra strokes, so it looks overwritten or corrected. SOLUTION.md item 7 calls it "identical" to the N of NOT, SUNDAY and CAN. The N in NY is clean. The literal reading N (writer's slip for M) can stand, but it should say that the sign in SANE is overwritten, which may also have been an attempt to correct it to M.
4. **minor – "?OS" remains the only unread word.** It is a single name in the salutation and the rest of the card reads, so under this run's rules the card counts as complete. The solver is right to leave it literal. "JOS" (or a nickname) is a hypothesis only.

## What I could not verify

- The exact identity of the Y-shaped sign in line 1 (a single occurrence).
- The I under the blot in LINE and the faint T of TO in line 7. Both rest partly on word sense, and both are disclosed.
- Whether the R in ROUN was originally another sign before it was overwritten.
- The real people (Pete and Edna, J. E. Fortune / "Jake" of Canal Lewisville, Coshocton County). I did no genealogical search.

## Verdict

ACCEPT. One key decodes the whole card into coherent period English that fits the postmarks and the recipient. The transcription matches the scan at every point I checked, and the uncertainties are disclosed. The four minor findings are corrections to the wording only. Register type: MASC.
