# HCP 1503 (pc_hcp_184): Morse love note to Miss Curtis, Lincoln, June 1905

**Status: complete reading of all the cipher text on the card. A few small residual points are disclosed below. Review 1: ACCEPT (four minor findings, addressed below; no letter changed).**

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1503. When it was captured on 2026-10-26 the portal showed *Not solved*, with no transcription or solution attached. I found no published solution of this card. The orchestrator checked the AI register on 2026-10-29 and found no record for it.

## Credit

- Source capture (both scans, `source/metadata.md`, `SOURCES.md`) and a first triage on 2026-10-26: OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol). The triage identified the script as Morse code and read the heading as MONDAY and the first word as SWEETHEART. It stopped there and claimed no body text (see NOTES.md).
- Full transcription of the 13 lines, segmentation, decoding, decoder script and this write-up: Claude Opus 5.5, 2026-10-29/30. The transcription is my own manual reading of enlarged crops of `source/address-large.jpg`. The portal supplied none.

## The card

The address side is a British halfpenny postcard: M. Ettlinger & Co., *The Royal Series*, Sunset Series No. 4397. It is postmarked TOOTING S.W., 9 AM, ..05. The portal date is 20 June 1905. It is addressed in clear to *Miss Curtis, Laurel House, Riseholme Rd, Lincoln*. The portal catalogue reads the recipient as "Suvtis", which is a misreading of "Curtis". The message fills the left half in Morse code: a heading plus 12 lines. The picture side is a painted sunset with a ship and has no cipher text.

## Cipher type and key

**Type:** International (Continental) Morse code, written with pen and ink.

- **Dash:** an ink blob with a tall upward tail.
- **Dot:** an ink blob with no tail or only a short one.
- **Letter separator:** after each letter the writer adds a small slanted comma-like stroke, set below the line and down to the left.
- **Word separator:** a wider gap between letters.

On the cramped last line the separators shrink to small low dots. There is no further encipherment, and the key is the standard Morse alphabet in `work/decode.py`.

## Transcription

The transcription is in `work/transcription.txt`. Each line of the card has its own entry, letters are separated by spaces and words by `/`.

## Single command (run from the repository root)

```
python3 -I ciphers/hcp-1503/work/decode.py
```

The script checks the SHA-256 hashes of the three files in `source/`, decodes every line, and prints the text line by line and as one running text.

## Plaintext (as decoded, line by line)

