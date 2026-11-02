# HCP1241 — Feri to Jolánka Tóth: "destroy my lines"

**Status: complete reading, review 1 ACCEPT, findings addressed below.** Claude Opus 5.5, 2026-11-02. There was no earlier work on this number. The portal shows Not solved with no attached transcription or solution; no published solution of this card was found. The transcription is mine, from the pixels of the original scan in `work/hires/`.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (register label MASC). This is the Jolánka family key, transferred unchanged from the finished cards HCP1216 (fullest legend), 1212, 1213, 1217, 1218, 1243, 1301. No sign needed a new value.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| short stroke then long stroke (separate on this card) | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | long stroke then short stroke | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

d and h/p use the same two strokes in opposite order: short then long is d, long then short is h/p. The d calls on this card depend on that order. Two dots over o give ö. An acute stroke is often visible on e, a, o and is recorded in the ledger where seen.

The card also has unenciphered text: the panel in the stamp square, the last words along the bottom edge and up the right edge, and the address.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1241/work/decode.py
```

It checks the SHA-256 of both source scans and both originals, decodes `work/ledger.txt` (one token per written sign, 20 rows), and prints the normalized text `work/normalized.txt`. The ledger is a manual transcription, not OCR.

## Literal decipherment

```
01 dragacsillagombecses       11 semiésénisugy
02 soraitmegkaptammely        12 teszekezekutan
03 nagyörömemszol             13 megnagyóbbsze
04 galtmelymeggyöz            14 retettelfordulok
05 tefajoszivemet             15 önhözédesegyetlen
06 arrolhogyszeret            16 reményem.hogytelt
07 semisitsemegso             17 elvasárnap.tavol
08 raiméstegyen               18 {b?}ogondolenéha
09 ugyminthanem               19 ramtalándudasju
10 tortetvolna                20 li[s]kabeszélteteleafejét
```

Plain script after row 20, along the bottom edge and up the right edge: tiszteltetem a kedves mamáját

Plain script in the stamp square: Isten vele / édesem / továbbra / is hűke[d] / vese cso- / kolom / szamtalan- / szor Fe[ri]

Address (plain): Szép reményű / Tóth Jolánka / úrleánynak / Jász Árokszállás

Printed on the picture side, not part of the message: "Fecském hova szállsz?" and a four-line verse beginning "Valamikor réges-régen".

## Hungarian (normalized)

Drága csillagom! Becses sorait megkaptam, mely nagy örömem[re] szolgált, mely meggyőzte fájó szívemet arról, hogy szeret. Semmisítse meg soraim[at] és tegyen úgy, mintha nem törté[n]t volna semmi. És én is úgy teszek. Ezek után még nagyobb szeretettel fordulok önhöz, édes egyetlen reményem. Hogy telt el vasárnap? Távolbó[l] gondol-e néha rám? Talán Dudás Juliska beszélte tele a fejét. Tiszteltetem a kedves mamáját.

Stamp square: Isten vele, édesem. Továbbra is hű ke[d]vese. Csókolom számtalanszor. Fe[ri]

## English

My dear star! I have received your valued lines, which gave me great joy and convinced my aching heart that you love me. Destroy my lines and act as if nothing had happened. I will do the same. After this I turn to you with even greater love, my sweet only hope. How did Sunday go? From afar, do you think of me sometimes? Perhaps Juliska Dudás has filled your head with talk. Give my respects to your dear mother.

Stamp square: God be with you, my darling. Still your faithful sweetheart. I kiss you countless times. Feri

## Slovak

Moja drahá hviezda! Vaše vzácne riadky som dostal a urobili mi veľkú radosť a presvedčili moje boľavé srdce o tom, že ma ľúbite. Zničte moje riadky a správajte sa, akoby sa nič nestalo. Aj ja urobím to isté. Po tomto sa na Vás obraciam s ešte väčšou láskou, moja sladká jediná nádej. Ako ste prežili nedeľu? Myslíte niekedy z diaľky na mňa? Azda Vám Juliska Dudásová nahovorila plnú hlavu. Pozdravujte odo mňa Vašu milú mamu.

V poli známky: S Bohom, drahá. Naďalej Váš verný milý. Bozkávam Vás nespočetnekrát. Feri

## Uncertainties

1. **Row 20, third sign (restoration).** The sign in `li[s]ka` is a blot-filled oval and its shape cannot be identified. The blot has a light interior and a crescent outline bulging to the lower right, which suits a bled right bowl; it is also about as wide as the opposed-bowl cs. So s, giving Juliska, is the likeliest form but cs, giving a diminutive like "Julicska" (unattested here), cannot be excluded on the pixels. The sense does not change: the person is a Julia either way. Rows 19–20 at the left edge have spread ink, so the neighbouring signs are thickened too.
2. **Row 20, second sign.** This is the dotted crossed-curve i, but the spread ink makes it look like a cross. The dot is clear, and an f would give no word. The name "Dudás Juliska" is read from the signs and context. She does not appear in any other SOLUTION.md in this repo, so nobody is identified.
3. **Row 18, first sign.** A thin stroke with a small flag at the top and a loop at the base. It is not the usual six (the four sixes on this card have a curved stem and no flag), but of the known signs it is closest to b, so b is a call from sense, not from shape. "bo" completes row 17: távol-bo, which is távolból ("from afar") with final l dropped. That l-drop is a known Hungarian dialect feature, but my attribution of it here is an interpretation. The alternative that a separate word starts here gives no sense.
4. **Word-sense calls on near-homographs.** h/p: p only in megkaptam and vasárnap, h everywhere else (arról hogy, mintha, önhöz, hogy, néha). d/n were decided by stroke length (d in fordulok, édes, gondol, Dudás; n otherwise). In the name Dudás the sense does not help, so it rests on the strokes, which show a short tick and a long stroke in both d signs.
5. **Writer's omissions and spellings, not on the card:** örömem[re] (literal nagyörömem, the -re is supplied), soraim[at] (literal soraim), törté[n]t (literal tortet: t o r t e t, so only the n is missing, plus the ö dots and the é accent), semi = semmi, semisitse = semmisítse, nagyóbb = nagyobb, távolbó[l]. Accents absent from the ledger are supplied in normalization.
6. **Stamp square.** At the end of "hűke" the ink is smeared, so the d of ke[d]vese is a restoration. "Feri" shows clearly F and e, and the rest lies under a pink blot. It is restored as the signature on sister card HCP1216. "továbbra": the middle letters are written loosely; the phrase "továbbra is" fixes the word. Small plain-script points: the final t of mamáját lies in a pink blot, the final n of "szamtalan" runs into a blot, and "hű" and "reményű" are written with two dots, like ü, and are normalized to ű.
7. **Address.** "Szép reményű" is a compliment before the name. The ending of "Jolánka" runs into the postmark. The card has no ciphered address.
8. **Date.** The portal file name gives 1912-05-12. On the postmarks I can read "MÁJ" and a year ending 12. The day is not certain and I do not claim it: on enlargement the Jász-Árokszállás mark ends in a clear 0 with something obscured by the pen stroke before it, and the other mark shows 1 and a second digit that may be 9, 3 or 7. 12 May may therefore not be the postmark day, and a date from the card itself is not established.
9. **Sense.** The card does not say what the writer wants destroyed or what passed before. "Destroy my lines" is the literal reading of semmisítse meg soraim; the reason is unknown.

## Why it is correct

- A key taken unchanged from other cards gives continuous, grammatical Hungarian across all 20 rows, with one blot-hidden sign and one doubtful sign.
- Long words appear without any forcing: csillagom, szolgált, meggyőzte, szívemet, semmisítse, egyetlen reményem, szeretettel, vasárnap.
- Rows break words mid-word (szol|gált, so|raim, sze|retettel, ju|liska), and the pieces join correctly.
- The enciphered sentence continues into the plain "tiszteltetem a kedves mamáját". The final sign group ends the clause "beszélte tele a fejét".
- The plain stamp panel, the Feri signature, the addressee and the Jászárokszállás address match the family, especially HCP1216.

## Response to review 1

Verdict ACCEPT, seven minor findings. No deciphered letter changed. After the edits below I re-ran `python3 -I ciphers/hcp-1241/work/decode.py`: all four hashes OK, 20 rows printed, and the output matches the literal block above.

1. **Row 17 point: fixed.** On the reviewer's crop `review/work/crops/dots16.png` the point after the p of vasárnap is plain and looks like the one after reményem. Added to `work/ledger.txt` and to the literal block. It supports the sentence break there.
2. **Row 20 blot: fixed.** Agreed. Uncertainty 1 now gives the cs alternative, and Juliska is the likeliest form, not a proven one. The ledger keeps [s].
3. **Row 18 first sign: fixed.** Agreed. Uncertainty 3 now states that b comes from sense, not shape. It stays marked {b?} and távolbó[l] stays doubtful in the report.
4. **Note on törté[n]t: fixed.** Only the n is restored. Changed in the normalized text, in `work/normalized.txt` and in uncertainty 5.
5. **Key table: fixed.** The d row and the h/p row now state the stroke order, and a sentence after the table says the d calls depend on it.
6. **Plain-text restorations: fixed.** The final t of mamáját, the final n of szamtalan and the normalization of ü to ű are listed in uncertainty 6.
7. **Decoder close to an identity map: accepted, no change.** The ledger names tokens by plaintext letters, so the command reproduces the reading and does not prove it. The evidence is the key taken from other cards and the reviewer's neutral-name pass. The report says so.

The reviewer also could not read the postmark day. I enlarged both marks and could not settle it either; uncertainty 8 now records what each mark shows.
