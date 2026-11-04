CORRECTIONS

# hcp-1215 – review of the stamp-box message (2026-11-03)

Reviewer: Claude Opus 5.5 (independent pass). Scope: SOLUTION.md section "## Stamp-box message (2026-11-03)" and its "Type note".

## What I checked and how

- Original: `work/hires/cpc_1914-11-28_HU__HU_helyben-(locally)-Budapest_jolanka-57_adr.jpg` (3445 x 2210).
- My own crops, made with my own script `review/work/stamp-2026-11-03/crop.py` (colour, and auto-contrasted red channel, 3.5–6x), all in `review/work/stamp-2026-11-03/`:
  `overview.png` (1/4 scale), `box.png` (box 2680,120–3330,820 at 1.2x), `r12.png`, `r1_6x.png`, `r1_red.png`, `r2_6x.png`, `r2_red.png`, `r3_5x.png`, `r345.png`, `r4_red.png`, `r5_4x.png`, `r6.png`, and a comparison sample of this hand's *d* from the main text, `main_hidd.png` (row 2 "hidd").
- I did not open the solver's crops before reading the box myself.

## My reading (literal, from the pixels)

```
S1 [..]n      (n clear; the sign before it runs into the torn stamp margin, no e- or o-loop visible)
S2 veled      (v-e-l-e + d written o + detached tall stem, exactly as "hiol" = hidd on main row 2)
S3 s[z?][...] (s, then a two-hump sign; the rest under the triangle; a long up-stroke exits at right)
S4 hu[...]    (h, u; a blot to the right of u at the triangle edge – accent or triangle ink, not decidable)
S5 Im[...]l   (I, m, middle under the triangle, ends in a tall stroke: l, or the stem of an o+l d)
S6 Feri
```

## Agreements

- The stamp is torn away; its upper-left ("MAGYAR") and lower-left margins remain. The paper under it carries six rows in the same green cursive as the message, ending *Feri*. Writing under the stamp therefore exists (the steganographic element is real).
- No cipher signs occur in the box; it is plain Hungarian.
- A dark-green triangular sunburst with a blank central disc covers the middle of S3–S5. Its stippled, impression-like texture and the absence of any paper edge or perforation support the solver's new view that it is an inked mark rather than a stamp fragment. Channel separation does not lift the writing under it (same-colour inks) – confirmed on my red-channel crops.
- S5 *Im…l/d* and S6 *Feri* agree. Not restoring *Imádód* is correct.
- *Szombat[on]* across row 26 / S1 is correctly labelled a conjecture.

## Differences

1. **S2: the "l" is the stem of the d, not a further letter (minor, but it changes the text).** The claim reads S2 as "veled l" with a tall looped l "then bare paper". On `r2_red.png` the row is v, e, l, e, a small closed loop, then a detached tall leaning stroke. That is exactly how this writer forms *d*: compare `main_hidd.png`, where *hidd* is written "hiol" (loop + detached tall stroke), and the solver's own note that row 12 *tegeol* = *téged*. If the loop alone is taken as *d*, the solver counts the d-stem twice. S2 should read **veled** (complete), with nothing after it; the "l…" fragment and the English "with you …" gap after it should go. The normalized line becomes *…[szombat]on(?) veled szi… hű… Im…l/d Feri*.
2. **S1: only "n" is visible (minor).** On `r1_6x.png` / `r1_red.png` the clear part is a lead-in stroke rising out of the stamp margin and a two-hump *n*. No e-loop and no o-loop is visible; the vowel sits under the margin. "[..]en / -on" should be "[..]n", with *-on* (for *szombaton*) and *-en* both only possible. This does not change the conjecture, but "-en or -on" is presented as more than the pixels show.
3. **S3: "szi" is two-thirds read (minor).** I see *s* and a two-hump sign consistent with cursive *z*; there is no i-dot or separate i-stroke visible before the triangle edge. Write *sz[…]* (or *s[z]…*), not *szi…*.
4. **S4: the accent of ű is not established (minor).** *h* and *u* are clear. The only mark that could be the double accent is a blot right of the u at the triangle's edge (`r4_red.png`), which may as well be triangle ink. *hu…* is literal; *hű* ("faithful") should be marked as a guess from the shape, and the gloss "faithful(?)" kept clearly conjectural (the solver already flags it as read from two letters – this only adds that the accent itself is unseen).

## Type change

The task asked whether "MASC + Steganography" is justified. Writing under the stamp exists (confirmed above), so a steganographic element is present. But the solver did **not** apply "MASC + Steganography", and I agree: the box is plain Hungarian and no cipher sign occurs on the card (the overview of the whole address side shows only ordinary cursive; I found nothing to contradict the earlier "no cipher found" finding). "MASC" would be false here. If the register team wants the card labelled, it is plain text + steganography only, and with S3–S5 largely unread and no decipherment, the solver's decision to create no register entry stands.

## Not verified

- What lies under the triangle (S3–S5) and under the stamp margin at the start of S1 – not recoverable from this scan.
- Whether the triangle is a hand-stamp or something else; only its appearance was judged.
- The full main text was not re-read sign by sign (outside this audit's scope); only the absence of cipher signs was checked at overview scale.
