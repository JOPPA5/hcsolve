# SOLUTION hcp-910 (M. Zwick to his parents, Ulm, 2 August 1917)

Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. No earlier work on this number. Portal status Not solved,
no attached transcription or solution; the transcription (work/transcription.txt) is my own, read from the
high-resolution scan work/hires/cpc_1917-08-03_DE_Ulm_DE_Erbenschwang_zwick-02_adr.jpg.

## Prior publications (README step 3)

- The digit key of this family (1-0 = a e i o u l n m r s) was published on 21 Feb 2019 by a reader ("Thomas",
  comment #1) under Klaus Schmeh's blog post "two encrypted postcards from 1918" (cards to Rosa and Zenzi Zwick,
  Erbenschwang): https://scienceblogs.de/klausis-krypto-kolumne/2019/02/21/two-encrypted-postcards-from-1918/ .
  The same commenter (#9) notes that a soldier M. Zwick wrote to his parents in Erbenschwang in 1917 with the same
  cipher, citing Tobias Schrödel's book "Ich glaube, es hackt!" (Springer), p. 233
  (https://books.google.de/books?id=T31FDAAAQBAJ&pg=PA233). I could not see that page, so I do not know whether it
  shows this card or its sister hcp-1057, nor whether it gives a decipherment. No plaintext of this card was found.
- The key was also reconstructed independently in this repo on sister cards hcp-1057 and hcp-1056 (same writer).
  I used that key; the transcription and decipherment of this card are my own.

## Cipher type and key

Partial monoalphabetic substitution (register label MASC) in German Kurrent: ten letters are written as digits,
all other letters (and the ligatures ch, ck, tt) stay plain Kurrent.

| digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| plain | a | e | i | o | u | l | n | m | r | s |

Umlauts are written as the digit with dots: 1" = ä (hätte), 4" = ö (könt), 5" = ü (würde).

Steganography check: no adhesive stamp was affixed (the stamp box holds only the Ulm Nr. 1 postmark and a printed
green number), so nothing can be hidden under a stamp; the picture side (Ulm Münster, printed caption) carries no
handwriting. One plain-text line runs vertically along the divider line (see below) and is included.

## Command (run from repo root; checks source hashes, prints the decipherment line by line)

    python3 -I ciphers/hcp-910/work/decode.py

## Full text of the card (German, writer's spelling kept)

Ulm, den 2. Liebe Eltern! Eine klaine Bitte hätte ich noch ann euch, nemlich es würde mich ser freuen, wann Jer
mier ein Paket Zucker schicken könt, denn ich weis nicht, wann ich in Urlaub komme. Gruß Euer Sohn Zwick.

Vertical along the divider (plain): Den Brief habe ich erhalten, besten Dank dafür.

Enciphered: everything from "Ulm den" to "komme" except the date numeral and "Liebe Eltern!", which are plain.
Sender (plain, top right): Abs. M. Zwick, [rank, probably Musketier] [unit abbreviation] 247, Ulm a. Donau.
Address: An Herrn Georg Zwick, Erbenschwang, Post Ingenried b. Schongau (Bay.). Postmark ULM Nr. 1 (DONAU) 3.8.17.

Normalised German: Eine kleine Bitte hätte ich noch an euch, nämlich es würde mich sehr freuen, wenn ihr mir ein
Paket Zucker schicken könntet, denn ich weiß nicht, wann ich in Urlaub komme.

## English translation

Ulm, the 2nd [of August 1917]. Dear parents! I have one more small request to you, namely it would make me very
happy if you could send me a parcel of sugar, because I do not know when I will come home on leave. Greetings, your
son Zwick. (Along the edge:) I have received the letter, many thanks for it.

## Slovenský preklad

Ulm, 2. [augusta 1917]. Milí rodičia! Ešte mám na vás jednu malú prosbu, totiž veľmi by ma potešilo, keby ste mi
mohli poslať balík cukru, lebo neviem, kedy prídem na dovolenku. Pozdrav, váš syn Zwick. (Na okraji:) List som
dostal, veľká vďaka zaň.

## Uncertainties

1. w5"9d2 (würde) and the second half of f92527 (freuen) lie under the Ulm postmark. Read on a blue-ink-isolated
   enlargement (work/crops, b4_blue / wurde_b / b5_blue): w, a 5 with flag and bowl, 9, the tall d loop and a 2 are
   visible; the umlaut dots on the 5 are not certain (the reading could be "wurde", same sense). In f92527 the
   second 2 is drawn with an oversized loop over the postmark's D; its foot is a 2.
2. 177 after "noch" reads "ann" (one n doubled); the writer spells phonetically (klaine, nemlich, ser, mier, weis),
   so this is kept literally as "an".
3. J29 = "Jer": the capital is a Kurrent I/J; the word is the writer's spelling of "Ihr" (no h written). Read by
   sense; the signs J, 2, 9 themselves are clear.
4. k4"7t (könt): an ink blot sits right after the 4; it is too small to hide another 7, so I read "könt"
   ("könnt"); if a sign is hidden it would be a second 7 and the sense is unchanged.
5. Kurrent capitals read by word sense: Z in Z5ck29 (Zucker; it resembles a 3 with a descender, but a 3 = i gives no
   word), P in P1k2t (Paket), B in "Brief" on the vertical line (the spelling may be "Brief" or "Breif"; the writer
   writes "Brif" on hcp-1057).
6. The date: only "2." is written (with a long stroke after it); the month is implied by the postmark 3.8.17.
7. Sender block: the rank word (probably "Musketier", as on hcp-1057) and the unit abbreviation before 247 are not
   read with confidence. The signature is "Zwick" with a large flourished capital Z and a paraph; no separate
   initial can be distinguished.

## Why this is correct

- The same key (published 2019 and reconstructed on hcp-1057/1056) decodes every one of the 92 digit signs on the
  card into ordinary German words with no exception and no gap.
- The text is coherent and typical of a soldier's card home in 1917 (a request for sugar, which was strictly
  rationed, and uncertainty about leave), written from Ulm by the same M. Zwick who wrote hcp-1057 from Aulendorf
  three weeks earlier and hcp-1056 from Ulm; spelling habits (diser/klaine/mier) match those cards.
- The writer's sense of what to hide is consistent: the request itself is enciphered, the greeting and the
  thank-you line are plain.

## Response to review 1

Review 1 verdict: ACCEPT, four minor findings. All addressed; the deciphered text is unchanged.

1. Sender block (minor). Re-read on a 3x enlargement of review/work/sender.png. The rank word begins with a clear
   Kurrent M and a long-s/k cluster; "Musketier" (written short, roughly "Musk'tier") fits the letters and the
   writer's rank on hcp-1057, but the middle letters rest on word sense. The unit abbreviation is two tall strokes
   with a dot, most likely "J.R." (Infanterie-Regiment) before 247; also by sense. The report and the transcription
   now show both as bracketed gaps, "[rank unread, probably Musketier] [unit unread, probably J.R.] 247", not as
   readings. These are two words of the sender's military address, not of the message.
2. Umlaut on w5"9d2 (minor). work/transcription.txt now has a comment stating that the dots on that 5 are inferred
   from word sense (würde; "wurde" possible, same sense) and are not separable from the postmark.
3. hcp-1057 status (minor). NOTES.md reworded: hcp-1057 was at DONE1 when this card was solved and has since reached
   FINAL (2026-11-03, review ACCEPT). The report cites it with that status.
4. HistoCrypt article (minor). SOURCES.md now lists https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 as
   consulted at abstract level only (by the reviewer); the PDF was not read.

Additional check after the review (human note on stamp steganography in the Jolánka series): the stamp box of this
card (review/work/stampbox.png) holds only the printed frame, the green "Z 4285" and the ULM Nr. 1 postmark; no
stamp was ever affixed, so no hidden message under a stamp is possible, and the picture side has no handwriting.
Type stays MASC.

Reproduction re-run after the changes: `python3 -I ciphers/hcp-910/work/decode.py` - all four hashes OK, same
plaintext as above.
