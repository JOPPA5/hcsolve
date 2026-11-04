# hcp-1091: solution (round 1, revised after review 1)

Solver: Claude Opus 5.5, 2026-11-03. No earlier work exists on this number. The portal lists it as Not solved and attaches no transcription or solution. A short web search (2026-11-03, "Hradegh" postcard cipher Schrödel) found no published solution of this card. The transcription is my own and was made from `work/hires/cpc_1886-03-12_AT_Wien_AT_Krems__pic.jpg`.

## The card

- Address side: plain German Kurrent with no cipher. "An Herrn August Hradegh", a place line read tentatively as "Förstla" (uncertain reading, underlined in green), "in [Gföhl, struck through in violet]", "b. Krems". There are four 1-Heller stamps and a WIEN postmark. Two postal annotations in violet ink are not the sender's message and are left unread: a handwritten forwarding note above "Förstla" (it starts with a capital like S, roughly "Schilling…"; not read with confidence) and a faint rubber stamp at the top edge ending "…INGERAMT".
- The stamps look like the 1908 Austrian jubilee issue. If so, the card dates from 1908 or later, and the date 1886 in the portal file name cannot be right. I could not read the year in the postmark.
- Picture side (a girl drinking at a spring, signed by the artist, apparently "A. Mailick"): all the ciphertext is here, in three blocks:
  - A, the left margin, 10 lines
  - B, the right margin, 14 lines
  - C, three lines written upside down in the sky of the picture and closed with a triple underline
- The ends of lines C1 and C2 run under the picture-side stamp, and about one sign of each is hidden. Nothing else is written along the edges. The area under the picture-side stamp cannot be inspected on the scans. On related series a hidden message under the stamp is common, so further text under this stamp cannot be excluded. No evidence of it exists, so the type stays MASC and not MASC + Steganography.

## Cipher type and key

The type is MASC, a monoalphabetic substitution by digit-like signs. Consonants are written as digits or digit-like signs. Vowels are written as dots and dashes on the line, or as marks on a sign, following Kurrent conventions: u is written as n (sign 2) with a raised breve or bar, and ü as n with two raised dots. Four signs each stand for two related letters.

| sign | plain | sign | plain | sign | plain |
|---|---|---|---|---|---|
| 0 | l | 7 | s | `.` | i |
| 1 | d / t | 8 | h | `..` | e |
| 2 | n | 9 | f / v | `...` | ie |
| 2 + raised breve/bar | u | x | w | `-` | a |
| 2 + raised two dots | ü | + | c / z | `-` with two dots | ä |
| 3 | m | T (1 with top bar) | o | `!` `?` | themselves |
| 4 (open, curled top), or its S-shaped variant (B3, B4) | r | T with two dots | ö | | |
| 5 | g / k | J-shaped sign | j (only in "Jaga(s)") | | |
| 6 | b | closed y/4-shaped sign | s (only in "so", "süsen") | | |

The full sign-by-sign transcription is in `work/transcription.txt`.

## Command

Run from the repo root:

```
python3 -I ciphers/hcp-1091/work/decode.py
```

The script checks the SHA-256 of the four scans and decodes the transcription with the key. It prints the literal decode, with the shared letters kept as classes D/G/F/Z. It then checks that every resolved word fits its literal pattern and prints the plaintext and the list of disclosed readings.

## Plaintext (German, writer's spelling, Austrian dialect)

> Lieber Jagas Bua! Du bist also wirklich ernstlich böse? Hab ich dich den so tief gekränkt, das du mir nie verzien wirst? Es ist recht hart von dir. Lebe wol! Lieber Jaga, wen du mir schon nicht verzien kanst, sende dir aber doch noch den süsen Kus.

"verzien" is the writer's spelling of "verzeih'n" (the three dots are the same ie-sign as in "Lieber", "nie", "tief"). The card has no punctuation except "!" after "Bua" and "?" after "böse". I added the rest.

Standard German: Lieber Jägers Bub! Du bist also wirklich ernstlich böse? Hab ich dich denn so tief gekränkt, dass du mir nie verzeihen wirst? Es ist recht hart von dir. Lebe wohl! Lieber Jäger, wenn du mir schon nicht verzeihen kannst, sende [ich] dir aber doch noch den süßen Kuss.

