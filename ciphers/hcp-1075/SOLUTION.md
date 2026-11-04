# hcp-1075 / cpc_--_USA__USA__ — American Morse postcard, Akron, Ohio (c. 1903–1910)

Status: complete reading of the whole card (round 1), with five disclosed
word-sense points listed below. Solved by Claude Opus 5.5 on 2026-11-03.
No earlier work on this number; no published solution was found or used
(portal status Not solved, no attached transcription or solution).

## The card

Raphael Tuck & Sons "Raphotype" postcard No. 5369, "Akron, Ohio. City
Hospital." (hospital completed July 1902). No postage stamp and no
postmark: the stamp box holds only the printed Tuck trademark (inspected,
nothing written under or in it). Language: English.

- Address side, plain: "Mr Ezra W Sipple / Meyersdale / Penna"
  (Meyersdale, Pennsylvania).
- Address side, left half and bottom: eight rows of dots and dashes with
  commas — the cipher (American landline Morse).
- Picture side, plain handwriting along the caption strip (not enciphered):
  "No 547 Carroll St / akron ohio" (left), "I have not forgot the code
  but do Not remember the Noo on the Bx card" (two lines), in the
  bottom-right corner, diagonally, "547 Carroll St", and the initials
  "J. N. S." (signature).

## Cipher type and key

American (railroad/landline) Morse, written by hand: a fixed
letter-for-symbol substitution (register label MASC/Morse). Key, as in
work/decode.py: O = `. .`, R = `. ..`, C = `.. .`, Y = `.. ..` (spaced
dots), L = long dash `=`, T = short dash `-`, other letters as in the
American code; numerals 4 = `....-`, 5 = `---`, 7 = `--..` (American
values; in International Morse `---` would be O and `--..` Z). Commas
drawn on the card separate words. International Morse does not read the
text (e.g. RECD would come out as `. ..`/`.. .` nonsense).

Same system as the FINAL sister card hcp-1453 (American Morse, Washington,
1906); key compared and identical for all shared letters.

## Transcription (rows as on the card; `*` = word-sense point)

