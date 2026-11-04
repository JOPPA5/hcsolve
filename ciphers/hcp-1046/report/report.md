# HCP 1046 (cpc_1909-07-13_DE_-(Schlesien)_DE_Hier_fritzlehmann-04): a number-cipher teasing line to Fritz Lehmann

Human solver: Tomáš Pavuk

**Status: deciphered in full (18 of 18 cipher numbers); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1046 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1046), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Fritz Lehmann, with no transcription or solution attached. The portal links the HistoCrypt article https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 as a general reference for the collection.

The picture side is a printed photographic card titled "Der Herzensschmied" (a smith hammering a heart on an anvil), with the printed verse "Mein Herz ist ganz, o Schmied dafür Dank ich mein ganzes Leben dir" and the publisher mark B.N.K. 32781/6; it carries no handwriting. The address side has a Germania 5-pfennig stamp of the Deutsches Reich with a postmark showing 13 . 09 (the portal date is 13 July 1909); the place name on the postmark is not legible on the scan, and the portal file name gives only "(Schlesien)". The address is in plain Kurrent: **An Herrn Fritz Lehmann, Hier, Alte L...straße No 29, Tischlerm. H. Franke** ("To Mr Fritz Lehmann, here [local delivery], Alte L... street no. 29, care of master joiner H. Franke"). The message is two short lines of ink numbers written sideways on the left half of the address side.

The card belongs to a group of cards to Fritz Lehmann in the same collection. The sister cards HCP 1113 (posted in Freiburg in Schlesien, 30 July 1909, signed "Susi") and HCP 1134 use the same number cipher; they were deciphered and reviewed earlier in this repository, and the key was transferred from them.

![Address side (source/address-large.jpg)](../source/address-large.jpg)

![Message turned upright, from the high-resolution scan (work/crops/msg.png)](../work/crops/msg.png)

![Picture side, printed only (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, made by Claude Opus 5.5 from the un-converted high-resolution scan of the address side (3469 x 2298 px, work/hires/). The message area was turned upright and every number was read on 3-5x enlargements. Dots separate letters and dashes separate words. The doubtful places were compared with other digits on the same card: the two crossed first numerals (5 and 3), the umlaut over 15, and the last number of line 2 (20, whose second digit has the same looped form as the 0 in both "10"s, unlike the heavy 1 of "21" in line 1; work/crops/cmp21_20.png).

All numbers lie between 3 and 23, which points to the plain number alphabet already found on the sister cards. Under that key, A=2 ... Z=26 with J omitted, the 18 numbers give three German words with no number left over and no letter adjusted.

The reviewer cut and rotated the message from the high-resolution scan itself, typed its own number sequence and decoded it with its own script; its reading agreed with the solver's number for number.

## Key

Number substitution (simple monoalphabetic), German, 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |

| O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

A diagonal stroke across the first numeral of a word (5 and 3 here) appears to mark a capital, as on the 19s of HCP 1113. A double mark over 15 makes it Ö. Numbers occurring on this card: 3 4 5 6 9 10 11 12 14 15 18 19 20 21 23.

## Plaintext

Transcription (x marks the diagonal stroke, : the umlaut):

```text
5x.21. - 11.12.6.10.14.6.18. -
3x.15:.19.6.23.10.4.9.20.
```

Decoded:

```text
DU KLEINER
BÖSEWICHT
```

German, normalized: **Du kleiner Bösewicht!**

English: **You little rascal!** (literally "you little villain")

Slovak: **Ty malý darebák!** (literally "ty malý zloduch")

A teasing endearment, in keeping with the love motif of the picture and with the other Lehmann cards of 1909.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1046/work/decode.py
```

The script checks the SHA-256 hashes of the two source scans and the high-resolution address scan, then decodes the manual transcription work/transcription.txt with the key above and prints `DU KLEINER BÖSEWICHT`. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **The two crossed first numerals.** Line 1 begins with a 5 and line 2 with a 3, each crossed by a diagonal stroke. They are read as 5 = D and 3 = B with a capital marker; read as stylised Latin capitals D and B they give the same text. There is no uncrossed 5 or 3 on this card to compare.
- **Last number of line 2** is 20 (T), from the shape of its second digit; word sense (BÖSEWICHT) agrees.
- **Umlaut.** The double mark stands above the 15 and is read as Ö. Without it the word would be BOSEWICHT, with the same meaning.
- **Faint stroke.** A very light, short wavy stroke to the right of the 15, before its dot, is much fainter than the writing and is taken as a pen trace, not a sign.
- **Address.** The house number reads No 29, possibly written over a 1. The street name is one unread Kurrent word ("Alte L...straße", possibly "...hofstraße"); it is not part of the message.
- **Sender and place.** The card has no signature; the postmark place is not legible on the scan.
- **Hidden writing.** The stamp is still affixed, so anything under it cannot be checked; no ink shows at its edges or in the stamp box margins. The picture side carries only printed text. No steganographic message was found on this card.
- **Prior publication.** One web search on 2026-11-03 found no published solution of this card (the nearest hit, Klausis Krypto Kolumne 2018-11-14, concerns a different 1909 card in shorthand); the portal had none attached.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (hash checks OK, output identical to the claimed plaintext), cut and rotated the message itself, read all 18 numbers from 3x enlargements and decoded them with its own script; its reading agreed number for number. It confirmed the crossed 5 and 3, the umlaut, the 20 at the end, the key against the sister cards, and that the picture side and the stamp box show no other writing. Its three minor findings and what changed:

- **Faint stroke right of the 15.** Now listed among the uncertainties as a pen trace.
- **Address details.** The house number is now given as No 29 (possibly corrected); the street name is stated as one unread address word.
- **Position of the umlaut.** The description is corrected: the mark stands above the 15 itself.

No decoded letter changed as a result of the review. Transcription and decipherment were done by Claude Opus 5.5; no earlier AI work existed for this card.

## Sources

- HC Portal record 1046, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1046 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3198/conversions/cpc_1909-07-13_DE_-(Schlesien)_DE_Hier_fritzlehmann-04_pic-large.jpg (source/picture-large.jpg) and the original https://api.hcportal.eu/media/3198/cpc_1909-07-13_DE_-(Schlesien)_DE_Hier_fritzlehmann-04_pic.jpg.
- Address side: https://api.hcportal.eu/media/3199/conversions/cpc_1909-07-13_DE_-(Schlesien)_DE_Hier_fritzlehmann-04_adr-large.jpg (source/address-large.jpg) and the original https://api.hcportal.eu/media/3199/cpc_1909-07-13_DE_-(Schlesien)_DE_Hier_fritzlehmann-04_adr.jpg.
- Sister cards: HCP 1113 and HCP 1134 in this repository (same recipient, same key).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.
