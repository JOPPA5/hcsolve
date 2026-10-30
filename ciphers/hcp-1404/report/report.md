# HCP 1404 (pc_hcp_85): "Your own E. L. girl", a Caesar-shift sweetheart postcard of 1908

Human solver: Tomáš Pavuk

**Status: deciphered in full (11 of 11 enciphered letters); one two-letter abbreviation (E. L.) kept literal and not expanded; independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1404 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1404), portal name pc_hcp_85, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1908-01-30, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached. No published decipherment of this card was found.

It is a Raphael Tuck "Oilette" picture postcard from the series *The Norfolk Broads III*; the picture side shows **Fritton Decoy, Norfolk Broads** and carries only the printed caption. The written message is on the left half of the address side, which is scanned sideways. The address, in plain writing, is to **Mrs W. Abbott, (Stokelake?) Farm, Chudleigh, S. Devon** (the farm name is not certain); the postmark reads **JA 30 08**.

![Picture side: Fritton Decoy, Norfolk Broads (source/picture.jpg)](../source/picture.jpg)

![Address side as scanned; the message is on the left half, turned 90 degrees (source/address.jpg)](../source/address.jpg)

The card belongs to a family of Caesar-shift sweetheart postcards in the same hand, written by one couple in 1907–08 and addressed to the same household in Chudleigh (HC Portal records 1386–1407, several of them deciphered in this repository, e.g. HCP 1386, 1395, 1397, 1401). The key was established on those cards and confirmed here; this is not a new key recovery.

## Method

The message area was turned upright and enlarged (3–9x), and every letter was read by hand from the crops. No OCR was used and the portal supplied no transcription.

![Message area turned upright: heading, two cipher lines and the plain date (work/message.png)](../work/message.png)

The message has four lines. The heading **"G. H. Thursday."** and the date **"January 30th = 08"** are ordinary writing (as on every card of the family). The two middle lines are the ciphertext:

![Line 1: "Zpvs. Pxo." (work/v2/crops/line1-zpvs-pxo.png)](../work/v2/crops/line1-zpvs-pxo.png)

![Line 2: "E-l. Hjsm." (work/v2/crops/line2-EL-hjsm.png)](../work/v2/crops/line2-EL-hjsm.png)

Letter-form notes: the Z of *Zpvs* is 2-shaped with a descender, and its final s is the writer's c-like terminal s; the P of *Pxo* has a long top stroke looping right over the line; the j of *Hjsm* is dotless with a long descender, and the m is a run of minims. In line 2 the first group is written **"E-l."**: a cursive E, a short dash, and a tall stroke with a looped foot. It is transcribed (normalised) as **E. L.**, because the same hand writes the identical closing formula "Pxo. E. L. Hjsm" on sister card HCP 1386, with the same E, the same dash separator and the same looped L in the same slot. A reading of the tall stroke as the numeral 1 was considered and rejected for that reason.

Decoding: shifting every enciphered letter back by one place in the alphabet gives English words (YOUR, OWN, GIRL); a scan of all 26 shifts gives English only for this one. The decoding is reproduced from the repository root by

```sh
python3 -I ciphers/hcp-1404/work/v2/decode.py
```

which checks the SHA-256 hashes of the source images, decodes the transcription in `work/v2/transcription.json`, checks the round trip, and prints the plaintext (saved as `work/v2/plaintext.txt`).

## Key

Caesar shift: each plaintext letter is written as the **next** letter of the alphabet (encipher +1, decipher −1).

```text
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

| Ciphertext (as on the card) | Plaintext |
|---|---|
| G. H. Thursday. *(plain)* | G. H. Thursday. |
| Zpvs. Pxo. | YOUR. OWN. |
| E-l. Hjsm. | [E. L.] GIRL. |
| January 30th = 08 *(plain)* | January 30th 1908 |

11 enciphered letters, all decoded by the one key; the 2 letters of the abbreviation E. L. are kept literal (their shifted value would be D. K.).

**English:** *"G. H. Thursday. Your own E. L. girl. January 30th '08."*

**Slovak:** *„G. H. Štvrtok. Tvoje vlastné E. L. dievča. 30. januára 1908."*

The message is the writer's standard closing formula, which recurs on the sister cards ("from your own girl" on HCP 1397, "your own E. L. girl" on HCP 1386 and HCP 1401). The written date agrees with the postmark JA 30 08 and with the portal date 1908-01-30, and 30 January 1908 was indeed a Thursday.

## Uncertainties

1. **The abbreviation E. L.** Its meaning is not established ("ever loving" is a possible expansion, but nothing on the card proves it), and it is not certain whether it is written in clear or is itself enciphered. Across this family the treatment is not uniform: on HCP 1395 the closing initials "M. & L." were read as ciphertext (giving L. & K., possibly "Love & Kisses"), while on HCP 1386, 1401 and this card "E. L." is kept literal. Here the literal value admits a natural expansion and the shifted value D. K. does not, which mildly favours the literal reading; both values are given.
2. **Normalisation.** On the card the group is written "E-l." with a dash and a lower-case-looking L; it is normalised to "E. L.".
3. **Heading initials** "G. H." could also be "C. H." (as read on HCP 1386); they are plain writing, not ciphertext, and are not expanded.
4. The farm name in the address is not read with certainty; it is not ciphertext.
5. Only a 1024x674 scan is available; at that resolution all 11 cipher letters and the abbreviation are nevertheless legible without ambiguity.

## Review and what changed

Work history: an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) downloaded the sources, identified the shift and produced a partial transcript on 2026-10-26, leaving the field before GIRL unresolved. Claude Opus 5.5, acting as solver, completed it on 2026-10-29 (re-transcription from the pixels, reading of the E. L. field by comparison with HCP 1386, new decoder in `work/v2/`). The earlier GPT files directly in `work/` are superseded and kept only for the record.

An independent reviewer (a separate Claude Opus 5.5 agent) re-read every sign from its own enlargements, decoded its own reading with its own script, scanned all 26 shifts, compared the E. L. field with HCP 1386, and checked the date and address against the postmark and the sister cards. Its reading agrees with the solver's in every position. Verdict: **ACCEPT**, with four minor findings, all about presentation:

1. state the family-level inconsistency in treating closing initials (HCP 1395 vs. 1386/1401/1404) — done, Uncertainty 1;
2. keep the "E-l." to "E. L." normalisation explicit — done, Method and Uncertainty 2;
3. do not assert G over C in the heading — done, Uncertainty 3;
4. cite only the `work/v2/` files — done.

No decoded letter changed as a result of the review.
