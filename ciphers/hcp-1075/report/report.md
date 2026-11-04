# HCP 1075 (cpc_--_USA__USA__): an American Morse postcard from Akron, Ohio, to Ezra W. Sipple

Human solver: Tomáš Pavuk

**Status: deciphered in full (64 of 64 Morse signs, 17 words); independent review 1 verdict ACCEPT, no change to the decoded text.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1075 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1075), portal name cpc_--_USA__USA__, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient "Mr. Ezra W.", with no transcription or solution attached. The portal links Schrödel's paper "Cryptographic postcards" (HistoCrypt 2021).

The card is a Raphael Tuck & Sons "Raphotype" postcard No. 5369, "Akron, Ohio. City Hospital." The hospital building shown was completed in July 1902, so the card dates from the first decade of the 20th century (roughly 1903–1910). It carries no stamp and no postmark, so it was probably sent in an envelope or delivered by hand. The stamp box holds only the printed Tuck trademark.

- **Address side, plain:** "Mr Ezra W Sipple / Meyersdale / Penna" (Meyersdale, Somerset County, Pennsylvania).
- **Address side, cipher:** eight rows of dots and dashes, with commas between words, on the left half and along the bottom. The last row (OHIO) runs under the grey HCPORTAL / Schrödel collector stamp.
- **Picture side, plain (not enciphered):** "No 547 Carroll St / akron ohio" at the left; "I have not forgot the code but do Not remember the Noo on the Bx card" in two lines along the caption strip; "547 Carroll St" written diagonally in the bottom-right corner; and the initials "J. N. S." as a signature.

