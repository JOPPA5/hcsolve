# HCP 913: an invitation to the cherry picking, from Emma to Fritz Lehmann

Human solver: Tomáš Pavuk

**Status: deciphered in full (all numbers of the 18-line block decoded); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 913 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/913), portal name cpc_-03-26_DE_Reichen-(Schlesien)_DE_Schneidwitz_fritzlehmann-18, from Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Fritz Lehmann, with no transcription or solution attached.

The picture side is a printed colour view "Reichenbach i. Schl. – Blick von der Promenade auf das Eulengebirge" (Verlag Rud. Hoefer's Buchhandlung, Reichenbach i. Schl., no. 18802). It carries no handwriting.

The address side is addressed in plain German script to **Herrn Fritz Lehmann, Schweidnitz** (today Świdnica, Poland); the street is hard to read (perhaps "Bögenstraße No. 6") and is not part of the cipher. It has a German 5-pfennig Germania stamp, stuck on at a slant and still affixed, and two postmarks REICHENBACH (SCHLES.) (today Dzierżoniów). The day 26 is clear, the month most likely 6, the year illegible; the portal file name gives "-03-26" instead. The message is an 18-line block of numbers in ink, written upside down relative to the address on the left half of the address side.

The card belongs to a family of number-cipher postcards to Fritz Lehmann in the Schrödel collection. Four of them (HCP 1044, 1045, 1113 and 1134) had already been deciphered and closed in this repository with the same key; it was transferred here unchanged and tested on every number of this card.

![Picture side: Reichenbach in Silesia with the Owl Mountains (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: the address to Fritz Lehmann, Schweidnitz, the slanted stamp and the REICHENBACH postmarks; the number block is on the left half, upside down (source/address-large.jpg)](../source/address-large.jpg)

![The number block turned 180 degrees, from the high-resolution scan (work/crops/block_rot.png)](../work/crops/block_rot.png)

## Method

The transcription is manual, made from the un-converted high-resolution scan of the address side (work/hires/), turned 180 degrees and read line by line on enlarged crops (work/crops/). No OCR was used. Numbers are separated by dots, words by dashes, and a plain cross "+" ends two sentences. The doubtful spots (a struck-out number in line 1, ink blots in line 9, an overwritten digit in line 15, and the slips described below) were enlarged 3–5 times before a reading was fixed.

The Lehmann family key decodes every number of the card into continuous German. The reviewer cut its own full-resolution strips, re-read all 18 lines against the transcription, and decoded them with a separately written script; the result was identical.

## Key

Number substitution (monoalphabetic): the 25-letter alphabet without J, numbered from 2.

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |

ß is written SZ; umlauts are not encoded (one umlaut is shown by two ticks, see GRÜSZE below). Numbers occurring on this card: 2–16, 18–23 and 26. This writer's 5 has a small looped flag on top; it is the normal digit 5 (it occurs in DIE, DOCH and KOMME alike).

## Ciphertext

As transcribed (card turned 180 degrees; "[struck 26]" is a crossed-out number with the correcting 7 written above it):

```text
12.10.3.6.18 - [struck 26] 7.18.10.20.26 +
3.10.20.20.6 - 19.6.10 - 5.15.4.9 - 21.15 -
8.15.20 - 21.14.5 - 11.15.13.13.6 -
19.15.14.14.20.2.8 - 13.10.20 - 10.14 -
5.10.6 - 11.10.18.19.4.9.6.14 - 14.2.4.9
9.15.9.6.14.16.15.19.6.18.10.20.26 +
3.10.20.20.6 - 19.4.9.18.6.10.3.6 -
13.10.18 - 15.3 - 5.15 - 11.15.13.13
6.14 - 11.15.13.13.19.20 - 23.21.18.5.6
13.10.4.9 - 19.6.9.18 - 7.18.6.21.6.14 -
5.10.4.9 - 23.10.6.5.6.18 - 26.21 -
19.6.9.6.14 - 21.13 - 23.6.12.4.9.6 -
26.6.10.20 - 10.4.9 - 7.2.9.18.6 - 23.6.10
19.20 - 10.4.9 - 14.15.4.9 - 14.10.4.9.20
23.6.14.14.19 - 8.6.9.20 - 3.10.20.20.6
11.15.13.13.6 5.15.4.9 -
22.10.6.12.6 - 8.13.10".19.26.6 - 22.15.14 -
5.6.10.14.14.6.18 - 6.13.13.2
```

## Plaintext

Literal decode, line by line (the cross "+" is rendered "!"):

```text
LIBER FRITZ !
BITTE SEI DOCH UO
GOT UND KOMME
SONNTAG MIT IN
DIE KIRSCHEN NACH
HOHENPOSERITZ !
BITTE SCHREIBE
MIR OB DO KOMM
EN KOMMST WURDE
MICH SEHR FREUEN
DICH WIEDER ZU
SEHEN UM WELCHE
ZEIT ICH FAHRE WEI
ST ICH NOCH NICHT
WENNS GEHT BITTE
KOMME DOCH
VIELE GMI"SZE VON
DEINNER EMMA
```

Normalised German (the writer's slips corrected, see Uncertainties):

**Lieber Fritz! Bitte sei doch so gut und komme Sonntag mit in die Kirschen nach Hohenposeritz! Bitte schreibe mir, ob du kommen kannst. Würde mich sehr freuen, dich wieder zu sehen. Um welche Zeit ich fahre, weiß ich noch nicht. Wenn's geht, bitte komme doch. Viele Grüße von deiner Emma.**

English translation: **Dear Fritz! Please be so kind as to come along on Sunday to the cherries [cherry picking] in Hohenposeritz! Please write and tell me whether you can come. I would be very glad to see you again. I don't know yet what time I am leaving. If it is possible, please do come. Many greetings from your Emma.**

Slovak translation: **Milý Fritz! Buď taký dobrý a príď v nedeľu so mnou na čerešne do Hohenposeritzu! Prosím, napíš mi, či môžeš prísť. Veľmi by ma potešilo opäť ťa vidieť. O koľkej pôjdem, ešte neviem. Ak sa dá, príď, prosím. Veľa pozdravov od tvojej Emmy.**

Hohenposeritz (today Pożarzysko, Świdnica County, Poland) is a village near Schweidnitz, north-east of the town; a Sunday outing there for the cherry harvest fits the Silesian setting of the postmark and the address, and a June date.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-913/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of both portal scans and both high-resolution originals, decodes the manual transcription in work/transcription.txt with the key above, and prints the 18 literal lines and the list of numbers used. The transcription step itself is manual; it was confirmed independently in review.

## Uncertainties

- **Writer's slips, kept literally.** "UO GOT" (21.15 – 8.15.20) where the set phrase demands "so gut"; "DO" (5.15) for "du"; "GMI"SZE" (8.13.10".19.26.6) for "Grüße", the largest slip, where the two ticks show the writer meant an umlaut vowel. All these numbers are clearly written on the scan; the corrected words rest on word sense.
- **Spelling as written:** LIBER (lieber), DEINNER (deiner), WEIST (weißt, used for "weiß"), WURDE (no umlaut for "würde"), and "ob du kommen kommst", a doubled verb evidently meant as "kommen kannst".
- **Damaged numbers.** In line 1 a struck-out number (probably 26) precedes FRITZ, with the correcting 7 written above; it is not decoded. In line 9 the 2 of 21 (WURDE) and a 13 of KOMMST are ink-blotted but readable. In line 15 the second 14 of WENNS is overwritten; reading it as 14 partly rests on word sense. In line 4 a 14 of SONNTAG lies under a brown stain but is legible.
- **The cross.** "+" is a sentence-end cross written in plain on the card; rendering it as "!" is editorial, and it is not an enciphered sign.
- **Under the stamp.** The stamp is still affixed (at a slant); nothing is visible around or through it, but writing under it cannot be ruled out. No other writing was found on either side.
- **Date.** Day 26 is clear, the month is probably 6 (the portal file name says 03), and the year is illegible. The Germania stamp and the postmark type point to the early 20th century, before 1920.
- **People.** The sender signs only "Emma"; her identity is unknown.
- **Key provenance.** The key was transferred from the Lehmann sister cards, not recovered blind from this card; it decodes every number here without change.
- No web search for a published solution of this card was made; the portal shows Not solved and the AI Decipherment Register had no record for it on 2026-11-03.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (all hash checks OK, output identical to the literal plaintext), decoded the transcription with its own script, cut its own strips of the high-resolution scan and re-read all 18 lines without finding a discrepancy, and confirmed every disclosed slip on 3x enlargements. It found no handwriting on the picture side. Its four findings were minor and are reflected here:

- **Hohenposeritz.** The location was first given as "between Reichenbach and Schweidnitz"; it is now given as a village near Schweidnitz, north-east of the town.
- **Date.** Kept uncertain, with the disagreement between the postmark month and the portal file name stated once.
- **Sister cards.** These were reviewed and accepted at the time of the review and are now closed; they are described accordingly.
- **The "+" marks.** Stated to be plain sentence-end crosses, not cipher.

After the review the stamp area was checked once more for steganographic writing, following a remark from a collaborator that such writing is common under the stamps of another postcard series; nothing was found on this card, so the type remains MASC. No decoded letter changed as a result of the review. Transcription, key transfer and decipherment were done by Claude Opus 5.5; there was no earlier work in this directory.

## Sources

- HC Portal record 913, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/913 (source/metadata.md). The portal links the HistoCrypt paper on the Schrödel collection: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- Portal scans of both sides (source/picture-large.jpg, source/address-large.jpg) and the un-converted high-resolution originals (work/hires/); see SOURCES.md.
- Family key: the Lehmann sister cards in this repository, ciphers/hcp-1044, 1045, 1113 and 1134.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03.
