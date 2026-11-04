# HCP 1234 (cpc_1913-12-16_HU__HU_Jasz Arokszalas_jolanka-45): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (449 signs: 20 main rows and 6 rows under the stamp); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1234 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1234), portal name cpc_1913-12-16_HU__HU_Jasz Arokszalas_jolanka-45, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a tinted photograph, scanned sideways, of a young man writing at a table while a dove carries off a sealed letter. A printed verse in plain Hungarian stands beside him:

"Van nekem egy tikom [sic] / Rejtegetem titkon / Csak az fejthetné meg, / Kinek e levél megy!"

("I have a secret, I hide it in secret; only the one this letter goes to could solve it.") The print has "tikom", an apparent misprint of "titkom".

The whole message is on the address side, written in brown ink in invented signs: 20 rows filling the left half and running along the bottom edge, and six short rows in the box under the place of the stamp. The address is plain handwriting: **Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás** ("To the promising young lady Jolánka Tóth, Jászárokszállás").

There are two postmarks. One is from Jászárokszállás with DEC 16 legible. The year is not read: 1913 comes only from the portal's file name. The digit just before DEC looks like a 1, which would suit a year ending in 1, but the other digits are illegible, so this is a doubt and not a correction. The second postmark begins GY... (perhaps GYÖ...) and is cut off, so its place is not identified.

