ACCEPT

# Review 1 — hcp-1495 (pc_hcp_176), Caesar −1 postcard to Miss L. Cory, 1906

Reviewer: Claude Opus 5.5, 2026-10-30. Round 1 (DONE1).

## What I verified and how

1. **Command from SOLUTION.md.** `python3 ciphers/hcp-1495/work/decode.py` run from the repo root:
   source hashes pass, round-trip passes, 60 enciphered letters, output
   `Darling Leky / Thought you would / like this one your / collection, dear / Wours`,
   identical to work/plaintext.txt and to the plaintext in SOLUTION.md.
2. **Independent decryption.** review/work/decode_indep.py (str.translate table, no code shared with
   the solver) on work/transcription.txt: `diff` against work/plaintext.txt → IDENTICAL.
3. **Key coverage.** Every one of the 60 letters is handled by the single −1 shift; no letter is
   left out or special-cased; 12 words, letter count recounted by hand (7+4+7+3+5+4+4+3+4+10+4+5 = 60).
4. **Transcription vs scan.** Own crops from source/address-large.jpg in review/work/
   (greet.png, name.png, name2.png at 5–8x; blockL.png, blockR.png, l2–l4, l4b.png at 4x;
   pale.png, pale2.png, pale3.png at 7–10x; mono.png at 4x).
   - Ordinary rows: `Ebsmjoh`, `Uipvhiu zpv xpvme`, `mjlf uijt pof zpvs`, `dpmmfdujpo, efbs` all
     match the pixels. Writer's forms: U as two l-like strokes, z as a ȝ-shaped sign with descender,
     x as a "+" cross with a long bar, j with a long descender loop (looks g-like in "dpmmfdujpo"),
     f with upper and lower loops. The comma after "dpmmfdujpo" is on the card.
   - **Greeting name (claimed correction Mfmz→Mflz).** At 6–8x the sign after M has both a lower
     loop and an upper stroke, matching the f of "pof"/"mjlf"; the next sign is one tall narrow
     loop, the same as the l of "mjlf", not the two humps of an m. Last sign is the writer's z.
     I agree with **Mflz → "Leky"**. The correction is supported by the pixels, not forced by
     context (context would rather have pushed towards "Lily"/"Lely").
   - **Pale closing word "Xpvst" (completion added on 2026-10-29).** At 7–10x: a pale "+"-type cross
     (one steep diagonal plus a short vertical; the diagonal is not a watermark line – radial lines
     of the watermark wheel run nearly horizontally at that spot), then a p-like sign, a v, an s,
     and a final sign that is a vertical with a foot loop and a diagonal from upper right: **k or t
     are both possible**, as the solver says. Letter forms are cursive lowercase, unlike the dealer's
     block capitals "CODED MESSAGE". The reading is plausible and its uncertainty is disclosed.
5. **Language and context.** "Darling Leky, thought you would like this one [for] your collection,
   dear" is natural Edwardian English; the picture side (Lily Brayton & Oscar Asche, a stage
   photograph) fits a card for a postcard collection; date 21 Mar 1906 and the Gravesend address
   are consistent with an English card. "Leky" starts with L as does "Miss L. Cory".
6. **Sister material.** The same couple of conventions (Caesar +1 encryption, word division kept)
   occurs in the English −1 cards hcp-1386…1407; this card is from a different hand and year,
   so nothing was borrowed silently.
7. **Honesty.** Portal status Not solved, no attached transcription/solution; no published
   solution used. Credit split GPT (2026-10-26) / Claude Opus 5.5 (2026-10-29) is stated truthfully.

## Findings

1. **minor – normalised English presents an interpretation as text.** The line
   "English (normalised): … dear. Yours, [monogram]" prints "Yours" unmarked, while the literal
   output is "Wours" and the final sign may be k ("Wourj"). In the report and any normalised
   rendering write "[Yours?]" or "Wours (= Yours?)", and keep the k/t alternative visible.
   The same applies to the Slovak "Tvoj(a)".
2. **minor – punctuation after the first word not transcribed.** There is a clear dot between
   "Ebsmjoh" and "Mflz" (greet.png). It does not affect the plaintext, but the transcription
   claims to keep punctuation (it keeps the comma in line 4). Either add "Ebsmjoh." or note it.
3. **minor – attribution of "Xpvst" to the original writer is not proven.** It is in paler
   ink/pencil, set apart from the message block. The solver says this ("likely … but not proven");
   the report should keep that caveat, since the wrong-way shift (Y→X) is itself a sign that it
   could be a later hand's attempt. Not a reason to drop it, only to keep it labelled.
4. **minor – stale statement in NOTES.md.** The 2026-10-26 block still says "55 letters" and that the
   pale mark is "excluded from the main-message scope"; superseded by the 2026-10-29 block. Fine as a
   log, but the report should quote only the current count (60).

No blocker or major findings.

## What I could not verify

- The monogram flourish below the message (J/F/P/H ligature) – unread by the solver and by me;
  sender remains unidentified.
- Who "Leky" is; the name may be a nickname or a slip. Cannot be checked from the card.
- The partly obliterated postmark place ("…IDGE", plausibly Cambridge/Tunbridge etc.) – not
  needed for the decipherment.
- The original card (only the portal's 1024 px JPEG with watermark was available).
