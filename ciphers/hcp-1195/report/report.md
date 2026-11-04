# HCP 1195: a rune-alphabet love card from Tepl to Anton Schönfelder, 1900

Human solver: Tomáš Pavuk

**Status: deciphered in full (12 lines, 198 cipher signs, every sign mapped); independent review 1 verdict ACCEPT, no change to the decoded text.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1195 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1195), portal name cpc_1900-02-25_AT_Tepi_AT_Wien_schoenfelder-01, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Anton Schönfelder, with no transcription or solution attached. The portal's source reference is the HistoCrypt article https://ecp.ep.liu.se/index.php/histocrypt/article/view/166.

The picture side is a printed card "Bergbleameln" (two girls in Alpine costume, one with a hay rake; E. Riedel, Kunstverlag, Berlin, No. 112) with the printed heading "Gruss aus" completed in pencil as **Tepl 25/II 00** (Teplá in western Bohemia, Sunday 25 February 1900). Twelve lines of rune-like signs fill the right half. Under the picture is a small pencil footnote in Kurrent: a star, an equals sign and one letter, read "i", which glosses a starred, overwritten sign in line 8.

The address side is in plain handwriting: **Wolgeborn Herrn Anton Schönfelder, Wien IV, Favoritenstrasse 64, Th. 29, V. Stiege**. It carries an Austrian 5 Heller stamp cancelled TEPL and a Vienna arrival mark of 26.2.00, which agrees with the written date.

![Picture side (source/picture-large.jpg): the twelve cipher lines right of the picture, the footnote under the picture](../source/picture-large.jpg)

![Address side (source/address-large.jpg): plain address to Anton Schönfelder, Wien IV](../source/address-large.jpg)

A sister card, HCP 1194, has the same sender, the same recipient and the same alphabet; it was worked separately and was not used for this reading. Its signature reads RASA, which under this alphabet's A/O homograph can be ROSA.

## Method

The portal supplied no transcription. The solver (Claude Opus 5.5) read all twelve lines sign by sign from enlarged crops of the full-resolution original scan (3468 x 2298 pixels) and wrote a sign-code transcription. The alphabet is a home-made set of rune-like shapes, so the key had to be recovered from the card itself. Short words gave the first cribs (BRIEF, FÜR, KARTE, ZU, UND). Lines 4 to 6 then turned out to quote Goethe: "Langen und bangen in schwebender Pein" from Klärchen's song in Egmont ("Freudvoll und leidvoll"), which fixed most of the remaining signs. The rest of the text then read without any further choice.

The writer follows the old idea of "dotted runes": a dot turns K into G, B into P, U into Ü and F into W. Two signs are homographs: one sign stands for both A and O, and the two-twig sign (fehu) stands for both F and V. Every word has exactly one German reading under these choices.

In GLIECHZIETIG the writer first wrote H before C, then marked the two signs with small "2" and "1" to reverse them; the decoder applies this.

The reviewer wrote its own decoder with no word-level fixes, printing every homograph as a set, and confirmed that each word admits only one German reading, that all 198 signs are mapped, and that recurring words (BRIEF twice, MORGEN twice) decode identically. It also compared the transcription sign by sign with the scan.

## Key

Monoalphabetic substitution; sign names describe the handwritten shapes.

| Sign | Letter | Sign | Letter |
|---|---|---|---|
| asterisk rune | H | plus or crossed stem (also Y-form, dotted, slanted with dot) | E |
| plain stem | I | R-rune | R |
| down arrow (↓) | Z | hook rune | L |
| lightning, sowilo (ϟ) | S | up arrow (↑) | T |
| fehu, two twigs | F or V | fehu with dot | W |
| one-twig rune | K | one-twig rune with dot | G |
| square u-rune (Π) | U | the same with dot | Ü |
| B | B | B with dot | P |
| lambda (Λ, λ) | N | stem crossed by two bars | D |
| angle (<) | C | stem with slant stroke on the left | A or O |
| psi, algiz (Ψ) | M | gamma with dot (once) | IC |

Letters J, Q, X and Y and the umlauts Ä and Ö do not occur. Word gaps and punctuation (full stops, dashes) are written in plain.

## Plaintext

