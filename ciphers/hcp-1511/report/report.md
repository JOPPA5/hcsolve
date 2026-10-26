# HCP 1511 - A mixed Pigpen letter from Felton

## Origin and context

HC Portal record **1511**, catalogue name **pc_hcp_192**, is a postcard
addressed to Edith Elsworth in Burlingame, California. Its picture is captioned
“Part of Felton, California” and shows the Grand Central Hotel. The postmark
preserves day **31** and year **1913**; the month cannot be securely read.
The portal listed the date as Unknown. The author is unidentified.

The portal capture of 26 October 2026 showed Not solved. General, Description
and Attachments were inspected; the two scans had no attached transcription
or solution. No published plaintext was used in this attempt.

Source: https://crypto.hcportal.eu/dashboard/cryptograms/1511

The message mixes ordinary cursive with thirteen Pigpen word fragments.
There are **73 non-cancelled cipher positions** and one blackened correction.
That count includes positions whose dot or outline is ambiguous at the
available resolution. It is not a count of 73 independently certain glyphs.

## Method and corrected key

The Pigpen signs alternate undotted and dotted letters. Most outlines are
consistent with an interleaved alphabet, but the rightward wedge appears
where the surrounding text requires both W and Y. The overwritten W-position
in WOODEN cannot be securely distinguished from the clear Y-position wedges
in LIVERY and LIBRARY. The original claim of one exact alphabet without
exceptions was therefore withdrawn after review.

| Outline | Undotted | Dotted |
|---|---|---|
| Bottom/right corner | A | B |
| Bottom/left/right | C | D |
| Bottom/left corner | E | F |
| Top/bottom/right | G | H |
| Four sides | I | J |
| Top/bottom/left | K | L |
| Top/right corner | M | N |
| Top/left/right | O | P |
| Top/left corner | Q | R |
| Downward wedge | S | T |
| Leftward wedge | U | V |
| Rightward wedge | W or Y in context | not established |

X and Z do not occur in the recovered words; their signs are not established.
No upward Y wedge is supplied merely to make the table unique.

## The thirteen words

The contextual readings, in source order, are:

```text
HOUSE, LOUISE, PORCH, LONG, WOODEN, STORE, SALOON,
BARBER, SHOP, FRANKS, LIVERY, STA[cancelled]BLES, LIBRARY
```

They fit the prose and the photograph. The scan-led alternatives remain:

| Position | Scan-led alternatives | Contextual reading |
|---|---|---|
| PORCH final sign | H/J, open/closed frame | H |
| WOODEN first | G/W/Y, overwritten right frame/wedge | W |
| WOODEN second | O/P, dot uncertain | O |
| WOODEN fourth | C/D, dot uncertain | D |
| WOODEN sixth | M/N, dot uncertain | N |
| LIVERY final | W/Y, rightward wedge | Y |
| STABLES L | J/L, nearly closed frame | L |
| LIBRARY final | W/Y, rightward wedge | Y |

G is possible at WOODEN's first position only if its outline is the alternative
right-side frame. It is not a proposed alternative word. The cancelled mark
inside STABLES remains unrecovered. The two plain cursive ampersands immediately
after LOUISE and between SHOP and FRANKS are not Pigpen signs.

## Running text

Uppercase words below are contextual readings of the encrypted fragments;
the remaining text is a best manual reading of the cursive prose. It is not
a diplomatic transcription of every stroke. Unread marginal continuation
is explicitly marked.

> Dearest Edith, Here it is. The little HOUSE here at the left is where
> LOUISE & I were last Sun. afternoon on the PORCH. The LONG building at
> the side of the house is the WOODEN STORE. The Hotel has the sign on it.
> The SALOON, BARBER SHOP & FRANKS store & the LIVERY STA[cancelled]BLES are
> on the right out of sight. The building with the x is where they have the
> LIBRARY. It is nothing now. Just full of old old magazines & papers.
> Last yr. they had books but they have all been taken.
> [Further closing/marginal cursive writing not securely read.]

Slovak translation: „Najdrahšia Edith, tu to je. V tom malom dome vľavo sme
boli s Louise minulú nedeľu popoludní na verande. Dlhá budova vedľa domu je
drevený obchod. Hotel má na sebe nápis. Hostinec, holičstvo, Franksov obchod
a stajne s ustajnením či prenájmom koní sú napravo, mimo záberu. V budove
s x majú knižnicu. Teraz to nie je nič, je len plná starých, starých
časopisov a novín. Vlani mali knihy, ale všetky už odniesli.
[Ďalší záver a text na okrajoch nie sú spoľahlivo prečítané.]“

FRANKS is not identified with a particular owner or business. A visible x-like cross lies on the roof of the building to the right of
the Grand Central Hotel (approximately original picture x825,y307). A new
working crop records it. This fits the prose marker; it does not independently
verify the building's historical use as a library. The translation does not
turn contextual references into independently verified facts.

## Independent review and response

Review 1 by **Claude Opus 5.5**, dated 26 October 2026, returned REVISE. The
reviewer independently read all thirteen fragments and confirmed the words,
while refuting the original shape/key record. All five findings were addressed:

1. The two falsely transcribed upward Y wedges were changed to observed
   rightward wedges. WOODEN's overwritten first outline is recorded as an
   alternative. The key openly permits W/Y ambiguity; no unique key is claimed.
2. Uncertain WOODEN dots and PORCH/STABLES outlines are listed by position
   and represented as alternatives in the manual transcript and decoder.
3. Both plain ampersands adjacent to cipher fragments are now explicitly
   recorded, outside the cipher count.
4. The running prose and translation were added, with unread text marked.
5. The old claim that no date was established was corrected to 1913, with
   day 31 visible and month unread. The original portal capture was preserved.

These corrections change the evidence record rather than the thirteen word
interpretations. The reviewer stated that another round was unnecessary once
the record was corrected as described. The limits above remain material.

## Reproduction and limits

From the repository root:

`python3 ciphers/hcp-1511/work/decode.py`

The command checks hashes of the unchanged originals, expands the uncertain
manual outline/dot tokens, and prints observed alternatives beside contextual
word readings. It checks that each selected letter belongs to the observed
candidate set. It does not claim a unique inverse-key roundtrip, perform OCR,
or automatically recover the cursive prose. Source and review files were
unchanged. Successful decoding of hand-made tokens alone is not independent
pixel evidence; the review and explicit shape alternatives supply that record.
