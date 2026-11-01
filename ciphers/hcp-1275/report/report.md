# HCP 1275: Feri's farewell to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: PARTIAL. All of the card's roughly 721 cipher signs are transcribed and decoded and nearly all of the letter reads, but one whole clause (rows 2–4) and two further words are not understood. Independent review 1 verdict REVISE; findings addressed, no letter value changed. No register entry is made for this card.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1275 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1275), portal name cpc_1913-08-13_HU__HU_Jasz Arokszalas_jolanka-40, from Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was found or used.

The picture side is a printed tinted photograph of a young couple, headed *Két szív ha földobog…* ("When two hearts leap up…"). The printed verse beside it says that the rich may hope while the poor stays alone. It carries no cipher, but it matches the complaint in the message about a richer rival.

The address side is in plain writing to Tóth Jolánka at Jászárokszállás, Hungary. The date 1913-08-13 comes from the portal file name; only 913 can be read in the cancellation at the stamp. The cipher fills the left half of the address side, then runs in four long rows across the bottom and up the right edge. Six more short rows, holding the signature, were written under the stamp, which has since been lifted.

![Address side: 27 cipher rows, the plain address, and the place of the lifted stamp (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: printed text only (source/picture-large.jpg)](../source/picture-large.jpg)

The card belongs to the family of cipher postcards to Tóth Jolánka. Several are deciphered in this repository (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). This card uses the same hand and the same key, and it has the family's habit of hiding a signature under the stamp.

## Method

The key was **transferred** from the finished family cards, not reconstructed. Every value was then confirmed on this card by words that recur or read clean.

The transcription is manual. Claude Opus 5.5 read every row from enlarged crops of the unconverted scan, using the red channel for the stamp block, and recorded one token per sign in a ledger. A short script checks the hashes of the images, decodes the ledger and prints the rows. The card has no key change and needs no value outside the table. The letter distribution fits Hungarian (index of coincidence 0.065; e 99, a 80, t 50 of 713 letters).

## Key

Monoalphabetic substitution with invented graphic signs (register label MASC). Only the opening M is an ordinary Latin capital.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | S-shaped section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left + right bowl | cs | three short strokes | m | gamma/corner | t |
| short then long stroke | d | two short strokes | n | bold plain cross | u (two dots: ü) |
| three bars | e | cursive loop | o (dots: ö, ő) | chevron | v |
| upright cross | f | long then short stroke | h / p | low loop with descender | y |
| lightning-shaped sign | g | dotted crossed curve | i | crossed diagonal with flag | z |
| inverted T | j | large joined loop + y | gy | | |

The h/p sign is one class; the only p on this card (*fénykép-*) is decided by word sense.

## Literal decipherment

`{}` marks a doubtful sign, `[]` a restored hidden one. E1 runs up the right edge; S1–S6 lie under the stamp.

```text
01 mejentiszteltjolanka
02 kisaszonyönaztmondta{n}agy
03 körhogynemhalgatah{?l}ely
04 karamikormegszeretelvolt
05 irantameznemlehetoka
06 elhidegülesinekirantam
07 masokotnemtalelhatok
08 minthogyakadtegyma
09 sikakigazdagabescsinosabb
10 legenyakinekszerencseje
11 voltmagatelhoditani
12 nemalokutja{d}alegyan
13 boldoojanbodoghogy
14 eszebesejusakhogynebant
15 saalelkiismerethogyaz
16 szivemöszetörtlehethogy
17 azistenmajdojanjohogy
18 megvaltafajdalmeimtol
19 majdakorenisbodogleszek.
20 eztavasutasnekalanyarol
21 amitirnemtudoksemitirni
22 mertnemtudommirölvan
23 szo.fenyke{p}itaztsoheki
24 nemadomkezböleden,ugyatöbbi{g}{t}ergyakotsemlegelabb
25 ezeketlethatomesmegleszorökitveemlekeber{z}ivem
26 beotleszorökreazenyemeltehetamitakarnekemmindegy
27 ha{t}üzbeteszivagyviszakildííslegalabbnemzaverjabold
E1 ogsagat
S1 sir{i?}[g]
S2 hüima
S3 dojaes
S4 volt
S5 kedves
S6 se{f}eri
```

## Plaintext (normalized Hungarian)

Mélyen tisztelt Jolánka kisasszony! Ön azt mondta, [unread clause: a nagy kör(?), hogy nem hallgat a h?ely(?), kár(?),] amikor még szeretet(?) volt irántam. Ez nem lehet oka elhidegülésének irántam; mást nem találhatok, mint hogy akadt egy másik, aki gazdagabb és csinosabb legény, akinek szerencséje volt magát elhódítani. Nem a lokutja(?), de legyen boldog, olyan boldog, hogy eszébe se jussak, hogy ne bántsa a lelkiismeret, hogy az [én] szívem összetört. Lehet, hogy az Isten majd olyan jó, hogy megvált a fájdalmaimtól, majd akkor én is boldog leszek. Ezt a vasutasnak a lányáról, amit ír, nem tudok semmit írni, mert nem tudom, miről van szó. Fényképét azt soha ki nem adom kezből, eden(?), úgy a többi tárgyakat sem; legalább ezeket láthatom, és meg lesz örökítve emlékbe, szívembe ott lesz örökre az enyém. Eltehet, amit akar, nekem mindegy, ha tűzbe teszi vagy visszaküldi is, legalább nem zavarja boldogságát.

Under the stamp: Sírig hű imádója és volt kedvese, Feri.

## English translation

Deeply respected Miss Jolánka! You said [unread clause: literally perhaps "the great kör(?), that does not listen to the h?ely(?), a pity(?)"], when there was still love(?) for me. That cannot be the reason for your cooling towards me; I can find no other than that there is another, a richer and more handsome young man, who had the luck to win you. Not the [lokutja?], but may you be happy, so happy that I do not even come to your mind, that your conscience does not trouble you that my heart is broken. Perhaps God will be so good as to deliver me from my pains; then I too shall be happy. About the railwayman's daughter whom you write of, I can write nothing, because I do not know what it is about. Your photograph I will never let out of my hand, [eden?], nor the other things; at least I can look at these, and it will be immortalized in memory; in my heart, there it will be mine forever. You may put away what you want, it is all the same to me, even if you put it in the fire or send it back; at least it does not disturb your happiness.

Under the stamp: Your adorer, faithful unto the grave, and former sweetheart, Feri.

## Slovak translation

Hlboko vážená slečna Jolánka! Povedali ste, [neprečítaná veta: doslova azda „veľký kör(?), že nepočúva h?ely(?), škoda(?)“], keď ešte bola(?) láska ku mne. To nemôže byť príčinou Vášho ochladnutia voči mne; nemôžem nájsť inú, než že sa našiel iný, bohatší a krajší mládenec, ktorý mal šťastie Vás získať. Nie [lokutja?], ale buďte šťastná, taká šťastná, aby som Vám ani na um neprišiel, aby Vás netrápilo svedomie, že moje srdce je zlomené. Možno bude Boh taký dobrý, že ma vyslobodí z mojich bolestí, potom budem šťastný aj ja. O tej dcére železničiara, o ktorej píšete, nemôžem napísať nič, lebo neviem, o čo ide. Vašu fotografiu nikdy nedám z ruky, [eden?], ani ostatné veci; aspoň sa na ne môžem pozerať, a bude zvečnená v pamäti; v mojom srdci, tam bude navždy moja. Môžete si odložiť, čo chcete, mne je to jedno, aj keď to dáte do ohňa alebo pošlete späť; aspoň to neruší Vaše šťastie.

Pod známkou: Váš do hrobu verný ctiteľ a bývalý milý, Feri.

## What remains uncertain

- **Rows 2–4, the unread clause (the reason the card is partial).** *Ön azt mondta* and *amikor … volt irántam* are sure. Between them the row 2 sign is a blot, not recognisably n, so *a nagy* is context only. The word `h{?l}ely` has a sign under the postmark and is not established. *kör* could also be *kor*. `kar` may be *kár* ("a pity") or the end of the previous word. Row 4 could be *még szeretet volt* or *meg szerettél volt*. The next sentence answers this clause, so the context does not supply it.
- **Row 12 `alokutja`:** all signs are clear, but the word is not identified.
- **Row 24 `eden`:** all signs are clear, but the word is not identified. It does not affect the sentence around it.
- **Readings from context, not from clean signs:**
  - Row 12 `{d}` is a blotted sign before two bars (*de*; h is not excluded).
  - Row 24 `{g}{t}` gives *tárgyakat*.
  - Row 25 `R {z}` is one overwritten composite, and no s is visible for *szívem*.
  - Row 27 `{t}ü` is a single wide arch with two dots running into the card edge, so *tűzbe* rests on context.
  - Row 13 `boldo ojan` has an o-like sign where g is expected.
  - S6 `{f}` is blotted and rests on the name Feri.
  - The g in S1 is hidden and restored from the family formula *sírig hű*.
- **Sign count:** 721 is approximate, because of the places above.
- **Spelling:** the writer spells unevenly (ly as j, single for double consonants, a and e swapped). The normalized text is an editorial step. Marks at the torn edge below S6 look like remains of the printed stamp, but a further sign cannot be excluded.
- **People:** Feri and the railwayman's daughter are not identified.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-ran the decoder, read the card from its own crops and recorded the signs in its own codes. 718 characters agreed with the solver, and six spans differed. Its verdict was **REVISE**: cipher and key are right, but the status and one passage had to change.

1. The card was called "whole message deciphered". It is now labelled partial because of rows 2–4, and no register entry is written. Further attempts on the clause gave no sentence.
2. Rows 20–21 were mis-divided (*írnom tudok*). They now read *amit ír, nem tudok semmit írni*, "whom you write of, I can write nothing".
3. Row 10 ends in e, not a (`szerencseje`).
4. Row 27 has two ticked i signs (`viszakildíís`), not o + í.
5. S6 is marked doubtful (`{f}`).
6. The one p is marked as a word-sense decision.
7. Row 25 is *meg lesz örökítve*, "will be immortalized", not *még*.
8. The sign count is now called approximate.
9. The date and its evidence are stated.

No key value changed.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1275/work/decode_opus.py
```

## Credits

Portal capture, key transfer, transcription, decipherment, response to review and this report: Claude Opus 5.5, 2026-11-01. The family key comes from earlier cards, where the work is credited to the OpenAI GPT solver and Claude Opus 5.5. Independent review: a separate Claude Opus 5.5 agent.
