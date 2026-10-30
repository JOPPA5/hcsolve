# HCP 1374 (pc_hcp_55): an English Caesar sweetheart postcard, 18 October 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (39 of 39 enciphered letters: 38 read and 1 emended by the word); two abbreviation groups kept literal. Independent review 1 verdict REVISE; all four findings addressed, with no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1374 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1374), portal name pc_hcp_55, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-10-18, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue spelling of Abbott), with no transcription or solution attached.

The picture side is a printed view, "Royal Pump Room and Baths. Leamington", with no cipher on it. The address side carries a halfpenny Edward VII stamp, the postmark WIMBORNE, 10 PM, OC 18 07, and the address Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon. The plain heading "Friday" and the plain date "Oct. 18th 1907" agree with the postmark and the portal date, and 18 October 1907 was indeed a Friday. The message runs along the left of the address side, so the card has to be turned 90° counter-clockwise to read it.

The card belongs to the correspondence of hcp-1386…1407: same recipient, same Wimborne postmark, same hand and the same formulas ("My own … boy", "your own … girl", E. L., N & L.). Those finished cards suggested the key and the letter forms as a hypothesis. The reading below was made from the pixels of this card. No published solution of this card was found or used, and there was no earlier work on this number: download, transcription and decipherment are by Claude Opus 5.5.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned: WIMBORNE postmark, address to Mr W. Abbott, Stokelake Farm, Chudleigh (source/address-large.jpg)](../source/address-large.jpg)

![The message turned upright (work/reading.png)](../work/reading.png)

## Method

The transcription is manual, with no OCR. The solver rotated the full-resolution original (work/hires/pc_hcp_55_adr.JPG) and read each word from enlarged crops, comparing doubtful signs with other signs of this hand on this card and on hcp-1386. The heading, the date and the address are ordinary writing. The five message rows are enciphered, apart from the groups `E. L.` and `N & L.`, which this writer leaves unshifted, as on hcp-1386.

One shift decodes every enciphered word, and no per-word adjustment is used. The script work/decode.py checks the hashes of the scans, decodes work/transcription.json, tests the round trip and prints the plaintext:

```sh
python3 -I ciphers/hcp-1374/work/decode.py
```

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. To decrypt, subtract one (A becomes Z).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext and translation

Square brackets around a single letter mark the emendation. `E. L.` and `N & L.` are literal, not deciphered. A single long stroke is drawn under `L. Hjsm` on the last row.

| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo E. L. Cpz. | MY. OWN [E. L.] BOY. |
| Wfs[z] jemf. tupsn | VER[Y] IDLE. STORM |
| up. Ebz. | TO. DAY. |
| Nz. N & L. zpvs Pxo | MY. [N & L.] YOUR OWN |
| E. L. Hjsm | [E. L.] GIRL |

**English:** My own E. L. boy. Very idle. Storm to-day. My N. & L., your own E. L. girl.

**Slovak:** Môj vlastný E. L. chlapec. Veľmi nečinne. Dnes búrka. Moje N. & L., tvoje vlastné E. L. dievča.

English is the plaintext language; the portal lists it as Unknown.

## Uncertainties

1. **Punctuation of "idle. storm".** The letters of IDLE are clear. A separate dot stands after `jemf`, so "Very idle. Storm to-day." is the preferred reading, and it mirrors "I have been very busy to-day" on hcp-1405. The dot is no proof, because the writer also puts dots inside `up. Ebz.`. "Very idle storm to-day" is possible but less natural. The card does not say who or what was idle.
2. **The Y of VERY is an emendation.** The fourth sign of `Wfs[z]` is faded at the top and is literally s-shaped, built like the s before it and unlike this writer's z. Literal `Wfss` gives VERR, which is no word. VERY is taken from the word, which recurs across this correspondence.
3. **The M of STORM.** The last sign of `tupsn` has two minims joined low and rising, as this writer's m does, and n and u cannot be separated in this hand. `tupsu` would give STORT, so n is chosen by the word. `tupsz` (STORY) is excluded, because the sign is not 2-shaped.
4. **Initials.** The heading initial may be G or C. `E. L.` and `N & L.` are not expanded, and the N could be another capital with similar legs. None of this affects the enciphered text.

## Review and what changed

An independent Claude Opus 5.5 reviewer tried to refute the solution. It ran the command, decoded its own transcription with its own script (same 39 letters), went through every row at 2x to 10x enlargement, and checked the context on the scans. It confirmed the key and the reading and returned REVISE with four findings:

1. **Major: sentence misparsed.** The handover gave "Very idle storm to-day" and suspected a writer's slip. The dot after `jemf` supports "Very idle. Storm to-day."; the translations and uncertainties were rewritten, and the slip suggestion was dropped.
2. **Minor: the z of `Wfsz` was shown as read.** The sign is s-shaped. It is now marked as an emendation in the table, the data file and the script's count.
3. **Minor: a dot after `Wfsz` was not on the card.** It was removed.
4. **Minor: the underline was not recorded.** It is now mentioned.

The decoded letters did not change, so no second review round was needed. The reviewer could not determine whether the paleness at the top of `Wf`, the s and the fourth sign comes from pen run-out or the portal watermark, because no clean scan exists. It also could not determine what E. L. and N & L. stand for.
