# HCP 1228: Feri to Jolánka Tóth, six kilometres away in a railway uniform

Human solver: Tomáš Pavuk

**Status: deciphered; one word of the text rests on a doubtful normalization and one word was struck out by the writer. Independent review 1 verdict REVISE; all seven findings addressed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1228 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1228), portal name cpc_1913-09-07_HU__HU_Jasz Arokszalas_jolanka-42, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The date 1913-09-07 and the place Jász-Árokszállás come from the scan file name. The postmark is too faint to confirm the date.

The picture side is a tinted photographic card: a man and a woman speaking by telephone, with the printed Hungarian captions "Szerelmi üzenet. Halló! Ki beszél? Kedvesed!" ("Love message. Hello! Who is speaking? Your sweetheart!"). The address side carries the plain address (Őnagysága Tóth Jolánka úrleánynak, Jász Árokszállás, that is, "To Her Ladyship Miss Jolánka Tóth") and the whole cipher message in green ink: 27 rows, plus six short rows written around the stamp.

The card belongs to the family of cipher postcards addressed to Jolánka Tóth. It was read with a **known, transferred key**, taken from the finished cards HCP 1216, 1212, 1213, 1217, 1218, 1243 and 1301. It is not a new key recovery. No reading of this card was supplied or consulted, and no earlier solver had worked on this number. No separate web search was made; the orchestrator's check of the AI Decipherment Register on 2026-11-02 found no record.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text and the rows around the stamp (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is **manual**. The solver read every sign from enlarged crops of the un-converted scan, with the family key in mind, so the reading is not blind. Each written sign is one token in the file work/ledger.txt (27 rows plus 6 stamp rows). The script work/decode.py checks the SHA-256 of the four image files, decodes the ledger and prints the literal text and the normalized text:

```sh
python3 -I ciphers/hcp-1228/work/decode.py
```

Every sign on the card falls into a sign class of the family key, and no new value was needed. Two near-homographs of the family were decided by sense and are listed under Uncertainties: the tall stroke with a short tick stands for h or p, and on this card once for d.

## Key

Monoalphabetic substitution with invented graphic signs. Word spaces are mostly kept, and digits stay in clear (6, 1/2, 11).

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| short + long stroke | d | two short strokes | n | plain thick cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short tick | h / p | descender with hook | y |
| open loop with descender | g | dotted crossed curve | i | curled crossed diagonal | z |
| inverted T | j | | | | |

Marks over a sign: two dots give ö or ü; a tick or dot gives á, é and the like. The digraphs gy and ny are written g + y and n + y. The g ends in a straight tail and the k in a hook curling left.

## Plaintext

Literal decipherment, as printed by the command. Square brackets mark restored signs, and the spelling is the writer's. The first word of row 10 was struck out by the writer and is not read.

```text
01 szeretet edes egyetlen remenyem
02 kivanom hogy a legjobb egesség
03 ben talalja soraim. az éjel voltam
04 magához közel csak 6 kilométer ta
05 volságra de sajnos épen anyit ert
06 mint ha ot se lettem volna mert
07 nem láthattam de jobban van ez
08 igy mert ha elmetem volna csak
09 kellemetlen let volna maganak
10 [cancelled] eben a vasuti ruhaban va
11 lo l.átas majd lehet hogy meg
12 virad meg enneke is valaha
13 azt tartom hogy türöké. es
14 szenvedöké a menyeknek országa
15 hát én is var[o]k varok még a viszont
16 látásörömeit élvezhetem
17 hana ha lme[n][t]em volna ara akar
18 hogy haragudot volna is rám
19 bementem volna mert nem
20 tudtam volna ellentalni
21 vagyaimnak. mar 1/2 11kor pesten
22 voltam anyi volt az egész
23 othonlétem hogy megnéz
24 te szüleimet egessegesek ézel
25 bezrom soraim maradok
26 sirig hü kedvesse és imado
27 ja feri
S1 csokol
S2 ja szam
S3 talan
S4 sz[o][r]
S5 ima[d]o
S6 ja feri
```

**Hungarian (normalized):** Szeretett édes egyetlen reményem! Kívánom, hogy a legjobb egészségben találja soraim. Az éjjel voltam magához közel, csak 6 kilométer távolságra, de sajnos éppen annyit ért, mintha ott se lettem volna, mert nem láthattam. De jobban van ez így, mert ha elmentem volna, csak kellemetlen lett volna magának [törölt szó] ebben a vasúti ruhában való látás. Majd lehet, hogy megvirrad még énnek[em] is valaha. Azt tartom, hogy tűrőké és szenvedőké a mennyeknek országa. Hát én is várok, várok, míg a viszontlátás örömeit élvezhetem. Hanem ha [e]lmentem volna arra, akárhogy haragudott volna is rám, bementem volna, mert nem tudtam volna ellentállni vágyaimnak. Már 1/2 11-kor Pesten voltam, annyi volt az egész otthonlétem, hogy megnéztem szüleimet, egészségesek. Ezzel bezárom soraim. Maradok sírig hű kedvese és imádója, Feri.

Under the stamp: Csókolja számtalanszor imádója, Feri.

