# SOLUTION hcp-992 (cpc_1903-12-04_DE_Munchen_DE_Eschersheim_kellermann-02)

Solver: Claude Opus 5.5, 2026-11-03. No earlier work exists on this number; the portal attaches no
transcription or solution and lists the card as Not solved. A short web search (2026-11-03) found no
published solution. The transcription is my own, read from the un-converted scans in work/hires/.

## Card
Picture postcard (Frauenkirche, Munich), written "München 4. Dez. 03." to Fräulein Margarethe Kellermann,
per Adr. Herrn A. Weyhe, Hochwohlgeboren, Eschersheim b/Frankfurt a/Main, Frankfurterstr. 49 (arrival postmark Eschersheim 5.12.03).
Language German. The message on the picture side mixes plain Kurrent handwriting (the practical news) with
ciphered lines (the endearments, the closing and one word inside a parenthesis). The address side carries no
cipher; nothing is visible at the stamp edges or picture borders (the stamp was not lifted, so the area under it is unknown).

## Cipher type and key
Monoalphabetic substitution (MASC) with digits and a few invented signs, one sign per letter.

| plain | sign | | plain | sign |
|---|---|---|---|---|
| A | 9 with filled (blacked) loop; an oval on a long descender (φ-like), as in hcp-993 | | L | 1 |
| Ä | same, two dots above | | M | 3 |
| B | 6 | | N | 2 |
| C | hook like a reversed c | | R | tall stroke with hook (open 6) |
| D | V | | S | 5 |
| E | 4 | | T | 7 |
| G | 9 (open loop) | | U / Ü | U-shaped sign / with two dots |
| H | 8 | | Z | capital-I-like sign |
| I | arch with a dot under it | | K | double-crossed sign (like ‡) |

Letters F, J, O, P, Q, V, W, X, Y and ß do not occur. Spaces between words are kept; no homophones are needed.

## Command
From the repo root:

    python3 -I ciphers/hcp-992/work/decode.py

(It also prints the token count: 111 cipher tokens, 20 key entries.)

It checks the SHA-256 of all four images, applies the key to work/transcription.txt and prints the deciphered
lines and the whole card text.

## Plaintext (original German; deciphered parts in capitals)
München 4. Dez. 03.
MEIN HERZINNIGGELIEBTES HERZENS[word inked out by the writer]....!
(hatte dir GUNKTE [= Punkte?] aufgeschrieben) Wollte dir noch schnell mitteilen, daß du Herrn(?) zum 7.
gratulierst, habe versehentlich der letzten Karte u. Paket falsche Adresse gegeben, bin kerngesund.
Morgen schreibe ich Brief. Grüße bitte alle Lieben recht herzlich.
DICH ABER UMARMT MIT UNZÄHLIGEN GRÜSSEN UND KUSSEN [= Küssen] DEIN SICH SEHR NACH DIR SEHNENDES ERIC[H] ...... ....

## English
Munich, 4 Dec. 03. My most dearly beloved heart's [inked-out word]....! (I had written you "points/dots"?)
I wanted to quickly tell you that you should congratulate Mr(?) on the 7th; by mistake I gave the wrong address
on the last card and parcel; I am perfectly healthy. Tomorrow I will write a letter. Please give my warmest
regards to all the dear ones. But you are embraced, with countless greetings and kisses, by your Erich(?),
who longs for you very much ...... ....

