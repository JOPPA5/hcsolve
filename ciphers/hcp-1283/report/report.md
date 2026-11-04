# HCP 1283 (cpc_1913-03-20_HU__HU_Jasz Arokszalas_jolanka-34): Feri to Jolánka Tóth, bored and short of money

Human solver: Tomáš Pavuk

**Status: deciphered; every sign transcribed (532 signs), two isolated words not understood, everything else reads. Independent review 1 verdict REVISE; all eight findings addressed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1283 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1283), portal name cpc_1913-03-20_HU__HU_Jasz Arokszalas_jolanka-34, part of Tobias Schrödel's cryptographic postcards collection (private collection; see https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When captured on 2026-11-01 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The date 1913-03-20 comes from the portal file name; the postmark date could not be read on the card.

The picture side carries a printed song text, Sokszor úgy szeretnék sírni..., and no cipher. The address side has the plain address Szépreményű Tóth Jolánka írnőnek, Jász-Árokszállás. The enciphered message fills the left half of this side, runs along the bottom edge, and has six short rows in the stamp field.

The card belongs to a large family of postcards to Jolánka Tóth in one substitution cipher. The writer signs Feri, as on hcp-1216 and others, but it is not proved that all the Feris are one person. No earlier work existed on this number and no published solution of this card was found.

