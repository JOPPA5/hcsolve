# HCP 1349 (pc_hcp_30): "this church is opposite Park Place", an English Caesar postcard from Harrogate

Human solver: Tomáš Pavuk

**Status: whole message read (69 of 69 enciphered letters); independent review 1 verdict ACCEPT, with no change to the decoded letters. Two kinds of material stay open: the abbreviation groups `M-h.` and `M- L.'`, kept undeciphered, and the street name, which is not confirmed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1349 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1349), portal name pc_hcp_30, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-08-31, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue spelling of Abbott), with no transcription or solution attached.

The picture side is a printed colour view titled "Christ Church, Harrogate": a church tower among trees beyond a broad green. It has no handwriting.

The address side is in plain writing: **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**, with a halfpenny Edward VII stamp. The postmark shows "10", fragments that fit a date of 31 August, and "07"; the town cannot be read. 31 August 1907 was a Saturday, which agrees with the heading of the message.

The message fills the left half of the address side and is read after turning the card 90° counter-clockwise. By hand, key and formula it belongs to the Abbott correspondence, a run of Caesar postcards between a couple (HCP 1386–1407 and neighbouring records in this repository).

![Picture side: Christ Church, Harrogate (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned: message on the left half, address on the right (source/address-large.jpg)](../source/address-large.jpg)

![Message side turned 90° counter-clockwise for reading (work/reading.jpg)](../work/reading.jpg)

## Method

The transcription is manual, made by the solver from the un-converted scan turned to reading position, with every sign checked on 3–7× enlargements. No OCR was used and the portal supplied no transcription. The heading "G. H. Saturday" is in clear.

The rest opened at once with the shift known from the sister cards: `Nz Pxo` = MY OWN, and `Divsdi`, whose repeated pattern fits CHURCH. The key was treated as a hypothesis from those cards and tested on this card; one shift gives English for every enciphered letter. Nothing was restored, and no letter needs an exception. Dead ends recorded along the way: "York" for `Qbsl` (sign 2 is b, not p), and a capital G inside `pqqptjuf` (it is t followed by j).

## Key

Simple Caesar substitution: each plaintext letter is written as the next letter of the alphabet, so decryption is a shift of −1.

```text
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Reproduction, from the repository root:

```sh
python3 -I ciphers/hcp-1349/work/solve.py
```

The script checks the SHA-256 of the source files, decodes work/transcription.json, tests the round trip and prints the lines below. Output ends: 69 enciphered letters decoded, round trip OK.

## Plaintext

| Line | Ciphertext | Plaintext |
|---|---|---|
| heading (clear) | G. H. Saturday | G. H. Saturday |
| 1 | Nz. Pxo. **M-h.** Cpz. | MY OWN [M-h.] BOY |
| 2 | uijt Divsdi Jt. | THIS CHURCH IS |
| 3 | pqqptjuf | OPPOSITE |
| 4 | Qbsl. Qmbdf. | PARK PLACE |
| 5 | uif. mbtu pof | THE LAST ONE |
| 6 | pg. uijt tupdl. | OF THIS STOCK |
| 7 | **M- L.'** Zpvs. Pxo. | [M- L.'] YOUR OWN |
| 8 | **M-h.** Hjsm. | [M-h.] GIRL |

The groups in bold are kept literally, not decoded. Dots on the card are irregular and carry no meaning.

**English (original language, punctuation editorial):** *G. H. Saturday. My own [M-h.] boy, this church is opposite Park Place. The last one of this stock. [M-L.] Your own [M-h.] girl.*

**Slovak:** *G. H. sobota. Môj vlastný [M-h.] chlapec, tento kostol je oproti Park Place. Posledná z tejto zásoby. [M-L.] Tvoje vlastné [M-h.] dievča.*

"This church" points straight at the printed picture. "The last one of this stock" most naturally means the last picture postcard of a stock she had; that gloss is the solver's, not on the card.

## Uncertainties

- **Abbreviation groups.** `M-h.` (lines 1 and 8) and `M- L.'` (line 7) are not expanded. Whether they are enciphered at all is unknown; shifted they would give L. G. and L. K. Their capital has three downstrokes, against two in `Nz`, so it is reported as M; sister cards report what is probably the same group variously as M or N. In line 7 a short stroke and a dot follow the L, reported as an apostrophe-like mark.
- **First sign of `Qbsl`.** It is pale and crosses the descenders of line 3. It is a large 2-shaped capital, not the 9-shaped Q read on HCP 1369. Q rests on its match with the capital of `Qmbdf`, where only Q gives a word, and on the sense. MARK and LARK are unlikely for that reason, and YARK is no word.
- **First sign of `Qmbdf`.** Its top overlaps a descender of the line above; the base and tail are clear, and Q rests on the word.
- **`pqq` in `pqqptjuf`.** The signs are pale and tangled with the watermark. They read as two bowls with descenders; g would give no word.
- **Final l of `tupdl`.** Pale and crossed by a dark descender, but its loop and foot are visible. STOCK is the only word found.
- **The street.** The card clearly spells PLACE, but a Park Place in Harrogate in 1907 is unverified. The reviewer's two web searches found none. They did find a Park Parade in the Christ Church area and York Place on the Stray. The name is the writer's, and it may be a loose name for Park Parade; this is a possibility only. York Place fails on the pixels.
- **Heading and postmark.** "G. H." is unexplained, and its G could be C on form, which does not affect the message. The postmark town could not be read.
- **Published solutions.** The portal shows none. No wider search for a published reading of this card was made beyond the street lookups.

## Review and what changed

The review was done by a separate Claude Opus 5.5 session; solver and reviewer are the same model, so this is not a cross-vendor check. The reviewer ran the command, decoded its own rows with its own script (same 69 letters; shifts 0, 2 and 25 give no language), re-read every row on its own crops, tested York Place as the best rival, and checked the date. Verdict: **ACCEPT**, with three minor findings:

- **Group capital.** The capital of the groups is M rather than N. Fixed in the transcription and glosses, after re-reading lines 1, 7 and 8. The 69 decoded letters did not change.
- **Wording on the `Qbsl` capital.** The foot had been called unparalleled, and MARK and LARK left too open. Corrected: the foot is probably re-inking.
- **Street name.** The Park Parade and York Place lookups were added, with the name marked as unconfirmed.

The reviewer could not verify the postmark town, the meaning of the groups and of "G. H.", or whether a Park Place existed in 1907, and considers the "last postcard" gloss reasonable but the solver's own. These points stay open.

## Credits

Capture, transcription and decipherment: Claude Opus 5.5, 2026-10-30; there was no earlier work on this number. Independent review: a separate Claude Opus 5.5 agent. The key and formulae were compared with sister cards in this repository as hypotheses and tested on this card's pixels.
