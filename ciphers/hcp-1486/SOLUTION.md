# hcp-1486 (pc_hcp_167) - Will to Miss A. Russell, c. 1905

Solver: Claude Opus 5.5 (round 1 handed over 2026-10-29 UTC; review response 2026-10-30 UTC). Earlier work: an OpenAI GPT solver
(2026-10-26) captured the portal page, the two scans and the metadata
(source/, SOURCES.md) and triaged the card as "custom dotted letterlike
correspondence", with no reading. Everything below - transcription, cipher
identification and plaintext - is new.

Portal status when captured: Not solved; no transcription or solution attached.
No published solution of this card was found or used.

## Cipher type and key

**Reversed writing (right-to-left), with null dots** - not a substitution.
Every line is written from right to left with ordinary cursive letters
(letters themselves are NOT mirrored), and dots are scattered between, above
and below the letters as nulls. Read each line from its right end to its left
end, top line first, and ignore the dots.

Because each word is written starting at its right, the writer gives the
**first letter of most words a flourished/odd form**. These are the only
"special" signs; the rest is plain handwriting:

| sign (see work/transcription.txt) | where | value |
|---|---|---|
| T-sign, form 1: crossbar with two short legs (pi-like) | think, this, Tuesday | t, t, T |
| form 2: crossbar with one 3-/z-shaped stem descending below the line | bit, be / hope | **b, b** / **h** (see uncertainties) |
| looped sign with long tail | you (x2) / quite | y / q |
| crossed loop standing alone | x2 | the word "a" |
| loop with descender | are | a |
| w-forms | well, with | w |
| 3-shaped sign | night | n |
| horizontal loop | love | l |
| open loop | Sha | S |
| looped ascender without bar | fright | f |
| "M"-like sign at end of "you" | x2 | u |

The signature `S.W.A.K  Will` is written normally (S.W.A.K. = "Sealed With A Kiss").
The address (Miss A. Russell, Mill House, Bugsell, Etchingham, Sussex)
is in clear.

## Plaintext (English, original)

Line by line (each line read right-to-left):

```
L1  Dont you
L2  think this a
L3  bit of a fright
L4  hope you are ll
L5  quite well Sha
L6  be down Tuesday
L7  night with love
    S.W.A.K.  Will
```

Running text: "Don't you think this a bit of a fright? Hope you are [a]ll quite
well. Sha[ll] be down Tuesday night. With love, S.W.A.K. Will"

(Bracketed letters are NOT on the card; see uncertainties. "this a bit of a
fright" = "consider this a bit of a fright" - presumably the picture side,
a "Language of Flowers / Forget-me-not - True Love" card.)

**Slovak:** „Nezdá sa ti to trochu strašné? Dúfam, že ste všetci celkom
zdraví. Prídem v utorok večer. S láskou, zapečatené bozkom (S.W.A.K.), Will"

## Single command (run from repo root)

```
python3 -I ciphers/hcp-1486/work/decode.py
```

It checks the SHA-256 of the three files in source/, reads
work/transcription.txt (glyphs in visual left-to-right order), drops the null
dots, reverses each line and prints the plaintext above.

## Uncertainties (all disclosed)

1. **The descending-stem sign stands for both b and h.** (Corrected after
   review 1.) There are two crossbar signs, not one: form 1 (two short legs,
   a pi-like capital T) is always t/T (think, this, Tuesday); form 2 (one
   3-/z-shaped stem descending below the line, work/sign-forms.png) is read
   **b** in "bit" and "be" and **h** in "hope". The b/h values of form 2 are
   assigned from context, not from distinct shapes ([B:b]/[B:h] in the
   transcription). Other values give no words ("tit of", "tope").
2. **"ll" (L4)**: literally only "ll" after "are"; almost certainly "all"
   ("hope you are all quite well") with the a omitted by the writer. Not
   restored in the plaintext.
3. **"Sha" (L5) + L6 "be"**: literally "Sha be down". Intended "Shall be".
   The second sign of L6 is a looped letter of height between e and l; read
   "e" (=> "be"). If it is an "l" and the T-sign = l, the reading would be
   "Shall down Tuesday night" - same meaning.
4. "D" of "Dont" is a flourished capital; "Dont" has no apostrophe.
5. Dots: treated as nulls. They are irregular (above, below and between
   letters) and carry no recoverable pattern; not recorded individually.
6. Place name in the address (clear text) reads clearly "Bugsell"; probably
   the hamlet of Bugsell near Hurst Green / Salehurst, a few km from the post
   town Etchingham (not checked against a map in this run).

## Why I believe it is correct

- Eleven words read unambiguously as reversed ordinary handwriting with
  no special sign at all except the initial (think, this, Tuesday, down,
  night, quite, well, with, love, fright, you), and they occur in
  idiomatic, period-appropriate English sentences.
- The whole body (7 lines, every letter) is covered; nothing is left over.
- "Tuesday night", "Hope you are all quite well", "a bit of a fright",
  "With love" and the plain S.W.A.K. sign-off are typical Edwardian British
  postcard phrasing; the card is a halfpenny King Edward VII stamp to Sussex,
  consistent with c. 1905.
- Mirrored versions of the scan were checked: the letters are not mirrored,
  only the order is reversed.

## Response to review 1

Verdict ACCEPT, four minor findings. The reading is unchanged.

1. **Two T-like sign forms (fixed).** Agreed after looking at the reviewer's
   side-by-side panel (copied to work/sign-forms.png) and the body crop
   (work/body.png): in think/this/Tuesday the bar has two short legs; in
   bit/hope/be it has a single 3-shaped stem descending below the line. The
   transcription now uses [T:t] for form 1 and [B:b]/[B:h] for form 2; the key
   table and uncertainty 1 above describe the two forms separately. Re-ran
   `python3 -I ciphers/hcp-1486/work/decode.py`: "source hashes OK" and the
   same seven lines; output identical (ignoring case) to the reviewer's
   independent review/work/indep_output.txt.
2. **"Bugsell [Buxted?]" (fixed).** The address scan reads "Bugsell" clearly;
   the "[Buxted?]" alternative is dropped here and in the report.
   source/metadata.md (earlier capture, "Buxted [reading provisional]") is left
   unchanged as required; the report notes the correction. Location stated as
   probable only.
3. **Dates (fixed).** DONE1 was created 2026-10-29T23:36Z; the header now
   gives UTC dates. The report and register entry use UTC dates
   (FINAL and the register entry: 2026-10-29 per orchestrator instruction for
   the register `submitted` field).
4. **Bracketed restorations (kept).** "[a]ll" and "Sha[ll]" stay bracketed in
   the running text and in the report; the literal lines are printed without
   restoration.
