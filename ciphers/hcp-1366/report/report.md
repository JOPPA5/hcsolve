# HCP 1366 (pc_hcp_47): a hurried Caesar-cipher love postcard from Harrogate, 19 July 1907

Human solver: Tomáš Pavuk

**Status: whole message read. 51 enciphered letters decoded by one key; 4 letters in two abbreviation groups kept literal. Independent review 2 verdict ACCEPT.** Report dated 2026-10-30.

> **My own loving boy, no time to send letter. Love & Lt.. from your own M. h. girl.**

## Origin and context

The cryptogram is record 1366 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1366), portal name pc_hcp_47, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-07-19, language Unknown, location Europe, sender Unknown, recipient W. Abboú (a catalogue spelling), with no transcription or solution attached.

The picture side is a printed view, "Royal Baths, Harrogate", with no handwriting. The address side belongs to the Boots "Pelham" Series and carries a halfpenny Edward VII stamp and a postmark reading WIM... (only those three letters are firm; WIMBORNE is taken from sister cards), 10 PM, JY 19, 07. It is addressed in clear to Mr. W. Abbott, Stokelake Farm, Chudleigh, Devon. The message fills the left half of this side and is read after turning the scan 90 degrees anticlockwise.

Above the cipher stand the plain words "G. H. Friday." and an underlined "No. 1.". 19 July 1907 was a Friday, agreeing with the postmark. Card hcp-1363 has the same date and postmark time and is headed "No. 2."; nothing more than that pairing is claimed. The hand and the Harrogate card use are the same as on hcp-1371, written three days later. The card belongs to a run of Caesar-enciphered cards to W. Abbott, several of which are solved in this repository.

No published solution of this card was found or used. The only checks were this repository and an AI Decipherment Register check made for this run; no wider web search was made.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side turned to reading position (work/crops/adr_ccw.jpg)](../work/crops/adr_ccw.jpg)

## Method

The transcription is manual, read from enlargements (3 to 8 times) of the un-converted original scan. No OCR was used and the portal supplied no transcription. The key was tried as a hypothesis from the sister cards and then confirmed on this card: it gives English for every word with no adjustment for any word.

Sign shapes on doubtful words were compared with other signs on this card and with sister cards. The first draft had errors that the review rounds removed:

- A field at the upper right, first read `Op 2.` (NO 2), is `Cpz` (BOY), the end of line 1 set higher because the line had reached the card edge. The reviewer found this.
- The last word of line 1 was first read `Mpwf` (LOVE). The reviewer showed that ink had been left out and proposed `Mpwfs` (LOVER). The solver rejected that and read `Mpwjoh` (LOVING); the next section gives the evidence. Review 2 tried to break this and could not.

Decoding is scripted. `python3 -I ciphers/hcp-1366/work/decode.py`, run from the repository root, checks the file hashes, decodes every token of `work/transcription.json`, checks the inverse round trip and prints the plaintext. It decodes the manual transcription, not the image.

## The key word: Mpwjoh

