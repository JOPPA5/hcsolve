# HCP 1367 (pc_hcp_48): a Caesar-shifted birthday greeting, 25 July 1907

Human solver: Tomáš Pavuk

**Status: whole message read (53 enciphered letters); independent review 1 verdict REVISE, findings addressed. One closing abbreviation stays unexpanded and two spelling slips of the writer are disclosed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1367 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1367), portal name pc_hcp_48, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-07-25, language Unknown, sender Unknown, recipient "W. Abboú" (a catalogue spelling of Abbott), with no transcription or solution attached.

The picture side shows the printed view "Shrine of Edward the Confessor, Westminster Abbey" and has no handwriting. The address side (Valentine's Series) has a halfpenny Edward VII stamp and the postmark WIMBORNE, 10 PM, JY 25 07. It is addressed in plain writing to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. The message stands on the left half of the address side, turned 90 degrees.

Recipient, hand and set phrases match a group of English cards sent in 1907–08 to W. Abbott by the same couple (HCP 1386–1407 and others in this repository).

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Message turned to reading position (work/crops/reading.png)](../work/crops/reading.png)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual. The message was read sign by sign from the un-converted portal scan, rotated and enlarged 3–6×. The family key was tried first as a hypothesis and fitted at once: `Nz Pxo` = MY OWN, `Pg uif Ebz` = OF THE DAY. The review then re-read every row from its own crops and decoded with its own script. Of the 26 possible shifts only −1 gives language.

The heading "Thursday" agrees with the date on the card and the postmark: 25 July 1907 was a Thursday.

## Key

Caesar shift: each plaintext letter is written as the next letter of the alphabet. To decrypt, subtract one (A becomes Z).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading `G. H. Thursday.` and the date `July 25th 07` are in plain writing. The group `M-h` is kept literal.

## Plaintext

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Pxo. Mpwjoh Cpz. | MY OWN LOVING BOY |
| Wfsz. nboz. | VERY MANY |
| Ibooz. Sfufsot. | HANNY RETERNS (intended HAPPY RETURNS) |
| Pg uif Ebz. | OF THE DAY |
| Zpvs. Pxo M-h. | YOUR OWN [M-h] |
| *July 25th 07* Hjsm. | *(plain date)* GIRL |

English (the original language), with the two slips normalised:

> G. H. Thursday. My own loving boy. Very many happy returns of the day. Your own M-h girl. July 25th 07.

Slovak:

> G. H. Štvrtok. Môj vlastný milujúci chlapec. Veľmi veľa šťastia k dnešnému dňu. Tvoje vlastné M-h dievča. 25. júla 1907.

To reproduce the text, run from the repository root: `python3 -I ciphers/hcp-1367/work/decode.py`

## Uncertainties

1. **`Ibooz` = HANNY.** Both middle signs are closed loops without tails, the same as `o` elsewhere, so the literal decode is HANNY. HAPPY (`Ibqqz`) is the intended word by the set phrase. This is an emendation, and its cause is unknown.
2. **`Sfufsot` = RETERNS.** Only two minims stand between the two f signs, which is one `u`; the second f is pale and re-inked. RETUERNS is a weaker alternative. RETURNS is not in doubt, but these are the weakest signs on the card.
3. **M of `Mpwjoh`.** The third leg merges into the following p. MOVING is excluded by sense, not by the pixels alone.
4. **`M-h`.** The capital has three downstrokes, like the M of `Mpwjoh` and unlike the N of `Nz`. The second sign is preferred as h, but L stays open, because the same slot is read L on HCP 1371 and 1402. Sister cards show `N. h.`, `N. L.` and `E. L.` here. The meaning is unknown, and it is undecided whether the group is enciphered.
5. **Heading.** The meaning of G. H. is not established, and sister solutions note that the G may be C; on this card G is the better reading.
6. **Occasion.** "Many happy returns of the day" implies a birthday or similar; nothing else on the card confirms it.
7. **Published solutions.** No web search was run. The AI Decipherment Register had no record of this card on 2026-10-30, and the portal attaches no solution.

## Review and what changed

An independent Claude Opus 5.5 agent (same model, separate session, so not a cross-vendor check) reviewed the card. It confirmed the decode, key coverage, plain text, postmark and language, and returned REVISE with five findings:

- The closing group was first given as `N-L`. It is now `M-h`, with L still open for the second sign.
- `Sfuvfsot` (RETUERNS, 54 letters) became `Sfufsot` (RETERNS, 53 letters).
- The argument for the M of `Mpwjoh` was strengthened by comparing it with the capital of `M-h`.
- The G/C doubt in the heading was disclosed.
- Dependent text was updated.

The sense of the message did not change.

## Credits

Capture, transcription, decipherment and review by Claude Opus 5.5 agents, 2026-10-30. The key and formulae were taken as hypotheses from accepted sister cards and tested on this card.
