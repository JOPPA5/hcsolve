# HCP 1511 / pc_hcp_192 — reviewed word readings with ambiguous glyphs

Review 1 returned REVISE: the thirteen contextual words are secure, but the
original unique-key/transcription claim was wrong. The revised record retains
observed outline alternatives and explicitly distinguishes them from words
selected using surrounding prose. There are 73 non-cancelled cipher positions,
not 73 independently unambiguous scan readings. A blackened item in STABLES
remains [cancelled]; its original value is not recovered.

## Contextual cipher-word readings

```text
HOUSE
LOUISE
PORCH
LONG
WOODEN
STORE
SALOON
BARBER
SHOP
FRANKS
LIVERY
STA[cancelled]BLES
LIBRARY
```

These encrypted fragments occur inside unencrypted cursive prose. In that
prose and the photograph the thirteen words are clear. They do not establish
a unique alphabet for every visible mark: the same rightward wedge appears
where the words require W and Y. No writer/person/business identity is inferred.

## Corrected observed key

| Outline strokes / wedge | Token | Undotted | Dotted |
|---|---|---|---|
| bottom/right | BR | A | B |
| bottom/left/right | B | C | D |
| bottom/left | BL | E | F |
| top/bottom/right | R | G | H |
| four sides | C | I | J |
| top/bottom/left | L | K | L |
| top/right | TR | M | N |
| top/left/right | T | O | P |
| top/left | TL | Q | R |
| downward wedge | V | S | T |
| leftward wedge | < | U | V |
| rightward wedge | > | W or Y in context | not established |

No upward Y wedge is observed in LIVERY or LIBRARY; both are rightward >0.
Their old ^0 tokens were incorrect. The first sign of WOODEN is overwritten
by the descender of “building”; it resembles > or a three-sided right frame
(R0). It is not securely an upward wedge. The record therefore openly permits
an inconsistent W/Y assignment on this card, rather than inventing a unique
shape distinction. X and Z are unobserved; no dotted-wedge value is established.

The revised scan-led output is:

```text
HOUSE
LOUISE
PORC[H/J]
LONG
[G/W/Y][O/P]O[C/D]E[M/N]
STORE
SALOON
BARBER
SHOP
FRANKS
LIVER[W/Y]
STA[cancelled]B[J/L]ES
LIBRAR[W/Y]
```

WOODEN first position includes G only for the alternative R0 outline; it is
not a proposed reading of the word. These brackets are alternatives, not
extra letters. Context selects the words in the first list.

## Running text and translation

Best reading of the cursive prose, with contextual Pigpen words uppercase:

> Dearest Edith, Here it is. The little HOUSE here at the left is where
> LOUISE & I were last Sun. afternoon on the PORCH. The LONG building at
> the side of the house is the WOODEN STORE. The Hotel has the sign on it.
> The SALOON, BARBER SHOP & FRANKS store & the LIVERY STA[cancelled]BLES are
> on the right out of sight. The building with the x is where they have the
> LIBRARY. It is nothing now. Just full of old old magazines & papers.
> Last yr. they had books but they have all been taken.
> [Further closing/marginal cursive writing not securely read.]

This is a best reading, not a full diplomatic edition of every cursive stroke.
The plain ampersand immediately after LOUISE and the one between SHOP and
FRANKS are recorded as cursive & signs, not Pigpen wedges. Other ordinary
ampersands remain in the running text. A standalone copy is work/running-text.txt.

Slovak translation: „Najdrahšia Edith, tu to je. V tom malom dome vľavo sme
boli s Louise minulú nedeľu popoludní na verande. Dlhá budova vedľa domu je
drevený obchod. Hotel má na sebe nápis. Hostinec, holičstvo, Franksov obchod
a stajne s ustajnením či prenájmom koní sú napravo, mimo záberu. V budove
s x majú knižnicu. Teraz to nie je nič, je len plná starých, starých
časopisov a novín. Vlani mali knihy, ale všetky už odniesli.
[Ďalší záver a text na okrajoch nie sú spoľahlivo prečítané.]“