![Address side: plain address to Ezra W. Sipple, Meyersdale, Penna, and the eight Morse rows (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Akron City Hospital, with the plain note along the caption strip and in the corner (source/picture-large.jpg)](../source/picture-large.jpg)

The plain note itself ("I have not forgot the code") says that the two correspondents shared a code. In the United States around 1900 the obvious shared code was the American (railroad or landline) Morse code used by telegraph operators.

## Method

The transcription is **manual**. The solver (Claude Opus 5.5) read every mark of the eight rows from 3–5x enlargements of the un-converted high-resolution scan of the address side (work/hires/). It recorded each letter as its pattern of dots (.), dashes (-), long dashes (=) and internal gaps, and the commas as word dividers (work/transcript.json, 17 words, 64 signs). Mark lengths and gaps were measured on the enlargements (helper script work/measure_marks.py). The writer's own I (tight pair) and O (wide pair), T (short dash) and L (long dash) elsewhere on the card were the reference for the doubtful signs.

International Morse does not read the text. The spaced-dot letters (C = `.. .`, O = `. .`, R = `. ..`, Y = `.. ..`) and the long-dash L exist only in American Morse, and so do the numerals 5 = `---` and 7 = `--..` (in International Morse they would be O and Z). American Morse reads every sign into plain English, with no unused or unmapped symbol. The same system was found on the finished sister card HCP 1453 (Washington, 1906), and its key agrees with this card for all shared letters.

Under the collector stamp, the ink dots were told apart from the stamp lettering by darkness. The ten dots of OHIO (2 + 4 + 2 + 2) are far darker (grey value about 60–130) than the stamp letters (about 150–157), and they lie on the sloping line of the row.

No hidden writing was found. The stamp box, the edges and the picture side were inspected, and the picture-side note is ordinary open writing, not steganography.

## Key

American (landline) Morse, a fixed letter-for-symbol substitution (register label MASC/Morse). Only the signs that occur on this card are listed. A space inside a sign is an internal gap within the letter.

| Letter | Sign | Letter | Sign | Letter | Sign |
|---|---|---|---|---|---|
| A | `.-` | I | `..` | S | `...` |
| C | `.. .` | K | `-.-` | T | `-` |
| D | `-..` | L | `=` (long dash) | U | `..-` |
| E | `.` | M | `--` | W | `.--` |
| H | `....` | N | `-.` | Y | `.. ..` |
| O | `. .` | R | `. ..` | 4 | `....-` |
| 5 | `---` | 7 | `--..` | | |

## Transcription

Rows as on the card. A trailing `*` marks a sign whose reading rests partly on word sense. `[^-..]` is a letter the writer added above the line with a caret.

```text
1  . ..  .  .. .  -.. ,  .. ..  . .               R E C D , Y O
2  ..-  . .. ,  .. .  .-  . ..  -.. ,             U R , C A R D ,
3  -  ....  ..  ... ,  .-  -- ,                   T H I S , A M ,
4  . .*  .--  ..  =*  =* ,  .--  . ..             I W I L L , W R
5  ..  -  . ,  ...  . .  ..*  -. ,  --            I T E , S O O N , M
6  .. ..*  ,  .-  -..  [^-..]  . ..  .  ...  ... ,  ..  ... ,
                                                  Y , A D D R E S S , I S ,
7  ....-  ---  --.. ,  .. .  .-  . ..  . ..  . .  =  = ,
                                                  4 5 7 , C A R R O L L ,
8  ...  - ,  .-  -.-  . ..  . .  -.  . .  ....  ..  . .
                                                  S T , A K R O N O H I O
```

![End of row 8: AKRON OHIO, the last dots running under the grey collector stamp (work/zoom_r8_end.png)](../work/zoom_r8_end.png)

## Plaintext and translation

Decipherment of all 64 signs:

```text
RECD YOUR CARD THIS AM I WILL WRITE SOON MY ADDRESS IS 457 CARROLL ST AKRON OHIO
```

Literal form of the word-sense points, with the card's own word division (no comma between I and WILL, nor between AKRON and OHIO):

```text
RECD YOUR CARD THIS AM OWI[L/T][L/T] WRITE SOIN MY ADDRESS IS 457 CARROLL ST AKRONOHIO
```

Normalised English: **"Rec'd your card this a.m. I will write soon. My address is 457 Carroll St., Akron, Ohio."**

**House number:** the Morse clearly gives 457, while the writer's own plain note on the picture side gives 547, twice. The decipherment keeps 457 as written; which of the two was the real address is not established.

Plain note on the picture side, normalised: **"No. 547 Carroll St., Akron, Ohio. I have not forgot the code but do not remember the No(s). on the Bx card. J. N. S."**

The text is English, so no English translation is needed.

Slovak translation:

- Cipher: **„Dnes ráno som dostal tvoju pohľadnicu. Čoskoro napíšem. Moja adresa je Carroll St. 457, Akron, Ohio.“**
- Picture-side note: **„Carroll St. č. 547, Akron, Ohio. Kód som nezabudol, ale nepamätám si čísla na tej ‚Bx‘ pohľadnici. J. N. S.“**

![Plain note along the caption strip of the picture side (work/pic_bx.png)](../work/pic_bx.png)

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1075/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of both portal scans and both high-resolution originals. It decodes the manual transcription in work/transcript.json with the American Morse key and checks that every decoded letter re-encodes to the transcribed sign. It prints the plaintext, the literal form above and the list of word-sense points. It decodes the transcription, not the image pixels; the transcription was checked independently in review.

## Uncertainties

- **I of "I WILL"** (row 4): two dots with a gap between this writer's I (tight) and O (wide). Read I; the pixels alone do not exclude O, and there is no comma between it and WILL.
- **WILL** (row 4): the two dashes are of middle length, shorter than the clear L's of CARROLL and about as long as the T of ST. Read L L by word sense; WITT is not a word.
- **SOON** (row 5): the second O is drawn with a tight gap that looks like I (literally SOIN). Read SOON by word sense.
- **MY** (row 6): the first pair of dots of the Y is a little wider than usual. Read Y; M + O + I gives no word.
- **457 vs 547:** see above. The writer's own remark that he does "not remember the No…" may explain a slip in numbers, but this is a guess.
- **Picture-side note:** "Bx" is an unexplained abbreviation (box? the name of a card?). "Noo" is read as "No(s)." (numbers). The initials are read J. N. S., where the N could be W. The rest of the note reads clearly.
- **Date and persons:** the card has no date or postmark. The date range rests on the printed view (hospital completed 1902) and the card type. The writer "J. N. S." and his relation to Ezra W. Sipple are not identified.
- The ten dots of OHIO lie under the collector stamp. The faintest of them is the least certain, but without it the word would read EHIO, which is nonsense.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, and the output was identical to the claimed plaintext. It made its own crops of the high-resolution scan, read all eight rows itself and decoded its reading with an independently written American Morse table. Its reading agreed with the solver's sign for sign. The only differences were exactly the disclosed word-sense points (O vs I before WILL, and the missing commas in OWILL and AKRONOHIO). It located the ten OHIO ink dots under the collector stamp with its own blob-finding script and confirmed that American Morse reads all 64 signs. It also checked the plain picture-side note and the empty stamp box, and found no hidden writing. Its four findings were minor and all were addressed:

- **Notation of the WILL dashes.** The transcription table now writes them as long dashes read by word sense (`=*`), matching the machine-readable transcription.
- **House number.** The 457 / 547 conflict is now stated next to the plaintext, not only among the uncertainties.
- **Published-solution check.** The full HistoCrypt 2021 paper linked from the portal was searched. It is a statistical overview of the collection (it counts eight Morse-code cards) and gives no reading of this card; Akron, Sipple, Meyersdale and Carroll do not occur in it. Recorded in SOURCES.md.
- **Literal vs read forms.** The script now also prints the literal form, shown above.

No decoded letter changed as a result of the review. The transcription, decipherment, response to review and this report were made by Claude Opus 5.5; there was no earlier work on this number.

## Sources

- HC Portal record 1075, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1075 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3285/conversions/cpc_--_USA__USA___pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/3285/cpc_--_USA__USA___pic.jpg (work/hires/).
- Address side: https://api.hcportal.eu/media/3286/conversions/cpc_--_USA__USA___adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/3286/cpc_--_USA__USA___adr.jpg (work/hires/).
- Tobias Schrödel, "Cryptographic postcards", HistoCrypt 2021: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 (searched, no reading of this card).
- Sister card in this repository: ciphers/hcp-1453 (American Morse, 1906).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.
