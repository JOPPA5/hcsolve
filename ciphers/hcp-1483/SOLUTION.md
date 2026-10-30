# HCP 1483 / pc_hcp_164 - solution (round 1)

Portal status: Not solved (all three tabs read on 2026-10-26). No transcription or solution
is attached, and no published decipherment was found or used. The card is a "Pictorial Comedy"
postcard (picture caption "Is a caddie always necessary?"). It is addressed in plain writing to
Miss G.(or J.) Williams, "Baronhill", York Road, Colwyn Bay, N. Wales, and postmarked FE 11 08
(the portal date is 1908-02-11). The picture side has no cipher writing. Sister cards
hcp-1484 and hcp-1485 have the same addressee and the same kind of signs. They are still
unsolved in this repo, and this key has not yet been tried on them.

## Credits

On 2026-10-26 an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) downloaded the files and did the
triage. It made the 180-degree working copy `work/upright.jpg`. It did not establish a key or
any plaintext. On 2026-10-29/30 Claude Opus 5.5 did everything below: the transcription, the
identification of the cipher, the key and the decipherment.

## Cipher type and key

This is a **monoalphabetic substitution with a home-made, systematic alphabet** (type: MASC).
Words are not separated, and ordinary punctuation is kept. A superscript "2" after a sign means
that the letter is doubled.

* **Consonants** are a vertical stem with short bars, assigned in alphabetical order. Each sign
  has three features:
  * which side the bars are on: left (l), right (r) or crossing the stem (x);
  * how many bars there are: 1, 2 or 3;
  * where they sit: in the upper part with the stem hanging below (t), or in the lower part with
    the stem rising above (b).

| | 1t | 2t | 3t | 1b | 2b | 3b |
|---|---|---|---|---|---|---|
| left bars  | B (7) | C | D (∃ high) | F (⅃) | G | H (∃ low) |
| right bars | J (Γ) | K (F) | L (F, 3 bars) | M (L) | N (Ŀ) | P (E low) |
| crossing   | Q (T) | R (Ŧ) | S (丰) | T (⊥) | V (±) | W (± 3 bars) |

* **Vowels and Y** are closed shapes:
  * A = circle or oval with a central dot (⊙)
  * E = triangle (Δ)
  * I = triangle with an inner vertical stroke
  * O = square (□)
  * U = square with a diagonal (⧄)
  * Y = square with a Y-shaped pair of strokes
* The letters J, X and Z do not occur in this message. The J slot (r1t) is therefore inferred
  from the alphabetical rule only, not observed; Q (x1t) is attested only twice (QUICK, QUITE).

Files:
* `work/key.json`: the key.
* `work/transcription.txt`: Claude's own sign-by-sign transcription of the whole card (468
  enciphered letters, P.S. and signature included), written as feature tokens.
* `work/zoom.py`, `work/sheet.py`, `work/mkwin.py`, `work/segment.py`: the tools used for the
  enlarged crops.

## Reproduce (from the repo root)

```
python3 -I ciphers/hcp-1483/work/decode.py
```

The script checks the SHA-256 of the three files in `source/`, decodes every line and fails on
any token it does not know. It ends with
`-- source hashes OK; 468 enciphered letters decoded, all signs mapped`.

## Plaintext (English, literal decode)

The `/` word divisions are editorial. `^T` is a sign written above the line with a caret.
`[?]` is an extra sign (see the uncertainties below).

```
P.S. THES^TAMP ON THIS CARD FAS BEEN KISSED!!!
Does this interest you AT ALL SWEETHEART?          ("Does this interest you" is in plain writing)
MY OWN CARIAD, THANK YOU SO
MUCH FOR THE CARD. I KNOW YOU WILL
CONSIDER ME AN.UNTHANKFUL BEAST
FOR NOT HAVING EVEN ACKNOWLEDGED
RECEIPT OF THE "MIONEER"! THANK
YOU VERY MUCH FOR YOUR DEAR
THOUGHTFULNESS, DARLING. I LOVE
YOU SWEETHEART MINE, MORE THAN
I DID YESTERDAY BUT NOT SO MUCH
AS I SHALL LOVE YOU TOMOROW!
I AM SO GLAD TO HEAR THAT YOU
ARE STILL GETTING BETTER. BE QUICK
AND GET QUITE ALL RIGHT, DARLING.
MY COLD SEEMS TO HAVE GONE
COM[?]PLETELY. I WOULD NOT SWOL
WITH MISTER KAY FOR
FORTY WORLDS. KISS ME GOONIGHT, DARLING
a.m. [script capital, R?] "YOUR BOY"                ("a.m." and the capital are in plain writing)
```

### Normalised reading

> My own cariad, thank you so much for the card. I know you will consider me an unthankful beast
> for not having even acknowledged receipt of the "Pioneer"! Thank you very much for your dear
> thoughtfulness, darling. I love you, sweetheart mine, more than I did yesterday but not so much
> as I shall love you tomorrow! I am so glad to hear that you are still getting better. Be quick
> and get quite all right, darling. My cold seems to have gone completely. I would not swop with
> Mister Kay for forty worlds. Kiss me good night, darling. — a.m. R(?) "Your boy"
>
> P.S. This stamp on this card has been kissed!!! Does this interest you at all, sweetheart?

("Cariad" is Welsh for "darling, love", which fits a card sent to Colwyn Bay.)

