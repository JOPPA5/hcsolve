# HCP 1038 (cpc_1908-10-16_DE_-Altst_HU_Arad_): a Hungarian apology from Sanyi to Jolika, Dresden 1908

Human solver: Tomáš Pavuk

**Status: deciphered in full (135 of 135 cipher signs); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1038 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1038), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, language Unknown, sender Unknown, recipient Meistrovich Jolanka, with no transcription or solution attached. The only reference given is the general HistoCrypt article on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166).

The card is a picture postcard **"Dresden – Blick von der Kreuzkirche"** (view over the roofs of Dresden from the Kreuzkirche, with the Frauenkirche and the Albertbrücke; publisher Alfred Hartmann, Dresden-A., no. 1658). On the picture side the writer added the plain date **1908. Okt. 16.** The card was posted at Dresden-Altstadt with a German 5-Pfennig Germania stamp, stuck upside down.

The address is in plain Hungarian: **Őnagysága Meistrovich Jolánka úrleánynak, Arad, Bockó [?] tér 7., Ungarn** ("To Her Ladyship Miss Jolánka Meistrovich, Arad, Hungary"). The street name is partly covered by the collection stamp and is uncertain (Bockó / Bocskó / Boczkó).

![Picture side: Dresden – Blick von der Kreuzkirche, with the handwritten date 1908. Okt. 16. (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: the digit cipher written at 90 degrees to the address on the left half, the plain signature "Szívélyesen üdvözlöm Sanyi", and one cipher line along the bottom edge (source/address-large.jpg)](../source/address-large.jpg)

The message on the left half of the address side is written at 90 degrees to the address, in eight short lines of digits with small marks. Under it, in plain Hungarian at the same angle, is the signature **Szívélyesen üdvözlöm / Sanyi** ("Kind regards, Sanyi") with a paraph. One more cipher line runs along the bottom edge, upright in the address orientation.

## Method

The transcription is manual, from the un-converted high-resolution scan of the address side (work/hires/, 3469 × 2298 pixels), rotated and enlarged sign by sign. No OCR was used and the portal supplied no transcription.

Each sign is a digit alone or a digit with a mark: a comma below, a dot on the baseline, a dot at mid height, a dot at the top, two dots, a colon, or a dot placed before the digit. The marks belong to the signs; there are no word divisions and no punctuation.

The repository already holds a digit-plus-mark key of the same kind, reconstructed independently on the Mezőkövesd cards to Margitka Sziber (HCP 1174, 1178, 1179, Hungarian, 1915–16). Applied here, it gave at once `2. 3 1: 7,` = ÉDES and `5 1. 5, 5, 0 8, 8, 1. 8` = HALLOTTAM. The remaining values (i, b, gy, j, ny, one l) followed from words, and the enciphered signature `7, 1. 6. 1..` = SANYI matches the plain signature.

The reproduction command, run from the repository root:

```sh
python3 -I ciphers/hcp-1038/work/decode.py
```

It checks the SHA-256 hashes of the four scans, decodes all 135 transcribed signs with the key, prints each line as written next to the reading, and lists the places where the reading departs from the letters as written. That list comes from comparing against a reading stored in the same script, so it documents the solver's choices; it is not independent evidence. The independent check is the reviewer's own transcription and decoder (see the review summary).

## Key

Monoalphabetic substitution, one sign per letter (register label: MASC).

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| `0` | o, ó | `3` | d | `6` | j |
| `1..` (two dots) | i | `3,` | r | `6,` | n |
| `1.` (baseline dot) | a | `3.` | v | `6.` | ny |
| `1·` (mid-height dot) | a, á | `4,` | g | `7` | k |
| `1'` (dot at top) | á | `4.` | gy | `7,` | s |
| `1:` | e | `5` | h | `7.` | sz |
| `·1` (dot before) | ü | `5,` | l | `8` | m |
| `1,` | b | `2` | l (once) | `8,` | t |
| `2.` | é | `2,` | cs | `9` | p |
| `9,` | z | | | | |

135 cipher signs, 28 distinct, none unmapped. Twenty-one values agree with the Mezőkövesd key (among them 0 o, 1. a, 1: e, 1' á, 2. é, 2, cs, 3 d, 3, r, 3. v, 4, g, 5 h, 5, l, 6, n, 7 k, 7, s, 7. sz, 8 m, 8, t, 9 p, 9, z). New on this card: `1..` i (the Mezőkövesd cards write plain `1`), `1,` b, `4.` gy, `6` j, `6.` ny, `2` l; ü is written with the dot before the 1 (Mezőkövesd `:1`). This card is seven years older than the Mezőkövesd cards and goes to a different person, so the shared system is noteworthy; the connection between the writers is not known.

## Plaintext

Signs as transcribed, line by line (`|` marks the word breaks inserted by the solver; the card has none; `1*` = mid-height dot, `^1` = dot before the 1):

```text
2. 3 1: 7, | 6 0 2 1.. 7 1* 8
5 1. 5, 5, 0 8, 8, 1. 8 | 6, 1. 4. 0 6, | 7 1.. 7 1. 9 0 8, 8, | 8 1.. 1. 8, 8,
1* 8 | 1.. 4, 1* 9, 1' 6, | 6, 1. 4. 0 6, | 7, 1. 6 6, 1* 5, 0 8 | 3 1: | 2. 6, 1: 8
1.. 7, | 4, 0 6, 3 0 5, 8, 1. 8 | 5 0 4. | 2. 3 1: 7, 1. 9 6 1. | 7 1: 9,
2. 1, 1: | 7 1: 3, ^1 5, 6, 1: 7 | 1. | 5, 1. 9 0 7
7, 0 7 7. 0 3, | 2, 0 7 0 5, 0 8
7, 1. 6. 1..
3. 1* 3, 0 7 | 3. 1* 5 1* 7. 8,      (bottom edge)
```

Letters as written:

```text
édes jolikam
hallottam nagyon kikapott miatt
am igazán nagyon sajnalom de énem
is gondoltam hogy édesapja kez
ébe kerülnek a lapok
sokszor csokolom
sanyi
varok vahaszt
```

Normalized Hungarian (accents, capitals, punctuation and word division editorial):

**Édes Jolikám! Hallottam, nagyon kikapott miattam. Igazán nagyon sajnálom, de én nem is gondoltam, hogy édesapja kezébe kerülnek a lapok. Sokszor csókolom Sanyi**

Plain: **Szívélyesen üdvözlöm Sanyi**

Bottom edge, cipher: **Várok választ.**

English translation: **Dear Jolika! I heard you were badly scolded because of me. I am truly very sorry, but I never thought that the cards would get into your father's hands. Many kisses, Sanyi. — Kind regards, Sanyi. — I await your reply.**

Slovak translation: **Milá Jolika! Počul som, že ste kvôli mne veľmi dostali vynadané. Naozaj ma to veľmi mrzí, ale ani som si nepomyslel, že sa lístky dostanú do rúk vášmu otcovi. Mnohokrát vás bozkávam, Šaňi. — Srdečne vás pozdravujem, Šaňi. — Čakám odpoveď.**

Notes on the reading:

- Jolika (with the possessive Jolikám, "my Jolika") is a pet form of Jolánka, the addressee; Sanyi is the pet form of Sándor.
- The writer uses the polite third person throughout (kikapott, édesapja, csókolom), the usual way for a young man to address an unmarried young lady.
- The content explains the cipher: earlier cards from Sanyi fell into the hands of Jolánka's father, who scolded her, and this card is enciphered to avoid a repeat.

![Bottom-edge line 3.1·3,07 3.1·51·7.8, = várok vahaszt, read as "Várok választ"; the 5 has no comma (review/work/bottom.png)](../review/work/bottom.png)

## Uncertainties

- **vahaszt → választ.** In the bottom-edge line the 5 has no comma beneath it even at 4–5× enlargement, so as written it is h (`5`), not l (`5,`). Read as "választ" by sense, a slip of the writer. This is the only letter on the card that does not decode as written; solver and reviewer agree on the pixels.
- **`2` = l.** It occurs only once, in Jolikám; elsewhere l is `5,`. That one value rests on word sense (the name of the addressee); the other six signs of the word decode by the table.
- **"de énem".** The signs `3 1: 2. 6, 1: 8` are clear and give "de énem"; read as "de én nem", one n written for two.
- **Accents.** á is written `1'` once (igazán), while `1·` stands for both a and á; ó is written as plain o (csókolom). Long vowels are restored by sense; no letter identity depends on them. The baseline and mid-height dots of `1.` / `1·` grade into each other, and both are a-type, so no reading depends on telling them apart.
- **Under the stamp.** The 5-Pf stamp is still attached (upside down), so whatever may be written under it cannot be seen on the scan; nothing shows through or around the perforations. In this collection hidden writing under the stamp is common: on the Árokszállás postcards to Tóth Jolánka there is almost always a plain or enciphered message under the stamp. This card is to a different Jolánka (Meistrovich, Arad) and uses a different cipher, and there is no evidence of hidden writing on it, so the type stays MASC. The decipherment is complete for everything visible, but not for the stamp area, which could only be checked on the physical card. The upside-down stamp may also be a "stamp language" sign; it is not interpreted here.
- **Address.** The street name (Bockó / Bocskó / Boczkó tér 7.) is partly covered by the collection stamp.
- **People.** The sender's surname and the identities of Sanyi and of Jolánka Meistrovich are not established beyond the address.
- **Prior publication.** The portal status is Not solved and no solution is attached; the HistoCrypt article linked from the portal was not checked card by card. No published reading of this card was found.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to SOLUTION.md), made its own crops of the high-resolution scan, transcribed all 135 signs itself before comparing (full agreement, including every mark that carries the key), and decoded its own transcription with its own key table and script, getting the same text. It compared the key with the Mezőkövesd key, confirmed on the pixels the missing comma in "vahaszt", the plain `2` in Jolikám and the "de énem" haplography, and found no other writing on the picture side. Its four findings were minor:

1. **Orientation of the bottom-edge line.** The solver had called it "upside down"; it is upright in the address orientation, at 90 degrees to the message. Corrected.
2. **Steganography / stamp.** In view of the collection's habit of hiding text under the stamp, the reviewer asked that the possibility be stated and that the card not be called complete for the stamp area, while keeping the type MASC. Done (see Uncertainties).
3. **Self-referential check.** The script's assertion only compares the decoding with the solver's own reading; this report presents it as such.
4. **Street name.** Marked as uncertain.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1038, General, Description and Attachments tabs, captured 2026-11-03: https://crypto.hcportal.eu/dashboard/cryptograms/1038 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3174/conversions/cpc_1908-10-16_DE_-Altst_HU_Arad__pic-large.jpg (source/picture-large.jpg); original resolution in work/hires/.
- Address side: https://api.hcportal.eu/media/3175/conversions/cpc_1908-10-16_DE_-Altst_HU_Arad__adr-large.jpg (source/address-large.jpg); original resolution in work/hires/.
- Mezőkövesd digit key: ciphers/hcp-1174/work/decode.py and SOLUTION.md in this repository.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-03: no entry for this card.

Transcription, key work, decipherment and this report: Claude Opus 5.5 (Anthropic). No earlier AI work on this number.
