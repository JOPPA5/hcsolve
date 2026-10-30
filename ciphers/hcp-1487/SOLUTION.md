# HCP 1487 / pc_hcp_168 — PARTIAL decipherment (no DONE marker)

Status: **partial**. Not handed to review. Portal status Not solved; no
supplied transcription or solution; no published solution found or used.

## Card
Pine Bush, N.Y., postmark Aug 31 1908 4 PM; to Miss Florence Miller,
Crawford, N.Y.; picture "On the Bend, Pine Bush, N.Y.". The cipher (pencil,
9 short rows of geometric signs on the message half; plain "P.M." in row 5)
is on the address side. HC Portal **#55 is the same physical card**; its clean
photo (ciphers/hcp-55/source/postcard-large.jpg) was used as reading copy.

## Cipher type
Monoalphabetic substitution with an ad-hoc set of geometric signs (lines with
ticks, arcs, circles, boxes, H-shapes), commas mostly between words. No
match with Pigpen variants or other sister alphabets in this repo.

## Key established (see work/glyphs.md for every sign)
Good/medium: a = –, e = ∩ with bar above, f = ∪ with bar below (medium),
g = ∟ (bar with left up-stroke), i = ⊣, l = circle on a line, m = ⊕
(medium), n = ∩, o = ∪ (medium), r = □, t = ⊠, v = θ-oval (medium),
w = crossing arcs. Weak/conflicting: u, s, y, h; about nine signs unresolved.

## Partial reading
Command (repo root): `python3 -I ciphers/hcp-1487/work/decode_partial.py`
(checks source hashes and prints the partial decode of work/transcription.txt)

```
R0: [EYE][HT].
R1: m[HT][ZIG]t, [DOTBAR][...hidden by postmark...][XLOOP]
R2: int, [HH]o[HX],
R3: again, for,
R4: I, am leavin[VEE]          -> "I am leaving"
R5: on, P.M. train
R6: fo[BOXMID], g[PBOX]e[HH][DOTBAR][CIRC][HT]rt,
R7: will, write
R8: [BOXDOT]o[OSLASH], t[NEQ]e[PBOX]e. [H]
```
Secure words: "again, for I am leaving on [ ] P.M. train ... will write".
Plausible but not proven: R1 "must" (HT = u, ZIG = s), R8 "you" (but that
needs a second sign for u) and "there"/"these". English translation of the
secure part: "... again, for I am leaving on the ... P.M. train ... will
write ...". Slovak: "... znova, lebo odchádzam ... vlakom o ... popoludní
... napíšem ...".

## Why it stops
1. Row 1, second word: several signs lie under a second (unread) circular
   postmark and its cancel; not recoverable on either scan (also tried hue
   separation). This alone rules out a complete reading.
2. About nine signs (HT, HH, HX, ZIG, DOTBAR, CIRC, PBOX, BOXMID, NEQ, EYE,
   BOXDOT, OSLASH) occur only 1–3 times; the candidate words for R0, R2,
   R6 and R8 give conflicting values (e.g. HT = u in "must" vs OSLASH = u in
   "you"; R2 "int" and R6 "...rt" fit no word with the established key).
   Assigning them would mean forcing words onto noise.

## Credits
Earlier triage (metadata, sources, no reading) by an OpenAI GPT solver
(GPT-6 Astra / GPT-6.1 Sol), 2026-10-26. Transcription, key and partial
reading: Claude Opus 5.5, 2026-10-30.
