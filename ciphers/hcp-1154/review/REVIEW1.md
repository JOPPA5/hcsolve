ACCEPT

# Review 1 of hcp-1154 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands. My own sign-by-sign reading of all 116 cipher signs gives the same token stream as the solver's. Only minor points remain, and they can be fixed without another review round.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1154/work/decode.py`: hashes OK, 116 signs (110 family, 5 sister, 1 by sense), assertion passes, output matches the plaintext in SOLUTION.md. The script only asserts the cipher part. The clear text is hard-coded, as SOLUTION.md says.
- Read the heading and all 7 cipher rows myself from the hires address scan at 2x to 5x (`review/work/crop.py`, `crop2.py`, `crop3.py`; crops in `review/work/crops/`) before comparing. Typed the rows without word division into `review/work/my_decode.py`, with a table built from the sign list of FINAL hcp-1174 plus the four sister signs. Result with `3.` taken as written, identical token for token to `work/transcription.txt`:

      kedvesmargitkám / kedves / margitkámnemhiszem / hogynemharagudnálne /
      istagadmevttegnapész / revettemasztpedigel / seképzeledhogyfájez / nekem

  116 signs, 24 distinct, 111 on the FINAL table (including the `3.` written), 5 sister. This confirms the solver's "24 distinct" and "25 in the script".
- Disputed signs, each seen enlarged:
  - `haragudnál`: one high round dot after the 1, nothing low (`z_nal.png`), so `1'` = á. The following `6, 1:` is a true colon by contrast.
  - `.1` in the same word: dot left of the stem (`r2b.png`).
  - `tegnap`: one low dot (`r4b.png`, `z_3b.png`).
  - `hiszem`: plain 1, no mark (`z_2b.png`); `7.` with a clear dot.
  - `tagad`: the first 1 has a blotted low mark at the foot, the second a round dot (`z_3a.png`). Both are `1.`.
  - `aszt`: `7.` with a dot, no comma, no 9 (`r4b.png`).
  - `fáj ez`: plain `4`, high-dot `1'`, plain `6` with no comma under it (`r5b.png`, `r6b.png`); then `1: 9,`.
  - Row-end hyphens after `7.` and `5,`: real (`r3b.png`, `r4b.png`).
- Key coverage: every sign has a value. The 20 FINAL-table signs agree with hcp-1174, whose FINAL marker I checked, as also for 1178 and 1179. The four other signs agree with hcp-1161, 1162, 1163, 1164, 1166, 1168, 1169 tables; none of those seven is FINAL yet (six have REVIEWED1, 1162 has DONE1), as the solver discloses. Here each occurs in an unforced word, and nothing was fitted to this card.
- Language: natural 1915 Hungarian with no forced words. Cipher reads continuously from the salutation to `nekem`. `Kedves Margitkám` repeats as identical sign strings.
- Clear text read at 2x to 3x (`t1`–`t6`, `clr1`–`clr4`, `z_mind.png`): agrees with the solution, except as in the findings. The dot before `csókollak` that looked like an extra `i` is the full stop of `ablak.` in the row above (`z_cso.png`), so no word is missed.
- Address, postmark (`9 15 NOV 2`, next digit lost at the stamp; `pm.png`), date note (`1915 XI/29`; `pen.png`), and the signature `Sz. A.` above the rule all agree. hcp-1140 is also signed Sz. A. in clear. The picture side has no writing.
- Translations in English and Slovak checked against the Hungarian: faithful, except finding 4.

## Findings

1. **minor: `mert`, the argument for the odd sign is weaker than stated.** The mark after the 3 is a short slanted dot (`z_3b.png`), the same form as the dot of `3.` in the row-0 `kedves` (`r0.png`). Every comma in this hand has a long tail. So "a very short comma" does not hold: the card has `mevt`, which should be called a writer's slip for mert. The reading `mert` is safe by sense. The plaintext prints it without any mark, so flag it there, for example `me[r]t`, with the note that `3.` is written.
2. **minor: `más különben`.** The card has `más-` at the row end with a hyphen, then `különben` (`t4.png`). This is the single word máskülönben split at a row end. It should be given so, like the row-end hyphens listed in uncertainty 2. Translations need no change.
3. **minor: underline not disclosed.** A long drawn stroke stands directly under `téli` in the verse (`clr3.png`, `z_mind.png`). It is not mentioned. It looks like the writer's underline, and it should be noted either way. The word `téli` itself is secure.
4. **minor: `már` dropped in English.** `nagyon hideg volt már talán nem is igen megyek` has no punctuation, so `már` can end one clause ("it was already very cold") or open the next. The English omits it; the Slovak attaches it to the second clause ("už"). Keep it in both, the same way, and mention the ambiguity.
5. **minor: deleted word description.** Besides the opening stroke and accent, a small closed end loop and a hook above the opening also survive (`del.png`). I cannot read the word either. The sentence reads without it, so it does not affect completeness.

## What I could not verify

- The HistoCrypt article linked by the portal was not consulted by the solver or by me. The solver discloses this, so whether it treats this card stays open.
- The last digit of the postmark day: it is lost at the stamp edge, so 29 rests on the handwritten note alone.
- Whether the date note is pencil, as SOLUTION.md says: on the scan it is blue, close to the ink.
- Who Sz. A. is. Árpád of hcp-1174 is likely, but that is not established by this card.
- `Mindnyájatokat`: the letters look like `...nyoisatokat`, and the word is taken by sense as disclosed. It is the most natural reading and I found no rival.

## Conclusion

No blocker or major finding. The solver may address findings 1 to 5 in the response section and proceed to the PDF, the register entry and `FINAL`. MASC is the correct register label. The single unread word is a writer's deletion, and the whole card otherwise reads.