**Slovak:** Môj vlastný cariad (miláčik), veľmi pekne ďakujem za pohľadnicu. Viem, že ma budeš
považovať za nevďačné zviera, lebo som ani nepotvrdil, že mi prišiel „Pioneer“! Veľmi pekne
ďakujem za tvoju milú pozornosť, miláčik. Ľúbim ťa, moja zlatá, viac ako včera, ale nie tak
veľmi, ako ťa budem ľúbiť zajtra! Tak sa teší, že počujem, že sa ti stále zlepšuje. Rýchlo sa
úplne uzdrav, miláčik. Moja nádcha už asi úplne prešla. Nevymenil by som sa s pánom Kayom ani za
štyridsať svetov. Pobozkaj ma na dobrú noc, miláčik. — „Tvoj chlapec“.
P.S. Známka na tejto pohľadnici bola pobozkaná!!! Zaujíma ťa to vôbec, zlatko?

## What remains uncertain (all disclosed)

1. **Writer's slips, reported literally.** The decode keeps the following exactly as written;
   the normalised reading corrects them.
   * The P.S. has one S shared by "THIS" and "STAMP". The T of STAMP is inserted above the line
     with a caret.
   * "FAS" is written for HAS: a single-bar ⅃ (F) where H (three low left bars) is expected.
   * "MIONEER" is written for PIONEER. The sign is clearly a plain L (M), not the three-bar P.
   * "TOMOROW" is written with only one R sign.
   * "GOONIGHT" has no D. The sign after OO is clearly the two-bar N.
   * "SWOL" stands where SWOP is expected. That last sign of line 15 is partly covered by the
     printed margin text, and its three right bars look high (L), not low (P).
2. **Extra sign in COM[?]PLETELY** (line 15, x≈630). A slanted stem with three crossing bars
   (S or W in shape) stands between M and P. It looks like a false start and is shown as `[?]`.
3. **"THES" in the P.S.** On this scan the first triangle shows no clear inner stroke (E). The
   second "THIS" has the stroke (I). Read as THIS.
4. **The dot in "AN.UNTHANKFUL"** (line 3) is a stray dot or word separator, kept as ".".
5. **Bar counts.**
   * Each sign is about 10 px high on the 1024-px scan, so at 10x enlargement two and three
     bars can look alike.
   * All count-critical signs were re-checked at 12-16x (key cases: CARIAD, C/D in
     ACKNOWLEDGED, D in DEAR, DID, GLAD and AND, S in SO, BEAST and KISSED, L in WILL and
     STILL, K in KAY, C in COLD and COMPLETELY). Wherever the enlargement was clear, the count
     agreed with the word.
   * A few signs that are blurred or covered by the printed text were read with help from the
     word: R in CARIAD, R in DEAR, W in TOMOROW, the I triangles at x≈940 under the vertical
     printed line, and Y in FORTY (stroke shape unclear).
6. **Signature.** "a.m." and a script capital (R? possibly another letter) are in plain writing.
   The quoted cipher word is small and cramped against the bottom edge:
   * O, B, O and the final Y are clear;
   * the first Y, the U and the R are only probable.
   * "YOUR BOY" is therefore a probable reading.
7. **Faint marks inside O** in "FOR" (line 16, x≈910) are lighter than the ink; read as a plain O.
8. **Triple underline and double underline.** "I" in "I WOULD NOT" (line 15) has three strokes
   under it. "MISTER KAY" (line 16) is underlined twice. Both are emphasis, not cipher signs.
9. **Unknown identities.** Neither the sender nor "Mister Kay" is identified. "The Pioneer" is
   probably a periodical, but which one is not established.

## Why we believe it is correct

* **One key covers the whole card.** All 468 enciphered letters on the card (body, P.S. and
  signature) decode with the single key in `key.json`. The only exceptions are the single
  extra sign and the slips listed above. The result is continuous, grammatical English of the
  period.
* **The key is not ad hoc.** It follows one rule: consonants in alphabetical order by
  side × count × position of the bars, and vowels as closed shapes. It was found from a few
  words: THE, the plain-text clue "Does this interest you … ?" followed by AT ALL SWEETHEART,
  and the P.S. HAS BEEN KISSED. Every later line then decoded on the first pass.
* **The content fits the card.** It is a love letter to a woman in Colwyn Bay. It uses the
  Welsh endearment "cariad", answers her card, mentions her illness ("still getting better")
  and his cold, and has the classic "this stamp has been kissed" postscript.

## Response to review 1

Verdict ACCEPT, four minor findings. All addressed; no decoded letter changed.

1. **Oak Road vs York Road.** Agreed. "Oak Road" was a provisional misreading in the GPT triage
   record (source/metadata.md, 2026-10-26), which stays unchanged as a source file. The scan
   (reviewer crop review/work/addr.png, the address upside down) reads "York Road". NOTES.md now
   records that the triage reading was wrong; SOLUTION.md and the report use York Road.
2. **Recipient initial.** Agreed. On the scan the address line is cut at the left edge, so the
   capital before "Williams" is not fully visible; the portal lists "J.Willams". The addressee is
   now given as "Miss G. (or J.) Williams" here and in the report.
3. **J and Q slots.** Agreed. key.json `_doc` and the key section now state that J (r1t) never
   occurs on the card and is inferred from the alphabetical rule, and that Q (x1t) is attested
   only twice (QUICK, QUITE), both consistently.
4. **THES^TAMP.** Agreed; the report explains the shared S and the caret-inserted T once.

Re-run after the changes: `python3 -I ciphers/hcp-1483/work/decode.py` prints the same 20 lines
and `-- source hashes OK; 468 enciphered letters decoded, all signs mapped`.
