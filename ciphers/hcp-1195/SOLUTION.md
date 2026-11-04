# hcp-1195 – solution (round 1, revised after review 1)

Card: picture postcard "Bergbleameln" (E. Riedel, Berlin, No. 112), header printed "Gruss aus" + pencil "Tepl 25/II 00";
posted Tepl (Teplá, Bohemia) to Anton Schönfelder, Favoritenstraße 64, Wien IV. T. Schrödel collection, portal status Not solved,
no attached transcription or solution. Transcription, key and decipherment: Claude Opus 5.5, 2026-11-03. No earlier work on this
number; no published solution found (sister card hcp-1194, same sender and recipient, same alphabet, was worked separately later; it was not used for this reading).

## Cipher type and key

Simple monoalphabetic substitution (MASC) with a home-made rune-like alphabet, German plaintext, word gaps kept.
Several signs follow the medieval "dotted rune" idea (dotted K = G, dotted B = P, dotted U = Ü, dotted F = W).
Sign codes (shape descriptions in `work/key.json`):

| sign | letter | sign | letter |
|---|---|---|---|
| asterisk rune (ᚼ) | H | plus / crossed stem (+, also Y-form, dotted, slanted-with-dot) | E |
| plain stem (ᛁ) | I | R-rune | R |
| down arrow (↓) | Z | hook rune (ᛚ) | L |
| lightning / sowilo (ϟ) | S | up arrow (↑) | T |
| fehu, two twigs (ᚠ) | F or V | fehu with dot | W |
| one-twig rune (ᚴ) | K | one-twig rune with dot | G |
| square u-rune (Π) | U | same with dot | Ü |
| B | B | B with dot | P |
| lambda (Λ, λ) | N | stem crossed by two bars (ǂ) | D |
| angle (<) | C | stem with slant stroke on the left (ᛅ) | A or O |
| psi / algiz (Ψ) | M | gamma with dot (once) | IC (see uncertainties) |

## Command (from repo root)

    python3 -I ciphers/hcp-1195/work/decode.py

It checks the SHA-256 of the four source images, applies `work/key.json` to `work/transcription.txt`, applies the
writer's own "2 / 1" reorder marks, and prints the raw output (homographs in braces) and the plaintext.

## Plaintext (as written, line by line)

    HERZLICHST FÜR LIEBEN BRIEF
    DANKEND GLIECHZIETIG BITTEND
    MIR VORIGE SONNTAGS KARTE
    ZU VERZIEHEN . LANGEND
    UND BANGEND IN SCHEBEN -
    DER PIEN -- FÜRCHTETE
    VERNEINDE ANTWORT
    AUF MEINE FRAGE .
    MORGEN ODER ÜBER MORGEN
    FOLGT BRIEF .
    MIT KUSS
    DEIN LIEB

Plain (not enciphered): "Gruss aus Tepl 25/II 00" in the header; under the picture a pencil footnote "[sign] = i." in Kurrent,
glossing the starred overwritten sign in line 8 (see below).

Normalised German: Herzlichst für [deinen] lieben Brief dankend, gleichzeitig bittend, mir [die] vorige Sonntagskarte zu
verzeihen. Langend und bangend in schwebender Pein – fürchtete [ich eine] verneinende Antwort auf meine Frage. Morgen oder
übermorgen folgt [ein] Brief. Mit Kuss, dein Lieb.

"Langen und bangen in schwebender Pein" is a line of Klärchen's song in Goethe's Egmont ("Freudvoll und leidvoll").

English: Thanking you most warmly for your dear letter, and at the same time asking you to forgive me for last Sunday's
card. Longing and fearing in suspended anguish – I feared a negative answer to my question. A letter follows tomorrow or
the day after. With a kiss, your love.

