# HCP 1140 (cpc_1915-12-10_HU_Mezokovesd_HU_Szomolya_szomolya-10): "I will write as long as I live", a Hungarian wartime postcard in digits

Human solver: Tomáš Pavuk

**Status: deciphered in full (125 of 125 cipher signs: 123 by the key as written, 2 by word sense, both disclosed); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1140 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1140), portal name cpc_1915-12-10_HU_Mezokovesd_HU_Szomolya_szomolya-10, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), which was not consulted, so it is unknown whether the article discusses this card. No published solution was used.

It is a picture postcard of a girl's head with a ribbon in her hair (print number 672/5, "Printed in Saxony"), written at Mezőkövesd in north-east Hungary and dated 10 December 1915, in the second year of the First World War. It is addressed in plain writing to **Tek. Szépreménnyü Sziber Margitka kisasszonynak, Szomolya, u. p. Bogács** ("To the Honoured Miss Margitka Sziber, of fair promise, Szomolya, post office Bogács"). The postmark shows MEZŐK… and 915 DE…; the day cannot be read. The stamp is a Hungarian 5 fillér.

The card belongs to the group of cards from Mezőkövesd to Margitka Sziber at Szomolya (hcp-1135 to 1179). This one is signed **Sz. A.** The message side mixes open Hungarian in ink with passages in digits: a salutation, a whole paragraph of complaint, and the last word of a verse. A faint pencil X crosses the message, and the name in the address has been struck through in blue. These later marks hide no sign. The picture side has no writing.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual. No transcription was attached, so the digits were read sign by sign from the un-converted portal original, enlarged 2 to 7 times. No OCR was used. Each sign is a digit plus an optional mark (comma, dot, two dots, a high dot, or a dot to the left), and the mark belongs to the sign, so `3` is d and `3,` is r.

![Second salutation, left part: the comma under the second 3 makes the slip Kedres (work/crops/r3a.png)](../work/crops/r3a.png)

The key was not recovered on this card. It was transferred from the finished sister cards hcp-1174 and 1179, with `.1` = u, `4.` = gy and `6` = j, which also stand on the finished cards hcp-1152, 1168 and 1170. Applied without adjustment, it turns 123 of the 125 signs into continuous Hungarian. All 22 distinct signs are in the key.

The reader can reproduce the decoding from the repository root with `python3 -I ciphers/hcp-1140/work/decode.py`. It checks the hashes of the scans, decodes every sign, asserts each word and prints the text. The open text is typed into the script, so only the cipher signs are reproduced by decoding.

## Key

Monoalphabetic substitution (MASC), Hungarian. Only key passages are enciphered. Vowel length is not marked for i, o and u.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| 0 | o | 3 | d | 6 | j |
| 1 | i, í | 3, | r | 6, | n |
| 1. | a | 3. | v | 7 | k |
| 1: | e | 4, | g | 7, | s |
| 1' (one high dot) | á | 4. | gy | 7. | sz |
| .1 (dot to the left) | u | 5 | h | 8 | m |
| 1, | b | 5, | l | 8, | t |
| 2. | é | | | | |

Hungarian gy and sz have one sign each. The card has plain u in `ugy` and `ugysem`; the plaintext prints the normal spellings `úgy`, `úgysem`.

## Plaintext

Ciphertext as transcribed:

```text
7 1: 3 3. 1: 7, 8 1. 3, 4, 1 8, 7 1' 8 !
(open text)
7 1: 3 3, 1: 7, 8 1. 3, 4, 1 8, 7 1' 8 8 1' 3,
.1 4. 5, 1' 8, 7. 1 7 5 0 4. 5 1 1' 1, 1. 7 2. 3,-
5, 1: 7 5 0 4. 1 3, 6 1' 5, . 8 1' 3, 6, 1: 8 1 3, 7.
6, 0 2. 6, 1 3, 0 7 8 1 4, 2. 5, 1: 7 5 1 7
1: 7 8, .1 4. 7, 1: 8 7, 0 7 1' 1 4, 1, 1 3, 0 8
1: 5, 3. 1 7, 1: 5, 6, 1 >
(open verse) Igazán 7. 1: 3, 1: 8, 6, 1 !
```

Hungarian, with enciphered passages in square brackets. Punctuation inside the brackets is editorial.

```text
[Kedves Margitkám]!
A legtisztább szívből üdvözöllek mindnyájatokat
```

[Kedres (= Kedves) Margitkám! Már úgy látszik, hogy hiába kérlek, hogy írjál. Már nem írsz, no én írok, míg élek, hisz eszt (= ezt) úgysem sokáig bírom elviselni.]

```text
Féld az Istent, szeresd a dalt,
Növelj virágokat!
Isten emel, dal vigasztal,
Virág illatot ad!
```

