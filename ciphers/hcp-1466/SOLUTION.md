# hcp-1466 (pc_hcp_147) – solution

Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Earlier triage (2026-10-26, OpenAI GPT
solver) captured the sources, read "Dear Sir / Replies as follows", saw seven numbered groups and
noted the values reach 28/29, but established no reading. Everything below was re-read from the scan.

## Cipher type and key

**Not a cipher.** The "ciphertext" is standard **English draughts (checkers) notation** – the
universal 1–32 square numbering of the playable dark squares (squares 1–4 on Black's side, 29–32 on
White's side; Black moves toward higher numbers, White toward lower). Key = that board numbering.
The card is a move-card from **seven simultaneous correspondence draughts games** between
E. P. Dunne (Warrington) and Mr D. Bryant (Portsmouth). Writing the card in numbers was ordinary
draughts practice, not concealment.

Evidence: every pair is two squares 1–32; every one of the 22 moves is a legal one-step diagonal
move or a two-step capture whose captured square is exactly the one the opponent's next move uses
(e.g. 22-18, 15x22 [over 18], 25x18 [over 22]); within each game the sides alternate correctly; the
opening moves are well-known draughts openings (11-15/11-16, 22-18, 12-16, 23x16 12x19 exchange…).
Dunne plays White in games 1, 3, 5, 7 and Black in 2, 4, 6 – the usual alternation of colours in
simultaneous correspondence play.

## Transcription (work/transcription.txt) and plaintext

Card text (English): *6 Manchester Rd / Warrington. Dear Sir / Replies as follows:*
then the games, then *Yours F[raterna]lly(?) E. P. Dunne.* Address: *Mr D. Bryant, Rathmine,
Milton Road, Portsmouth.*

Large black-ink lines (Dunne's hand) and small, lighter bluish lines (one small hand throughout).
Each line is a **move sequence** – a player's move together with any forced capture/recapture that
follows it – so a line can contain moves of both colours; colour is given by direction (W = White,
moving to lower numbers; B = Black, moving to higher numbers):

| Game | large ink line | small ink line |
|---|---|---|
| 1 | 22-18 W, 15x22 B, 25x18 W | 6-10 B |
| 2 | 11-16 B | 24-19 W, 15x24 B, 28x19 W |
| 3 | 29-25 W | 16-20 B |
| 4 | 12-16 B | 21-17 W |
| 5 | 22-17 W | 1-6 B |
| 6 | 6-10 B | 22-17 W |
| 7 | 23x16 W, 12x19 B, 22-18 W | 9-14 B, 18x9 W, 5x14 B (same small hand, written on one line right of the large line, "." as separator) |

English: "Dear Sir, my replies [moves] are as follows: game 1 …" (as above).
Slovak: „Vážený pane, moje odpovede (ťahy) sú nasledovné: partia 1 …" (ťahy ako vyššie; dáma –
anglická notácia polí 1–32).

## Command (from repo root)

    python3 -I ciphers/hcp-1466/work/decode.py

Checks SHA-256 of both source images, validates every move geometrically (step or jump, captured
square named) and prints the plaintext; exits non-zero on any illegal move.

## Uncertainties

- The small entries are in a different, smaller, lighter hand/ink. Most probably Bryant's (or
  Dunne's file-copy) note of the reply made to each move; who wrote them cannot be proven. Their
  digits are clear (game 2 "15-24": the 5 is slightly blotted, but 15x24 is the only capture that
  fits between 24-19 and 28x19).
- The game-3 header "3" has a stray stroke through it (overwritten 1/3 or a crossing line);
  ordering 1–7 makes "3" certain.
- Closing "Yours F. Fully" – probably "Fraternally" (common among draughts players) or
  "Faithfully"; signature read E. P. Dunne (portal: "E. P. Dunns").
- Date: postmark "10 OCT ·2" with a George V Downey-head ½d green stamp (first issued June 1911, redrawn dies 1912), so the card is not before 1911 → **10 Oct 1912**; the
  portal's 1902 is impossible. Recipient initial: card reads "Mr D. Bryant" (portal "W. D.").
- Game positions before these moves are unknown, so only local legality (geometry and consistency
  of captures within each card entry) is verified, not full board legality.

## Why it is correct

100 % of the numerals are accounted for; all 22 moves are legal draughts geometry, every capture
jumps exactly the square the opponent just occupied, and the context ("Replies as follows",
numbered games, two addresses) is the standard form of a correspondence-draughts card. No published
solution of this card was found; the portal lists it as Not solved.

## Response to review 1

Review 1 verdict: **ACCEPT**, four minor findings. All accepted; the reading (all 22 moves) is
unchanged. After the edits `python3 -I ciphers/hcp-1466/work/decode.py` was re-run: both SHA-256
checks OK, "ALL MOVES GEOMETRICALLY VALID", exit 0.

1. *Game-7 small entry "pencil-like"* – agreed. Re-checked the 4x crop (review/work/c_g7.png and
   source/address-large.jpg): "9-14.18-9.5-14" is the same small bluish ink and hand as the other
   small lines, only written on one line with "." separators. Wording fixed in the plaintext table
   and in the transcription header.
2. *Stamp issue date* – agreed. Wording changed to "George V Downey-head ½d green (first issued
   June 1911, redrawn dies 1912), so not before 1911". The date conclusion 10 Oct 1912 is unchanged.
3. *Large/small lines are move sequences, not one player's moves* – agreed. The plaintext table now
   heads the columns "large ink line" / "small ink line", explains that each line is a move plus any
   forced capture/recapture, and marks every move W/B. decode.py labels were changed from
   "Dunne (large ink)" / "small entry" to "large ink line" / "small ink line"; the move output
   (colour derived from direction) is unchanged.
4. *Register type* – agreed. The register entry uses type "Draughts notation (not a cipher)".
