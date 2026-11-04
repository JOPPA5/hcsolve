# hcp-1082 — solution (Claude Opus 5.5, 2026-11-03)

HC Portal cryptogram 1082, T. Schrödel collection: postcard "258. TOURS — La Poste" (picture: the Tours post and telephone office), postmarked GARE DES AUBRAIS / LOIRET 27-8-42, 1F50 Pétain stamp, addressed in plain writing to "Mr Lucien Rabaud, 6 rue Fellonneau, Nantes, L. Inf." (street name corrected after review 1). Portal status Not solved, language Unknown, no transcription or solution attached. No earlier work on this number; all reading and decipherment here is by Claude Opus 5.5. No published solution of this card was found or used (the portal only links the general HistoCrypt article on the Schrödel collection).

## Cipher type and key

Monoalphabetic number substitution (MASC). Each letter is one digit plus an optional mark (tick ' or double tick "); digits taken in the order 1 2 3 4 5 6 7 8 9 0:

| digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| no mark | A | B | C | D | E | F | G | H | I | J |
| ' | K | L | M | N | O | P | Q | R | S | T |
| " | U | V | W | X | Y | Z | | | | |

Words are separated by dashes. The key was found from the card itself: the isolated word "1" (= À) and "2 5' 4' - 6' 5' 8' 0'" = BON PORT fix the scheme, and every other group then reads.

## Transcription

`work/transcription.txt` (marks exactly as written, 10 lines, 27 written groups (26 words; SOUVENIRS runs over a line break), 105 signs). Read from the un-converted original `work/hires/..._adr.jpg`, enlarged 2-4x (crops in work/lines/ and work/zoom/).

## Command

```
python3 -I ciphers/hcp-1082/work/decode.py
```
(run from repo root; checks SHA-256 of the four images, prints the literal decryption and the decryption with the 7 disclosed slip corrections.)

## Plaintext

Literal output (marks as written):
```
MON CHER LUCIFN / JE PENSE BIEN / A TOI JAI FAIT / BON VOYAGE ET / SUIS ARRIVEE / A BON PORT / JE TEDBEIE / BIED DEI CHOSES / BONS SOUVE / DIRS ANDRE
```

Read text (French, accents and apostrophes added):

> Mon cher Lucien, je pense bien à toi. J'ai fait bon voyage et suis arrivée à bon port. Je t'envoie bien des choses. Bons souvenirs. André

English: My dear Lucien, I am thinking of you. I had a good journey and arrived safely. I send you all the best. Fond memories / regards. André

Slovak: Môj drahý Lucien, veľmi na teba myslím. Mala som dobrú cestu a šťastne som docestovala. Posielam ti veľa pozdravov. Pekné spomienky. André

## Uncertainties and writer's slips (all disclosed)

1. LUCIEN: the 5th sign is clearly 6 (= F), not 5 (= E); a digit slip. The name is confirmed by the plain address "Lucien Rabaud".
2. Omitted ticks (digit is right, mark missing), six signs: T'ENVOIE written 0' 5 4 2 5 9 5 (should be 4' 2" 5'), BIEN in line 8 written 2 9 5 4 (4'), DES written 4 5 9 (9'), and the 4 starting line 10 (NIRS, 4'). In every case the digit sequence equals the intended word exactly; the same words carry their ticks elsewhere on the card (BIEN line 2, BON, SOUVE-). These are corrections of the writer's enciphering, not of the reading, and are listed in decode.py (EMEND).
3. Line 1: the 4 of MON is retraced in darker pencil with a small round tick; read 4' (N). The first sign is a loop-topped 3 with tick (M), same 3 shape as in "3858'".
4. Line 5: the second 8 of ARRIVEE has its tick written low (comma-like) next to a small blot; read 8' (R). The 4th sign of SUIS is 9 with a curved tick, read 9' (S). A short black stroke above line 5 is in a different (black) medium and was ignored.
5. Signature 1 4' 4 8' 5 = ANDRE; the "ч"-shaped 4 is the writer's usual 4 (same as in BIEN, DES). The feminine "arrivée" does not agree with André; either the writer is Andrée (one E left out) or the agreement is a slip. Reported literally as ANDRE.
6. The stamp box was inspected (stamp intact, nothing visible around it); the picture side carries no writing (only ink specks at the top). Anything under the stamp cannot be checked from the scans.
7. Street name in the address (plain): read "6 rue Fellonneau" after review 1 (looped F; work/zoom/street.png); it is not ciphertext.

## Why it is correct

All 27 groups and all 105 signs decode with one fixed, systematic key (alphabet in three rows of ten), giving grammatical, idiomatic French of a typical travel card ("j'ai fait bon voyage et suis arrivée à bon port", "bien des choses", "bons souvenirs"). The decrypted salutation names the addressee in the plain address. The only departures are one digit slip and six missing ticks, each on a sign whose digit matches the intended letter.

## Response to review 1

Verdict ACCEPT, four minor findings, no change to the decipherment. `python3 -I ciphers/hcp-1082/work/decode.py` re-run from the repo root after the edits: "source hashes OK", literal and corrected outputs unchanged (as above).

1. Street name: agreed and fixed. On the un-converted original enlarged (work/zoom/street.png, crop 1900,1000-3300,1250 of work/hires/..._adr.jpg) the initial is a looped cursive f with a descender below the ruled line, followed by "ellonneau"; together with the reviewer's note that Nantes has a rue Fellonneau, this reads "6 rue Fellonneau". Item 7 and the header corrected; the report uses Fellonneau.
2. Line 5, sign 4 (S of SUIS): agreed. On my enlargement (work/zoom/suis.png) the 9 is followed by a curved pencil tick and a second faint stroke partly under the black stroke, so a double mark cannot be excluded from the scan. 9" has no value in the key (the third row ends at 6" = Z), and 9' = S is the only reading that gives a letter and the word SUIS. The report states that this call rests partly on the key and word sense.
3. Gender in the Slovak translation: agreed. The report adds a note that the feminine forms (mala som, docestovala) follow the written "arrivée", and that the writer's gender (André or Andrée) is unresolved (item 5).
4. Emendations: agreed; the report shows the literal and the corrected decryption side by side and lists all seven emendations.

On steganography (prompted by a note from the human about hidden messages under stamps on another card series): both sides were inspected again. The stamp is intact and the area round it, the picture side and the edges carry no further writing; whatever may lie under the stamp cannot be checked from scans. No steganographic part is claimed, so the type stays MASC (number substitution).
