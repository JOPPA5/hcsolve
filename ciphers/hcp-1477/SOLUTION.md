# HCP 1477 / pc_hcp_158 — Rommehed (St. Tuna) postcard to Sara Erickson, 9 May 1904

**Status: review 1 ACCEPT; closed (FINAL) after the response below.** Every one of the 143 cipher signs is read from
the scan and decoded with one consistent key. One phrase in line 7 of the verse
(`ging sbät`) decodes letter by letter but its meaning is not established; it is
reported literally, not repaired (see Uncertainties).

## Credit and sources

- Portal page https://crypto.hcportal.eu/dashboard/cryptograms/1477, captured
  2026-10-26 (`source/metadata.md`, `SOURCES.md`): status **Not solved**, no
  transcription or solution attached. No published solution of this card was found;
  two web searches (2026-10-29) for the decoded verse lines found no source text.
- Setup (download of scans and metadata) and a triage note were done by an earlier
  OpenAI GPT solver session (2026-10-26), which left the card unread.
- Transcription, key, decipherment and these files: Claude Opus 5.5, 2026-10-29.

## Where the cipher is

The narrow right margin of the picture side (`source/picture-large.jpg`, x≈870–975),
four lines written with the card turned 90° clockwise; read with the card in that
position, top line first. The other writing on the card (verse beside the picture,
"Rommehed den 9/5 04. Många kära hälsningar...", left margin) is plain Swedish and not
part of the cipher. The address side has no cipher.

## Cipher type and key

Partial substitution ("vowels in clear"): vowels are written normally (å with a dot,
ä/ö with a small 2/^-shaped mark; y is written as i), consonants are replaced by
signs. The consonants b–l use their position in the consonant row
b c d f g h j k l (b=1, d=3, g=5, h=6, k=8, l=9; c, f, j not used); the later ones
have ad-hoc signs:

| Sign | Letter | | Sign | Letter |
|---|---|---|---|---|
| 1 | b | | – · (dash then dot) | m |
| 3 | d | | : (two dots) | n |
| 5 (also a heavy closed б-like 5) | g | | ⁝ (three dots) | p |
| 6 | h | | X | r |
| 8 (sometimes drawn g-like) | k | | ÷ (dash, dot above and below) | s |
| 9 | l | | dash with dot below | t |
| | | | X with dot above | v |

Files: `work/transcription.txt` (sign labels, legend at the top), `work/key.json`,
`work/decode.py`.

## Command (from the repository root)

```
python3 -I ciphers/hcp-1477/work/decode.py
```

It checks the SHA-256 of the three files in `source/`, then prints:

```
har du ingen vän i värden den du trikt kan
lita nå litet ödslig blir då härden men var
glad ändå. vänskap brites bandet brister knits
igen ingen ging sbät man mister som en vän.
[143 signs decoded, 4 lines]
```

## Plaintext (Swedish)

Literal decryption above. Laid out as the verse it is (trochaic, rhymes
världen/härden, på/ändå, brister/mister, igen/vän), with the writer's spellings
normalised in brackets:

```
Har du ingen vän i värden [världen],
den du trikt [tryggt; or trigt] kan lita nå [på],
litet ödslig blir då härden,
men var glad ändå.
Vänskap brites [brytes], bandet brister,
knits [knytes] igen,
ingen ging sbät [?] man mister
som en vän.
```

**English:** "Have you no friend in the world whom you can safely rely on — the
hearth becomes a little desolate then; but be glad all the same. Friendship is
broken, the bond bursts, is tied again; [line 7 not understood: 'ingen ging sbät']
one loses … as a friend."

**Slovak:** „Nemáš na svete priateľa, na ktorého sa môžeš pevne spoľahnúť — trochu
pusté je potom ohnisko (domov); ale buď aj tak veselá. Priateľstvo sa láme, puto
praská, znova sa zaväzuje; [7. riadok nezrozumiteľný: „ingen ging sbät“] človek stráca …
ako priateľa.“

## Uncertainties