![Picture side, printed song text (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the plain address and the cipher text (source/address-large.jpg)](../source/address-large.jpg)

## Method

The key was taken unchanged from the finished family card hcp-1216. The solver deskewed the un-converted high-resolution scan of the address side, enlarged it row by row (2x to 5x), and read each sign into a manual ledger, `work/ledger.txt`. A short script decodes the ledger and prints the text. The transcription is manual and the solver knew the key while reading, so it was not blind. The independent reviewer read all rows again on its own enlargements and decoded the ledger with its own key table.

To reproduce, run this from the repository root:

```sh
python3 -I ciphers/hcp-1283/work/decode.py
```

It checks the SHA-256 hashes of the four images, decodes the ledger and prints the literal rows and the normalized text. It does not read the images.

## Key

**Cipher type: MASC + Steganography** (updated 2026-11-03). Hungarian simple monoalphabetic substitution with invented signs; the closing ([Ist]en vele, édes egyetlen reményem. Csókolom, Feri.) is hidden in six cipher rows in the stamp box, written under the postage stamp, which has since been lifted. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three strokes | m | gamma | t |
| short + long stroke | d | two strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | long stroke + short tick | h / p | loop with long tail | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | opposed bowls | cs | | |

On this card gy is written g + y. Dots over a sign give é, í, ö, ü; most other accents are not written and are supplied in normalization.

## Plaintext

Literal decipherment by written row (the stamp field is the last line; square brackets mark signs hidden or blotted and restored):

```text
01 szeretetédesjolankankiva
02 nomhogyalegjobbkedveben
03 talaljasoraimhogymulat
04 vasarnapremelemjolle
05 galabbisjobbanmintén
06 makisementemazucza
07 raojunalmasnekemit
08 azéletbarigahogypesten
09 lehetmulatdemindenpez
10 bekerüesnekemettöltar
11 tozkodnomkelmegaza
12 alegnagyobbbajhogynem
13 erzemjolmagamsehol
14 hamegacskavollehetakor
15 nemcserélnéksenkivelde
16 leszmégezjobbanis.jö
17 vöhétenkimegyeharasz
18 tiraszívaemégatanya
19 ilevegöt.miujsagarok
20 szalasbajarnak
21 eberekbegondoe
22 néharamöntudom
23 unatkozikdeenra
24 erekhatgondolok
25 dragahejetzs,soraitvarvaimadojaferi
stamp: [i][s][t]envele | édesegy | etelen | remeny | emcsoko | [l]omferi
```

The writer spells loosely: single for double consonants, j for ly, dropped final letters. The normalized text below is editorial; square brackets there mark letters not on the card, and ⟨ ⟩ marks words not understood.

**Hungarian:** Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Hogy mulat vasárnap? Remélem, jól, legalábbis jobban, mint én. Ma ki se mentem az uccára, oly unalmas nekem itt az élet. Bár igaz, hogy Pesten lehet mulat[ni], de minden pé[n]zbe kerü[l], és nekem ettől tartózkodnom kell. Meg az a legnagyobb baj, hogy nem érzem jól magam sehol. Ha meg a ⟨cskavol⟩ lehet, akkor nem cserélnék senkivel, de lesz még ez jobban is. Jövő héten kimegy-e Harasztira? Szív[j]a-e még a tanyai levegőt? Mi újság Árokszállásba[n]? Járnak-e Berekbe? Gondol-e néha rám? Ön, tudom, unatkozik, de én ráérek, hát gondolok. Drága ⟨hejetzs⟩, sorait várva, imádója Feri.

**Stamp field:** [Ist]en vele, édes egyetlen reményem. Csókolom, Feri.

**English:** My beloved sweet Jolánka! I wish that my lines find you in the best of moods. How are you enjoying yourself this Sunday? Well, I hope, at least better than I am. Today I did not even go out into the street, life here is so boring for me. True, one can have fun in Pest, but everything costs money, and I have to keep away from that. And the biggest trouble is that I do not feel well anywhere. But if ⟨unread word⟩ is possible (frame tentative), then I would not change places with anyone, but this will get better yet. Will you go out to Haraszti next week? Are you still breathing the farm air? What is new in Árokszállás? Do they go to Berek? Do you think of me sometimes? You, I know, are bored, but I have time, so I think [of you]. Dear ⟨unread word⟩, awaiting your lines, your adorer, Feri.

**Stamp field:** God be with you, my sweet only hope. I kiss you, Feri.

**Slovak:** Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Ako sa zabávate v nedeľu? Dúfam, že dobre, aspoň lepšie ako ja. Dnes som ani nevyšiel na ulicu, taký nudný je tu pre mňa život. Pravda, v Pešti sa dá zabaviť, ale všetko stojí peniaze a ja sa tomu musím vyhýbať. A najväčšia bieda je, že sa nikde necítim dobre. Ak však môže byť ⟨neprečítané slovo⟩ (rámec vety je neistý), potom by som nemenil s nikým, ale ešte to bude lepšie. Pôjdete budúci týždeň na Haraszti? Dýchate ešte vzduch z majera? Čo je nové v Árokszállási? Chodia do Bereku? Myslíte niekedy na mňa? Vy sa, viem, nudíte, ale ja mám čas, tak myslím [na Vás]. Drahá ⟨neprečítané slovo⟩, čakajúc na Vaše riadky, Váš ctiteľ Feri.

**Pole pod známkou:** S Bohom, moja sladká jediná nádej. Bozkávam Vás, Feri.

## What remains uncertain

- **Row 14 `a cskavol`** is not understood. All signs are clear. Csókával, csak a vol[na] and an instrumental in -val all need letters the card does not show. The frame "if ... is possible" is therefore tentative.
- **Row 25 `hejetzs`** is not understood. It may be a misspelled adjective or a pet name. A small tick follows it, so Drága ⟨...⟩, is taken as a form of address; that division is editorial.
- **Row 15 de:** read from a short stroke plus a long stroke. The short stroke touches the preceding l, an unexplained dot stands under the long stroke, and row 23 de has the strokes in the reverse order. The call rests partly on word sense.
- **Calls resting on word sense:** Jolánkám (the last sign of row 1 has two strokes, n), the p of vasárnap (drawn short+long), the d of drága, and bár (the sign is blotted).
- **Supplied letters:** mulat[ni], pé[n]zbe, kerü[l], szív[j]a-e, Árokszállásba[n]. Iga is normalized to igaz, gondoe to gondol-e. A doubled a at rows 11-12 is reduced to one.
- **Restorations:** stamp row 1 Ist (only sign bottoms show under the stamp), stamp row 6 l (a blot), stamp row 4 n (one stroke visible).
- **Places:** Haraszti is a place Jolánka stays at (hcp-1305; also hcp-1265, not yet final) but is not identified; Berek is read as a place name, also not identified.
- **Overwriting:** row 10 ettől and row 22 tudom are heavily inked; row 12 y and row 18 i are inked over but legible.

## Why the reading is believed correct

The family key, applied unchanged, gives connected, idiomatic Hungarian over 25 main rows and 6 stamp rows with no fitted value. Árokszállás, the addressee's town, appears inside the cipher independently of the plain address. The polite Ön register and the closings (Isten vele, csókolom) match the family. Words recur with the same signs: hogy four times, and jobban, nekem, mulat and gondol- twice each.

## Review and what changed

A separate Claude Opus 5.5 agent reviewed the solution. It reran the command, wrote its own key table and decoder (0 mismatches, every token mapped), read all 25 main rows on its own enlargements, and tried to refute the reading. Its verdict was REVISE: key and most of the letter correct, with three major and five minor findings. The solver re-examined the pixels of each and accepted all eight:

- **Rows 17-18:** the first handover had Feri going to Haraszti, with invented letters (kimegye[k], szívom meg). With the question particle -e the signs read as questions to Jolánka: kimegy-e, szív[j]a-e még. This reverses who travels.
- **Row 19:** the last sign is k, not g; the claimed spelling Árog- was false.
- **Row 15:** the first handover read `!` and discarded the following e. It now reads de, with the caveat above.
- **Smaller changes:** three missing accent dots added (nék, még twice); Árokszállásba[n] replaces Árokszálláson; the last sign of `hejetz` read as s plus a tick; two full stops ledgered; row counts corrected; Haraszti tied to the sister cards.

The key did not change, and the rest of the letter is as first read.

The reviewer could not verify the postmark date, or the three signs under the stamp and the blotted l beyond their compatibility with the sign remains.
