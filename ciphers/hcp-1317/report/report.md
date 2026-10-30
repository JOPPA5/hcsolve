# HCP 1317 (cpc_1913--_HU__HU_Jasz Arokszalas_jolanka-110): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: all cipher text on the card is read (33 written rows, 491 signs: 486 seen, 5 restored under the stamp tear). One word of row 10 stays unresolved. Independent review 1 verdict REVISE; all nine findings addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1317 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1317), portal name cpc_1913--_HU__HU_Jasz Arokszalas_jolanka-110, part of Tobias Schrödel's collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language Unknown, location Europe, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side carries only print: *Szerelem törvénye. 5. §.* ("Law of love, § 5") and *Csókolni nem bűn-engem!* (roughly "Kissing is no sin: me!"). It has no cipher text.

The message is on the address side, in green ink, in invented signs: 24 rows on the left half, one long row (25) along the whole bottom edge, the signature *Feri* above its right end (row 26), and a further seven short rows (S1 to S7) in the place where the stamp was stuck. The stamp has been removed, leaving tears that hide a few signs. The address is in plain cursive: *Szépreményű / Tóth Jolánka / úrleánynak / Jászárokszállás* (first and last words read at reduced confidence, the last partly under the portal stamp). The cancellation shows a year ending *913*. A clear B and a following stroke at its top and an F at its bottom are visible, but no place name is claimed.

The card belongs to the family of Hungarian cipher postcards from Feri to Jolánka Tóth, several of which are read in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). This card was read with a **known key transferred from that family**; this is not a new key recovery.

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, print only (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is **manual**, not OCR. The solver enlarged crops of the un-converted original scan and recorded one token per written sign in `work/ledger.txt`. A small script applies the key to the ledger. Sign groups that are close to each other (h/p, u/z, t/f, a/e) were checked by shape and, where the shape alone does not decide, by word sense; those calls are listed under Uncertainties. An image filter was tried under the stamp but gave nothing better than plain enlargement.

## Key

Simple monoalphabetic substitution with invented graphic signs. It is the family key of HCP 1216, unchanged. Words are mostly spaced. Accents are written as ticks and dots over the base sign.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S-shaped) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma | t |
| short + long stroke, tick on the left | d | two short strokes | n | heavy plain cross | u, with dots ü |
| three bars | e | cursive loop | o, with dots ö/ő | chevron | v |
| upright cross | f | long stroke + tick on the right | h / p (near-homograph) | low descender loop | y |
| hooked sign with descender | g | dotted crossed curve | i | thin crossed diagonal with tail | z |
| inverted T | j | | | | |

The family's gy is written on this card as two signs, g + y.

## Plaintext

Literal decipherment (h stands for the h/p sign; square brackets mark restorations):

```text
01 szeretetedesegyetlenre        14 miteloreisköszö
02 menyemkivanomhogya            15 nökedesemmostgyak
03 legjobbkedvebentalalja        16 ranjarokujvarba
04 soraimedesesjolankama         17 majnemmindigot
05 miafenykehetileti             18 vagyokszetnekmar
06 csakküldjeelakarsikerül       19 hatvanbaismenni
07 akarnemmarcsakazert           20 marazerzesijjol
08 ishogyazilonkaisraj           21 esnehogyközel
09 tavanmertirnikene             22 volnekmagahoz
10 kiheaztvaromhogy              23 edesembarakoris
11 afenykehetmegkahjam           24 elegmeszevolnek
12 tehatkeremedesem              26 feri
13 kuldjeminelelöbb
25 ezzezaromsoraimmaradoksirighükedvesse

Under the stamp: is[t]enve | leedes[e]m | csokol | szamta | lanszor | [i]madoja | [f][e]ri
```

Normalized Hungarian (accents, capitals, punctuation and word division are editorial):

