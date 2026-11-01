# HCP 1179 (cpc_1915-09-26_HU_Mezokovesd_HU_Szomolya_szomolya-01): a rhymed couplet in numbers on a Hungarian postcard

Human solver: Tomáš Pavuk

**Status: the enciphered text is deciphered, with one word not fully understood and two letters taken by word sense; independent review 1 verdict REVISE, findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1179 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1179), from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-01 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Szegedi Janosné, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), which was not consulted. No published solution was found.

The card belongs to a series sent from Mezőkövesd to Szomolya in north-east Hungary during the First World War. It is dated in the open text Mezőkövesd, 1915 IX/26, signed Sz. A., and addressed to Tek. Szegedi Jánosné, Szomolya, Borsod megye, u.p. Bogács, yet it opens "Kedves Margitkám!" ("Dear Margitka!"). A sister card, hcp-1174, is addressed to Margitka Sziber at the same place and signed Árpád in cipher, which favours A. in the signature here, though the pixels also allow K.

The left of the message side is open Hungarian in violet copying pencil, later struck through in brown ink. Only the figures at the foot are enciphered: one row along the bottom edge and a shorter row above its right part. They add a private line to an open note.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

## Method

The figures were transcribed by hand from the highest-resolution original available, on enlargements of 3 to 10 times. No OCR was used. Each sign is a digit followed by an optional mark (dot, colon, comma), and the mark belongs to the sign: 8 is m and 8, is t.

![Left part of the figures (work/crops/rep_left.png)](../work/crops/rep_left.png)

![Right part, with the upper row above the bottom row (work/crops/rep_right.png)](../work/crops/rep_right.png)

The card is too short to break alone, so the key was reconstructed from digit passages on sister cards in the same hand, then applied here. Examples, as filed in those cards' directories: hcp-1174 *Édes Margitkám* and *szívem éled*, hcp-1178 *csókollak téged*, hcp-1175 *(fő)b lövöm magam*.

Reproduction from the repository root (checks source hashes, prints the raw decode): `python3 -I ciphers/hcp-1179/work/decode.py`.

## Key

Monoalphabetic substitution (MASC), with variants. Signs on this card:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| 1 | i | 2. | é | 6, | n |
| 1. | a | 3 | d | 7 | k |
| 1: | e | 3, | r | 7. | sz |
| 1, | b | 4, | g | 8 | m |
| :1 (dots left) | ü | 5. and 5, | l | 8, | t |
| 0 | o | 0, | ö | 8. | t? (variant of 8,) |

Elsewhere in the family, not on this card: 7, = s, 3. = v, 2, = cs, 1' = á, 5 = h, 9 = p, 9, = z.

## Ciphertext and plaintext

Reading order: bottom row left to right, then the upper row. `[ ]` marks a value taken by word sense, not from the pixels.

```text
8 1 6, 3 1: 6, 8,            mindent
8 1: 4, 8, 1: 6, 6, 2. [7]   megtenné[k]
2. 6,                        én
2. 3, 8, 1: 3                érted
1.                           a
5. 1: 4, 7. 1: 1,            legszeb
7 1. 3, 8. 1 8               kart?im
7 :1 5, 3 0, 8               küldöm
6, [2.] 7 1: 3               n[é]ked
```

Hungarian (a rhymed couplet, érted / néked): **Mindent megtenné[k] én érted, a legszeb[b] kar[t?]im küldöm n[é]ked.**

English: I would do anything for you; my finest [card(s)?] I send you.

Slovak: Všetko by som pre teba urobil; moju najkrajšiu [pohľadnicu?] ti posielam.

The unenciphered text, provisional because of the overstriking and not part of the decipherment:

> Kedves Margitkám! Rokoni és baráti szeretetből Második lapot küldöm ... gondolva ... Küldök még én százat is de várom a válaszát is. Poéta én sohasem voltam, Szerelemről nem dalol tam. Bocsásd meg e hibát nekem S fogadd igaz üdvözletem. Kelt Mezőkövesd 1915 IX/26. Sz. A.

English of the legible parts: Dear Margitka! Out of kinship and friendship I send a second card ... I will send a hundred more, but I also await your reply. A poet I have never been, I have not sung of love. Forgive me this fault and accept my true greeting.

Slovak: Drahá Margitka! Z príbuzenskej a priateľskej lásky posielam druhú pohľadnicu ... Pošlem ešte aj sto, ale čakám aj odpoveď. Básnikom som nikdy nebol, o láske som nespieval. Odpusť mi túto chybu a prijmi môj úprimný pozdrav.

A line along the top edge reads roughly "... vasárnap ... nem mehetek megint" ("Sunday ... again I cannot go") and is cut by the edge.

## What remains uncertain

1. **kar[t?]im, not fully understood.** The dot after the 8 is clear. This writer uses a dot for the comma in this same passage (`5.` = `5,`), so `8.` is taken as `8,` = t, literally *kartim*. The proposed sense is a loose or dialect form of *kártya*, "card", because the open text speaks of sending cards. This is not proven: y and an a are unwritten, the 1 is unexplained and no accusative ending appears. *karjaim*, "my arms", is a weak alternative: no sign for j is attested in the family. Reading the dot with the following 1 gives *karmam*, which does not fit.
2. **The blot in megtenné[k].** A blot and smear of about 157 px on the scan, room for 2 or 3 signs, hide an unknown number of signs, possibly a correction, and a comma-shaped mark follows it. The final k is a restoration by word sense only.
3. **n[é]ked.** No dot is visible after the 2; the pixels favour `2,` or nothing, and the key alone gives "ncsked". *néked* (older or dialect *neked*) rests on word sense and the rhyme with *érted*.
4. **`:1` = ü.** Dots left of the stem, on a stain. The same sign is filed on hcp-1174 in *üdvözöllek*.
5. **legszeb** has one sign for bb, a spelling simplification.
6. **Row order.** Bottom row first fits the left margin, the period ending the upper row and the rhyme. The reverse cannot be strictly excluded. A short tick at the extreme top right corner is unexplained.
7. **Sister cards** are cited as filed; hcp-1175 is only partly read.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) read the signs on its own crops, decoded them with its own script from the hcp-1174 table, and confirmed the decipherment; it gave verdict REVISE. Changes made as a result:

- The word first given as *kar[j?]im* became *kar[t?]im*, with `8.` treated as a variant of `8,` and the card sense proposed; the translations changed with it.
- The blot is now described in full, including its width and the comma-shaped mark, and [k] is labelled a restoration.
- The *néked* sign is flagged as read by sense, with the rhyme as evidence. The reviewer noted the rhyme, which the first draft had missed.
- A false statement that plain 5 is l was removed (on hcp-1174 it is h), and quotations from hcp-1174 were conformed to that card's filed reading.
- The signature note now cites the sister cards, and the decoder's output was cleaned up.

The reviewer could not determine what lies under the blot or what the corner tick is, and neither could the solver.