“Franksov” is a grammatical translation of FRANKS, not an identification of
its owner. A visible x-like cross is on the roof of the building to the
right of the Grand Central Hotel (approximately source picture x825,y307;
work/photo-cross-large.jpg). It fits the prose's marker, but the image alone
does not establish the building's historical use as a library.

## Reproduction

`python3 ciphers/hcp-1511/work/decode.py`

The manual work/transcription.txt records ? for uncertain dots and {a|b}
for alternative outlines. The decoder prints scan alternatives and separately
labelled contextual words. It checks each selected contextual letter belongs
to the observed candidate set, and checks original source hashes. It does not
claim a unique inverse-key roundtrip, OCR or automatic recovery of the prose.
Source and review files are unchanged.

## Position-specific uncertainties

- WOODEN: first outline >0/R0; second sign's dot uncertain (O/P); fourth
  sign's dot uncertain (C/D); sixth sign's dot uncertain (M/N).
- PORCH final sign is nearly/factually closed: R1/C1 gives H/J. H comes
  from the surrounding prose and the evident porch, not a secure open frame.
- STABLES L is nearly closed: L1/C1 gives L/J. The blackened item before B
  remains an explicitly cancelled mark, not a guessed cipher letter.
- LIVERY and LIBRARY final signs are clearly >0, producing W/Y alternatives
  under the observed ambiguous assignment. Context chooses Y.

## Date, provenance and scope

The postmark shows day 31 and **1913**; its month is illegible. This is enough
to date the card to 1913, despite the portal's Unknown date. The photo caption
is “Part of Felton, California”; the Grand Central Hotel is visible. The card
addresses Edith Elsworth. The author remains unidentified. All three rendered
tabs were captured, fresh Not solved, with no attached solution/transcription.
No published target plaintext was used; no historical-priority claim is made.

## Response to review 1

1. **Y and W outlines (major).** Accepted. Re-read source/address-large.jpg
   and review/work/cmp_livery_Y.jpg, cmp_library_Y.jpg and cmp_wooden_W.jpg.
   Changed lines 11 and 13 from ^0 to >0; recorded WOODEN first sign as
   {>0|R0}. Removed the false one-alphabet-without-exceptions claim. The
   decoder now exposes W/Y ambiguity rather than fabricating a distinct Y.
   The thirteen context-selected words are unchanged; no new full key is claimed.
2. **Weak dots/outlines (minor).** Accepted and listed by position above.
   Updated WOODEN positions 2, 4 and 6 with uncertain-dot tokens, PORCH final
   with R1/C1 and STABLES L with L1/C1. This lowers overclaimed certainty
   instead of making the scan conform to expected words.
3. **Plain ampersands (minor).** Accepted. Recorded both signs in the manual
   transcript comments, decoder output and running text. Neither is counted
   among the 73 cipher positions or assigned a wedge value.
4. **Running prose (minor).** Accepted. Added the best reading and Slovak
   translation above and in the report, marking unread marginal continuation.
5. **Date (minor).** Accepted after viewing review/work/pm.jpg and the
   original. Corrected the old “no date established” statement to 1913;
   month remains unread, day 31 observed. Original metadata capture unchanged.

The reviewer explicitly considered another round unnecessary if these record
corrections were made. They are addressed here without changing the thirteen
word interpretations. The glyph record remains resolution-limited and the
W/Y assignment remains ambiguous; final documentation must preserve those
limits. No watcher or handover/final marker was created by this response pass.


## Finalization - 2026-10-26

The coordinating solver verified the item-by-item review response, reran the
corrected decoder with original-source hash checks, and produced the report
PDF. All rendered pages were visually inspected after final typography
corrections. The review explicitly permits closure after the specified local
corrections without another round. Remaining reading uncertainties are
preserved; no new independent ACCEPT verdict is claimed.

The local register-entry.txt is prepared with solver TODO because no solver
name was supplied for the entry. Nothing was submitted externally. Original
source files and review files were left unchanged. FINAL records closure
after these review conditions and report checks.
