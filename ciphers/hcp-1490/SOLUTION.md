# HCP 1490 / pc_hcp_171 — Pigpen fragments on a postcard to Annie Kepler, Middletown MD (1911)

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1490 — status **Not solved**,
no transcription or solution attached (source/metadata.md, SOURCES.md). No published
decipherment of this card was found or used. The transcription is my own
(`work/transcription.txt`), made from enlarged crops of `source/address-large.jpg`.

**Credit.** Source capture and a first triage (three cipher fragments, sign shapes
`C{blot} L C C TR` in the greeting, the lower final sign in the body; HONEY noted as
speculative) were done by the OpenAI GPT solver (GPT-6 Astra/GPT-6.1 Sol), 2026-10-26.
The key, the full transcription and the reading below are by Claude Opus 5.5, 2026-10-30.

## Cipher type and key

Monoalphabetic substitution, Pigpen family (MASC). Each letter is one of the nine
cell outlines of a tic-tac-toe grid; the **number of dots (0, 1, 2)** selects the block
A–I, J–R, S–Z (no X-shaped cells occur). Same cell layout as the dot-count cards
HCP 1131/1189/1190/1441, but here the first block has no dot.

| Outline (strokes) | Token | 0 dots | 1 dot | 2 dots |
|---|---|---|---|---|
| bottom + right | BR | **A** | J | **S** |
| bottom + left + right | B | B | **K** | T (std) / **U** on this card |
| bottom + left | BL | C | L | U (std) / **T** on this card |
| top + bottom + right | R | **D** | M | V |
| four sides | C | **E** | **N** | W |
| top + bottom + left | L | F | **O** | X |
| top + right | TR | **G** | P | **Y** |
| top + left + right | T | **H** | Q | Z |
| top + left | TL | **I** | R | — |

Bold = attested on this card. The two-dot B and BL cells occur once each, exactly
where the text needs U and T (SUNDAY, NIGHT); the standard layout has them the other
way round. Either the writer's grid had T and U exchanged, or he slipped twice; with
only one occurrence each this cannot be decided. The decoder prints both.

## Transcription (19 cipher signs)

```
greeting:  C* L1 C1 C0 TR2
body:      BR2 B2 C1 R0 BR0 TR2 | C1 TL2x TR0 T0 BL2
signature: [b] R0 B1
```
(The last body sign BL2 is written below the line, under T0, at the end of the word.)

## Plaintext

Cipher passages in capitals, clear text as written on the card:

> Hello **[?]ONEY** (= HONEY?)
> how is times with you – they are fine with me.
> I want to see you at the Party to-morrow night not **SUNDAY NIGHT**
> be sure and come. I must stop from a friend
> **[b]DK**

English (normalised): "Hello [Honey?], how are things with you? They are fine with me.
I want to see you at the party tomorrow night – not Sunday night. Be sure and come.
I must stop. From a friend, [b]DK."

Slovak: „Ahoj [zlato?], ako sa máš? U mňa je všetko v poriadku. Chcem ťa vidieť zajtra
večer na večierku – nie v nedeľu večer. Určite príď. Musím končiť. Od priateľa, [b]DK.“

## Reproduce

From the repository root:

```sh
python3 -I ciphers/hcp-1490/work/decode.py
```

It checks the SHA-256 of all three files in `source/`, decodes `work/transcription.txt`
with the standard layout (literal) and with the card key, and prints the full message.
It does not OCR the scan; the pixel→token step is manual (crops can be rebuilt from
`source/address-large.jpg`, e.g. body at x 195–540, y 445–525; greeting x 225–360,
y 105–140; signature x 85–215, y 565–610).

## Uncertainties (all disclosed)

1. **Greeting, first sign (C\*)**: a full four-sided square with a 4-/x-shaped ink mark
   inside; the dot count cannot be read. A square is E/N/W in this key, none of which
   makes a word with -ONEY. HONEY (H = top+left+right, no dot, as in NIGHT) is the
   obvious greeting, but MONEY/CONEY are also words, so this is a contextual
   interpretation, **not** a reading; the decoder prints `?`.
2. **T/U exchange** (B2, BL2) — see the key section. Without it the body would read
   STNDAY NIGHU.
3. **I in NIGHT (TL2x)**: the outline is clearly top+left (the I/R cell) but carries two
   dots (which would be the unused 27th cell) and a small x/inverted-V mark below,
   possibly a correction. Read as I by its outline; R (one dot) gives no word.
4. **Signature**: the first sign is a b-/6-shaped stroke in ordinary script (an initial?)
   and is reported literally as [b]; R0 = D and B1 = K are clear (the dot of K: one dot
   visible). The sender is not identified.
5. Dot counts of all other signs were read at 10–16× enlargement and are clear:
   S(BR2) N(C1, ×3) O(L1) E(C0) Y(TR2, ×2) D A G H with no dot, K(B1).
6. Clear-text words ("how is times", "stop from a friend") are transcribed as written.

## Why I believe it is correct

- 14 of 19 signs (14 of 18 if the script [b] is not counted as a cipher sign) decode
  under one fixed standard Pigpen layout with no adjustment; the other five (C\*, B2,
  BL2, TL2x, [b]) are listed above.
- "tomorrow night not SUNDAY NIGHT" fits the surrounding clear sentence exactly,
  including the word gap after SUNDAY, the repeated N (C1) in positions 3 and 7, the
  repeated G-cell (TR) for Y/G with 2/0 dots, and D/A/G/H all dotless.
- -ONEY after "Hello" uses the same N and adds O and E consistently (E dotless, N with
  one dot, as in the body), giving the expected endearment.
- Postmark 1911, Maryland address and picture side (Gapland, Md.) are consistent; the
  picture side has no cipher text.

## Response to review 1

Review 1 (Claude Opus 5.5, verdict **ACCEPT**) confirmed every sign of the transcription
on its own 6-12x crops and its own decoder. All five findings were minor; all accepted.

1. **Count of clean signs (fixed).** The figure was wrong: C\*, B2, BL2, TL2x and [b] are
   five non-standard or unresolved signs, so 14 of 19 (14 of 18 cipher outlines) decode
   with no adjustment. Corrected in "Why I believe it is correct" and in the report.
2. **HONEY in the translations (fixed).** English now reads "Hello [Honey?]", Slovak
   „Ahoj [zlato?]"; the cipher reading stays `?ONEY`.
3. **I of NIGHT (agreed, stated in the report).** TL with two dots is the 27th cell of the
   grid and has no letter in the S–Z block. The I is therefore a contextual restoration
   from the outline (TL = I/R cell) and the word NIGHT, of the same kind as the U/T
   exchange; it is not a direct reading.
4. **Hard-coded "Full message" (fixed).** `work/decode.py` now states in its output that the
   clear text is a manual transcription and only the capital cipher passages come from the
   decoder. Re-ran `python3 -I ciphers/hcp-1490/work/decode.py`: hashes OK, output
   unchanged otherwise (`?ONEY / SUNDAY N(I)GHT / [b]DK`).
5. **Partial character (agreed).** The status is now stated as: cipher passages solved,
   except the first letter of the greeting (unresolved) and the script initial of the
   signature (not a pigpen sign, unidentified). The report and the register entry say so.

No decoded letter changed.
