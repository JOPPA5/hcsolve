# HCP 1166: a Hungarian love letter in cipher from Árpád to Margitka Sziber

Human solver: Tomáš Pavuk

**Status: deciphered in full (391 cipher signs; 387 decode as written, 4 are taken by word sense); independent review 1 verdict REVISE, all findings addressed, one word form corrected.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1166 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1166), portal name cpc_1916-04-11_HU_Mezokovesd_HU_Szomolya_szomolya-27, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article; it was not checked for this card, so whether it discusses the card is unknown.

It is a picture postcard of a couple among roses, with no writing on the picture side. The address side is open: **Őnagysága. / Rózsa reményű. / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács.** The place and date stand in clear along the vertical rule, **Mezőkövesd 1916 IV/11**. The stamp's postmark is partial (…VESD) and its date is not readable, so the date rests on the card's own text and the portal's file name.

The card belongs to the Mezőkövesd family: cards to Margitka Sziber at Szomolya from 1915 and 1916, in Hungarian, some signed Árpád. Several are deciphered in this repository (HCP 1174, 1178, 1179). On this card the whole left half of the message side is cipher in blue ink: a short letter, three four-line stanzas, and a closing. The stanzas mix open words and letters with cipher signs. The printed lines at lower left (Vero Art, No 3745, No 3845, Import, Germany) are the card's imprint.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The key was **transferred** from the finished sister cards HCP 1174, 1178 and 1179 and then extended; it is not a new key recovery. The transcription was made by hand from enlarged crops of the un-converted high-resolution scan. Each sign is a digit with an optional mark, and the mark is part of the sign. Unlike HCP 1174, this card divides words by spaces, which helps a good deal. The sister key gave the salutation "Édes Margitkám" and most of the text at once.

Three signs did not occur on the sister cards and were fixed from whole words on this card: `6` = j (párja, rája, hagyj, Adjatok), `4.` = gy (nagyon, egy, légy, hagyj, egymás and others) and `8.` = ty (kártyát, one token).

A script (work/decode.py) checks the hashes of the scans, decodes every sign of work/transcription.txt by the key, and stops if any line differs from the stated literal reading. The reviewer wrote a separate decoder with the key typed afresh and read all 22 lines against its own contrast-stretched crops.

## Key

Monoalphabetic substitution; each Hungarian letter or digraph has one sign. Long and short o, u, i are not told apart, and ő, ű share the signs of ö, ü. 28 distinct signs occur.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o, ó | `2,` | cs | `6` | j (new) |
| `0,` | ö, ő | `2.` | é | `6,` | n |
| `1` | i, í | `3` | d | `7` | k |
| `1.` | a | `3,` | r | `7,` | s |
| `1:` | e | `3.` | v | `7.` | sz |
| `1'` (high dot) | á | `4,` | g | `8` | m |
| `1,` | b | `4.` | gy (new) | `8,` | t |
| `:1` (dots at left) | ü, ű, ú | `5` | h | `8.` | ty (new) |
| `9` | p | `5,` | l | `9,` | z |

One further sign, `5.`, occurs once (see Uncertainties). The 5 always carries a short stroke above it, so it is easy to tell from other digits.

## Plaintext

Literal decode, row by row. Open text keeps its capitals; the letters are as the signs give them.

```text
L01 édes margitkám
L02 szerencsésen hazaérkeztünk nagyon szép
L03 és meleg idö volt egy negyed ketöre ér-
L04 tünk haza a kertekig
L05 danolaztünk de aztán álmos
L06 lettünk és csak ügy mentünk
L07 némán egymás ütán erröl
L08 most többet nem irok szervüsz
P09 Sehol nincs a világon
P10 Margitkának párja
P11 Adjatok egy kis kártyát
P12 Hadd irom izt rája
P13 Udvarloid seregében
P14 Minő helet adsz nekem
P15 Utolsonak ne hagyj engem
P16 Végy elsönek édesem
P17 M betüvel ir most a tollam
P18 S rád gondolok margitkám
P19 Üdvözletem küldöm neked
P20 S azt kivánom légy vidám
B21 üdvözlettel sok csokkal és öleléssel
B22 maradok hü kedvesed árpád
```

Reading in normal spelling:

```text
Mezőkövesd, 1916. IV/11.

Édes Margitkám!
Szerencsésen hazaérkeztünk, nagyon szép és meleg idő volt,
egy negyed kettőre értünk haza a kertekig, danolásztunk,
de aztán álmos lettünk és csak úgy mentünk némán egymás után)
erről most többet nem írok) Szervusz.

Sehol nincs a világon
Margitkának párja,
Adjatok egy kis kártyát,
Hadd írom ezt rája.

Udvarlóid seregében
Minő helyet adsz nekem?
Utolsónak ne hagyj engem,
Végy elsőnek, édesem.

M betűvel ír most a tollam,
S rád gondolok, Margitkám,
Üdvözletem küldöm neked,
S azt kívánom: légy vidám!

Üdvözlettel, sok csókkal és öleléssel
maradok hű kedvesed) Árpád)
```

## Translation