![Picture side, scanned sideways, with the printed verse at the left (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: the cipher text, the box under the stamp place, the two postmarks and the plain address (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth in Jászárokszállás, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery. The opening of the message refers to the cipher itself: the writer says he is practising "the writing" so as not to forget it.

## Method

Everything on this number was done on 2026-11-02 by Claude Opus 5.5; there was no earlier work on it. The key comes unchanged from the finished family cards, above all HCP 1216, which were solved by the OpenAI GPT solver and completed by Claude Opus 5.5. No published solution of this card was found or used.

- **Transcription.** The solver read every row on 2× to 5× enlargements of the high-resolution address scan and recorded one token per written sign in a ledger (work/ledger.txt). The ledger is manual, not OCR, and it is not blind, because the family key was known.
- **Decoding.** A short script (work/decode.py) checks the hashes of the source scans, decodes the ledger and prints the literal rows and the normalized text. It reports 449 signs and no unknown sign.
- **Sign checks.** Doubtful signs were settled on enlargements, for example the gamma in row 4 (tudatom, not tudarom) and the two bars in row 13 (inkáb, not inkéb).
- **Review.** A separate Claude Opus 5.5 agent re-ran the command, re-read all 26 rows on its own 3× to 6× crops, and decoded them with its own script using the sign classes of HCP 1216. All rows agreed. Its reading was also not blind, since it had seen the solver's text first.

The writer spells by ear and writes only some of the accents. The literal decipherment keeps what he wrote; the normalized Hungarian is editorial.

## Key

Cipher type: **MASC + Steganography** (updated 2026-11-03): a simple monoalphabetic substitution with invented graphic signs, with part of the message (six rows) hidden in the stamp box under the stamp, which has since been lifted. The names below are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| long stroke, short tick on the left | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke, tick on the right | h / p | low descender | y |
| hook with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

The digraphs sz, gy and ny are written as two signs (s + z, g + y, n + y). Dots over o and u give ö and ü. Acute ticks appear on some vowels only. One sign serves both h and p. On this card the plain x and the z cross are not reliably separable by shape, so u or z is chosen by the word. Three of the 449 tokens are ordinary Latin letters, not cipher signs: a cursive A (row 12), a cursive N (row 16) and a cursive l (row 8).

## Plaintext

Literal decipherment by written row (spaces are editorial; h stands for the h/p sign):

```text
01 szeretet édes jolankam
02 gyakorlatot tartok
03 az írasban hogy el ne
04 felejtsem tudatom hogy
05 nem sikerült hazamen
06 ni délelőt írok egy
07 harat a gondolataimbol
08 boldog csak ugy Lehetek én
09 hogy ha te leszel az enyem
10 nem szeretek mast csak téged
11 csokal teszek ra hecsétet
12 A csókadas nem szégyen
13 hanem inkáb erény
14 ha csokot adsz babám
15 sohasem légy szerény
16 Nem kérek én lehetetlent
17 csuhan azt hogy szeres
18 hedig ez okvetlenül kell
19 hogy te boldog lehess
20 isten vele a viszontlátásra imádoja feri
S1 hit remeny
S2 és szeretet
S3 kösse össze
S4 szivonket
S5 imadoja
S6 feri
```

Normalized Hungarian (brackets mark letters not on the card):

Szeretet[t] édes Jolánkám! Gyakorlatot tartok az írásban, hogy el ne felejtsem. Tudatom, hogy nem sikerült hazamenni délelőt[t]. Írok egy párat a gondolataimból.

Boldog csak úgy lehetek én, hogy ha te leszel az enyém, nem szeretek mást, csak téged. Csók[k]al teszek rá pecsétet.

A csókadás nem szégyen, hanem inkáb[b] erény. Ha csókot adsz, babám, sohasem légy szerény.

Nem kérek én lehetetlent, csupán azt, hogy szeres[s], pedig ez okvetlenül kell, hogy te boldog lehess.

Isten vele, a viszontlátásra. Imádója Feri.

Under the stamp: Hit, remény és szeretet kösse össze szívünket. Imádója Feri.

## Translation

**English**

My beloved sweet Jolánka! I am practising the writing so that I do not forget it. I let you know that I did not manage to get home in the morning. I am writing down a few of my thoughts.

I can only be happy if you become mine; I love no one else, only you. I set a seal on it with a kiss.

Giving a kiss is no shame, rather a virtue. When you give a kiss, my baby, never be modest.

I ask nothing impossible, only that you love me, yet this is absolutely needed so that you may be happy.

God be with you, until we meet again. Your adorer, Feri.

Under the stamp: May faith, hope and love bind our hearts together. Your adorer, Feri.

**Slovak**

Moja milovaná sladká Jolánka! Cvičím sa v tomto písme, aby som ho nezabudol. Oznamujem, že sa mi nepodarilo dostať sa domov predpoludním. Píšem niekoľko svojich myšlienok.

Šťastný môžem byť len vtedy, ak budeš moja; nemilujem nikoho iného, len teba. Bozkom na to dávam pečať.

Dať bozk nie je hanba, ale skôr cnosť. Keď dávaš bozk, zlatko, nikdy nebuď skromná.

Nežiadam nič nemožné, len aby si ma milovala, a to je nevyhnutne potrebné, aby si bola šťastná.

S Bohom, dovidenia. Tvoj ctiteľ Feri.

Pod známkou: Nech viera, nádej a láska spoja naše srdcia. Tvoj ctiteľ Feri.

## Why the reading is sound

- The family key, transferred unchanged, turns all 449 signs into Hungarian with no unknown sign value and no unread clause.
- The middle of the card scans as rhymed verse, which the decipherer did not impose: erény / szerény and szeress / lehess. The box under the stamp gives the familiar triad of faith, hope and love (1 Corinthians 13).
- Repeated words decode identically: hogy five times, boldog, szeretet and imádója Feri twice each.
- The context fits: the addressee, the printed verse about a secret only the recipient can solve, the remark about practising the writing, and a closing formula and signature that match the family.

## What remains uncertain

None of these changes the sense.

- **Overwritten signs read partly from sense.** The s of sikerült (row 5); the ő of délelőt (row 6), a loop with a double mark under a blot; the s of szégyen (row 12), a heavy sign beside a separate cross; the h of lehetek (row 8), under a blot; the last s of lehess (row 19), a bowl overwritten in purple. Two signs in row 14 (o of csokot, d of adsz) are merely heavy and are legible.
- **h or p.** The one sign is read p in párat, pecsétet, csupán and pedig, and h elsewhere. These calls rest on word sense.
- **u or z.** The 20 cross signs divide into 17 z and 3 u (tudatom, úgy, csupán). Every one gives the only available word, but the split rests on sense, not on shape.
- **Stamp row 3.** The second bowl of össze looks close to the chevron v, and the z and e after it nearly touch. The phrase kösse össze settles it.
- **Stamp row 4.** The word is written with a plain o, szivonket, where standard Hungarian has ü. It is normalized to szívünket; the writer may have left out the marks, or the form may be dialectal. The k has a closed, 8-like shape.
- **Latin letters.** The cursive A and N stand where a new sentence of the verse begins. The l of lehetek (row 8) is a cursive loop, perhaps also a plain letter.
- **Spellings normalized:** szeretet to szeretett, délelőt to délelőtt, csokal to csókkal, inkáb to inkább, szeres to szeress. Csókadás is taken as one word. Most accents are supplied.
- **Layout.** Word division, punctuation and verse lines are editorial. A long dash between te and boldog in row 19 has no letter value. A few commas and full stops on the card are not transcribed, and faint ticks are recorded only approximately.
- **Style.** "Isten vele" is formal, while the verse says "te"; that is what the card says.
- **Date.** The year on the postmark is not read, as stated above.
- **Sender and source.** Feri is named on the card, and HCP 1216 is also signed Feri, but identity with the sender of the other family cards is not proved. Whether the verse comes from a known source was not traced.
- **Independence.** Neither the transcription nor the review was blind.

## Review summary

Review 1 (a separate Claude Opus 5.5 agent, 2026-11-02) tried to refute the reading and could not. Its verdict was **ACCEPT**, with five minor disclosure findings. All were accepted, and no letter of the plaintext changed.

1. The printed verse was silently corrected. It is now given as "tikom" [sic], with the normalization stated.
2. The long dash in row 19 was not mentioned. It is now recorded as having no letter value.
3. The doubtful second bowl of össze was not listed. It now is.
4. Two ledger flags in row 14 had no matching note. They now have one.
5. The report gives 1913 as the portal's date only and states the doubt about the year.

The reviewer could not verify the postmark year, the place of the second postmark, the source of the verse, or the identity of this Feri with the Feri of other family cards.
