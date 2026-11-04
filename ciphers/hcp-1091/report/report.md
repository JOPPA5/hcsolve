# HCP 1091: an Austrian love note to August Hradegh in a digit-and-dot cipher

Human solver: Tomáš Pavuk

**Status: deciphered in full (27 lines, 52 words, 189 cipher signs); independent review 1 verdict ACCEPT, no change to the meaning of the text.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1091 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1091), portal name cpc_1886-03-12_AT_Wien_AT_Krems_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient August Hradegh. No transcription or solution was attached.

The address side is in plain German Kurrent and carries no cipher: **An Herrn August Hradegh**, a place line read tentatively as "Förstla" (uncertain, underlined in green), **in Gföhl** (struck through in violet) and **b. Krems** ("near Krems", Lower Austria). It carries four 1-Heller stamps cancelled WIEN. A fifth 1-Heller stamp is on the picture side. The stamps show the portrait and inscription of the 1908 Austrian jubilee issue, so the card was sent in 1908 or later. The date 1886 in the portal file name cannot be right. The year in the postmark is not legible.

There are also two postal annotations in violet ink. Neither is part of the sender's message, and both are left unread: a handwritten forwarding note above "Förstla" (it begins with a capital like S, roughly "Schilling…") and a faint rubber stamp at the top edge ending "…INGERAMT".

The picture side shows a girl in a red dress drinking at a mountain spring. It is signed by the artist at the bottom left, apparently A. Mailick. All of the ciphertext is on this side, in three blocks:

- **A**, 10 lines in the left margin
- **B**, 14 lines in the right margin
- **C**, 3 lines written upside down in the sky above the spring and closed with a triple underline

The ends of lines C1 and C2 run under the picture-side stamp.

![Picture side, turned so that the girl is upright: block A on the left, block B on the right, block C upside down in the sky, ending under the stamp (report/picture-rotated.jpg)](picture-rotated.jpg)

![Address side: August Hradegh, b. Krems, with the violet forwarding note and struck-through Gföhl (source/address-large.jpg)](../source/address-large.jpg)

## Method

This is a new key recovery. No earlier work on this number exists, and a short web search on 2026-11-03 found no published solution. The transcription was made by hand from the full-resolution scan, sign by sign on enlarged crops. No OCR was used.

The breaks came in this order:

1. The ending "· + 8" recurs several times and suggested ich / dich / nicht.
2. The group "0 ··· 6 ·· 4" appears twice, at the start of block A and in the middle of block B. Read as "Lieber", it gives one dot = i, two dots = e and three dots = ie.
3. The words "also", "wirklich", "doch" / "noch", "böse" and "gekränkt" then fixed the rest of the key.

The vowels follow Kurrent handwriting conventions. In Kurrent, u is written as an n with a breve over it. Here the sign 2 (n) with a raised breve or bar is u, and 2 with two raised dots is ü. The o-sign with two dots is ö, and the a-dash with two dots is ä.

The reproduction script checks the SHA-256 of the scans and decodes the transcription. It prints a literal reading in which the four shared signs are kept as classes (D = d/t, G = g/k, F = f/v, Z = c/z). It then checks that every word of the resolved text fits its literal pattern.

## Key

Monoalphabetic substitution. Consonants are written as digits or digit-like signs, and vowels as dots and dashes on the line or as marks on a sign. Four signs each stand for two related letters, and the word decides which.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| 0 | l | 7 | s | one dot | i |
| 1 | d / t | 8 | h | two dots | e |
| 2 | n | 9 | f / v | three dots | ie |
| 2 with raised breve or bar | u | x | w | dash | a |
| 2 with two raised dots | ü | + | c / z | dash with two dots | ä |
| 3 | m | 1 with top bar (T) | o | ! and ? | themselves |
| 4 (curled top), or its S-shaped variant | r | T with two dots | ö | | |
| 5 | g / k | J-shaped sign | j | | |
| 6 | b | closed y-shaped sign | s | | |

The J-shaped sign occurs only in "Jaga(s)". The closed y-shaped s occurs only in "so" and "süsen". Elsewhere s is 7. The S-shaped variant of r occurs in B3 and B4.

## Plaintext

Transcription, as signs (words separated by " / "; [x] marks a sign hidden by the stamp or the picture and restored):

```text
A1  0 ... 6 .. 4                 lieber
A2  J - 5 - 7 / 6 2u - / !       jagas bua !
A3  1 2u / 6 . 7 1               du bist
A4  - 0 7 T / x . 4 5 0 . + 8    also wirklich
A5  .. 4 2 7 1 0 . + [8]         ernstlic[h]
A6  6 T: 7 .. / ?                böse ?
A7  8 - 6 / . + 8                hab ich
A8  1 . + 8 / 1 .. 2             dich den
A9  Y T / 1 ... 9                so tief
A10 5 .. 5 4 "- 2 5 1            gekränkt
B1  1 - 7 / 1 2u                 das du
B2  3 . 4 / 2 ...                mir nie
B3  9 .. S + ... 2               verzien
B4  x . S 7 1 / .. 7             wirst es
B5  . 7 1 / 4 .. 1 8 1           ist recht
B6  8 - 4 1 / 9 T 2              hart von
B7  1 . 4                        dir
B8  0 .. 6 .. / x 7 0            lebe wol
B9  0 ... 6 .. 4                 lieber
B10 J - 5 - / x .. 2             jaga wen
B11 1 2u / 3 . 4                 du mir
B12 7 + 8 T 2 / 2 . + 8 1        schon nicht
B13 9 .. 4 + ... 2               verzien
B14 5 - 2 7 1                    kanst
C1  7 .. 2 1 .. / 1 . 4 / - 6 .. [4]   sende dir abe[r]
C2  1 T + 8 / 2 T + 8 / 1 .. [2]       doch noch de[n]
C3  Y 2: 7 .. 2 / 5 2u 7               süsen kus
```

