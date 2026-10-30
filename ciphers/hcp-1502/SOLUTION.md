# HCP 1502 / pc_hcp_183 - Morse code love letter to "Nell", 10 May 1911

**Status: complete reading of all Morse on the card (233 letters); review 1 verdict ACCEPT, reading unchanged.**
Residual points (all small and disclosed below): the two dots of one "I" are drawn long,
one K has a point-sized dot, one dash is broken by a pen lift, one letter boundary is
under a cursive stroke, and the signature reads literally GEORGI.

**Credit.** The earlier OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) captured the portal
page on 2026-10-26 (all three tabs, `source/metadata.md`, both scans, `SOURCES.md`) and
identified the dots and dashes as apparent Morse. It made no transcription or plaintext
claim. On 2026-10-29/30 Claude Opus 5.5 read every row on enlarged crops, wrote
`work/transcription.txt` and `work/decode.py`, and made this claim.

**Context.** Portal status "Not solved", no attached transcription or solution. Card dated
in cursive "May 10th 1911"; addressed to Miss O. Davy, Gilberdyke, E. Yorks; halfpenny
Edward VII stamp, Gilberdyke R.S.O. postmarks of May 1911. Picture side: "Natures wild
Beauty" (waterfall in a flower frame), no cipher. I found no published solution of this card.

## Cipher and key

- **Type:** plain International (Continental) Morse code, written in pen. No substitution
  on top of it.
- **Writing conventions:** a Morse dot is a short stroke (about 6-16 px in
  `address-large.jpg`), a dash a long stroke (about 19-39 px); a small point closes each
  letter; a large round ink blot closes each word.
- **Key:** the standard A-Z Morse table (in `work/decode.py`). Only letters occur, plus one
  handwritten "&" sign that is not Morse.
- **Layout:** two blocks on the address side, read left to right, top to bottom.
  Block A (8 rows, top left, beginning beside a cursive "P.S.") is a postscript.
  Block B (24 rows, below the printed "This space may be used for communication") is the
  letter. No rotation is needed.

## Plaintext (English, original; punctuation and case are editorial)

Main letter (block B):

> Dear Nell, just a line as usual. Hope you are not killing yourself this week. It's grand
> weather for the job. Well, sweetheart, I'm longing for Sunday; it seems such a long week.
> Well, so long, dearest, till I see you. With all my love & kisses, yours Georgi[e]

Postscript (block A):

> P.S. Save me one for Sunday. I am ready for one now, Nell.

Raw decoder output:

```
P.S. SAVE ME ONE FOR SUNDAY I AM READY FOR ONE NOW NELL
DEAR NELL JUST A LINE AS USUAL HOPE YOU ARE NOT KILLING YOURSELF THIS WEEK ITS GRAND
WEATHER FOR THE JOB WELL SWEETHEART IM LONGING FOR SUNDAY IT SEEMS SUCH A LONG WEEK WELL
SO LONG DEAREST TILL I SEE YOU WITH ALL MY LOVE & KISSES YOURS GEORGI
```

**Slovak translation:** „Milá Nell, len pár riadkov ako zvyčajne. Dúfam, že sa tento týždeň
neumáraš. Na tú robotu je nádherné počasie. Nuž, zlatko, túžim po nedeli; zdá sa mi to
taký dlhý týždeň. Nuž, maj sa, najdrahšia, kým ťa neuvidím. So všetkou mojou láskou a
bozkami, tvoj Georgi[e].“ — „P.S. Nechaj mi jeden na nedeľu. Na jeden som pripravený
hneď teraz, Nell.“

(English needs no translation; the "one" saved for Sunday is presumably a kiss, which the
card does not say.)

## Transcription and reproduction

`work/transcription.txt` holds every Morse group, one pen row per line, with `/` for the
word-end blots. Single command, run from the repository root:

```
python3 ciphers/hcp-1502/work/decode.py
```

It checks the SHA-256 of the three files in `source/` (`work/source-sha256.json`), decodes
the transcription with the standard table (every group must be a valid letter, or the
script stops with a KeyError) and prints both blocks and the letter count (233).
The other scripts in `work/` (`components.py`, `chain.py`, `rowfit.py`, `segments.py`,
`strips.py`, `rowstrip.py`, `zoom.py`) only made enlarged crops and stroke-length lists
to help the eye; the transcription itself is manual.

