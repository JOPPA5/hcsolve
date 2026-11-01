# HCP 1178 (cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43): a kiss in numbers on a Hungarian postcard

Human solver: Tomáš Pavuk

**Status: the enciphered line is deciphered in full (13 of 13 signs); independent review 1 verdict REVISE, findings addressed.** The surrounding open text has two small unread places. Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1178 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1178), portal name cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-01 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Szegedi Janosné, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), which was not consulted.

The card belongs to a series sent from Mezőkövesd to Szomolya in north-east Hungary during the First World War; the portal's name for the group gives 1915, and sister cards are dated 1915 and 1916. This card itself carries no date, and its postmark is illegible apart from fragments. It is addressed to *Tek. Szegedy Jánosné úrasszonynak, Szomolya, u. p. Bogács*, but it speaks to "Margitka". A sister card, hcp-1174, is addressed to Margitka Sziber at the same place and is signed Árpád. The writer seems to have been courting her under cover of cards to, or through, a relative.

Almost everything on the message side is open Hungarian in violet copying pencil: a greeting and a four-line verse. A later hand in brown ink struck the text through and tried out dates (1848, 1918, 1920). These additions are not part of the message. The only enciphered text is one boxed line of 13 signs near the foot. Right after it the writer dares the reader: "if you can, read the number-letters as well". The picture side has no writing.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The line was transcribed by hand from the highest-resolution original available, enlarged 4 times. No OCR was used. Each sign is a digit followed by an optional mark (dot, comma or colon), and the mark belongs to the sign.

![First part of the boxed line (work/crops/dig1.png)](../work/crops/dig1.png)

![Second part of the boxed line (work/crops/dig2.png)](../work/crops/dig2.png)

Transcription:

```text
2, 0 7 0 5, 5. 1. 7 8, 2. 4, 1: 3
```

Thirteen signs are far too few to break a cipher alone, so the key was reconstructed from the digit passages of sister cards in the same hand (hcp-1174, 1175, 1179). On hcp-1174 a 13-sign salutation fits *Édes Margitkám*, and open words there gave starting values. Those values make the end of this card read *téged* ("you"). This card therefore played a small part in forming the key and is not a fully independent test. The independent evidence is that the same key gives connected Hungarian on the sisters: *ölelhetlek én*, *csókollak* and *a legszeb(b)*.

The reader can reproduce the decoding from the repository root with `python3 -I ciphers/hcp-1178/work/decode.py`.

## Key

Monoalphabetic substitution (MASC). Eleven distinct signs occur on this card, standing for ten letters:

| sign | letter | sign | letter |
|---|---|---|---|
| 0 | o/ó | 3 | d |
| 1. | a | 4, | g |
| 1: | e | 5, and 5. | l |
| 2, | cs | 7 | k |
| 2. | é | 8, | t |

Hungarian digraphs such as cs have a single sign, and vowel length is not marked. The two forms of l are variants. The fuller family key is given on the sister cards.

## Plaintext

Enciphered line, signs decoded to `csokollaktéged`:

**csókollak téged**

English: "I kiss you".

Slovak: „bozkávam ťa“.

Open text around it, read through the brown strokes (square brackets show gaps or uncertain letters, and the boxed cipher line appears as digits):

```text
[top margin] Vasárnap k[i]m[e]g[y]ek(?) egy [...] vonatnál.
Kedves Margitkám!
Üdvözöllek, Angyukádal
és a kis Mariskával
együtt üdvözlésedre
ezt a pársoros ver-
secskét írom!
Tavasszal is hull a
levél,  Hol a f[...] fujja(?) a szél,
A szivet is bánat tépi,
Hogyha zord csalódás
éri. (2,0705,5.1.78,2.4,1:3
ha tudod olvasd(?) el a szám betűt is)   Sz. A.(?) Mezőkövesd
```

English: "Dear Margitka of mine! I greet you, together with your ángyuka (aunt or sister-in-law by marriage; or: your mummy) and little Mariska, and to greet you I write this little verse of a few lines! Leaves fall in spring too, where the wind blows [one word unread]; the heart too is torn by sorrow when harsh disappointment strikes it. (I kiss you; if you can, read the number-letters as well) Sz. A.(?), Mezőkövesd." Margin: "On Sunday I (perhaps) go out ... a ... at the train."

Slovak: „Drahá moja Margitka! Pozdravujem ťa spolu s tvojou ángyukou (teta či švagriná, príbuzná cez manželstvo; alebo: mamičkou) a malou Mariškou a na pozdrav ti píšem tento veršík na pár riadkov! Aj na jar padá lístie, kde fúka vietor [jedno slovo neprečítané]; aj srdce trhá žiaľ, keď ho postihne kruté sklamanie. (bozkávam ťa; ak vieš, prečítaj aj číselné písmená) Sz. A.(?), Mezőkövesd.“ Okraj: „V nedeľu (azda) vyjdem ... jeden ... pri vlaku.“

## What remains uncertain

In the cipher line, no sign is in doubt. Two values rest on limited evidence:

- `5.` = l could not be decided on this card alone. It rests on the secure *a legszeb(b)* on hcp-1179 and on the expected formula *csókollak*.
- `2,` = cs occurs only in this word on the cards used here, and depends on word sense.

More generally, 13 signs prove nothing by themselves. The case rests on the family key, and hcp-1174 and hcp-1179 are reviewed but not yet closed.

In the open text, none of which affects the decipherment:

- **Verse line 6:** the word after *Hol a* begins with f and is unread. *Fujja* is a fair reading under heavy strokes.
- **Top margin:** the word between *egy* and *vonatnál* is unread, and *kimegyek* is only a suggestion.
- **Angyukádal:** the scan does not separate g+y from y alone. I prefer the kin term because the sister card hcp-1175 greets the same addressee as *Ángyika* (from that directory's unreviewed notes). *Anyukádal*, "with your mummy", stays possible.
- **Signature:** *Sz. A.* or *Sz. K.* The hcp-1174 signature Árpád favours A.
- **Other points:** *olvasd* could be *olvasod*, and the start of *ha tudod* is faint. The card's date is unknown.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) read the 13 signs itself, decoded with values taken only from hcp-1174, and checked sister passages and open text on the scans. It agreed with all 13 signs, the cipher type and the other values, and gave the verdict REVISE with these points:

1. **`5.` is l, not j.** The solver's first reading was *csókoljak téged* ("let me kiss you"). The reviewer showed `5.` in *a legszeb(b)* on hcp-1179, and the plaintext was corrected to *csókollak téged*.
2. **A false control.** The solver claimed hcp-1174 had `5.` in the same word; a faint comma shows it has `5,`. The control and the claim were corrected.
3. **Verse line 6.** *Fuvalmas* was withdrawn, *fujja* adopted, and the word before it left unread.
4. **Smaller open-text and disclosure points.** *Versecskét* was corrected, and the alternatives for *Angyukádal* and the signature are now disclosed.
5. **Overstated support.** The solver's claim of unforced agreement was removed, and the unreviewed hcp-1175 passages were dropped from the controls.

No sign of the transcription changed, and the change of one letter is the only change to the deciphered text.
