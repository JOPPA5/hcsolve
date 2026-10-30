# HCP 1494 (pc_hcp_175): a postcard from Clarence, Crookston, Minnesota, 1915

Human solver: Tomáš Pavuk

**Status: deciphered in full (115 of 115 cipher signs). Independent review 1 gave the verdict ACCEPT, and no decoded letter changed.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1494 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1494), portal name pc_hcp_175. It belongs to the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26, the portal listed it as **Not solved**. Its tags were Postcard, HCPortal collection and category Substitution; the date was 1915-02-18, the language Unknown, the location North America and the sender Unknown. The recipient was given as Elvira Jungleseth. No transcription or solution was attached.

The picture side is a printed view of Houston Avenue, Crookston, Minn. The address side carries a US 1-cent stamp and two postmarks, Crookston and Fertile, Minn., 18 Feb 1915. It is addressed in plain cursive to **Miss Elvira [surname] / Fertile / Minn.** The portal reads the surname as Jungleseth. The first letter can equally be read as F or I, which gives **Fugleseth** (a Norwegian surname that fits the Norwegian-settled Fertile area) or Ingleseth. The message is written sideways in the lower half of the address side. Plain English handwriting and lines of cipher signs alternate there. The cipher signs are digits and keyboard-like marks (%, #, +, =, −).

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Address side turned so that the message reads left to right (work/upright.jpg)](../work/upright.jpg)

![Picture side: Houston Avenue, Crookston, Minn. (source/picture-large.jpg)](../source/picture-large.jpg)

Some of the message is not cipher. It is plain handwriting: "since", "I am still at my old Place", "and", the question mark, the return address "715 Hunter St." and a cursive closing word above the signature. These plain words interlock with the decoded cipher words, so they act as an independent check.

## Method

An earlier OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol, 2026-10-26) named the symbols, found the key from the obvious words (DEAR, HEARD, FROM, HAVE, WORKING, EVERY, DAY) and made a first transcription. It left the card as partial, with an unresolved last word (literal WANTTM). On 2026-10-29, Claude Opus 5.5 rotated the scan and read every sign again on 4–12× enlargements. It corrected three places (TIME, ALLTOGETHER and the last word), wrote a new transcription and wrote a decoder that prints both a sign-by-sign literal reading and a normalised text. The transcription was made by hand; no OCR was used.

The cipher is a **simple monoalphabetic substitution**. Each sign stands for one letter, with no homophones and no nulls, and the writer keeps the word division. No sister card in the same cipher is known in this repository.

## Key

| Letter | Sign | Letter | Sign | Letter | Sign |
|---|---|---|---|---|---|
| A | 1 | H | 8 | R | T-like stroke |
| C | c / C | I | 7 | S | # |
| D | 2 | K | 4 | T | % |
| E | ε | L | 5 | U | u |
| F | = | M | 9 (q-like) | V | V/U-shape |
| G | + | N | 6 | W | cursive-D shape |
| O | 0 | Y | − | | |

The key covers 20 letters. B, J, P, Q, X and Z do not occur, so their signs are unknown. Each sign gives the same letter everywhere on the card. For example, 8 is H in HEARD, HAVE, HEAR and TOGETHER; = is F in FROM (twice) and IF; − is Y in YOU (four times), EVERY and DAY.

## Plaintext

Literal decode, line by line as on the card. Cipher words are in capitals, plain handwriting is in lower case or as written, and [a|b] shows two possible readings of one sign:

```text
DEAR D
IT IS A LONG TIMH AGO
since I HEARD FROM
YOU HAVE YOU FORGGOTT
EN ME ALLTOG[A|I]GTHER ?
I am still at my old Place
and WORKING EVERY DAY
LET ME HEAR FROM YOU
IF YOU WANT T[O|M]   <two 9-like marks below the last word>
715 Hunter St.
<plain closing word, probably "Yours">
CLARENCE
```

Normalised English (original language):

**Dear D: It is a long time ago since I heard from you. Have you forgotten me altogether? I am still at my old place and working every day. Let me hear from you if you want to. 715 Hunter St. [Yours?] Clarence**

Slovak translation:

**Milá D., je to už dávno, čo som od teba počul. Zabudla si na mňa úplne? Stále som na svojom starom mieste a pracujem každý deň. Ozvi sa mi, ak chceš. Hunter St. 715. [Tvoj?] Clarence**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1494/work/decode_v2.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the two scans and the metadata. It then decodes the manual transcription (work/transcription-v2.txt) with the key (work/key.json) and prints the literal and normalised text, with the line `cipher signs: 115; with alternative readings: 2; writer slips/extra signs: 4`.

## Uncertainties

- **Greeting "DEAR D".** The second sign is clearly a 2 (D), although it lacks the small loop the writer gives his other 2s. The card is addressed to Elvira, so D may be a nickname or an initial. This is **not resolved**.
- **TIMH.** The fourth sign of TIME is a closed 8 (H), not the open ε (E). In this hand the two shapes are close, so it is read as a writer's slip.
- **FORGGOTTEN.** Two distinct + signs (G) are written. This is a writer's error, normalised to "forgotten".
- **ALLTOGETHER.** The signs are 1 5 5 % 0 + [dark flagged stroke] + % 8 ε T. Where E is expected there is a heavy, apparently re-inked stroke that resembles 1 (A) or 7 (I), followed by a second +. The word is certain from the context. These two signs are treated as a slip or correction and not read as anything else. "Alltogether" is the writer's spelling.
- **Question mark.** The mark after ALLTOGETHER has no dot and looks like the writer's 2. It stands outside the cipher word at the end of a question, so it is read as a plain "?".
- **Last word.** % 0 = TO. The 0 has a faint, thinner tail, which is why the earlier partial reading had M (9). There are also two 9-like marks below the word. They may be a later addition or a correction (for example towards "want me"). They are reported and not decoded. "If you want to" fits the sentence.
- **Plain closing word** above the signature: probably "Yours", but it is not securely legible.
- **People and places.** Clarence and the recipient have not been identified. The surname (Jungleseth / Fugleseth / Ingleseth) is uncertain, and 715 Hunter St. is presumably in Crookston. No external search was made.

## Review summary

The reviewer was a separate Claude Opus 5.5 agent (Anthropic). Round 1 gave the verdict **ACCEPT**. The reviewer ran the reproduction command and got output identical to the claimed plaintext. It rotated and enlarged the scan itself, read all nine cipher rows and the signature under its own sign names, and decoded them with a key it rebuilt independently. Its reading agreed with the solver's sign for sign (115 signs, 20 letter signs plus the two disclosed slips). It confirmed that the key is one-to-one and covers the whole cipher text. It also confirmed that the text is idiomatic early-20th-century American English, which fits a private card between two small Minnesota towns.

Its five findings were minor:

1. SOLUTION.md said "21-letter key". This was corrected to 20.
2. A garbled sentence in SOLUTION.md was corrected.
3. The question mark looks like a 2. A note was added to the transcription saying that it is read as a plain "?".
4. The recipient's surname may be Fugleseth or Ingleseth. These alternatives are now given in this report.
5. "DEAR D" against "Elvira" is left as an open point.

No decoded letter changed as a result of the review.

Credit: the symbol inventory, key and first partial transcription were made by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol). Claude Opus 5.5 completed the transcription and decipherment and prepared this report. A separate Claude Opus 5.5 agent carried out the independent review.

## Sources

- HC Portal record 1494, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1494 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4543/conversions/pc_hcp_175_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4542/conversions/pc_hcp_175_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no record for this card.
