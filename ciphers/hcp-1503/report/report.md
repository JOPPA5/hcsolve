# HCP 1503 (pc_hcp_184): a Morse love note to Miss Curtis, Lincoln, June 1905

Human solver: Tomáš Pavuk

**Status: deciphered in full (13 lines, 189 Morse letters, 484 elements); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1503 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1503), portal name pc_hcp_184, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Unknown, date 1905-06-20, language Unknown, location Europe, sender Unknown, recipient "Suvtis", with no transcription or solution attached.

The address side is a British halfpenny picture postcard published by M. Ettlinger & Co., London E.C. (*The Royal Series*, Sunset Series No. 4397). It carries a green halfpenny stamp of Edward VII cancelled **TOOTING S.W., 9 AM, ..05** (the day and month are not legible on the scan; the portal gives 20 June 1905). It is addressed in plain handwriting to **Miss Curtis, Laurel House, Riseholme Rd, Lincoln**. The portal's recipient "Suvtis" is a misreading of "Curtis".

The message fills the left half of the address side (the half the Post Office allowed for "inland communication") with a heading and twelve lines of ink marks that look like rows of commas and tall strokes. They are Morse code. The picture side is a painted sunset with a ship and carries no cipher text.

![Address side: Morse message at the left, address to Miss Curtis, Laurel House, Riseholme Rd, Lincoln at the right, TOOTING S.W. postmark (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Sunset Series painting, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

Other marks on the card, none of them cipher: the printed postcard headings and publisher's line, the stamp and postmark, the address, and the HCPortal watermark.

## Method

**Earlier work.** On 2026-10-26 an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) captured the portal record and both scans, recognised the script as Morse code and read the heading as MONDAY and the first word as SWEETHEART. It could not reliably tell dots from letter separators and stopped without claiming the body text.

**Full reading.** On 2026-10-29/30 Claude Opus 5.5 established the writer's convention on the pixels and transcribed all thirteen lines by hand from enlarged crops (7x contrast tiles and 9-16x raw crops of every line; doubtful spots were checked as raw pixel values). No OCR was used and the portal supplied no transcription. The convention is:

- **dash:** an ink blob with a tall upward tail;
- **dot:** an ink blob with no tail or only a short one;
- **letter separator:** a small slanted comma-like stroke after each letter, set below the line and running down to the left (on the cramped last line these shrink to small low dots);
- **word separator:** a wider gap.

The observation that unlocked the body was that the separators sit about 10-15 px below the baseline and slant down-left, so they can be told apart from the dots and from the dash tails of the line below. The transcription (letters separated by spaces, words by "/") was then decoded with the standard International Morse alphabet by a short script.

In review a separate Claude Opus 5.5 agent made its own 4-8x enlargements, checked most lines sign by sign, and decoded the transcription with its own independent Morse table and parser; it obtained the same thirteen lines.

## Key

Standard International (Continental) Morse code, with no further encipherment:

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| A `.-` | B `-...` | C `-.-.` | D `-..` | E `.` | F `..-.` | G `--.` | H `....` |
| I `..` | J `.---` | K `-.-` | L `.-..` | M `--` | N `-.` | O `---` | P `.--.` |
| Q `--.-` | R `.-.` | S `...` | T `-` | U `..-` | V `...-` | W `.--` | X `-..-` |
| Y `-.--` | Z `--..` | | | | | | |

Every one of the 189 letter groups on the card is a valid Morse letter; no group needed adjustment. P, Q, X and Z do not occur. The Morse has no punctuation and no apostrophes; the only non-letter marks are one isolated tiny dot in line A and a horizontal pen flourish before the signature.

## Plaintext

Transcription, line by line as on the card (HD = heading, A-L = body lines):

```text
HD: -- --- -. -.. .- -.--
A: ... .-- . . - .... . .- .-. - / (.) / .-- .. ..-. .. .
B: .-- --- .-. -.- / .-- . -. - / -.. --- .-- -. / .-. .- - .... . .-.
C: ..-. .-.. .- - / - --- -.. .- -.-- / .. / .- --
D: -.. .-. . .- -.. ..-. ..- .-.. .-.. -.-- / - .. .-. . -.. / - ---
E: -. .. --. .... - / .. ...- . / -... . . -. / ... . - - .. -. --.
F: -... ..- - - --- -. ... / --- -. / ... --- / .- ... / - ---
G: -- .- -.- . / -- -.-- / -.-. .-.. --- - .... . ...
H: .... .- -. --. / --- -. / .... --- .-- / ... .... --- ..- .-.. -..
I: -.-- --- ..- / .-.. .. -.- . / - .... .- - / .--- --- -...
J: .. / .- -- / .- / .-.. --- ...- . ... .. -.-. -.- / -.-. --- --- -.
K: .-- --- .-. ... . / - .... .- -. / . ...- . .-. / .. / .-- .- ...
L: -... . ..-. --- .-. . / ~ / -.-. ..- -.-. -.- --- ---
```

Decoded, line by line (`(.)` = the isolated stray dot, `--` = the pen flourish; both are kept in this diplomatic text):

```text
HD: MONDAY
 A: SWEETHEART (.) WIFIE
 B: WORK WENT DOWN RATHER
 C: FLAT TODAY I AM
 D: DREADFULLY TIRED TO
 E: NIGHT IVE BEEN SETTING
 F: BUTTONS ON SO AS TO
 G: MAKE MY CLOTHES
 H: HANG ON HOW SHOULD
 I: YOU LIKE THAT JOB
 J: I AM A LOVESICK COON
 K: WORSE THAN EVER I WAS
 L: BEFORE -- CUCKOO
```

Normalised English (punctuation, capitals and apostrophes are editorial; the stray dot is omitted; TO|NIGHT is the period spelling *to-night*):

**Monday. Sweetheart wifie, work went down rather flat today. I am dreadfully tired to-night; I've been setting buttons on so as to make my clothes hang on. How should you like that job? I am a lovesick coon, worse than ever I was before. — Cuckoo**

Slovak translation:

**Pondelok. Miláčik, ženuška, práca dnes išla dosť bez nálady. Dnes večer som strašne unavený; prišíval som si gombíky, aby mi šaty držali pokope. Ako by sa ti páčila taká robota? Som zaľúbený až po uši (doslova „zaľúbený coon“), horšie než kedykoľvek predtým. — Kukučka**

Notes on the reading:

- **"Sweetheart wifie"**: *wifie* is an affectionate diminutive of *wife*; between sweethearts it does not prove the two were married.
- **"setting buttons on"**: sewing buttons on so that his clothes "hang on" (hold together), the mending of a young man living away from home.
- **"COON"**: around 1905 the word was common in the titles and lyrics of music-hall "coon songs", which used phrases of the "lovesick coon" type. The writer applies it to himself as jocular slang for a lovesick fellow. Today it is a racial slur. It is given literally because it is what the Morse says.
- **"Cuckoo"**: the sign-off after the flourish, presumably the writer's pet name; he is not otherwise identified.
- **Date**: 20 June 1905 (portal date) was a Tuesday, so "MONDAY" fits a note written on Monday 19 June and posted at Tooting at 9 am the next morning.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1503/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the two scans and the metadata in source/, decodes the manual transcription in work/transcription.txt with the standard Morse alphabet, and prints the thirteen lines and the running text. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

- **Three letters are supported by context rather than by the pixels alone.** In each case the other possible element count gives no word:
  - the **H of RATHER** (line B) is written as one merged blob about 15 px wide, read as four dots (three would give "RATSER");
  - the **G of SETTING** (line E) is a heavy blot on the printed centre rule followed by a dot; one dash cannot be told from two merged dashes there (one dash would give N, "SETTINN"), so G is restored from context;
  - the **last O of COON** (line J) has its third dash on the printed rule, where its tail cannot be separated from the rule (a dot would give "COGN").
- **Letter grouping.** In a few places a faint separator stroke cannot be told with certainty from a dash tail of a neighbouring line. There the grouping was chosen to give English words: WENT, TODAY, LOVESICK, WORSE, CUCKOO. The dots and dashes themselves are read from the scan.
- **Marks not read as letters:** the isolated tiny dot between SWEETHEART and WIFIE (line A; read as E it would make no sense), a faint grey blob after NIGHT (line E; apparently a failed dot), a short smear on the centre rule after TO (line D), and a tiny dot before the V of EVER (line K; with it the V would be `....-`, not a letter). The pen flourish in line L is punctuation.
- **Line L** is squeezed against the card edge; the B of BEFORE is read as `-...` from the relative tail lengths (the first element is clearly the tallest).
- **Date.** Only "..05" of the postmark year is legible on the scan; the exact day rests on the portal metadata.
- **People.** The writer ("Cuckoo") and Miss Curtis of Laurel House, Riseholme Road, Lincoln are not further identified.
- No search for a prior publication was made beyond the portal status (Not solved, no attachments) and the AI Decipherment Register (no record for this card, checked 2026-10-29).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (hash checks OK, output identical to the claimed plaintext) and decoded the transcription with its own independent Morse decoder (same thirteen lines, every group a valid Morse letter). It checked the transcription against its own 4-8x enlargements of the scan, most lines sign by sign, and judged the text to be natural Edwardian English, consistent with the Tooting postmark, the Edward VII halfpenny stamp and the 1905 date. It confirmed that "Suvtis" is a misreading of "Curtis" and that the earlier GPT work was credited truthfully. Its four findings were minor and are reflected here:

- **Element count.** The write-up had said "about 330" Morse elements; the true count is 484 in 189 letters. Corrected.
- **G of SETTING.** The element count of this letter cannot be decided from the scan; the write-up now states plainly that G is restored from context.
- **Context-supported letters.** The H of RATHER and the last O of COON are now listed with the G of SETTING as context-supported; the write-up no longer claims that every element is read from the pixels.
- **Stray dot in the running text.** The write-up now states that the dot is kept in the diplomatic text and omitted from the normalised English.

No decoded letter changed as a result of the review.

## Credit

Source capture and first triage (Morse identified; MONDAY and SWEETHEART read): OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26. Full transcription, decipherment, decoder script and write-up: Claude Opus 5.5, 2026-10-29/30. Independent review: a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1503, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1503 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4570/conversions/pc_hcp_184_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4569/conversions/pc_hcp_184_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
