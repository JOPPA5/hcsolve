# hcp-1038 solution (round 1)

Solver: Claude Opus 5.5, 2026-11-03. No earlier work on this number. The portal (status Not solved) attaches no transcription and no solution; I transcribed the card myself from the hi-res scan `work/hires/cpc_1908-10-16_DE_-Altst_HU_Arad__adr.jpg`. A published solution of this card was not found (the portal's linked HistoCrypt article was not checked card by card).

Card: picture postcard "Dresden – Blick von der Kreuzkirche", dated on the picture side "1908. Okt. 16.", posted Dresden-Altstadt, addressed in plain Hungarian to "Őnagysága Meistrovich Jolánka úrleánynak, Arad, Bockó [?] tér 7., Ungarn" (address read from the scan; the street name is partly covered by the collection stamp and is uncertain: Bockó / Bocskó / Boczkó).

## Cipher type and key

Hungarian, monoalphabetic substitution with digits (register label: MASC). Each letter is one sign: a digit alone or a digit with a mark (comma below, dot on the baseline, two dots, dot at mid height, dot at the top, colon, dot before the digit). No word divisions; the commas and dots are part of the signs, not punctuation. The message is written at 90 degrees to the address, plus one line along the bottom edge that runs upright, left to right, in the address orientation (at 90 degrees to the message, not upside down).

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2` | l (once, in Jolikám) | | `6` | j |
| `1..` (two dots) | i | | `2.` | é | | `6,` | n |
| `1.` (baseline dot) | a | | `2,` | cs | | `6.` | ny |
| `1·` (mid-height dot) | a, á | | `3` | d | | `7` | k |
| `1'` (dot at top) | á | | `3,` | r | | `7,` | s |
| `1:` | e | | `3.` | v | | `7.` | sz |
| `·1` (dot before) | ü | | `4,` | g | | `8` | m |
| `1,` | b | | `4.` | gy | | `8,` | t |
| `5` | h | | `5,` | l | | `9` | p |
| `9,` | z | | | | | | |

135 cipher signs, 28 distinct. This is the same key family as the Mezőkövesd cards (hcp-1174, 1178, 1179: 0 o, 1. a, 1: e, 2. é, 2, cs, 3 d, 3, r, 3. v, 4, g, 5 h, 5, l, 6, n, 7 k, 7, s, 7. sz, 8 m, 8, t, 9 p, 9, z all agree), here seven years earlier and to a different recipient. New on this card: `1..` i, `1,` b, `4.` gy, `6` j, `6.` ny, `2` l. The key was found on this card by reading `2. 3 1: 7,` = édes and `5 1. 5, 5, 0 8, 8, 1. 8` = hallottam with the Mezőkövesd values, and the rest followed.

## Plaintext (Hungarian)

Cipher (90 degrees to the address):

Édes Jolikám! Hallottam, nagyon kikapott miattam. Igazán nagyon sajnálom, de én nem is gondoltam, hogy édesapja kezébe kerülnek a lapok. Sokszor csókolom Sanyi

Plain, under it: Szívélyesen üdvözlöm Sanyi

Cipher, along the bottom edge (upright in the address orientation): Várok választ.

Picture side, plain: 1908. Okt. 16.

## English translation

Dear Jolika! I heard you were scolded badly because of me. I am truly very sorry, but I never thought that the cards would get into your father's hands. Many kisses, Sanyi. — Kind regards, Sanyi. — I await a reply.

## Slovak translation

Milá Jolika! Počul som, že ste kvôli mne veľmi dostali vynadané. Naozaj ma to veľmi mrzí, ale ani som si nepomyslel, že sa lístky dostanú do rúk vášmu otcovi. Mnohokrát vás bozkávam, Šaňi. — Srdečne vás pozdravujem, Šaňi. — Čakám odpoveď.

(The writer uses the polite third person: "kikapott", "édesapja", "csókolom".)

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1038/work/decode.py

It checks the SHA-256 of the four scans, decodes every one of the 135 signs as transcribed, prints the letters as written next to the reading, asserts that the only non-accent difference is the one listed below, and prints the full text.

## Uncertainties

- `vahaszt` → választ: the 5 in the bottom-edge line has no comma under it at 5x enlargement, so as written it is h (`5`), not l (`5,`). Read as "választ" by sense (writer's slip). This is the only letter on the card that does not decode as written.
- `2` = l occurs only once, in "Jolikám"; elsewhere l is `5,`. "Jolikám" (pet form of Jolánka, the addressee) rests on word sense for that one sign; the other six signs of the name decode by the table.
- "de én nem" is written `3 1: 2. 6, 1: 8` = "de énem", one n for two; read as "de én nem".
- Accents: á is written `1'` once (igazán), but `1·` (mid-height dot) stands for both a (miattam, választ second a) and á (Jolikám, sajnálom, várok, választ first a); ó is written as plain o (csókolom). Long vowels are restored by sense; this changes no letter identity.
- The dot heights `1.` / `1·` grade into each other; both are a-type and no reading depends on telling them apart.
- A faint grey bracket-like curve after `1·8` at the start of the third line and grey streaks are pencil/paper marks, not signs.
- Stamp: the 5-Pfennig Germania stamp is stuck upside down. It is still attached, so the area under it cannot be inspected on the scan; nothing shows through or around it. Other cards of the collection carry hidden writing under the stamp; whether this one does is unknown. The upside-down stamp may be a "stamp language" sign, which I do not interpret. No writing was found in the picture or along the picture-side edges besides the date.
- Signature: the plain "Sanyi" (Kurrent-style S) agrees with the enciphered "Sanyi"; the flourish under it is a paraph.
- Sender's surname unknown; "Meistrovich Jolánka, Arad" is from the address.

## Why I believe it is correct

All 135 signs decode with one table to fluent, grammatical Hungarian of the period with consistent polite address; 134 decode exactly as written (accent marks aside). Twenty-one sign values coincide with the independently reconstructed Mezőkövesd key. The enciphered signature "Sanyi" matches the plain signature, and "Jolikám" matches the addressee Jolánka. The content (an apology that earlier cards fell into her father's hands) explains why the message is enciphered.

## Response to review 1

Verdict ACCEPT, four minor findings. No decoded letter changed.

1. Orientation of the bottom-edge line (minor) – fixed. Rechecked on source/address-large.jpg and review/work/bottom.png: `3.1·3,07 3.1·51·7.8,` stands upright, left to right, in the address orientation, at 90 degrees to the message. "Upside down" was wrong; corrected in the card description, the plaintext section and (as an appended correction) NOTES.md. The reading "Várok választ" is unchanged.
2. Steganography / stamp (minor) – agreed and made explicit. The human's note for this run says that on the Árokszállás Jolánka postcards (to Tóth Jolánka) there is almost always a hidden message under the stamp, plain or enciphered, and suggests the type `MASC + Steganography` for those. This card is addressed to a different Jolánka (Meistrovich Jolánka, Arad), from Dresden, in a different (digit) cipher family. Its 5-Pf Germania stamp is still attached (upside down), so the area under it cannot be seen on the scan, and nothing shows through or around the perforations; the picture side has only the printed caption and the date. Given the collection's habit, a message under the stamp is possible and could only be checked on the physical card. The card is therefore complete with respect to everything visible, but not with respect to the stamp area. Register type stays `MASC`, because there is no evidence of hidden writing on this card; if the stamp is ever lifted and writing is found, the type should become `MASC + Steganography`.
3. Self-referential check in work/decode.py (minor) – agreed. The assertion compares the decoded signs with the READING list in the same script, so it only documents where the reading departs from the letters as written (one place, vahaszt → választ); the independent evidence is the reviewer's own transcription and decoder (135/135 signs agree). The report says so.
4. Street name (minor) – fixed: marked as uncertain ("Bockó [?] tér 7."; Bockó / Bocskó / Boczkó). It does not affect the decipherment.

Re-ran `python3 -I ciphers/hcp-1038/work/decode.py` after the edits: hashes OK, 135 signs, 28 distinct, the only difference is line 7 `varok vahaszt` → `várok választ`, plaintext unchanged.
