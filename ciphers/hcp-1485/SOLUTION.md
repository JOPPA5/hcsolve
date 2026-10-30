# hcp-1485 — Solution (round 1)

Card: HC Portal cryptogram 1485 (`pc_hcp_166`), postcard "A good game for two"
("Pictorial Comedy" series, James Henderson & Sons, London; picture: a courting couple
on a golf course with a golf bag). Address side, in plain script: Miss G. Williams,
"Baronhill", York Road, Colwyn Bay, N. Wales (corrected after review 1; the portal capture in
`source/metadata.md` has the provisional misreading "Bowntree", Oak Road); ½d
Edward VII stamp, 1908 postmark (portal: "around 3.1908"). Signed "Arthur" in plain script.
The portal lists the status "Not solved" and attaches no transcription or solution; no
published solution of this card was found. The decipherment below is my own
(Claude Opus 5.5, 2026-10-29). Earlier triage by the GPT solver (2026-10-26) captured the
sources, made the 180° working image `work/upright.jpg` and noted the geometric glyph
set; it established no key or plaintext.

## Cipher type and key

Monoalphabetic substitution with an invented **stroke alphabet** (homemade, systematic).
English plaintext, word divisions and punctuation kept, a superscript "2" after a glyph
means a doubled letter.

* Consonants: a vertical stem carrying 1–3 short ticks. Three parameters:
  side (L = ticks left of the stem, R = right, X = bars crossing the stem),
  count (1, 2, 3), position (t = ticks on the upper part of the stem, b = lower part).
  The consonants run alphabetically in groups of three:

  | | 1t | 2t | 3t | 1b | 2b | 3b |
  |---|---|---|---|---|---|---|
  | L | B | C | D | F | G | H |
  | R | J* | K | L | M | N | P* |
  | X | Q* | R | S | T | V | W |

  (* = not attested on this card; filled in from the pattern.)
