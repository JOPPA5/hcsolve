# hcp-1456 (pc_hcp_137) – solution, round 1 (with response to review 1)

Postcard "The Old Chorister (2)" (Bamforth), postmarked East Grinstead 6 a.m. 18 March 1905,
addressed to Miss B. Evison, Crown Hotel, Cowden, Kent. All handwriting is on the address
side (`source/address-large.jpg`, read rotated as `work/reading.jpg`); the picture side has
only printed verse. No transcription or solution is attached on the portal; status "Not solved".
No published solution of this card was found. The transcription below is my own (Claude
Opus 5.5, 2026-10-29/30), read from enlarged crops (4–12x); the earlier GPT triage
(2026-10-26) had captured the sources and noted "false spacing / inserted letters" as an
untested possibility but produced no transcription or key.

## Cipher type and key

**Null cipher (letter interleaving), English plaintext.** Every cipher word is
`null null P1 null P2 null P3 ... ` – two dummy letters, then the plaintext letters with one
dummy letter after each. Decryption of each cipher word: `word[2::2]`. There is no
substitution; nulls are arbitrary letters (often n, i, a, r, h). The writer's word
divisions are kept except that a few cipher words are split by a line break or a space
(`tem|deraen` = mean, `gnpalae|hnatay` = plenty, `zah|iazrirry` = Harry, `zi|tioa` = to,
`thmia znioar` = Manor, `th-|tohaias` = this), and some cipher words cover two plain words
(`ariratm` = "I am", `nifaohrad` + `thmia znioar` = Ford Manor). Even-length words end in a
trailing null (e.g. `zitioa`, `rahaerrae`), which the same rule handles.

## Transcription (`work/transcription.txt`)

```
Nitchuavnikes nifaoyr tiyhoauir
nawkhiart nadio riyaoru tem=
deraen . ranao prsrtiarmkt
ariratm nothono hiliarthe
rafiour natrhoe nimuanial
rathornaihgrhat nagiort
pahaormae raforoorm nawhoarak
hiart zinaianhe hablcalaorcak . gnpalae=
hnatay raouf hawaohrak niarbioaurt
rahaerrae . rawhornadaekr nawrhiy zah=
iazrirry nadiornat ziwhraiatae zi=
tioa yamae . nahiarvae nabseaetn
hoart nifaohrad thmia+znioar th-
tohaias niwaeaeok ? nikhirnrd
yaraehgiakrades kitao hiatlil
nimraibreal . rebaeiart . niahninaiae      [Ewtt]
```

## Plaintext (English, original)

Raw decode (one group per cipher word):
`thanks for your what do you mean . no stamt iam too late for the mail tonight got home
from work at nine bclock . plenty of work about here . wonder why harry dont write to me .
have been at ford manor this week ? kind regards to all mabel . beat . annie`

Read:

> Thanks for your … What do you mean. No stamt [stamp?]; I am too late for the mail
> tonight. Got home from work at nine o'clock. Plenty of work about here. [I] wonder why
> Harry don't write to me. Have [you] been at Ford Manor this week? Kind regards to all.
> Mabel. Beat. Annie.

**English translation:** same as above (the plaintext is English).

**Slovak translation:** Ďakujem za tvoj(u) … Čo tým myslíš. Žiadna známka(?); dnes večer
už nestihnem poštu. Prišla som domov z práce o deviatej. Je tu veľa roboty. Čudujem sa,
prečo mi Harry nepíše. Bola si tento týždeň vo Ford Manor? Srdečné pozdravy všetkým.
Mabel. Beat. Annie.

## Command

From the repo root:

```
python3 -I ciphers/hcp-1456/work/decode.py
```

It checks the SHA-256 of the three files in `source/`, joins the split cipher words of
`work/transcription.txt`, applies `word[2::2]` to every cipher word, prints the raw decode,
asserts it equals the expected letter string, and prints the readable plaintext.

## Uncertainties (all disclosed)

1. **`prsrtiarmkt` → "stamt".** Read letter by letter at 10x: p r s r t i a r m k t; the
   rule gives s-t-a-m-t, not a word. Likely "stamp" (writer's slip for the last plain
   letter) or less likely "start"; the 5th letter could also be read k/h. Left as decoded.
