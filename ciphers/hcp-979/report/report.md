# HCP 979 (cpc_1909-09-10_DE_Dortmund_DE_Hier_fritzlehmann-08): a fever note to Fritz Lehmann in number cipher

Human solver: Tomáš Pavuk

**Status: deciphered in full (114 of 114 cipher numbers); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 979 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/979), portal name cpc_1909-09-10_DE_Dortmund_DE_Hier_fritzlehmann-08, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Fritz Lehmann, with no transcription or solution attached. The portal links the HistoCrypt article on the collection as its reference.

The address side carries a Germania 5-pfennig stamp of the Deutsches Reich, still affixed, cancelled **FREIBURG (SCHLESIEN) 10.9.09 1-2N** (10 September 1909). The "Dortmund" in the portal file name is not what the postmark shows. The address is written in plain Kurrent pencil, "Herrn Fritz Lehmann, Hier" ("Mr Fritz Lehmann, here", i.e. local post), followed by a street line and a house number that are partly covered by the collection's watermark stamp and are left unread. The message itself is a ten-line block of dotted numbers in pencil, written sideways on the left half of the address side.

The picture side is a printed photographic card, "Gretchen", with the caption "Wie sollte mir die Kette stehen?" (Goethe's Faust; publisher number 4034-2). It belongs to the same series as HCP 1045 (4034-6), another card to Fritz Lehmann. The picture side has no handwriting.

![Address side: the number block on the left, plain address on the right, FREIBURG (SCHLESIEN) postmark on the stamp (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Gretchen, "Wie sollte mir die Kette stehen?" (source/picture-large.jpg)](../source/picture-large.jpg)

The card is one of a group of cipher postcards to Fritz Lehmann in this collection. The sister cards HCP 1134 (also Freiburg in Schlesien, signed Susi), 1113 and 1050 are finished in this repository, and HCP 1045 (same Gretchen series, October 1909, signed Susi) was accepted in review. They all use the same number key. This card is unsigned, so "Susi" as its writer is only a likely attribution.

## Method

The solver (Claude Opus 5.5) worked from the high-resolution original of the address scan (work/hires/), turned the block upright and read all ten rows number by number from 3–5× enlargements. No OCR was used. The key was **transferred** from the Lehmann sister cards, not recovered anew, and was then checked against every number on this card: all 114 numbers fall inside the table and give connected German with no leftover sign. One script (work/decode.py) checks the SHA-256 of the scans and decodes the transcription:

```text
python3 -I ciphers/hcp-979/work/decode.py
```

The reviewer (a separate Claude Opus 5.5 agent) cropped and rotated the block itself (below), read all ten rows independently and decoded them with its own parser. Its reading agrees number for number with the solver's.

![The number block turned upright (reviewer's crop, review/work/block_rot.png)](../review/work/block_rot.png)

## Key

Number substitution (monoalphabetic), German. The 25-letter alphabet without J is numbered from 2:

| Letter | A | B | C | D | E | F | G | H | I | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Number | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| Letter | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Number | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

Dots separate the numbers of a word, dashes separate words. A dark cross or slash drawn over the first number of a word (12 of Lieber, 7 of Fritz and Fieber, 9 of Heut twice, 2 of Abend, 19 of Sollte) marks a capital letter, as on the sister cards; it does not change the letter. The sharp s is written SZ. The closing "½ VIII" (a fraction I over II, then the Roman numeral VIII with an overbar) is written in plain, not enciphered. Numbers used on this card: 2–12, 14, 15, 18, 19, 20, 21, 23, 26.

## Plaintext

Transcription, row by row (x = capital stroke):

```text
12x.10.6.3.6.18 - 7x.18.10.20.26 - !
9x.6.21.20 - 8.6.9.20 - 6.19 -
23.10.6.5.6.18 - 3.6.19.19.6.18
23.6.10.19.26 - 2.3.6.18 14.15.4.9 -
14.10.4.9.20 - 23.10.6 - 6.19 - 9x.6.21.20 -
2x.3.6.14.5 - 19.6.10.14 - 23.10.18.5 -
8.6.19.20.6.18.14 - 9.2.20.20.6 -
10.4.9 - 19.20.2.18.11.6 -
7x.10.6.3.6.18 - 19x.15.12.12.20.6 -
10.4.9 - 14.10.4.9.20 - [1/2 VIII]
```

Decoded, line for line:

```text
LIEBER FRITZ !
HEUT GEHT ES
WIEDER BESSER
WEISZ ABER NOCH
NICHT WIE ES HEUT
ABEND SEIN WIRD
GESTERN HATTE
ICH STARKE
FIEBER SOLLTE
ICH NICHT 1/2 VIII
```

German, with normalised spelling and punctuation (the punctuation is ours):

**"Lieber Fritz! Heut geht es wieder besser, weiß aber noch nicht, wie es heut Abend sein wird. Gestern hatte ich starke Fieber. Sollte ich nicht ½ 8 ..."**

The writer's own forms are kept: Heut (for heute), starke Fieber (standard: starkes Fieber), WEISZ for weiß.

English: "Dear Fritz! Today it is going better again, but I don't know yet how it will be this evening. Yesterday I had a high fever. Should I not ... half past seven ..."

Slovak: "Milý Fritz! Dnes je to už zase lepšie, ale ešte neviem, ako to bude dnes večer. Včera som mal(a) vysokú horúčku. Keby som ... nie o pol ôsmej ..."

The last clause is elliptical: every sign is read, but no verb follows. Two readings fit, and neither is on the card: "Should I not [be there] at half past seven, [that is why]" (an excuse in advance for missing an evening meeting), or more plainly "Should I not [come] at half past seven?". "½ VIII" is German "halb acht" = 7.30.

## Uncertainties

1. The ending "SOLLTE ICH NICHT ½ VIII" lacks a verb; the completions above are interpretation. There is no signature.
2. End of row 5: the last digit of the second HEUT (9.6.21.20) runs into the printed blue "Briefkaart" line. The 2 of 20 is visible; the 0 is largely covered by the print. 20 = T is restored by word sense (HEUT) and by the same word in row 2.
3. 5 versus 8 in this hand: 5 (D of WIEDER, ABEND, WIRD) is an open S-shape with a detached top flag; 8 (G of GEHT, GESTERN) has a closed lower loop. The two are distinct on the pixels; word sense agrees (DEHT, DESTERN would not be words).
4. 18 versus 19: the first numbers of STARKE and SOLLTE have the 9-form (closed top loop, straight tail), unlike the S-shaped 8 of 18 = R in the same word. Pixel reading, supported by word sense (RTARKE, ROLLTE would not be words).
5. The separator after FIEBER is a small "+" (a dash with a cross stroke); it is taken as a word separator.
6. The plain address: the street line and house number are partly covered by the collection stamp and are left unread. They are not part of the message.
7. The stamp is still affixed and postmarked over both stamp and card, and no pencil shows at its edges; anything under it cannot be checked from the scans. No steganographic text was found elsewhere on either side.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-ran the decoding command, decoded the transcription with its own script, read all ten rows from its own crops of the high-resolution scan, and checked the key against the sister cards. Verdict: **ACCEPT**, with four minor findings:

1. The partly hidden 0 at the end of row 5 was not listed as a word-sense restoration. Now listed (uncertainty 2).
2. The completion of the elliptical ending must stay marked as interpretation, and the plainer alternative should be given. Both readings are now given and marked.
3. The sister cards were called "finished" and the key "already proven" while some were only accepted in review. The wording was corrected.
4. A guessed street name in the address was withdrawn; the street line is now reported as unread.

None of these changed a decoded letter. Following a remark from the human team about hidden messages under stamps on another card series, the stamp box and the picture side were checked again; nothing was found, so the cipher type stays MASC.
