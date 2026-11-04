# HCP 1047: a number-cipher love note from Susi to Fritz Lehmann (Freiburg in Schlesien, 1909)

Human solver: Tomáš Pavuk

**Status: deciphered in full (79 of 79 cipher numbers); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1047 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1047), portal name cpc_1909-07-24_DE_Freiburg-(Schlesien)_DE_Hier_fritzlehmann-05, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Fritz Lehmann, with no transcription or solution attached.

The picture side is a printed photographic card "Der Herzenschmied" (publisher's mark B.N.K., number 3278/7): a young smith holding hands with a girl over an anvil, with a printed four-line verse. It carries no handwriting.

The address side is written in plain German Kurrent: **An Herrn Fritz Lehmann, Hier, Alte Bahnhofstr. No 29** (the street name is read loosely and is not part of the cipher). "Hier" means the card was posted for local delivery. The Germania 5-pfennig stamp is cancelled **FREIBURG (SCHLESIEN) 24.7.09**, i.e. Freiburg in Silesia (today Świebodzice, Poland), 24 July 1909. The message itself is a block of nine lines of numbers written sideways on the left half of the address side.

The card belongs to a series of cipher cards to Fritz Lehmann in this collection. Two of them, HCP 1113 (Freiburg, 30 July 1909, six days later) and HCP 1134 (Schweidnitz, 1910), are signed "Susi", are in the same hand and the same number style, and were deciphered earlier in this repository with the same key.

![Address side: the sideways number block on the left, the plain address and the FREIBURG (SCHLESIEN) postmark on the right (review/work/adr_overview.png)](../review/work/adr_overview.png)

![Picture side: printed card "Der Herzenschmied", no handwriting (review/work/pic.png)](../review/work/pic.png)

## Method

The solver (Claude Opus 5.5) rotated the high-resolution original of the address scan 90° clockwise and read all nine lines number by number from enlarged crops (work/crops/). No OCR was used and the portal supplied no transcription. The transcription is in work/transcription.txt.

The key of the sister cards HCP 1113 and HCP 1134 (a shifted alphabet starting at A=2, without J) was then tested on this card rather than assumed. It turns every number into a letter of connected German; no number falls outside the table and none is left over.

![The number block turned upright (work/crops/rot.png)](../work/crops/rot.png)

In review a separate Claude Opus 5.5 agent rotated the scan itself, read the whole block independently, decoded its own transcription with its own script (review/work/my_decode.py) and obtained the same text, number for number.

## Key

Number substitution (monoalphabetic), 25-letter alphabet without J:

| Number | Letter | Number | Letter | Number | Letter | Number | Letter | Number | Letter |
|---|---|---|---|---|---|---|---|---|---|
| 2 | A | 7 | F | 12 | L | 17 | Q | 22 | V |
| 3 | B | 8 | G | 13 | M | 18 | R | 23 | W |
| 4 | C | 9 | H | 14 | N | 19 | S | 24 | X |
| 5 | D | 10 | I | 15 | O | 20 | T | 25 | Y |
| 6 | E | 11 | K | 16 | P | 21 | U | 26 | Z |

Conventions of the writer: dots separate the numbers of a word, dashes separate words, a double tick over a number marks an umlaut (21 with ticks = Ü), a bar over a number doubles the letter (13 with bar = MM), and "+" stands for a comma. Z stands for ß (GRÜSZT, KÜSZT). Twenty distinct numbers occur on this card: 2–15, 18–21, 23 and 26.

## Plaintext

Ciphertext as transcribed, one card line per row (" = umlaut ticks, = = doubling bar):

```text
12.10.6.3.6.19 - 12 - 19.2.20.26.4.9.6.14 -
19.15.12.12.20.6 - 6.19 - 19.4.9.12.10.13=.6.18
8.6.23.15.18.5.6.14 - 19.6.10.14 + 23.2.19
10.4.9 - 14.10.4.9.20 - 9.15.7.7.6 -
19.15 - 8.6.9.6 - 23.10.6.5.6.18 -
26.21.13 2.18.26.20 +
6.19 - 8.18.21".19.26.20 - 21.14.5 -
11.21".19.26.20 - 5.10.4.9 -
5.6.14.6 19.21.19.10 -
```

Decoded, as written:

```text
LIEBES L SATZCHEN
SOLLTE ES SCHLIMMER
GEWORDEN SEIN, WAS
ICH NICHT HOFFE
SO GEHE WIEDER
ZUM ARZT,
ES GRÜSZT UND
KÜSZT DICH
DENE SUSI
```

Normalised German: **"Liebes [L.] Schätzchen! Sollte es schlimmer geworden sein, was ich nicht hoffe, so gehe wieder zum Arzt. Es grüßt und küßt dich deine Susi."**

English translation: **"Dear [L.] sweetheart! Should it have got worse, which I hope it has not, then go to the doctor again. Greetings and kisses, your Susi."**

Slovak translation: **"Milý [L.] poklad! Ak by sa to zhoršilo, v čo nedúfam, tak choď znova k lekárovi. Pozdravuje a bozkáva ťa tvoja Susi."**

The note is a short, caring message to someone who is ill or injured; a visit to the doctor is also mentioned on the Lehmann card HCP 1060.

## Uncertainties

- **The lone "12" (L)** standing between two dashes after LIEBES. Its purpose is unknown (an initial, perhaps of Lehmann, or an abandoned start). It is reported literally and is the only unexplained sign.
- **SATZCHEN.** The writer left out the CH of Schätzchen and wrote no umlaut over the A. "Schätzchen" is word sense; the sister card HCP 1134 has the full form.
- **DENE.** The I of "deine" is missing; the scan clearly shows four numbers. Normalised by word sense.
- **WAS (line 3).** The last number is read 19 (S). Its second digit has a closed top loop like this writer's 9 but also a base stroke like his 2, so the choice of 19 over 12 (which would give WAL) rests on word sense.
- **HOFFE (line 4).** The first 9 has a tall loop reaching above the line, as if written over a 1.
- **Capital marks.** The first number of Liebes, Schätzchen, Sollte, Arzt and Susi is crossed or overwritten with a dark lead-in stroke. These are exactly the words capitalised in German, so the strokes are read as the writer's capital mark, not as deletions. The only real deletion is a blotted "26" at the end of line 5, rewritten as the first number of line 6.
- **Small tick after 5.** The flourish after several 5s is the writer's normal 5, not an umlaut.
- **Hidden writing.** The stamp is still affixed and only the scan is available, so what lies beneath it cannot be inspected. No ink is visible at its edges or at its creased corner. The picture side carries only print; the dark marks on the man's shoulder and sleeve are spots and damage to the photographic surface, not writing. No steganographic part was found.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1047/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of both source scans and of the high-resolution address scan, decodes the manual transcription in work/transcription.txt with the key above, and prints the nine decoded lines. The transcription step itself is manual and was confirmed independently in review.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), read the whole block itself and decoded it with its own script (identical result), checked that the key covers every number, checked the doubtful signs on enlargements, inspected the stamp, the picture side and the edges for hidden writing (none found), and confirmed that no published solution was used. Its three minor findings and what changed:

- **WAS vs WAL.** The solution had said that 12 was excluded on the pixels; it now says that 19 rests on word sense, because the digit is a hybrid of 9 and 2. The reading is unchanged.
- **Capital marks.** The reviewer noticed that the crossed first numbers fall on exactly the capitalised German words; this is adopted above and supports reading them as digits, not deletions.
- **Register type.** MASC (number substitution); no steganographic part, so not "MASC + Steganography". The solver rechecked the stamp and the picture side on the high-resolution scans and agrees.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1047, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1047 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3201/ (source/picture-large.jpg; original in work/hires/).
- Address side: https://api.hcportal.eu/media/3202/ (source/address-large.jpg; original in work/hires/).
- Sister cards in this repository with the same key and signature: ciphers/hcp-1113, ciphers/hcp-1134.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.
