# HCP1235 — to Tóth Jolánka, Jászárokszállás

**Status: PARTIAL (2026-11-02, Claude Opus 5.5). One clause in rows 12-13 is unread. No DONE marker, no register entry.** No earlier work on this number; no published solution found; portal status Not solved.

## Cipher and key

Hungarian simple monoalphabetic substitution with invented signs: the Jolánka family, key as in `ciphers/hcp-1216/SOLUTION.md`, transferred unchanged. This card adds sign forms: the k appears as S and as 8; two bars with a low dot or high tick are á; sz is written as right bowl + crossed z.

## Reproduction

```sh
python3 -I ciphers/hcp-1235/work/decode.py
```

Checks the four image hashes and decodes the manual sign ledger `work/ledger.txt` (read from pixels on `work/crops/`).

## Literal decipherment

```
01 kedvesjolankam            10 soraimistenvele
02 kivanomhogya              11 vasarnahhajoidlesz
03 legjobbkedveben           12 lemegyeke{?}elege
04 talaljasoraim             13 sztemkieledot
05 kimentetanyá              14 istenemhalgasdmeg
06 radolgozni                15 eszerenyimámat
07 miojságaroksza            16 addnekemörökre
08 lasbanitnincssemi         17 szeretettbabamat
09 ujságezebezarom           18 tiszteleakedvesmamajat
```

Under the stamp, in plain script: Isten vele és csókolom számtalanszor.

Address, plain: Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás.

## Normalized Hungarian

Kedves Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Kiment-e tanyára dolgozni? Mi ójság Árokszállásban? Itt nincs semmi újság. Ez[z]el bezárom soraim. Isten vele! Vasárnap, ha jó id[ő] lesz, lemegyek. <UNREAD: e ? e l e g e sz t e m k i e l e d o t> Istenem, hallgasd meg e szerény imámat, add nekem örökre szeretett babámat! Tisztele[m] a kedves mamáját.

Under the stamp: Isten vele, és csókolom számtalanszor.

## English

My dear Jolánka! I hope my lines find you in the best of spirits. Did you go out to the farm to work? What is new in Árokszállás? Here there is nothing new. With this I close my lines. Farewell! On Sunday, if the weather is good, I shall come down. [unread clause] My God, hear this humble prayer of mine, give me my beloved sweetheart for ever! My respects to your dear mother.
Under the stamp: Farewell, and I kiss you countless times.

## Slovak

Moja milá Jolánka! Želám si, aby Vás moje riadky našli v najlepšej nálade. Išli ste na usadlosť pracovať? Čo je nové v Árokszállási? Tu nie je nič nové. Týmto končím svoje riadky. S Bohom! V nedeľu, ak bude pekné počasie, prídem dolu. [neprečítaná veta] Bože môj, vypočuj túto moju skromnú prosbu, daj mi navždy moju milovanú! Pozdravujem Vašu milú mamu.
Pod známkou: S Bohom a bozkávam Vás nespočetnekrát.

## Uncertainties

1. **Rows 12-13, unread clause.** Letters are clear except the over-inked sign ?: an arch with a right arm. Candidates and failed word guesses are in NOTES.md. No reading is offered.
2. Row 11: `vasarnah` is vasárnap (h/p near-homograph, on word sense); `joidlesz` lacks the ő of idő.
3. Word sense decides h vs d in `halgasd` (first sign has d-like form), and d in `add`.
4. Row 9 `eze` is normalized Ezzel, as on hcp-1217; a black spot lies on the middle bar of its second e. Row 10: i of Isten lies under black spots (red dot visible); t of Isten is an overwritten sign (inverted T plus top hook).
5. Row 15: the e of `szerény` is overwritten and blotted. Row 17 ends with a separate red blot under the t, read as no letter.
6. Row 18 `tiszteleakedves`: the m of tisztelem is not written; normalization supplies it.
7. The writer spells ójság once with o (row 7), újság once with u (row 9).
8. Other cards' sender Feri is not named here; no signature is on this card. No legible date.

## Why the read part is correct

The unchanged family key gives Hungarian in 16 of 18 rows, with family formulas (Kívánom hogy a legjobb kedvében találja soraim; Ezzel bezárom soraim; Isten vele; mamáját), the addressee's town, and a rhymed couplet (imámat / babámat). The picture side is a printed poem, not cipher.