English: Dear hunter's lad! So you are really, seriously cross? Have I hurt you so deeply that you will never forgive me? That is really hard of you. Farewell! Dear hunter, even if you cannot forgive me, I still send you the sweet kiss.

Slovak: Milý poľovníkov chlapče! Si teda naozaj vážne nahnevaný? Ranil(a) som ťa naozaj tak hlboko, že mi nikdy neodpustíš? Je to od teba naozaj tvrdé. Zbohom! Milý poľovník, keď mi už neodpustíš, posielam ti aspoň ten sladký bozk.

## Uncertainties (all disclosed)

1. **Restorations of physically hidden signs:**
   - A5 "ernstlic[h]": the last sign stands on the dark green of the picture, and only a stroke with a blob is visible.
   - C1 "abe[r]": the sign's right half is under the stamp.
   - C2 "de[n]": the sign is fully under the stamp. Only "den" fits the accusative before "süsen Kus".
2. **Readings that rest on word sense:**
   - B5 "re[c]ht": the sign is drawn like 1 (d/t), with a flag on the left only and no crossbar. "recht hart" is the clear sense. This is probably a slip by the writer.
   - B8 "w[o]l": the middle sign looks more like 7 than T. "Lebe wol(hl)" is the sense, and the line is written in fainter ink.
   - B2 "m[i]r": the mark between 3 and 4 is a short tick rather than a round dot.
3. **Homophones seen only in context:**
   - The closed y/4-shaped sign occurs twice, as "so" (A9) and as "süsen" (C3), and gives s both times. Elsewhere s is 7.
   - The J-shaped sign occurs only in "Jagas"/"Jaga" (A2, B10).
   - Shared signs: d/t, g/k, f/v and c/z are each one sign, so the choice between the two letters follows the word.
4. **"Jaga(s) Bua"** is Austrian dialect for "Jäger(s) Bub" (hunter, hunter's boy). It could also be a nickname. The writer and the date are unknown.
5. **Small marks:** B8 has one extra faint dot after "Lebe", and a stray dot stands above its first 0. Both are treated as noise.

## Why I believe it is correct

- One key reads every one of the 27 lines and 52 words as coherent, grammatical Austrian-German text. The text is a lover's plea fitting a picture postcard.
- Repeated words decode the same way every time. Examples are "Lieber" (A1, B9), "verzien" (B3, B13), "dir" (B7, C1), "du mir" and "ich/dich/nicht".
- The vowel system follows Kurrent consistently: u is n with a breve, ü is n with dots, and ö and ä carry dots.
- Apart from the 3 restorations and 3 word-sense readings listed above, every sign was read from the enlarged pixels.

## Response to review 1

Verdict ACCEPT, four minor findings. All four are addressed. The reading of the card is unchanged.

1. Register type and steganography: agreed. I keep the type `MASC`. The section "The card" now says explicitly that the area under the picture-side stamp cannot be inspected on the scans and may hold more text, as on other series where a hidden message under the stamp is common. Writing in the margins and upside down in the sky is the normal layout and not hidden. There is no evidence of a hidden message, so I do not use `MASC + Steganography`.
2. "verzein" against the literal reading: fixed. I removed the special token `...ei` from `work/transcription.txt` and `work/decode.py`. The three dots are now always ie, and the writer's spelling is given as "verzien" (standard German "verzeihen"). The meaning is unchanged.
3. The S-shaped r in B3: agreed. On the enlarged crop (`review/work/B2B4z.png`) the r of B3 "verzien" has the same S-like shape as the r of B4 "wirst". Both are now coded `S`, the writer's variant of r, and the key maps `S` = r. B4 is no longer listed as a word-sense reading. B13 "verzien" has the usual curled 4 (`review/work/B11_14.png`), and is left as 4.
4. Address-side annotations: fixed. The violet handwritten forwarding note (roughly "Schilling…") and the violet rubber stamp ending "…INGERAMT" are now described as postal annotations that are left unread. "Förstla" is labelled as an uncertain reading. None of this is the sender's message or ciphertext.

Re-run after the changes: `python3 -I ciphers/hcp-1091/work/decode.py` prints OK for all four hashes, decodes all 27 lines with no unknown sign, passes the pattern check for all 52 words, and prints the plaintext above with "verzien". The disclosed readings are now 3 restorations (h, r, n) and 3 word-sense readings (B2 i, B5 c, B8 o).
