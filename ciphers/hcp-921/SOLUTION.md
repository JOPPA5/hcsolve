# HCP 921 — Pigpen postcard to Miss Larkin, Horsmonden (1912)

Status: complete reading of a very short message; review 1 verdict ACCEPT (FINAL).
One sign value (the dotted right-pointing wedge = S) is contextual, see below.

## Origin

HC Portal cryptogram 921, `cpc_1912-12-06_UK_Horsmonden_UK_Horsmonden_`,
T. Schrödel postcard collection, tags Postcard / Pigpen, status *Not solved*,
no transcription or solution attached (capture of 2026-10-25, `source/metadata.md`).
Bamforth picture postcard "Two's company, three's none." addressed to
Miss Larkin, Hoath Hatch, Horsmonden; Horsmonden postmark; handwritten date
4-12-12 beside the cipher (catalogue date 1912-12-06). The cipher is two short
lines written sideways on the message half of the address side; the picture
side carries no cipher.

## Cipher type and key

Interleaved Pigpen (undotted/dotted pairs per cell), the same alphabet as the
finished sister cards HCP 1188, 1187, 1497, 1498:

| Outline / wedge | Undotted | Dotted |
|---|---|---|
| bottom/right BR | A | B |
| bottom/left/right B | C | D |
| bottom/left BL | E | F |
| top/bottom/right R | G | H |
| closed square C | I | J |
| top/bottom/left L | K | L |
| top/right TR | M | N |
| top/left/right T | O | P |
| top/left TL | Q | R |
| down wedge V | S | T |
| right-pointing wedge > | U | V |
| left-pointing wedge < | W | X |
| up-pointing wedge ^ | Y | Z |

Card-specific exception: **dotted right-pointing wedge (>1) = S** on this card.

Signs observed (upright orientation): TR0 C0 [blot] >1 >1 . | TR0 BR0 ^0 . / B1 C0 BL0 B1 .

## Plaintext

```text
MI[blotted sign]SS. MAY.
DIED.
```

English (original language): **Miss May died.**
Slovak: **Slečna May zomrela.**

## Reproduce (from repo root)

```sh
python3 -I ciphers/hcp-921/work/decode.py
```

Verifies SHA-256 of the three files in `source/`, decodes the manual
transcription `work/transcription.txt` and prints `MISS. MAY. / DIED.`
plus what the unchanged sister key gives. It does not OCR the scan;
the transcription was read by hand from enlarged crops (`work/message-large.jpg`
is an upright crop of `source/address-large.jpg`).

## Uncertainties

1. **S value is contextual (main residual point).** Both signs of the doubled
   letter are clearly right-pointing wedges with a clear dot inside (checked at
   4x). Under the sister key that sign is V ("MIVV", not a word); in no common
   interleaved layout is S dotted. The value S comes from the word MISS: a
   4-letter MI+doubled letter word before a name, with M, I, A, Y, D, E fixed by
   the key. The writer evidently placed S/T differently or dotted it in error;
   with only one wedge type besides Y on the card, the writer's own X layout
   cannot be established.
2. **Blotted sign** after MI: a heavily inked-over sign, original outline not
   recoverable. Read as the writer's own cancellation (probably a first,
   wrong attempt at S) and omitted; not restored.
3. "May" may be a forename or a surname; nobody's identity or death is verified.
   The handwritten 4-12-12 and catalogue date 6 Dec 1912 are not reconciled
   (the catalogue may use the postmark).
4. Periods after MISS, MAY and DIED are the writer's dots, kept as punctuation.

## Why it is believed correct

- Nine of the eleven intact signs decode with the unchanged, externally
  established sister-card key into two ordinary English words, MAY and DIED,
  plus MI-; DIED uses D twice consistently (both dotted B outlines).
- The orientation is fixed: rotating 180 degrees gives nonsense (SQE / WW?IE).
- The only free value (one sign type, two occurrences) completes MI__ to the
  single natural word MISS, giving a grammatical sentence fitting a postcard
  between neighbours ("Miss May died."). The blot directly before the doubled
  sign is consistent with the writer struggling with exactly that letter.
- Weakness, disclosed: the message is 11 signs long, so the statistical
  support is small and rests on the sister key plus context.

## Credit

Source capture, transcription and the candidate MISS MAY DIED by the earlier
OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-25. Re-verified on the
pixels, decoder rewritten with the full sister key and this solution written
by Claude Opus 5.5 on 2026-10-30. No published solution of this card was found
or used.

## Response to review 1

Verdict ACCEPT, three minor findings. The reading is unchanged.

1. **Missing punctuation dot after the doubled wedge — fixed.** I re-checked
   `review/work/blot_wedges_x16.png` and `work/message-large.jpg`: a baseline
   dot of the same size and height as those after MAY and DIED follows the
   second `>1`. `work/transcription.txt` line 1 now reads
   `TR0 C0 {cancelled} >1 >1 . | TR0 BR0 ^0 .`. Re-run of
   `python3 -I ciphers/hcp-921/work/decode.py` (hashes pass) prints
   `MISS. MAY.` / `DIED.`, 11 intact signs, 1 blot omitted; sister key
   unchanged gives `MIVV. MAY. / DIED.`. Plaintext and sign list above updated.
   The writer thus put a dot after every word ("Miss. May. Died."); the
   normalized sentence stays "Miss May died."
2. **S value is contextual — agreed, kept as disclosed.** The report and the
   register entry describe >1 = S as a card-specific value inferred from the
   word MISS, not as part of the key derived from the sister cards.
3. **Date bookkeeping — clarified.** DONE1 (`2026-10-29T23:04Z`) is UTC; the
   NOTES heading 2026-10-30 was the local (CET, UTC+1) date of the same
   session, i.e. 00:04 local. Markers are not edited. On the card dates: the
   handwritten 4-12-12 (4 December 1912) and the catalogue date 1912-12-06 are
   left unreconciled; the postmark day is not legible enough in the scan to
   decide, and the report does not choose between them.
