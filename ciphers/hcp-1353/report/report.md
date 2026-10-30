# HCP 1353 (pc_hcp_34): "Just a little surprise from Loo", a Caesar-shift note of 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (26 of 26 enciphered letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1353 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1353), portal name pc_hcp_34, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-02-07, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue spelling of Abbott), with no transcription or solution attached. None was found or used.

The picture side is a printed view, "The Minster & Grammar School, Wimborne", with no handwriting. The address side carries a halfpenny Edward VII stamp and a postmark reading WIMBOR[NE], 10 PM, FE 7, 07; the end of the town name is off the visible arc, but the printed view and the related cards make it safe. The address reads Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon.

The message is on the left half of the address side, written along the card, so the scan must be turned 90° counter-clockwise. It is headed by a plain date, "Feb. 7th 1907" (a Thursday), separated from the message by a ruled pen line. A pencilled "(1)" at the top left is probably a later owner's number and is not interpreted.

The card belongs to a large group of Caesar-shift cards in this repository addressed to W. Abbott. The signature on this card also stands on hcp-1398. The writer signs here as "Loo"; that this is a pet form of a name such as Louie or Louisa is conjecture.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side (source/address-large.jpg)](../source/address-large.jpg)

![The message, turned upright (work/reading.png)](../work/reading.png)

## Method

The transcription is manual. The solver turned the un-converted original scan upright and read each sign from enlargements (work/crops/). No OCR was used. A first pass took the second group for a digit 6, the long word for a plural, and the signature for "Mfp"; all three were corrected by rereading the pixels against the rest of the card and related cards, never by changing the key.

The cipher was recognised as the one on the related Abbott cards, so the key was tested rather than recovered afresh. All 26 letters then decoded under the one shift, with no exceptions. The script work/solve.py checks the SHA-256 of the source files, decodes work/transcription.json, verifies the inverse round trip and prints the plaintext.

To reproduce, from the repository root:

```sh
python3 -I ciphers/hcp-1353/work/solve.py
```

## Key

A monoalphabetic Caesar shift: each plaintext letter is written as the next letter of the alphabet. To decrypt, subtract one (A becomes Z).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

Ciphertext and literal decoding, line by line. The dots are the writer's word dots and carry no meaning.

```text
kvtu. b. mjuumf         JUST. A. LITTLE
tvsqsjtf. gspn. Mpp     SURPRISE. FROM. LOO
```

**English (original language):** "Just a little surprise from Loo." (dated Feb. 7th 1907)

**Slovak:** „Len malé prekvapenie od Loo.“ (7. februára 1907)

## Uncertainties

1. **The `b` looks like a digit 6.** It could be taken for a 6, or for a shifted 5. It is read as cipher `b` = A because the `b` of the plain "Feb." on this same card has the same shape, the same phrase `b. mjuumf` stands on hcp-1375, and SURPRISE is singular.
2. **`tvsqsjtf` is the hardest group.** It lies over the printed grey watermark. The `t` near its end descends further than this writer's usual `t`; this is the one unusual shape, and the only parallel, on hcp-1350, is not closed and leans on this card. SURPRISE therefore rests on the other seven signs and on sense as much as on that sign. No letter follows the final `f`, so the word is singular.
3. **The signature `Mpp`.** The second `p` is very faint, probably because the pen ran dry. The capital is compressed, but at 10× it shows a looped first stroke and three feet, matching the signature on hcp-1398. Capital `N` would give MOO, a conceivable pet name, but the stroke count and the sister signature exclude it.
4. **The last sign of `kvtu`.** Its raised finial could suggest a `w`, but `kvtw` decodes to nothing, and `kvtu` is the same word as on hcp-1383.
5. **What is not stated.** Who Loo was and what the surprise was are not on the card. The card itself may be the surprise; that is an inference only.

## Review

An independent Claude Opus 5.5 reviewer tried to refute the reading and could not. It re-ran the command, recomputed all source hashes, decoded the text with its own script sharing no code with the solver's (26 of 26 letters, the same text), and checked every sign on its own crops of the original scan at 3× to 10×. It also confirmed that the card holds no further ciphertext. Its verdict was **ACCEPT**, with four minor findings:

1. A faint word dot after `tvsqsjtf` was missing from the transcription. It was added.
2. "Accepted Abbott cards" was overstated. The argument now names only closed cards: hcp-1375, 1383 and 1398.
3. The capital of `Mpp` was undersold and the alternative misdescribed. The stroke count is now stated, and `Npp` = MOO is named and excluded.
4. Better evidence for `b` was available. The `b` of "Feb." on this card is now the lead evidence.

No letter of the ciphertext or plaintext changed. The reviewer could not verify the portal page itself (it relied on the captured metadata), the descending `t`, or the identity of Loo. Afterwards the solver also narrowed the postmark wording to the letters actually visible.

## Credits

All work on this card is by Claude Opus 5.5, 2026-10-30: capture of scans and metadata by the orchestrator, transcription and decipherment by the solver, review by a separate agent. The key and the sister readings come from cards read earlier in this repository.
