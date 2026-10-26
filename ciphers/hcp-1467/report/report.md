# HCP 1467 - A Pigpen postcard to Adah Thompson

## Origin and scope

HC Portal record 1467, catalogue name **pc_hcp_148**, is a privately held
postcard dated **13 July 1907**. The portal capture of 26 October 2026 showed
Not solved. General, Description and Attachments were inspected; only two
scans were attached, with no supplied transcription or solution. The address
reads Miss Adah Thompson, Streatham, London; the catalogue spells the surname
Thompsson. The picture caption “Miss Hope” is printed matter.

This report covers all **62 handwritten Pigpen letters**. Ordinary address,
postmark, printing and ornamental strokes are outside the cipher. One cluster
of dots outside the signature glyphs is preserved without assigning it a
letter or punctuation function. The writer and the people mentioned remain
unidentified; the postmark town has not been securely read.

Source: https://crypto.hcportal.eu/dashboard/cryptograms/1467

## Method and key

The message uses interleaved Pigpen: each outline represents an undotted
letter and the next alphabetic letter when dotted. Outline names describe
the strokes present, relative to the upright working reading.

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
| Rightward wedge | U | V |
| Leftward wedge | W | X |
| Upward wedge | Y | Z |

The same table reads all 62 letters. Repeated O, U and the two BOO groups
provide internal comparisons; the ordinary English message independently
supports the resulting word boundaries.

## Literal plaintext

Dots between written words are retained. Spaces and line layout assist reading.

```text
HOPE. TO.
SEE. YOU. WITH.
LUCK. SOON. LOOK.
OUT. FOR. THREE.
COUNTRY. YOKELS.
LOVE.
BOO [EXTERNAL DOT CLUSTER] BOO.
```

An editorial sentence reading is: “Hope to see you with luck soon. Look out
for three country yokels. Love, Boo Boo.” This does not establish whether the
writer is one of the “yokels” or whether Boo Boo identifies a particular person.

Slovak translation: „Pri troche šťastia ťa čoskoro uvidíme. Dávaj pozor na
troch vidieckych truhlíkov. S láskou, Boo Boo.“ The plural subject is an
interpretive translation; the English opening does not state its subject.

## Scan uncertainties

LOVE's third glyph has a dot **inside** the wedge, giving V. In contrast, the
signature's dot cluster lies outside the third glyph's O outline. The first O
in LOOK has a smudge beyond its lower-right foot, between letters; it is not
an internal dot and does not change O to P. These distinctions retain the
visible marks without converting stray ink into letters.

## Review and correction

Independent review 1 by **Claude Opus 5.5**, dated 26 October 2026, returned
REVISE. The reviewer read the scan separately and independently decoded every
glyph. It found a single transcription error: the solver had missed the dot
in glyph 55 and defended LOUE. The corrected transcript uses dotted >1 and
now reads **LOVE** literally. The other 61 glyphs are unchanged. The reviewer
explicitly considered a second round unnecessary after this correction.

The response also retained the external signature dots, added the LOOK smudge
note, and corrected missing spaces in the documentation. Both decoders now
agree on all 62 letters. No published solution was used; no priority claim or
historical identification is made.

## Reproduction and evidential limits

From the repository root:

`python3 ciphers/hcp-1467/work/decode.py`

The command verifies source hashes and decodes the solver's disclosed manual
transcription. It is not OCR. The independent review supplies the separate
scan collation; successful token roundtrips alone would not prove the reading.
Original scans and review files were left unchanged.