* Vowels and Y are shapes: circle with central dot = A, triangle = E,
  triangle with an inner vertical stroke = I, plain square = O,
  square with a `\` diagonal = U, square with a `/` diagonal = Y. (X, Z not attested.)

Machine-readable key: `work/key.json`. Full glyph transcription: `work/transcription.txt`
(notation explained in its header).

## Plaintext (English, original line breaks)

```
Gwennie darling.
Golf is a good game for
two but I don't think
it beats our game of
"In the Gloaming" (also
for two!) What do you
think dearest? Aren't
you also rather struck
with the "game"? Cariad!!!
I love you Gwennie dear,
A.M.H.L.
Arthur            [plain script]
```

"Cariad" is Welsh for "darling/love" — natural for a card to Colwyn Bay, North Wales.
"In the Gloaming" is the popular Victorian love song (1877), used as a playful euphemism
for courting at dusk.

### English translation

The plaintext is already English; the only non-English word is Welsh *cariad* = "darling, love".

### Slovak translation

Gwennie, miláčik. Golf je dobrá hra pre dvoch, ale nemyslím si, že prekoná našu hru na
„V súmraku" (tiež pre dvoch!). Čo si o tom myslíš, najdrahšia? Nie si aj ty tou „hrou"
dosť uchvátená? Cariad (miláčik)!!! Ľúbim ťa, Gwennie drahá, A.M.H.L. Arthur

## Command

From the repo root:

```
python3 -I ciphers/hcp-1485/work/decode.py
```

It verifies the SHA-256 of the three files in `source/`, then prints the literal
decipherment of `work/transcription.txt` with `work/key.json`, and the reading with the
three writer's slips marked (`intended{literal}`). Exit code 0 = hashes OK.

## Uncertainties and departures from the literal glyphs

1. **Three writer's slips** (the glyphs are clear on the pixels; the plaintext corrects them):
   * line 3 `B□T` literally "BOT" → **but**: U written as a plain square (no diagonal);
   * line 6 `YO□` literally "YOO" → **you**: same omission (compare "YOU" with the `\`
     square on lines 8 and 10, and "OUR", "STRUCK");
   * line 4 literally "CAME" → **game**: the first glyph has its two left ticks high on the
     stem (= C) instead of low (= G, as in "game" on lines 2 and 9).
   No other emendation or restoration was needed; no glyph is hidden.
2. **Closing initials "A.M.H.L."** are deciphered literally (A = circle-dot, M = R1b,
   H = L3b, L = R3t). Their meaning is not established (perhaps Arthur's initials, or a
   lovers' abbreviation); reported as read.
3. The scan is only 1024 px wide, so tick counts are 2–4 px features. Each count was
   checked on 9–16× enlargements; every count agrees with the key except the slip in (1).
   The faint stem of the very first glyph (G of "Gwennie") is pale, but its two low-left
   ticks are clear.
4. Word divisions in `work/transcription.txt` are partly editorial where the card's spacing
   is tight; they do not affect any letter.
5. Letters J, P, Q, X, Z do not occur; their glyphs in the table are inferred.
6. Address reading "Miss G. Williams" (portal: "J. Willams") — the deciphered "Gwennie"
   supports the initial G. House and street read "Baronhill", York Road (see Response to review 1); irrelevant to the cipher.

## Why this is correct

* The key is fully systematic (alphabetical consonants in a 3 × 3 × 2 stroke grid, vowels
  as shapes) and was derived from a handful of words, then predicted every other glyph.
* The whole ciphertext (≈ 175 letters, 10 lines + initials) decodes to fluent, period
  English with no unexplained residue; only the three disclosed slips deviate.
* Content agrees with the context independently: the picture caption "A good game for
  two" and the golf scene ("Golf is a good game for two"), the Welsh destination
  ("Cariad"), the addressee's initial G ("Gwennie"), the plain signature "Arthur", and the
  1908 date (the song "In the Gloaming").

## Response to review 1

Review 1 (separate Claude Opus 5.5 agent, 2026-10-30): verdict **ACCEPT**, four minor findings.
No decoded letter changes. `python3 -I ciphers/hcp-1485/work/decode.py` was re-run after the
edits below: all three SHA-256 checks OK, exit code 0, literal and reading output unchanged.

1. **Address misread — fixed.** On the unrotated address side (`review/work/address.png`) the
   house name and street read `"Baronhill"` and `York Road` (the B-o-r-o-n-h-i-l-l loops and
   the capital Y of York are clear; the portal-capture reading "Bowntree"/"Oak Road" was
   wrong). This agrees with the independent reading of sister card hcp-1484 ("Baron Hill",
   York Road). Corrected in the card description at the top and in uncertainty 6;
   `source/metadata.md` is left untouched as the original capture. The cipher is unaffected.
2. **Sister card as corroboration — accepted.** hcp-1484 (pc_hcp_165, same addressee and
   address, same "Pictorial Comedy" series, 30 Jan 1908) was deciphered independently on
   2026-10-29 with the same construction: stems with 1-3 bars, left/right/both sides,
   bars at top/bottom, consonants B C D / F G H / J K L / M N P / Q R S / T V W, and vowels
   A E I O U Y as dotted circle, triangle, triangle with stroke, square, square with one
   diagonal, square with a second diagonal form. Its `work/key.json` maps to the same
   letters as ours glyph for glyph (Lt1=B … Bb3=W vs our L1t=B … X3b=W). Neither card was
   used to derive the other's key, so the agreement is independent support. Differences:
   hcp-1484 describes Y as "a V from the two top corners", while on this card the Y-square
   shows a stroke from the upper right corner (`/`, e.g. `review/work/yoo2.png`); the two
   descriptions are of the same sign class, distinct from U (`\`). hcp-1484 reports **no**
   U-without-diagonal and no C-for-G slip (its uncertainties are one faint abandoned D and
   three signs overlapped by print), so the three slips here are specific to this card.
   hcp-1484 is signed "your boy", this card "Arthur"; the shared address and system make a
   common sender likely but this is not proved.
3. **Slip classification — no change needed.** BOT, CAME and YOO stay labelled as literal
   glyphs corrected in the reading; `decode.py` prints both the literal text and the reading
   with `intended{literal}` marks, and the report shows the literal forms.
4. **Initials A.M.H.L. — kept unexplained.** Reported literally. A lovers' formula such as
   "all my heart's love" is possible but is only a guess and is labelled as such in the
   report; Arthur's own initials are another possibility. Neither is asserted.
