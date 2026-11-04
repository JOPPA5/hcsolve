# HCP 1192 / cpc_1906-11-06_USA_Cobleskill. NY_USA__ — solution (round 1)

**Status: complete reading, awaiting independent review.** Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. There is no earlier work on this number. The portal shows status *Not solved* and attaches no transcription or solution (source/metadata.md). A short web search on 2026-11-03 found no published solution of this card (SOURCES.md). The transcription is my own; the portal has none.

## The card

Picture postcard "After the Chase" (Copyright 1906, American-Journal-Examiner), "Compliments of the New York Sunday American and Journal" (Hearst). Address side, in clear: "Master Warren Becker, City." (surname cursive, partly under the portal watermark; "Becker" is my reading and does not affect the decipherment). Postmark COBLESKILL N.Y. NOV 6 5 PM 1906. No stamp is affixed on the scan; the printed stamp box is empty, so there is nothing hidden under a stamp to inspect. The whole message is enciphered and runs in the white margin around the picture on the picture side; there is no other writing on either side apart from the address.

## Cipher type and key

Simple monoalphabetic substitution (register type **MASC**) with 18 invented signs, one sign per letter, no homophones, no nulls. Punctuation (? . , ') and the date digits are written in clear.

The text is written all round the picture with the **tops of the signs toward the picture**: the top strip is upside-down relative to the card, the right-hand and left-hand margins are sideways, and only the bottom strip is upright. Read in that orientation, every line runs normally left to right, and the message spirals counter-clockwise round the picture: right margin (three lines, card bottom to top, innermost line first), top strip (card right to left), left strip (card top to bottom), bottom strip (left to right), then the outermost right-hand line (date and signature). The orientation is confirmed independently by the literal characters: the question marks look like "¿" and the date digits like "9 … 9" only when the card is held the other way.

Signs are described as they look in the writer's orientation (tops toward the picture):

| Letter | Sign | Token |
|---|---|---|
| a | single stroke, near vertical | BAR1V |
| b | single horizontal dash | DASH |
| d | single stroke at about 45° (/) | BAR1D |
| e | two strokes, near vertical (‖) | BAR2V |
| g | two strokes leaning the other way (\\\\) | BAR2B |
| h | two strokes at about 45° (//) | BAR2D |
| i | plus sign + | PLUS |
| l | asterisk | STAR |
| m | T-shape | TEE |
| n | I with serifs (I-beam) | IBEAM |
| o | circle with a horizontal bar through it and beyond | OBAR |
| r | two parallel strokes closed by end bars (Gemini-like), end bars running / | LADDR |
| s | the same sign mirrored, end bars running \\ | LADDS |
| t | circle with a single stem | LOLLI |
| u | circle with an upright cross through it and beyond | OCROSS |
| v | circle with a diagonal cross through it and beyond | OX |
| w | circle with 6–8 spokes (wheel) | WHEEL |
| y | hooked stroke | HOOK |

Letters c, f, j, k, p, q, x, z do not occur. The key was not taken from any sister card; no card in this repo uses this alphabet.

How the key was found: the sign classes were transcribed first and fed to a word-pattern annealer (work/solve.py, word list work/common_words.txt). With the line order reversed it produced "hello", "warren" (the addressee) and "how" in the innermost right-hand line. That fixed h, e, l, o, w, a, r, n; "are you? going to vote today?" and "give my love to mamma" then fixed the rest, and only then did it become clear that the reversal is simply the 180° orientation of the writing. "Going to vote today?" fits the date: 6 November 1906 was Election Day in New York (Hughes against Hearst for governor), and the card is a Hearst newspaper give-away.

## Plaintext (English, as written, in reading order)

```
hello warren, how
are you? going to
vote today?
how is anna gertrude?
give my love to mamma.
be a good boy.
nov 6,'06.
sis.
```

Normalised: "Hello Warren, how are you? Going to vote today? How is Anna Gertrude? Give my love to Mamma. Be a good boy. Nov. 6, '06. Sis."

English translation: the text is English (see above).

Slovak: „Ahoj, Warren, ako sa máš? Ideš dnes voliť? Ako sa má Anna Gertrúda? Pozdravuj odo mňa mamičku. Buď dobrý chlapec. 6. nov. 1906. Sestra (Sis)."

## Command

From the repository root:

```
python3 -I ciphers/hcp-1192/work/decode.py
```

It checks the SHA-256 of both source scans and both hi-res originals, decodes the manual transcription work/transcription.txt (writer's orientation and reading order, tokens named by shape) with the key above, prints each line and the joined plaintext, and reports that every key entry is used. It does not do OCR: the image-to-token step is the manual transcription, which the reviewer should check against the scan (crops in work/crops/ help; the right margin is easiest to read in work/crops/rpanel_a.png and rpanel_b.png, rotated so that the writer's orientation is upside down, i.e. read them right to left).

## Uncertainties

1. **Final "a" of "mamma"** (bottom end of the left strip). The stroke is faint and leans more (about 25–30°) than the other a-strokes (about 10–15°), less than the clear d-strokes (about 45°). Read as a by word sense; "mammd" is not a word. The dot next to it is a full stop.
2. **"e" of "give"** (top of the left strip). The double stroke leans about 15–20°, like the e of "love" next to it, and much less than the h-sign (about 40–45°). Read as e; this is a slant judgement supported by word sense.
3. **Date digits.** Digits are plain. In the writer's orientation they read "6, '06."; the middle digit is an open loop partly overlapped by the portal watermark and could also be taken for a damaged 6/9, but "06" agrees with the postmark (NOV 6 1906). The comma and apostrophe are two small ticks.
4. **"Anna Gertrude"** is read letter by letter (one person with two names, or two people with "and" omitted; the card does not say). No restoration.
5. **"Becker"** (address, in clear) is my reading of a cursive surname partly under the watermark; it plays no part in the decipherment.

No sign is restored, no sign is left unread, and every sign on the card is covered by the key or is literal punctuation/digits.

## Why I believe it is correct

- All 86 cipher signs decode with one fixed 18-sign key into grammatical, period-appropriate English; each line breaks naturally at the line ends, and the reading path is one continuous spiral round the picture.
- The key is tested on many repeats: o (OBAR) 14×, e 9×, a 8×; "how" twice; "to" twice; "love" and "give" share v and e; r occurs 5× in "warren"/"gertrude"/"are" and the mirrored sign s 3× in "is"/"sis" with a consistent visible difference.
- The orientation is confirmed by literal characters that are not part of the key: the question marks and the date digits only read correctly in the writer's orientation, and "Nov 6 '06" matches the postmark.
- Content fits the context: a boy ("Master Warren") is teased about voting on Election Day 1906 on a Hearst election-season card, and asked about family members; signed "Sis".

## Credit

Transcription, key reconstruction and decipherment: Claude Opus 5.5 (2026-11-03). No earlier work and no published solution were used.

## Response to review 1

Review 1 (separate Claude Opus 5.5 agent, 2026-11-03) gave the verdict **ACCEPT**. The reviewer read every sign independently from its own rotated crops of the hi-res original, wrote its own key and decoder (review/work/my_decode.py) and got the same 86 signs and the same plaintext. There are four findings, all minor, and each one repeats an uncertainty I had already disclosed. None of them changes the reading.

1. **minor – final "a" of "mamma".** Agreed. The stroke leans more than the other a-strokes but clearly less than a d-stroke, and "mammd" is not a word. The reading stays; uncertainty 1 above already says it rests partly on word sense. No change.
2. **minor – e-strokes in "give"/"love".** Agreed. Both e-signs lean about 15–20°, the h-signs about 45°, and the split is consistent across the card. Uncertainty 2 stays as written. No change.
3. **minor – middle date digit.** Agreed. "0" is the natural reading and matches the postmark year 1906. Uncertainty 3 stays. No change.
4. **minor – surname "Becker".** Agreed. It is a reading of clear cursive and plays no part in the decipherment (uncertainty 5). No change.

**Steganography check (repeated at closing).** On other postcard series the human team found hidden messages under the stamp, so I checked this again. The scan of the address side shows the printed stamp box at the top right, partly cut off by the scan edge, with its printed text ("PLA… / UNITE… / CUBA / AN…") visible. No stamp was ever affixed, so nothing can be hidden under one. The postmark is struck beside the box. The picture and the edges hold no writing other than the cipher border. The reviewer reached the same conclusion on its own. The type therefore remains **MASC**, not MASC + Steganography.

I re-ran `python3 -I ciphers/hcp-1192/work/decode.py` after this review: source hashes OK, "unused key entries: none", and the plaintext is unchanged. No file in work/ needed fixing.
