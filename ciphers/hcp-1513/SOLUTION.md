# hcp-1513 (pc_hcp_194) – solution

Status: complete reading of all ciphertext on the card (body + rotated margin); two small disclosed reading points (see Uncertainties).
Solved by Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Earlier work: an OpenAI GPT solver captured the portal metadata and scans
(2026-10-26) and triaged the card as a custom symbolic substitution without attempting a key; it claimed no plaintext.
No published solution of this card was found: the portal shows status "Not solved" and attaches no transcription or solution,
and the orchestrator's AI-register check (2026-10-29) found no record. The transcription is my own (no portal transcription exists).

## Card
Picture postcard "View of Hendricks, Minn.", postmarked HENDRICKS MINN. JUL 18 1910 (a Monday), one-cent Franklin stamp.
Addressed in clear to Miss Anna Lackrem, 711 So. Div. St., Northfield, Minn. Writer signs (in cipher) "Anton".

## Cipher type and key
Monoalphabetic simple substitution (MASC) of English with invented signs, one sign per letter; words separated by commas
(occasionally periods); the numeral 2 is written in clear. Key (token name in work/key.json → sign shape → letter):

| letter | sign | token |  | letter | sign | token |
|---|---|---|---|---|---|---|
| A | + (plus) | plus |  | M | Λ (inverted V) | lam |
| B | − (dash) | minus |  | N | square with a diagonal (◪) | nsq |
| C | reversed C (Ↄ) | revC |  | O | O | o |
| D | 8 | eight |  | P | E/B-like box (日) | box3 |
| E | Ж/K-like (X with a vertical stroke) | ex |  | R | L joined to П (LП) | LN |
| F | Γ | gamma |  | S | 5 | five |
| G | open square □ | sq |  | T | hourglass ⧗ | hg |
| H | triangle Δ | tri |  | U | Z/8 with bars (S-shaped, barred) | zbar |
| I | 1 | one |  | V | circle with vertical stroke (Φ) | phi |
| K | ÷ | div |  | W | circle with X (⊗) | ow |
| L | V | vee |  | Y | arch ∩ | cap |

J, Q, X, Z do not occur. 22 letters, 22 distinct signs, no homophones, no nulls.

## Command (run from repo root)
```
python3 -I ciphers/hcp-1513/work/decode.py
```
It verifies SHA-256 of the three files in source/, then decodes work/transcription.txt with work/key.json.

## Plaintext (English, as decoded; punctuation normalised)
Dear Anna:- Got your card Saturday. Thank you. I went up to Astoria Saturday afternoon, and from there went home,
got back here at 2 P.M. yesterday, and after that I went down to the lake to watch ball game.
[margin, upside-down/rotated in the upper left:] I dreamt about you last night. With love. Anton.

## Slovak translation
Milá Anna, dostal som tvoju pohľadnicu v sobotu. Ďakujem. V sobotu popoludní som šiel hore do Astorie a odtiaľ som šiel domov,
vrátil som sa sem včera o 2. popoludní a potom som šiel dolu k jazeru pozrieť sa na zápas v bejzbale.
[okraj:] Včera v noci sa mi o tebe snívalo. S láskou. Anton.

## English translation
(The plaintext is English; see above.)

## Uncertainties (all small)
1. DREaMT (margin line 1): the A sign (+) is written above the line between E and M as an insertion by the writer; it is read
   from the pixels (it appears tilted with the rotated text) and marked lower-case in the decoder output.
2. DOWN (body line 9): the W sign is a heavily inked oval in which the X of ⊗ is not separately visible; it is clearly not the
   open O sign, and W is the only letter giving a word. Read as W (blotted ⊗) – a disclosed restoration of a blotted sign.
3. "P.M." (body line 7): the M sign stands on the printed wavy divider of the card and has an extra stroke near its base, so it
   looks partly like the Δ (H) sign; "P.H." gives nothing, the Λ shape is visible, and "2 P.M." is required by context. Disclosed.
4. Punctuation (commas vs periods between words) is approximate and does not affect the reading.
5. "Astoria" is read letter by letter (+5⌛OLП1+); identified as Astoria, South Dakota, about 15 miles west of Hendricks.
   "The lake" fits Lake Hendricks. These identifications are context, not cipher evidence.

## Why I believe it is correct
- The salutation pattern +◫◫+ (ABBA) gives ANNA, matching the addressee in clear; 8X+LП gives DEAR.
- One fixed key of 22 signs decodes all 194 cipher signs on the card (157 body + 37 margin, incl. the inserted A; numeral 2 in clear) into fluent 1910 American English with no leftover or
  contradictory sign; repeated words (SATURDAY ×2, WENT ×3, AND, GOT, TO, YOU, THERE/HERE) are spelled identically each time.
- Context agrees: postmark Monday 18 July 1910 from Hendricks, Minn.; "Saturday … yesterday [Sunday]" timeline; Astoria SD and
  Lake Hendricks are local; ball game on a summer Sunday; writer signs Anton to "Miss Anna" (Norwegian-American Northfield).

## Response to review 1
Review 1 (Claude Opus 5.5, separate agent) gave verdict ACCEPT; its independent transcription and decode agree word for word.
1. (minor, sign count) Fixed. Counting the tokens of work/transcription.txt gives 194 cipher signs: 157 in the body and 37 in
   the margin, including the inserted A of DREaMT; the numeral 2 is in clear and not counted. "~230" in "Why I believe it is
   correct" is replaced by this figure. The reviewer's 197 comes from its own segmentation; the difference does not affect any word.
2. (minor, P.M. and DOWN) Agreed; both remain flagged as context-supported readings of imperfect signs in Uncertainties 2–3
   and in the report, which does not present them as sign-exact.
3. (minor, punctuation) Agreed; the decoder prints the separators as transcribed (BACK HERE has none on the card); the
   normalised plaintext punctuation is editorial, as stated in Uncertainty 4.
4. (minor, Astoria distance) Agreed; "about 15 miles west" is an unsourced approximation and is kept labelled as context
   only (Uncertainty 5), not cipher evidence.
No change to the key, the transcription or the reading. Reproduction command re-run on 2026-10-30: "source hashes OK" and
output identical to the plaintext above.
For the report two illustration crops were added: work/margin_rotated.png (margin rotated 122°, 3x) and work/body.png
(body text, 2x), both cut from source/address-large.jpg.
