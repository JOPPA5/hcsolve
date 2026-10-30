# HCP 1502 (pc_hcp_183): a Morse code love letter to "Nell", 10 May 1911

Human solver: Tomáš Pavuk

**Status: deciphered in full (233 of 233 Morse letters, no unreadable group, no restored letter); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1502 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1502), portal name pc_hcp_183, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Unknown, date 1911-05-10, language Unknown, location Europe, sender Unknown, recipient O. Davy, with no transcription or solution attached.

The picture side is a printed colour view titled "Natures wild Beauty" (a waterfall in a flower frame) and carries no cipher. The cipher is on the address side. That side carries a cursive date **May 10th 1911**, written beside the printed words "This space may be used for communication", and the plain address **Miss O. Davy, Gilberdyke, E. Yorks.** (Gilberdyke is a village in the East Riding of Yorkshire). It has a green halfpenny Edward VII stamp and two GILBERDYKE R.S.O. postmarks dated May 1911 (one reads 6 AM, MY 11, 11). The printer's line on the left edge reads "Series 1362. Printed in Saxony."

Almost the whole address side, except the address itself, is covered with rows of pen dots, dashes and round blots. These are International Morse code. A cursive "P.S." stands at the top left.

![Address side: rows of Morse in pen, the cursive date May 10th 1911, the address to Miss O. Davy, Gilberdyke, E. Yorks, and the Gilberdyke postmarks (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, "Natures wild Beauty"; no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

**Who did what.** An earlier OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) captured the portal page on 2026-10-26 (all three tabs, both scans, the source list) and noted that the marks look like Morse. It made no transcription and no plaintext claim. Claude Opus 5.5 transcribed and deciphered the card on 2026-10-29/30. A separate Claude Opus 5.5 agent reviewed the result. No published solution of this card was found or used.

## Method

The writer uses ordinary Morse with pen strokes:

- a **short stroke** is a dot (about 6–16 px long in the 1024 × 674 scan);
- a **long stroke** is a dash (about 19–39 px);
- a **small point** closes each letter;
- a **large round ink blot** closes each word.

So both letter and word boundaries are written out explicitly. That removes the usual ambiguity of handwritten Morse.

There are two blocks of text, both read left to right and top to bottom with no rotation:

- **Block A** (8 rows, top left, starting beside the cursive "P.S.") is a postscript.
- **Block B** (24 rows, below the printed "This space may be used for communication") is the letter itself.

The rows run across the whole card, past the printed dividing line, and slope down to the right by about 30 px over the card's width. Because of that slope, the right-hand ends of one row lie at the same height as the left-hand starts of the next one or two rows. In the transcription each row is labelled with the y-coordinate of its **left end** (for example B607 starts at y ≈ 607 but ends near y 640).

The transcription is **manual**. Small scripts made enlarged and straightened crops of each row (6–14× enlargement) and listed stroke lengths to help the eye. They were not used to read the text, because they miss faint strokes and small points. A fixed length threshold between dot and dash also fails for this writer: it turned HOPE into VOPE and SEE into GEE, because some of his dots run to 16 px. Every row was therefore read by eye. The result is a file with one line per pen row, in dots and dashes, with `/` for each word blot. A short decoder decodes it with the standard Morse table. Every group must be a valid Morse letter, or the decoder stops with an error.

## Key

Plain **International (Continental) Morse code**, letters A–Z only, with no further substitution:

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| .- | -... | -.-. | -.. | . | ..-. | --. | .... | .. |
| **J** | **K** | **L** | **M** | **N** | **O** | **P** | **Q** | **R** |
| .--- | -.- | .-.. | -- | -. | --- | .--. | --.- | .-. |
| **S** | **T** | **U** | **V** | **W** | **X** | **Y** | **Z** | |
| ... | - | ..- | ...- | .-- | -..- | -.-- | --.. | |

Q, X and Z do not occur. One handwritten "&" sign, which is not Morse, stands in "love & kisses". Morse for digits and punctuation does not occur.

## Transcription

Block A (postscript):

```text
A050: ... .- ...- . /
A064: -- . / --- -. . /
A081: ..-. --- .-. /
A100: ... ..- -. -..
A117: .- -.-- / .. /
A135: .- -- / .-. . .- -.. -.-- /
A151: ..-. --- .-. / --- -. . /
A167: -. --- .-- / -. . .-.. .-.. /
```

Block B (letter):

```text
B222: -.. . .- .-. / -. . .-.. .-.. /
B235: .--- ..- ... - / .- / .-..
B249: .. -. . / .- ... / ..- ... ..-
B265: .- .-.. / .... --- .--. . /
B280: -.-- --- ..- / .- .-. . /
B299: -. --- - / -.- .. .-..
B316: .-.. .. -. --. / -.--
B333: --- ..- .-. ... . .-.. ..-. /
B353: - .... .. ... / .-- . . -.- /
B375: .. - ... / --. .-. .- -. -.. /
B395: .-- . .- - .... . .-. /
B414: ..-. --- .-. / - .... . /
B438: .--- --- -... / .-- . .-.. .-.. /
B458: ... .-- . . - .... . .- .-. - /
B481: .. -- / .-.. --- -. --. .. -. --. /
B503: ..-. --- .-. / ... ..- -. -.. .- -.-- /
B521: .. - / ... . . -- ... / ... ..- -.-. .... /
B539: .- / .-.. --- -. --. / .-- . . -.- /
B557: .-- . .-.. .-.. / ... --- / .-.. --- -. --. /
B576: -.. . .- .-. . ... - / - .. .-.. .-.. / .. / ... . . /
B593: -.-- --- ..- / .-- .. - .... / .- .-.. .-.. /
B607: -- -.-- / .-.. --- ...- . / & / -.- .. ... ... . ... /
B619: -.-- --- ..- .-. ... /
B632: --. . --- .-. --. .. /
```

Rows without a final `/` end in the middle of a word, and the word continues on the next row (SUND|AY, USU|AL, KIL|LING, Y|OURSELF, JUST A L|INE). In every such case the row break matches the decoded words.

## Plaintext

Decoded, as written (233 letters):

```text
P.S. SAVE ME ONE FOR SUNDAY I AM READY FOR ONE NOW NELL

DEAR NELL JUST A LINE AS USUAL HOPE YOU ARE NOT KILLING YOURSELF THIS WEEK ITS GRAND
WEATHER FOR THE JOB WELL SWEETHEART IM LONGING FOR SUNDAY IT SEEMS SUCH A LONG WEEK
WELL SO LONG DEAREST TILL I SEE YOU WITH ALL MY LOVE & KISSES YOURS GEORGI
```

Normalized English (case, punctuation and apostrophes are editorial; the card has none):

**Dear Nell, just a line as usual. Hope you are not killing yourself this week. It's grand weather for the job. Well, sweetheart, I'm longing for Sunday; it seems such a long week. Well, so long, dearest, till I see you. With all my love & kisses, yours Georgi.**

**P.S. Save me one for Sunday. I am ready for one now, Nell.**

The text is in English, so the translation is only a modernized paraphrase. "Killing yourself" means working too hard. "The job" is a task she has that week, apparently outdoor work, given the remark about the weather. The "one" saved for Sunday is presumably a kiss, which the card does not say.

Slovak translation: **Milá Nell, len pár riadkov ako zvyčajne. Dúfam, že sa tento týždeň neumáraš. Na tú robotu je nádherné počasie. Nuž, zlatko, túžim po nedeli; zdá sa mi to taký dlhý týždeň. Nuž, maj sa, najdrahšia, kým ťa neuvidím. So všetkou mojou láskou a bozkami, tvoj Georgi.**

**P.S. Nechaj mi jeden na nedeľu. Na jeden som pripravený hneď teraz, Nell.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1502/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the three files in `source/`, decodes the manual transcription in `work/transcription.txt` with the standard Morse table, and prints both blocks with the line `233 Morse letters decoded, all groups valid. Source hashes OK.` It does not read the image. The reading of the image is manual and was checked independently in review.

## Uncertainties

None of these affects the decoded text. Each is noted as a comment on its row in the transcription file.

- **ITS (row B375).** The two dots of I are drawn long (16 and 19 px), close to the length of a short dash. They are still about half as long as the T dash that follows. `..` = I gives "its grand weather"; reading them as dashes would give no word.
- **AM (row A135).** The second dash of M has a tiny pen-lift gap. It is read as one dash, because read as two dots it would give no word.
- **DEAR NELL (row B222).** No letter-end point is visible between E and the first L, where the "1" of the cursive date "1911" crosses the row; a point may be hidden under it. The second L begins with a heavier dot where the pen crossed the printed dividing line. NELL is written clearly in the P.S.
- **KISSES (row B607).** The dot of K is a tiny point rather than the writer's usual short stroke. `-.-` = K is the only reading that gives a word. The "&" is handwritten, not Morse.
- **ALL (row B593).** The first dot of the second L is a heavy mark that looks like a word blot. The strokes after it show that it is a dot.
- **Long dots elsewhere** (13–17 px) occur in HOPE, SEE and YOURSELF. The words fix them unambiguously.
- **Signature.** The ink of the last row is faint. The name ends GEORGI, followed by a word blot and then the card edge, so it is complete as written. It is presumably *Georgie* or a nickname. No letter is restored.
- **Nell and Miss O. Davy.** The letter is addressed to "Nell", the card to Miss O. Davy. "Nell" may be her name, a pet name, or someone else in the household; nothing on the card links "Nell" to the initial O. Neither the writer "Georgi(e)" nor the recipient has been identified; no genealogical search was made.
- Only the portal scan (1024 × 674) was available, with no higher-resolution original. The faintest points were read at the limit of that resolution.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer:

- ran the reproduction command and got exactly the claimed text;
- decoded the transcription with its own, separately written Morse decoder and got the same 233 letters, with no invalid group;
- made its own crude machine read of the pixels, classifying marks by length only, with no knowledge of words. This produced fragments such as ONE, FOR, AS USU, KIL, OURSELF, SWEETHEART, IT SEE.S SU..H, DEAREST TILL I SEE and ..ORGI, and no row contradicted the reading;
- checked about a third of the rows mark by mark on 5–6× enlargements, with pixel coordinates (among them SAVE, AM READY, DEAR NELL, ITS GRAND, ALL, & KISSES and GEORGI);
- confirmed that the language and the context fit (English of the period, Gilberdyke postmarks of May 1911), and that the portal had no attached solution.

It made four minor findings, all addressed with no change to the reading:

1. **Signature row.** SOLUTION.md said that nothing follows the last `..` of GEORGI. In fact a word blot follows it. The text now says so, and the transcription marks it.
2. **Unusual marks only in prose.** The broken M dash, the hidden E|L boundary, the long I dots, the heavy L dot and the point-sized K dot are now flagged as comments on their rows in the transcription. The decoder ignores those comments.
3. **Nell vs Miss O. Davy.** The text now says that "Nell" may be a pet name and that nothing on the card links it to the initial O.
4. **Row labels.** The transcription and this report now explain that labels give the y of a row's left end and that the rows slope about 30 px across the card.

Not verified by anyone: the identity of the writer and of the recipient. The remaining two thirds of the rows were checked by the reviewer only through its noisy machine read.

## Sources

- HC Portal record 1502, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1502 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4567/conversions/pc_hcp_183_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4566/conversions/pc_hcp_183_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no record for this card.
