# HCP 1513 (pc_hcp_194): Anton to Anna Lackrem, Hendricks, Minnesota, 1910

Human solver: Tomáš Pavuk

**Status: deciphered in full (194 of 194 cipher signs); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1513 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1513), portal name pc_hcp_194, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1910-07-18, language Unknown, location North America, sender and recipient Unknown, with no transcription or solution attached.

It is a picture postcard titled "View of Hendricks, Minn." The address side is written in clear: **Miss Anna Lackrem, 711 So. Div. St., Northfield, Minn.** It carries a green one-cent Franklin stamp and the postmark **HENDRICKS MINN. JUL 18 1910** (18 July 1910 was a Monday). Hendricks is a small town in south-western Minnesota on the South Dakota line; Northfield lies far to the east, south of the Twin Cities.

The whole message is in cipher on the left half of the address side: nine lines of body text in blue ink, and five short lines written at an angle (rotated by about 120°) in the upper-left corner. The large wheel-shaped watermark with letters and the HCPortal logo across the card belong to the portal's scan, not to the cipher.

![Address side: cipher body in nine lines at the left, rotated margin note in the upper-left corner, address in clear at the right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, "View of Hendricks, Minn." (source/picture-large.jpg)](../source/picture-large.jpg)

No sister card by the same writer was found in this repository, and no published solution of this card was found. The decipherment below is new.

## Method

The transcription is **manual**: the text lines were located on the address side, each half-line was read sign by sign at 5x enlargement, and the margin block was rotated by 122° and read at 5–6x. The signs are geometric and letter-like shapes (+, 8, Δ, ⊗, 5, a V, an hourglass, an L joined to a П and others); words are separated by commas or periods, and the numeral 2 is written in clear. The transcription with one token name per sign is in work/transcription.txt.

The opening word pair gave the entry. The second word has the pattern ABBA with a + at both ends, which matches the addressee **ANNA** (written in clear on the card); the first word, ending in + and a fourth sign, then reads **DEAR**. GOT YOUR CARD, SATURDAY and THANK YOU followed from the letters already fixed, and every remaining word fell into place with no conflict. The result is one fixed key of 22 signs for 22 letters, with no homophones and no nulls. Repeated words (SATURDAY twice, WENT three times, AND, GOT, TO, YOU, THERE/HERE) are spelled identically each time.

![Body text, nine lines (work/body.png, 2x crop of the address side)](../work/body.png)

![Margin note rotated by 122° (work/margin_rotated.png, 3x crop): I, DREaMT, / ABOUT, YOU, / LAST, NIGHT, / WITH, LOVE. / ANTON.](../work/margin_rotated.png)

The decoding is reproducible from the repository root with one command, which first checks the SHA-256 hashes of the source files and then decodes the transcription with the key (work/key.json):

```text
python3 -I ciphers/hcp-1513/work/decode.py
```

In review a separate agent made its own crops, wrote its own glyph transcription with its own sign codes, built its own table from the ANNA / DEAR crib and decoded with its own script. Its output agrees with the solver's **word for word**.

## Key

Monoalphabetic simple substitution (MASC) of English with invented signs. The descriptions are conventional names for handwritten shapes.

| Letter | Sign | Letter | Sign |
|---|---|---|---|
| A | + (plus) | M | Λ (inverted V) |
| B | − (dash) | N | square with a diagonal |
| C | reversed C (Ↄ) | O | O |
| D | 8 | P | box with a middle bar (E/B-like) |
| E | Ж-like (X with a vertical stroke) | R | L joined to П |
| F | Γ | S | 5 |
| G | open square □ | T | hourglass (two triangles point to point) |
| H | triangle Δ | U | Z/S-shape with bars |
| I | 1 | V | circle with a vertical stroke (Φ) |
| K | ÷ | W | circle with an X (⊗) |
| L | V | Y | arch ∩ |

J, Q, X and Z do not occur in the text. The 194 cipher signs are 157 in the body and 37 in the margin (the latter including one A inserted above the line).

## Plaintext