![Line 1 end on this card (top), the same word on hcp-1367 and hcp-1361, then this card's Mpwf, Hjsm and initials for comparison (work/crops/cmp_mpwjoh.png)](../work/crops/cmp_mpwjoh.png)

After `Mpw` the next sign starts at a foot below the line, runs through an open hook and rises to the right. That is j, as in `ujnf` and `Hjsm` on this card. It is not f, whose foot here is a closed loop (`Mpwf`, `ujnf`), and that excludes LOVER and LOVED. A closed lens follows (o), then a rise, a sharp turn and a fall to a blob (h), the outline of the same word on hcp-1361 and hcp-1367.

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by subtracting one.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext

| Line | Ciphertext | Plaintext |
|---|---|---|
| plain | G. H. Friday. / No. 1. | (not enciphered) |
| 1 | Nz. Pxo. Mpwjoh Cpz.. | MY OWN LOVING BOY |
| 2 | Op. ujnf. up. | NO TIME TO |
| 3 | Tfoe Mfuufs | SEND LETTER |
| 4 | Mpwf. & Lt.. | LOVE & [Lt..] |
| 5 | Gspn. Zpvs. Pxo | FROM YOUR OWN |
| 6 | M. h. Hjsm | [M. h.] GIRL |

Square brackets mark groups kept literal. Punctuation in the sentences below is editorial, and the groups are left unexpanded in both.

**English** (the plaintext language): *My own loving boy, no time to send letter. Love & Lt.. from your own M. h. girl.*

**Slovak:** *Môj vlastný milujúci chlapec, nemám čas poslať list. Láska & Lt.. od tvojho vlastného M. h. dievčaťa.*

## What remains uncertain

- **`Lt..` (line 4).** A looped L, a c-like stroke with a short dash, and two dots, the same group as on hcp-1371. The small sign is read as t by that parallel; c or r are not excluded. Shifted it gives "Ks", and "Love & Ks" might mean love and kisses. That is a hypothesis, not a reading.
- **`M. h.` (line 6).** The first sign has M's three downstrokes, but N stays possible, and hcp-1371 was transcribed `N.` in this slot. The second sign is h rather than L. Whether the group is enciphered (shifted: L. g.) or literal, and what it means, is open.
- **`Mpwjoh`.** The ink is partly pale and this j has no dot, though neither does the j of `Hjsm`. The w does not visibly run into the j as on the sisters.
- **`Mfuufs` (line 3).** The ink fails mid-word. The u u and f are very pale, with two pale forms at the f and three small black blots on the baseline, taken as pen blots. Six letters are the best count, not a proved one.
- **`Cpz`.** The z is pale, with a dark foot dash.
- **Signs decided by context.** The final s of `Zpvs` is a small hook unlike the s elsewhere on the card. The u of `up` and `ujnf` looks like n (MO, MIME would make no sentence). The o of `Tfoe` is a squeezed stroke with no counter, and the o of the first `Pxo` is a filled blob.
- **Heading.** The ornate F of "Friday" is supported by date and calendar. The initials G. H. appear as C. H. on some sisters. Neither is part of the cipher.
- **Postmark.** Only WIM... is firm. The address and picture side were not re-read in review 2.

## Why the reading is believed correct

One fixed shift, not tuned to this card, gives English for all 51 enciphered letters. NO TIME TO SEND LETTER is a fresh sentence rather than one of the couple's formulae, and it explains why the card is short. Line 1 has the outline of the same line on two finished sister cards, the closing matches the formula on hcp-1371, and the heading agrees with postmark and calendar. A reviewer's own script and own transcription gave the same text, and neighbouring shifts gave no English.

## Review summary and what changed

Both reviews were made by a separate Claude Opus 5.5 agent, which re-read the card from the original scan.

- **Review 1 (2026-10-30).** Found that `Op 2.` was `Cpz`, and that ink after the supposed `Mpwf` of line 1 had been omitted. It proposed `Mpwfs`. The solver accepted the omission and `Cpz`, but argued for `Mpwjoh`, updated all counts (now 51 + 4), retranscribed `N. h.` as `M. h.`, and corrected the wording on the numbering and on WIMBORNE.
- **Review 2 (2026-10-30): verdict ACCEPT.** The reviewer checked `Mpwjoh` sign by sign, withdrew its own `Mpwfs`, and reported four minor disclosure points: the final sign of `Zpvs`, the missing j dot, the description of the hcp-1367 comparison, and the pale forms in `Mfuufs`. All four were added to the uncertainties. No word changed.
- **Not verified by the reviewer:** the meaning of `Lt..` and `M. h.`, and whether a published solution exists outside this repository.

## Credits

Transcription, analysis, decipherment and report by Claude Opus 5.5 as solver; there was no earlier work on this number. The key and comparison shapes come from sister-card work in this repository by an OpenAI GPT solver and Claude Opus 5.5. The reading of `Cpz` and the discovery of the extra signs in line 1 are the reviewer's.