Slovensky: Najsrdečnejšie ďakujem za milý list a zároveň prosím, aby si mi odpustil minulú nedeľnú pohľadnicu. Túžiac a
bojac sa v napätom trápení – obávala som sa zápornej odpovede na moju otázku. Zajtra alebo pozajtra príde list. S bozkom,
tvoja láska. (The recipient, Herr Anton Schönfelder, is male; the writer is probably a woman – a love card signed "Dein Lieb", and the sister card hcp-1194 is signed RASA, which under this alphabet's A/O homograph can be ROSA – so the Slovak uses feminine forms for the writer. This is an inference, not a certainty.)

## Uncertainties (all disclosed)

1. Homographs resolved by word sense: the ᛅ sign stands for both A and O (DANKEND, KARTE, SONNTAGS, LANGEND, BANGEND, AUF,
   FRAGE, ANTWORT vs VORIGE, SONNTAGS, ANTWORT, MORGEN, ODER, FOLGT); I could not find a stable shape difference at this
   resolution. The two-twig fehu stands for F (FÜR, BRIEF, FÜRCHTETE, AUF, FRAGE, FOLGT) and V (VORIGE, VERZIEHEN, VERNEINDE).
2. Line 1, HERZLICHST: between L and H stands a single sign shaped like a gamma with a dot inside, used nowhere else. It must
   carry "IC" (or C with I left out); the word itself is certain. A printed flourish of the header ornament runs over this spot.
3. Line 8, MEINE: the third sign is heavily overwritten and marked with a star; the footnote under the picture glosses it.
   The footnote reads: asterisk, "=", one Kurrent letter, full stop. The letter has a lead-in, one tall down stroke and a
   w-like connector ending in a short stroke; no i-dot is clearly visible (the short final stroke may be a displaced dot).
   I read it as "i", but that reading rests partly on MEINE, the only sense of the word. The gloss is therefore consistent
   with MEINE, not independent proof of it.
4. Signs under the collector's stamp "PORTAL OF HISTORICAL CIPHERS" (compatible only, not confirmed by shape):
   - Line 11, KUSS: K and U are clear; the two S signs cannot be separated from the stamp lettering even after
     thresholding. Their pencil remains are compatible with the lightning S, nothing more: SS is a restoration from
     context ("Mit Kuss").
   - Line 7, ANTWORT: the R and the final T lie under the stamp ring; faint but compatible.
   - Line 9, second MORGEN: the final N lies at the stamp edge; faint but compatible.
5. Writer's spellings kept as written: GLIECHZIETIG (gleichzeitig), VERZIEHEN (verzeihen), PIEN (Pein) – EI written IE, while
   DEIN, MEINE, VERNEINDE have EI correctly; SCHEBEN-DER with the W of "schwebender" omitted; VERNEINDE for verneinende.
   In GLIECH the writer wrote H before C and marked the two signs "2" and "1" to reverse them; the script applies that.
6. Line 4, LANGEND: the first sign does not have the usual hook-L shape of LIEBEN, GLIECH, FOLGT and LIEB. It is a stem with
   a diagonal running down to the right and a dot at the upper right, written over erased traces; in shape it is closer to
   the λ-type N. The letter L is supplied by the word sense and the Goethe line ("Langen und bangen"), not by the sign's
   shape. FOLGT ends in an up-arrow with a dot (read T).
7. E against K: on this card E (Y-form) has a bar crossing the stem, K is a one-sided twig. In MEINE (final sign) and
   FÜRCHTETE the left half of the bar is faint, so those E calls rest partly on word sense, like the A/O and F/V homographs.
8. Steganography check: the picture side has no further writing (stamp box is on the address side; I cannot see beneath
   the affixed 5 Heller stamp). The address side is plain Kurrent/Latin writing. Nothing hidden was found, but under the
   stamp could not be inspected.

## Why I believe it is correct

Every sign on the card is decoded with one fixed table; the whole text gives coherent, period German love-letter prose
with a recognisable Goethe quotation (Egmont), fits the date (25 Feb 1900 was a Sunday; "vorige Sonntagskarte" = the
previous Sunday's card) and the sender–recipient pair. Medieval dotted-rune logic (K/G, B/P, U/Ü, F/W) makes the key
internally consistent. Recurring words (BRIEF twice, MORGEN twice) decode identically.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave verdict ACCEPT with six minor findings and no blocker or major. I re-checked
the relevant places on the hires scan (work/hires/..._pic.jpg, footnote and line-8 crops enlarged 3–4x). None of the
findings changes the plaintext; all are documentation fixes, made above.

1. Slovak genders – fixed. "aby si mi odpustil" (recipient Herr Anton Schönfelder is male) and "obávala som sa" (writer
   probably female, signed "Dein Lieb"; sister card hcp-1194 signed RASA/ROSA). The inference is stated as such.
2. L of LANGEND – agreed, fixed. Uncertainty 6 now says the sign looks closer to the λ-type N and that L is supplied by
   word sense and the Goethe line, not by the shape. The key is unchanged (the transcription keeps the sign as L by
   restoration; a literal shape-reading NANGEND gives no word).
3. KUSS – agreed, fixed. Uncertainty 4 now calls SS a restoration from context; the pencil remains are only compatible.
4. Footnote gloss – agreed, fixed. My own 3x crop shows the same: lead-in, one down stroke, w-like connector, no clear dot.
   Uncertainty 3 now says the "i" reading leans on MEINE and is not independent proof.
5. Faint signs under the stamp in ANTWORT (R, final T) and MORGEN (final N) – listed now with KUSS in uncertainty 4.
6. E against K on faint strokes – added as uncertainty 7 (MEINE final sign, FÜRCHTETE).

Steganography: the reviewer and I both found no hidden writing on the picture side (image, margins, caption, edges) or the
address side; only the affixed 5 Heller stamp could not be looked under. The register type is therefore MASC, not
"MASC + Steganography" (the human's stego remark concerned the Jolánka series).

Reproduction re-run after the edits (no files in work/ changed): `python3 -I ciphers/hcp-1195/work/decode.py` – all four
SHA-256 checks OK, plaintext identical to the block above.
