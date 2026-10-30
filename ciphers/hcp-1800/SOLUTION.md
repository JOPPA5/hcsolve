# HCP 1800 (pc_hcp_481) — numbered-Pigpen postcard to William S. Wilson, Highrock, Pa. (complete reading)

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1800 (name `pc_hcp_481`,
HCPortal cryptographic postcards collection). Portal status: **Not solved**; no
transcription or solution attached (source/metadata.md). No published
decipherment of this card was found or used. The transcription is the solvers'
own (work/transcription.txt), made from `source/picture-large.jpg`.

**Credit.** The sources were captured and the card was first examined by the
OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol session, 2026-10-26), which made
the rotated and enlarged working images in work/ but obtained no stable
transcription or plaintext (NOTES.md). On 2026-10-30 Claude Opus 5.5
identified the system from the sister card HCP 1193, transcribed all 48 signs
from enlarged crops (work/opus/) and decoded them.

## Cipher type and key

Monoalphabetic substitution (MASC), Pigpen family: each letter is one of the
nine cell outlines of a plain 3×3 grid plus a small handwritten **numeral 1, 2
or 3** written inside it, selecting the block A–I, J–R or S–Z. The key is the
same as on HCP 1193 (numerals) and the dot-count cards HCP 1131/1189/1190; it
was carried over as a hypothesis and confirmed by the text, not derived from
this card alone.

| Outline (strokes present) | Token | 1 | 2 | 3 |
|---|---|---|---|---|
| bottom + right | BR | A | J | S |
| bottom + left + right | B | B | K | T |
| bottom + left | BL | C | L | U |
| top + bottom + right | R | D | M | V |
| all four sides | C | E | N | W |
| top + bottom + left | L | F | O | X |
| top + right | TR | G | P | Y |
| top + left + right | T | H | Q | Z |
| top + left | TL | I | R | — |

Letters attested (20): A B C D E F G H I K L M N O P R S T U Y. Word gaps are
left as blank space on the card; there is no punctuation.

## Plaintext (English, two lines as on the card)

```text
YOUR ROCKING CHAIR PLAN LOOKS
SAFER AND MORE COMFORTABLE
```

Punctuated: "Your rocking-chair plan looks safer and more comfortable."

The cipher is written directly under the printed caption "LOVE AT IT'S HEIGHT."
on the picture side, which shows a couple kissing on top of a tall step-ladder;
the message jokes that the recipient's rocking-chair plan is safer and more
comfortable than the ladder.

Slovak: „Tvoj plán s hojdacím kreslom vyzerá bezpečnejšie a pohodlnejšie."

## Reproduce

From the repository root:

```sh
python3 -I ciphers/hcp-1800/work/decode.py
```

It checks the SHA-256 of both scans in `source/`, then decodes the manual
token transcription `work/transcription.txt` with the key above. Output:

```text
source hashes OK
YOUR ROCKING CHAIR PLAN LOOKS
SAFER AND MORE COMFORTABLE
```

The script does not read the image; the pixel-to-token step is manual.

## Uncertainties

1. **Low resolution.** Only the portal's 1024-px "large" scans are available;
   each sign is about 10 px high, and the portal watermark crosses the text.
   Readings were made from 2–6× enlarged, contrast-stretched crops
   (work/opus/t1a–t2c.png, z_*.png, rightend.png).
2. **R in MORE** (line 2, word 3, sign 3, marked `TL2?`): the left stroke and
   the numeral 2 are clear; the top stroke is faint. Top+left+2 = R; no
   one-stroke cell exists in the key, and MORE is the only word.
3. **M in COMFORTABLE** (line 2, word 4, sign 3, marked `R2?`): the outline
   (top+bottom+right) is clear; the numeral is blotted and could be taken for
   a 3 (giving V, "COVFORTABLE"); the independent reviewer reads it as
   closer to 3. M is therefore fixed by context (the word COMFORTABLE),
   not by the pixels.
4. **First R of ROCKING** (TL2) and **P of PLAN** (TR2): the base of the
   numeral 2 sits low in the cell and can look like a bottom stroke; read by
   the stroke ends, top+left and top+right respectively. Alternatives
   (O, or M/J) give no word.
5. **K and S in LOOKS** (line 1, word 5, signs 4–5): outlines B and BR are
   clear, but K's numeral (2) is indistinct and the final S's numeral (3) is
   faint against the right edge; both numerals are context-supported.
6. The last sign of line 1 (S of LOOKS) stands close to the right edge of the
   card but is whole; nothing appears to be cut off.
7. No cipher text on the address side. The pencil note "30- SECRET CODE" in
   the top left corner of the address side is a later dealer/collector note.
   The sender is not named; the date is unknown (the stamp is a 2-cent
   Washington of the 1903 series; the address side is a divided back
   ("This space may be used for correspondence"), allowed in US mail only
   from 1 March 1907, so c. 1907–1910 is likely but not established). A faint
   circular postmark left of the stamp shows only "...ORK"; town and date
   are illegible. The card was printed by the Douglass Post-Card Co.,
   27 N. 10th St., Philadelphia.

No sign was restored or guessed; every one of the 48 letters has a readable
outline; the R of MORE (weak top stroke) and the numerals of M, K and S are
fixed by context rather than by the pixels, as listed.

## Why this is correct

One fixed, previously attested key decodes all 48 signs into nine ordinary
English words with no leftover signs; repeated letters keep their sign
throughout (O = L2 seven times, R = TL2 six times, A = BR1 five times,
C = BL1 three times, E = C1 three times, L = BL2 three times). The message
fits the printed picture (a ladder kiss, "Love at its height") exactly.

## Response to review 1

Review 1 verdict: ACCEPT, four minor findings. All are accepted; none
changes a letter of the reading. Re-run after the edits:
`python3 -I ciphers/hcp-1800/work/decode.py` still prints `source hashes OK`,
`YOUR ROCKING CHAIR PLAN LOOKS`, `SAFER AND MORE COMFORTABLE`.

1. **Sign count (fixed).** The transcription has 48 tokens
   (4+7+5+4+5 + 5+3+4+11); "47" was a counting slip. Corrected to 48
   throughout.
2. **Statistics (fixed).** Recounted from the plaintext with a script:
   R = TL2 six times, A = BR1 five times; U (BL3, in YOUR) was missing from
   the attested list, which now has 20 letters. Corrected in "Key" and
   "Why this is correct".
3. **Context-fixed letters (fixed).** I re-examined review/work/z_m.png:
   the numeral in M of COMFORTABLE does look more like a 3. Uncertainty 3
   now says plainly that M is fixed by the word, not the pixels. The
   numerals of K and S in LOOKS are added as uncertainty 5; the closing
   sentence of "Uncertainties" now names R (MORE), M, K and S as
   context-supported.
4. **Dating (fixed).** Checked on source/address-large.jpg: the back is
   divided ("This space may be used for correspondence"), the stamp is the
   2-cent Washington of 1903, the printer is Douglass Post-Card Co.,
   Philadelphia, and a faint postmark left of the stamp shows only
   "...ORK". Uncertainty 7 now gives c. 1907–1910 (divided backs allowed
   in US mail from 1 March 1907) and mentions the postmark.
