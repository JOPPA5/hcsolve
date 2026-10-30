# HCP 1495 (pc_hcp_176): a Caesar-shifted postcard to Miss L. Cory, 1906

Human solver: Tomáš Pavuk

**Status: deciphered in full (60 of 60 enciphered letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1495 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1495), portal name pc_hcp_176, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution, date 1906-03-21, language Unknown, location Europe, sender Unknown, recipient "L.Gory", with no transcription or solution attached.

The picture side is a Rotophot photographic card of the actors **Miss Lily Brayton & Mr Oscar Asche**, a popular Edwardian stage couple; it carries no cipher. The address side is addressed in plain writing to **Miss L. Cory, Bankside Villa, Gravesend, Kent** (the portal's "Gory" is a misreading of the C), with a postmark dated 21 March 1906 whose place name is partly obliterated ("…IDGE"). The cipher message stands in the message area of the address side, in dark ink, in four lines; below it are a pale word and a large monogram flourish. A later pencil note at the bottom, "CODED MESSAGE" with a price/reference, is a dealer's or collector's mark, not part of the correspondence.

![Address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Lily Brayton and Oscar Asche (source/picture-large.jpg)](../source/picture-large.jpg)

![Message area enlarged: four ink lines, the pale closing word and the monogram (work/message.jpg)](../work/message.jpg)

## Method

The transcription is **manual**, made from enlarged crops of the address-side scan (the portal attaches no transcription). The writer keeps word division and punctuation, and the letter shapes are ordinary cursive with a few individual forms: U written as two l-like strokes, z as a ȝ-shaped sign with a descender, x as a "+"-like cross, j with a long descender loop, f with an upper and a lower loop.

With word division visible, the cipher is recognisable at once: short words such as "zpv", "pof" and "uijt" become "you", "one" and "this" when every letter is moved one place back in the alphabet. All 26 Caesar shifts were printed by script (work/all-shifts.txt); only the shift −1 gives English, and it gives English throughout.

Earlier work and credit: the card capture, the identification of the −1 shift and the first reading of the four message lines were done by an OpenAI GPT solver (GPT-6 Astra) on 2026-10-26. On 2026-10-29 Claude Opus 5.5 re-checked every sign on enlarged crops, corrected the greeting name (first read "Mfmz" → "Lely", on the pixels "Mflz" → "Leky"), added the comma and the pale closing word, and completed the solution. A separate Claude Opus 5.5 agent reviewed it independently.

## Key

Caesar shift (a monoalphabetic substitution): to encrypt, each letter is replaced by the next letter of the alphabet; to decrypt, by the previous one. Case, word division and punctuation are kept.

| Plain | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cipher | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A |

## Plaintext

Ciphertext as transcribed (line by line, punctuation as on the card; the fifth line is the pale word below the message):

```text
Ebsmjoh. Mflz
Uipvhiu zpv xpvme
mjlf uijt pof zpvs
dpmmfdujpo, efbs
Xpvst
```

Literal output of the −1 shift:

```text
Darling. Leky
Thought you would
like this one your
collection, dear
Wours
```

Normalised English (punctuation editorial; "for" is missing on the card):

**Darling Leky, thought you would like this one [for] your collection, dear. [Yours?], [monogram]**

Slovak translation:

**Drahá Leky, myslel(a) som, že by sa ti táto (pohľadnica) páčila do tvojej zbierky, drahá. [Tvoj(a)?], [monogram]**

Notes on the reading:

- **"this one … your collection"**: the card itself, a photograph of a well-known stage couple, is sent for the recipient's postcard collection, a common pastime of the period.
- **"Leky"** is read literally from the pixels; its initial L agrees with "Miss L. Cory", so it is probably a pet name, but the name itself is not established.
- **"Wours"** is the literal decryption of the pale word; "Yours" is the probable intent, the writer apparently shifting Y the wrong way (to X instead of Z). This is an interpretation and is marked as such.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1495/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in source/, applies the −1 shift to the manual transcription in work/transcription.txt, checks that re-encrypting the output gives the transcription back exactly, and prints the five plaintext lines followed by `Encrypted letters: 60`. With `--all-shifts` it also prints all 26 shifts. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **Greeting name.** The second sign of the name rises above and descends below the line like this writer's f (as in "mjlf", "pof"), and the third is one tall loop like the l of "mjlf", not the two humps of an m; hence "Mflz" → "Leky", not "Lely". A slip for another name cannot be excluded.
- **Pale closing word.** It is in pale ink or pencil, overlapped by the portal's watermark. The signs are read X, p, v, s and a last sign that may be t or k; the literal output is "Wours" (or "Wourj" with k). That it was written by the same hand at the same time is likely (same cursive forms, same cipher) but not proven: the wrong-way shift of Y could also point to a later hand's attempt.
- **Monogram.** The flourish below the message (a J/F/P/H-like ligature) is not read; the sender is unidentified.
- **Postmark place.** Only "…IDGE" is legible; it is not needed for the decipherment.
- Only the portal's watermarked 1024-pixel images were available, not the original card.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decrypted the transcription with its own independent script (identical result), recounted the 60 letters, and checked every line on its own 4–10× crops of the scan. It confirmed the corrected greeting name "Mflz" → "Leky" as supported by the pixels rather than forced by context, and judged the pale closing word plausible with its k/t uncertainty disclosed. Its four findings were minor and are reflected here:

- **Normalised "Yours".** It is now written "[Yours?]" (and the Slovak "[Tvoj(a)?]"), with the literal "Wours" and the alternative "Wourj" stated.
- **Dot after the first word.** A clear dot after "Ebsmjoh" was added to the transcription; the plaintext now reads "Darling. Leky". The reproduction command was re-run and still passes on 60 letters.
- **Attribution of the pale word.** The caveat that it may not be by the original writer is kept above.
- **Stale letter count in the notes.** The working log's earlier "55 letters" is superseded; this report quotes only the current count, 60.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1495, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1495 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4546/conversions/pc_hcp_176_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4545/conversions/pc_hcp_176_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), no entry for this card (checked 2026-10-26 and 2026-10-29).
- No published solution of this card was found or used.
