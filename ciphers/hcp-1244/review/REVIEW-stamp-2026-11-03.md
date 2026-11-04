CORRECTIONS

# HCP 1244: review of the stamp-box message (2026-11-03)

Reviewer: Claude Opus 5.5, independent check of SOLUTION.md section "Stamp-box message (2026-11-03)". The human (Tomáš Pavuk) ordered it. I did not change any solver file, source file or marker.

**Result.** The message text stands as claimed: *Csókolom a távolból szeretettel, Feri. Holes Ferencz.* I found no letter that should change. The corrections are to wording and disclosure only (items 1–3 below). The type change to **MASC + Steganography** is justified.

## What I checked and how

- Original: `work/hires/cpc_1912-04-10_HU__HU_Jasz-Arokszalas_jolanka-16_adr.jpg` (3445×2210).
- I made my own crops with `review/work/stamp-2026-11-03/crop.py`, run with python3 -I under the codex runtime Python, which has PIL. Each crop was enlarged 3–7× and some were also split into the green or blue channel. I did not open the solver's crops in `work/stamp-2026-11-03/` before reading.
  - `overview.png`: the whole address side
  - `box.png`: the stamp box
  - `l1.png`, `om.png`: line 1
  - `l2.png`, `l2tear.png` (green channel), `l2right.png`: line 2
  - `l3.png`, `l3g.png` (green channel): line 3
  - `l4.png`, `l4g.png`, `l4mid.png`, `l4mid_b.png` (blue channel): line 4
  - `l5.png`, `l5g.png`, `feri.png`, `feri_b.png`, `feri2.png`: line 5
  - `sig.png`: the signature
  - `addr_kis.png`: the address word, for comparing the s
- **Steganography.** The stamp is gone. A torn, fibrous patch at the upper left of the box marks where it was lifted. Inside the dashed stamp frame, over the printed blue emblem (circle, wreath, "P.", "R. A."), there are five lines of red handwriting and a purple signature. The writing sits where the stamp covered it. So a message hidden under the stamp exists, and adding "+ Steganography" to MASC is justified. `register-entry.txt` already reads `type: "MASC + Steganography"`, and the report and NOTES agree.

## My reading, sign by sign

| line | what I see | my reading | claim | agrees |
|---|---|---|---|---|
| 1 | c s o k o l; then a small o and a zigzag running down the right edge (`om.png`) | csokolom (the o and m are cramped, the m is written downwards) | csokolom | yes |
| 2 | round a; a stroke going up into the tear; the tear; then a cramped wavy run of loop, wave and wave, joining the descender of line 1 (`l2right.png`) | a t[á]vol | a t[á]vol | yes, but see item 2 |
| 3 | tall looped stem with a bowl, o, looped l (b/h, o, l); then a pointed sign: up, peak, down with a hook. Then z and e (`l3g.png`) | ból sze | ból sze | yes |
| 4 | n-like r; e; a tall stroke with no open loop, its up and down strokes laid over each other, darker (`l4mid.png`, `l4mid_b.png`); e; a tall stroke ending in a bowl at the lower right | retet | retet | yes, but see item 1 |
| 5 | faint pink t and e, then a bright red looped l; a red cursive capital F with a wavy cap; purple marks on its foot; a purple n-like r; a purple i with its dot (`feri2.png`) | tel F(e)ri | tel F(e)ri | yes |
| sig | Holes, then F with a detached T-like top bar, e, r, e, then strokes fading under the postmark (`sig.png`) | Holes Fere… | Holes Fe…, completed as Ferencz from sister cards | yes (disclosed) |

The pointed sign in line 3 matches the pointed s of *kis-* in the address (`addr_kis.png`). It does not match the round a of line 2. The reading *az e-* gave no word, and *sze | retet | tel = szeretettel* does. The enciphered word below the address, *szeretettel*, is independent support.

## Differences

1. **minor: how the line-4 t is described.** SOLUTION.md (and report.md line 107) call the third sign of *retet* "a tall looped stroke", the same form as the writer's t. In my crops (`l4mid.png`, `l4mid_b.png`) the sign has **no open loop**: it is a single tall stroke, retraced. This writer's l is clearly looped: the l of *ból* in line 3 and the l of *tel* in line 5 both show an open loop (`l3g.png`, `l5g.png`). So the pixels favour t over l more than the solver claims. The judgement is still sound, but the description should say "unlooped, retraced tall stroke, unlike the looped l". The solver also points to "the t opening line 5" for comparison, which is not apt. That t is a low, faint pink stroke with a red blob above it (`l5.png`), not a tall looped stroke.
2. **minor: disclosure for *-vol*.** The claim restores only the t and á of *távolból* and implies that *vol* is read. In my crops the part after the tear (`l2tear.png`, `l2right.png`) is one cramped wavy run: a loop, then two waves, then a join into the downward m of line 1. It fits *vol*, but I cannot separate v, o and l sign by sign. Its reading leans on the HCP1278 formula as well. The disclosure should say that *vol* is a compressed run read with the help of the formula, not separate legible letters.
3. **minor: the b of *ból* has dropped out of the disclosure.** Item 13 of 2026-11-01 says the first letter of *ból* "looks like h or b; b by sense". The new section's "What stays unread or restored" no longer mentions it, and item 13 is marked as superseded. The first sign of line 3 is still a tall looped stem with a bowl that could be h or b (`l3g.png`). The caveat should be repeated in the new section.

No difference in letters. *Feri* (the e is not seen) and *Ferencz* (completed from sister cards) are correctly disclosed. The note that the reproduction script does not cover the stamp text is accurate.

## What I could not verify

- The t and á of *távolból* are in the tear. Nothing I can see confirms or refutes them.
- Whether the purple lump on the foot of the F holds an e. My channel separation did not settle it.
- The end of *Ferencz* under the postmark.
- My sister-card comparison: I did not open HCP1278, 1268, 1303 or 1309 in this review.