As written, line by line (the writer's spellings kept):

```text
HERZLICHST FÜR LIEBEN BRIEF
DANKEND GLIECHZIETIG BITTEND
MIR VORIGE SONNTAGS KARTE
ZU VERZIEHEN . LANGEND
UND BANGEND IN SCHEBEN -
DER PIEN -- FÜRCHTETE
VERNEINDE ANTWORT
AUF MEINE FRAGE .
MORGEN ODER ÜBER MORGEN
FOLGT BRIEF .
MIT KUSS
DEIN LIEB
```

Normalised German: **Herzlichst für [deinen] lieben Brief dankend, gleichzeitig bittend, mir [die] vorige Sonntagskarte zu verzeihen. Langend und bangend in schwebender Pein – fürchtete [ich eine] verneinende Antwort auf meine Frage. Morgen oder übermorgen folgt [ein] Brief. Mit Kuss, dein Lieb.**

English: **Thanking you most warmly for your dear letter, and at the same time asking you to forgive me for last Sunday's card. Longing and fearing in suspended anguish – I feared a negative answer to my question. A letter follows tomorrow or the day after. With a kiss, your love.**

Slovak: **Najsrdečnejšie ďakujem za milý list a zároveň prosím, aby si mi odpustil minulú nedeľnú pohľadnicu. Túžiac a bojac sa v napätom trápení – obávala som sa zápornej odpovede na moju otázku. Zajtra alebo pozajtra príde list. S bozkom, tvoja láska.**

Notes on the reading:

- The writer's own spellings are kept in the literal text: GLIECHZIETIG (gleichzeitig), VERZIEHEN (verzeihen) and PIEN (Pein) write EI as IE, while DEIN, MEINE and VERNEINDE have EI correctly; SCHEBEN-DER drops the W of "schwebender"; VERNEINDE stands for "verneinende".
- "Langen und bangen in schwebender Pein" is a line of Klärchen's song in Goethe's Egmont; the writer turns it into participles (langend und bangend).
- 25 February 1900 was a Sunday, so "die vorige Sonntagskarte" is the card of the previous Sunday.
- The recipient is a man (Herr Anton Schönfelder). The writer is probably a woman: a love card signed "Dein Lieb", and the sister card is signed RASA or ROSA. The Slovak translation therefore uses feminine forms for the writer; this is an inference, not a certainty.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1195/work/decode.py
```

The script checks the SHA-256 hashes of the four source images, applies work/key.json to the manual transcription in work/transcription.txt, applies the writer's "2 / 1" reorder marks, and prints the raw output (homographs in braces) and the plaintext above.

## Uncertainties

- **Homographs.** A/O (the slant-stroke sign) and F/V (the fehu) are chosen by word sense; no stable difference in shape was found. Each word has only one German reading.
- **HERZLICHST.** Between L and H stands a single gamma-with-dot sign that occurs nowhere else; it carries "IC" (as a ligature, or C with I left out). A flourish of the printed header runs over it. The word itself is certain.
- **MEINE (line 8).** The third sign is heavily overwritten and starred; the footnote glosses it. The Kurrent letter of the footnote has a lead-in, one down stroke and a w-like connector, with no clearly visible i-dot. It is read as "i", but that reading leans on MEINE, the only sense of the word; the footnote is consistent with MEINE rather than independent proof of it.
- **LANGEND (line 4).** The first sign is not the usual hook-L: it is a stem with a diagonal down to the right and a dot, written over erased traces, closer in shape to the N sign. L is supplied by word sense and the Goethe line.
- **Under the collector's stamp.** The two S of KUSS cannot be separated from the stamp lettering; SS is restored from context ("Mit Kuss"). The R and final T of ANTWORT and the final N of the second MORGEN are faint under the stamp ring and only compatible with the reading.
- **E against K.** On this card E has a bar crossing the stem and K is a one-sided twig. In MEINE (final sign) and FÜRCHTETE the left half of the bar is faint, so those E calls also lean on word sense.
- **Hidden writing.** Both solver and reviewer searched the picture, its margins, the caption and the edges, and the address side: there is no further writing besides the cipher, the header date, the footnote and the address. Beneath the affixed 5 Heller stamp could not be inspected on the scan.
- **No published solution** of this card was found; the portal attaches none and lists it as Not solved.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (all hash checks OK, output identical to the plaintext), decoded the transcription with its own independent script, checked the transcription sign by sign against the full-resolution scan, confirmed the date and postmarks, and compared the alphabet with the sister card 1194. Its six findings were all minor and concerned documentation only:

- **Slovak genders.** The Slovak translation had the genders reversed; it now addresses a male recipient and uses feminine forms for the probably female writer.
- **L of LANGEND.** Now stated to rest on word sense and the Goethe line, not on the sign's shape.
- **KUSS.** The two S are now called a restoration from context.
- **Footnote gloss.** The "i" reading is now stated to lean on MEINE.
- **Faint signs under the stamp.** ANTWORT (R, T) and MORGEN (N) are now listed with KUSS.
- **E against K.** The faint bars in MEINE and FÜRCHTETE are now listed as calls that partly rest on word sense.

No decoded letter changed as a result of the review. The register type is MASC: no steganographic message was found on this card.

Credits: transcription, key reconstruction and decipherment by Claude Opus 5.5 (Anthropic), 2026-11-03; no earlier AI work on this number; independent review by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1195, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1195 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3645/conversions/cpc_1900-02-25_AT_Tepi_AT_Wien_schoenfelder-01_pic-large.jpg (source/picture-large.jpg); full-resolution original in work/hires/.
- Address side: https://api.hcportal.eu/media/3646/conversions/cpc_1900-02-25_AT_Tepi_AT_Wien_schoenfelder-01_adr-large.jpg (source/address-large.jpg).
- J. W. von Goethe, Egmont (1788), Act III, Klärchen's song "Freudvoll und leidvoll".
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.
