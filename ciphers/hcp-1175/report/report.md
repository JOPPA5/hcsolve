# HCP 1175 (cpc_1915-10-25_HU_Mezokovesd_HU_Szomolya_szomolya-03): a Hungarian love card with a digit block

Human solver: Tomáš Pavuk

**Status: the digit block is deciphered in full (57 of 57 signs) and every written word on the card reads. One line, `mert . . . m . . .`, is a sentence ending the writer withheld behind dots; it cannot be read and its meaning is unknown. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1175 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1175), portal name cpc_1915-10-25_HU_Mezokovesd_HU_Szomolya_szomolya-03, from Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Szegedi Janosné, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166); this was not read for this card, and no published solution was used.

The picture side is a sepia studio photograph of an embracing couple. All the writing is on the address side. The address is in plain writing: **Tek. Szegedi Jánosné urasszonynak / Szomolya / Borsod m. / u. p. (Bogács)**, that is, to Mrs János Szegedi at Szomolya, Borsod county, post office Bogács. The card has a 2-fillér and a 3-fillér Hungarian stamp; the postmark shows OKT 25, with the year smudged. A pen note in the top corner gives `1915. (X.25.)`. The left half holds a greeting, five lines of digits, a violet `(Margitkám!)`, a four-line verse and a few closing lines signed Sz. A. Later, someone struck through nearly all the writing, and the address, in brown ink. It remains readable beneath the strokes.

The card belongs to the Mezőkövesd family of cards (HCP 1135 to 1179, Hungarian, 1915 to 1916), most of them to Margitka Sziber at Szomolya. Several carry short enciphered passages in a digit-plus-mark key, which was reconstructed on HCP 1174, 1178 and 1179. HCP 1174 is signed Árpád in cipher, and this writer's cards are signed Sz. A.

![Address side: greeting, digit block, violet (Margitkám!), struck-through verse, and the address to Szegedi Jánosné (work/rev/adr_ov.jpg)](../work/rev/adr_ov.jpg)

## Method

A first attempt on 2026-11-01 (also Claude Opus 5.5) stalled and stayed partial: it forced the word `hadifelszerelés` onto line 1, which inverted many key values, and it misread three signs. The second attempt on 2026-11-02 dropped that key, started from the table of HCP 1174, and read every sign again from new 2x and 5x crops of the unconverted high-resolution scan, in colour and in the red channel, which suppresses the brown strokes.

With the HCP 1174 table, line 1 gives `ha még e?szer el`, so the sign `4.` must be gy, and the sentence then runs on to the end of the block. 52 of the 57 signs decode by that table unchanged. The other 5 use four signs outside it, which the key tables of finished sister cards (HCP 1138, 1165, 1167) give with the same values. The transcription is manual; no OCR was used.

Three places on the card needed a close look:

- Line 2, sign 4 and line 4, sign 1 are `.1`, with a dot left of the 1. On line 2 the dot stands clear of the 3 before it, and `3.` plus `1` would give `invilok`, which is no word. On line 4 the dot is a dark blob of the writer's ink, above a brown stroke.
- Line 3, last sign, is `9,` = z. Its comma rises higher than usual. Bare `9` = p would give `ap`, which is no word.
- Line 4 reads bare `4` then `0,`, and `1,` then `5,`: the comma after the 4 belongs to the 0, giving f + ő, and the next comma belongs to the 1, giving b.

The reviewer read all 57 signs independently and wrote a separate decoder with the key parsed from the HCP 1174 table. The token lists came out identical.

![The digit block and the text around it, from the high-resolution scan (work/block.jpg)](../work/block.jpg)

## Key

Each letter is a digit plus an optional mark, and the mark changes the letter, so a digit with its mark is one sign. There are no word divisions. Hungarian digraphs such as gy and sz have one sign. The cipher is a monoalphabetic substitution.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o | `2.` | é | `6,` | n |
| `0,` | ö, ő | `3` | d | `7` | k |
| `1` | i | `3,` | r | `7,` | s |
| `1.` | a | `3.` | v | `7.` | sz |
| `1:` | e | `4,` | g | `8` | m |
| `.1` (dot left of the 1) | u, ú (s) | `4.` | gy (s) | `8,` | t |
| `1,` | b (s) | `4` | f (s) | `9,` | z |
| `5` | h | `5,` | l | | |

(s) = not in the HCP 1174 table, attested on sister cards HCP 1138, 1165 and 1167.

Ciphertext, line by line:

```text
5 1. 8 2. 4, 1: 4. 7. 1: 3, 1: 5,
1 6, 3 .1 5, 0 7 2. 7, 0 3 1. 6, 1: 8
2. 3, 5 1: 8, 1: 7 1. 7 0 3, 1. 9,
.1 8, 0 6, 4 0, 1, 5, 0, 3. 0, 8
8 1. 4, 1. 8
```

Decoded by line:

```text
hamégegyszerel
indulokésodanem
érhetekakoraz
utonföblövöm
magam
```

