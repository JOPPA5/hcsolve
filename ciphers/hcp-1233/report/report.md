# HCP 1233: Feri tells Jolánka Tóth that he passed his first exam

Human solver: Tomáš Pavuk

**Status: complete reading with disclosed sense calls; one word (hál') is restored from sense, because its l is not written. Reviewed twice (both REVISE, all findings addressed).** Report dated 2026-11-02. Solver and decipherment: Claude Opus 5.5. Independent reviewer: a separate Claude Opus 5.5 agent.

## Origin and context

The cryptogram is record 1233 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1233), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-67, from Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. There was no earlier work on this number, and no published solution was seen.

The card has a printed picture side, titled "Kis házikóm ablakánál" with a printed verse and no handwriting. The address side is in plain handwriting: Tóth Jolánka úrleány[nak], Jász-Árokszállás, Hungary. An upper-left note is tentatively read "Szigorúan magán" ("strictly private"); its first word is not certain. The postmark is only partly legible (letters PAL and SO, compatible with the Rákospalota cancellation of HCP 1216, not established), and no date can be read. Nothing on the card gives a year.

The rest of the address side is covered with cipher writing in purple pencil. It fills the left half, runs along the bottom edge, turns up the right edge, runs upside down along the top edge, and ends inside the stamp box, on top of the printed triangle. The postage stamp has since been lifted (only a green corner with the cancellation remains), so the closing in the box was written under the stamp: a hidden message, in the cipher signs. It reads "Csókolja számtalanszor Feri" (Feri kisses you countless times; rows 22 to 26). This was confirmed in a stamp-box audit on 2026-11-03.

The card belongs to the family of postcards to Jolánka Tóth, of which several are already deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). The language is Hungarian.

