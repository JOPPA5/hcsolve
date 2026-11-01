# HCP 1271 (cpc_1912-03-16_HU__HU_Jasz Arokszalas_jolanka-10): a new workshop and a new address, to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: whole message read (all 17 cipher rows, 263 signs); independent review 1 verdict ACCEPT, no change to the Hungarian text.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1271 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1271), portal name cpc_1912-03-16_HU__HU_Jasz Arokszalas_jolanka-10, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The date 16 March 1912 comes from the file name; the left cancellation shows compatible fragments (12, MA, 16).

The picture side is a tinted photograph of a couple, turned sideways on the scan, with the printed title Akiknek a szívük fáj... ("Those whose hearts ache...") and a printed verse, series number 1376/5. It has no handwriting.

The message is on the address side, in red ink: 17 rows of invented signs fill the left half. A plain line, Gyöngyös Püspöki, stands large between rows 9 and 10 and belongs to the sentence. The stamp box holds a plain greeting. The address reads Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás ("To the promising young lady Jolánka Tóth, Jászárokszállás"); its last word runs under the collector's stamp and is read partly from the family's other addresses.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: cipher rows at the left, Gyöngyös Püspöki in plain between rows 9 and 10, plain greeting in the stamp box (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards to Jolánka Tóth, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301, 1303, 1310). This card was read with a **known, transferred key**; it is not a new key recovery.

## Method

No earlier work exists on this number. The key was taken from the finished family cards, chiefly HCP 1216. That key was first transferred by the OpenAI GPT solver and completed by Claude Opus 5.5.

- **Reading (2026-11-01), Claude Opus 5.5:** every row was read on enlarged crops of the un-converted scan and recorded as a sign ledger, one token per written sign (`work/ledger.txt`). The reading is manual, not OCR, and not blind: it was made for sense. A small script checks the scan hashes and decodes the ledger.
- **Review (2026-11-01), a separate Claude Opus 5.5 agent:** re-ran the command, typed its own sign-by-sign transcription from its own crops, decoded it with the key from the HCP 1216 legend, and tried to refute the reading on the pixels. That transcription was made after seeing the solver's text, so it is not blind either.

The whole key is unchanged and every sign on the card maps to a key value. The reproduction command, from the repository root, is `python3 -I ciphers/hcp-1271/work/decode.py`.

## Key

Hungarian, simple monoalphabetic substitution with invented graphic signs. Word spaces are partly kept. The sign names are conventional labels for handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S, 8 forms) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl (€-like) | c | three short strokes | m | gamma | t |
| opposed bowls | cs | two short strokes | n | plain cross x | u |
| short stroke left + tall right | d | cursive loop with hooked arm | o | chevron (1-shaped) | v |
| three bars | e | tall stroke + short right | h / p | low descender | y |
| open loop with descender | g | loop with straight crossbar, dotted | i | crossed flagged diagonal | z |
| loop + descender joined | gy | inverted T | j | | |

The signs for h and p are near-homographs. Dots over x give ü. `cz` is the old spelling for c (czím). No f occurs on this card.

## Plaintext

Literal decipherment, row by row. `[x]` is a blotted sign restored by word sense, and `h` is the h/p sign.

```text
01 dragacsilagomki      10 ideczimezesorait
02 vanomhogyalegjobb    11 kedvesjolankam
03 kedvebentalaljaso    12 [j][o]mulatastkiva
04 raimedesemtudatom    13 [n]okholnahragon
05 hogyenmarmamunka     14 [d]oljonn[e]haram
06 bademostmasmühely    15 kiszintengon[d]ol
07 betehataczimem       16 onristenveaviszont
08 ismegvaltozik        17 latasracsokolomezersze
09 [c]zimemiseshedig
```

### Hungarian (normalized, editorial)

Drága csil[l]agom! Kívánom, hogy a legjobb kedvében találja soraim. Édesem, tudatom, hogy én már ma munkába [megyek?], de most más műhelybe, tehát a czímem is megváltozik. Czímem is, és pedig: **Gyöngyös Püspöki** [plain]. Ide czímez[z]e sorait. Kedves Jolánkám, jó mulatást kívánok holnapra. Gondoljon néha rám, ki szintén gondol önr[e]. Isten ve[le], a viszontlátásra. Csókolom ezersze[r].

Stamp box, plain: Üdvözlöm a távolból, hű kedvese.

### English

