# HCP1223 — Fr… (probably Feri) to Jolánka Tóth: he missed the train; the fire brigade's general meeting

**Status: complete reading, review 1 (REVISE) addressed.** Claude Opus 5.5, 2026-11-02. There is no earlier work on this number. No published solution was found or used; the portal shows Not solved with no attached transcription or solution.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (MASC): the Jolánka postcard family. The key is transferred unchanged from the finished cards hcp-1216, 1212, 1213, 1217, 1218, 1243 and 1301 (table in `ciphers/hcp-1216/SOLUTION.md`); no sign needed a new value. Summary as used here:

a two bars; b six; cs opposed bowls; d short stroke on the left of a long one; e three bars; f upright cross; g open loop with descender; h/p long stroke with a separate short tick on its right (one class); i dotted loop; j inverted T; k section mark; l wave; ly wave joined to a descender; m three strokes; n two strokes; o cursive loop; r F-like; s right bowl; t gamma; u/ü plain cross; v chevron; y low descender; z tailed cross. Accents are marks over the base sign and often invisible.

The picture side (printed photograph, no. 1012) has no writing. The address side is plain: "Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás". Postmark: fragment GY…, year 913 (1913), rest lost at the stamp.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1223/work/decode.py
```

It checks the SHA-256 of all four scans, decodes `work/ledger.txt` (one token per written sign, 414 signs; a manual transcription made from enlarged crops of the un-converted original, not OCR), prints the literal rows and then `work/normalized.txt`.

## Literal decipherment (as printed)

```
01 szeretetédesjolan          12 sajnalokszamittot
02 kamvárvavártsora           13 temkeddenreggelle
03 itmegkaptammelynek         14 mennideaztgondol
04 nagyonmegörültem           15 temhétköznapnem
05 kivanomhogyaleg            16 alkalmatlankodok
06 jobbkedvebentalal          17 szerelmemésminde
07 jasoraim.nehara            18 nemazértnemmehet
08 godjonrámédesem            19 temmalemertatüz
09 ho.gymanemmehettem         20 oltottestületne
10 ledelekéstemavonat         21 vanaközgyülése.hogymulatotgondolt
11 rolamitigazan.             22 enéhrmimadojaraistenveleédesem
under the stamp: isten | vele | édesem | csokol | jahüked | vessefr
```

## Hungarian (normalized)

Szeretet[t] édes Jolánkám! Várva várt sorait megkaptam, melynek nagyon megörültem. Kívánom, hogy a legjobb kedvében találja soraim. Ne haragudjon rám, édesem, hogy ma nem mehettem le, de lekéstem a vonatról, amit igazán sajnálok. Számítottam kedden reggel le menni, de azt gondoltam, hétköznap nem alkalmatlankodok. Szerelmem és mindenem, azért nem mehettem ma le, mert a tűzoltó testületne[k] van a közgyűlése. Hogy mulatott? Gondolt-e néh[a] r[á]m, imádójára? Isten vele, édesem!

Under the stamp: Isten vele, édesem! Csókolja hű kedvese, Fr…

## English

My beloved sweet Jolánka! I have received your long-awaited lines, which made me very glad. I hope my lines find you in the best of moods. Do not be angry with me, my darling, that I could not come down today, but I missed the train, which I truly regret. I had counted on going down on Tuesday morning, but then I thought that on a weekday I would not trouble you. My love and my all, the reason I could not come down today is that the fire brigade has its general meeting. How did you enjoy yourself? Did you sometimes think of me, your admirer? God be with you, my darling!
Under the stamp: God be with you, my darling! Kisses from your faithful sweetheart, Fr…

## Slovak

Moja milovaná sladká Jolánka! Dostal som Vaše dlho očakávané riadky, z ktorých som sa veľmi potešil. Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Nehnevajte sa na mňa, drahá, že som dnes nemohol prísť dole, ale zmeškal som vlak, čo naozaj ľutujem. Počítal som s tým, že pôjdem dole v utorok ráno, ale pomyslel som si, že cez všedný deň nebudem obťažovať. Moja láska a moje všetko, dnes som nemohol prísť dole preto, lebo hasičský zbor má valné zhromaždenie. Ako ste sa zabávali? Spomenuli ste si niekedy na mňa, svojho ctiteľa? S Bohom, drahá!
Pod známkou: S Bohom, drahá! Bozkáva Vás Váš verný milý, Fr…

## Uncertainties

1. **Row 22 `néhrm`** is the weakest point. The signs are clear: e, n, é (three bars with a tick), the h/p sign, r, m, with no a between h and r and none between r and m. Normalized *néh[a] r[á]m* ("sometimes ... me"), so two vowels are supplied. It is a reading of a contracted word by sense (*gondolt-e ... imádójára*, "did you think of ... your admirer"), not of visible signs. The tick over the second e could instead be a third bar of the e/a above it (next point); then *ne* would stand literally here, which gives no better word. Everything around these two words reads without doubt.
2. **Row 21 `vana`**: the signs at the left margin are v, two bars, n, then two bars plus a slanting dash, which sits between rows 21 and 22. I take the dash as the accent of the é below, giving *van a*; if it is a third bar, the word is *vane*, which is no word here. Note also that rows 21 and 22 begin close together at the left and share this margin.
3. **Row 20 `testületne`**: no k before the v; supplied in brackets (*testületne[k]*). Writer's omission, not damage.
4. Withdrawn after review 1: the claimed row 19 `malen` was a transcription error. The card has *ma le*, with nothing irregular.
5. **Signature `fr`**: the sign row ends in f, r at the edge of the surviving stamp fragment. This is reported literally. Other cards of the family sign Feri, which is a likely expansion, but *-eri* is not on the card as read, and I do not know whether anything follows under the stamp remnant. Not a restoration.
6. **d written in the h/p shape, three times**: *de* in rows 10 and 14 and *gondolt* in row 21 have a long stroke with a short tick on its right, not the usual d with the short stroke on the left. Read d because only d gives sense, as on hcp-1216 (uncertainty 3 there). Literally row 10 would be *le he lekéstem*, and *gonhol-* gives nothing.
7. **h/p calls resting on word sense**: every h and p on the card is this one sign. P was chosen only in *kaptam* (row 3) and *hétköznap* (row 15); all others h.
8. **Row 4 `nagyon`**: the y and o are run together in one dark blot after the g; the word is certain, the shapes are not separate. **Row 15**: an ink blot touches the p of *-nap*. **Row 21**: the u of *mulatot* is a cross filled with ink. The m at the end of row 4 and the signs around *melynek* and at the end of row 3 are crossed by the postmark but legible.
9. **S1**: the first sign under the stamp (i of *isten*) is smeared by stamp glue; its value is confirmed by the repeated phrase in row 22. Other faint signs under the stamp are legible.
10. **Writer's spellings, normalized**: *szeretet* → szeretett; *haragodjon* → haragudjon (the sign after g is a clear o); *amit* written on row 11 after *vonatról* with two bars; *szamittottem* → számítottam (double t and final *-tem*); *reggel le* written as *reggelle*; *minde|nem* across a row break; *mulatot* → mulatott; *oltottestület* → tűzoltó testület (one t too many: the row has two t's after the o, where the words need one on each side of it, *oltotestület*); *vessefr* → *kedvese* with doubled s, split as *ked|vesse*; *kedvebentalal|ja*. The stroke after *édesem* in row 22 is a fourth, shorter stroke after m, treated as a point; a stray dot sits after the o of *hogy* in row 9 and is kept in the ledger.
11. **Accents**: most á, é, í, ó, ú are invisible at this hand and are supplied in normalization; only marks seen are in the ledger. ű is shown by two dots (*tűz, közgyűlése, hű*), not distinguished from ü.
12. Row 22 ends with the same phrase that opens the stamp area: *isten vele édesem* is written twice. I read both on their own signs; it is not a duplicate transcription.
13. The ledger is not blind: the key and family formulas were known while reading.

## Why it is correct

- A key taken unchanged from other cards turns all 414 signs into continuous Hungarian with no unvalued sign and no key change.
- Long words appear without forcing: *megörültem, alkalmatlankodok, közgyűlése, tűzoltó, testület, hétköznap, imádójára*; repeated words decode alike (*nem* ×3, *mehettem* ×2, *édesem* ×3, *hogy* ×3).
- The text fits the family: *Várva várt sorait*, *a legjobb … találja soraim* and formal Ön address recur on sister cards, as does *hű kedvese* and *imádója*. The text is about going down by train to the addressee's town, also a family theme.
- The result is a mundane, specific excuse (a fire brigade meeting) that nobody would guess; it was not expected from context.

## Credit

Transcription, key transfer and decipherment by Claude Opus 5.5. The key itself was reconstructed on the sister cards (OpenAI GPT solver with later Claude Opus 5.5 completion; see those directories).

## Response to review 1

Verdict REVISE. All four findings accepted; I rechecked 1 and 2 on the hires scan (`work/crop4.py`, `work/crops/z21word.png`, `zr01.png`, `zr14.png`, and the reviewer's `row19.png`, `z19.png`). The normalized text and the translations do not change.

1. **Major, row 19 `malen`: fixed.** Between the e of *le* and the e of *mert* there are exactly three strokes, one m. My earlier five came from counting across the seam of two overlapping crops. The N token is deleted from `work/ledger.txt`, the count is 414, the literal row is `temmalemertatüz`, and uncertainty 4 is withdrawn. The note in NOTES.md stands as a record, with a correction added beneath it.
2. **Minor, row 21 *gondolt*: fixed.** The sign is a long stroke with a short tick on its right; the normal d in rows 1 and 14 has the short stroke on the left. The ledger token is now HD, uncertainty 6 lists three cases, and the key summary and ledger header state which side the short stroke is on.
3. **Minor, signature: fixed.** The title now says Fr… (probably Feri).
4. **Minor, descriptions: fixed.** Uncertainty 10 now describes *oltottestület* as one t too many and gives *kedvese*; *nem* is ×3 (rows 9, 15, 18).

`python3 -I ciphers/hcp-1223/work/decode.py` re-run after the changes: all four hashes OK, 414 signs, none without a value, row 19 as above; `gondolt` still decodes because HD has the value d.
