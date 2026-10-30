# HCP 1466 (pc_hcp_147): a correspondence-draughts move card from Warrington to Portsmouth, 1912

Human solver: Tomáš Pavuk

**Status: read in full – the card is not a cipher but English draughts (checkers) notation; all 22 moves in seven games read and checked; independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1466 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1466), portal name pc_hcp_147, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Unknown, date 1902-10-10, language Unknown, location Europe, sender "E. P. Dunns", recipient "W. D. Bryant", with no transcription or solution attached.

The picture side is an ordinary printed coloured view of two children by a pond under a blossoming tree, titled "Sweet Summer Time"; it carries no writing.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

All the writing is on the address side (a J.W.B. London "Commercial Series" postcard). In plain English it reads **6 Manchester Rd / Warrington / Dear Sir / Replies as follows:**, then seven numbered groups of number pairs, and closes **Yours F. Fully E. P. Dunne**. The address is **Mr D. Bryant / Rathmine / Milton Road / Portsmouth**. The stamp is a green George V halfpenny of the Downey-head type (first issued June 1911), and the machine postmarks read "10 OCT ·2" and "OCT ·12". The card was therefore posted on **10 October 1912**; the portal's 1902 is impossible, since George V acceded only in 1910.

![Address side: heading, the seven numbered games, signature and address (source/address-large.jpg)](../source/address-large.jpg)

The number pairs are written in two hands or inks: large, black entries in the sender's hand (22·18 etc., with a raised dot between the numbers), and small, lighter bluish entries in one smaller hand (24-19 etc., with a hyphen), set below or beside the large ones.

## Method

An earlier triage of the card (2026-10-26, OpenAI GPT solver) captured the sources, read the plain heading and noted seven numbered groups with values up to 28/29, but established no reading. On 2026-10-30 Claude Opus 5.5 re-read the whole card from 4x enlargements and transcribed every pair manually (no OCR; the portal supplied no transcription).

Every number lies between 1 and 32, the pairs are close together (22·18, 11·16, 29·25 …), and the card says "Replies as follows" with numbered groups. This is the form of a **correspondence draughts** card: in English draughts the 32 playable dark squares are numbered 1–32 (1–4 on Black's side, 29–32 on White's side), and a move is written as start square and end square. Black moves towards higher numbers, White towards lower ones.

The reading was tested by a script (work/decode.py) that models the 8x8 board and checks every pair: it must be either a one-step diagonal move or a two-step jump, and for a jump the script names the captured square. All 22 pairs pass. More tellingly, the captures interlock: in game 1, 22-18 is followed by 15x22 (jumping the piece on 18) and 25x18 (jumping the piece on 22); in game 7, 23x16 jumps 19, 12x19 jumps 16, and later 18x9 jumps 14 and 5x14 jumps 9. A chain of mutually consistent captures like this does not arise by chance in arbitrary number pairs; the draughts reading is effectively certain. The openings (11-15/11-16, 22-18, 12-16, the 23x16 12x19 exchange) are ordinary ones.

There is therefore no cipher and no key to recover: the numerals were the normal way of writing draughts moves, not a means of concealment.

## Key

The "key" is the standard English draughts square numbering:

```text
        Black's side
   .  1  .  2  .  3  .  4
   5  .  6  .  7  .  8  .
   .  9  . 10  . 11  . 12
  13  . 14  . 15  . 16  .
   . 17  . 18  . 19  . 20
  21  . 22  . 23  . 24  .
   . 25  . 26  . 27  . 28
  29  . 30  . 31  . 32  .
        White's side
```

Command that reproduces the reading from the transcription and checks the source images (run from the repository root):

```text
python3 -I ciphers/hcp-1466/work/decode.py
```

## Plaintext and translation

Each line on the card is a **move sequence**: a move plus any forced capture or recapture that follows it, so one line can contain moves of both colours. "x" marks a capture; W = White, B = Black (from the direction of the move).

| Game | large ink line (sender) | small ink line |
|---|---|---|
| 1 | 22-18 W, 15x22 B, 25x18 W | 6-10 B |
| 2 | 11-16 B | 24-19 W, 15x24 B, 28x19 W |
| 3 | 29-25 W | 16-20 B |
| 4 | 12-16 B | 21-17 W |
| 5 | 22-17 W | 1-6 B |
| 6 | 6-10 B | 22-17 W |
| 7 | 23x16 W, 12x19 B, 22-18 W | 9-14 B, 18x9 W, 5x14 B |

On this reading Dunne plays White in games 1, 3, 5 and 7 and Black in games 2, 4 and 6 – the usual alternation of colours in simultaneous correspondence play.

**English:** "6 Manchester Road, Warrington. Dear Sir, my replies [moves] are as follows: game 1 … game 7 [as in the table]. Yours fraternally (?), E. P. Dunne." Addressed to Mr D. Bryant, Rathmine, Milton Road, Portsmouth.

**Slovak:** „6 Manchester Road, Warrington. Vážený pane, moje odpovede (ťahy) sú nasledovné: partia 1 … partia 7 [ťahy ako v tabuľke, anglická notácia dámy s poľami 1–32]. Váš (bratsky?) E. P. Dunne." Adresát: pán D. Bryant, Rathmine, Milton Road, Portsmouth.

## What remains uncertain

- **Who wrote the small lines.** They are in a different, smaller hand and lighter bluish ink. Most probably the recipient noted his replies on the card on receipt, or the sender kept a record; this cannot be proved from the scan. Their digits are clear; in game 2 the "5" of 15-24 is blotted, but 15 is the only square from which a capture over 19 lands on 24.
- **Prior positions.** The earlier moves of the seven games are not on the card, so only local legality (geometry and consistency of captures within each line) is verified, not legality on the full board.
- **Closing word.** "Yours F. Fully" – probably "Fraternally" (common among draughts players) or "Faithfully".
- **Names.** The signature reads E. P. Dunne (portal: "E. P. Dunns"); the card reads "Mr D. Bryant" (portal: "W. D. Bryant"). Neither person was identified in external records.
- The game-3 header "3" is crossed by a stray stroke; the order 1–7 makes "3" certain.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-ran the command, typed its own transcription from its own 3–4x crops, and checked it with its own board model (step or jump, side from direction, alternation of sides, every capture jumping the square the opponent had just occupied). Result: 22 moves, 0 problems, identical to the solver's reading. It also confirmed the heading, signature, address and the 1912 date from the stamp and postmarks. Verdict **ACCEPT**, with four minor findings, all accepted:

1. The game-7 small line had been called "pencil-like"; it is the same small bluish ink and hand as the other small lines. Wording corrected.
2. The stamp's issue date was given as 1912; the Downey-head halfpenny was first issued in June 1911. Wording corrected; the date 10 October 1912 is unchanged.
3. The table had labelled the columns "Dunne / small entry", which suggested one player per line; each line is a move sequence with forced replies. Column labels and the script's output labels were changed, and every move is now marked W/B.
4. For the AI Decipherment Register the type is given as draughts notation, not a cipher family.

No move, square or interpretation changed in response to the review.
