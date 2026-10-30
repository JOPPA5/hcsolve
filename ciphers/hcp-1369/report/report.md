# HCP 1369 (pc_hcp_50): an English Caesar sweetheart postcard, 26 July 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (41 of 41 enciphered letters, none restored). Two abbreviation groups and one short trailing group are kept literal and unexplained. Independent review 1 verdict REVISE; its findings are addressed and no decoded letter changed.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1369 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1369), portal name pc_hcp_50, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-07-26, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue misreading of Abbott), with no transcription or solution attached.

The picture side is a printed view, "The Bridge, Knaresborough", with no handwriting. The address side is a Boots Cash Chemists "Pelham" Series card with a halfpenny Edward VII stamp, postmarked WIMBORNE, 10 PM, JY 26, 07, and addressed in clear to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. The disc with an alphabet and the building logo on both scans are a scanning overlay, not part of the card.

26 July 1907 was a Friday, which matches the heading "G. H. Friday" written on the card. The message runs up the left half of the address side, so the card must be turned 90° counter-clockwise to read it. The heading and the date "July 26th 07" are ordinary writing.

The card belongs to a correspondence of a young couple sent to W. Abbott in 1907–08, with the same cipher, hand and formulae as cards hcp-1376 and hcp-1386 to 1407. A second card posted the same day, hcp-1368, shares its heading, date and 10 PM postmark. No published solution of this card was found or used.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![The message turned to reading position, from the un-converted original (work/crops/msg.png)](../work/crops/msg.png)

## Method

The transcription is **manual**, without OCR, made from the un-converted original scan and enlarged crops. The Caesar shift found on the sister cards was treated as a hypothesis and tested on this card. It held on every enciphered token with no adjustment, including words that are not stock formulae of the couple: SCHOOL, TREAT and PARK. Rejected first readings are in `NOTES.md`: `zpvs` was first read as "2 hrs" by analogy with hcp-1376, and the third sign of `Tdippm` as u.

In review, a separate agent made its own greyscale crops, read every token sign by sign and decoded them with its own script, arriving at the same 41 letters.

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. To decrypt, subtract one.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

Square brackets mark groups kept literal, not shifted.

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Pxo [M-h] Cpz. | MY. OWN [M-h] BOY. |
| Tdippm usfbu. | SCHOOL TREAT. |
| Jo. Qbsl. up. | IN. PARK. TO. |
| Ebz. [M. & L.] [t..] | DAY. [M. & L.] [t..] |
| zpvs. Pxo [M-h] > | YOUR. OWN [M-h] > |
| (after the date on the bottom line) Hjsm | GIRL |

41 letters read and decoded, 0 restored; 7 letters kept literal (M, h twice; M, L once; t once, tentative).

**English** (original language; punctuation editorial): *"G. H., Friday. My own M-h boy. School treat in park to-day. M. & L. t.. your own M-h girl. July 26th 07."*

**Slovak:** *„G. H., piatok. Môj vlastný M-h chlapec. Dnes školská slávnosť v parku. M. & L. t.. tvoje vlastné M-h dievča. 26. júla 1907."*

"School treat" is the period term for an outing or party given to schoolchildren. The groups `M-h`, `M. & L.` and `t..` are not translated.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1369/work/decode.py
```

The script checks the SHA-256 of the scans, decodes every token of `work/transcription.json`, checks the inverse round trip, and prints the text and counts. `work/crop.py` regenerates the crops.

## Uncertainties

- **`M-h` (twice), unexpanded.** The capital has three downstrokes against two in the N of `Nz`, so it is reported as M. The second letter is a tall stroke with a small arch at the foot, unlike the capital L on this card. Sister cards report this slot as `N-L`, `M-L`, `N-h.`, `N. h.` or `M-h.`, and the same-day hcp-1368 reports `N. L.` although its pen forms match this card. That disagreement is unresolved, and it is probably one group throughout. Shifted it would give L-G, which is not a word.
- **`M. & L.`, unexpanded.** Its meaning is unknown, and it may or may not be enciphered.
- **`t..` after `L`.** A curved stem, a short dash detached at its upper right, one dot below the dash, and two dots higher. It stands in the same slot as `N. & L. t` on hcp-1368, a very similar sign on hcp-1359, and `t..` on hcp-1361 and hcp-1363. Those cards are not finished, so this is a recurring pattern and not an accepted reading. The detached bar leaves c possible, and the dots are placed differently from hcp-1361. No word depends on it.
- **The `>` mark** ends the penultimate line. It is taken as a pointer to `Hjsm`, which stands after the date. hcp-1368 closes the same way.
- **Pale signs.** The pen was running dry in `Tdippm`, `Qbsl`, `zpvs` and `Hjsm`. The signs are faint but readable. The final m of `Hjsm` is flattened, as also noted on hcp-1386 and hcp-1376.
- **The capital Q of `Qbsl`** is 9-shaped, the same form as the q of `qptu` on hcp-1368. hcp-1349 reads a different, 2-shaped capital as Q, so the form varies across the series.

## Why the reading is correct

One fixed shift, not tuned to this card, gives English for every enciphered token. SCHOOL with its double letter, TREAT and PARK are not formulae of the couple. The sentence stands between their usual salutation and closing, "My own … boy" and "your own … girl". The weekday, postmark and plain date agree, and the card shares its recipient, address and town of posting with the sister cards.

## Review summary

Review 1 (a separate Claude Opus 5.5 agent, verdict **REVISE**) re-ran the command, decoded independently, and checked every token against the original scan. It could not refute any of the 41 letters. It had five findings:

1. **Major:** the marks after `L` are not ornament but the recurring `t..`, and were missing from the "all ciphertext" table. Fixed: added as a tentative literal with its parallels and doubts. The count of literal letters went from 6 to 7.
2. **Minor:** the sister list for `M-h` left out the closest evidence, including hcp-1368. Fixed.
3. **Minor:** the capital Q had not been compared with sister cards. Fixed.
4. **Minor:** a "small gap" in `Tdippm` is really a fine hairline, so the word is joined. Corrected.
5. **Minor:** the same-day card was not mentioned. Added.

The "0 restored" line in the script, previously a fixed string, is now computed. The review did not verify the meaning of `M-h` or `M. & L. t..`, or the whole series for sameness of hand, and it relied on the capture record for the portal status.

## Credits and sources

Transcription, decipherment and this report: Claude Opus 5.5 as solver, 2026-10-30. Independent review: a separate Claude Opus 5.5 agent. No GPT work exists on this number; sister-card work is credited in its own directories.

- HC Portal record: https://crypto.hcportal.eu/dashboard/cryptograms/1369
- File list with hashes: `SOURCES.md`
