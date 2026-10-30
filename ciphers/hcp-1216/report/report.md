# HCP 1216 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-64): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 23 main rows and the 6 rows under the stamp); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1216 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1216), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-64, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-10-12 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side carries only a printed caption, *Szerelem törvénye 6. §: Hűségemben ne kételkedj!* ("Law of love, § 6: do not doubt my faithfulness!"), and no cipher text. The whole message is on the address side, written in green ink in invented signs: 22 rows across the card, a final word running up the right edge, and six short rows under the stamp. The card was posted at **Rákospalota** (near Budapest) to Jolánka Tóth at **Jászárokszállás**; the date of the cancellation is not legible.

![Picture side (source/picture.jpg)](../source/picture.jpg)

![Address side with the cipher text, the stamp and the Rákospalota cancellation (source/address.jpg)](../source/address.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth in Jászárokszállás, several of which are deciphered in this repository (HCP 1213, 1217, 1218, 1243, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery.

## Method

The key was taken unchanged from the sister card HCP 1301 (its graphic key file is byte-for-byte the same as this card's `work/graphic-key.json`). The work then was a careful transcription of the signs.

- **Earlier passes (2026-10-12/13), OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol):** source capture, transfer of the key, and five reading passes on enlarged crops. They read most of the text but left rows 4–5, the sign after *menni* (row 18) and the sign before *og* (row 21) unresolved.
- **Completion (2026-10-30), Claude Opus 5.5:** every row was re-read on 6–14× enlargements of the address side and recorded as a sign ledger, one token per written sign (`work/ledger-opus.txt`). Rows 4, 5, 9, 18 and 21 were corrected or completed. The ledger is manual (no OCR) and not blind, since earlier readings were known.
- **Review (2026-10-30), a separate Claude Opus 5.5 agent:** re-ran the command, wrote its own decoder using HCP 1301's key file rather than the solver's key table, got identical literal output (493 letters), and checked the difficult rows and a sample of all others on its own enlargements.

The writer spells phonetically and carelessly: he drops letters, repeats syllables and writes no visible acute accents at this scan's resolution. The literal decipherment is kept as written; the normalized Hungarian below is editorial.

## Key

Hungarian simple monoalphabetic substitution with invented signs. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma / corner | t |
| long stroke + short tick | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short tick | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

One sign serves for both h and p (the "h/p near-homograph" of the family). Dots over o and u give ö and ü, a double mark gives ű. Acute accents are faint or absent and are supplied in normalization.

## Plaintext

Literal decipherment, row by row (`{m|n}` = sign read as m, n not excluded; `{|}` = an isolated stroke with no letter value; h stands for the h/p sign):

```text
01 szeretettedesjolankam          13 hogyjolnezkimerbi
02 nemtudommirevelnihogy          14 zonyregennemlattam
03 nemirmarszerdaihostais         15 amultkorhogyerement
04 elmentesme{m|n}ostisneküznöm   16 temojannezemreesett
05 kelsoraitdehighiggyjeel        17 vamosgyörkmelletel
06 edesemugyvaromminta            18 men{|}ennideleküzdottem
07 zsidokamessiastedesegye        19 fajdalmammertbiz
08 tlenremenyemhogyvan            20 tatottazatudathogy
09 egessegesealligvarom           21 nemsokafelfogjonni
10 hogyviszontlathas              22 esakorviszontlathatomistenveleaviszont
11 sammulthetenbeszeltem          23 latasra  (up the right edge)
12 asandorralmondta               under the stamp: csokolom / szamta / lanszor / sirighű / kedvese / feri
```

Normalized Hungarian (word division, accents, spelling and punctuation are editorial; letters in square brackets are not on the card):

**Szeretett édes Jolánkám! Nem tudom, mire vélni, hogy nem ír. Már szerdai posta is elment, és mé[g] most is nélkülöznöm kell sorait. De higgye el, édesem, úgy várom, mint a zsidók a Messiást. Édes egyetlen reményem, hogy van, egészséges-e? Alig várom, hogy viszontláthassam. Múlt héten beszéltem a Sándorral, mondta, hogy jól néz ki, mer[t] bizony régen nem láttam. A múltkor, hogy erre mentem, olyan nehezemre esett Vámosgyörk mellett elmenni, de leküzdöttem fájdalmam, mert biztatott az a tudat, hogy nemsoká fel fog jönni, és akkor viszontláthatom. Isten vele, a viszontlátásra.**

**Under the stamp: Csókolom számtalanszor. Sírig hű kedvese, Feri.**

English translation: **My beloved sweet Jolánka! I do not know what to make of your not writing. The Wednesday post has already gone, and even now I must do without your lines. But believe me, my darling, I wait for them as the Jews await the Messiah. My sweet, only hope, how are you, are you well? I can hardly wait to see you again. Last week I spoke with Sándor; he said you look well, for indeed I have not seen you for a long time. The last time I came this way it was so hard for me to pass by Vámosgyörk, but I overcame my pain, because I was encouraged by the knowledge that you will soon come up [to town], and then I can see you again. Farewell, until we meet again.**

**Under the stamp: I kiss you countless times. Your sweetheart, faithful unto the grave, Feri.**

Slovak translation: **Moja milovaná, sladká Jolánka! Neviem, čo si mám myslieť o tom, že nepíšete. Už aj stredajšia pošta odišla a ešte stále sa musím zaobísť bez Vašich riadkov. Ale verte mi, drahá, čakám na ne, ako Židia čakajú na Mesiáša. Moja sladká jediná nádej, ako sa máte, ste zdravá? Sotva sa dočkám, kedy Vás znova uvidím. Minulý týždeň som hovoril so Šándorom, povedal, že vyzeráte dobre, lebo veru dávno som Vás nevidel. Keď som tadiaľto minule išiel, tak ťažko mi padlo prejsť popri Vámosgyörku, ale premohol som svoju bolesť, lebo ma povzbudzovalo vedomie, že čoskoro prídete hore a potom Vás znova uvidím. S Bohom, dovidenia.**

**Pod známkou: Bozkávam Vás nespočetnekrát. Váš do hrobu verný milý, Feri.**

Notes on the reading:

- The letter uses the formal address (*ír, higgye el, van, fel fog jönni*), usual between courting couples of the period. *Mint a zsidók a Messiást* ("as the Jews await the Messiah") is a common idiom of the time.
- **Vámosgyörk** is the railway junction where the branch line to Jászárokszállás and Jászberény leaves the Budapest–Hatvan–Miskolc main line. Travelling along the main line past Vámosgyörk without turning off to her is exactly what the writer describes. *Fel fog jönni* ("will come up") fits a writer in or near Budapest (Rákospalota cancellation).
- **Sándor** also appears on the family card HCP 1217. The sender signs as **Feri** (Ferenc); he is not identified with any sender on other cards.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1216/work/decode_opus.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of both scans, decodes the manual sign ledger `work/ledger-opus.txt` with the family key, prints the 23 main rows and 6 stamp rows shown above, and prints the normalized text `work/normalized-opus.txt`. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

None of these changes the sense of the letter.

- **Contextual sign readings.** At this resolution each sign is only 8–12 pixels tall. Three signs are read from context, not from a clean match:
  - row 5: the d of *de* has its tick on the right, like the h/p sign;
  - row 21: the f of *fog* is a tilted cross, between the f and u shapes;
  - row 18: the single slash before *e leküzdöttem* is read as a reduced d.
  
  In each case the alternative gives no Hungarian word.
- **Row 4.** *me{m|n} ostis* is normalized *még most is* ("even now"). The g is not on the card. *neküznöm* (all signs clear) is normalized *nélkülöznöm* ("I must do without"), a misspelled word with *l…lö* omitted. The alternative *ne küzdöm* is excluded because the sign after z is n, not d.
- **Writer's repetitions.** Row 5 has *hig higgyje* (a false start, then the word). Row 18 has *men | enni*, a repeated *-en-* with a stray stroke between; it is normalized *elmenni*.
- **Other normalized spellings:**
  - *kel* → kell, *egessegese* → egészséges-e (z omitted), *higgyje* → higgye;
  - *ojan* → olyan, *nezemre* → nehezemre, *mer* → mer[t], *erement | temojan* → erre mentem, olyan;
  - *mellet* → mellett, *akor* → akkor, *allig* → alig, *hostais* → posta is (h/p sign).
- **Accents.** Acute accents are not visible and all are supplied. Diaeresis dots are seen on some signs only (for example a single dot on the ö of *neküznöm*, none on *jönni*); the rest are supplied.
- **The right edge.** *látásra* up the right edge is faint and partly under the portal watermark; it is consistent with the signs but was not confirmed sign by sign in review.
- **Date and sender.** The card has no legible date, and the cancellation date cannot be read. The identity of Feri is not established.
- **Prior work.** The key was transferred from the family, not recovered blind from this card. No published reading of this card exists as far as was checked: the portal status (Not solved) and the AI Decipherment Register (no record, checked 2026-10-29).

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. It confirmed:

- the command's output, and an identical output from its own decoder built on HCP 1301's key file;
- the restored passages in rows 4, 5, 9, 18 and 21, and a sample of all other rows, against its own enlargements of the scan;
- the language and the geography (Rákospalota, Jászárokszállás, Vámosgyörk);
- that no published solution was used.

Its five findings were all minor disclosure points:

- **Row 21, f of *fog*.** Now described as a tilted cross read from context.
- **Row 5, d of *de*.** Now described as contextual (its tick is on the right, as on h/p).
- **Row 18.** The normalization *elmenni* is now said to delete a repeated *-en-* as well as the stray stroke.
- **Normalization list.** The missing changes (*kell*, *egészséges-e*, *higgye*, *erre mentem, olyan*) are now listed.
- **Diacritics.** The reviewer thought a diaeresis was marked on *jönni*; the ledger in fact marks none there, so no change was needed. The single dot on the ö of *neküznöm* is now named in the ledger header.

No letter of the literal decipherment and no word of the normalized text or the translation changed as a result of the review.

## Credits

- **OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol), 2026-10-12/13:** source capture, transfer of the family key and reading passes 1–5.
- **Claude Opus 5.5, 2026-10-30:** completion of the transcription (sign ledger), decipherment of the remaining passages, response to review and this report.
- **Claude Opus 5.5, separate reviewer agent:** independent review.

## Sources

- HC Portal record 1216, General, Description and Attachments tabs, captured 2026-10-12: https://crypto.hcportal.eu/dashboard/cryptograms/1216 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3708/conversions/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-64_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/3709/conversions/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-64_adr-large.jpg (source/address.jpg).
- Family key: ciphers/hcp-1301/work/graphic-key.json (Jolánka family, HCP 1213, 1217, 1218, 1243, 1301).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