`=` is a long dash (L). In row 4 the two dashes of WILL are of middle
length (between this writer's T and L); they are transcribed `=` (L) by
word sense, hence `=*`, as in work/transcript.json.

```text
1  . ..  .  .. .  -.. ,  .. ..  . .               R E C D , Y O
2  ..-  . .. ,  .. .  .-  . ..  -.. ,             U R , C A R D ,
3  -  ....  ..  ... ,  .-  -- ,                   T H I S , A M ,
4  . .*  .--  ..  =*  =* ,  .--  . ..             I W I L L , W R
5  ..  -  . ,  ...  . .  ..*  -. ,  --            I T E , S O O N , M
6  .. ..*  ,  .-  -..  [^-..]  . ..  .  ...  ... ,  ..  ... ,
                                                  Y , A D D R E S S , I S ,
7  ....-  ---  --.. ,  .. .  .-  . ..  . ..  . .  =  = ,
                                                  4 5 7 , C A R R O L L ,
8  ...  - ,  .-  -.-  . ..  . .  -.  . .  ....  ..  . .
                                                  S T , A K R O N O H I O
```

Machine-readable form: work/transcript.json (17 words, 64 signs).

## Plaintext

Literal decipherment (all 64 signs):

```text
RECD YOUR CARD THIS AM I WILL WRITE SOON MY ADDRESS IS 457 CARROLL ST AKRON OHIO
```

Normalised: "Rec'd your card this a.m. I will write soon. My address is
457 Carroll St., Akron, Ohio."

House number: the Morse clearly gives 457; the writer's own plain note
on the picture side gives 547 twice. The decipherment keeps 457 as
written; which number is the real address is not established.

Literal form of the word-sense points (printed by decode.py), with the
card's own word division:

```text
RECD YOUR CARD THIS AM OWI[L/T][L/T] WRITE SOIN MY ADDRESS IS 457 CARROLL ST AKRONOHIO
```

Plain note on the picture side: "No 547 Carroll St, Akron Ohio. I have not
forgot the code but do not remember the No(s) on the Bx card. J. N. S."

English translation: the text is English already.

Slovak translation:
- Šifra: „Dnes ráno som dostal tvoju pohľadnicu. Čoskoro napíšem. Moja
  adresa je Carroll St. 457, Akron, Ohio.“
- Poznámka na obrázkovej strane: „Carroll St. č. 547, Akron, Ohio. Kód som
  nezabudol, ale nepamätám si čísla na tej ‚Bx‘ pohľadnici. J. N. S.“

## Single command

From the repository root:

```sh
python3 -I ciphers/hcp-1075/work/decode.py
```

It checks the SHA-256 of both source scans and both hi-res originals,
decodes every transcribed sign with the American Morse key, checks the
key/inverse roundtrip and lists the flagged readings. It decodes the manual
transcription, not the pixels. work/measure_marks.py (needs PIL; the
runtime at /Users/tomaspavuk/.cache/codex-runtimes/.../python3) prints
rough mark positions per row; its row windows are approximate and it misses
some light dots, so it is only a helper.

## Uncertainties (all disclosed)

1. I (row 4, first letter): two dots with a gap between this writer's I
   (tight) and O (wide). Read I ("I WILL"); there is no comma between I and
   WILL. O is not excluded by the pixels alone.
2. WILL (row 4): the two dashes are of middle length (shorter than the
   clear L's of CARROLL, about as long as the T of ST). Read L L by word
   sense; WITT is not a word.
3. SOON (row 5): the second O is written with a tight gap that looks like
   I; literally S O I N. Read SOON by word sense.
4. MY (row 6): the first pair of the Y is a little wider than usual. Read
   Y; M + O + I is not a word.
5. Number 457 vs 547: the Morse clearly gives `....-` `---` `--..` =
   4 5 7, while the plain note on the picture side writes the house number
   twice as 547 (first digit a looped 5; an 8 cannot be fully excluded).
   The Morse is reported as written; the writer's own note ("do not
   remember the No… ") may explain a slip in the numbers. Which is the true
   house number is not established.
6. Picture-side note: "Bx" (in "the Bx card") is an unexplained
   abbreviation (box? a card name?), "Noo" is read as "No(s)"; the
   initials "J. N. S." are reported literally (N could be W). The rest of
   the note reads clearly.
7. The second D of ADDRESS is a writer's caret insertion above the line
   (not a reading problem).

Ink vs collector stamp: the last row (OHIO) lies under the grey
HCPORTAL/Schrödel collector stamp. Dot darkness was sampled: the ten ink
dots read about 60–130 (grey value) against about 157 for the stamp
letters, so all ten dots (O H I O = 2+4+2+2) are ink.

## Why it is correct

- One standard historical key (American Morse, used by US telegraphers
  c. 1900) reads all 64 signs with no unused or unmapped symbol.
- The result is plain period English, an ordinary postcard reply.
- The decoded address (Carroll St, Akron, Ohio) agrees with the printed
  card view (Akron City Hospital) and with the plain address written on
  the picture side (Carroll St, Akron Ohio); the note itself says "I have
  not forgot the code", confirming an intended code.
- The spaced-dot letters (C, O, R, Y), long L and American numerals 5 =
  `---`, 7 = `--..` only make sense in American Morse.

## Response to review 1

Verdict ACCEPT, four minor findings; no reading changed.

1. Notation mismatch (WILL dashes). Fixed: the row-4 transcription now
   writes `=*  =*`, with a note that the middle-length dashes are read as
   L by word sense, matching work/transcript.json.
2. House number 457 vs 547. Fixed: the conflict is now stated directly
   under the normalised plaintext (Morse 457, plain note 547 twice), not
   only in the uncertainty list. The decipherment keeps 457 as written.
3. Published-solution check. Done 2026-11-03: the full PDF of Schrödel,
   "Cryptographic postcards", HistoCrypt 2021
   (https://ecp.ep.liu.se/index.php/histocrypt/article/download/166/122/65,
   6 pages) was downloaded to a scratch directory and its text searched.
   It is a statistical overview of the collection (it counts 8 Morse-code
   cards) and contains no reading of this card; Akron, Ohio, Sipple,
   Meyersdale and Carroll do not occur. Recorded in SOURCES.md.
4. Literal vs read forms. Done: work/decode.py now also prints the literal
   form `... AM OWI[L/T][L/T] WRITE SOIN MY ... AKRONOHIO`, shown above
   under the plaintext. Re-ran `python3 -I ciphers/hcp-1075/work/decode.py`
   from the repo root: same plaintext, 17 words, 64 signs, hashes and
   roundtrip OK.

Steganography check (requested by the human for the whole collection):
the stamp box on the address side holds only the printed Tuck trademark
and nothing written; no hidden, upside-down or under-stamp writing was
found on either side by solver or reviewer. The register type therefore
stays MASC/Morse, not MASC + Steganography.