**Szeretett édes egyetlen reményem! Kívánom, hogy a legjobb kedvében találja soraim, édes Jolánkám. Ami a fényképet illeti, csak küldje el, akár sikerül, akár nem, már csak azért is, hogy az Ilonka is rajta van. Mert írni kéne {kihe|kipe}, azt várom, hogy a fényképet megkapjam. Tehát kérem, édesem, küldje minél előbb, mit előre is köszönök. Édesem, most gyakran járok Újvárba, majdnem mindig ott vagyok. Sze[re]tnék már Hatvanba is menni, már az érzés i[s] jól esne, hogy közel volnék magához, édesem, bár akkor is elég messze volnék. Ezze[l] zárom soraim, maradok sírig hű kedvese Feri.**

**Under the stamp: Isten vele, édesem! Csókol számtalanszor imádója Feri.**

English translation: **My beloved sweet only hope! I wish that these lines of mine find you in the best of spirits, sweet Jolánka. As for the photograph, just send it, whether it turned out well or not, if only because Ilonka is in it too. For I ought to write [one unresolved word], I am waiting to get the photograph. So I ask you, my darling, send it as soon as you can, for which I thank you in advance. My darling, I go to Újvár often now, I am there nearly all the time. I would like to go to Hatvan now too; the feeling alone would do me good, that I would be near you, my darling, although even then I would be quite far away. With this I close my lines, and remain, faithful unto the grave, your sweetheart Feri.**

**Under the stamp: Farewell, my darling! Your adorer Feri kisses you countless times.**

Slovak translation: **Moja milovaná, sladká, jediná nádej! Želám si, aby Vás moje riadky našli v najlepšej nálade, sladká Jolánka. Čo sa týka fotografie, len ju pošlite, či sa vydarila, alebo nie, už len preto, že je na nej aj Ilonka. Lebo by som mal napísať [jedno nerozlúštené slovo], čakám, že fotografiu dostanem. Prosím Vás teda, drahá, pošlite ju čím skôr, za čo Vám vopred ďakujem. Drahá, teraz často chodievam do Újváru, som tam takmer stále. Chcel by som už ísť aj do Hatvanu, už len ten pocit by mi dobre padol, že by som bol blízko Vás, drahá, hoci aj tak by som bol dosť ďaleko. Týmto končím svoje riadky a zostávam až do hrobu Váš verný milý Feri.**

**Pod známkou: S Bohom, drahá! Bozkáva Vás nespočetnekrát Váš ctiteľ Feri.**

The polite third-person address (*találja, küldje, magához*) is rendered with "you" in English and with Vy-forms in Slovak.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1317/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of both source scans and both un-converted originals, decodes the 491 tokens of `work/ledger.txt` with the key, prints the literal rows, and prints `work/normalized.txt`. It does not read the images: the transcription is manual and was checked by the reviewer against the scan, row by row.

## Uncertainties