Decoder output, line by line as on the card (commas and periods are the word separators as written; the lower-case a marks a sign inserted above the line):

```text
DEAR , ANNA :-
GOT , YOUR , CARD ,
SATURDAY . THANK , YOU .
I , WENT , UP , TO , ASTORIA ,
SATURDAY , AFTERNOON ,
AND , FROM , THERE , WENT ,
HOME , GOT , BACK HERE , AT , 2 , P . M .
YESTERDAY , AND , AFTER , THAT ,
I , WENT , DOWN , TO , THE , LAKE , TO , WATCH , BALL , GAME ,
--- margin ---
I , DREaMT ,
ABOUT , YOU ,
LAST , NIGHT ,
WITH , LOVE .
ANTON .
```

Normalised text (punctuation editorial):

> Dear Anna:- Got your card Saturday. Thank you. I went up to Astoria Saturday afternoon, and from there went home, got back here at 2 P.M. yesterday, and after that I went down to the lake to watch ball game.
> [margin] I dreamt about you last night. With love. Anton.

The plaintext is English, so it serves as its own English translation.

**Slovak translation:**

> Milá Anna, dostal som tvoju pohľadnicu v sobotu. Ďakujem. V sobotu popoludní som šiel hore do Astorie a odtiaľ som šiel domov, vrátil som sa sem včera o 2. popoludní a potom som šiel dolu k jazeru pozrieť sa na zápas v bejzbale.
> [okraj] Včera v noci sa mi o tebe snívalo. S láskou. Anton.

The text fits the card. Posted on Monday 18 July 1910, it describes the preceding weekend: a trip to Astoria on Saturday afternoon, home, back "here" on Sunday at 2 p.m., then a ball game at the lake on a summer Sunday. Astoria is a small town in South Dakota just west of Hendricks, and "the lake" is presumably Lake Hendricks beside the town; both identifications are context, not cipher evidence.

## Uncertainties

1. **DREaMT** (margin, line 1): the A (+) is written above the line between E and M, an insertion by the writer; it is read from the scan and shown in lower case.
2. **DOWN** (body, line 9): the W sign is a heavily inked oval in which the X of ⊗ is not separately visible. It is clearly different from the open O beside it, and W is the only letter that gives a word. This is a context-supported restoration of a blotted sign.
3. **P.M.** (body, line 7): the M sign stands on the printed wavy divider of the card and has an extra stroke near its base, so it looks partly like Δ (H). The Λ apex is visible and "2 P.M." is required by the sense; "P.H." gives nothing. Context-supported reading.
4. **Punctuation**: commas and periods between words are approximate; BACK HERE has no separator on the card. This does not affect the reading.
5. **Identifications**: Astoria (South Dakota) and Lake Hendricks are inferred from geography; distances were not checked against a source. The identity of "Anton" and of Anna Lackrem beyond the address was not researched.
6. The work was done from the portal's scans (about 1024 px wide); the original card was not examined.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the reproduction command, decoded the card with its own transcription and script, checked every word against 5x crops of the scan (including the R of ASTORIA, the inserted A, the blotted W, the M of P.M. and the Y of YESTERDAY), confirmed the date (18 July 1910 was a Monday) and the local geography, and confirmed that no published solution exists. Verdict: **ACCEPT**, with four minor findings:

1. The sign count "~230" in the solution was wrong; corrected to 194 (157 body + 37 margin) from the transcription.
2. P.M. and DOWN should stay flagged as context-supported readings; they are (Uncertainties 2 and 3).
3. Punctuation is approximate; stated (Uncertainty 4).
4. The Astoria distance is unsourced; kept labelled as context (Uncertainty 5).

No letter of the reading changed. Two illustration crops (body and rotated margin) were added for this report.

## Credits

An OpenAI GPT solver captured the portal metadata and scans on 2026-10-26 and triaged the card as a custom symbolic substitution without proposing a key or plaintext. Transcription, key recovery, decipherment and this report: Claude Opus 5.5 (2026-10-30). Independent review: a separate Claude Opus 5.5 agent.
