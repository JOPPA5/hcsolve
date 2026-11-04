ACCEPT

# Review 1 – hcp-1113 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Ran the solver's command from the repo root: `python3 -I ciphers/hcp-1113/work/decode.py`. All three SHA-256 checks print OK and the
   output is GELIEBTER / SCHATZ! / BIN ZUR / BESTIMMTEN / STUNDE / BEI DIR / DEINE / SUSI, identical to the claimed plaintext.
2. Independent reading and decoder: I cut the message area from the hi-res address scan (work/hires/..._adr.jpg, 3468x2298), rotated
   it 90 degrees (review/work/msg_rot.png) and read every number myself before comparing with work/transcription.txt. My own script
   review/work/indep_decode.py (A=2 ... Z=26, J omitted, written without reference to decode.py) gives
   `GELIEBTER SCHATZ BIN ZUR BESTIMMTEN STUNDE BEI DIR DEINE SUSI`. My reading agrees with the solver's transcription number for number
   (44 numbers, 10 words, 8 rows).
3. Enlarged crops (3–4x, review/work/z_*.png) of every disclosed point:
   - z_first.png: first sign is an S-shaped numeral with a separate rising top stroke. The 5 of DEINE (z_deine.png) has a different form
     (hooked top plus detached flag), so 5 is not a good fit; an open German 8 fits the shape. G is also required by word sense. Disclosed.
   - z_schatz.png, z_stunde.png: both noun-initial 19s carry a heavy diagonal stroke across them; the underlying 1 and 9 are visible.
     Decoding as 19 = S is forced (CHATZ / TUNDE otherwise). The "capital marker" explanation is an interpretation; a correction stroke
     is equally possible, but the decoded letter is the same either way. Disclosed.
   - z_bestimmten.png: 13 has a clear bar over it (MM); the last number is a retraced 1 plus a clear 4 = 14 (N). Confirmed.
4. Key consistency: one fixed table, identical to the one on sister card hcp-1134 (same recipient Fritz Lehmann, same signature Susi,
   both posted in Freiburg, Schlesien). Every number on the card decodes; no leftovers, no ad-hoc letters.
5. Language and context: fluent standard German, a short rendezvous note, entirely plausible for a 1909 love postcard; date 30.7.09 and
   FREIBURG (SCHLESIEN) are legible on the postmark (review/work/stamp.png), matching the file name and SOURCES.md.
6. Steganography check: stamp crop shows the Germania 5 Pf stamp still affixed, no ink at its edges; picture side (review/work/pic_small.png)
   carries only the printed Faust caption, "Gretchen" title and publisher mark. No hidden or extra writing found on either side.
7. Sources/honesty: portal status Not solved with no attached solution per source/metadata.md; the solver states the transcription and
   decipherment are its own and records a negative web search. I found nothing contradicting this.

## Findings

1. (minor) First numeral 8 vs 5: the call rests partly on word sense and there is no other 8 on the card. The solver discloses this
   correctly; no change needed beyond keeping the wording in the report.
2. (minor) The diagonal strokes on the two 19s: SOLUTION.md calls them "apparently a capital marker". A correction/over-writing stroke
   is an equally plausible explanation; the report should say the purpose is unknown and that it does not affect the decoding.
3. (minor) The plain Kurrent street name in the address ("Alte L...straße", review/work/street.png) is left unread. It is a single word
   in the address, not part of the message, so it does not make the card partial, but SOLUTION.md/report should state it as an unread
   word rather than "read loosely".
4. (minor, register) For the register entry, the type should be `MASC` (number substitution) – no steganography was found on this card,
   so `MASC + Steganography` does not apply.

## What I could not verify

- Whether anything is written under the stamp (stamp is affixed on the scan).
- The identity of "Susi" and of the street.
