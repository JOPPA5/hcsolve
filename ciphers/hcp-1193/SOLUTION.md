# HCP 1193 — numbered-Pigpen love postcard to Helen, Kingston NY, December 1906

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1193
(`cpc_1907-12-08_USA_Kingston, NY_USA_New York_`, T. Schrödel collection).
Portal status: **Not solved**; no transcription or solution attached. No
published decipherment of this card was found or used (see SOURCES.md).

**Credit.** The key and the reading of lines 1–11 were established by the
OpenAI GPT solver (GPT-6 Astra/GPT-6.1 Sol session, 2026-10-25; see
`work/transcription.txt`, `work/decode.py`, NOTES.md). On 2026-10-30
Claude Opus 5.5 re-collated every sign against `source/picture-original.jpg`
(enlarged, rotated, contrast-enhanced crops in `work/opus/`), found a missed
word in line 11 (**SO**), and transcribed lines 12–13 for the first time.

## Cipher type and key

Monoalphabetic substitution (MASC), Pigpen family: each letter is one of
the nine cell outlines of a 3×3 grid plus a small written **numeral 1, 2 or 3**
that selects the block A–I, J–R or S–Z. Same alphabet as the dot-count
cards HCP 1131/1189/1190 (which took it over from this card).

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
| top + left | TL | I | R | — (unused 27th cell) |

Word gaps, `,` `.` `?` `-` and a cursive `&` are written in clear.

## Reproduce

From the repository root (checks the SHA-256 of all five source files, then
decodes the symbolic transcription `work/transcription-full.txt`):

```sh
python3 -I ciphers/hcp-1193/work/decode_full.py
```

Output:

```text
{W}ELL HELEN MY <TL3>, I DID
NOT GET THE LETTER I
EXPECTED TONIGHT - WAS
IST LOSDENN MIT DIR? - WELL
SWEETHEART AS I WILL BE
THERE ALMOST AS SOON AS
{T}HIS CARD, I WILL ONLY
{T}ELL YOU HOW MUCH I MISS
YOU & HOW MUCH I WILL
LOVE YOU, TO MAKE UP FOR
IT WHEN I SEE YOU. SO GOOD
{N}IGHT, LOVE & KISSES YOUR
[F/C]ETT[S/J][O/L]C[K/L] ~

223 cipher signs: 4 restored {}, 4 ambiguous [], 1 outside the key <>; ~ = signs under the stamp, not legible.
```

`{x}` = restored sign (stain), `[x/y]` = ambiguous sign (preferred reading
first), `<TL3>` = sign outside the key, `~` = illegible marks under the stamp.

## Plaintext (English, with a German sentence and a German-looking signature)

Clear-text header: *Friday. 9 P.M.* (followed by a short mark, possibly "’06").

> Well Helen my ⟨TL3⟩, I did not get the letter I expected tonight —
> *Was ist los denn mit dir?* — Well sweetheart, as I will be there almost as
> soon as this card, I will only tell you how much I miss you & how much I
> will love you, to make up for it when I see you. So good night, love &
> kisses, your FETTSOCK [signature, literal; see below] …

The German sentence is written as WAS IST LOSDENN MIT DIR (no gap in
LOSDENN); idiomatic German would be *Was ist denn los mit dir?*

## Translations

**English** (German parts translated): Well Helen my [?], I did not get the
letter I expected tonight — what is the matter with you? Well sweetheart, as
I will be there almost as soon as this card, I will only tell you how much I
miss you and how much I will love you to make up for it when I see you. So
good night, love and kisses, your [signature: FETTSOCK, possibly the German
nickname *Fettsack*, "fatso" (an interpretation)].

**Slovak:** Nuž, Helen, moja [?], dnes večer som nedostal list, ktorý som
čakal — čo sa to s tebou deje? Nuž, miláčik, keďže tam budem takmer
súčasne s touto pohľadnicou, napíšem ti len, ako veľmi mi chýbaš a ako
veľmi ťa budem ľúbiť, aby som ti to vynahradil, keď ťa uvidím. Tak dobrú
noc, láska a bozky, tvoj [podpis: FETTSOCK, možno nemecká prezývka
*Fettsack*, „tlstoch“ (interpretácia)].

## Uncertainties (all disclosed)

1. **⟨TL3⟩ after MY (line 1).** A clear top+left outline with numeral 3
   (`work/opus/glyph_q.jpg`): the 27th cell, which has no letter in this
   key. Probably a private sign for an endearment; it is reported literally
   and **not** read as a word.