1. **Line 7, `ingen ging sbät`** (signs `i:5e: Gi:5 S1äT`). Every sign is clear on the
   scan and decodes as shown, but the words make no sense as written. Metre and
   sense suggest something like *ingenting så lätt man mister* ("nothing does one
   lose as easily"), which would need G = t and `S1äT` = "så lätt" (missing å, 1 for
   l) — two writer errors. This is a conjecture only; it is not adopted.
2. `värden` (line 1): no l sign between r and d; read as the writer's spelling of
   *världen* (rhyme with *härden* confirms the word).
3. `trikt` (line 1): *tryggt* expected. Writer uses i for y throughout (trikt, brites,
   knits). The second consonant is the tall g-like glyph (see 5); read as g the word is
   *trigt*, which is closer to *tryggt*. *trikt* and *trigt* are equal alternatives.
4. `ö` in *ödslig* (line 2): the vowel is a dark round blob with the 2-mark; read as
   ö (the same mark the writer puts on ä).
5. **One glyph, two values chosen by context.** A tall g-like glyph with a descender
   occurs three times: in *trikt/trigt* (line 1), *vänskap* (line 3) and *igen*
   (line 4, first word). It looks the same in all three and differs from the plain 8
   of *kan* and *knits* and the plain 5 of *ingen*. It is transcribed as 8 (k) in
   *trikt* and *vänskap* and as 5 (g) in *igen*, by context only; the scan does not
   separate the two values.
8. **`nå` for *på* (line 2).** The sign before å is written with two dots (n), not the
   three dots of p (compare *vänskap*). The transcription keeps the two dots, so the
   literal output is *nå*; *lita på* is certain from sense and the rhyme på/ändå, so it
   is read as a writer slip for p.
6. The heavy closed б-sign is taken as a variant of 5 = g (*glad*, line 3); in line 7
   it gives *ging* (see 1).
7. Word division and line layout of the verse are editorial; the writer's ":" is the
   letter n, not a separator (ingen, den, kan, ändå, men, en, vän).

## Why this is believed correct

- One key covers all 143 signs with no unread sign; 33 of 35 words are ordinary
  Swedish words (or transparent spellings of them).
- Independent confirmation of each consonant: d (du, då, den, bandet), g (ingen,
  igen, glad, ödslig), k (kan, vänskap, knits), l (lita, litet, blir, glad),
  m (men, man, mister, som), n (ingen, den, vän, ändå), r (har, blir, var, brister),
  s (ödslig, vänskap, brister, mister, som), t (lita, litet, bandet, mister, knits),
  v (vän, var, vänskap), b (blir, bandet, brister), p (vänskap; *på* is written with n).
- The digits follow the consonant order b c d f g h j k l exactly (b1 d3 g5 h6 k8 l9),
  a key a writer would naturally construct.
- The result is a coherent rhymed album verse in two quatrains with consistent
  metre, fitting a 1904 friendship postcard; the plain verse on the same card is
  also on friendship/remembrance.

## Response to review 1

Review 1 (`review/REVIEW1.md`, Claude Opus 5.5, verdict **ACCEPT**) had four minor findings.

1. **"på" written with two dots — agreed, fixed.** On my own look at `review/work/pa2.png`
   and the strip (`work/strip-clockwise.png`) the sign before å has two dots, spaced like
   every other ":"; *vänskap* has three. `work/transcription.txt` now writes `:å`
   (literal *nå*), with a comment; SOLUTION.md gives the literal *nå* and the restored
   *på* and lists it as Uncertainty 8. The p-evidence line no longer cites *på*.
2. **One g-like glyph read two ways — agreed, disclosed.** Uncertainty 5 now says plainly
   that the same glyph is read k in *trikt*, *vänskap* and g in *igen* by context only;
   Uncertainty 3 and the verse give *trigt* as an equal alternative to *trikt*. The
   transcription header notes this too. The key and labels are unchanged.
3. **Word count — fixed.** Now "33 of 35 words".
4. **Translations of line 7 — fixed.** English and Slovak now carry an explicit
   "[line 7 not understood: 'ingen ging sbät']" marker instead of a phrase that reads as
   a sentence.

Re-run after the changes (`python3 -I ciphers/hcp-1477/work/decode.py`): source hashes
OK, 143 signs, 4 lines; the only change in the output is *på* → *nå* (literal). The
reading of the verse is otherwise unchanged.