Dear star of mine! I hope my lines find you in the best of spirits. My darling, I let you know that I am already [going] to work today, but now to another workshop, so my address changes too. My address too, namely: Gyöngyöspüspöki. Address your lines here. Dear Jolánka, I wish you a good time tomorrow. Think of me sometimes, who also thinks of you. Farewell, until we meet again. I kiss you a thousand times.

Stamp box: I greet you from afar. Your faithful sweetheart.

### Slovak

Drahá moja hviezda! Želám si, aby Vás moje riadky našli v najlepšej nálade. Drahá, oznamujem Vám, že už dnes [idem] do práce, ale teraz do inej dielne, takže sa mení aj moja adresa. Aj moja adresa, a to: Gyöngyöspüspöki. Sem adresujte svoje riadky. Milá Jolánka, želám Vám na zajtra dobrú zábavu. Myslite niekedy na mňa, ktorý tiež myslí na Vás. S Bohom, dovidenia. Bozkávam Vás tisíckrát.

Pole na známku: Pozdravujem Vás z diaľky. Váš verný milý.

## Why the reading is believed

- The family key, unchanged, turns all 17 rows into Hungarian with no unexplained sign.
- It gives long unforced phrases and family formulas: kívánom, hogy a legjobb kedvében találja soraim also occurs on HCP 1303, and mulatást kívánok on HCP 1310.
- The cipher fits the plain text around it: a czímem is megváltozik announces the new address, the plain place name follows, and ide czímez[z]e sorait ("address your lines here") comes straight after it.
- Repeated words decode identically: czím- three times, édes-/kedves-, gon- twice.

## What remains uncertain

- **Blots, restored by word sense:** row 9 c of czímem (solid blot) and row 13 n of kívánok. Row 14 d, row 14 e and row 15 d are heavily inked, but their shapes survive. The k in row 1 is smudged but legible.
- **Row 12 jó:** the j is blotted. The o is wiped in a pink smear with a mark above it; its right arm is damaged, so it could be i, but ji gives no word. The ó rests on word sense.
- **Row 9 word division:** the signs after the blot are clean. Czímem is, és pedig ("my address too, namely") is an awkward repeat. An accent stroke above the e favours és over the alternative czíme Mises, pedig..., with Mises as a name, but that alternative is not excluded. Pedig rests on word sense for the p.
- **h/p by word sense:** p in holnapra and pedig; h in hogy, műhely, tehát, néha.
- **Rows 5–6 munkába:** no verb is written, and megyek ("I am going") is supplied. Műhelybe may stand for műhelybe[n], so "am going" against "am at" is not settled. All the written words are read.
- **Row 16 önr[e]:** no ö dots are visible, though a descender from row 15 crosses the loop and may hide them. The e is not on the card.
- **Row 17:** the a's of látásra are blurred bars. The o of csókolom is overwritten into a dense mass, and no accent is visible on it.
- **Writer's omissions, normalized:** csilagom, czímeze, ve for vele, ezersze.
- **Sender and date:** the card is signed only hű kedvese. The hand, formulas and Gyöngyös connection fit the "Feri" of HCP 1303 and 1310, but no identification is claimed. 16 March 1912 was a Saturday, which fits holnapra for a Sunday outing, but that is only suggestive. The date is not independently confirmed beyond the file name and the postmark fragments.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the command, compared the output with the stated text, went through all 17 rows on its own enlargements, judged each restoration on the pixels, and checked the key against the HCP 1216 legend and the language against the family cards. It could not refute the reading. Its five findings were all minor, and all were accepted:

- **Row 3 sign 7.** It has three bars, so it is e, not a. The ledger and literal now give kedveben-; the normalized text already had this.
- **Row 17 "stray" sign.** The supposed separate s is the hooked arm of the overwritten o. The sign count falls from 264 to 263.
- **Row 1 k.** It is legible, so the restoration brackets were dropped, and the smudge is now disclosed.
- **Row 9 accent.** The stroke above the e is now noted as evidence for és.
- **Supplied verb.** The English and Slovak now bracket it.

The normalized Hungarian did not change.

## Sources

- HC Portal record 1271, all three tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1271 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3873/conversions/cpc_1912-03-16_HU__HU_Jasz-Arokszalas_jolanka-10_pic-large.jpg, with the original in work/hires/.
- Address side: https://api.hcportal.eu/media/3874/conversions/cpc_1912-03-16_HU__HU_Jasz-Arokszalas_jolanka-10_adr-large.jpg, with the original in work/hires/.
- Family key: finished Jolánka cards in this repository, chiefly ciphers/hcp-1216.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-01: no record of this card.
