# HCP 1422 / pc_hcp_103 — Ivy to Carl Wieler, Mt. Carmel, Illinois

**Status: complete reading (round 1), handed to review.** Two glyphs under the
postal cancellation are restorations and are marked `[ ]` in the output; everything
else is read from the scan.

## Credit and sources

- Portal page https://crypto.hcportal.eu/dashboard/cryptograms/1422 was read on
  2026-10-26: status **Not solved**, no transcription or solution attached
  (see `SOURCES.md`, `source/metadata.md`). No published solution of this card
  was found or used.
- The key, the glyph-class labels and the first transcript (`work/transcript.txt`,
  `work/decode.py`) are the work of an earlier OpenAI GPT solver session
  (2026-10-26), which left the card partial with two spans under the postmark open.
- Claude Opus 5.5 (2026-10-29/30) re-checked every line on enlarged crops of
  `source/address.jpg`, read the two postmark spans, corrected one omission
  (the word IN before CYNTHIANA, line 9, which the earlier transcript had taken
  as a comma), added two punctuation marks, and wrote `work/transcript_v2.txt`
  and `work/decode_v2.py`.

## Cipher type and key

Simple monoalphabetic substitution (MASC) with invented symbols, written in
English; overlines group the words. The labels are ASCII names for the drawn
shapes (`work/key.json`):

| Label | Shape | Plain |
|---|---|---|
| `:` | two dots side by side | A |
| `2` | curved 2-like stroke | B |
| `//` | two parallel strokes | C |
| `+` | short plus | D |
| `#` | hash / two crossed strokes (sometimes drawn π-like) | E |
| `~` | low m-shaped / wavy stroke | F |
| `.` | single dot | G |
| `i` | stroke with dot above | H |
| `!` | stroke with dot below | I |
| `n` | hooked/arched stroke | K |
| `u` | cup with dot | L |
| `=` | dash with dot above and below (÷-like) | M |
| `-.` | dash followed by dot (dot sometimes comma-like) | N |
| `O` | circle | O |
| `p` | loop with stem | P |
| `,` | comma-shaped stroke | R |
| `v` | v-shaped stroke | S |
| `t` | long cross | T |
| `\` | backslash | U |
| `^` | caret | V |
| `N` | zigzag | W |
| `>` | chevron | Y |

J, Q, X, Z do not occur. The R glyph and the writer's comma are the same shape;
a `,` is taken as punctuation only where it stands outside a word.

## Command

From the repository root:

```
python3 -I ciphers/hcp-1422/work/decode_v2.py
```

It checks the SHA-256 of all three files in `source/`, then decodes
`work/transcript_v2.txt` with `work/key.json`.

## Plaintext (as decoded, line by line of the card)

```
WELL KID HOW IS YOUR
COLD ? HOPE IT IS BETTER
I AM NOT GOING HOME SAT[U]RDAY
AS I HAD A LETTER FROM [H]ER .
AND SHE IS COMING / IF YOU ARE
ABLE , WOULD LIKE TO HAVE YOU BE
IN MT . CARMEL SATURDAY
NIGHT I AM GOING TO MEET
HER IN CYNTHIANA I WOULD
LIKE TO SEE YOU BEFORE THEN
IF YOU COULD COME TO THE
DEPOT I HAVE SOME THING TO TELL
YOU , I HAV SOMETHING REAL
CANADISH FOR YOU IF I DONT
GET TO SEE YOU BEFORE SATURDAY
BE SURE AND BE AT THE CITY
WHEN WE ARRIVE OR ELSE MEET US
AT SKELTON LOVINGLY IVY
```

374 glyphs read, 2 restored.

**Normalised:** Well kid, how is your cold? Hope it is better. I am not going
home Saturday, as I had a letter from her, and she is coming. If you are able,
would like to have you be in Mt. Carmel Saturday night. I am going to meet her in
Cynthiana. I would like to see you before then; if you could come to the depot,
I have something to tell you. I hav[e] something real "Canadish" for you. If I
don't get to see you before Saturday, be sure and be at the city when we arrive,
or else meet us at Skelton. Lovingly, Ivy.

**Slovak:** No, drobec, ako je s tvojou nádchou? Dúfam, že je lepšie. V sobotu
nejdem domov, lebo som dostala list od nej a ona prichádza. Ak budeš môcť, chcela
by som, aby si bol v sobotu večer v Mt. Carmel. Idem sa s ňou stretnúť
v Cynthiane. Rada by som ťa videla ešte predtým; keby si mohol prísť na stanicu,
mám ti niečo povedať. Mám pre teba niečo naozaj „kanadské“ [CANADISH]. Ak sa
s tebou neuvidím pred sobotou, určite buď v meste, keď prídeme, alebo nás stretni
v Skeltone. S láskou Ivy.

(The writer's gender is not stated; the feminine forms follow the name Ivy.)

## Uncertainties

1. **SAT[U]RDAY (line 3).** Under the "FEB 8" of the cancellation the pen glyphs
   S (`v`, over the F), A (two dots inside the E), T (long cross over the B),
   R (comma stroke right of the 8) and D-A-Y (`+ : >`) are visible; the U
   (backslash) is hidden by the stamped "8". SAT_RDAY admits only U. The word
   SATURDAY occurs twice more on the card in clear.
2. **[H]ER (line 4).** The word after FROM is under the time line of the
   cancellation. A vertical pen stroke, the hash-shaped E (`#`) and the
   4-shaped R (`,`) are visible and match HER as written in clear on line 9;
   the dot that distinguishes H (dot above) from I (dot below) is not separable
   from postmark ink (a dark dot below the stroke may be postmark or line-5
   ink). Among the stroke-type glyphs only H gives a word (IER, TER, PER do not
   fit). Restoration of the H, disclosed.