2. **Restorations in the water stain (left margin).** Four first-of-line
   signs lose their left and/or bottom strokes in the stain; numeral and
   remaining strokes are visible:
   - line 1 `{W}ELL`: numeral 3, box outline faint (`work/opus/f1.jpg`);
     with numeral 3 only S/T/V/W/Y are possible: SELL/TELL/WELL/YELL —
     WELL is chosen from the parallel "WELL SWEETHEART" in line 4, i.e. a
     contextual choice, not a unique-word restoration.
   - line 7 `{T}HIS`: numeral 3 + right stroke; only T gives a word
     (SHIS/VHIS/WHIS/YHIS are not words).
   - line 8 `{T}ELL`: numeral 3 (faint) + right stroke; SELL/WELL/YELL are
     words but do not fit "I will only — you how much I miss you"; TELL is
     a contextual choice.
   - line 12 `{N}IGHT`: top and right strokes and numeral 2 clear, left and
     bottom faint (`work/opus/Q0.jpg`); C2 = N; the only alternative with
     these strokes, TR2 = P, gives PIGHT.
3. **Line 13 (signature) — reported literally.** Preferred reading
   FETTSOCK, with these ambiguities (`work/opus/G12.jpg`, `G34`, `G56`,
   `G78`): sign 1 L1 = F or BL1 = C (its top stroke touches the tail of the
   `&` above); sign 5 BR3 = S (numeral written like the other 3s, but
   loose — BR2 = J not excluded); sign 6 L2 = O or BL2 = L (its "top" may be
   the end of a long underline from line 12); sign 8 B2 = K or BL2 = L
   (right stroke partly under the stamp). The resemblance to German
   *Fettsack* ("fatso", a jocular self-name) is an **interpretation**: the
   pixels show O, not A, in sign 6. Further dark marks under the
   collection stamp to the right (`work/opus/G9.jpg`) may be one or two more
   signs or a flourish; they are not read.
4. **LOSDENN** written as one word; kept literally.
4a. **KISSES, sign 6 (line 12).** The outline is BR, but its numeral is a
   single open hook, not the two-bowled "3" of the neighbouring signs
   (`review/work/k6.jpg`); it could be taken for a "2". BR2 = J gives
   KISSEJ, so S (BR3) is read from the word; the transcription keeps it as
   BR3 with a comment.
5. The cursive `&` (lines 9 and 12) is written in clear, not enciphered.
6. **Date.** The address-side postmark reads KINGSTON N.Y. / DEC 8 / 7 A /
   190[6] (last digit partly covered). The header says "Friday 9 P.M.";
   7 Dec 1906 was a Friday, so the card was written the evening before an
   8 Dec 1906 postmark. The catalogue date 1907-12-08 (a Sunday) is
   probably one year off; this is an observation, not a portal correction.
   Addressee: Mrs. M. R. Rod[?]mond (surname not securely read), Oyster
   Bay, New York; the message addresses her as Helen.

## Why the reading is believed correct

- One fixed 26-letter key decodes all 223 enciphered signs; 214 are read
  directly, 4 are restorations of stain-damaged signs, 4 are ambiguous
  between two letters (signature line), 1 lies outside the key.
- The result is continuous, grammatical, period-plausible English (with one
  German question) over 12 lines: a man telling Helen he will arrive almost
  as soon as the card. Long words (EXPECTED, SWEETHEART, ALMOST, KISSES)
  and repeated phrases (HOW MUCH I) decode consistently.
- The alphabet is the natural 3×3 grid order with numerals for blocks and
  has since decoded three independent sister cards (HCP 1131, 1189, 1190).
- The content fits the card: Kingston-to-Oyster Bay mail, written Friday
  night, postmarked the next morning.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) verdict **ACCEPT**, five minor
findings. Responses by Claude Opus 5.5, 2026-10-30:

1. **KISSES, sign 6, loose numeral.** Agreed; I looked at
   `review/work/k6.jpg`: the numeral is a single hook. Added uncertainty
   item 4a above and a comment in `work/transcription-full.txt`. The token
   stays BR3 (S) because BR2 = J gives no word; the decoded text is unchanged.
2. **NIGHT depends on context.** Already disclosed (uncertainty 2, line 12);
   carried into the report.
3. **Provenance of `source/picture-original.jpg`.** The download URL was not
   recorded by the session that saved it and cannot be reconstructed
   reliably here (no new browsing in this run). The "not recorded" note stays
   in SOURCES.md and is repeated in the report, with the SHA-256 and the
   observation that its content matches `picture-large.jpg`, whose URL is
   recorded.
4. **Fettsack wording.** Fixed: both translations now say "possibly …
   (an interpretation)" / "možno … (interpretácia)".
5. **HistoCrypt PDF not examined.** Agreed; stated in the report as well as
   in SOURCES.md.

Re-ran `python3 -I ciphers/hcp-1193/work/decode_full.py` after the edits:
hashes OK, the same 13 lines and the same count (223 signs, 4 restored,
4 ambiguous, 1 outside the key). The reading is not changed.
