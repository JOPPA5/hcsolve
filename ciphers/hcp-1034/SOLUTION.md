# hcp-1034 / cpc_1904-09-05_DE_Munster_DE_Bremen_ — Münster to Bremen, 5 Sept 1904

Status: complete reading of the whole card (round 1), with the disclosed
points listed under "Uncertainties". Solved by Claude Opus 5.5 on
2026-11-03. There was no earlier work on this number. No published solution
was found or used: the portal status is Not solved and it has no attached
transcription or solution.

## The card

The picture is a view captioned "Wersepartie bei Handorf" (the river Werse
near Handorf, Münster). The address side is plain: "Fräulein / Mathilde
Meyer / in Bremen / Caprivi Str. 6." The stamp is a 5 Pf Germania, cancelled
MÜNSTER 5.9.04, with an arrival mark BREMEN 6.9.04. The publisher's line
reads "Verlag: Richard Borek, Braunschweig". The stamp box and the address
side carry no cipher. The scan cannot show anything underneath the stamp,
and no writing shows at its edges. Language: German. The plain part is in
Kurrent script.

The picture side carries two parts:

1. **Plain Kurrent text (not enciphered).** It runs along the top, and the
   date is written into the first line on the right:
   "Liebe Tilly! Du mußt heute schon mit einer Karte zufrieden sein, da es
   schon sehr spät geworden ist, und du doch morgen einen Brief bekommst."
   Date: "Münster, d. 5/9 1904."
2. **Cipher.** There are five rows of invented symbols. The first row is to
   the right of the plain text's line 3, the next three rows are below it on
   the left, and the last row is under those. A single extra sign sits just
   right of the church spire.

## Cipher type and key

The cipher is a simple monoalphabetic substitution with invented symbols
(register label **MASC**). Each symbol stands for one letter, and the
writer's word gaps are mostly kept. ß is written as two signs, s + z,
following the Kurrent ſʒ ligature ("Gruſʒ", "Kuſʒ"). The sign labels used in
work/decode.py are:

| sign (label) | description | letter |
|---|---|---|
| TRI | open triangle, no dot | I (capital) |
| TRId | triangle with a dot | i |
| VTRd | downward triangle with a dot | i (variant) |
| H2 | two verticals with a crossbar | n |
| H3 | three verticals with a crossbar | m |
| SQ | square or flat-bottomed box | d |
| D | D-shape (sometimes inked solid) | e |
| OV | narrow slanted oval "0" | c (once read as u, see U1) |
| L | L/b-shape | h |
| XL | crossed, looped X | f / F |
| U | u-shape (once with a dot or arc above) | u |
| R | r-shape | r |
| P | P-shape | l |
| N | N / V-with-hook zigzag | b |
| X | small x or crossed loop | a |
| XG | tall X | G |
| S | k-like sign (long s) | s (ß = S + Z8) |
| Z8 | 8 / Kurrent z | z |
| THk | circle or c with a bar and a small hook mark | k |
| CX | circle struck through diagonally | t |
| DAG | double-dagger cross | v |

## Transcription (reading order)

```text
A  TRI H2 SQ D H3 / TRId OV L / H3 TRId OV L / XL U R / SQ D TRId H2 D P TRId D N D
B  X OV XL / H3 D R THk / S X H3 / THk D TRId CX / L D R Z8 P TRId OV L - N D SQ X H2 .
   (lone THk right of the church spire)
C  THk D , / DAG D R / N P D TRId N D / VTRd OV L / H3 TRId CX / XG R U S Z8 / U H2 SQ
D  THk U S Z8
E  SQ D TRId H2 / CX R . / XL R TRId CX Z8 .
```

## Plaintext

Literal output of the command (word gaps as drawn):

```text
Indem ich mich fur deineliebe auf merk sam keit herzlich-bedan. ke, ver bleibe ich mit Grusz und kusz dein tr. fritz.
```

Normalised German (the cipher part):

> Indem ich mich für deine liebe Aufmerksamkeit herzlich bedanke, verbleibe
> ich mit Gruß und Kuß dein tr[euer] Fritz.

Full card in German:

> Liebe Tilly! Du mußt heute schon mit einer Karte zufrieden sein, da es
> schon sehr spät geworden ist, und du doch morgen einen Brief bekommst.
> [cipher:] Indem ich mich für deine liebe Aufmerksamkeit herzlich bedanke,
> verbleibe ich mit Gruß und Kuß dein tr[euer] Fritz.
> Münster, d. 5/9 1904.

English:

> Dear Tilly! Today you will have to make do with just a card, since it has
> already got very late and you will be getting a letter tomorrow anyway.
> Thanking you warmly for your kind attentiveness, I remain, with greetings
> and a kiss, your faithful Fritz. Münster, 5 September 1904.

Slovak:

