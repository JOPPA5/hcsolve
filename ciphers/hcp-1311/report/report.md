# HCP 1311 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-81): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: the 28 main rows are read in full; the closing under the torn stamp is only partly read, and its end rests on the family formula. Independent review 1 verdict REVISE, findings addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1311 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1311), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-81, part of Tobias Schrödel's collection of cryptographic postcards (see the HistoCrypt proceedings, https://ecp.ep.liu.se/index.php/histocrypt). When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution was found.

The picture side has only a printed verse (*Ezüsttükrös kávéházban*) and the publisher's number. The message is on the address side, in green ink in invented signs: 28 rows across the card and seven short rows in the place of the stamp, which has since been torn away. A black triangular postage-due mark and tear patches lie over that block. The plain address reads *Tóth Jolánka úrleánynak, Jász-Árokszállás*. The railway box reads *…LOTA-ÚJPEST P.U.* (Rákospalota-Újpest). The cancellation date is not legible, so the card is undated. A green cursive word above the cancellation could not be read; it does not appear to be cipher text.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards from Feri to Jolánka Tóth, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). They share one key, so this card was read with a **known, transferred key**, not by a new key recovery.

## Method

Claude Opus 5.5 did all the work on this number; there was no earlier work on it. The key was taken from the family legend in HCP 1216. Every row was read by eye on 2.4–10× crops of the un-converted address scan and recorded as a ledger with one token per written sign, 512 in all. No OCR was used. A green-ink mask and single-channel views helped under the postage-due mark. The S-hook form of k was proved by *Árok|szállás* in rows 19–20.

A separate Claude Opus 5.5 agent then cut the card into its own strips and transcribed all rows in its own glyph names with its own key. It agreed on every sign of rows 1–26 but one. That reading was not blind, since the reviewer had read the solution first.

## Key

Simple monoalphabetic substitution with invented signs. Word division is not written, and accents appear only occasionally.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark or S-hook | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three strokes | m | corner, Γ | t |
| tall stroke, tick at left | d | two strokes | n | plain cross x | u |
| three bars | e | loop without dot | o | chevron | v |
| tilted or upright cross | f | loop with two dots | ö | long tail, hooked head | y |
| ς | g | loop with dot | i | crossed diagonal | z |
| inverted T | j | tall stroke, tick at right | h / p | opposed bowls | cs |

## Plaintext

Literal decipherment; {x?} marks a sense-based sign and · an unresolved one:

```text
01 szeretetedesjolánkamki        15 hestreamimarcsak2½
02 vanomhogyalegjobbegesseg      16 honahlasanmajdel
03 bentalaljasoraimkedvesjo      17 mulikaziskedvesem
04 lankamhogymulatotta           18 irjo{n?}{h?}ogymulatot
05 mulatsagbaremelemjol          19 azthiszemutolsoarok
06 bareniselmehete{m?}vol        20 szalasomulatsagba
07 naigazansajnalomhogy          21 voltmostenmost
08 nemkadtammegegynah            22 mastirokmivelnem
09 halelöbbmintirtam             23 tudokmitirirjon
10 isletvolnaanyiszabad          24 sokathogysokat
11 sagomhogyelmehetem            25 tudakval{e?}szolni
12 volnaheezenmar                26 {i?}stenveledesem
13 nemlehetsegitenimajd          27 yma{d?}{o?}{j?}a
14 mulatunkhafeljön              28 {f?}er

Under the stamp:
S1 udvö{z?}{l?}i··   S2 szam   S3 talan   S4 szor
S5 szer{e?}          S6 ··{k?}ed   S7 {v?}ese{f?}{e?}ri
```

**Hungarian (normalized).** Szeretett édes Jolánkám! Kívánom, hogy a legjobb egészségben találja soraim, kedves Jolánkám. Hogy mulatott a mulatságba[n]? Remélem, jól. Bár én is elmehet[t]em volna! Igazán sajnálom, hogy nem kaptam meg egy nappal előbb, mint írtam, [akkor] is lett volna annyi szabadságom, hogy elmehet[t]em volna, de ezen már nem lehet segíteni. Majd mulatunk, ha feljön Pestre, ami már csak 2½ hónap, las[s]an majd elmúlik az is, kedvesem. Írjon, hogy mulatott; azt hiszem, utolsó Árokszálláso[n] mulatságba[n] volt. Most én most mást írok, mivel nem tudok mit ír[ni]. Írjon sokat, hogy sokat tud[j]ak válaszolni. Isten vele, édesem! Imádója Fer[i].

