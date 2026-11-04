# HCP 1191: a 1907 family postcard from Pete and Edna to J. E. Fortune, Ohio

Human solver: Tomáš Pavuk

**Status: deciphered in full (268 of 268 cipher signs; one name in the salutation, "?OS", has an unread first letter); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1191 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1191), portal name cpc_1907-09-07_USA_Coshocton, Ohio_USA_Canal, Lewisville, Ohio_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient JE Fortune, with no transcription or solution attached.

It is a United States one-cent postal card with an imprinted McKinley stamp. The address side is in plain writing: **J E Fortune, Canal Lewisville, O.** It carries the cancellation COSHOCTON OHIO SEP 6 4-PM 1907 and the receiving mark CANAL LEWISVILLE OHIO SEP 7 1907. Coshocton and Canal Lewisville are a few miles apart in Coshocton County, Ohio.

The other side holds the message, written entirely in invented symbols in violet ink, except for the date digits "5 1907" in the header. The scan is turned sideways; read upright (scan rotated 90° counter-clockwise) it has a header and twenty lines, the last of which curves up the right-hand edge.

![Message side turned upright (work/message-upright.jpg, from source/picture-large.jpg)](../work/message-upright.jpg)

![Address side: J E Fortune, Canal Lewisville, O.; imprinted one-cent stamp and Coshocton cancellation (source/address-large.jpg)](../source/address-large.jpg)

Hidden writing was looked for on both sides. Because the stamp is printed on the card, nothing can be hidden under it, and no extra or hidden writing was found anywhere else. Both the solver and the reviewer checked this. There is no picture side.

## Method

All the work on this number was done by Claude Opus 5.5 on 2026-11-03; there was no earlier work by another model.

The transcription is **manual**. The solver read the un-converted high-resolution scan, turned upright, line by line, with 2–4x enlargements of difficult places and a violet-ink separation for the two signs that lie under the HCPortal collection stamp. Each sign was given a short code (work/transcription.txt), and the code-to-letter table is work/key.tsv.

The key was recovered from the text alone; there are no sister cards to this recipient in the repository. The repeated four-sign word with a doubled last sign was taken as WELL. Three words that end in the same four signs gave -IGHT (NIGHT twice, RIGHT), which fixed G, H, T and I. THE, THIS, GUESS, the closing "ALL FOR THIS TIME" and the signature "FROM PETE AND EDNA" then fixed the rest. Every letter that occurs only a few times (F, K, B, C, P, J) gives a real word in each place: FEW, FOR, FROM, KNOW, BE, BUGGY, CAN, CLOSE, COME, PA, PETE, HOPE, JAKE.

In review a separate Claude Opus 5.5 agent read the scan band by band, wrote its own code-to-letter table from its own reading and decoded the transcription with its own script. Its output was identical line for line to the solver's.

## Key

Simple monoalphabetic substitution (MASC) with invented symbols. Words are divided by small ticks, dots or gaps. The descriptions are of the card read upright.

| Plain | Sign | Plain | Sign |
|---|---|---|---|
| A | rhombus with one diagonal | L | ÷ |
| B | right-triangle wedge | M | V with a tail or base stroke |
| C | downward triangle ∇ | N | box open at the top with a middle bar (like ㅂ) |
| D | crescent "(" | O | circle with a slash leaving at the lower left |
| E | circle with a horizontal bar (θ) | P | "7" |
| F | "4"-like sign | R | "+" |
| G | two or three verticals with a crossbar (卅) | S | square on a stem |
| H | circle on a stem ♀ | T | dome (half disc, flat side down); twice an inverted bowl |
| I | X, often with a top bar | U | circle with a central dot ⊙ |
| J | asterisk (once, by word sense) | W | circle with a short stroke on its left |
| K | vertical with two crossbars | Y | "%"-like slash with two dots |
| ? | Y-shaped sign, once, in the salutation | | |

Q, V, X and Z do not occur.

## Plaintext

