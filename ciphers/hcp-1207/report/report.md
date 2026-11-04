# HCP 1207 (cpc_--_HU__HU_Budapest_jolanka-62): Feri to Jolánka Tóth, ordered onto a train

Human solver: Tomáš Pavuk

**Status: all ciphertext deciphered (23 rows, plus six rows in the stamp square), with one stray sign and two plain pencil marks in the address unread; independent review 1 verdict REVISE, findings addressed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1207 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1207), portal name cpc_--_HU__HU_Budapest_jolanka-62, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was found or used.

The picture side is a tinted photographic card of a couple seated together, with a printed Hungarian verse headed "Oh csak még egyszer összejönnénk" ("Oh, if only we could meet once more"). The verse is a commercial caption and not part of the message.

The address side is in plain pencil: **Szépreményű Tóth Jolánka úrleánynak, Budapest, Petőfi …** ("To Miss Jolánka Tóth, of fair hopes"), with a street number read as 10 or 16, partly under the portal seal. The postmark shows only BUD… and 13, so no full date can be given. The message is written in pencil across the left half of the card, in 23 rows, the last of which runs on along the bottom edge under the address to the right corner. Six more rows, also in the cipher signs, stand in the square for the stamp: the stamp has since been lifted, and the postmark stops at the edge of the square, so these rows were hidden under the stamp when the card was posted (a stamp-box audit of 2026-11-03 re-read them from the original and confirmed the reading: Csókolom számtalanszor, hű kedvese Feri). Row 9 mixes in plain matter: the digits 7 0 and the cursive word "orakor".

The card belongs to the Jolánka family of Hungarian cipher postcards addressed to Jolánka Tóth, several of them signed Feri, who writes elsewhere about trains and travel. The surname Pásztori read on this card also appears on sister card HCP 1290.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher rows at the left and the stamp square at the top right (source/address-large.jpg)](../source/address-large.jpg)

## Method

The key was **transferred unchanged** from the family, where it was reconstructed on sister cards (HCP 1216 and related cards; earlier work there by an OpenAI GPT solver and later by Claude Opus 5.5). It is not a new key recovery. The transcription and reading of this card are new, by Claude Opus 5.5.

The transcription is **manual**, not OCR: every row was read sign by sign from enlargements of the un-converted original scan, and each written sign was recorded in a ledger (work/ledger-opus.txt). The command `python3 -I ciphers/hcp-1207/work/decode_opus.py`, run from the repository root, checks the SHA-256 of the scans, decodes the ledger and prints the literal rows and the normalized text.

The h/p sign is a known problem in this family: the two letters share one shape class, so the choice between them rests on word sense. The same is true of some g/d and d/h calls, listed under Uncertainties.

## Key

Cipher type (register label, updated 2026-11-03): **MASC + Steganography**. Simple monoalphabetic substitution with invented graphic signs, with joined digraph signs for cs and gy; part of the message is hidden under the stamp. The labels are conventional names for handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three strokes | m | gamma | t |
| long stroke + short tick | d (near h/p) | two strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short | h / p | low descender | y |
| hooked stroke with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | joined hook + descender | gy | | |

Dots over o give ö. The Hungarian digraph sz is written with the two signs s + z.

## Plaintext

Literal decipherment, row by row, as written (the letter h stands for the h/p sign throughout; {?} is the stray sign):

```text
01 szertetedesegyetlen
02 remenyemkivanomhogyaleg
03 jobbkedvebentalaljaso
04 raimsajnalattalkeltu
05 datnomhogyemitöleny
06 nyirafeltembekövet
07 kezetmertojanvonathoz
08 lettemvezenyelveeseste
09 7 0 [orakor] jönviszaesregel
10 retelikleahihenöm
11 esigylegnagyobbsajnala
12 tomrakedenenestelatoga
13 hatommegdecsakkeson
14 nemerkezekhazaedesem
15 irjameghogymikomegyhasz
16 toriektolcsakmararadjo
17 nonededesemamedilehet
18 mulasonjolhamarenem
19 mulathatokmagaval
20 edesemhajolmulatgon
21 doljonimdojarki
22 ijsokatgondol{?}kodom
23 magafelölistenveledesemimadojaferi
stamp square: csoko / lomsza / mtalan / szo{r|h}ű / kedvese / feri
```

**Hungarian, normalized.** Square brackets mark letters with no sign on the card. Other spelling changes are listed under Uncertainties.

Szer[e]tet[t] édes egyetlen reményem! Kívánom, hogy a legjobb kedvében találja soraim. Sajnálattal kel[l] tudatnom, hogy [a]mitől ennyire féltem, bekövetkezet[t], mert olyan vonathoz lettem vezényelve, és este 7 0 [sic] órakor jön vis[s]za, és reg[g]elre telik le a pihenőm, és így legnagyobb sajnálatomra ked[d]en én este látoga[t]hatom meg, de csak későn, nem érkezek haza, édesem. Írja meg, hogy miko[r] megy Pásztoriéktól. Csak maradjon ön, édesem, amed[d]i[g] lehet, mulas[s]on jól, ha már én nem mulathatok magával. Édesem, ha jól mulat, gondoljon im[á]dójár[a], ki ily sokat gondolkodom maga felől. Isten vele, édesem. Imádója Feri.

Stamp square: Csókolom számtalanszor, hű kedvese Feri.

