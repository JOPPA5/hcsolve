# HCP 1261 (cpc_1912-03-07_HU__HU_Jasz Arokszalas_jolanka-07): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 19 main rows, the left-edge column, the bottom row and the stamp box); independent review 1 verdict REVISE, all findings addressed; one word division changed, no sign value changed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1261 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1261), portal name cpc_1912-03-07_HU__HU_Jasz Arokszalas_jolanka-07, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side shows a couple embracing by moonlight, with a printed Hungarian verse: *Örömest jöttünk ki az éjszakába, / Nem háborgat minket a hold világa. / Jer közelebb drágám ülj ide, / Hadd nézzek gyönyörű szemedbe.* It carries no cipher text.

The address side is written in pink ink. The address is plain: *Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás* ("to the promising young lady Jolánka Tóth, Jászárokszállás"). The message is in invented signs: 19 rows on the left half, a short column down the left edge, a row along the bottom edge, and a small block in the stamp box. One postmark shows 912 and a Roman month, partly lost; the other shows 912 MAR 7, which agrees with the date 1912-03-07 in the portal file name.

![Address side with the cipher text, the plain address and the postmarks (source/address-large.jpg)](../source/address-large.jpg)

![Picture side with the printed verse (source/picture-large.jpg)](../source/picture-large.jpg)

The card belongs to the "Jolánka" family: Hungarian postcards to Jolánka Tóth in one hand and one cipher, signed Feri. Several are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). The key was **transferred unchanged** from those cards; it is not a new recovery. The family key was first worked out with the OpenAI GPT solver (see the HCP 1216 notes). No earlier work on this number existed, and no published solution of this card was found or used.

## Method

The transcription is **manual**. The solver read every sign from enlarged crops of the high-resolution original of the address side and recorded one token per written sign in a ledger of 445 tokens. No OCR was used. A short script checks the hashes of the scans and decodes the ledger with the family key.

Row 1 gave *ne haragudjon érte hogy* at once. The reading order then came from the text: the sentence ending row 19 (*…nem pediglen kér*) continues down the left edge (*b. sorait*), turns the corner into the bottom row (*várva … Feri*), and closes in the stamp box. The last words in the stamp box change to plain cursive.

The reviewer cut separate crops, read the whole card independently with neutral shape names, and decoded it with its own script and key table. The two readings differed only at the blotted signs that the solver had already flagged, plus the points listed under Review summary.

## Key

Simple monoalphabetic substitution with invented graphic signs; the plaintext is Hungarian. The names are conventional labels for handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | hook ")" | s |
| six + hook | cs | three strokes | m | gamma | t |
| tick left + long stroke | d | two strokes | n | plain x | u (dots ü) |
| three bars | e | cursive loop | o (dots ö) | chevron | v |
| upright cross | f | long stroke + tick right | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | g + y joined | gy | | |

The h/p sign is one sign for two letters, and the writer does not cleanly separate it from d.

## Plaintext

Literal decipherment, row by row. `*` marks a blotted or ambiguous sign, `[#]` a blot without a value, `^` a plain letter.

```text
01 neharagudjonertehogy
02 ijsürünküldömalapo
03 katdeennemagygondol
04 kozommintönenekem
05 jolesikhaönnelbeszel
06 hetekedesjolankammert
07 enmikorsoraimirom
08 ö[#]nn*ekugyerzemmagammint
09 habeszlgnekedesjolankam
10 elsemtudjakepzelaimily
11 hoszuidöazmegmegka
12 pomsoritugyszeretnem
13 harepülnealev*elerepülö
14 gepetszerzekbehogygy
15 orsabanjönnebecseslapjai
16 m^idengondolatnal
17 atettlegtöbbeter
18 igytes*zkicsókotad
19 snempediglenker
E  b.sorait
B  varvamaramaradokszivenekrabszolgajaferi
S1 istenvele
S2 atavolb.
S3 olcsoko
S4 ljaszam
S5 talanszo
S6 r, then plain: egy igaz
S7 plain: sziv
```

**Hungarian (normalized):** Ne haragudjon érte, hogy ily sűrűn küldöm a lapokat, de én nem [úgy] gondolkozom, mint Ön. Énnekem jól esik, ha Önnel beszélhetek, édes Jolánkám, mert én, mikor soraim írom Önnek, úgy érzem magam, mintha beszélgetnék, édes Jolánkám. El sem tudja képzelni, mily hosszú idő az, még megkapom sorait. Úgy szeretném, ha repülne a levele; repülőgépet szerzek be, hogy gyorsabban jönne becses lapjai. Minden gondolatnál a tett legtöbbet ér. Így tesz, ki csókot ad, s nem pediglen kér. B[ecses] sorait várva maradok szívének rabszolgája, Feri.

Stamp box: Isten vele! A távolból csókolja számtalanszor egy igaz szív.

**English:** Do not be angry that I send you cards so often, but I do not think the way you do. It does me good when I can talk with you, my sweet Jolánka, because when I write my lines to you I feel as if I were talking [with you], my sweet Jolánka. You cannot imagine what a long time it is until I get your lines. How I wish your letter could fly; I will get an aeroplane so that your esteemed cards come faster. Above every thought, the deed is worth the most. So does he who gives a kiss and does not merely ask for one. Awaiting your esteemed lines, I remain the slave of your heart, Feri.

