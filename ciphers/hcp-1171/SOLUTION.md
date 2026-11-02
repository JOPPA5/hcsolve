# hcp-1171 solution (round 1)

Solver: Claude Opus 5.5, 2026-11-02. No earlier work on this number. The portal shows Not solved and attaches no solution or transcription. No published solution of this card was found in the repo. The HistoCrypt article the portal links was not checked for this card, so I cannot say whether it discusses it.

## Cipher type and key

Hungarian open text with only two items enciphered: the salutation and the signature. Register label: MASC. Each letter is one sign, a digit alone or a digit plus a mark. The key is transferred from FINAL card hcp-1174 (same correspondence: Mezőkövesd to Sziber Margitka, Szomolya); it was not rebuilt here. Signs attested on this card:

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `1` | i | | `3` | d | | `7` | k |
| `1.` | a | | `3,` | r | | `7,` | s |
| `1:` | e | | `3.` | v | | `8` | m |
| `1'` (high dot) | á | | `4,` | g | | `8,` | t |
| `9` | p | | | | | | |

Ciphertext (20 signs, all decoded by the table):

- Top line: `7 1: 3 3. 1: 7,  8 1. 3, 4, 1 8, 7 1' 8 !` = Kedves Margitkám!
- Foot, in brackets: `( 1' 3, 9 1' 3 )` = Árpád

## Plaintext (Hungarian; [ ] = enciphered on the card)

[Kedves Margitkám]!

Szerencsésen megérkeztünk, nagyon szép és világos üdő volt és jól megvolt fagyva, hazafelé mindenüt örömtől eltelve daloltunk és fütyörésztünk, csak mégis mind a kettőnket hogy ilyen alkalmatlanságot csináltunk nektek, mert olyan későre maradtunk és nem hagytunk aludni, no de bocsás meg, mert nagyon nehéz volt ott hagyni téged. Más ujságot nem irhatok majd levélbe többet.

Szerencsésen megérkeztem,
Nincsen semmi bajom,
Csak te nélküled, édesem,
Unatkozom nagyon.

Mindnyájatokat számtalanszor csókollak a legtisztáb szivvel. ([Árpád]) (A)

Commas in the prose are added by me where the card has none. Normal spellings: üdő = idő, mindenüt = mindenütt, bocsás = bocsáss, legtisztáb = legtisztább, szivvel = szívvel, ujságot = újságot, irhatok = írhatok.

Address: Tek. / Szépreménnyu / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács. The word is given as written, four minims after é and no accent on the last letter; the normal form is szépreményű ("promising"), and hcp-1140 and hcp-1152 record the doubled spelling Szépreménnyü. Postmark: only M of the town is legible on this strike, so Mezőkövesd is inferred from the series; 915 NOV 2?, with the day's second digit not clear; the portal file name gives 1915-11-22.

## English translation

Dear Margitka! We arrived safely. The weather was very fine and clear and it was well frozen; on the way home, filled with joy everywhere, we sang and whistled. Only still, the two of us [regret: verb unwritten] that we caused you such inconvenience, because we stayed so late and did not let you sleep. Well, forgive me, because it was very hard to leave you. I cannot write any more news, later in a letter.

I have arrived safely, / nothing is wrong with me, / only without you, my sweet, / I am very bored.

I kiss you all countless times with the purest heart. (Árpád) (A)

## Slovak translation

Milá Margitka! Šťastne sme dorazili. Počasie bolo veľmi pekné a jasné a dobre primrzlo; cestou domov, všade naplnení radosťou, sme spievali a pohvizdovali. Len predsa nás oboch [mrzí: sloveso nie je napísané], že sme vám spôsobili takú nepríjemnosť, lebo sme zostali tak dlho a nenechali sme vás spať. No odpusť mi, lebo bolo veľmi ťažké ťa opustiť. Ďalšie novinky nemôžem napísať, viac potom v liste.

Šťastne som dorazil, / nič mi nechýba, / len bez teba, moja sladká, / sa veľmi nudím.

Všetkých vás nespočetnekrát bozkávam s najčistejším srdcom. (Árpád) (A)

