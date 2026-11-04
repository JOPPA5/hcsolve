# HCP 1095: a Morse-code "yes" to Raymond Donaldson, Fultonville, N.Y., 1905

Human solver: Tomáš Pavuk

**Status: deciphered in full (8 Morse lines, 77 letters and 2 question marks); independent review 1 verdict ACCEPT, no change to the decoded letters.** One word, the signature surname WHAL, is uncertain. Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1095 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1095), portal name cpc_1905-06-23_USA_Fultonville, NY_USA_Fultonville, NY_, part of the T. Schrödel collection of cryptographic postcards (private collection; see the HistoCrypt paper linked from the portal, https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When captured on 2026-11-03 the portal listed it as **Not solved**, language Unknown, sender Unknown, recipient Raymond Donaldson, with no transcription or solution attached. A web search for a published reading of this card found nothing.

It is an American "Private Post Card" with a printed view of the **M. E. Church, Fultonville, N.Y.** (Montgomery County, New York State). The address side, in clear plain cursive, reads "Raymond Donaldson, Fultonville, New York." It carries a 1-cent Franklin stamp of the 1902 series and a FULTONVILLE N.Y. postmark of June, 7 AM. The pencil notes "119" and "Box 15" are later collector or dealer marks.

The message side has a plain dateline **June 23-'05  Fultonville N.Y.** (Friday, 23 June 1905), six lines of pen dots and dashes, a plain cursive closing **Yours without a shudd(e)r,** and two more lines of dots and dashes (the signature).

![Picture side: the M. E. Church view, the dateline, eight lines of Morse and the plain closing (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Raymond Donaldson, Fultonville, New York (source/address-large.jpg)](../source/address-large.jpg)

Hidden writing: the stamp box, the picture and all edges of both sides were inspected by the solver and the reviewer; nothing is written around the stamp, in the picture or along the edges. The stamp has not been removed, so what may lie under it cannot be checked from the scans.

## Method

The transcription is **manual**, from the high-resolution original scan (3468 x 2298 px). Every Morse group was read sign by sign on enlarged per-line crops, noting for each mark whether it is a dot, a short dash or a long dash, and measuring gaps between dots where they matter. The writer separates letters with a small comma-like stroke and words with a tall slash, so the letter boundaries are explicit.

A first attempt with International Morse fails at once (DEAR and RAYMOND do not come out). **American Morse** (the original 1844 "railroad" code used on US landline telegraphs) decodes the whole card: its peculiar letters with an internal gap, R `. ..`, O `. .`, Y `.. ..`, C `.. .`, and its long-dash L, appear exactly where the words need them. The decoding is done by a script with a fixed American Morse table; there is no secret parameter.

In review a second agent cropped the scan independently, re-read all eight lines, typed its own American Morse table and decoded with its own script. Its output agrees with the solver's letter for letter.

## Key

Standard American Morse; the writer's conventions:

| Mark on the card | Meaning |
|---|---|
| dot / short dash | Morse dot / dash |
| long dash | American Morse L |
| comma-shaped stroke | end of letter |
| tall slash | end of word |
| curl with a dot below | question mark, written in clear |
| very large dots | emphasis (the word YES) |

American Morse letters occurring on this card: A `.-`, B `-...`, C `.. .`, D `-..`, E `.`, G `--.`, H `....`, I `..`, L (long dash), M `--`, N `-.`, O `. .`, R `. ..`, S `...`, T `-`, W `.--`, Y `.. ..`.

## Ciphertext and plaintext

Transcription, line by line (`,` = letter separator, `/` = word separator, `_` = long dash):

```text
[1] -.. , . , .- , . .. / . .. , .- , .. .. , -- , . . , -. , -.. /
[2] -- , .. .. / .- , -. , ... , .-- , . , . .. / .-- , .... , .- , - /
[3] ... , .... , .- , _ , _ / .. , - / -... , . , ? / ... , .... , .- ,
[4] _ , _ / .. / .- , --. , . .. , . , . / .-- , .. , - ,
[5] .... / - , .... , . , . , ? / - , .... , . , -. / _ , . , - /
[6] .. , - / -... , . / .. .. , . , ... /
[7] .. . , .- , . .. , . . , _ , .. .. , -. , -. /
[8] .-- , .... , .- , _ /
```

Decoded:

```text
[1] DEAR RAYMOND
[2] MY ANSWER WHAT
[3] SHALL IT BE? SHA-
[4] LL I AGREE WIT-
[5] H THEE? THEN LET
[6] IT BE YES
[7] CAROLYNN
[8] WHAL
```

The full card, with the plain parts:

```text
June 23-'05   Fultonville N.Y.
Dear Raymond, my answer - what shall it be?
Shall I agree with thee? Then let it be YES.
Yours without a shudd(e)r,
Carolynn Whal[?].
```

**English** (the original is English): a young woman's playful, rhymed acceptance of a proposal or invitation from Raymond ("what shall it be? / shall I agree with thee? / then let it be yes"), signed "yours without a shudder", i.e. without hesitation.

**Slovak translation:**

```text
23. júna 1905, Fultonville, N.Y.
Drahý Raymond, moja odpoveď - aká má byť?
Mám s tebou súhlasiť? Tak nech je to ÁNO.
Tvoja bez zaváhania (doslova: bez zachvenia),
Carolynn Whal[?].
```

## Uncertainties

1. **Surname WHAL.** After W, four dots are spaced pair, gap, single, gap, single, not evenly like the H in WHAT, WITH and THEE. H is the most economical reading; C followed by E with a missing separator is possible. The final dash is clearly long only with its lighter tail; read as T it would give WHAT, which is not a name, so the final L partly rests on sense. WHAL may be a truncated or abbreviated surname (Whalen?). This is the only uncertain word on the card.
2. **First SHALL (line 3).** Both L dashes are only a little longer than T dashes; L rests on word sense (SHATT is not a word). The other L's (second SHALL, LET, CAROLYNN) are clearly long.
3. **I against O** depends on the gap between two dots; the I of "SHALL I" also rests partly on word sense.
4. **Separators.** In RAYMOND and WITH a slash is overwritten by a heavy blot (read as a corrected letter separator, since the word runs on); in ANSWER a separator lies on an abraded spot.
5. **Question marks.** The curls after BE and THEE are read as written "?"; reading their dot as an extra E gives no text.
6. **"shudd(e)r".** The closing word shows "shudd" and a short "r" squeezed against the right edge; it may be a misspelling "shuddr" or "shudder" written cramped.
7. Nothing can be checked under the stamp.

## Why the reading is correct

- One standard alphabet with no free parameters decodes every Morse group on the card; no sign is left over.
- The American spaced letters and the long-dash L occur exactly where English words need them, which fits a writer in New York State in 1905, where American Morse was the landline code.
- The text is fluent period English, rhymed, addresses the card's recipient (Raymond Donaldson) by his first name, and runs on naturally into the plain closing.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-transcribed all eight lines from its own crops, decoded them with its own script and table, checked the plain parts, the postmark and the stamp box, and gave the verdict **ACCEPT** with five minor findings:

1. The surname WHAL should state that the final L partly rests on sense - now stated (uncertainty 1).
2. The first SHALL rests on word sense - already disclosed, kept.
3. The question marks could formally be read as extra E's - already disclosed, kept.
4. "shuddr" should be shown as "shudd(e)r" rather than a certain misspelling - changed in this report.
5. Register entry: type MASC/Morse and a short role - adopted.

No decoded letter changed as a result of the review.

## Credits

Transcription, identification of American Morse and decipherment by Claude Opus 5.5 (Anthropic); independent review by a separate Claude Opus 5.5 agent. Portal data and scans: HC Portal, T. Schrödel collection.