Stamp box: God be with you! From afar one true heart kisses you countless times.

**Slovak:** Nehnevajte sa, že Vám tak často posielam pohľadnice, ale ja [tak] nezmýšľam ako Vy. Mne dobre padne, keď sa môžem s Vami rozprávať, sladká moja Jolánka, lebo keď Vám píšem svoje riadky, cítim sa, akoby som sa rozprával, sladká moja Jolánka. Ani si neviete predstaviť, aký dlhý je to čas, kým dostanem Vaše riadky. Tak by som chcel, aby Váš list letel; zaobstarám si lietadlo, aby Vaše vážené pohľadnice prichádzali rýchlejšie. Nad každú myšlienku má najväčšiu cenu čin. Tak robí ten, kto bozk dáva, a nie ten, kto oň prosí. Čakajúc na Vaše vážené riadky, zostávam otrokom Vášho srdca, Feri.

V rámčeku na známku: S Bohom! Z diaľky Vás nespočetnekrát bozkáva jedno verné srdce.

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1261/work/decode_opus.py
```

The command checks the SHA-256 of all four scans, decodes work/ledger-opus.txt and prints the literal rows and the normalized text.

## Uncertainties

None of these changes the sense of the message. They rest on word sense, not on the shape alone.

1. **Row 3:** the sign before *gy* is two bars (a), where sense wants *úgy*. Printed as written, with [úgy] supplied. The clause means "I do not think as you do" either way.
2. **Row 8, *önnek*:** six written signs for a five-letter word: ö, a heavy blot, two strokes, a stroke pair nearer d than n, e, k. The blot is treated as a discarded false start.
3. **Blots in rows 13 and 18:** v in *levele* rests on a chevron-like arm plus sense, s in *tesz* on sense alone.
4. **Row 13, *a levele; repülőgépet*:** the writer leaves no word spaces, so this division is editorial. See Review summary.
5. **h/p/d:** p against h is decided by sense only, since the sign is the same, and the d is close to it too. *Pediglen* is a genuine older emphatic form of *pedig*.
6. **Row 10:** two bars where *képzelni* needs n, a writer's slip.
7. **Writer's omissions, restored in normalization only:** *beszlgnek*, *sorit*, *miden*, *hoszu*, *orsaban*, *ij* (ily), *még* for *míg*. *Jönne* stays singular with plural-sense *lapjai*, as written.
8. **Bottom row, *mara maradok*:** the writer began the word and restarted. Normalized to one *maradok*.
9. **Left edge, *b.*:** expanded *b[ecses]* because *becses lapjai* occurs in row 15. This is an interpretation: the same six + dot falls inside the word *távol-b.-ól* in the stamp box, where it cannot be an abbreviation.
10. **Row 16:** the first letter is a plain Latin capital M, not the cipher sign.
11. **Stamp box:** heavy ink. The first sign of S2 is a filled loop, read a on sense. The closing *egy igaz szív* is plain cursive, and its last letter is uncertain.
12. **Unread line:** a short line stands below *úrleánynak* in the address, partly under the collection stamp. It looks like plain cursive, roughly *sz r t*, then spaced letters including *e e e t*, then a heavy blot. Neither solver nor reviewer could read it. It lies outside the cipher text and is reported, not forced.
13. **Sender:** the signature reads *Feri*. No surname is claimed. Acute accents are mostly invisible and are supplied in normalization.

## Review summary

Review 1 was carried out independently by a separate Claude Opus 5.5 agent, which tried to refute the solution. Its verdict was **REVISE**: the key, the reading order and nearly every word were confirmed; 440 of 444 ledger signs agreed, and the differences were all flagged blots. It found no undisclosed misreading and no sign of a published solution. It raised five findings, and all were accepted:

1. **Major, row 13:** the first version divided *a levél: e repülőgépet* ("this flying machine"), but the picture shows no aeroplane for *e* to point at. Now *a levele; repülőgépet szerzek be* ("your letter… I will get an aeroplane"), which needs no change of signs and fits the formal address. The normalized text and both translations changed.
2. **Minor, row 8:** the ledger had dropped a written sign. A valueless blot token was added, and the count rose from 444 to 445.
3. **Minor, row 16:** the plain capital M is now marked in the ledger and disclosed.
4. **Minor, dot after 6:** the dot inside *távol-b.-ól* is now disclosed against the *b[ecses]* expansion.
5. **Minor, English:** "with you" is now bracketed, since the Hungarian has only *beszélgetnék*.

The reviewer could not verify the blotted signs beyond their sense, the unread address line, the place and month on the right-hand postmark, or the sender's identity.

## Credits

Transcription, key transfer and decipherment by Claude Opus 5.5; independent review by a separate Claude Opus 5.5 agent. The family key comes from earlier finished cards, first worked out with the OpenAI GPT solver.

## Sources

- HC Portal record: https://crypto.hcportal.eu/dashboard/cryptograms/1261
- Scans from the portal; files and hashes are listed in SOURCES.md.
- HistoCrypt paper on the collection: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- Sister cards in this repository: HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301.