- **Row 10, `kihe` / `kipe`: unresolved.** After *írni kéne* come k, i, the h/p sign, e, then a gap and *azt*. No fitting word was found, so it stays literal and untranslated, and the link of that sentence is uncertain. One unadopted hypothesis is *írni kéne [ne]ki, de azt várom* ("I ought to write to her, but I am waiting…"). It suits the sense but costs two writer's errors (*ne* dropped at the row break, the tick of d on the wrong side), and the sign itself is h/p, not d.
- **Restorations under the stamp (5 signs).** The t of *Isten* (S1), the e before m in *édesem* (S2), the i of *imádója* (S6, only its dot shows), and f and e of *Feri* (S7, two bar ends of the e show). In each case one letter gives the word.
- **Faint signs read with word sense under the stamp.** The first sign of S1; the third sign of S2 (only two short bars show, so literally a, read as e of *vele édesem*); the z of S4; *la* of S5; the last sign of S5 (top bar and stem show, no mid-bar, so literally t, read as r of *számtalanszor*); the last sign of S7 (a cross taken as i). *Csókol* is third person: clean paper follows the l.
- **h/p calls resting on word sense.** *fényképet* (rows 5, 11) and *megkapjam* (row 11) take p; *hogy, tehát, Hatvanba, magához, hű* take h.
- **u/z.** The heavy and thin crosses are normally distinct; the calls were also confirmed by sense. Row 13 *küldje* shows no dots; the ü is supplied.
- **Row 12 `t` of *tehát*:** a tall gamma whose stem crosses the bar, close to a cross; read t from word sense.
- **Row 26 `r` of *Feri*:** an F with a curled stem; read r from word sense and the family signature.
- **Writer's slips, normalized editorially.** Row 4 *edes-es*: the s is an over-inked blot and the writer restarted. Row 18 *szetnek* → *sze[re]tnék*. Row 20 *ijjol* → *i[s] jól*, taken as a slip (s dropped, j doubled), with no phonetic explanation claimed. Row 25 *ezze* → *ezze[l]*, and *kedvesse* → *kedvese*. Also *szeretet edes* → szeretett édes, *ileti* → illeti, *majnem* → majdnem, *ot* → ott, *meszevolnek* → messze volnék, *barakoris* → bár akkor is. Accents are supplied where ticks are not clear; the ledger does not transcribe them.
- **Small writing accidents.** A short fourth stroke after the m at the end of row 12 is not in the ledger and may be a comma-like mark. The k of row 11 *megkapjam* is a heavy blot and the o of row 24 *volnék* is overwritten; both are readable.
- **Row 25 start.** The first e and the second z are cut by the corner or smudged, but their outlines are visible.
- **People and places.** *Újvár* is not identified (several Hungarian towns carry the name). *Hatvan* is near the addressee's Jászárokszállás, which fits *közel*. *Ilonka* is unidentified, and Feri is known only as the family's sender.
- **Date.** The card has no written date; the cancellation year ending *913* and the portal file name point to 1913.
- **Limits of the check.** Hungarian usage was judged without a dictionary or corpus. Solver and reviewer are the same model, and the reviewer's reading was not blind.
- No prior publication was searched beyond the portal status (Not solved, nothing attached) and the AI Decipherment Register (no record, 2026-10-30).

## Why the reading is believed

- The HCP 1216 key, unchanged, turns all 491 ledger signs into Hungarian with no sign left without a value; only one word has no meaning found.
- Repeated words decode identically in separate places: *hogy* ×4, *fényképet* ×2, *édesem* ×4, *soraim* ×2, *küldje* ×2, *már* ×3, *volnék* ×2.
- The prose is coherent, and its formulas (*legjobb kedvében találja soraim*, *mit előre is köszönök*, *sírig hű kedvese*, *Isten vele*, *imádója*) match the family. The sense runs across row breaks (*re|ményem, raj|ta, köszö|nök, gyak|ran*).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, read all 33 rows sign by sign from its own crops, counted bars on every a/e sign, and decoded its reading with its own key script. Of 33 rows, 29 were identical. It confirmed the key, the restorations, *csókol* in the third person and the repetition counts. What changed because of the review:

- **Row 16, last sign (major).** It has two bars, so it is a, not e. The solver had misread it; the card has *Újvárba* correctly spelled, and a claimed misspelling was withdrawn.
- **Comma in rows 19-20.** Now *…menni, már az érzés is jól esne*; the second *már* opens the next clause. The translations already meant this.
- **Disclosures added.** The S2 third sign and S5 last sign as word-sense calls; the row 12 fourth stroke and two blots; the visible letters of the cancellation; 486 signs seen and 5 restored rather than a flat 491.
- **Row 10.** The reviewer's unadopted hypothesis is recorded with its costs. The word stays unresolved.
- **`ijjol`.** The unsupported phonetic explanation was replaced by "writing slip".

Apart from that one literal letter and one comma, no word of the reading changed. The whole of the work on this number (transcription, decipherment, report) was done by Claude Opus 5.5; the key comes from the finished family cards, whose earlier work is credited in their own directories.

## Sources

- HC Portal record 1317, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1317 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4011/conversions/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-110_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4011/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-110_pic.jpg.
- Address side: https://api.hcportal.eu/media/4012/conversions/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-110_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4012/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-110_adr.jpg.
- Family key: ciphers/hcp-1216 and sister cards in this repository.
- HistoCrypt proceedings, as cited by the portal: https://ecp.ep.liu.se/index.php/histocrypt
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
