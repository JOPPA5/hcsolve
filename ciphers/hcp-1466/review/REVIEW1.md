ACCEPT

# Review 1 – hcp-1466 (pc_hcp_147)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Solver of record for this round: Claude
Opus 5.5 (2026-10-30); earlier triage by an OpenAI GPT solver (2026-10-26), credited correctly in
SOLUTION.md.

## Claim under review

The card is not a cipher: the numerals are English draughts (checkers) notation on the standard
1–32 board – move replies in seven simultaneous correspondence games from E. P. Dunne
(6 Manchester Rd, Warrington) to Mr D. Bryant (Rathmine, Milton Road, Portsmouth), postmarked
10 Oct [19]12.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1466/work/decode.py` – both SHA-256 checks OK,
   prints all seven games, "ALL MOVES GEOMETRICALLY VALID", exit 0. Output matches the table in
   SOLUTION.md exactly.
2. **Independent decoder.** `review/work/verify.py` uses my own transcription (typed from my
   crops, not from work/transcription.txt) and an independent 8x8 board model. It checks, for every
   move: one-step diagonal or two-step jump; side derived from direction; strict alternation of
   sides within each game's sequence; and that every jump captures exactly the square the opponent
   last moved to. Result: 22 moves, 0 problems, exit 0. My reading is identical to the solver's.
   Notable consistency: game 1 22-18 / 15x22 (over 18) / 25x18 (over 22); game 2 24-19 / 15x24
   (over 19) / 28x19 (over 24); game 7 23x16 (over 19) / 12x19 (over 16) / 22-18 / 9-14 / 18x9
   (over 14) / 5x14 (over 9). Such a chain of mutually consistent captures does not occur by chance
   in an arbitrary list of number pairs 1–32; the draughts reading is effectively certain.
3. **Transcription vs scan.** 3–4x crops in review/work/ (c_left, c_mid, c_right, c_g7,
   c_g4small, c_head, c_post, c_oct, c_stamp). Every entry checked sign by sign:
   - Game 1 large 22·18 / 15·22 / 25·18; small 6-10 (overlapping the "4" header) – confirmed.
   - Game 2 large 11·16; small 24-19 / 15-24 / 28-19 – confirmed; the "5" of 15 is blotted as the
     solver says, but 15 is the only square that makes the capture over 19 land on 24.
   - Game 3 29·25 (header "3" crossed by a long stroke) / 16-20 – confirmed.
   - Game 4 12·16 / 21-17; game 5 22·17 / 1-6; game 6 6·10 / 22-17 – confirmed.
   - Game 7 23·16, 12·19, 22·18 / small "9-14.18-9.5-14" – confirmed.
   No restorations or "completion" sections exist in this solution; nothing is forced from context.
4. **Context.** Heading "6 Manchester Rd / Warrington / Dear Sir / Replies as follows", closing
   "Yours F. Fully E. P. Dunne", address "Mr D. Bryant / Rathmine / Milton Road / Portsmouth" – all
   read the same in my crops. Numbered games with moves and replies is the standard form of a
   correspondence-draughts card; openings (11-15/11-16 family, 22-18, 12-16, 9-14 exchanges) are
   ordinary.
5. **Date.** Stamp is a George V ½d green with crown, POSTAGE/REVENUE and dolphins (Downey-type
   head, 1911–12 issues); postmarks read "10 OCT ·2" and "OCT .12". George V acceded 1910, so the
   portal's 1902 is impossible; 1922 is unlikely because the inland postcard rate then exceeded ½d.
   10 Oct 1912 is well supported.
6. **Sources/honesty.** No published solution is used; the portal lists the card as Not solved.
   Uncertainties (writer of the small entries, "F. Fully", initial D vs W, unknown prior positions)
   are disclosed.

## Findings

1. (minor) SOLUTION.md calls the game-7 small entry "pencil-like". In the crop it is the same
   small bluish ink and hand as the other small entries (only written on one line with "." as
   separator). Suggest describing it as the same small hand.
2. (minor) "George V profile ½d stamp (issued 1912)" – the stamp is the Downey-head type, first
   issued June 1911 (redrawn dies 1912). The date conclusion (1912) is unaffected; the wording
   could be "1911–12 Downey-head ½d, so not before 1911".
3. (minor) The large entries are not purely Dunne's own moves: game 1's large line contains
   Black's forced 15x22, and the small lines of games 2 and 7 contain White's forced recaptures.
   SOLUTION.md notes this for game 1 only; the plaintext table should make clear that each line is
   a move sequence (own move + forced replies), so the "Dunne (large) / small entry" labels are
   not read as "Dunne / Bryant" move-by-move. The decode.py output labels moves by colour, which is
   correct.
4. (minor) Register type: the card is draughts notation, not a cipher; if a register entry is
   written, the type should say so (e.g. "Draughts notation / not a cipher"), not a cipher family.

## What I could not verify

- Who wrote the small entries (Bryant on receipt, or Dunne's own reply-record) – unprovable from
  the scan.
- Full-board legality of the games (prior moves are not on the card).
- The exact closing word behind "F. Fully" and the recipient's first initial (portal "W. D.");
  the card itself shows "Mr D. Bryant".
- Identity of E. P. Dunne / D. Bryant in draughts club records (no external search done).