## Slovak
Mníchov, 4. dec. 03. Moje najvrúcnejšie milované srdiečko [začiernené slovo]....! (napísal som ti „bodky"?)
Chcel som ti ešte rýchlo oznámiť, že máš 7. zablahoželať pánovi(?); omylom som na poslednej pohľadnici a balíku
uviedol nesprávnu adresu; som úplne zdravý. Zajtra napíšem list. Pozdravuj, prosím, srdečne všetkých milých.
Ale objíma ťa s nespočetnými pozdravmi a bozkami tvoj po tebe veľmi túžiaci Erich(?) ...... ....

## Uncertainties (all disclosed)
1. Blotted word after HERZENS: fully inked out by the writer, unreadable (followed by four dots and "!").
2. Parenthesis group "9 U 2 K 7 4" decodes by the key to GUNKTE, not a German word. "Punkte" (dots) fits the
   context (the dots after the blotted word and at the end) but needs P for the 9-sign; P does not occur elsewhere.
   If "Punkte" is meant, the writer used the G-sign (9) for P by mistake. Reported literally; meaning uncertain.
3. Closing name: E R I C + a sign with a filled blob over a lower loop, then dots. It is either a 2 (N) with a
   blob or a cramped 8 (H) with this writer's filled upper loop; read H ("Erich"), printed ERIC[H]. Support:
   word sense and sister hcp-993, signed "Erich" with 8. The C there is a plain curve, slightly simpler than the C-hook in "sich/nach/Dich".
   A stray dot stands before the E. "sehnendes" (neuter) before a male name is as written.
4. Word sense calls on faint/stamp-overlaid signs: in UMARMT the 2nd sign could be 3 or 5 (M chosen) and the 3rd
   is a 9 with partly filled loop (A chosen, not G); in DIR the first sign is faint (D). The second arch-sign in
   HERZINNIG has a tick instead of a round dot (read I). KUSSEN has no umlaut dots on U (written so).
5. Plain Kurrent: one word after "daß du" is uncertain ("Herrn"? H + short letters + a hook mark + n); "kerngesund"
   and "versehentlich" are read with some help from word sense. Everything else reads.
6. Area under the postage stamp not inspected (stamp not removable); no hidden writing seen elsewhere.

## Why it is correct
Every ciphertext sign on the card is covered by one 20-sign key with no conflicts across 111 cipher
tokens; the key recurs consistently (HERZ in two words, SICH/NACH/DICH share C and H, UND/DEIN/DIR share D).
The result is idiomatic German of 1903 love-letter style that fits the plain Kurrent around it and the context
(Munich to Eschersheim, December 1903). Type for the register: MASC.

## Response to review 1

Reviewer verdict: ACCEPT (Claude Opus 5.5, separate agent). All five findings are minor; none changes the reading.

1. Final sign of the signature. Agreed. Re-examined at 4x (review/work/sig.png): the sign has a filled upper part
   over a lower loop, which fits this writer's 8 with a filled upper loop as well as a 2 with a blob. Sister card
   hcp-993 (same writer, same recipient, same key) signs "Erich" with a plain 8. work/decode.py now maps the token
   2* to "[H]" with a comment and prints ERIC[H]; the plaintext above now reads ERIC[H]. Uncertainty 3 is updated
   below. Re-run of `python3 -I ciphers/hcp-992/work/decode.py`: source hashes OK, output unchanged except
   ERIC[H].
2. Letter count. Fixed: 111 cipher tokens, 20 key entries; decode.py now prints this count.
3. GUNKTE gloss. Agreed and stated in uncertainty 2: if "Punkte" is meant, the writer used the G-sign (9) where
   P was needed; P is attested neither here nor on hcp-993. The word stays reported literally. The context
   supports "Punkte": this couple's cards close greetings with rows of dots (Herzens....!, Erich ......).
4. Key description. Fixed: the A row now cross-refers to hcp-993's description of the same sign (oval crossed by a
   long vertical, φ). The key of hcp-993 agrees with this card in every shared letter (L N M E S B T H G A R C D Z
   I U Ü K). The NOTES remark that hcp-993 had no work was true when written.
5. Address. Fixed: "Hochwohlgeboren" added.

Steganography check (prompted by the human's note that some Schrödel-collection cards hide messages under the
stamp): the stamp on this card is on the address side, placed diagonally, not lifted, and no writing is visible
at its edges, in the picture or along the borders (checked by solver and reviewer). The type stays MASC; the area
under the stamp is not inspected and stays listed as unverified.