## Command

Run from the repo root:

    python3 -I ciphers/hcp-1171/work/decode.py

It checks the SHA-256 of all four scans, decodes the 20 signs with the key, asserts each word, and prints the card. The open text is hard-coded, so the command reproduces only the decoding of the cipher signs.

## Uncertainties

The cipher has none of substance. All 20 signs are clean on 3x and 4x crops. The dots of `1'` stand high in the digit in both the top line and the signature.

All other points concern the open text. It is struck through in brown and was read mainly in the red channel (`work/crop.py`, `work/crop2.py`).

1. `csókollak` is the least sure word. It lies across the printed publisher line ("Printed in Saxony", with a circled copyright mark and a date) and the strike-out. On `work/crops/w_col.png` and `w_blue.png` the end -k-o-l-l-a-k is clear; the opening c-s-ó rests on a thin stroke under the print. The sentence and the sister card hcp-1174 (`csókollak`) support it. The accent on ó is not seen.
2. `legtisztáb-` is followed by a dash under the line end, then `szivvel` on the next line. The word has one b. I read the second b as a spelling slip. The final letters run into the strike-out and the green margin rule.
3. `csak mégis mind a kettőnket / hogy ilyen ...` has no main verb on the card (a verb like bántja, "troubles", is understood). All the words are read; the gap is the writer's. The translations mark the implied verb. The a of `mind a` is blotted and heavier than the clean a of `a legtisztáb`, a descender from the row above runs into it, a brown stroke crosses it, and it may be overwritten. `mind a kettőnket` is the only idiomatic reading, so this letter rests on word sense.
4. `Más` has an open initial that could look like another capital; the word fits the next words exactly.
5. `levélbe többet` follows `majd` at a line end. My translation "later in a letter" is free; literally "more ... then in a letter".
6. `(A)` after the signature is open and its meaning is not explained. It is likely his initial: hcp-1179 is signed Sz. A. (that card's own solution says the pixels there also allow Sz. K., and hcp-1175 reads Sz. A.). The thin stroke before it is the opening bracket, the same thin straight stroke as the bracket before the enciphered name. It may be Á; no accent is seen.
7. `csókollak` with a plural object (`Mindnyájatokat`) is normal Hungarian, -lak covers "you all".

## Why I believe it is correct

- A key taken unchanged from another card gives two exact words and a name for 20 of 20 signs, no adjustments. This is a fixed test: the key was not fitted here.
- The name agrees with the enciphered signature `Árpád` on hcp-1174, and the salutation is the same type as on hcp-1179 ("Kedves Margitkám!", in clear).
- The open text fits: a thank-you and apology after a late visit, with a four-line rhyme (megérkeztem / édesem, bajom / nagyon).
- Enciphering just the name and the tender address matches the sister cards.

## Response to review 1

Verdict ACCEPT, seven minor findings. All are addressed; the cipher reading and the open text did not change, apart from the address spelling in finding 1. I rechecked the reviewer's crops in review/work/ myself.

1. Address word: fixed. `x_nny.png` shows four minims after é, then y, then u with no accent. SOLUTION.md and work/decode.py now give `Szépreménnyu`, with the normal form stated. The earlier form was a normalised miscopy.
2. Bracket collision: fixed. The plaintext now has `legtisztáb`; the normal spelling stays in the list below it, and [ ] now means enciphered only.
3. Empty translation notes: fixed. Both removed; no word is implied there.
4. The a of `mind a`: fixed. Uncertainty 3 now describes the sign as on `x_a2.png` and says it rests on word sense.
5. `(A)`: fixed. Uncertainty 6 now says the stroke is the opening bracket. On `sig.png` it matches the thin straight bracket before the enciphered name. The hcp-1179 signature is cited, with that card's own caveat.
6. Postmark town: fixed. Stated as inferred from the series, only M legible.
7. Dot height: fixed. On `top.png` and `sig.png` the dots stand at about the same height, so the claim and the Arpad alternative are withdrawn.

`python3 -I ciphers/hcp-1171/work/decode.py` was re-run after the changes: hashes OK, 20 signs decoded.