**English:** My beloved sweet only hope! I wish that these lines find you in the best of health. Last night I was close to you, only 6 kilometres away, but sadly it was worth just as much as if I had not been there at all, because I could not see you. But it is better this way, because if I had gone, it would only have been unpleasant for you [cancelled word] to see me in this railway uniform. Perhaps one day the dawn will come for me too. I hold that the kingdom of heaven belongs to those who endure and suffer. Well, I too wait, I wait, until I can enjoy the joys of seeing you again. But if I had gone that way, however angry you might have been with me, I would have gone in, because I could not have resisted my longing. By half past ten I was already in Pest; that was all there was to my stay at home, that I looked in on my parents, they are well. With this I close my lines. I remain, faithful unto the grave, your sweetheart and adorer, Feri.

Under the stamp: Your adorer Feri kisses you countless times.

**Slovak:** Moja milovaná sladká jediná nádej! Želám si, aby Vás tieto riadky našli v najlepšom zdraví. Minulú noc som bol blízko Vás, len 6 kilometrov ďaleko, ale žiaľ, malo to takú cenu, akoby som tam vôbec nebol, lebo som Vás nemohol vidieť. Ale je to takto lepšie, lebo keby som bol išiel, bolo by Vám len nepríjemné [prečiarknuté slovo] vidieť ma v tejto železničiarskej rovnošate. Možno raz svitne aj mne. Tvrdím, že trpezlivým a trpiacim patrí nebeské kráľovstvo. Veď aj ja čakám, čakám, kým si budem môcť vychutnať radosti opätovného stretnutia. Ale keby som bol išiel tam, nech by ste sa na mňa hnevali akokoľvek, bol by som vošiel, lebo by som nebol vedel odolať svojim túžbam. Už o pol jedenástej som bol v Pešti; to bol celý môj pobyt doma, že som pozrel rodičov, sú zdraví. Týmto končím svoje riadky. Zostávam Vám do hrobu verný milý a ctiteľ, Feri.

Pod známkou: Bozkáva Vás nespočetnekrát Váš ctiteľ Feri.

## Uncertainties

Readings that rest on word sense:

- **Row 17, hana ha lme[n][t]em.** This is the weakest place on the card. The signs h a n a are firm, but taking them as "hanem" and supplying the e of "[e]lmentem" rest on sense. The following clause fixes the meaning.
- **Row 4, final ta.** The first of the two signs looks like F (r) with a heavy second arm, near the printed divider. It is read t because "kilométer tá|volságra" is the only sense.
- **Row 7, de.** The first sign is the h/p shape, not the usual d. Read d from sense, as on HCP 1216. The alternative "hej" would not change the meaning.
- **Rows 5 and 21, épen and pesten.** p against h from sense, as usual in this family.
- **Row 12, enneke.** The signs are clear. Normalized "énnek[em]" ("for me"), which assumes a dropped m. "Virad" is taken as "megvirrad", used figuratively.
- **Rows 13–14.** The ending -ké reads naturally as "belongs to those who endure and suffer".
- **Row 15.** The accent on the a of "hát" is faint; the two-bar count does not depend on it. "Még" is normalized as dialect "míg" ("until").

Restorations of physically hidden signs:

- **Row 15, first var[o]k:** under a pale blot; a stub, a hook and a tail survive, and the same word follows in clear.
- **Row 17, lme[n][t]em:** n and t lie under a wet blot. One stroke of n and the top arm of t are firm.
- **Stamp rows:** in sz[o][r] the r shows outside the printed triangle and the o is only a bowl on the printed monogram; the d of ima[d]o is damaged. The two bars in the stamp disc are read as the writer's a, but could be print. The words are fixed by "számtalanszor" and by rows 26–27.

Other points:

- **Row 10:** the struck word, about 5 or 6 signs, could not be recovered by solver or reviewer. It has no effect on the sentence.
- **Spelling:** the writer's text has single consonants for double ones (szeretet, éjel, ot, let, anyit, anyi, menyeknek, eben and others), dropped letters (elmetem, bezrom, megnézte) and few accents. Accents are shown only where a mark is visible, and the normalized text supplies the rest.
- **Dots:** two small dots, inside l.átas in row 11 and after türöké in row 13, have no text value.
- **Date and person:** the date rests on the file name. That Feri was a railway employee rests only on "ebben a vasúti ruhában". No identification beyond the first name is claimed.

## Why the reading is believed correct

The family key, unchanged, turns all signs into continuous Hungarian with formal third-person address (találja, magának, haragudott volna) and the family's closing formula (sírig hű kedvese). Long words decode without forcing (egészségben, távolságra, kellemetlen, viszontlátás örömeit, vágyaimnak, szüleimet). The digits in clear agree with the words around them. Repeated words decode the same way: volna ×7, hogy ×5, mert ×3, soraim ×2, imádója Feri ×2.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **REVISE**. The reviewer re-ran the command, read all rows on its own crops, wrote its own shape-named transcription and decoded it with its own script, taking the letters from the HCP 1216 key file. The comparison was not blind, because the solver's text had been seen. It covered 666 letters: 21 of 27 main rows and all stamp rows agreed, and the real differences lay in four rows. It confirmed the key, the cipher type and the sense of the card.

What changed because of the review:

- Row 15 is **hát én is** ("well, I too"), not "héten is" ("all week"). This is the one change of meaning.
- Rows 5 and 22 are **anyit** and **anyi**. The solver had supplied a second n that is not on the card.
- Row 14 is **menyeknek**, not "menyegnek": the sign has the hook of k.
- The restored signs in row 17 and stamp row 4 are now marked, and the two written dots are recorded.
- Two wrong word counts and one Slovak phrase were corrected.

The reviewer could not verify the postmark date, the struck word, the meaning of "hana", or whether a published solution exists outside the portal.