![Address side with the cipher text: 19 rows at left and bottom, then the right edge, the top edge and the stamp box (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: printed title and verse only (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The key was **transferred, not recovered**: it is the shared key of the finished Jolánka cards, above all HCP 1216. The work on this card was a new, manual, sign-by-sign transcription from enlarged crops of the un-converted portal scan, together with a purple-ink mask, (R+B)/2−G, that removes most of the blue print and the black portal stamp. No OCR was used.

The opening gave "szeretet edes jolan|kam tudatom hogy" at once, and the rest followed row by row. The harder part was the writing order. The top band looked unreadable until it was seen to be upside down, read right to left with the card turned 180 degrees. The order was found from the signs themselves: words join across the turns of the text (lefek|sz-, nem | aludtam, Isten vele).

Each sign is recorded in work/ledger.txt, 349 tokens in 26 rows. The command below checks the hashes of all four images, applies the key and prints the rows and the normalized text. It proves the key application, not the reading of the pixels; that was checked separately by the reviewer, who read the card sign by sign with its own crops and its own decoding script.

```sh
python3 -I ciphers/hcp-1233/work/decode.py
```

## Key

Cipher type (register): **MASC + Steganography** (changed from MASC on 2026-11-03, because the closing is hidden under the stamp). Simple monoalphabetic substitution with invented graphic signs. The names are conventional descriptions of handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls ( ) | cs | three short strokes | m | gamma corner | t |
| long stroke + tick on the left | d | two strokes | n | plain cross x | u |
| three bars | e | tilted or upright cross | f | chevron | v |
| open loop with descender | g | long stroke + tick on the right | h / p | low descender | y |
| dotted crossed curve | i | inverted T (also T-like, leaning) | j | crossed curve with hook | z |
| cursive loop | o | | | | |

Notes on this hand: the three bars are sometimes crossed by a stroke (rows 2, 5), read as e/é. The T-like first sign of tudatom (row 2) is taken as a t variant from sense. Dots or ticks over o and u give ö, ő, ü; other acutes are faint and are supplied in the normalized text. h and p share one sign and are told apart by the word.

## Plaintext

Literal decipherment by written row. [x] is a value from word sense or a damaged trace, not from a clean shape; ? is a visible mark with no value. Rows 18 and 19 run along the bottom edge, row 20 up the right edge, row 21 along the top edge, rows 22 to 26 in the stamp box.

```text
01 szeretetedesjolan
02 kamtudatomhogyel
03 sővizsgammasi
04 kerrelvegzödöt
05 hedigojelőkeszü
06 letlenültalalt
07 mertnemszami
08 tottamracsakszom
09 batontudtammeg
10 hogymahetfon
11 vizsgaleszes
12 nagyinutanna
13 keletneznem
14 hogytudjakva
15 lamiejszahig
16 benavonatonis
17 tanultamhogy
18 akezemrafagyottakönyvrede[h]a[i]st[e]n
19 neknemtanultamhiabamostmarlefek
20 sz?[o]mertketnahotanem
21 aludtamistenvela
22 csokol
23 jasza
24 mta
25 lansz
26 orfe[r][i]
```

Normalized Hungarian. Punctuation, word division and accents are editorial; [x] here marks a letter that is not written, or is a sense call inside a restored word:

**Szeretett édes Jolánkám! Tudatom, hogy első vizsgám ma sikerrel végződött, pedig oly előkészületlenül talált, mert nem számítottam rá, csak szombaton tudtam meg, hogy ma, hétfőn vizsga lesz, és nagyon utána kellett néznem, hogy tudjak valami[t]. Éjszakáig benn a vonaton is tanultam, hogy a kezem ráfagyott a könyvre, de [h]á[l]' Istennek nem tanultam hiába. Most már lefeksz[o/e]m, mert két nap óta nem aludtam. Isten vele. Csókolja számtalanszor Feri.**

English translation: **My beloved sweet Jolánka! I inform you that my first exam ended successfully today, although it found me so unprepared, because I was not counting on it; only on Saturday did I learn that the exam would be today, Monday, and I really had to look into it so as to know something. Until nightfall I studied, on the train too, so that my hand froze to the book, but thank God I did not study in vain. Now I am going to bed, because I have not slept for two days. God be with you. Feri kisses you countless times.**

Slovak translation: **Moja milovaná, sladká Jolánka! Oznamujem Vám, že moja prvá skúška sa dnes skončila úspešne, hoci ma zastihla takého nepripraveného, lebo som s tým nepočítal; až v sobotu som sa dozvedel, že dnes, v pondelok, bude skúška, a musel som sa na to poriadne pozrieť, aby som niečo vedel. Až do noci som sa učil, aj vo vlaku, takže mi ruka primrzla ku knihe, ale vďakabohu som sa neučil márne. Teraz už idem spať, lebo už dva dni som nespal. S Bohom. Bozkáva Vás nespočetnekrát Feri.**

Why the reading is believed: a key taken unchanged from other cards turns the whole address side, including the margins, into consecutive Hungarian with one continuous story. Repeated words decode identically (hogy four times, nem three times, vizsga and tanultam twice each), and the formal close (Isten vele, csókolja) matches the family.

## Uncertainties

**The weakest place: de hál' Istennek (rows 18 and 19).** This is one restored word in a clause that otherwise reads. What stands after könyvre is d e [?] a [i/o] s t [e] n | n e k.

- **No l is written.** Taken literally the card has de ha Istennek, or de ya Istennek, which is not idiomatic. hál' (hálistennek, the spoken contraction of hála Istennek) is a restoration from sense. No better word was found: de ha and de hát give Istennek no role, while Istennek, nem tanultam hiába and the passed exam all point to it.
- **The first sign** is close in shape to y. Only a short stroke to the right of the crossing favours h; the rest of the case is sense.
- **The [i]** is the sign shared by i and o, with an unusually long, straight upper arm and no clear dot.
- **The [e]** has three staggered bars, the top one standing apart near the card corner, so isten against istan rests on that bar and on sense.

![Tail of row 18: the h-or-y sign, a, the long-armed i, s, t and the staggered e, with the stamp letters behind them (work/resp/row18_tail.png)](../work/resp/row18_tail.png)

![The disputed sign (left) beside ö of könyv and i of row 21, same scale: arm, apex, descender, loop (review/work2/cmp_loop.png)](../review/work2/cmp_loop.png)

**Row 20, lefeksz-m.** After clear s, z there is a dash, then the address flourish, then a small closed loop on a stem, then the m of mert. No m stands here, so one m is shared with mert. Either the loop is o (colloquial lefekszom), or the dash is the bottom bar of an e hidden in the flourish (standard lefekszem), with the loop left over. Neither is firmer. The sense "I am going to bed" is the same.

**Other calls resting on word sense:**

- Row 2 első: the crossed three-bar sign is read e, and the word is split over rows 2 and 3.
- Row 12 nagyin: the sign after y is an open i with a dot, not the o loop. The card has i; the normalized text has nagyon.
- Row 15: h stands where k is expected in éjszakáig, read as a slip. The final t of valamit is not written. The division valami(t). Éjszakáig is editorial; valami éjszakáig would give the same words.
- Row 16 is: the i has no visible dot and could be taken as z, but vonaton is decides it.
- Row 20 nap: p is the h/p sign, and nap is from sense. A stray long stroke beside nem has no value, and neither does a small v-like mark at the card corner.
- Row 21 vela: two bars plus a smudge at the card edge, where a third bar may be cut off; normalized vele.
- Rows 23 to 25: the signs of row 24 lie across the blue triangle. The mask shows m, a stem of t, and bars; számtalanszor fits all visible traces, but not every sign is confirmed.
- Row 26 Feri: e has two clear bars plus a blot; f is close to plain u and rests on the name, as on HCP 1216; r and i run through stamp residue. No identity with the Feri of HCP 1216 is claimed.

**Writer's spellings normalized:** szeretet edes, végzödöt, ojelő-, utanna, kelet (kellett), ben a. The dropped double letters agree with each other and with the hand.

**Not established:** the year, the place of writing, and the identity of the sender.

## Review summary

Reviewer: Claude Opus 5.5, a separate agent, two rounds, both **REVISE**. Each round the reviewer ran the reproduction command, read the card from its own crops and decoded the text with its own script (350 tokens in round 2 before the fix below, no unknown token).

Round 1 confirmed the key, the writing order and nearly all of the text, but rejected the first reading of the row 18 clause (de ha [m]ost annak): it needed an unwritten m and a changed vowel, and its sense was unclear. The solver reread the crops at 7×, and this changed the reading:

- The clause became de hál' Istennek, using a third bar of e that had been missed. The bars at the card corner proved to belong to row 18, not row 20.
- The first sign of row 13 is k, not b, as both solver and reviewer had read it. This gives kelet(t) néznem, and the sentence gets its finite verb.
- The unjustified e and m in row 20 were removed.
- Sense calls in row 26 and row 21 were disclosed, and a Slovak form was corrected.

Round 2 confirmed all of that but found that the l counted in hál' is not a sign; it is the upper arm of the following i/o sign. As a result:

- l is now marked as supplied, and the claim that no letter was inserted is withdrawn.
- The evidence for h was reduced to the short right stroke and sense, with y named as the alternative shape.
- lefekszem and lefekszom are given as equal options.
- The corner mark is listed, and row 26 e is softened.

The words and the meaning of the letter did not change in round 2. The reviewer found no use of a published solution.

The reviewer could not verify: how the writer came to hál' (no sister card has the word), the signs under the address flourish, every sign of rows 24 and 25 across the triangle, and the postmark and the note, on which no claim depends.

## Sources

- HC Portal record 1233, all three tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1233 (source/metadata.md).
- Scans: https://api.hcportal.eu/media/3759/ (picture side) and https://api.hcportal.eu/media/3760/ (address side), conversions in source/, un-converted originals in work/hires/.
- Family key: finished Jolánka cards in this repository, above all ciphers/hcp-1216.
- Portal attachment reference: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked by the orchestrator on 2026-11-02: no record of this card.