3. **Punctuation.** The dark oval mark at the end of line 4 is read as a full
   stop (not a cipher glyph); the stroke after COMING (line 5) is a separator
   of uncertain kind (shown as `/`); commas after ABLE and YOU and the stop after
   MT are pen marks outside words. None changes the reading.
4. **HAV (line 13)** has no E on the card: a writer's omission, kept literally.
   HAVE is written in full twice elsewhere.
5. **CANADISH (line 14)** is clearly C-A-N-A-D-I-S-H; its meaning (a jocular
   "Canadian-ish" thing?) is unexplained. Not altered.
6. **SKELTON (line 18):** S-K-E-L-T-O-N, with K in the same hooked form as in
   KID/LIKE and E in its π-like form. Probably a place (a rendezvous on the way
   into "the city"); not identified with certainty, not normalised to SHELTON.
7. **IVY** is the signature as decoded; who Ivy is, and who "her" is, is unknown.
8. **Date.** Portal: 1943-02-08. The cancellation reads MT CARMEL ... FEB 8; the
   year digits are too faint to read here. The 1-cent green Washington stamp is
   of the 1908-1920s design; the year is not established by this solution.
9. The image is only 1024 px wide; some glyphs (e.g. dots of `!` vs `i`) are
   2-3 px. Readings were confirmed by consistency across repeated words.

## Why it is correct

- One 22-symbol key decodes all 374 visible glyphs into fluent, grammatical
  1900s-1940s American English with no unused or conflicting symbols.
- Repeated words decode identically in different places: YOU (x7, plus YOUR), SATURDAY
  (x3), HAVE/HAV, GOING (x2), BEFORE (x2), SEE YOU (x2), WOULD (x2).
- The content fits the address: the card is addressed to Mt. Carmel, Illinois,
  and mentions Mt. Carmel and Cynthiana (Posey County, Indiana, about 30 miles
  from Mt. Carmel), a depot and Saturday travel.
- The only non-read material is one glyph in each of two words under the
  postmark, each forced by the visible neighbours.

## Response to review 1

Review 1 verdict: **ACCEPT**, three minor findings. No decoded letter changes; the
reproduction command `python3 -I ciphers/hcp-1422/work/decode_v2.py` was re-run on
2026-10-30 and still prints the 18 lines above ("374 glyphs read ..., 2 restored;
source hashes OK").

1. **Postmark year (minor) – accepted.** On the reviewer's 7-8x crop
   `review/work/year2.png` (x 360-470, y 170-215 of `source/address.jpg`) I also
   see, under the pen writing, a grey stamped 9, a thin 1 and a 3 after a lost first
   digit. Uncertainty 8 is therefore superseded: the cancellation reads
   MT CARMEL ... FEB 8, year **probably 1913** (last three digits seen as 913, the
   first lost under ink). This agrees with the 1-cent green Washington stamp of the
   1908-1922 design and argues against the portal date 1943-02-08. February 8, 1913
   was a Saturday. The date remains a reading of a faint postmark, not certain.
2. **Punctuation (minor) – accepted.** The report states explicitly that `?`, `/`,
   `,` and `.` in the output are the solver's readings of pen marks outside words,
   not cipher letters, and that the `/` after COMING and the stop at the end of
   line 4 are guesses.
3. **CANADISH and SKELTON (minor) – accepted.** The report explains that both words
   are written exactly so on the card (letters confirmed by the reviewer), that
   CANADISH is unexplained (perhaps jocular "Canadian-ish") and that Skelton is
   probably a local place or station near Mt. Carmel / Cynthiana, not identified,
   so that neither is mistaken for a decoding error.
