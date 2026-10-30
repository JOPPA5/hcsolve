# HCP 1187 - Pigpen love letter, corrected after review 1

Human solver: Tomáš Pavuk

## Origin and scope

The HC Portal catalogue identifies this postcard as
`cpc_--_UK__UK_Croydon Surrey_`, from the T. Schrödel Collection, addressed
to Miss N. Harrison. General, Description and Attachments were inspected
on 2026-10-25; status was Not solved, with no supplied transcription or
solution. Immutable scans and the original catalogue capture remain in
`source/`; acquisition URLs are in `SOURCES.md`.

The handwritten address reads Miss N. Harrison, 67 Limes Rd, Croydon,
Surrey. The date and sender's historical identity are not established.
The picture caption is “Swans with Cygnets”; the writer calls them “Ducks”
in the ordinary cursive introduction. The introduction is not cipher text.
The decipherment covers the eight Pigpen lines: **158 symbol positions**,
including a probable but uncertain first signature letter.

## Literal decipherment

Line breaks retained; spaces are editorial. The preferred readings of weak
signs are printed below, with their limits explicitly listed afterward.

```text
YOU ARE A PRECIOUS
DARLING A LETTER SO SOON
I AM QUITE CONVINCED AND
HAPPY NOW I KNOW YOU ARE
BETTER MY HEART IS JUST OVER
FLOWINQ FOR YOU WITH LOVE
GOD BLESS YOU MY DEAR FOR
EVER WILL WRITE SOON [J/I]IM
```

The final sign of FLOWINQ is a top/left corner, not the three-sided G sign.
Q is the preferred literal value; R is possible if the nearby dot belongs
to the sign rather than the separator. **FLOWING is an editorial correction**
of the writer's apparent slip, never substituted in the raw tokens.
The signature has a closed square with a probable dot, so **Jim is probable**;
if that dot is printed/overlapping ink, the literal alternative is IIM.
Neither reading identifies a historical person.

Editorial punctuation and spelling: “You are a precious darling! A letter
so soon! I am quite convinced and happy now I know you are better. My heart
is just overflowing for you with love. God bless you, my dear, for ever.
Will write soon. [Probably Jim].” Joining OVER / FLOWINQ and FOR / EVER is
editorial; the manuscript line boundaries are preserved above.

## Slovak translation

„Si vzácny miláčik! List tak skoro! Teraz som celkom presvedčený a šťastný,
keď viem, že sa máš lepšie. Moje srdce preteká láskou k tebe. Nech ťa Boh
žehná, moja drahá, navždy. Čoskoro napíšem. [Pravdepodobne Jim].“

This translation follows the intended FLOWING meaning and FOR EVER closing.
The literal Q and uncertain signature remain documented above. Grammatical
gender is a translation choice, not proof of the sender's identity.

## Cipher and key

Standard interleaved Pigpen: undotted/dotted pairs in the grid, then wedges.
The solver transferred this key unchanged from its own HCP 1188 work.
The reviewer independently reconstructed the same fixed table.
Token labels specify strokes present in the upright working orientation.

| Outline / token | Undotted 0 | Dotted 1 |
|---|---|---|
| bottom/right BR | A | B |
| bottom/left/right B | C | D |
| bottom/left BL | E | F |
| top/bottom/right R | G | H |
| four sides C | I | J |
| top/bottom/left L | K | L |
| top/right TR | M | N |
| top/left/right T | O | P |
| top/left TL | Q | R |
| downward wedge V | S | T |
| right wedge > | U | V |
| left wedge < | W | X |
| upward wedge ^ | Y | Z |

## Reproduction and evidence

From repository root:

```sh
python3 ciphers/hcp-1187/work/decode.py
```

The command checks immutable original scan/metadata hashes, then decodes the
explicit manual outline/dot transcription in `work/transcription.txt` under
one key. It emits all 158 positions, including the signature alternative.
The portal supplied no transcript. This is not OCR: image-to-token decisions
are manual, with the independent scan comparison documented in review 1.
A token round trip merely checks internal consistency and is not pixel evidence.

No cipher symbol is intentionally omitted from the revised eight-line list.
Coverage of positions does not make every obscured dot certain. The changed
signs were rechecked against the original and the review crops, not accepted
solely because the resulting English is fluent. No published target plaintext
was used; no historical-priority claim is made.

## Uncertainties retained

- Line 5 U in JUST: dark wedge over the printed divider; >0 is compatible.
- Line 6 final Q in FLOWINQ: left stem and top bar; nearby dot probably a
  separator, with R an alternative. G is editorial, contradicted by the outline.
- Line 6 O and V in LOVE: printed outline overlap leaves limited stroke/dot evidence.
- Line 7 F in the added FOR: dotted slanted L partly overlaps printed lettering;
  O and R are clearer. F is the preferred compatible reading.
- Line 8 V in EVER: hasty dotted wedge resembles dotted top/right corner N;
  V is preferred with context, not securely proved by the small outline alone.
- Line 8 first signature glyph: closed square with probable dot; J preferred,
  I retained as a dot-loss alternative.
- Postmark date and personal identities remain unverified.

These limits are also indexed in `work/uncertainties.json`. The catalogue's
immutable metadata is preserved; later solver observations do not overwrite it.

## Response to review 1

Reviewer: Claude Opus 5.5, 2026-10-26, verdict **REVISE**. All five findings
were addressed locally; the substitution key did not change. The reviewer
explicitly stated that these corrections need no further review round.

1. **Missing FOR - corrected.** Added `BL1 T0 TL1` after DEAR on line 7.
   The original and `review/work/z-L7-dear-for.png` show the three signs
   continuing to the right margin. Literal text, interpretation, translation
   and coverage now include FOR EVER; total increases from 155 to 158 positions.
2. **FLOWING transcription - corrected.** Replaced final `R0` with `TL0`.
   `review/work/z-L6-G2.png` shows a left stem/top bar, unlike G in DARLING
   and GOD. Literal FLOWINQ is retained, possible TL1/R disclosed, and FLOWING
   appears only as an editorial intended reading.
3. **Signature - clarified.** Replaced an unspecified unknown by the as-seen
   closed-square alternatives `C1/C0`; `review/work/z-L8-sig2.png` supports
   probable J. Decoder shows [J/I]IM, with Jim preferred but no identity claim.
4. **Weak signs - individually disclosed.** Listed JUST/U, LOVE/O and V,
   EVER/V, and new FOR/F above and in `work/uncertainties.json`, with crop references.
5. **Reproduction - corrected and scoped.** Updated the manual tokens and
   regenerated `work/plaintext-check.txt`. Decoder verifies source hashes,
   applies the fixed key and retains alternatives. Removed the tautological
   round-trip claim as evidence of image correctness. Independent visual evidence
   is the review and the solver's subsequent collation. The cursive bird name
   is correctly reported as Ducks, distinct from the printed swan caption.

