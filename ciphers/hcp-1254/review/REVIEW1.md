ACCEPT

# HCP1254 review, round 1 (Claude Opus 5.5, reviewer, 2026-11-01)

The enciphered message reads as claimed. No finding changes the plaintext. All findings are minor and concern wording or disclosure. One decision is left to the human: finding 1, whether the lost plain-hand lines bar a register entry.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1254/work/decode_opus.py` ran. All four SHA-256 checks print OK, and the output matches the literal and normalized text in SOLUTION.md.
- **Independent decode.** `review/work/indep_decode.py` uses my own sign names, typed from my own crops, with the key restated from the HCP1216 table and not imported. All 15 rows are SAME as the solver's literal, over 194 sign tokens. Limit: I had read the ledger before reading the pixels, so this is a check, not a blind reading.
- **Transcription against pixels.** I read all 15 rows sign by sign on 2x crops of the hires address scan (`review/work/g1L..g5R.png`). I also made 3-4x zooms of the hard spots (`z_r02`, `z_r04end`, `z_r09`, `z_r12b`, `z_r13`, `z_r15`). Row 5 (cs) and row 10 (the end of *lannek*) I judged on the 2x crops only; the `z_r10end` crop was made but not opened. I found no sign that needed a different class.
- **Key coverage.** Every sign maps to the HCP1216 key except the two disclosed tokens: the small cross (row 4) and the heavy sign (row 15). The scored-out word in row 9 is not text. The h and p signs are near-homographs and are called by sense, as disclosed.
- **Language.** The text is coherent, idiomatic Hungarian of the period: *tudatom, hogy szerencsésen megérkeztem*; *áldozatokra is képes lennék*; *ki Önt tiszta szívéből imádja a távolból*. It is specific rather than a string of isolated words. The formulas recur in the family (*Isten vele, édesem* and *gondoljon néha rám* on HCP1217; *néha rám* also on HCP1250). The English and Slovak translations are faithful.
- **Address and postmark.** The address reads as claimed in clear. See finding 5 for the postmark.
- **Picture side.** I viewed it. There is only a printed Hungarian verse and no handwriting or cipher.
- **Sources.** The portal capture shows Not solved with no attached solution. No use of a published solution is evident, and the lack of a web search is disclosed.

## Restorations, judged on pixels

| Item | Pixels | Verdict |
|---|---|---|
| Row 5 *kics[it]* | i + opposed bowls, then s-z directly | Disclosed. *it* is supplied, not written. Fine. |
| Row 10 *l[e]nnék* | two bars, no third bar visible | Correct as a slip. Disclosed. |
| Row 12 *néh[a]* | row ends in h; row 13 opens with F | Supplied letter, correctly described. |
| Row 12 two heavy n | each a heavy overwritten shape plus a clean stroke | The stroke count fits n n. The heavy shapes do not establish n alone. Disclosed as partly from sense. |
| Row 15 j | heavy overwrite; a long stem and slanting base over what looks like a looped sign | Agree: j rests on sense. *imádja* is the only sensible word. |
| Row 2 o, h | blotted but the frame is clear | Fine. |

## Findings

1. **minor (human decision on the register).** The four rubbed lines under the stamp are a real gap. The status line, Uncertainties item 1 and the normalized text all say so honestly. My green- and blue-channel crops (`stamp_G.png`, `stamp_B.png`) recover no more than the solver's line ends. I see line 5 possibly as -lat, and nothing firm. The enciphered text is complete, and the lost lines are plain hand, physically smeared, between the legible frame *Csókolom ... számtalanszor, édesem*. My judgement is that this is not an unread decipherment clause, so the card counts as complete with a register entry allowed. The batch rule says "a whole unread clause is partial", so if it is meant to cover plain-hand notes, the card would get no entry; that call is for the human. Whichever way it goes, the entry and report must say that the plain note is partly lost.
2. **minor.** Row 13, *rám*: the sign is better called e than "e or a with a tick". Its third bar is short, like the short third bar of ordinary e in row 1, and accents in this hand go above the sign, not below. The literal is therefore *rem*, normalized *r[á]m* as a writer's slip, and it should be listed as such. The reading stands by sense. "Why it is correct" also says only the item 2 and item 8 signs lack a shape-based value, which understates this one.
3. **minor.** Row 4 cross: Uncertainties item 2 says it is "joined to nothing". At 3x its bar runs right up to the head of the tall stroke of the h of *hogy*, so it may be a false start of that sign. The word should be softened. The text is unaffected.
4. **minor.** "Why it is correct" claims *-ból/-ből* ×3. Only *szívéből* and *távolból* carry the suffix; the third *bol* is in *boldogság*. It should be ×2.
5. **minor.** Date: item 12 undersells the postmark. Turned 180°, the Jászárokszállás cancel shows `91` then a damaged digit space, MÁR, and day digits that begin with 2 and are compatible with 27, partly under the ink. So 1912 and March are supported by the card, not only by the file name. A second partial cancel beside the stamp is not mentioned and is unread. I could not confirm the day exactly.
6. **minor.** The third bar of the *á* in row 9 is not an issue, but the tick on the second *a* of row 15 is unexplained: the article *a* needs no accent. It should be noted as a stray or misplaced mark.
7. **minor.** Item 12 keeps the sender unknown, which is correct for this card. The report may add that family cards to the same addressee are signed Feri, as context and not as a reading. The picture side should be mentioned as printed verse only.

## What I could not verify

- The four rubbed lines and the deleted word in row 9.
- The exact day of the postmark.
- Any publication elsewhere: I ran no web search, and the register check is the orchestrator's.
- A truly blind transcription, since I read the ledger before the pixels.