Under the stamp (tentative): Üdvözli [..] számtalanszor szere[tő?] [k?]ed[v?]ese [F?]eri.

**English.** Beloved sweet Jolánka! I wish that my lines find you in the best of health, dear Jolánka. How did you enjoy yourself at the dance? Well, I hope. If only I could have gone too! I am truly sorry that I did not get it one day before I wrote; I would then have had enough leave to go, but nothing can be done about that now. We will have our fun when you come up to Pest, which is only 2½ months away; that too will slowly pass, my dear. Write how you enjoyed yourself; I think that was your last dance at Árokszállás. Now I am writing about something else, since I do not know what to write. Write a lot, so that I can answer a lot. God be with you, my sweet! Your adorer, Feri.

Under the stamp (tentative): [Your] loving sweetheart Feri greets [you] countless times.

**Slovak.** Milovaná sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšom zdraví, drahá Jolánka. Ako ste sa zabavili na zábave? Dúfam, že dobre. Keby som tam bol mohol ísť aj ja! Naozaj ľutujem, že som to nedostal o deň skôr, než som písal; potom by som bol mal dosť voľna, aby som mohol ísť, ale s tým sa už nedá nič robiť. Zabavíme sa, keď prídete hore do Pešti, čo už je len 2½ mesiaca; pomaly aj to prejde, drahá moja. Napíšte, ako ste sa zabavili; myslím, že to bola Vaša posledná zábava v Árokszállási. Teraz píšem o inom, lebo neviem, čo písať. Píšte veľa, aby som mohol veľa odpovedať. Zbohom, sladká moja! Váš ctiteľ, Feri.

Pod známkou (neisté): Nespočetnekrát [Vás] pozdravuje Váš milujúci milý Feri.

## Uncertainties

![The block under the torn stamp, enlarged (work/crops2/S_all.png)](../work/crops2/S_all.png)

- **Closing under the stamp.** This is the main residue: 4 unresolved tokens and 7 uncertain ones, and nothing here affects the message.
  - Clear are *üdvö…*, *számtalanszor*, *szer-*, *…ed*, *ese*, and *ri*.
  - The end is read *szerető kedvese Feri* because that closing occurs on HCP 1307 and the visible signs fit it. The t is not visible, the head and two strokes in S6 are unresolved, and k, v and f are tentative.
  - *édese Feri* would suit S7 as well if the left fragment is not v.
  - The two marks at the right edge beside S2 are unread and may not belong to S1.
- **Sense calls in the main text.** Row 8 *kaptam* has the d form (literal *kadtam*). Row 12 *de* has the h/p form (literal *he*). Row 22 *írok* has an undotted loop, though the shape favours i. Row 25 *válaszolni* has an e-like blotted sign. Row 26 *Isten* begins with a compressed sign at the corner. Row 28 *Fer* begins with a tilted cross. Row 18 *irjon hogy* has a blotted patch with one stroke unaccounted for. Row 6 *elmehetem* has an overwritten m. The middle of row 27 *imádója* lies under a smudge. The h/p choices in *Pestre*, *hónap*, *nappal* rest on sense.
- **Writer's habits normalized.** Doubles are written single (*anyi*, *lasan*, *letvolna*); a shared letter stands in *szeretetedes* and *veledesem*; *tudak* is *tud[j]ak*; *mit ir irjon* is read *mit ír[ni]. Írjon*. "[akkor]" is supplied in row 10.
- **Date.** Nothing on the card fixes it.

## Review and what changed

Review 1 (a separate Claude Opus 5.5 agent) ran the command, checked the source hashes, transcribed independently and returned **REVISE**. It confirmed the 26 message rows and the key, and found the closing printed too firmly. Changes made:

- The tentative closing *szeret, imád, [éd]esem* was withdrawn. The sign before d has three bars, so *imád* fails. The review's suggestion of a signature *…eri* was tested, and the end of the block now reads *…ese [f]eri*.
- The row 25 literal became e, and the first signs of rows 26 and 28 and the row 18 group were marked as sense calls.
- Counts (*hogy* ×6, *mulat-* ×5) and the note on *nap|pal* (both p written) were corrected. A sign table was added.

The reading of the 28 main rows did not change.
