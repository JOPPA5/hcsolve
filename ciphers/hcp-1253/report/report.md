# HCP 1253 (cpc_1913-02-22_HU__HU_Jasz Arokszalas_jolanka-33): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 20 main rows and the 7 rows in the stamp box); one sign restored, one writer's omission supplied. Independent review 1 verdict REVISE; all six findings addressed, with one word of the closing changed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1253 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1253), portal name cpc_1913-02-22_HU__HU_Jasz Arokszalas_jolanka-33, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side shows a photographed couple and carries no handwriting, only the printed series number 3601/02. The whole message is on the address side: 20 rows in the left panel, of which the last two run past the printed divider, and 7 short rows inside the printed stamp box, where the stamp is now lost.

The address is in plain writing: *Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás* ("to the promising young lady Jolánka Tóth"). Its first word is overlapped by postmarks. The cancellations are only partly legible: one shows *GY…* and *913 F…*, the other *…ÁROKSZ…* and *22*. The date 1913-02-22 comes from the portal's file name and fits those fragments.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the stamp box and the cancellations (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth and signed Feri, many of which are deciphered in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243, 1250, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery. No reading of this card existed or was consulted.

## Method

The work was a careful manual transcription; no OCR was used. There was no earlier work on this number.

- **Transcription (Claude Opus 5.5):** the rows rise by up to about 5 degrees, so straight crops mix lines. The solver rotated and enlarged crops of the un-converted scan and recorded a sign ledger, one token per written sign (`work/ledger.txt`, 365 signs).
- **Decoding:** the script `work/decode.py` checks the SHA-256 of the images, decodes the ledger with the family key and prints the literal letters and the normalized text.
- **Review (a separate Claude Opus 5.5 agent):** re-ran the command, wrote its own transcription and decoder, read all rows on its own crops and checked the contested places at 2–6×. It saw the solver's text first, so this was a check against the pixels, not a blind reading. After the fixes below, its script differs from the ledger only in the marking of one uncertain token (S7), not in any letter.

The writer spells phonetically and carelessly: he drops letters and writes few visible accents. The literal decipherment keeps what is on the card; the normalized Hungarian is editorial.

## Key

Simple monoalphabetic substitution with invented graphic signs, with a hidden message under the stamp (type **MASC + Steganography**, updated 2026-11-03). The seven rows in the stamp box were written where the stamp would cover them; the stamp is now lifted. Hungarian digraphs are spelt with two signs (sz = s + z), and gy and cs usually as joined forms.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark S (or 8) | k | F-like | r |
| six | b | wave | l | right bowl; on this card also left bowl | s |
| opposed bowls; on this card also left bowl + stroke | cs | three short strokes | m | gamma/corner | t |
| tick on the left + long stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop (undotted) | o | chevron | v |
| upright cross + | f | tall stroke + tick on the right | h / p (rarely d) | crossed diagonal | z |
| open loop with descender | g | dotted crossed curve (same loop with a dot) | i | low-crossed T | j |
| g + low descender | gy | | | | |

Marks: dots over the loop give ö, two ticks give ő, dots on the cross give ü, a tick gives an acute. Most acutes are not written or not visible and are supplied in normalization.

Two variants on this card are in no sister key table searched: the left bowl for s (three positions) and left bowl + stroke for cs (two positions). The family otherwise gives the left bowl to c.

## Plaintext

Literal decipherment, row by row. `{}` marks a call on an unclear sign, `[]` a restoration; rows S1–S7 are in the stamp box.

```text
01 sszeretetédesjolánkám          15 lentszeretnékdolgoz
02 kivanomhogyjoegeszég           16 niésmarkezdődia
03 bentaláljasoraim               17 munkaesithonnem
04 hogymulatnakoda                18 akarokdolgozni
05 hazaremélemjol                 19 masujsagitnincsugyanézis
06 bejönhéntekenva                20 régiistenveédesem
07 romhanemjönleéde               S1 [cs]okolom
08 semésírjameghale               S2 szamtalan
09 kellenevinnvala                S3 szorima
10 mitszivesenle                  S4 {d}o{j|t}aés
11 viszemitnincs                  S5 irighü
12 semiujsagmunkam                S6 kedvese
13 nincsamit{n}emisna             S7 fer{i}
14 gyokeresekmertcsak
```

### Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy jó egészségben találja soraim. Hogy mulatnak oda haza? Remélem, jól bejön pénteken, várom. Ha nem jön le, édesem, és írja meg, ha le kellene vinni valamit, mit szívesen leviszem. Itt nincs semmi újság, munkám nincs, amit nem is nagyon keresek, mert csak lent szeretnék dolgozni, és már kezdődik a munka, és itthon nem akarok dolgozni. Más újság itt nincs, ugyanez is régi. Isten ve[le], édesem.

Stamp box: [Cs]ókolom számtalanszor. Imádója és sírig hű kedvese, Feri.

### English

Beloved sweet Jolánka! I wish that my lines may find you in good health. How are you all enjoying yourselves at home? I hope you will come in safely on Friday; I am waiting for you. If you are not coming down, my sweet, then write and tell me whether anything should be taken down, which I will gladly take. There is no news here. I have no work, and I am not looking very hard for any, because I would only like to work down there; the work is already starting, and I do not want to work at home. There is no other news here, and even this is old. Farewell, my sweet.

