# HCP 1307 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-79): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 26 main rows and the 6 rows under the stamp, 591 written signs); independent review 1 verdict REVISE, all findings addressed, no change to the sense of the text.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1307 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1307), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-79, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt proceedings, https://ecp.ep.liu.se/index.php/histocrypt). When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language unknown, sender unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card turned up and no outside plaintext was used.

The picture side is printed: a four-line verse beginning "Én édes párom", with the title "Édes párom szállj velem…", and it carries no cipher. The whole message is on the address side, written in green ink in invented signs. Twenty-four rows fill the left part of the card; rows 25 and 26 run on along the bottom edge, below the address; six short rows stand in the box under the stamp.

The address is in clear: Tóth Jolánka urleányok(?) Jász Árokszállás. The line after the name reads literally like urleanyok, presumably for úrleánynak. The card was cancelled at **Rákospalota** (near Budapest), but the round cancel is almost blank and the date cannot be read. One handwritten word in clear above the cancel begins Szép…; it runs through the cancel and could not be read further.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher rows, the stamp box and the address in clear (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth in Jászárokszállás, of which several are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key. The sender's name, Feri, and the formula csókolom számtalanszor ... kedvese, Feri also stand on HCP 1216, which has the same Rákospalota cancel and the same address; that he is the same person is an inference from these parallels. This card was read with a **known, transferred key**, not by a new key recovery.

## Method

The key was taken unchanged from the finished sister cards, above all HCP 1216; earlier work on that family was done by the OpenAI GPT solver and Claude Opus 5.5. There was no earlier work on this number.

- **Transcription (2026-10-30), Claude Opus 5.5:** every row was read sign by sign on enlarged crops of the un-converted original scan and recorded as a ledger, one token per written sign (`work/ledger.txt`). This is manual work, not OCR, and the reader knew the key and the emerging text. Row 8 sem was corrected on zoom (three strokes, first read as four). The rows under the address were found and read last.
- **Decoding:** `work/decode.py` checks the hashes of the scans, decodes the ledger with the key and prints the literal rows. The normalized text (`work/normalized.txt`) is editorial and is not computed.
- **Review (2026-10-30), a separate Claude Opus 5.5 agent:** re-ran the command, made its own crops and its own row-by-row transcription in its own sign names, and decoded it with its own script against the key table of HCP 1216. It had seen the solver's text first, so this was not a blind reading. It differed in row 26 only.

To reproduce, from the repository root: `python3 -I ciphers/hcp-1307/work/decode.py`

## Key

Hungarian simple monoalphabetic substitution with invented signs. No nulls and no homophones. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section-mark S | k | F-shape | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three strokes | m | gamma | t |
| long stroke, tick at upper left | d | two strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short stroke at right | h / p | looped descender (after g: gy) | y |
| small zigzag with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | | | | |

Accents are marks over the base sign: an acute tick for á, é, í, ó, ú, and two dots or ticks for ö, ü and also ő, which this hand does not tell apart. Most acutes are not written. One sign serves both h and p, as across the family, so each of those letters rests on the word.

## Plaintext

Literal decipherment, one line per written row; h stands for the h/p sign, word division is absent as on the card, and [m] marks the hidden sign.

```text
01 szereretetédesjolan
02 kámvarvavártsorait
03 megkahtammitnagyon
04 széhenköszönökédesem
05 ojannehezenmégnemvartam
06 soraitmintmostédesem
07 ugyjajtszivemangyalom
08 hogymégkedensemkahtam
09 megsoraitmintrende
10 senmindjartarragondol
11 tamédesemhogymeghara
12 gudothogynemmentem
13 leigazanédesemcsakijen
14 korérziazemberhogy
15 menyireszeretemma
16 gátédesemmérazagondo
17 latiselkeseritetanyira
18 hogynemvoltkedvemsem
19 mihezistenmentsarra
20 nemismerekgondolnide
21 magátelvesztenémbiz
22 toshalálomlennekérem
23 magátédesemnemkiva
24 noktöbetcsaklegalabb
25 egylahotitjonvasárnahmerthatudnamijennehezen
26 váromensoraiteztakérésemteljsitenifogja
S1 csokolo[m]
S2 szamta
S3 lanszor
S4 szeretö
S5 kedvese
S6 feri
```

**Hungarian (normalized; square brackets mark what the editor supplies):**

Szeretett édes Jolánkám! Várva várt sorait megkaptam, mit nagyon szépen köszönök, édesem. Olyan nehezen még nem vártam sorait, mint most, édesem, úgy fájt szívem, angyalom, hogy még kedden sem kaptam meg sorait, mint rendesen. Mindjárt arra gondoltam, édesem, hogy megharagudott, hogy nem mentem le. Igazán, édesem, csak ilyenkor érzi az ember, hogy mennyire szeretem magát, édesem, mer[t] az a gondolat is elkeserített annyira, hogy nem volt kedvem semmihez. Isten ments, arra nem is merek gondolni, de [ha] magát elveszteném, biztos halálom lenne. Kérem magát, édesem, nem kívánok többet, csak legalább egy lapot írjon vasárnap, mert ha tudná, milyen nehezen várom én sorait. Ezt a kérésem telj[e]síteni fogja.

Under the stamp: Csókolo[m] számtalanszor. Szerető kedvese, Feri.

**English:**

My beloved sweet Jolánka! I have received your long-awaited lines, for which I thank you very much, my darling. I have never waited for your lines as anxiously as now, my darling; my heart ached so, my angel, that I had still not received your lines by Tuesday, as I usually do. I thought at once, my darling, that you were angry because I did not go down. Truly, my darling, only at such times does one feel how much I love you, my darling, for even that thought embittered me so much that I had no heart for anything. God forbid, I dare not even think of it, but [if] I were to lose you, it would surely be my death. I ask you, my darling, I wish for nothing more, only at least to write me a card on Sunday, for if you knew how anxiously I wait for your lines. This request of mine you will fulfil.

Under the stamp: I kiss you countless times. Your loving sweetheart, Feri.

**Slovak:**

Moja milovaná sladká Jolánka! Dlho očakávané riadky som dostal, za čo veľmi pekne ďakujem, drahá. Ešte nikdy som na Vaše riadky nečakal tak úzkostlivo ako teraz, drahá, tak ma bolelo srdce, anjel môj, že som Vaše riadky nedostal ani v utorok ako obyčajne. Hneď som si pomyslel, drahá, že sa hneváte, že som neprišiel dolu. Naozaj, drahá, len v takej chvíli človek cíti, ako veľmi Vás milujem, drahá, lebo aj tá myšlienka ma tak roztrpčila, že som nemal chuť do ničoho. Chráň Boh, na to sa ani neodvážim pomyslieť, ale [keby] som Vás stratil, bola by to moja istá smrť. Prosím Vás, drahá, nežiadam viac, len aby ste mi aspoň napísali lístok v nedeľu, lebo keby ste vedeli, ako ťažko čakám na Vaše riadky. Túto moju prosbu splníte.

Pod známkou: Bozkávam Vás nespočetnekrát. Váš milujúci milý, Feri.

## What remains uncertain

**Hidden sign (one).** The final m of csókolom in the stamp box: after the last o only one stroke shows at the torn edge of the stamp paper. Only the family formula and the sense say m rather than n.

**Supplied by the editor.** These are omissions by the writer, not hidden signs: [e] in telj[e]síteni (row 26; the card has teljsiteni, with clean paper between the j and the s), [t] in mer[t] (row 16; the card has mér with a clear tick, and mér "why" does not fit because the clause gives a cause and is no question), and the word [ha] (row 21; the card reads only de magát elveszteném).

**Emendations of what is written.**

- Row 7, fájt: both signs of literal jajt are clearly j, neither is the f of fogja. Úgy jajt szívem gives no verb, so fájt is an emendation. If it is wrong, only the sense of this clause is lost.
- Row 25, írjon: the sign after i is a clear t (itjon). Egy lapot ... vasárnap leaves no other word.

**Calls that rest on word sense.**

- Row 1, szeretett: literal szereretet. The last sign is a faint t close to the r shape. The e of the repeated -re- is much fainter than its neighbours and may be a wiped slip.
- Row 2, várt: the r is a dark F over an earlier sign. The writer began a v and corrected it.
- Row 19, mihez: the e looks two-barred with a smudge, so a is not excluded by shape.
- Row 21, magát: the t lies in a brown stain and could be r by shape.
- The h/p sign throughout. In row 5 nehezen its long stroke lies under a blot and only the tick is clean. In megharagudott and halálom the short stroke is unusually long, near an n, but menaragudott and nalálom are not words.
- g and k can look alike, most of all in the stamp box (csókolom, kedvese).
- Row 26, én: literal en, read as the emphatic pronoun. E[z] is not excluded by sense, but would need an omitted letter.
- The ő of szerető: the ticks could equally be ö marks.

**Writer's spellings normalized:** ojan → olyan, ijen → ilyen, mijen → milyen, keden → kedden, menyire → mennyire, anyira → annyira, elkeseritet → elkeserített, megharagudot → megharagudott, töbet → többet, mér → mer[t], teljsiteni → telj[e]síteni. Most accents are supplied, and the word division is editorial.

**Not established.** The date; the identity of Feri beyond the parallels with HCP 1216; the word in clear above the cancel.

## Why the reading is believed

The family key, taken over unchanged, gives Hungarian for every sign of the card with no sign left without a value. Repeated words decode identically (édesem ×6, hogy ×5, sorait ×4, magát ×3, mint ×2). The text is continuous love-letter prose with the formal address of the family (magát, írjon, tudná) and the writer's j for ly (ojan, as on HCP 1216). The closing formula, the signature, the cancel and the address all match HCP 1216. These checks are not independent of the sense, since the transcription was made knowing the key; the reviewer's own pass over the pixels is the main outside control.

## Summary of the review

Review 1 (a separate Claude Opus 5.5 agent) gave the verdict **REVISE**. Its independent transcription agreed with the solver's in 31 of 32 rows, and it confirmed the key, the coverage of the whole card and the contested signs. It raised four findings, all accepted after checking on the scan:

1. **Major.** The ledger of row 26 held a sign that is not on the card: an e in teljesiteni, supplied from the word. Removed; the literal now reads teljsiteni, the normalized text telj[e]síteni, and the count went from 592 to 591.
2. **Minor.** An acute over the a of várom (row 26) was missing from the ledger. Added. The stroke lies between the g and y of egy in row 25, but hogy elsewhere has no such stroke, so it belongs to neither sign. It is somewhat longer than this writer's usual acute.
3. **Minor.** "One restored sign" understated what is supplied. The hidden [m] is now separated from the editor's [e], [t] and [ha], and mér "why" is ruled out.
4. **Minor.** Two soft spots were undisclosed: the faint e of row 1 and the blotted h/p of row 5. Both are now listed.

After the fixes the reproduction command passes, and the reviewer's transcription matches the ledger in all 591 signs. None of these changes alters the sense of the letter, so no second review round was needed. The reviewer could not verify the date, the identity of Feri, the word in clear above the cancel, or the sign under the stamp fragment.