2. **`hablcalaorcak` → "bclock", read as "o'clock".** The third letter is a tall-loop form
   that I read as b; "o'clock" needs an o there (the form may be a looped o/"lo"). A stroke
   that looks like the descender of a p at position 9 is the ascender of the final k of
   `hawaohrak` in the line below (corrected after review 1); the letter itself is o, supported
   both by its bowl shape and by the context "o'clock".
3. **"Thanks for your …"** – no noun follows "your" (`tiyhoauir`, final r has a line-end
   descender flourish); the writer seems to have omitted "card/letter". "[I] wonder" and
   "Have [you] been" likewise lack the pronoun in the cipher.
4. **`rathornaihgrhat` (tonight):** the 3rd letter is a short uncrossed t (could be taken for
   s); the 13th is h (not k).
5. **Overwritten letters:** `rahaerrae`, `iazrirry`, `yamae`, `hoart` are partly retraced
   or blotted in darker ink and crossed by the y-descender of `hnatay`; the plain letters
   (h-e-r-e, -a-r-r-y, m-e, a-t) are legible, some nulls (e.g. `hoart`/`hiart`) are not
   certain but do not affect the plaintext.
6. **Line order of lines 7–8:** lines slope strongly; "pahaormae" sits above "hiart
   zinaianhe". Order chosen by baseline continuity: "got home from work at nine o'clock"
   (the alternative "got home at nine o'clock from work" has the same meaning).
7. **Names:** "Beat" (`rebaeiart`, b-e-a-t; probably short for Beatrice – the addressee is
   Miss B. Evison, so this may be the recipient rather than a co-sender) and "Annie"
   (`niahninaiae`). Small x-shaped marks stand over letters in `nimraibreal`,
   `rebaeiart`, `niahninaiae` (two stacked over the last); they are probably the
   conventional postcard kisses (corrected after review 1) and are ignored. The closing
   names may be three signatures or the persons greeted ("regards to all – Mabel, Beat,
   Annie"); the sender is not known.
8. **`Ewtt`** after the last word: written in a different, larger style, not decodable by
   the rule (would give a single t); reported literally as an unenciphered flourish or
   initials.
9. Null letters (e.g. initial `N`/`K` of the first word, `nawkhiart` read with or without an
   i) are sometimes uncertain but never change the plaintext.

## Why I believe it is correct

- One fixed rule (`word[2::2]`) applied to all 49 cipher words (after joining split words) yields grammatical,
  colloquial English of 1905 with no exception except the two letters in items 1–2.
- Long words decode exactly: `yaraehgiakrades` → regards, `rawhornadaekr` → wonder,
  `rathornaihgrhat` → tonight, `ziwhraiatae` → write, `niarbioaurt` → about,
  `Nitchuavnikes` → thanks.
- Context fits: the card was posted at East Grinstead to Cowden, Kent; Ford Manor
  (Dormansland/Lingfield) lies a few miles from both. "Too late for the mail tonight"
  fits the 6 a.m. postmark.
- The writer's punctuation (`.` and `?`) falls at sentence ends in the decoded text, e.g.
  the `?` after "this week".

## Response to review 1

Verdict ACCEPT (reviewer Claude Opus 5.5). All five findings are minor; none changes the
decoded text. Re-ran `python3 -I ciphers/hcp-1456/work/decode.py` after the fixes: hashes OK,
assertion passes, output unchanged.

1. **Index-8 letter of `hablcalaorcak`.** Agreed. On the reviewer's 8x crop
   (`review/work/oclock3.png`) the descender-like stroke runs into the ascender of the final
   **k** of `hawaohrak`, not the h. Uncertainty item 2 corrected; the letter remains o
   (bowl shape and context).
2. **Marks over the last line.** Agreed. On `review/work/last.png` they are small x-crosses
   (two stacked over `niahninaiae`), probably postcard kisses. Item 7 now says so.
   Plaintext-neutral. `Ewtt` stays unexplained.
3. **Closing names.** Agreed. Item 7 now gives both readings (three signatures, or persons
   greeted) and states that the sender is not known; the report presents both.
4. **`for d manor` in decode.py.** Fixed to `ford manor` in `work/decode.py`; the
   comparison was on letters only, so behaviour is unchanged.
5. **"your" at line end.** No change needed; reviewer agrees r is the natural reading and
   the missing noun is disclosed (item 3).