Stamp box: I kiss you countless times. Your adorer and sweetheart faithful unto the grave, Feri.

### Slovak

Milovaná sladká Jolánka! Želám si, aby Vás moje riadky našli v dobrom zdraví. Ako sa zabávate doma? Dúfam, že v piatok dobre prídete, čakám Vás. Ak neprídete dolu, drahá, napíšte mi, či by bolo treba niečo zaniesť dolu, rád to zaveziem. Tu nie je nič nové. Prácu nemám a ani ju veľmi nehľadám, lebo by som chcel pracovať len tam dolu; práca sa už začína a doma pracovať nechcem. Inej novinky tu niet, aj táto je stará. Zbohom, drahá.

V rámčeku známky: Bozkávam Vás nespočetnekrát. Váš zbožňovateľ a do hrobu verný milý, Feri.

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1253/work/decode.py
```

The command checks the four image hashes, decodes `work/ledger.txt` and prints the literal rows and the normalized text. `work/crop.py`, `strip.py` and `low.py` rebuild the crops.

## Uncertainties

Restoration and omission:

- **S1 *[cs]ókolom*:** the first position is a heavy blot at the edge of the stamp residue. Only one thick stroke survives, so *cs* is a restoration; *okolom* is clean and the word opens the box on sister cards.
- **Row 20 *Isten ve[le]*:** the signs run *v e é d e s e m*; *le* is not on the card and no sign is hidden there. It is the writer's omission.

Calls that rest on word sense:

- **h/p:** one sign serves both. p in *pénteken* (written *héntek-*), and h in *hanem/ha nem*, *hogy*, *meg ha*, *itthon*, *hű*, are all by word sense.
- **Row 13:** the sign before *em* is overwritten, two strokes crossed by two bars, read n for *nem*. The t before it is also overwritten.
- **S4 *imádója*:** the first sign has the h/p shape and is read d. The heavy third sign is an inverted T and a gamma superimposed; j gives the word, t gives none.
- **S6 *kedvese*:** the d is two longish strokes, close to n; *kenvese* is no word.
- **S7 *Feri*:** the last sign is an undotted loop, literally o; *Feri* rests on word sense and the family signature.
- **Left bowl = s:** rows 12 and 15 have it where only s makes sense. Row 1 opens left bowl + right bowl + z; *cs* gives no word there, so this is read as a corrected false start for *sz*.
- **Rows 11 and 19, *nincs*:** the cs is left bowl + stroke. The final s of *is* in row 19 is retouched.
- **Row 11, stray mark:** a heavy tick stands on the baseline after *viszem*. It carries no letter and is probably a comma.

Spelling normalized (these signs are simply not on the card): *szeretet* to szeretett; *egeszég-ben* to egészségben; *semi* to semmi; *itnincs*, *ithon* to itt nincs, itthon; *ugyanéz* to ugyanez; *vinn* to vinni; *nagyo* to nagyon; *kezdődi a* to kezdődik a. In *és sírig* one written s is shared by the two words.

Interpretation, not affecting the letters:

- Word division in rows 5–8 is editorial. *Jól* may go with *remélem* ("I hope you are well", then *Bejön pénteken?*). *Hanem jön le* ("but do come down") is possible beside the printed *ha nem jön le*.
- The card does not say what place *le*, *lent* and *bejön* refer to.
- *Ugyanéz is régi* may also be *ugyan ez is régi*, "though this too is old".
- The year and month of posting come from the file name, not from a fully legible postmark.

## Review summary

Round 1 verdict: **REVISE**. The reviewer confirmed the key, the coverage and the letter body, and raised six findings:

| No. | Severity | Finding | Outcome |
|---|---|---|---|
| 1 | major | A sign was missed at the end of row 2: g past the printed divider, with a tick on the preceding e | Fixed: *egeszég-ben* |
| 2 | major | The second sign of S4 is o, so *imádója*, not *imádja* | Fixed in ledger, text and translations |
| 3 | minor | The last sign of *Feri* is literally o | Fixed: marked as a call |
| 4 | minor | Stray tick in row 11 not disclosed | Disclosed; the solver differs on its cause, since a dot already stands above the next i, and takes it as a probable comma |
| 5 | minor | The claim of a single key extension was too narrow | Fixed: both variants are listed |
| 6 | minor | Alternative reading of *ugyanéz is régi* | Added |

The sense of the letter body did not change. The closing changed from "your adoring sweetheart" to "your adorer and sweetheart". The reviewer did not read the first address word letter by letter, did not audit every faint accent tick, and did not check the sister scans for left bowl = s.

## Credits

Transcription, key transfer and decipherment: Claude Opus 5.5. Independent review: a separate Claude Opus 5.5 agent. Family key: finished Jolánka cards in this repository, chiefly HCP 1216.

## Sources

- HC Portal record 1253 and its images (hashes in SOURCES.md): https://crypto.hcportal.eu/dashboard/cryptograms/1253
- Tobias Schrödel's postcards, HistoCrypt: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- Family key: ciphers/hcp-1216/SOLUTION.md in this repository.
