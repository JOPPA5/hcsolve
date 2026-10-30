# HCP 1363 (pc_hcp_44): an English Caesar sweetheart postcard, 19 July 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (55 of 55 enciphered letters); two abbreviation groups, `Lt..` and `M. h.`, kept literal. Review 1 verdict REVISE (one headline word corrected), review 2 verdict ACCEPT.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1363 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1363), portal name pc_hcp_44, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-07-19, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached. No published solution of this card was found or used. That rests on this repository and on a check of the AI Decipherment Register; no general web search was made.

The picture side is a printed view, "Royal Baths, Hospital, Harrogate", with no handwriting. The address side, from the Boots "Pelham" Series, carries a halfpenny Edward VII stamp. The postmark reads 10 PM, JY 19, 07, and its town name is not legible. The card is addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**; the portal's "Abboú" is a misreading of Abbott. 19 July 1907 was a Friday, which agrees with the plain heading "Friday. No. 2."

The message is written on the left half of the address side and is read after turning the scan 90 degrees counter-clockwise. It is the companion of HC Portal 1366: same day, same postmark time, same card series and same Harrogate subject, headed "No. 1." where this one is headed "No. 2." Both belong to the group of Caesar-shifted English cards from one couple in 1907–08, sent to W. Abbott at Stokelake Farm. The disc and building logo on the scans are a scanning overlay, not part of the card.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![The message turned to reading position (work/crops/message_ccw.png)](../work/crops/message_ccw.png)

## Method

The transcription is manual, made from enlarged crops of the un-converted scan (3–6x, with a blue-minus-red ink filter and a contrast boost for pale strokes). The Caesar shift was taken as a hypothesis from sister cards and then tested on this card: the single shift decodes every enciphered letter, with no adjustment for any word. Among the 26 possible shifts, only this one yields English words, in an independent test by the reviewer (13 of 13 distinct tokens; every other shift gave none).

The heading "Friday. No. 2." is in ordinary writing. The decoder (work/decode.py) checks the file hashes, decodes the transcription (work/transcription.json) and verifies the inverse round trip. It works from the manual transcription, not from the image.

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the next letter of the alphabet. To decipher, subtract one.

```text
Cipher  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain   ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

Dots are the writer's separators, not sentence punctuation. Groups in square brackets are kept literal.

| Line | Ciphertext | Plaintext |
|---|---|---|
| plain | Friday. No. 2. | (not enciphered) |
| 1 | Nz. Pxo Mpwjoh Cpz | MY OWN LOVING BOY |
| 2 | Nboz. uibolt - | MANY THANKS |
| 3 | gps. dbset. pg. | FOR CARDS OF |
| 4 | Xjoetps. Mpwf. | WINDSOR. LOVE |
| 5 | &. L. t.. gspn. | & [Lt..] FROM |
| 6 | Z. P. M. h. Hjsm | Y. O. [M. h.] GIRL |

English: *"Friday. No. 2. My own loving boy, many thanks for cards of Windsor. Love & Lt.. from Y. O. M. h. girl."*

Slovak: *„Piatok. Č. 2. Môj vlastný milujúci chlapec, veľká vďaka za pohľadnice Windsoru. Láska & Lt.. od Y. O. M. h. dievčaťa."*

The punctuation of the sentences is editorial. Y. O. probably stands for "Your Own", which the companion card writes out, but the text keeps the initials.

Two marks on the message side are not text: a grey streak with a dark upright blot under `gps`, and a long dark line under `Hjsm` running to the card edge, which is a pen flourish or a card defect.

## Uncertainties

- **`& L. t..` (line 5).** The ink runs out here. The & and the L are very pale and are identified by shape and slot from the same group on hcp-1366 and hcp-1371, not by being readable alone. The small sign is read t by that parallel; c or r are not excluded. The two marks after it are unequal: the first is about twice as wide as the second and has a tail, so it may be a dot run into a stroke. The meaning of the group is not established. Shifted it gives "Ks", which might mean kisses, but that is a hypothesis and the plaintext does not use it.
- **`M. h.` (line 6).** The first sign has three downstrokes, as an M, though N is possible; L for the second sign is not excluded. Meaning unknown. Kept literal; shifted it would be L. g.
- **`Z. P.` (line 6).** Treated as enciphered, Y. O., because that has an expansion in the usual closing slot. The expansion is an inference.
- **`Xjoetps`, end (line 4).** The final s is only a very pale reduced stroke, the weakest sign of the word. No other letter gives a word.
- **Final t of `uibolt` and `dbset`.** Neither has a bar on the stem, so by shape alone each could be l; the words rest on the sense. The dash after `uibolt` may be a line filler or a displaced t-bar. `dbset` also has a run-together s and e and rests partly on the same word on hcp-1368 and hcp-1400.
- **`pg.` (line 3).** The g is pale but complete. A dot between p and g is taken as stray.
- **Not verified.** The postmark town, and whether the Windsor cards existed: no sister card mentions them.

The text is short, so the proof rests on the shared key and on THANKS, CARDS and WINDSOR. "Many thanks for cards of Windsor" is a fresh sentence, found on no other card in this repository, and suits a couple who exchanged view postcards. `Nz Pxo Mpwjoh Cpz` is word for word line 1 of accepted hcp-1360, 1361 and 1367.

## Review and what changed

Two independent review rounds were made by a separate Claude Opus 5.5 agent, which decoded the card with its own script and its own retyping of the ciphertext and checked each line on its own enlargements.

**Review 1 (REVISE).** The solver first read line 1 as `Mpwfs` (LOVER). The reviewer showed that the ending has no support in this hand's s, and that the same outline stands in this slot on sister cards. The solver found that the error began one sign earlier: the long stroke ends in the hooked foot of a j, not the closed foot loop of an f, and the word is `Mpwjoh`, LOVING. The comparison is shown below. Four minor points were also fixed: M rather than N in `M. h.`, a fuller description of the final t strokes and the dash, the support for `Lt..`, and the two non-text marks.

![Line 1 compared with the f and j of this card and with the same word on sister cards (work/review1/cmp_mpwjoh_1363.png)](../work/review1/cmp_mpwjoh_1363.png)

**Review 2 (ACCEPT).** The reviewer tried to refute `Mpwjoh` on the pixels and could not. It re-read every word, repeated the decode with `Mpwjoh` retyped and found no other shift that gives words. Three minor record points were fixed without changing any letter: stale notes about the sister cards, the separator dots (none after `Pxo`; one each after the & and the L), and a more exact description of the marks after the small sign in line 5.

## Credits

Transcription, decipherment and report by Claude Opus 5.5, 2026-10-30, with independent review by a separate Claude Opus 5.5 agent. The reading `Mpwjoh` for this card was first suggested in a reviewer's note on hcp-1360. The key and the comparison shapes come from sister-card work in this repository by an OpenAI GPT solver and Claude Opus 5.5. No earlier work on this number exists.