> Milá Tilly! Dnes sa musíš uspokojiť len s pohľadnicou, lebo je už veľmi
> neskoro a zajtra aj tak dostaneš list. Srdečne ti ďakujem za tvoju milú
> pozornosť a zostávam s pozdravom a bozkom tvoj verný Fritz. Münster,
> 5. 9. 1904.

("Tilly" is a pet form of Mathilde, the addressee.)

## Single command

From the repo root:

```bash
python3 -I ciphers/hcp-1034/work/decode.py
```

It checks the SHA-256 of both source/ images and both work/hires/ originals.
It then decodes the transcription with the key and prints each row, the
literal plaintext and the normalised sentence.

## Uncertainties

- **U1: the oval in "auf".** The narrow oval OV stands for c in all four
  occurrences of "ich" (including "herzlich"). In the first group of row B,
  "X OV XL", the same glyph has to be u to give "Auf-merk-sam-keit". The
  other 11 signs of that word fit the key without exception. The reading
  rests on word sense and is either a writer's slip or a homograph. The
  script marks this token OV* and outputs u.
- **U2: the lone k by the spire.** A single THk (k) sign stands right of the
  church spire at the height of row B. Row B ends "bedan." at the spire, and
  row C begins "ke,". The lone sign is read as an abandoned start of "ke",
  rewritten on the next line. It is shown as [k] and left out of the
  plaintext. The full word is "bedanke" whichever way it is read. The dot
  after "bedan" is treated as a line-break mark.
- **U3: the dark figure at the right end of row A.** A small dark figure
  (a person with a staff) touches the last sign of "liebe" at the card
  edge. Its tone and grain match the printed picture. If a sign is hidden
  under it, the sentence does not need one ("deine liebe Aufmerksamkeit").
- **U4: one sign for each of k and b, in two forms.** k appears as a circle
  with a bar and hook ("keit", "ke", "Kuß") and as a c with a hook ("merk").
  b appears as an N zigzag ("liebe", "bleibe") and as a V with a hook
  ("bedanke"). Each pair is treated as one sign drawn in two ways. Shape
  and word sense both support this.
- **U5: "tr."** is read as the common abbreviation of "treuer". It is
  written with a period.
- **U6: capitals.** I (open triangle) and G (tall X) have their own capital
  forms. The other letters show no case distinction.
- **U7: the plain Kurrent text.** "heute", "zufrieden" (split over two
  lines, "zu / frieden") and "spät" are read from the letter shapes and
  confirmed by word sense. The text has no other unread word.
- **Stamp.** The stamp could not be lifted in a scan. No writing shows at
  its edges, and nothing in the message refers to a hidden note.

## Why it is correct

- One fixed key decodes every cipher sign on the card into fluent,
  grammatical German of 1904. The only exception is the single oval in
  "Auf" (U1). There are 92 signs in the five rows, plus 1 orphan sign.
- The key letters were not chosen in isolation. They are cross-checked
  across many words: e (D) appears in 14 places, i (triangles) in 11, and
  m/n (three versus two strokes) in 9 words. h appears at both ends of
  "herzlich", and r and z in "herzlich", "Gruß", "Kuß" and "Fritz".
- The text is a standard letter closing ("Indem ich mich ... herzlich
  bedanke, verbleibe ich mit Gruß und Kuß dein treuer ...") and follows
  naturally from the plain lines, which promise a letter for tomorrow. The
  signature "Fritz" and the salutation "Tilly", a pet form of Mathilde,
  match the addressee Mathilde Meyer.
- ß written as s + z matches Kurrent spelling habits, which confirms the
  values of S and Z8 on their own.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave the verdict ACCEPT with three
minor findings. Response, 2026-11-03, Claude Opus 5.5:

1. **Hyphen in row B (fixed).** On the 3x crop review/work/B2.png a short
   dash clearly joins the final L (h) of "herzlich" to the V-with-hook (b)
   of "bedan.". It is now in the transcription above and in work/decode.py
   (token "-", printed as punctuation). The literal output is now
   "... keit herzlich-bedan. ke, ver ...". No letter changed. I re-ran
   `python3 -I ciphers/hcp-1034/work/decode.py`: all four SHA-256 checks
   print OK and the output is as given under "Plaintext".
2. **Evidence for U1 (agreed, added to the report).** The writer's u in
   "für", "Gruß", "und" and "Kuß" is open at the top; the second sign of
   "Auf" is a closed narrow oval identical to the c of every "ich". So the
   card literally has a c-sign there, and u rests on word sense alone. The
   report states this contrast. No change to the reading.
3. **Stamp (agreed, stated in the report).** The scans cannot show what is
   under the stamp, and other series in this collection (for example the
   Jolánka cards) often hide a message there. The report now says plainly
   that a hidden message under the stamp cannot be excluded from the scans.
   Nothing visible on this card is steganographic, so the register type
   stays MASC, not "MASC + Steganography".

The reading is not changed by the review.
