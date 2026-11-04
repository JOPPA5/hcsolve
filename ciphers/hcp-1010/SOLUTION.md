# hcp-1010 — solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-03. No earlier work on this number (directory captured the same day by the orchestrator). No transcription or solution is attached on the portal; status there is "Not solved". No published solution of this card was searched for or used.

## Card
Picture postcard (embossed scene: a young man and a girl at a wooden fence), T. Schrödel collection. Address side, plain German Kurrent, not enciphered: "Fräulein Helene Schlauch, Hier, Rathskeller" (local delivery). The stamp has been removed; the stamp box shows only bare paper and glue residue, no writing. All ciphertext is on the picture side, in three places: two upside-down lines at the bottom edge, the fence boards, and the brim of the young man's hat (the last two hidden in the picture).

## Cipher type and key
Number substitution (MASC), with part of the ciphertext hidden in the picture (steganographic placement on the fence boards and on the young man's hat brim). Suggested register label: `MASC + Steganography`.

Key: the alphabet without J, first half ascending, second half descending:

| A | B | C | D | E | F | G | H | I | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 |

Umlauts are written as the base number with two umlaut strokes above it (1 with strokes = Ä, 18 with a mark = Ü). Q, X, Y, Z (and P, 6=F, 13–15, 22, 23) do not occur; their values follow from the pattern, not from the card.

## Transcription (work/transcription.txt)
Bottom edge of the picture side, written upside down (read with the card turned 180°):

- A: `4 [5] 21 | 2 18 21 20 [3] 8 5 | 9 20 19 | 10 18̈ 8 25 5 21 . | 8 9 5 21 | 16 9 5 | 20 9 5 | 20 5 8 5 25 .`
- B: `16 1 20 | 16 9 21 4 | 16 2[4] 8 11 | 9 12 | 25 1̈ 3 8 20 19 5 25 | 12 24 12 5 25 19 | 8 9 5 21 | 7 5 20 3 8 5 8 5 25 .`

Orientation below is relative to the scan as published (landscape, figures lying on their side).

On the fence boards in the picture (upright when the scan is turned 90° counter-clockwise, i.e. with the picture upright):

- C: `17 5 21 | 2 24 19 | 5 25 | 5 21 | 16 5 7`

On the brim of the young man's hat (upright when the scan is turned 90° clockwise, i.e. upside down relative to the picture):

- H: `7 2[1] 18 20 [20]`

## Plaintext (German)
A: Der Bursche ist kühner. Hier, wie Sie sehen.
B: Was wird wohl im nächsten Moment hier geschehen.
C (fence): Verbotener Weg.
H (hat brim): Gruss (Gruß).

Read as one text: "Der Bursche ist kühner hier, wie Sie sehen. Was wird wohl im nächsten Moment hier geschehen? — [fence:] Verbotener Weg. — [hat brim:] Gruß."

English: "The lad is bolder here, as you see. What will happen here in the next moment? — [on the fence:] Forbidden path. — [on the hat brim:] Greetings." (Translation follows the reading "bolder here, as you see"; the alternative with the full stop after "kühner" is "The lad is bolder. Here, as you see.")

Slovak: "Mládenec je tu odvážnejší, ako vidíte. Čo sa tu asi stane v najbližšej chvíli? — [na plote:] Zakázaná cesta. — [na okraji klobúka:] Pozdrav."

## Command
From the repo root:

```
python3 -I ciphers/hcp-1010/work/decode.py
```

It checks the SHA-256 of the source images, prints the key and decodes work/transcription.txt (restored letters printed lower-case).

## Uncertainties
- Restorations (letters physically hidden, each the only letter that makes the word):
  - A, "Der": the middle sign sits on a damaged/pale spot; only faint traces; E (5) restored.
  - A, "Bursche": the 3 (C) lies under the "H" of the HCPortal collection stamp; only part of a stroke is visible. The 21 (R) before it is inside the stamp's "O" — the 2 is visible, the 1 only partly.
  - B, "wohl": the 4 of 24 (O) is under the stamp's "O"; the 2 is visible.
- Line order: the two upside-down lines are given top-to-bottom as seen with the card turned. Line A is shorter and ends mid-card, so it may have been written after line B; the meaning does not depend on the order. The punctuation in A (point after "kühner") is on the card; whether "hier" belongs to the first or second clause is a matter of reading.
- A long pencil stroke runs through "20 5" in "sehen" and under "8 9" of the second "hier" in B; it reads as an incidental line/underline, not a correction (the digits under it are clear).
- The darker, retraced 9 in "ist" looks like a 7 or 4 at first sight; 9 is confirmed by shape and by IST.
- Fence C, first sign: at a damaged board edge, it could be 17 (V) or 13 (Z); 17 rests on word sense (VERBOTENER).
- Hat brim H: `7 . 18 20` is clear. The second group is a 2 followed by a 4-like stroke (this writer's 4 is open and crossed, cf. 24 in "Moment"); it is read 21 = R on word sense, since 24 = O gives GOUS…, no word. After 20 the brim is in dark shading; a faint trace there may be a second 20, restored as S (GRUSS). Without it the word is still GRUS = Gruß.
- The card has no date or signature.

## Why it is correct
- One simple, systematic key (A–M ascending 1–12, N–Z descending 25–13, J omitted) decodes all four passages (two bottom lines, fence, hat brim) with no leftover sign. Every number found on the card is used; the hat-brim group was missed in round 1 and found by the reviewer, and the reviewer's search of the rest of the picture found no further digits.
- The output is fluent, grammatical German of the period and fits the picture: a young man approaching a girl at a fence, with the caption-like joke "what will happen next?" and "forbidden path" hidden on the fence boards.
- Umlaut marks fall exactly on Ä (nächsten) and Ü (kühner).

## Response to review 1

1. **[major] Hat-brim group — fixed.** I confirmed the group on my own enlargements of work/hires/cpc_--_DE__DE_Hier__pic.jpg (work/crops/hat_cw.png, hat_mid5.png, hat_start5.png, hat_hp_end5.png; red channel, 3–5x, high-pass). With the scan turned 90° clockwise it reads `7 2? 18 20` clearly, then dark brim shading with a faint trace. The second group's last stroke is crossed like this writer's 4; I read it 21 on word sense (GRUS…; 24 gives GOUS…, no word) and say so. The trailing 20 (second S) is a restoration. Added as line H to work/transcription.txt (`7 2[1] 18 20 [20]`), which the unchanged decoder now prints as `H: GrUSs`. Plaintext, English and Slovak translations, the uncertainty list and the "Why it is correct" claim are updated, and the hat brim is named as a second hidden placement. Command re-run: hashes OK, A/B/C unchanged, H = GrUSs.
2. **[minor] Fence orientation — fixed.** Checked on the overview of the scan (work/crops/pic_overview.png) and the reviewer's fence2.png: the fence numerals are upright with the scan turned 90° counter-clockwise (picture upright). SOLUTION.md and the transcription header now say this and state that orientations refer to the scan as published.
3. **[minor] First fence sign — fixed.** Added to Uncertainties: 17 or 13 at the damaged board edge; 17 rests on word sense.
4. **[minor] Clause boundary — fixed.** The English translation now states which reading it follows and gives the alternative; the report will do the same.
5. **[minor] Register type — agreed.** `MASC + Steganography` kept; with the hat brim, the ciphertext is hidden in two places in the picture.

The reading of A, B and C is unchanged; the change is one added greeting word.
