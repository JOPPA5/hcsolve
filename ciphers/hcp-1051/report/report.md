# HCP 1051: a number-cipher postcard from Minna to Fritz Lehmann, Schweidnitz 1910

Human solver: Tomáš Pavuk

**Status: deciphered in full (83 of 83 numbers); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1051 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1051), portal name cpc_1910-03-31_DE_Schweidnitz_DE_Schweidnitz_fritzlehmann-12, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Fritz Lehmann, with no transcription or solution attached.

The address side carries a German 5-pfennig Germania stamp cancelled SCHWEIDNITZ 31.3.10 (Schweidnitz in Silesia, today Świdnica, Poland). It is addressed in plain Kurrent script to "Herrn Fritz Lehmann, Schweidnitz", with a street that reads roughly "..ögen str. No 6" (the capital is L or B; the name is not certain). A plain heading reads "Schweidnitz d. 31/3 10". The message itself is a block of nine pencil lines of numbers on the left half of the address side.

The picture side is a printed, hand-tinted photo card with the song lines "Kommt ein Vogel geflogen!" and "Und der Sommer ist kommen und mein Schätzchen ist weit." (publisher B.N.K., no. 33090/4). It has no handwriting.

![Address side: number block on the left, address to Fritz Lehmann on the right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: printed love card, no handwriting (source/picture-large.jpg)](../source/picture-large.jpg)

The card belongs to a group of cipher postcards to Fritz Lehmann in Schweidnitz in the Schrödel collection. Two of them, HCP 1113 and HCP 1134, were deciphered earlier in this repository with the same number key; they are signed "Susi". This card is signed "Minna". Whether Susi and Minna are the same person is not established, and this report does not assume it.

## Method

The transcription is manual, by Claude Opus 5.5, from the high-resolution original scan (the portal supplied none). Each of the nine lines was read from enlarged crops; doubtful digits were checked at 30–60x zoom. The writer separates numbers with dots and words mostly with dashes; in two places (RECHT IST, HERZ LIEN) a word break is written only with a dot.

The key was taken from the Lehmann sister cards HCP 1113 and HCP 1134 and tested on this card: it decodes every number into connected German without any leftover or unknown sign. This is a known, transferred key, not a new key recovery. A web search found no published solution of this card.

In review a separate Claude Opus 5.5 agent transcribed the block on its own from the same scan, got a number-for-number identical transcription, and decoded it with its own script to the same letters.

## Key

Simple substitution with numbers: the 25-letter alphabet without J, numbered from 2.

| A | B | C | D | E | F | G | H | I | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |

| O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

Numbers used on this card: 2–15, 18, 19, 20, 21, 23 and 26.

## Ciphertext

```text
12.10.6.3.6.18 - 7.18.10.20.26 -
10.4.9 - 11.15.13.13.6 - 9.6.21.20 -
23.10.6.5.6.18 - 6.10.14
3.10.19.4.9.6.14 - 26.26
5.10.18 - 23.6.14 - 6.19 -
18.6.4.9.20 . 10.19.20 -
9.6.18.26 . 12.10.6.14 -
8.18.21.19 - 21 - 11.21.19
5.6.10.14.6 - 13.10.14.14.2 -
```

## Plaintext

Literal decoding, line for line:

```text
LIEBER FRITZ
ICH KOMME HEUT
WIEDER EIN
BISCHEN ZZ
DIR WEN ES
RECHT IST
HERZ LIEN
GRUS U KUS
DEINE MINNA
```

Normalised German: "Lieber Fritz! Ich komme heut wieder ein bisschen zu dir, wenn es recht ist, Herzlein. Gruß u. Kuss, deine Minna."

English: "Dear Fritz! I am coming to you again for a little while today, if that is all right, sweetheart. Greetings and a kiss, your Minna."

Slovak: "Milý Fritz! Dnes zase na chvíľku prídem k tebe, ak ti to vyhovuje, srdiečko. Pozdrav a bozk, tvoja Minna."

The spellings BISCHEN, WEN, GRUS, KUS and HEUT are the writer's own (for bisschen, wenn, Gruß, Kuss, heute), typical of informal writing of the time; they are not reading errors.

## Uncertainties

- Line 4, "26.26": both groups are clearly 26, which gives ZZ. "zu dir" needs 26.21; the reading ZU is word sense (a writer slip).

![Line 4, the two 26 groups (work/crops/zu.png)](../work/crops/zu.png)

- Line 7, "9.6.18.26 . 12.10.6.14" gives HERZ LIEN. It is read as "Herzlein" (sweetheart) with I and E swapped; the letters LEIN rest on word sense.
- Line 2, last group of HEUT: the 2 is clear, the second digit is crossed by the printed divider line of the card; what is visible fits 0, so 20 = T. This is a restoration by word sense.

![Line 2, HEUT, last group under the printed divider (work/crops/heut.png)](../work/crops/heut.png)

- Line 1, FRITZ: the third group is 10 (I), an open 0 loop without a crossing stroke, clearly different from the crossed 8 of the 18 before it. This call rests on the pixels.
- The street name in the address and the identity of Minna are unknown. The heading's month digit looks like 8, but the postmark and file name give 31 March 1910.
- Steganography: the stamp is still on the card, so anything written under it cannot be seen on these scans; no ink shows at its edges. The picture side has only printed text. No hidden message was found, so the cipher type is given as plain MASC.

## Review and what changed

The review (verdict **ACCEPT**) re-ran the reproduction command, transcribed the card independently with an identical result, decoded it with its own script, checked the doubtful digits on the pixels and confirmed that the plaintext is natural German of 1910. It raised four minor points:

1. The handover gave a wrong number count (55); it is now corrected to 83 numbers.
2. The 10 in FRITZ was not listed among the sign checks; it is now listed, with the evidence from the zoomed crop.
3. The street name was read only loosely; it was re-read as "..ögen str. No 6" and remains marked uncertain (it is outside the cipher).
4. The signature Minna must not be merged with the Susi of the sister cards; this report keeps them apart.

No decoded letter changed.

## Reproduction

From the repository root: `python3 -I ciphers/hcp-1051/work/decode.py` checks the SHA-256 of the source scans and decodes work/transcription.txt with the key above.