```
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

Here `(.)` is an isolated tiny dot that I do not read as a letter, and `--` is the writer's horizontal pen flourish. Both are kept in this diplomatic (line-by-line) output; the stray dot is omitted from the normalised English below.

**Normalised English:** "Monday. Sweetheart wifie, work went down rather flat today. I am dreadfully tired tonight; I've been setting buttons on so as to make my clothes hang on. How should you like that job? I am a lovesick coon, worse than ever I was before. — Cuckoo"

The Morse has no punctuation or apostrophes. "TO NIGHT" runs across a line break and is the period spelling *to-night*. "IVE" is *I've*.

**Slovak translation:** „Pondelok. Miláčik, ženuška, práca dnes išla dosť ťažko / bez nálady. Dnes večer som strašne unavený; prišíval som si gombíky, aby mi šaty držali pokope. Ako by sa ti páčila taká robota? Som zaľúbený až po uši (doslova „zaľúbený coon“, pozri nižšie), horšie než kedykoľvek predtým. — Kukučka“

**Note on "COON":** in 1905 this word was common in the titles and lyrics of music-hall "coon songs" ("lovesick coon" style phrases). Today it is a racial slur. Here the writer uses it about himself as jocular slang for a lovesick fellow. It is given literally because it is what the Morse says.

## Uncertainties (all disclosed)

1. **Line A, x≈313:** between SWEETHEART and WIFIE there is a very small round dot, raised and without a tail. Its letter separator is unclear. I treat it as a stray mark or punctuation, not as a letter. If it were read as E, the text would be "SWEETHEART E WIFIE", which makes no sense.
2. **Line B, RATHER (H):** the four dots of H are written as one blob about 15 px wide, at x 495–509. The middle part is double-width. I count 4 dots, which gives RATHER. A count of 3 would give "RATSER", which is not a word. The following E sits on the printed centre rule (x≈513). The ink there is visibly darker than the rule, which I checked pixel by pixel.
3. **Line E, x≈103:** a very faint grey blob after the N of NIGHT. It looks like an erased or failed dot and I do not read it.
4. **Line E, SETTING (final G):** the last letter is a large blot on the centre rule (x≈514), followed by a dot (x≈521). The scan does not show whether the blot is one dash or two merged dashes: as one dash the letter would be `-.` (N, "SETTINN"), as two it is `--.` (G). The element count of this letter is therefore **not decidable from the pixels**; G is restored from context (SETTING). Separator strokes are clearly visible after S, E and both Ts.
5. **Line D, x≈513:** a short horizontal smear on the centre rule after "TO". I treat it as a stray mark or punctuation, not a letter.
6. **Line J, COON:** the third dash of the second O (x≈513) lies on the printed rule. Its blob is darker than the rule, but its tail cannot be told apart from the rule line. A dot would give "COGN", which is not a word. The C before it (`-.-.`) has a medium-length tail on its third element, and C is the only reading that fits.
7. **Line K, x≈343:** a tiny dot before the V of EVER is not read as an element. With it, the V would be `....-`, which is not a letter.
8. **Line L (cramped bottom line):** the tails of the dots in B (BEFORE) are medium length because the line is squeezed against the card edge. I read `-...` (B) from the relative lengths: the first element is clearly the tallest.
9. **Segmentation:** the separator strokes are faint in places. In a few spots, a separator stroke could not be told with certainty from the tail of a mark on a neighbouring line. In those spots I chose the letter boundaries that give English words: WENT (B), TODAY (C), LOVESICK (J), WORSE (K), CUCKOO (L). In every case the dots and dashes themselves are read from the pixels. Only the grouping was chosen.
10. **Signature "CUCKOO":** this is clearly the sign-off after the flourish, presumably a pet name. The writer is not otherwise identified.
11. The year on the postmark is only partly legible ("..05"). The exact day comes from the portal metadata, 1905-06-20, a Tuesday. "MONDAY" therefore probably means the note was written on Monday, 19 June 1905.

## Why I believe it is correct

- **Coverage:** every mark on the address side's message area is accounted for. That is 13 lines, 189 letters and 484 Morse elements, all decoded with the plain standard Morse alphabet and no adjustments. The only marks not read as letters are the items above (1, 3, 5, 7) and the flourish. Three letters are **context-supported rather than pixel-certain**: the H of RATHER (merged 4-dot blob, item 2), the G of SETTING (blot on the rule, item 4) and the last O of COON (third dash on the rule, item 6); in each case the alternative element count gives no word. The letter grouping at the spots in item 9 is also chosen by context. All other elements are read from the pixels.
- **Coherence:** the decoded text is fluent, idiomatic Edwardian English, with grammar that runs across line breaks (TO|NIGHT, SO AS TO | MAKE MY CLOTHES | HANG ON, HOW SHOULD | YOU LIKE THAT JOB). Forcing words onto noise could not produce this.
- **Context:** it fits a love-letter postcard from Tooting (London) to a young woman in Lincoln: a heading with the weekday, endearments, an account of the day, and a pet-name signature.
- **Independent anchors:** the heading MONDAY has unambiguous separators. The earlier GPT triage arrived at the same opening (MONDAY, SWEETHEART) independently.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave verdict **ACCEPT** with four minor findings. All are accepted; none changes a decoded letter. The reproduction command `python3 -I ciphers/hcp-1503/work/decode.py` was re-run after the edits: the three SHA-256 checks are OK and the output is unchanged (13 lines, HD + A..L).

1. **Element count (minor) – fixed.** Recounted from `work/transcription.txt` with a one-line script: 189 Morse letters, 484 elements (the reviewer's figure). The "about 330" in the Coverage paragraph is replaced by these numbers.
2. **SETTING final G (minor) – fixed.** Agreed: at high enlargement the blot at x≈514 on the printed rule is one dark mass, and one dash cannot be told from two merged dashes. Uncertainty 4 now says plainly that the element count is not decidable from the scan and that G (rather than N, "SETTINN") is restored from context.
3. **RATHER H and COON last O (minor) – fixed.** The Coverage paragraph no longer says all elements are read from the pixels; it lists these two letters and the G of SETTING as context-supported, and notes that the grouping in item 9 is chosen by context.
4. **`(.)` in the running text (minor) – fixed.** A sentence under the line-by-line plaintext now states that the stray dot and the flourish are kept in the diplomatic output and that the dot is omitted from the normalised English. The decoder output itself is left unchanged as the diplomatic transcription.