## Uncertainties (all disclosed)

1. **ITS (row B375).** The I is written as two strokes of 16 and 19 px, longer than the
   writer's usual dots and close to short dashes; the separation point after them is a
   small heavy blob at x 79-82. Read as `.. - ...` = ITS, which the sentence ("its grand
   weather") requires; `-- - ...` would give no word.
2. **AM (row A135).** The second dash of M is one stroke (x 121-148) with a tiny pen-lift
   gap near x 132; read as one dash. Read as two dots it would be `-.-` (no word).
3. **DEAR NELL (row B222).** No letter-end point is visible between E and the first L,
   where the stroke of "1" in the cursive date "May 10th 1911" crosses the row (x 381-388);
   a point may be hidden under it. The second L begins with a dot that is a heavier blob
   where the pen crossed the printed vertical line (x 455). The same name NELL is
   clearly written in the P.S. (row A167).
4. **KISSES (row B607).** The dot of K is a small point (x 637-640) rather than the usual
   short stroke; read `-.-` = K. The "&" before it is a handwritten non-Morse sign.
5. **Long dots elsewhere.** Several clear dots are 13-17 px (e.g. the four of H in HOPE,
   the three of S in SEE, the last of S in YOURSELF); words fix them unambiguously.
6. **Signature GEORGI (row B632).** The ink is faint; the first dash of G is a stroke
   x 33-43 with a faint continuation to x 52 (about 20 px). The final `..` is followed by
   a word-end blot (about x 400-407, y 638) and then nothing more before the card edge, so
   GEORGI is a complete word as written (presumably Georgie or a nickname); no letter is
   restored. (Corrected after review 1, finding 1.)
7. **Identity.** "Nell" is addressed as the recipient; the card is addressed to Miss O. Davy.
   Whether Nell is her name or a pet name is not stated; nothing on the card links "Nell"
   to the initial O.

## Why I believe it is correct

- Every one of the 233 Morse groups is a valid International Morse letter; there is no
  unreadable group and no restored letter.
- The point/blot conventions are used consistently and give word breaks that match the
  decoded words in every row, including words split over two rows (KIL|LING, Y|OURSELF,
  USU|AL, SUND|AY).
- The text is fluent, idiomatic English of the period ("just a line as usual", "it's grand
  weather for the job", "so long, dearest") and coherent with the card: a Yorkshire love
  letter to "Nell", sent from Gilberdyke in May 1911, with a P.S. that picks up the main
  letter's "longing for Sunday".

## Response to review 1

Verdict ACCEPT, four minor findings. All addressed; no letter of the reading changed.
After the changes `python3 -I ciphers/hcp-1502/work/decode.py` (from the repo root)
prints the same two blocks and "233 Morse letters decoded, all groups valid. Source
hashes OK."

1. **Signature row (blot after GEORGI)** - agreed. On the reviewer's crop
   (`review/work/end1.png`) a round word-end blot clearly follows the final `..` of
   GEORGI. Uncertainty 6 now says so, and row B632 of `work/transcription.txt` now ends
   with ` /` like every other word-final row. Decoded output unchanged.
2. **Non-standard marks not flagged in the transcription** - fixed. `decode.py` now
   ignores text after `#` on a row, and rows A135 (broken M dash), B222 (hidden E|L
   boundary, heavy L dot on the printed line), B375 (long I dots), B593 (heavy first dot
   of the second L of ALL), B607 (point-sized K dot, handwritten "&") and B632 (faint G,
   final blot) carry short comments with the pixel positions.
3. **"Nell" vs Miss O. Davy** - agreed; uncertainty 7 now states that "Nell" may be a pet
   name and that nothing on the card links it to the initial O. The report repeats this.
4. **Row labels and slope** - agreed; the header of `transcription.txt` now says the
   label is the y of the row's left end and that rows slope down about 30 px across the
   card, and rows B593/B607 note that their right halves lie at y 620-640. The report
   explains the same.
