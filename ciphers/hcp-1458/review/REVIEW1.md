ACCEPT

# Review 1 – hcp-1458 (pc_hcp_139)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Solution under review: SOLUTION.md (Claude Opus 5.5, 2026-10-29), DONE1.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1458/work/decode.py` (repo root) prints `source hashes OK` and exactly the
   claimed output (P LOVE MOLLIE / B1 ARE YOU / B2 GOING TO / B3 CARDIF / B4 NEXT MONTH / B5 TO HEAR THIS / B6 GENT / B7 ,).
   The script is a plain lookup in the standard Morse table; the only special token, `[BLOT]`, is skipped and decodes to nothing.
2. **Independent transcription and decode.** I read every stroke group myself from 4–7x crops of `source/address-large.jpg`
   (`review/work/r1a…r7b.png`, `r3mid.png`, `Pa.png`, `Pb1.png`, `Pb2.png`, `Pb3.png`), wrote the reading as tall/short
   (`review/work/my_reading.txt`, T/s notation, not copied from the solver's file) and decoded it with my own table
   (`python3 -I review/work/review_decode.py review/work/my_reading.txt`). Output is identical to the solver's line for line:
   `LOVE MOLLIE / ARE YOU / GOING TO / CARDIF / NEXT MONTH / TO HEAR THIS / GENT / ,`.
3. **Sign-by-sign check of all lines** (not a sample – the card is short):
   - B1: check-mark sT (A), sTs (R), s (E), stop; TsTT (Y), TTT (O), ssT (U), stop – clear.
   - B2: TTs TTT ss Ts TTs, stop, T TTT, stop – GOING TO, clear.
   - B3: TsTs sT sTs Tss ss ssTs, stop – CARDIF; only one ssTs group before the stop, so the single F is genuinely written.
   - B4: Ts s TssT T, stop; TT TTT Ts T [blot] ssss, stop – NEXT MONTH. The blot sits between T and H; no stroke can be seen in
     it, and none is needed. Disclosed by the solver (uncertainty 2); nothing restored.
   - B5: T TTT, stop; ssss s sT sTs, stop; T ssss ss sss, stop – TO HEAR THIS, clear.
   - B6: TTs s Ts T, stop – GENT, clear.
   - B7: TT ss TT, stop – one group at the foot of the card.
   - P (purple, faint, over the grey watermark): sTss TTT sssT s, stop; TT TTT sTss sTss ss s, stop – LOVE MOLLIE. The second L's
     two trailing shorts and the final I E sit next to the watermark letters A and B; at 7x with colour boost they are
     purple strokes distinct from the grey print (Pb2/Pb3). Readable, though this is the weakest part of the card.
4. **Key coverage.** One rule (tall = dash, short = dot, gap = letter boundary, written point = word end) accounts for every
   ink stroke group on the address side; there are no leftover or undecodable groups. There is no key to be inconsistent.
5. **Language and context.** "Are you going to Cardif[f] next month to hear this gent" is natural Edwardian English. The picture
   side carries the printed caption "Mr. George Alexander" (actor-manager, toured the provinces), so "this gent" fits; the
   recipient address (Miss Peggie Lewis, Post Office, Machen, "Nr Newpt: Mon.") is in Monmouthshire near Cardiff. No anachronism.
6. **Honesty.** The portal page captured on 2026-10-26 shows status "Not solved", no attached solution; the solver credits the
   earlier GPT triage truthfully and claims only its own work. I found nothing indicating use of a published solution.

## Findings

1. **minor – B7 is interpreted, not read.** `--..--` is the comma in later International Morse; I am not certain it already had
   that value in the 1904 Continental code (older tables give the comma as `.-.-.-`), so "comma" itself is partly an
   interpretation of the writer's intent, alongside the solver's "maybe meant ?" suggestion. The solver already labels the
   question-mark reading as interpretation; the report should say plainly that B7 is a punctuation-like closing sign whose
   exact value (comma / question mark / flourish) is uncertain. It does not affect the message.
2. **minor – sender attribution.** The open greeting on the picture side is signed "Sallie" (catalogue "Sollir"), while the
   Morse sign-off says "Mollie". The solver notes both but the report should keep these as two possibly different names
   (or Sallie writing on behalf of/with Mollie) and not merge them; the register `name`/description should not "correct" the
   catalogue's sender.
3. **minor – geography wording.** "Machen … about 13 km from Cardiff": Machen is nearer Newport (as the address line "Nr Newpt"
   itself says) and roughly 13–16 km from Cardiff depending on the point measured. Harmless, but phrase it as "between
   Newport and Cardiff".
4. **minor – the postmark date was not independently read.** The stamp postmark on the scan is not legible enough for me to
   confirm the day; "1904-09-11" comes from the portal metadata. State the source of the date in the report.

## What I could not verify

- The exact 1904 value of the B7 sign (see finding 1).
- The postmark day (see finding 4).
- Whether any stroke lies wholly under the ink blot in B4 (cannot be seen; not needed for MONTH).