German, in the writer's spelling (Austrian dialect, single consonants; the "!" after "Bua" and the "?" after "böse" are on the card, the rest of the punctuation is editorial):

**Lieber Jagas Bua! Du bist also wirklich ernstlich böse? Hab ich dich den so tief gekränkt, das du mir nie verzien wirst? Es ist recht hart von dir. Lebe wol! Lieber Jaga, wen du mir schon nicht verzien kanst, sende dir aber doch noch den süsen Kus.**

Standard German: Lieber Jägers Bub! Du bist also wirklich ernstlich böse? Hab ich dich denn so tief gekränkt, dass du mir nie verzeihen wirst? Es ist recht hart von dir. Lebe wohl! Lieber Jäger, wenn du mir schon nicht verzeihen kannst, sende [ich] dir aber doch noch den süßen Kuss.

English translation: **Dear hunter's lad! So you are really, seriously cross? Have I hurt you so deeply that you will never forgive me? That is really hard of you. Farewell! Dear hunter, even if you cannot forgive me, I still send you the sweet kiss.**

Slovak translation: **Milý poľovníkov chlapče! Si teda naozaj vážne nahnevaný? Ranil(a) som ťa naozaj tak hlboko, že mi nikdy neodpustíš? Je to od teba naozaj tvrdé. Zbohom! Milý poľovník, keď mi už neodpustíš, posielam ti aspoň ten sladký bozk.**

Notes on the reading:

- "Jaga" and "Bua" are Austrian dialect for Jäger ("hunter") and Bub ("lad"). This fits an address to a forester's place near Gföhl. It could also be a nickname.
- "verzien" is the writer's spelling of verzeih'n ("forgive"). The three dots are the same ie-sign as in "Lieber", "nie" and "tief".
- The writer uses single consonants throughout (wen, den, das, kanst, süsen, Kus) and writes "wol" for wohl. These are kept as written.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1091/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 of the four scans, decodes the transcription in work/transcription.txt with the key, prints the literal reading of all 27 lines, checks every one of the 52 resolved words against its literal pattern, and prints the plaintext and the list of disclosed readings. It does not read the images. The transcription step is manual and was checked independently in review.

## Uncertainties

- **Three restored signs, hidden on the card.** A5 "ernstlic[h]": the last sign stands on the dark green of the picture, and only a stroke with a blob is visible. C1 "abe[r]": the right half of the sign is under the stamp. C2 "de[n]": the sign is wholly under the stamp, and "den" is the only form that fits before "süsen Kus".
- **Three readings that rest on word sense.** B2 "m[i]r": the vowel mark is a short tick rather than a round dot. B5 "re[c]ht": the sign is drawn like 1 (d/t), with a flag on the left only and no crossbar, probably a slip by the writer. B8 "w[o]l": the middle sign has its bar on the left, like 7, rather than the centred bar of the o-sign. The line is in fainter ink.
- **Shared signs.** d/t, g/k, f/v and c/z are each one sign, so the choice between the two letters comes from the word. Every word allows only one choice.
- **Homophones seen only a few times.** The closed y-shaped s appears twice and the J-sign twice. Both are fixed by the words they occur in.
- **Under the picture-side stamp.** The scans cannot show what is under this stamp. On some other postcard series a hidden message under the stamp is common, so further text here cannot be excluded. There is no evidence of one, so the cipher type is given as MASC and not MASC + Steganography. Writing in the margins and upside down in the sky is the normal layout of these cards and is not hidden.
- **Address side.** The place line "Förstla" is an uncertain reading. The violet forwarding note and rubber stamp are postal annotations and are left unread. They are not part of the message.
- **Dating and persons.** The card is dated by the 1908 jubilee stamps (1908 or later). The postmark year is not legible. The writer is unknown, and nothing more is known of August Hradegh.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command and got the claimed plaintext. It made its own enlarged crops of the scan, read all 27 lines sign by sign, and decoded its own transcription with its own single-value key. Its reading agreed with the solver's on every sign, and the key covers the whole ciphertext with no unknown sign. It checked each restoration and word-sense reading on the pixels, and confirmed that the stamp design points to 1908 or later. Its four findings were minor and are all addressed:

- **Steganography.** It is now stated that the area under the picture-side stamp cannot be inspected and may hold more text. The type stays MASC because there is no evidence of hidden text.
- **"verzein" against "verzien".** The first version read the three dots of B3 and B13 as "ei" through a special exception. That exception is removed. The three dots are always ie, and the writer's spelling is given as "verzien". The meaning is unchanged.
- **S-shaped r.** The r in B3 has the same S-like shape as the r in B4. Both are now coded as the writer's variant of r, and B4 is no longer listed as a word-sense reading.
- **Address-side annotations.** The violet forwarding note and rubber stamp are now described, and "Förstla" is labelled as uncertain.

No word of the meaning changed as a result of the review.

## Sources

- HC Portal record 1091, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1091 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3333/cpc_1886-03-12_AT_Wien_AT_Krems__pic.jpg (full resolution, work/hires/) and its large conversion (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/3334/cpc_1886-03-12_AT_Wien_AT_Krems__adr.jpg (full resolution, work/hires/) and its large conversion (source/address-large.jpg).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.
