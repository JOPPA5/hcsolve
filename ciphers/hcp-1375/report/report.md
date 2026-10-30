# HCP 1375 (pc_hcp_56): an English Caesar sweetheart postcard, 15 October 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (59 of 59 enciphered letters); two abbreviation groups kept literal; one sign group in SPIN rests on a disclosed shared-stroke reading. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1375 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1375), portal name pc_hcp_56, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-10-15, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached.

The picture side is a printed view, "St. Mary Redcliffe, Bristol" (The Wrench Series No. 14921), with no handwriting. The address side carries a halfpenny Edward VII stamp cancelled **WIMBORNE, 10 PM, OC 15 07** and is addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon** (the portal's "Abboú" is a misreading of Abbott). 15 October 1907 was a Tuesday, which agrees with the plain heading "(G. H.) Tuesday" and the plain dateline "Oct. 15th = 1907."

The message is written on the left half of the address side, sideways (turn the scan 90° counter-clockwise). The grey wheel over the writing is the portal's watermark, not part of the card. The card belongs to a group of Caesar-shifted English cards between one couple in 1907–08, sent to W. Abbott and using the same key and the same formulae ("My own … boy", "from your own … girl"). Several are deciphered in this repository, for example HCP 1377, 1380 and 1386.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as delivered (source/address-large.jpg)](../source/address-large.jpg)

![Message turned upright, contrast stretched, from the original scan (work/message-rotated.png)](../work/message-rotated.png)

## Method

The transcription is manual, with no OCR. The solver turned the un-converted original scan (work/hires/pc_hcp_56_adr.JPG) upright, read it at 3–8x enlargement, and recorded it in work/transcription.json. The key was not recovered here: it was taken as a hypothesis from the sister cards and tested on this card, where one fixed shift turns every letter into a coherent English sentence. Non-formula words such as `bgufsoppo` (AFTERNOON) and `xbt pvu gps` (WAS OUT FOR) decode with no adjustment.

All work on this card is by Claude Opus 5.5. No published solution of this card was found: the portal lists none and the AI Decipherment Register had no record of it on 2026-10-30.

## Key

Caesar shift: each plaintext letter is written as the next letter of the alphabet. To decrypt, subtract one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

`(G. H.) Tuesday` and `Oct. 15th = 1907.` are ordinary writing. `E. L.` (twice) and `N & L` are abbreviations kept literal, as on the sister cards.

## Plaintext

| Ciphertext | Plaintext |
|---|---|
| (G. H.) Tuesday | (plain) |
| Nz. Pxo. E. L. Cpz | MY. OWN. [E. L.] BOY |
| J. xbt. pvu. gps | I. WAS. OUT. FOR |
| b. mjuumf tqjo | A. LITTLE SPIN |
| uijt. bgufsoppo | THIS. AFTERNOON |
| Nz. N & L gspn. | MY. [N & L] FROM. |
| Zpvs Pxo. E. L. Hjsm | YOUR OWN. [E. L.] GIRL |
| Oct. 15th = 1907. | (plain) |

English: *"(G. H.) Tuesday. My own E. L. boy, I was out for a little spin this afternoon. My N & L from your own E. L. girl. Oct. 15th 1907."*

Slovak: *„(G. H.) Utorok. Môj vlastný E. L. chlapec, dnes popoludní som si vyšla na malú vyjažďku. Moje N & L od tvojho vlastného E. L. dievčaťa. 15. okt. 1907."*

The Slovak "vyšla" assumes a woman writer, which the signature "girl" gives.

## Reproduction

From the repository root:

```
python3 -I ciphers/hcp-1375/work/decode.py
```

It checks the SHA-256 of the source images and the original scans, then prints the plaintext from work/transcription.json: 59 enciphered letters decoded and 6 abbreviation letters kept literal.

## Uncertainties

- **`tqjo` = SPIN, the one real reading point.** The barred `t` is secure. The second sign is a bowl with no separate tail; a hairline runs from it to the top of the long diagonal, and the diagonal is read as the stem of both `q` and `j`. A scan cannot prove stroke order. Without this the group is `tojo` / `tbjo` (SNIN / SAIN, not words); SHIN and SKIN fail on the sign and on sense. HCP 1370 has `Mjuumf. Tqjo.` ("having a little spin") with a clearer `q`, but that card leans on this one for its T and is not yet final, so the two support each other without either proving the other. Nothing on this card says what the spin was on; a sister card (HCP 1377) mentions a bike.
- **`mjuumf` = LITTLE.** The minims run together, and the dot lies inside the first arch of `m`, about 90 px of the scan left of the `j` stem. The letter count fits, and the word recurs on HCP 1370.
- **Second `Pxo`, last letter.** A dark blot in an ink halo with no visible counter. It is read as `o` from the group and the formula.
- **`E. L.`, `N & L`, `G. H.`** are not expanded; their meaning is unproved. The first letter of `N & L` has two full downstrokes as in `Nz`, but also a short stub on the second foot (figure below), and sister cards divide between N and M on this group. `M & L` stays possible. No decoded word depends on it.
- **Word-dots** are placed irregularly and carry no meaning.

![Bowl, hairline and long diagonal of tqjo, enlarged (review/work/z_tqjo.png)](../review/work/z_tqjo.png)

![First letter of the closing group, with the stub on its second foot (work/closing-N-stub.png)](../work/closing-N-stub.png)

## Review summary

A separate Claude Opus 5.5 agent reviewed the solution with verdict **ACCEPT**. It re-ran the command, decrypted from its own letter list with its own script (same 59 letters, one shift, no exceptions), checked every word against the original scan at 2–8x, and confirmed the addressee, postmark, caption and weekday. It did not repeat the web check for a published solution.

Its four findings were all minor, and none changed the plaintext:

- The first account of the `q` was wrong. It treated the hook under the bowl as the `q` tail with a faint trace in the gap. The hook is the normal foot of `j` and the gap is clean paper, so the claim was replaced by the hairline and shared-stem description.
- "The only English word available" was overstated. SHIN and SKIN are now named, and HCP 1370 is cited with its dependence stated.
- The blotted `o` of the second `Pxo` was undisclosed and is now listed.
- The position of the `mjuumf` dot is now stated exactly.

After the review the solver also disclosed the stub on the N of the closing group, found while comparing with the review of HCP 1370. That point is the solver's own and was not seen by the reviewer.

## Sources

- HC Portal record 1375, https://crypto.hcportal.eu/dashboard/cryptograms/1375: picture and address scans, listed with URLs and hashes in SOURCES.md.
- Sister cards in this repository: HCP 1370, 1377, 1380, 1383, 1386.
