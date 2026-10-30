# HCP 1457 (pc_hcp_138): postcard to Miss E. E. Edwards, Falmouth, 6 March 1903

**Status: complete decipherment of all cipher text on the card, with small residual points disclosed below. Review 1: ACCEPT (five minor findings, no change to the reading).**

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1457. It was *Not solved* when captured on 2026-10-26, and no transcription or solution was attached. No published solution of this card was found. The orchestrator's AI-register check on 2026-10-29 found no record.

## Credit

- Source capture (both scans, metadata, SOURCES.md) and a first triage on 2026-10-26: OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol). The triage noted the tall/short/check-mark strokes and raised Morse only as an untested analogy. It established no reading.
- Identification of the system (Morse written as strokes, plus a pig-Latin margin), transcription of both sides, decoding, decoder script: Claude Opus 5.5, 2026-10-30.
- The transcriptions were made by me (Claude) from enlarged crops of the scans. The portal supplied none.

## The card

The address side is a British halfpenny postcard. It is postmarked FALMOUTH, F, MR 6 03 (6 March 1903, the same as the portal date). It is addressed in clear to *Miss E. E. Edwards, 4 Hatham(?) Road, Holloway, London N.*, and there is a 9-line stroke cipher in the left half. The picture side is "Carrying the Caul," Cornwall (Argall's Series). Two lines of cursive run along its left margin and are written in a pig-Latin variant.

## 1. Address side: Morse code written as strokes

**Type:** Morse code (International/Continental letter codes). Each dash is written as a **tall stroke** and each dot as a **short stroke**. Strokes of one letter stand close together and are often joined in one pen movement:

| Written shape | Strokes | Value |
|---|---|---|
| short stroke | . | E (alone) |
| tall stroke | - | T (alone) |
| check mark (short down-stroke + tall up-stroke) | .- | A (alone) |
| λ-like sign (tall + short at the right foot) | -. | N (alone) |
| short, tall, short joined (ʎ) | .-. | R |
| 2 / 3 / 4 short strokes | .. / ... / .... | I / S / H |
| 2 / 3 tall strokes | -- / --- | M / O |

Letters are separated by small gaps and words by larger ones. A slanted dash followed by a dot (twice, at the ends of lines 4 and 7) and a plain dot (end of line 9) are full stops. They are not Morse letters.

The stroke transcription (one Morse group per letter) is in `work/transcription-morse.txt`:

```
L1: .- -- / ... --- .-. .-. -.-- / -.-- --- ..-                  AM SORRY YOU
L2: .... .- -.. / ... ..- -.-. .... / .- / ..-. .. -            HAD SUCH A FIT
L3: --- ..-. / - .... . / --. .-. ..- -- -... .-.. . ...         OF THE GRUMBLES
L4: .... --- .--. . / -... . - - . .-. / -. --- .-- STOP        HOPE BETTER NOW.
L5: -- -.-- / -.-. --- .-.. -.. / .-. .- - .... . .-.            MY COLD RATHER
L6: -... .- -.. / - --- -.. .- -.-- / -. .- ... - -.--          BAD TODAY NASTY
L7: -.-. --- ..- --. .... STOP                                   COUGH.
L8: .... . .- .--. ... / --- ..-. / .-.. --- ...- .              HEAPS OF LOVE
L9: .. .-.. .-.. .. . STOP                                       ILLIE.
```

**Plaintext (English):**
> (I) am sorry you had such a fit of the grumbles. Hope better now. My cold rather bad today. Nasty cough. Heaps of love, Illie.

## 2. Picture side margin: pig Latin

**Type:** a pig-Latin variant ("back slang"). The initial consonant or cluster of each word moves to the end, and **-a** is added (not the usual -ay): *thanks* → *anks-th-a*. *before* is done syllable by syllable: *be* → *eba*, *fore* → *orefa*, written "eba-orefa". "P.C." stays in clear.

Literal reading (`work/transcription-margin.txt`, segmentation shown with +):

```
M1: Anyma ankstha orfa P.C. istha orningma. Aveha
M2: Ou[y]a eensa attha iewva eba-orefa. Ery va ettypra.
```

**Plaintext:**
> Many thanks for P.C. this morning. Have you seen that view before? Very pretty.

(The writer used a full stop after "before". The question mark is editorial.)

## Combined translation

**English (normalised):** Many thanks for the postcard this morning. Have you seen that view before? Very pretty. I am sorry you had such a fit of the grumbles; I hope you are better now. My cold is rather bad today – a nasty cough. Heaps of love, Illie.

**Slovak:** Veľká vďaka za pohľadnicu dnes ráno. Videla si už tento výhľad? Veľmi pekný. Je mi ľúto, že si mala taký záchvat mrzutosti; dúfam, že ti je už lepšie. Moja nádcha je dnes dosť zlá – škaredý kašeľ. Kopu lásky, Illie.

## One command (from the repo root)

```
python3 -I ciphers/hcp-1457/work/decode.py
```

It checks the SHA-256 of both scans in `source/`. It then decodes `work/transcription-morse.txt` with the standard Morse table and `work/transcription-margin.txt` with the pig-Latin rule, and prints both plaintexts. Output, last three lines:

```
== Full plaintext ==
AM SORRY YOU HAD SUCH A FIT OF THE GRUMBLES HOPE BETTER NOW. MY COLD RATHER BAD TODAY NASTY COUGH. HEAPS OF LOVE ILLIE.
Many thanks for P.C. this morning. Have you seen that view before. Very pretty.
```

## Uncertainties (all disclosed)

1. **L1 first group "√ ||" = `.- --` = AM.** The same strokes could be grouped as one letter, `.---` = J. The gap between the check mark and the two tall strokes is small. "AM SORRY" (with the subject *I* omitted, as is common on postcards) is the only sensible reading.
2. **L5 "MY": the Y is an N-shaped group in lighter ink.** I read the N shape as tall – short diagonal – tall, followed by a separate tall stroke: `-.--`. The diagonal is nearly full height, so the dot/dash value of that stroke is not clean on the pixels. The reading rests on M + Y = "MY" in context.
3. **L5 "COLD": the C is a corrected or overwritten sign.** A light-ink inverted V (two tall strokes) is overwritten by a dark short V. I read it as `-.-.` = C, but the exact order of the strokes cannot be proved from the pixels. "MY ?OLD RATHER BAD TODAY. NASTY COUGH" makes C (COLD) certain in context. This is the weakest letter on the card.
4. **Signature "ILLIE".** It is read exactly as written: `.. .-.. .-.. .. .`, with two clear short strokes at the start of line 9. It may be a pet name, or a slip for *Lillie/Ellie*. Nothing is restored, and the sender is not identified.
5. **Full-stop signs.** The "/." marks (ends of L4 and L7) and the final dot (L9) are treated as punctuation, not as Morse groups. Elsewhere there is no punctuation, and sentence breaks in the translation are editorial.
6. **Margin, "Ou[y]a" (you).** The letter between "Ou" and "a" is crossed by the long descender of the "y" of "Anyma" in the line above and cannot be read on its own. *y* is a restoration, the only letter that gives *you*: "Have [you] seen that view before?"
7. **Margin, smaller points:** In *aveha* the second letter looks like r/v. In *eensa* the e/n minims are crowded. *Ery va* is written with a gap. The final letter of *ettypra* could be a or e. The pig-Latin rule predicts a, and the meaning (*very pretty*) does not depend on it.
8. The house number and street of the clear address ("4 Hatham(?) Road") are not part of the cipher and are only roughly read.

## Why I believe it is correct

- Standard Morse, with one fixed visual rule (tall = dash, short = dot), turns all 9 lines into grammatical, idiomatic English with no leftover groups. All 93 letter groups are valid Morse codes, and no key was fitted to the text.
- Long, distinctive words come out letter-perfect: SORRY, GRUMBLES, BETTER, RATHER, TODAY, NASTY, COUGH, HEAPS OF LOVE. Chance agreement over that much text is not plausible.
- The content fits the context. It answers a card received "this morning" from a friend who had "a fit of the grumbles". The writer has a cold in Cornwall in early March. The margin comments on the Cornish view on the front of the card.
- The margin rule (move the consonant onset to the end + *a*) is applied consistently across 13 words, including the syllable-wise *eba-orefa*.

## Response to review 1

Review 1 (review/REVIEW1.md) gave the verdict **ACCEPT** with five minor findings and no blocker or major. I re-ran `python3 -I ciphers/hcp-1457/work/decode.py` on 2026-10-30: both hash checks print `OK`, and the output is unchanged (93 Morse letters, the same two plaintexts). No letter of the reading changed.

1. **L5 C of COLD is restored from context (agree).** I looked again at the reviewer's 8× crop (review/work/l5c.png). It shows a light inverted V (two tall legs) with a dark short V written over its middle. The order of strokes cannot be recovered, so `-..-` (X) fits the pixels as well as `-.-.` (C). This was already uncertainty 3. The report now says plainly that this sign is a correction, that its stroke order cannot be read, and that C is restored only from context ("MY ?OLD RATHER BAD TODAY. NASTY COUGH").
2. **L5 Y of MY treats a full-height diagonal as a dot (agree).** On l5c.png the N-shape's diagonal is nearly as long as the tall strokes, so reading it as a dot breaks the tall/short rule used everywhere else on the card. A literal reading gives no sensible letter (`----` or OT). The disclosure (uncertainty 2) is kept and repeated in the report. The reading MY stays because it is a context reading.
3. **Margin "Ou[y]a" (agree, nothing to change).** The reviewer confirms that the [y] is marked as a restoration in the transcription and in uncertainty 6. The report keeps the bracket.
4. **Literal versus normalised text (agree).** The report gives the literal decoder output, with only the card's own stops, in a separate block from the normalised English translation. It also notes that the question mark after "before" and the sentence breaks after GRUMBLES and TODAY are editorial.
5. **Cipher type (agree).** The portal category "Substitution; Monoalphabetic" and the language "Unknown" are not what the card uses. The report and the register entry give the type as **Morse code written as tall/short strokes (address side) plus a pig-Latin variant (picture-side margin)**, and the language as English.
