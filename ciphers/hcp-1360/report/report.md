# HCP 1360 (pc_hcp_41): "No letter", a Caesar-shift postcard of 3 July 1907

Human solver: Tomáš Pavuk

**Status: whole message read (56 enciphered letters, all decoded by one key; one abbreviation group of 2 letters kept literal and not expanded); independent review 1 verdict REVISE, findings addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1360 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1360), portal name pc_hcp_41, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-07-03, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue spelling of Abbott). No transcription or solution is attached.

The picture side is a printed view, "St. Paul's Cathedral, London", with no handwriting.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address side is addressed in plain to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon. It has a halfpenny Edward VII stamp and two strikes of a WIMBORNE postmark, time 10 PM; the date in the postmark cannot be read.

![Address side (source/address-large.jpg)](../source/address-large.jpg)

The message stands at the left of the address side, turned 90 degrees. Its heading "G. H. Wednesday." and its date "July 3rd 07" are in plain writing. 3 July 1907 was a Wednesday, and the portal gives the same date. The English language was established by the decipherment.

The recipient, the Wimborne postmark, the hand and the formulae match a series of cards to W. Abbott in this repository (for example HCP 1361, 1366, 1367 and 1386–1407), written by a young woman to her sweetheart in 1907–08.

## Method

The transcription is manual. The solver turned the high-resolution scan of the address side and enhanced it by dividing the blue channel by a local background estimate, which separates pale ink from the grey HC Portal watermark better than a plain threshold.

![Message rotated and enhanced, watermark partly suppressed (work/msg_flat.png)](../work/msg_flat.png)

The key was not recovered blind. The shift known from the sister cards was tested first as a hypothesis, and it gave English at once. The script `work/decode.py` checks the file hashes, decodes every token of the manual transcription and prints the text; it does not read the image.

## Key

Caesar substitution: each plaintext letter is written as the next letter of the alphabet. To decrypt, subtract one (A→Z).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading and the date are in clear. The group `M. h.` is an abbreviation of the kind found in this series (`M-h` on HCP 1367 and 1369) and is kept literal.

## Plaintext

| Line | Ciphertext | Plaintext |
|---|---|---|
| heading (clear) | G. H. Wednesday. | G. H. Wednesday. |
| 1 | Nz. Pxo. Mpwjoh Cpz | MY OWN LOVING BOY |
| 2 | J. Gffm wfsz | I FEEL VERY |
| 3 | Ejtbqqpjoufe. up | DISAPPOINTED TO |
| 4 | Ebz. "Op Mfuufs". | DAY "NO LETTER". |
| 5 | Zpvs. M. h. Hjsm. | YOUR [M. h.] GIRL. |
| date (clear) | July 3rd 07. | July 3rd 07. |

The card is in English, so the first version below is the normalized original rather than a translation.

**English:** *G. H. Wednesday. My own loving boy, I feel very disappointed to-day: "no letter". Your M. h. girl. July 3rd 07.*

**Slovak:** *G. H. Streda. Môj vlastný milujúci chlapec, dnes som veľmi sklamaná: „žiadny list". Tvoje M. h. dievča. 3. júla 1907.*

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1360/work/decode.py
```

The script reports `enciphered letters decoded: 56 | abbreviation letters kept literal: 2` and writes `work/plaintext.txt`.

## Uncertainties

- **`Mpwjoh`, pale ending.** The j, o and h are pale, because the pen was failing, and they partly lie on a watermark band. Their outline matches the same word on HCP 1361 and 1367.
- **O of `Op`.** The sign is pale, crosses a band and shows no closed loop. NO rests on the sense ("disappointed", then LETTER).
- **`M. h.`** The first sign has one stroke more than the N of `Nz`, but N stays possible. The second sign is preferred as h, but L stays open because the same slot is read L on some sisters. The meaning is unknown, and it is undecided whether the group is enciphered. A spot after the first sign may be a period or foxing.
- **`Pxo` and `Ejtbqqpjoufe`.** The P runs into the underline, and letters of the long word tangle with descenders from the line above. Both words are fixed by the pattern and by the sense.
- **Quotation marks.** The two closing ticks are clear. Before `Op`, part of the marks is the foot of a j from line 3, so the opening pair is only plausible.
- **"to / day".** `up` ends one line and `Ebz` opens the next; no hyphen is visible, though sisters write `up-Ebz`.
- **Heading and postmark.** The meaning of "G. H." is not established, and some sisters are read C. H. The postmark date is illegible, so the date rests on the writer's plain date, the weekday and the portal.
- **Identity.** The writer is known only through the series, and the portal gives no sender.
- **Published solutions.** No web search was run. The portal attaches no solution, and the AI Decipherment Register had no record of this card on 2026-10-30.

## Review and what changed

An independent Claude Opus 5.5 agent (same model, separate session, so not a cross-vendor check) reviewed the card. It ran the command, verified the hashes, decoded its own transcription with its own script, and re-read every line from enlargements of the original scan. It returned **REVISE** with five findings:

- **Line 1 was misread.** The solver first read `Mpwf` + a literal `h.` (MY OWN LOVE [h.] BOY), rejecting `Mpwjoh` for lack of an o loop and a final h. The pixels show otherwise: a long stroke to a foot under the line (j), a thin closed lens (o), and a stroke rising and falling to a blob (h).

  ![The word on this card (top) beside the same word on HCP 1361 and 1367 and a parallel from HCP 1363 (review/work/cmp_mpwjoh.png)](../review/work/cmp_mpwjoh.png)

  The solver checked this comparison and agreed, so the line now reads MY OWN LOVING BOY, the stock opening of the series.
- **Counts corrected.** The card has 56 enciphered letters and one literal group of 2 letters, not 54 and 3.
- **O of `Op`.** The weak capital is now disclosed.
- **`N. h.` became `M. h.`** The sign has three strokes, with N still possible.
- **Opening quotation ticks.** The foot of a j from line 3 is now noted.

The key, and the other four lines, did not change.

## Credits

Capture, transcription, decipherment and review by Claude Opus 5.5 agents, 2026-10-30. There was no earlier work on this number. The key and formulae were taken as hypotheses from accepted sister cards and tested on this card.

## Sources

- HC Portal record 1360, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1360 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4140/pc_hcp_41_pic.JPG
- Address side: https://api.hcportal.eu/media/4141/pc_hcp_41_adr.JPG
- Sister cards in this repository: ciphers/hcp-1361, 1366, 1367, 1369, 1386–1407.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked by the orchestrator on 2026-10-30.