```text
Hiába, hiába
Nem tudlak feledni...
Csak tégedet foglak
Örökké keresni,
Igazán [szeretni]!
```

Sz. A.

Számtalanszor csókollak maradtam) Mezőkövesd, 1915. XII/10

**English translation**

```text
[Dear Margitka]!
With the purest heart I greet you all.
```

[Dear Margitka! It already seems that I beg you in vain to write. You no longer write; well, I will write as long as I live, since I cannot bear this for long anyway.]

```text
Fear God, love song,
Grow flowers!
God lifts up, song consoles,
A flower gives fragrance!
```

```text
In vain, in vain,
I cannot forget you...
You alone I shall
Seek for ever,
Truly [love]!
```

Sz. A.

Countless times I kiss you, I remain) Mezőkövesd, 10 December 1915

**Slovak translation**

```text
[Milá Margitka]!
Z najčistejšieho srdca vás všetkých pozdravujem.
```

[Milá Margitka! Už to vyzerá tak, že ťa márne prosím, aby si písala. Už nepíšeš, no ja budem písať, kým budem žiť, veď toto aj tak dlho neznesiem.]

```text
Boj sa Boha, miluj pieseň,
Pestuj kvety!
Boh povznáša, pieseň utešuje,
Kvet dáva vôňu!
```

```text
Márne, márne,
Nemôžem ťa zabudnúť...
Len teba budem
Naveky hľadať,
Naozaj [milovať]!
```

Sz. A.

Nespočetnekrát ťa bozkávam, zostal som) Mezőkövesd, 10. decembra 1915

## What remains uncertain

Cipher signs:

1. **`hisz eszt` (2 signs read by sense).** Both 7s in these words are plain crossed 7s with no dot, so the table alone gives `hik ekt`, which is not Hungarian. They are read as `7.` = sz with the dot left off. `5 1 7` for `hisz` also stands on hcp-1152, and the writer's `aszt` for azt on hcp-1151, 1154 and 1161 supports the spelling `eszt` for ezt. The rest of the sentence does not depend on them.
2. **`Kedres`.** The second 3 in the second salutation clearly has a comma, which makes r. The same word in the first salutation has `3.`, so this looks like a slip. It is printed as written, with the normal form beside it.
3. **First `Margitkám`.** The 3 and the 4 overlap and the dot of `1.` is a blot, but the marks can be seen and the word is the same as in the second salutation.
4. **Off-key marks.** A dot before the 8 on row 5 is taken as a full stop after `írjál`, a small dot left of the first 7 on row 3 as a speck or stop, and the hyphen at the end of row 4 as a word break (`kér-lek`). `no` could be `nó`; it is read as the interjection.

Open text:

5. **`maradtam)`.** Written over the printed copyright mark and 672/5, so the middle is cramped. The reading was compared with hcp-1170 of 14 December 1915, which closes with the same phrase. On the red channel m-a-r-a, an `ol`-shaped d, a crossed t and `am` can be seen, but the pixels alone do not settle every letter. The word stands alone and the rest of the line reads. The `)` has no opening partner.
6. **`üdvözöllek`.** The card breaks it as `üdv-` / `vözöllek`, with the v written twice. The normal form is printed.
7. **Marks with no text value.** Rule lines between the sections, thin diagonal strokes right of the second verse and beside Sz. A., a curve under the t of `dalt` (most likely a large comma), the `>` ending the cipher block, and the `)`. None of them carries a sign. The purpose of `>` and `)` is unknown.
8. **Date.** The last year digit is a looped 5, and the postmark shows 915 DE…, with the day illegible.
9. **Verses.** No printed source was searched for, so it is not known whether they are the writer's own.
10. **The sender.** Only the initials Sz. A. stand on this card. Who they stand for is not established here.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the command, typed its own sign-by-sign reading of all ten cipher rows from its own crops, and decoded it with its own script. It agreed with every sign. It decoded to the same text, with `hik ekt` where the solver reads `hisz eszt` and with `kedres` in the second salutation. It also checked the open text, date and key against the sister cards. Its verdict was ACCEPT, with six minor points:

1. The doubled v in `üdv-vözöllek` was not mentioned. It is now.
2. `.1` was given as "u, ú", though the card has plain u. The key now says u, and `úgy` is marked as the normal spelling. Support from hcp-1152 and 1168 was added.
3. The script reported 23 distinct signs because it counted a working label. It now reports 22, the true figure.
4. An alternative `így` for the first `úgy` was overstated, because the dot is clear at 6x. It was dropped.
5. Some non-text marks were undisclosed. They are now listed.
6. The type label for the register is MASC, and the `hisz eszt` and `Kedres` notes carry into this report.

No sign of the transcription and no word of the deciphered text changed. The reviewer could not verify the HistoCrypt article, the postmark day or the meaning of `>` and `)`, and neither could the solver.