## Plaintext

Square brackets mark the enciphered sentence. Spelling is as written.

```text
1915. (X.25.)   [pen, top corner]
Kedves Ángyika!

[Ha még egyszer elindulok és oda nem érhetek akor az uton főblövöm magam]
(Margitkám!)   [violet, beside the box]

A szellő is csak azt sugja,
Amely tőlem hozzád téved,
A gerle is csak azt bugja:
Mikor látlak ujra téged?

Távolban a vágyam-
nekem;
Ha te is itt volnál
velem.   [boxed:] Légy szives irjál
mert . . . . . . . . m . . . . .
Sz. A.
```

In normal spelling the cipher sentence is: Ha még egyszer elindulok és oda nem érhetek, akkor az úton főbelövöm magam.

## English translation

Dear Ángyika (a kin word: sister-in-law or aunt by marriage)!

[If I set out once more and cannot get there, then I will shoot myself in the head on the way.] (My Margit!)

Even the breeze whispers only this, / the one that strays from me to you; / the turtle-dove too coos only this: / when will I see you again?

My longing is far away, for me; / if only you too were here with me. Please be so kind as to write, because . . . m . . . (the rest withheld by the writer) Sz. A.

## Slovak translation

Milá Ángyika (príbuzenské slovo: švagriná alebo teta cez manželstvo)!

[Ak sa ešte raz vydám na cestu a nedostanem sa tam, tak sa cestou strelím do hlavy.] (Moja Margitka!)

Aj vánok šepká len to, / ktorý odo mňa k tebe zablúdi; / aj hrdlička vrká len to: / kedy ťa zas uvidím?

Moja túžba je ďaleko, pre mňa; / keby si aj ty bola tu so mnou. Buď taká dobrá a napíš, lebo . . . m . . . (zvyšok pisateľ zamlčal) Sz. A.

## What remains uncertain

- **The dotted line, `mert . . . m . . .`.** After `mert` ("because") the card has only dots and short ticks and one written m: 8 marks, the m, 5 marks. The brown strokes hide no other letters. The marks are not letters, so nothing written is unread, but the end of the sentence is withheld and **its meaning is unknown**. Treating this as one single unread item, and so the card as complete, is a judgement call about the completeness rule, not a fact about the card, because the line is one even run with no visible word space and everything else reads. On a stricter reading the card is partial.
- **A conjecture, not a reading.** 8 + m + 5 is the letter count of `főbelövöm magam`, the end of the cipher sentence, with the m in the place of the m of `-lövöm`. That would give "write, because I will shoot myself". A count this short proves little. The tallest mark does fall on the b, but the l is low, and the raised marks after the m do not fit `agam`. It is not in the plaintext.
- **Who the digits are for.** The card is addressed to Szegedi Jánosné and opens to Ángyika, a kin word, and HCP 1165 notes that a personal name is not excluded. `(Margitkám!)` stands beside the box. That Ángyika is the addressee, and that the digits are meant for Margit, are inferences from placement and from sister cards.
- **Spelling.** `akor` for akkor and `főb` for főbe are kept as written. Single letters for double ones fit this writer's habit on HCP 1178 and 1179. The vowel length of ő and ú comes from word sense, as the cipher does not show it. `érhetek` is literally "I may reach".
- **`Távolban a vágyam- / nekem`.** The letters are clear, but the sense is slightly odd, and it is translated plainly. No printed source of the verse was found.
- **The sentence itself.** It reads as a lover's exaggeration, and nothing outside the card tests it. Sister cards fit: on HCP 1174 the writer apologises for not coming to Szomolya, and the top line of HCP 1179 seems to say he cannot go again.
- **The date.** The pen note is probably the writer's own, by its ink and the form of its 5. The third digit of the year has a blot and a crossing stroke, so 1915 rests partly on the card family and the portal file name. The postmark year is smudged.
- **The brown overstriking.** Who made it, and when, is unknown.
- **Not checked.** The HistoCrypt article linked by the portal was not read.

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1175/work/decode.py
```

It checks the SHA-256 of all four scans, decodes work/transcription2.txt, asserts the result letter by letter, and prints the sign counts and the card. The open text in its output is hard-coded, so the command reproduces only the decoding of the digits.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) tried to refute the solution. It ran the command, read all 57 signs on its own crops, decoded them with its own script and key parser, reread the open text and address through the brown strokes, and counted the dotted line independently. It found no disagreement on any sign and gave the verdict **ACCEPT**, with five minor findings:

- The dotted line is a judgement call and must be described as one. Done above.
- The four signs outside the HCP 1174 table had been called new; they are ordinary family signs. Corrected, with citations.
- The date note had been called pencil; it is pen, probably the writer's. Corrected, with a note on the blotted digit.
- `Ángyika` had not been glossed as a kin word. Gloss added.
- The dots had been described wrongly: three marks are raised, not two. Corrected, with the misfit in the conjecture stated.

No sign, key value or word of the plaintext changed as a result of the review.
