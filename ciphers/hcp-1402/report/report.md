# HCP 1402 (pc_hcp_83): a shift-by-one love postcard from Wimborne, 28 January 1908

Human solver: Tomáš Pavuk

**Status: deciphered in full (59 of 59 enciphered letters); three short abbreviation groups are kept literal, as on the sister cards; independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1402 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1402), portal name pc_hcp_83, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard HCPortal collection, category Substitution, date 1908-01-28, language Unknown, location Europe, sender Unknown, recipient W. Abboú, with no transcription or solution attached.

The picture side is a printed Raphael Tuck & Sons "Oilette" card, *The Norfolk Broads / On the Waveney*, with no handwriting. The address side, read with the card turned 90° anticlockwise, is addressed in plain writing to **Mr Abbott, Stokelake Farm, Chudleigh, S. Devon** (the portal's "W. Abboú" is a misreading of Abbott). The halfpenny Edward VII stamp is cancelled **WIMBORNE / 10 PM / JA 28 / 08**. The message begins with the plain heading **"G. H. Tuesday."**; 28 January 1908 was a Tuesday, so heading, postmark and portal date agree.

The card belongs to a long run of cards to the same recipient on the portal (records 1386–1398 and 1401–1407, 1907–1908), written by a girl to her sweetheart in the same hand, the same cipher and the same formulae ("My own … boy", "… from your own … girl"). Several are already deciphered in this repository (for example HCP 1397). The key was therefore known from the family; it was tested here on every letter. The circular alphabet disc visible across the scans is an overlay on the images, not part of the card.

![Address side turned upright: plain address and postmark at the top, heading and seven cipher lines below (work/reading.png)](../work/reading.png)

![Picture side: The Norfolk Broads, On the Waveney (source/picture.jpg)](../source/picture.jpg)

## Method

The transcription is **manual**, from the rotated scan and from 3–5× enlarged crops of every line (work/v2/crops/); the portal supplied no transcription and no OCR was used. An earlier session (OpenAI GPT) read 57 letters and identified the shift; a second session (Claude Opus 5.5) re-read every line from the pixels, added the second `Nz` at the start of line 5, and read the three abbreviation groups as `N. L.`, `N. & L.` and `N. L.`.

Subtracting one from every enciphered letter gives ordinary English with no exceptions: Mfuufs → LETTER, npsojoh → MORNING, uibolt → THANKS, gspn → FROM, Hjsm → GIRL. Long words make a chance fit impossible; nothing is left over and no word is supplied.

In review a separate agent typed its own transcription from its own rotated crops and decoded it with its own script; it obtained the same seven lines and the same 59 letters.

## Key

A Caesar shift of +1 for encryption (−1 for decryption): each plaintext letter is written as the letter after it.

| Plaintext | A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Written | B | C | D | E | F | G | H | I | J | K | L | M | N |

| Plaintext | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Written | O | P | Q | R | S | T | U | V | W | X | Y | Z | A |

The heading "G. H. Tuesday." is ordinary writing and is not shifted. The abbreviation groups are left as written.

## Plaintext

Ciphertext as written (after the plain heading "G. H. Tuesday."), and its decryption line for line:

| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo. N. L. Cpz. | MY. OWN. [N. L.] BOY. |
| Mfuufs uijt. | LETTER THIS. |
| npsojoh xbt. | MORNING WAS. |
| GJOF. Nboz uibolt | FINE. MANY THANKS |
| Nz. N. & L. gspn. | MY. [N. & L.] FROM. |
| zpvs Pxo N. L. | YOUR OWN [N. L.] |
| Hjsm. | GIRL. |

59 enciphered letters, all decoded; 6 abbreviation letters kept literal. FINE is written in capitals (GJOF) for emphasis.

Normalized English (punctuation editorial): **My own N. L. boy, [your] letter this morning was FINE. Many thanks. My N. & L. from your own N. L. girl.** The literal "letter this morning was fine" means that the writer had received the recipient's letter that morning and liked it.

Slovak translation: **Môj vlastný N. L. chlapec, [tvoj] list dnes ráno bol VÝBORNÝ. Veľká vďaka. Moje N. & L. od tvojho vlastného N. L. dievčaťa.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1402/work/v2/decode.py
```

The script checks the SHA-256 hashes of the source files, decodes the manual transcription in work/v2/transcription.json with the shift above, checks the round trip, and prints the seven lines (with the shifted values of the abbreviation letters shown alongside for information) and the line `59 enciphered letters decoded + 6 abbreviation letters kept literal; hashes OK.` It does not read the image; the transcription is manual and was confirmed independently in review.

## Uncertainties

- **The abbreviations N. L. and N. & L.** are not expanded. Their meaning is not established (as on the sister cards hcp-1386, 1401, 1403, 1404); they may be plain initials or private terms of endearment.
- **The closing N. L.** is read by analogy with the salutation: its second sign is a short slanted stroke with only a faint foot, less clearly an L than in the salutation; N. 1 or N. l is not excluded. It does not affect the enciphered text.
- **The final t of uibolt (THANKS)** stands at the card edge and looks more like a short loop (e-like) than a crossed t; this one letter rests on context.
- Dots and capitals are manual readings and do not affect the decipherment.
- The sender is known only by the initials G. H. in the plain heading (C. H. is less likely); her identity is not established.
- No search for a prior publication was made beyond the portal status (Not solved), the absence of an attached solution, and the AI Decipherment Register (no record, checked 2026-10-29).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, rotated the scan itself, cut 3–5× crops of every line, transcribed the card sign by sign and decoded it with its own script; it obtained the same seven lines and the same 59 letters. It confirmed the postmark and the weekday, the recipient and the family key, and found no restoration or forced word. Its four findings were minor and are reflected here:

- **Closing N. L.** is now described as read by analogy with the salutation, with N. 1/l not excluded.
- **Final t of uibolt** is now stated as resting on context.
- **Unreadable early notes:** the first working-log entry (written without spaces) is kept as history but not used in this report.
- **Gloss** "(your) letter this morning was fine" is added beside the literal wording.

No decoded letter changed as a result of the review.

Credits: initial portal capture, rotation, a 57-letter partial transcription and identification of the shift by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26; completion of the transcription from the pixels, reading of the abbreviation groups, decipherment, response to review and this report by Claude Opus 5.5, 2026-10-29/30.

## Sources

- HC Portal record 1402, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1402 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4266/conversions/pc_hcp_83_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4267/conversions/pc_hcp_83_adr-large.jpg (source/address.jpg).
- Related cards to the same recipient: HC Portal records 1386–1398 and 1401–1407; deciphered sister card in this repository: ciphers/hcp-1397.
