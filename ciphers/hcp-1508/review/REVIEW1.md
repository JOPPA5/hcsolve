ACCEPT

# Review 1 of hcp-1508 (pc_hcp_189), reviewer Claude Opus 5.5, 2026-10-30

## What I verified and how

1. **Reproduction command.** `python3 -I ciphers/hcp-1508/work/decode2.py` (from the repo
   root) passes the SHA-256 check of all three `source/` files and prints exactly the
   plaintext in `SOLUTION.md`; its output is byte-identical to `work/plaintext-v2.txt`
   (`diff` empty). Counts: 201 numeral signs, 200 mapped, 1 unmapped (`2`), 5 letter-shaped signs.

2. **Independent decryption.** `review/work/mydecode.py` uses my own transcription,
   typed from my own crops, not copied from `work/`. It also derives the key itself, from
   12 cribs only: MY, DEAR, GIRL, THE, LOOK, PLACE, BUT, XX, FELT, AWFUL, WHEN, STOP. No
   crib conflicted, and the key is injective. Applied to the whole card, this key yields the
   same 22 values as the solver's key and the same text word for word: 201 numeral tokens,
   with only the signature's `2` unmapped. The key is identical to that of the FINAL sister
   cards hcp-1506 and hcp-1507 (same recipient, Knoxville PA, 1913). 14=K occurs twice on
   this card (LOOK, AWAKEN) and is also attested by hcp-1507's LOOK `6.7.7.14`.

3. **Transcription vs. scan.** All crops are in `review/work/`: autocontrast, 3–14x, made
   with `crops.py`.
   - Rows 1–20 (`r01-04.png`, `r05-09.png`, `r09-13.png`, `r14-20.png`): I read every word
     against `work/transcription-v2.txt` and found no discrepancy in the ordinary rows.
   - Restoration BN, `15.25` (`l4.png`, `l4b.png`, `l4went.png`):
     - The `g` descender of *morning* does run into the top of the second digit.
     - A short detached bar sits at the upper right, separate from the following dash, as on
       the 5 of WENT's `25`.
     - I agree that 25 is the better reading. Either 23 or 25 is a non-word, and BY is
       interpretation, so this is properly disclosed.
   - K sign in LOOK and AWAKEN (`l6look.png`, `awaken.png`): a curved stroke plus a looped
     4-like form, clearly different from the plain `2` of the signature (`sig.png`).
     Changing EKRA to E[2]RA is justified.
   - RI|NG, `4.17` (`ri.png`): the second digit has a top bar and a diagonal with no base
     stroke, so it is a 7, not a 2. RING is confirmed.
   - DO, `18.7` (`r14-20.png`): a clear `18.7` before `26.7.16`. The old IF reading was wrong.
   - BELL (`r05-09.png`): the final sign is 6-shaped under the watermark. 6 is acceptable.
   - WINDOW [N] (`window.png`): a letter-shaped N.
   - [V] ×3: a V/Y-shaped letter sign, not a numeral.
   - I AM: see finding 1.

4. **Language and context.** The text is idiomatic American English of 1913: a courting
   note with apology, buggy-bell detail, "Sat. eve" and closing kisses. It agrees with the
   postmark (KNOXVILLE JUN 13 1913 PA) and with the recipient, Miss Leah Doane, Little
   Marsh, Pa. The cursive plain words (*morning*, *Sat.*, *disappointed*, *you*) fit the
   decrypted text around them. This is not noise forced into words.

5. **Sources and honesty.** The portal status was Not solved, with no attached solution.
   I found no evidence of a published solution being used. GPT's earlier work is credited
   truthfully, and the earlier notes are kept as the record.

## Findings

1. **minor: the [I] sign of "I AM" is described inaccurately, and its control crop cuts it off.**
   - What the pixels show: `review/work/iam2.png` (14x, box 235,455–290,505) shows a
     small *closed loop* sitting on a faint downward stem, about at y≈476. Taken together
     the sign looks rather like a small `9`. The solid dot above it belongs to `1.3` (ME) on
     the line above.
   - What SOLUTION.md says: uncertainty 3 calls it "a single faint upright stroke".
   - The control crop misses it: `work/controls-v2.py` crops this row from y=478, which cuts
     away most of the loop.
   - Why it matters: as a 9 the word would be PAM, which is not a word. I AM therefore still
     rests on context, which is acceptable.
   - Fix: describe the loop, name the 9 (P) possibility and the possibility that the loop is
     stray ink, and enlarge the control box.

2. **minor: the signature `3.2.4.12`.**
   - E[2]RA ("probably Ezra") is honestly flagged.
   - Missing from the disclosure: on sister card hcp-1506 the same writer wrote a lone `2`
     for an intended `26`, giving [2]OU for YOU (see hcp-1506 REVIEW1, finding 2). So the
     `2` here could also be a truncated two-digit number, not a separate key value.
   - Requested change: the uncertainty should say so, and "only Z gives a name" should be
     softened to "Z gives the most plausible name".
   - What the card itself supports: no 2=Z entry belongs in the key, and the solver keeps
     none. The identity of the sender is not established. The portal names the sender of
     hcp-1506 as "Egna", and that cannot be read from these digits.

3. **minor: small wording inconsistency.**
   - The `decode2.py` docstring says every value "except 14 and 5" is attested on this card.
   - `SOLUTION.md` says "except 14", and then says 14 is attested twice here.
   - 5 indeed never occurs as a numeral here, and 14 does occur. Harmonise the wording.

4. **minor: the cursive word's spelling.**
   - On the scan it looks closer to "dissapointed" (double s, single p), as the solver
     already suspects.
   - It is plain text, not cipher, so this is cosmetic only.

## What I could not verify

- The sender's identity (Ezra?) and any relationship to Leah Doane beyond the three cards.
- Whether 2 is a deliberate key value or a writer's slip: it occurs only once.
- The exact strokes under the dark watermark bands (the last 6 of BELL, and the upper part
  of BN's second digit). Both readings rest on the visible parts plus agreement with the rest
  of the card.
