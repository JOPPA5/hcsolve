# hcp-1197 – Solution (Claude Opus 5.5, 2026-11-03)

Status: **complete**, with one disclosed restoration (one digit hidden by the collection stamp).
All work on this card was done by Claude Opus 5.5 in this session; there is no earlier work on this number.
No published solution of this exact card was found (one short web search, see SOURCES.md).
Note: the card itself already carries a pencil decipherment in block capitals along its lower edge
("DEINEN GELIEBTEN BRAUTIG..."), added by an unknown hand (recipient or a later owner). It agrees with
the decoding below; the key below was established independently from the numbers and checked against it.

## The card

Picture postcard (girl and boy in a meadow, printed caption "O Jugendzeit, O schöne Zeit!"), posted in
Frankfurt (Main)-Sachsenhausen; the large postmark on the address side reads 4.2.99, 8-9 N (the portal
file name gives 1899-02-14; the smaller cancel on the stamp is not fully legible). Addressed to
"Fräulein Käthchen Walther, Hofconfection, Sachsenhausen, Dreieichstraße 1. St." with a further word
below, read as "Laden" (shop) – this last word is uncertain and only an address detail.

Message (German, Kurrent, on the picture side), plain text with one enciphered line:

    Gruß aus Frankfurt a/M
    sendet dir
    dieser kleine Junge hier.
    Ungenannt und nur
    zu gut bekannt.
    Liebe Grüße an:
    4,5,9,13,5,13 – 7,5,11,9,5,2,19,5,13
    2,17,1,20,19,9,7,1,1[2]
    und an – – – –
    "   " Fräulein Schwester

## Cipher type and key

Number substitution (monoalphabetic, register label **MASC**): letters numbered in alphabet order with
J omitted (the usual 24/25-letter German school alphabet). Umlaut Ä written as A.

    A1 B2 C3 D4 E5 F6 G7 H8 I9 K10 L11 M12 N13 O14 P15 Q16 R17 S18 T19 U20 ...

Used on this card: A B D E G I L M N R T U. Without the J-omission (A=1…N=14) the first word would be
"DEIMEM", so the J-less numbering is forced by the text.

## Plaintext

    DEINEN GELIEBTEN BRÄUTIGAM

Full message in German: "Gruß aus Frankfurt a/M sendet dir dieser kleine Junge hier. Ungenannt und nur
zu gut bekannt. Liebe Grüße an: deinen geliebten Bräutigam und an – – – – [Liebe Grüße an] Fräulein Schwester."

English: "Greetings from Frankfurt am Main are sent to you by this little boy here. Unnamed and only too
well known. Love to: your beloved bridegroom, and to – – – – [love to] Miss Sister."

Slovak: "Pozdrav z Frankfurtu nad Mohanom ti posiela tento malý chlapec tu. Nemenovaný a až príliš dobre
známy. Srdečné pozdravy: tvojmu milovanému ženíchovi a – – – – [srdečné pozdravy] slečne sestre."

(The ditto marks under "Liebe Grüße" repeat the greeting; the dashes after "und an" are written on the
card as a teasing blank.)

## Command (from the repo root)

    python3 -I ciphers/hcp-1197/work/decode.py

It verifies the SHA-256 of the four source images, reads `work/transcription.txt` and prints
`DEINEN GELIEBTEN / BRAUTIGAm` (lower case = restored digit).

## Uncertainties

1. **Restoration**: the last group of line 2 is "1" + a digit under the printed HCPortal collection stamp
   (the stamp letter "C" covers it; a diagonal stroke with a top knot is visible, consistent with the
   writer's "2" but not fully readable). Read as 12 = M; it is the only value giving a word (BRÄUTIGA_).
2. The "19" of GELIEBTEN in line 1 also lies under the stamp: its "1" shows as a slanted stroke through the
   stamp's "C" and its "9" loop over the "P"; read from the pixels, not restored.
3. Plain text, Kurrent letters resting partly on word sense: "Liebe" (capital L vs V), and "Schwester",
   whose middle letters "chwe" are partly under the stamp (initial S and "ster" are clear).
4. A faint pencil word on the girl's skirt in the picture is illegible (possibly a name label such as the
   recipient's name; not confirmed). It is a single isolated word and not ciphertext.
5. The address word read as "Laden" under the street line is uncertain (not part of the message).
6. The stamp on the address side is affixed; nothing written around it; what is under it cannot be seen.
7. Sender is deliberately anonymous ("Ungenannt") – no name to check.

## Why it is correct

- Every one of the 24 number groups decodes; the three words are real German, grammatical after
  "Liebe Grüße an:" (accusative "deinen geliebten Bräutigam"), and fit the playful anonymous-admirer text.
- The key is the most common schoolchild number cipher; the J-less form is forced by "DEINEN" (13=N).
- The independent pencil decipherment on the card agrees with it.

## Response to review 1

Review 1 verdict: ACCEPT, four minor findings. No ciphertext reading or plaintext letter changes.
Reproduction command re-run after this response (`python3 -I ciphers/hcp-1197/work/decode.py`): four SHA-256 OK,
output `DEINEN GELIEBTEN / BRAUTIGAm`, unchanged.

1. **Inverted stamp – accepted.** I checked the stamp on the address side (review/work/stamp.png and
   source/address-large.jpg): the 5 Pfennig Reichspost stamp is affixed upside down ("REICHSPOST" and the "5"
   are inverted). In the "Briefmarkensprache" of the period an inverted stamp is often listed as a love signal,
   but the meanings vary between published tables, so I record it only as a possible deliberate signal on a
   teasing card, with no meaning claimed. Nothing is written beside or around the stamp. Uncertainty 6 is
   replaced by this note.
2. **Date – accepted.** The large Frankfurt (Main)-Sachsenhausen postmark clearly reads 4.2.99, 8-9 N; the
   cancel on the stamp reads "4 2 99" with a stroke before the 4 that may be a digit 1 or the postmark's box
   edge. The portal file name gives 1899-02-14. The card is therefore dated 4 February 1899 (clear postmark),
   possibly 14 February 1899 (portal); I give 4 February 1899 as the main reading. A further, mostly faded
   circular postmark ("…FURT…") stands on the picture side, top left; its date is not legible.
3. **Pencil decipherment wording – accepted.** The old pencil capitals on the lower edge read "DEINEN
   GELIEBTEN BRAUTIG" and then run into the HCPortal stamp. They agree with the decoding as far as BRAUTIG
   only; they do not confirm the restored final M. The wording at the top of this file should be read
   accordingly ("agrees up to BRAUTIG").
4. **Register type – accepted.** No steganographic part was found (stamp box, picture side, edges were
   checked by solver and reviewer). The human's note that "MASC + Steganography" applies to the Árokszállás /
   Jolánka cards concerns that Hungarian family, not this German card. The type stays **MASC**.

Additional check after review: the faint pencil word on the girl's skirt (hires picture side, unenhanced)
shows a word beginning with a capital K-like letter followed by "…th…", plausibly "Käthchen", the recipient's
name, as a label for the girl. It is not confirmed letter by letter, is a single plain word and is not ciphertext.