**English.** My beloved sweet only hope! I wish that my lines find you in the best of moods. I regret to have to tell you that what I so feared has happened, for I have been ordered onto a train that comes back at 7 [written "7 0"] o'clock in the evening, and my rest period is over by morning, and so, to my greatest regret, I can visit you on Tuesday evening, but only late, I will not get home [sooner], my sweet. Write and tell me when you are leaving the Pásztoris'. Just stay, my sweet, as long as you can, have a good time, since I cannot have a good time with you. My sweet, when you are having a good time, think of your admirer, who thinks about you so much. God be with you, my sweet. Your admirer, Feri.

Stamp square: I kiss you countless times, your faithful sweetheart, Feri.

**Slovak.** Moja milovaná sladká jediná nádej! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. S ľútosťou Vám musím oznámiť, že to, čoho som sa tak bál, sa stalo, lebo ma pridelili na taký vlak, ktorý sa vracia večer o 7 [napísané „7 0"] hodine, a do rána sa mi skončí oddych, a tak Vás, na moju najväčšiu ľútosť, môžem navštíviť v utorok večer, ale až neskoro, skôr domov neprídem, drahá. Napíšte mi, kedy odchádzate od Pásztoriovcov. Len zostaňte, drahá, kým sa dá, zabavte sa dobre, keď už ja sa s Vami nemôžem zabávať. Drahá, keď sa budete dobre zabávať, myslite na svojho ctiteľa, ktorý na Vás toľko myslí. S Bohom, drahá. Váš ctiteľ Feri.

V štvorci na známku: Bozkávam Vás nespočetnekrát, Váš verný milý Feri.

## Uncertainties

The writer drops and repeats letters. The ledger keeps what is written; the normalization is editorial.

1. **Unread pencil marks in the address, not cipher.** Below the Petőfi line, one more short pencil line runs under the portal seal to the right edge. Neither solver nor reviewer could read it, even with colour separation (one or two words, ending roughly "-lleg…" or "-hegy"). A small separate mark at the extreme right edge above the end of row 23 (roughly "Hé" or "Hö") is also unread; it may belong to that line or be a further note. Both are plain address matter, not message clauses.
2. **Row 9, "7 0 orakor".** Plain figures and a plain cursive word. The time is taken as 7 o'clock; why the 0 stands there is unknown. The subject of "jön vissza" is taken as the train.
3. **Row 15/16, Pásztoriéktól.** The signs are clear; the reading takes the h/p sign as p. The name is on HCP 1290. That it is the same household, and that Jolánka was staying there in Budapest, is a hypothesis.
4. **Row 13/14, "de csak későn, nem érkezek haza".** All signs read, but the clause order is odd. The alternative is that "nem" is a slip. Either way he comes late.
5. **Calls resting on word sense.** h/p: p in pihenőm (row 10, first of its two h/p signs) and Pásztori- (row 15), h elsewhere. g against d: regelre (row 9), first g of legnagyobb (row 11), ameddi (row 17). d against h/p: de (row 13; the reviewer types the sign as h/p, the solver as d, and only de gives a word), the h of -hoz in vonathoz (row 7). The i of vissza (row 9) has no dot and is read by word sense.
6. **Row 22, stray sign.** Between gondol and kodom stands a tick plus long stroke with no value in the word. It is printed {?} and dropped as a false start.
7. **Row 21–22.** imdojar ki is normalized im[á]dójár[a], ki; ij is read ily (the writer's l-j spelling, as ojan for olyan), with a slanted j.
8. **Stamp square.** In row 4, after szo stands a reduced tall stroke, then a cross with a heavy mark. Either szor + ű with h omitted, or szo with r omitted + hű. The normalization is számtalanszor, hű either way. A few signs here are cursive variants read by word sense.
9. **Spellings changed without brackets.** emitöl to [a]mitől (written e); enynyira to ennyire; ojan to olyan; mararadjo|non to maradjon ön (repeated ar, ö without visible dots); ededesem to édesem (repeated ed); veledesem to vele, édesem (one e serves both). In row 12 a loop is written over two strokes in latoga and read o. Accents are mostly not visible and are supplied.
10. **Date and sender.** No full date is legible. Feri is the signature here; that he is the same man as on every other Feri card is likely but not proven.

Why the reading is trusted: the key was transferred unchanged and turns every sign into Hungarian, with one stray sign left over. Repeated words decode identically (édesem four times plus édes, hogy three times, mulat- three times). The story is specific and unforced, and the opening and closing are family formulas that the signs give without being assumed.

## Review and what changed

An independent Claude Opus 5.5 reviewer ran the command, walked every row on its own crops, and decoded its own row reading with a separate key table. 22 of 23 rows were identical; row 13 differed only at the near-homograph before csak (item 5). The reviewer notes that it had seen the solver's ledger first, so this is a check on the pixels and not a blind transcription. Verdict: **REVISE**.

1. **Major: row 15/16.** The first reading was "haza Toriéktól", with an invented pet name Tori and two emendations. The reviewer showed that taking the h/p sign as p gives Pásztoriéktól with no emendation, a name known from HCP 1290. Accepted; no sign changed, only the h/p choice and the translations.
2. **Minor: dropped t.** látoga[t]hatom is now marked, and brackets were made consistent.
3. **Minor: a count.** édesem occurs four times, not five.
4. **Minor: address.** The corner mark was added to the disclosure; both unread items stay unread.
5. **Minor: wording.** The h/p calls are now listed in one place.

No key value and no ledger sign changed. The reviewer could not verify the two address marks, the household link, or the reason for the 0 in row 9, and neither can this report.
