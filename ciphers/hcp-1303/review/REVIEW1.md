REVISE

# HCP1303, review round 1 (Claude Opus 5.5, reviewer, 2026-10-30)

The reading stands: every sign of the cipher text decodes to Hungarian that fits the card, and I found no sign that changes a word. Fixes are needed in the context and disclosure sections, chiefly the false statement that the card carries no date, and the sender's surname on the sister card HCP1309, which the solver missed.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1303/work/decode.py` from the repo root: all four SHA-256 checks print OK. The output matches the literal rows and normalized text in SOLUTION.md.
- **Independent decode.** `review/work/mydecode.py` holds my own sign-class transcription of all 16 rows and 5 stamp-box rows, plus the key typed from the HCP1216 legend. Result: 275 signs, all 21 rows equal to the solver's ledger (after removing accents, plain insertions and the stray dots). This was not blind: I had read the ledger first. Each row was still compared with crops, not copied.
- **Pixels.** Crops are in `review/work/crops/` (crop.py to crop5.py), made from the un-converted `work/hires/*_adr.jpg`. Every row was read at 3–4x. Rows 10, 12, 13, 14, 15, 16 and the plain lines were also read at 4–6x. crop5 uses the red channel to weaken the brown portal watermark.
- **Key coverage.** All 22 sign classes used here fall in the family table. No sign is unassigned and nothing is skipped.
- **Language and context.** The Hungarian is natural period colloquial with this writer's known habits (*szeretet* for *szeretett*, *soraim* formula, *ha van, írjon*; see HCP1309 *írjon, hogy mi újság Árokszállásba[n]*). Pest, Gyöngyös and Árokszállás fit. The English and Slovak match the Hungarian.
- **Family claims.** HCP1213 does close *Imádja Feri*; HCP1212, 1213, 1216 are signed Feri; HCP1212 and 1243 give 1912.
- **Sources.** SOLUTION.md discloses the key's origin. SOURCES.md hashes match. I saw no sign of an undisclosed published solution. I did no web search of my own. skip.txt and register-exclusions.json have no 1303 entry.

Spot checks of the solver's disclosed hard signs, all confirmed as described:

- r8 *de*: tall stroke + short tick (h/p class), not the short + long d of r1. Sense only.
- r14 start: hooked h.
- r14 h of *ha valaki*: two strokes through the watermark, the first longer.
- r13 blot before y: two heavy strokes, overwritten.
- r15 Á of *Árok-*: two bars with a tick visible inside the printed O.
- r15 end: k, s, z, a run under the watermark, each visible.
- r16 first sign: wave running into a long hooked descender. No plain l or y; *Árokszá|láson* fixes it.
- r16 j: heavily overstruck, base stroke visible, sense only.
- s5 f: tilted cross.

Restorations are all disclosed as editorial: *de*, *teh[e]ti*, *küld[je]*.

## Findings

1. **major. The card does carry date evidence; "The date is not on the card" (item 11) is false.** The round postmark upper centre, rotated 180°, reads `…ÁROKSZÁ…` in the ring, and in the date band a clear `13` stands at the right end (`review/work/crops/pm1rot.png`, `pm_c.png`, `pm_c2.png`). The rest of the band is under the pencil *Szépreményű*. A second, separate, heavy cancellation rings the torn stamp (lower arc with an `E`-like letter and a stroke, upper arc with `A`; `pm2.png`, `pmA.png`), and SOLUTION.md does not mention it. I cannot say whether `13` is a year (1913) or a day, nor where the second cancellation was struck. Fix: describe both postmarks, report `13` with that ambiguity, and remove the statement. If it is a year it fits the catalogued 1913 of HCP1213 and the April draft, but that is not established.

2. **minor. Sender's surname missed; item 11's "The card does not say who 'Holes' is" should be revised.** HCP1309 (same family, already reviewed in this run) has in cipher *…cím Holes Feri* with a plain return address (*Rákos Palota*), with the first letter of the surname open there as {H|P|D}. Here *cím Holes* is a return address in the same formula, so Holes is the writer's own surname in all likelihood, and this card's plain H strengthens the reading on 1309. Cite it as a cross-reference, not a proof.

3. **minor. The word after *Holes* is partly legible; "not readable" (item 10) is too strong.** With the watermark weakened (`crops/name.png`, `name2.png`) it begins with a crossbar capital, an F-type form, followed by a looped e, and runs on for several more letters, one or two tall, under the portal stamp. *Fe[…]*, plausibly *Ferencz* or similar, is a fair candidate; the ending is not legible. Also, the capital of *Holes* is not an obvious H: it has a crossbar and a foot stroke, closer to this writer's *J* in *Jolánka*/*Jász* (`addrJ.png`). "Clear" should become "read as Holes, capital uncertain", which is also what HCP1309 records.

4. **minor. The 4-like mark before *Népszínház* (item 10).** The mark has a closed upper triangle and a lower loop (`crops/p2.png`): a 4 or 8. Népszínház utca is in Budapest's VIII district from my general knowledge, so `8` (= kerület) is a candidate worth stating. I did not verify this in a source.

5. **minor. Undisclosed sign variant in r12 (*elfelejtettem*).** The f of *elfe-* is not the "upright cross +" of the key table: it is a slanted x with an added right arm (`crops/r12tail.png`), the same form as the stamp-box f of *Feri*. Item 8 flags only the stamp-box instance. Both f values on this card therefore rest on word sense; add r12 to the list and note the allograph, which differs from the plain x (u) of r7.

6. **minor. GY is not a separate sign here.** In r15 *Gyöngyös* the ledger token `GY` and the table's "joined loop + descender" describe what is really an enlarged g followed by the ordinary y sign, joined (`crops/d2.png`). The value is unaffected. A one-line note is enough.

7. **minor. Plain *10 er* (r10).** There is a tail after the r running into the following h/p sign, and a dot above *er* that may be an accent or a stray (`crops/c2.png`, `r10er.png`). The literal is at least *10 ér*; *10-ére* supplies a final e that is not clearly written. Item 9 mentions the normalization but should say that the e is supplied, as it does for *teh[e]ti*, and the normalized text should be bracketed accordingly.

## What I could not verify

- The full date in the postmark, the office of the second cancellation, and whether `13` is year or day.
- The word after *Holes*, the end of *szak…* (under my crop *sza* then k, followed by letters I cannot fix), and the plain word up the right edge (T, o, then uncertain).
- Whether *külj* stands for *küldj* or *küldje*.
- The h/p and d calls of the reading can only be settled by sense; the sense is unambiguous, though.
- Blind independence: I read the card after the solver's ledger.