Literal English as decoded, line for line (the writer's own spellings kept):

```text
SET 5 1907
WELL ?OS I THOUGHT
I WOULD WRITE YOU A
FEW LINE TO LET YOU
KNOW THAT WE ARE
ALL WELL AND HOPEING
ARE THE SANE WELL WE
WILL GO UP TO PA A
SUNDAY NOT A SATDAY
NIGHT SO YOU CAN
COME A ROUN SATDAY
NIGHT WELL JAKE I
GOT NY BUGGY PAINT
ALL RIGHT WELL I
GUESS THIS WILL BE
ALL FOR THIS TIME
SO CLOSE HOPE TO
SEE A SATDAY
SO GOODBY
FROM PETE AND EDNA
```

Normalised English: **Sept. 5, 1907. Well [?]os, I thought I would write you a few lines to let you know that we are all well and hope you are the same. Well, we will go up to Pa's on Sunday, not on Saturday night, so you can come round on Saturday night. Well Jake, I got my buggy painted all right. Well, I guess this will be all for this time, so I close. Hope to see you on Saturday. So goodbye, from Pete and Edna.**

Slovak translation: **5. sept. 1907. Nuž [?]os, pomyslel som si, že ti napíšem pár riadkov, aby si vedel, že sme všetci zdraví, a dúfame, že ty tiež. Nuž, v nedeľu pôjdeme hore k otcovi, nie v sobotu večer, takže v sobotu večer môžeš prísť k nám. Nuž, Jake, dal som si v poriadku natrieť bričku. Nuž, myslím, že to bude zatiaľ všetko, tak končím. Dúfam, že sa uvidíme v sobotu. Tak zbohom, Pete a Edna.**

Notes on the reading:

- "A Sunday", "a Saturday" is the old colloquial "a-" for "on". It is used the same way all three times.
- SET in the header is the month (Sept.): the date digits "5 1907" are in clear, and the Coshocton postmark is the next day, Sep 6, 1907.
- HOPEING, LINE (for lines), ROUN (around), SATDAY (three times), GOODBY and PAINT (for painted) are the writer's spellings, typical of an informal rural family letter of the time.
- JAKE fits the recipient's initial J (J. E. Fortune).

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1191/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the two portal scans and the high-resolution message scan, decodes the manual transcription work/transcription.txt with work/key.tsv, and prints the literal plaintext above. A saved copy of the output is work/plaintext.txt. The transcription step itself is manual and was confirmed independently in review.

## Uncertainties

- **"?OS" in line 1.** The first sign of the name in the salutation is a Y-shaped mark that occurs nowhere else. JOS (Jos., Joseph) is likely, but the asterisk in JAKE is already J, and one key should not have two J signs. The word is left as "?OS". It is the only unread word on the card.
- **J in JAKE.** The asterisk occurs only once; J rests on word sense (the only free letter that makes a word with -AKE).
- **Restored and deleted signs.** A heavy ink blot covers one sign in LINE (line 3); it is restored as I. A blotted mark with a stem before SEE (line 17) is taken as a deletion, not a letter.
- **Faint signs.** WE in line 4 lies under the HCPortal collection stamp and was read after ink separation. The T of TO in line 7 is a faint dome on an abraded patch, and a pale ghost stroke before PA is ignored. The R of ROUN (line 10) is overwritten, with a + visible inside a loop, and the dot of its U is not clear, so U rests partly on word sense.
- **N where M is expected, twice:** SANE (same) and NY (my). The N of NY is a clean N sign. The N of SANE has extra strokes and looks overwritten, perhaps an attempt to correct it towards M. Both are read literally as N and taken as writer's slips; M has its own sign elsewhere (COME, TIME, FROM).
- **Two forms of T.** An inverted bowl in GOT and PAINT is read as T by word sense, as a flipped form of the dome.
- **Line-end mark.** A small "(" after WE at the end of line 6 is smaller and thinner than the crescent D; it is taken as a line-end divider, not as D.
- **Word division.** AND / EDNA on the curved last line has no visible divider.
- The people (Pete and Edna, J. E. Fortune or "Jake") were not identified; no genealogical search was made.
- A short web search on 2026-11-03 found no published solution of this card, and the portal attaches none.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the saved plaintext), decoded the transcription with its own independently written table (identical output, no uncovered sign), checked every line of the transcription against enlarged crops of the high-resolution scan, and confirmed that the address side has no hidden writing and the card no picture side, so the type is plain MASC. Its four findings were minor and were handled as follows:

- **Counts.** SOLUTION.md overstated the repeats (now WELL 5×, ALL 3×) and the sign count (now 268 cipher signs plus one struck-out mark).
- **Line-end mark in line 6.** Now disclosed as a divider.
- **Overwritten N in SANE.** Now described as overwritten, not identical to the other N signs; the reading N is kept.
- **"?OS".** Left literal as the only unread word, as before.

No decoded letter changed because of the review.

## Sources

- HC Portal record 1191, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1191 (source/metadata.md).
- Message side and address side scans from the portal (source/picture-large.jpg, source/address-large.jpg) and the un-converted originals (work/hires/); see SOURCES.md.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.
