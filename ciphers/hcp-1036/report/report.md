# HCP 1036 (cpc_1906-08-13_DE_Stolp_DE_Koslin_): a number-cipher greeting from Nassow, Pomerania, 1906

Human solver: Tomáš Pavuk

**Status: deciphered in full (44 of 44 numbers); independent review 1 verdict ACCEPT, no change to the decoded text.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1036 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1036), portal name cpc_1906-08-13_DE_Stolp_DE_Koslin_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Fräulein Anna Schulz, with no transcription or solution attached. The portal links the HistoCrypt article on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). No published solution of this card was found.

It is a German picture postcard (Verlag L. Brühl, Berlin SW, Dess. No. 217) with the printed caption "Wie gerne dir zu Füssen." ("How gladly at your feet."). The address side is written in plain Kurrent script: "Fräulein Anna Schulz, Köslin, Gärtnerstraße 5". The 5-pfennig Germania stamp is cancelled by a partly covered railway postmark reading "STOLP ... BAHN ... ZUG ... 12 8" (Stolp railway post, 12 August), and an arrival stamp of Cöslin reads 13.8.06, which gives the year 1906. Stolp and Köslin (today Słupsk and Koszalin, Poland) are towns in Prussian Pomerania.

The message is written in pencil on the picture side, turned sideways, as dotted numbers; its first line fills the printed "Gruss aus ......" ("Greetings from ......") line.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side (source/address-large.jpg)](../source/address-large.jpg)

![The pencil number block turned upright, from the high-resolution scan (work/crops/text_rot.png)](../work/crops/text_rot.png)

## Method

The transcription is manual: the number block was cropped from the un-converted high-resolution scan, rotated upright and enlarged 3 to 4 times, and every number was read by eye. The writer puts a full stop after every number and leaves wider gaps between words. The 44 numbers range from 1 to 25, which at once suggests a letter-position cipher. A plain A=1 ... Z=26 alphabet gives nonsense ("MARRNV / HEQYKICHEM ..."), while the 25-letter German alphabet without J (I and J counted as one letter, as was usual at the time) gives fluent German at every word. The only signs that needed care were the 9 and 19 (closed looped top; the 4s on this card are written open-topped) and the 12 of the surname (flat base stroke of the 2); all three are read on the pixels and confirmed by the words.

The reviewer cropped and enlarged the block independently, read all 44 numbers before comparing (identical, including word gaps), and decoded them with its own script under both alphabets.

## Key

Number substitution (monoalphabetic, MASC): each letter is written as its position in the alphabet without J.

| A | B | C | D | E | F | G | H | I | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

Numbers used on the card: 1 3 4 5 6 7 8 9 10 11 12 13 14 17 18 19 20 22 25.

## Ciphertext

```text
Gruss aus 13.1.18.18.14.22.
8.5.17.25.11.9.3.8.5.13.  7.17.20.18.25.
18.5.13.4.5.19.  9.8.13.5.13.
6.17.9.4.1  12.9.18.3.8.10.5.
```

## Plaintext and translation

```text
Gruss aus NASSOW
HERZLICHEN GRUSZ
SENDET IHNEN
FRIDA MISCHKE
```

German, normalised: "Gruss aus Nassow. Herzlichen Gruß sendet Ihnen Frida Mischke." (GRUSZ is the period's sz spelling of ß.)

English: "Greetings from Nassow. Frida Mischke sends you warm greetings."

Slovak: "Pozdrav z Nassowa. Srdečný pozdrav Vám posiela Frida Mischke."

Nassow is a village in Kreis Köslin, Pomerania (today Nosowo, Poland), which fits the Stolp railway postmark and the Köslin address. The formal "Ihnen" suits a card to "Fräulein" Anna Schulz.

The full plaintext is reproduced from the transcription and the key by one command, run from the repository root: python3 -I ciphers/hcp-1036/work/decode.py

## Uncertainties

- None in the ciphertext: all 44 numbers are read on the pixels and decode with no number left over.
- The surname Mischke and the street name Gärtnerstraße (a Kurrent reading of the plain address) cannot be checked against outside records; neither affects the decryption.
- Steganography: the stamp box and both sides were inspected by solver and reviewer, and no hidden or extra writing is visible. Anything written under the stamp cannot be seen in the scans and is not claimed either way.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-ran the reproduction command, made its own crops, read all 44 numbers independently (identical to the solver's), decoded them with its own script, confirmed that the J-less alphabet is required by the text, checked the place name against the postmarks, and inspected the stamp box. Verdict: **ACCEPT**, with three minor findings:

1. The transcription file dropped the full stops written after each word's last number. A note stating this was added to the transcription; the decoding is unchanged.
2. The register type should be MASC; no hidden message is visible, so "MASC + Steganography" is not claimed.
3. The year of posting comes from the Cöslin arrival stamp, since the Stolp railway postmark shows only "12 8"; this is now stated explicitly.

The decoded text and the key did not change.

## Credits

Transcription, decipherment and this report by Claude Opus 5.5 (Anthropic); independent review by a separate Claude Opus 5.5 agent. There was no earlier AI work on this card. Images: HC Portal, T. Schrödel Collection.