**English.** Sweet Margitka! We got home safely. The weather was very fine and warm. At a quarter past one we reached home as far as the gardens, we were singing, but then we grew sleepy and just walked silently one behind the other. I will not write more about this now. Servus.

Nowhere in the world / is there Margitka's equal; / give me a little card, / let me write this on it.

Among the host of your suitors / what place do you give me? / Do not leave me for last, / take me first, my sweet.

With the letter M my pen writes now, / and I think of you, Margitka, / I send you my greetings, / and I wish you this: be cheerful!

With greetings, many kisses and an embrace, I remain your faithful sweetheart, Árpád.

Address: To Her Ladyship, the rose-hopeful Miss Margitka Sziber, Szomolya, post office Bogács.

**Slovak.** Moja sladká Margitka! Šťastne sme došli domov. Bolo veľmi pekné a teplé počasie. Štvrť na dve sme došli domov po záhrady, spievali sme si, ale potom sme ospaleli a len sme išli mlčky jeden za druhým. O tom teraz viac nepíšem. Servus.

Nikde na svete / niet Margitkinej rovne; / dajte mi malú pohľadnicu, / nech na ňu napíšem toto.

V zástupe tvojich ctiteľov / aké miesto mi dáš? / Nenechávaj ma ako posledného, / vezmi ma ako prvého, moja sladká.

Písmenom M píše teraz moje pero, / a myslím na teba, Margitka, / posielam ti pozdrav / a želám ti: buď veselá!

S pozdravom, mnohými bozkami a objatím zostávam tvoj verný milý, Árpád.

Adresa: Jej Milosti, ružovo sľubnej slečne Margitke Sziberovej, Szomolya, pošta Bogács.

## Uncertainties

No uncertainty touches more than one letter of the ciphertext; the message itself is not in doubt.

- **Four signs rest on word sense against the shape as written.** Margi-t-kám in stanza 3 (an 8 with no comma, so m as written; the name has `8,` elsewhere). kü-l-döm (a 5 with no comma of its own, h as written; a tick stands above and to the right). üdvözlette-l in the closing (a 5 with no comma, h as written). mara-d-ok in the closing (abraded; what survives looks more like 8 than 3, and maramok is not a word). Dropped commas on 5 and 8 are a habit of this writer.
- **be-t-űvel.** The long stroke under the 8 is taken as its comma, and only one dot of `:1` is visible. Without the comma the word would be bemüvel, which means nothing.
- **Rubbed signs.** In gondolok the 0 is thin and the `6,` is a smudge with only its top and comma; the 3 has its middle in the rubbed patch. In the bottom rows some signs of üdvözlettel are faint and crossed by the printed "Import". Each has visible ink.
- **Spelling as written, normalised above.** ketöre for kettőre, danolaztünk for danolásztunk, helet for helyet, csokkal for csókkal, szervüsz for szervusz.
- **izt.** The sign is a plain 1 with a long flag and no dots, so the text says izt. It is taken as a dialect or loose form of ezt, "this". This is an emendation; ízt, "taste", does not fit.
- **`5.` in helet.** The mark is a clear dot, and this is the only `5.` on the card. It could be a deliberate ly, in the pattern of g/gy and t/ty, giving helyet exactly, or plain l, as on HCP 1179. One token cannot settle it. The word is helyet either way.
- **M betűvel.** Literally "with the letter M", taken as a play on Margitka's initial. Only the capital M is written.
- **Rózsa reményű** in the address is an open adaptation of the usual Szépreményű, and the translation is loose. **egy negyed kettőre** is taken as a quarter past one.
- **Punctuation.** The `)` after után, írok, kedvesed and Árpád has no opening bracket and works as a pause. The sign after nekem looks like `2.` and is taken as a question mark by its position.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the decoder, wrote its own, checked the key against the sister cards and read every row against the scan. Verdict: **REVISE**. The key and the message stood. Seven findings, all accepted after re-reading the enlargements:

- **Major, Adjatok.** The first draft read Adnátok, assuming a comma on the 6. There is none; the strokes below it are the ascenders of the d's of Hadd in the next row. As written, `6` = j gives Adjatok, a better word that needs no excuse.
- **Major, üdvözlette-l.** An undisclosed sign taken by sense: the transcription gave `5,`, but that 5 has no comma. The nearest stroke is the comma of the next sign. Now disclosed.
- **Minor, gon-d-olok.** The first draft read `3.` taken as d. The blob is at lower left, where the foot of a 3 ends, not where a dot stands. Now a plain 3.
- **Minor, mara-d-ok.** Now marked as resting on word sense.
- **Minor, `5.`.** Both explanations are now stated in place of a settled merge with l.
- **Minor.** The script and the solution now agree on csókkal, and a Slovak grammar error was corrected.

The count of signs taken by sense is four, not three. The review could not verify the postmark date or the HistoCrypt article, and left `5.` open.

![Adjatok: no comma on the 6 (P11, enlarged by the reviewer)](../review/work/d_adnatok.png)

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1166/work/decode.py
```

This checks the scan hashes, decodes the 391 signs of work/transcription.txt and prints the literal lines and the reading. The normalised reading is written into the script; only the literal decode is computed.
