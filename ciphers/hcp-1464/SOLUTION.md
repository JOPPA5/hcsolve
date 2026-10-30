# HCP1464 — mirror writing, damaged-edge reading

Horizontal reflection of the address scan reveals:
```
I hope you
will like thi[edge]
from Joe.
Amen
```
Likely restoration THIS (terminal s partly cut at original left edge), not
claimed fully observed. Slovak: „Dúfam, že sa ti toto bude páčiť. Od Joea. Amen.“
Translation uses that restoration. Joe is a reading, not an identified person.
No cipher observed on picture. Lower dashes not interpreted as a second code.

Reproduce readable source pixels:
`sips -f horizontal ciphers/hcp-1464/source/address-large.jpg --out /tmp/hcp-1464-decoded.jpg`

work/decoded.jpg and enlarged edge crop allow comparison. This is an actual
pixel transformation, not text generated from a hypothesized plaintext.
Complete visible message largely readable; damaged terminal letter prevents
an unqualified full reading. No DONE1/FINAL or accepted review claimed.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading, handed to review (DONE1).** Cipher type: mirror
writing (horizontal reflection), with no substitution key.

> I hope you / will like this / from Joe. / Amen

In work/decoded.jpg the last word of line 2 shows `thi` and the start of a
final hooked stroke at the card's left edge (in the original orientation),
the usual cursive terminal *s*. Read **this**. Its tail is cut by the edge,
which is disclosed; *thi* alone is not English. The postmark on the
reflected image reads “DE 12 05”, i.e. 12 December 1905 (stamp and
cancellation, not cipher). Addressee as written: Miss L. Wood, Hayrick(?),
Northallerton, Yorks. The address is plain writing and is not reflected.

Slovak: „Dúfam, že sa ti toto bude páčiť, od Joea. Amen.“

## Response to review 1 — Claude Opus 5.5 as solver, 2026-10-30

Verdict ACCEPT, four minor findings. The reading is unchanged.

1. **Address (Hayrick → Kepwick). Fixed.** On a 2x crop of the original
   address (work/address-2x.png) the second line is plainly K-e-p-w-i-c-k.
   Kepwick is a village near Northallerton, a few miles from Felixkirk and
   Thirsk (the picture side). Corrected addressee: **Miss L. Wood, Kepwick,
   Northallerton, York's.**
2. **Postmark wording. Fixed.** "DE 12 05" is read on the *original* scan
   (it is mirrored on the reflected image). Date 12 December 1905, which
   matches the portal date 1905-12-12.
3. **Stale text. Superseded.** The first section ("No DONE1/FINAL or accepted
   review claimed", "not claimed fully observed") was written before
   handover by the earlier OpenAI GPT solver and is superseded by the
   completion section and this response; it is kept as the record. The
   single Slovak rendering to use is: „Dúfam, že sa ti toto bude páčiť. Od
   Joea. Amen.“
4. **Disclosure wording. Accepted and corrected.** At 5x in the original
   orientation (work/edge-original-5x.png) the word ends `t-h-i` (with the
   i-dot) followed by a heavy ink blot that runs into the card edge. It is
   *not* a recognisable letter form; my earlier phrase "the usual cursive
   terminal s" overstated it. Correct statement: the final *s* of **this**
   is restored from context ("will like thi-" admits essentially only
   "this") and from the presence of ink in the final-letter position; it is
   not seen as a letter.

Reproduction re-run 2026-10-30: `sips -f horizontal
ciphers/hcp-1464/source/address-large.jpg --out /tmp/hcp-1464-decoded.jpg`
gives a file byte-identical to work/decoded.jpg (`cmp` silent).

Final reading: **I hope you / will like thi[s] / from Joe. / Amen**
