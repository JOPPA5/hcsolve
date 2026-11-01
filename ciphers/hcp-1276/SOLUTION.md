# HCP1276 — Feri to Jolánka Tóth, 11 August 1912: a goddaughter's death and a harvest ball

**Status: complete reading with one unresolved group of about six signs (uncertainty 1); the rest of the message reads. Revised after review 1.** Claude Opus 5.5, 2026-11-01. No earlier work on this number; no published solution found. The portal shows *Not solved* and attaches no transcription or solution. The transcription is mine, made from the scan.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (MASC): the Jolánka family key, transferred unchanged from finished cards HCP1216, 1212, 1213, 1217, 1218, 1243, 1301. Sign classes are those in the table of `ciphers/hcp-1216/SOLUTION.md`:

a two bars; b six; c left bowl; d long stroke + short tick; e three bars; f upright cross; g open loop with descender; gy joined loop + descender; h/p tall stroke + short (near-homographs); i dotted crossed curve; j inverted T; k section mark; l wave; m three short strokes; n two short strokes; ny = n + y; o cursive loop; r F-like; s right bowl (sz = s + z); t gamma/corner; u cross x; v chevron; y low descender; z crossed diagonal. Marks over o/u give ö/ü. Numerals stay in clear: `7` in row 12.

The card is only partly enciphered: the opening is in ordinary handwriting, then the cipher starts on the same line after *köszönetemet*. The stamp box holds a further five cipher rows.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1276/work/decode_opus.py
```

It checks the SHA-256 of the two source scans and the two hi-res originals, decodes `work/ledger-opus.txt` (one token per written sign, 16 rows plus 5 in the stamp box; corrected after review 1) and prints the literal letters and `work/normalized-opus.txt`. The ledger is a manual transcription, not OCR.

## Literal decipherment

```
01 igazansaj              09 hadeluta{|}menn  
02 nalomakeresztla        10 akorestereokvet
03 nyunkatonnekedesem     11 lenszeptember
04 evelahalallal          12 7enleszegyszü
05 aremenyeiosze          13 retimulatsagis
06 döltekkedvesem         14 deszeretnemnahogykan
07 amulatsagbaok          15 feljonneazmulatsagba
08 vetlenlemegyek         16 istenvelaviszontlatasraferi
stamp box: üdvöz | lomata | volbol | hükedves | ceferi
```

## Hungarian (normalized)

Plain script: Szeretett Édes Jolánkám! Becses sorait megkaptam, melyért fogadja köszönetemet.

Cipher: Igazán sajnálom a keresztlányunkat. Önnek, édesem, evvel a halállal a reményei összedőltek. Kedvesem, a mulatságba okvetlen lemegyek; ha délután menn[ék], ak[k]or estére okvetlen. Szeptember 7-én lesz egy szüreti mulatság is, de szeretném, {na/ha hogy kan} feljönne a(z) mulatságba. Isten vel[e], a viszontlátásra! Feri.

Stamp box: Üdvözlöm a távolból, hű kedvese, Feri.

Address, plain script: Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás.

## English

Plain script: Beloved sweet Jolánka! I have received your esteemed lines, for which please accept my thanks.

Cipher: I am truly sorry about our goddaughter. For you, my sweet, your hopes have collapsed with this death. My dear, I will certainly go down to the party; if I went in the afternoon, then by evening for certain. On 7 September there will also be a harvest ball, but I would like [unresolved: *na/ha hogy kan*; probably "if … "] you to come up to the ball. God be with you, until we meet again! Feri.

Stamp box: I greet you from afar, your faithful sweetheart, Feri.

Address: To the young lady of fair hopes, Miss Jolánka Tóth, Jászárokszállás.

## Slovak

Rukopisom: Milovaná sladká Jolánka! Vaše vzácne riadky som dostal, za čo prijmite moju vďaku.

Šifra: Naozaj ľutujem našu krstnú dcéru. Vám, drahá, sa touto smrťou zrútili nádeje. Moja milá, na zábavu určite prídem; ak by som šiel popoludní, tak do večera určite. Siedmeho septembra bude aj oberačková zábava, ale chcel by som [nevyriešené: *na/ha hogy kan*; asi „keby …“], aby ste prišli hore na zábavu. S Bohom, dovidenia! Feri.

V rámčeku na známku: Pozdravujem Vás zďaleka, Váš verný milý, Feri.

Adresa: Slečne krásnych nádejí Jolánke Tóthovej, Jászárokszállás.

## Uncertainties

1. **Row 14, end, `na hogy kan`, unresolved.** After *szeretném* the row climbs above the line and is cramped. It reads: two strokes (n, or h: on the 3x crop `work/crops/rv_r14end.png` the second is about two-thirds of the first, less sharp than a normal h), a; a 2-shaped sign with a crossbar found nowhere else on the card; a large O; a sign overwritten by a blot with a descender and rising tail; section mark k; a; two strokes n. *Hogy* is a guess from the outline: h rests on word sense only, gy on what shows through the blot (a small comma-shaped mark stands above it). *ka-n* has no identified meaning (name? false start? the last sign could be d/h/p). After review I checked whether the first two signs are *ha*, since *szeretném, ha … feljönne* ("I would like it if … came up") is the normal construction. That is a word-sense suggestion only, and it would leave one unread word of about six signs, perhaps a form of address such as a pet name; the family has *jolakám* elsewhere, but the 2-shaped sign, the blot and the final n do not support any such form, so I do not claim it. The clause sense ("I would like … you to come up") does not depend on this group, but those letters are not an understood word.
2. **Rows 9/10, literal `...uta{|}menn | akor`.** Between the a of *-uta-* and the e of *menn* the card has exactly four strokes: one with a curled foot, then three. *Délután* + *menn* needs five, so one stroke is missing: the writer ran the words together or dropped a stroke, and `|` + m stands for *-n m-*. This rests on word sense. In *menn* the last four strokes are uneven (tall + short + two short), so nn is also a sense-based choice. Row 10 opens with a, so the word is *akor* = *akkor*, the family spelling (HCP1216, 1258, 1262). *Mennék* has a supplied ending: the card has only *menn*. The sentence *estére okvetlen* has no verb on the card.
3. **Blotted signs, read through the blot:** row 9 u of *délután* and row 15 u of *mulatságba* (the cross arms show on both sides); row 13 s of *mulatság* (overwritten, shape not a clean match, the word requires s); row 14 gy (uncertainty 1); row 11 p (uncertainty 4); row 15 z of *az*: the crossed arm suits z, but the closed loop on the left is not part of z. It may be a slip (*az* before a consonant) or an overwritten or struck sign, in which case the text is plain *a mulatságba*. Hence *a(z)*. I did not restore any sign that was fully hidden.
4. **Row 11, p of *szeptember*:** overwritten with thick ink, tall stroke + short; h/p homograph, p from the word. **Row 4:** first sign of *halállal* is the same class, h from the word. **Row 12:** `7` is read as a digit, with *-én*; it matches no key sign.
5. **Stamp box end, `kedves | ceferi`:** right bowl at the end of row 4, left bowl at the start of row 5. Taken apart they give *kedvesc e*; together, opposed bowls, they would be cs, *kedvecse*. Normalized *kedvese* (the family's closing formula, HCP1216), but this is my reading of an odd spelling. Stamp row 3 second sign is o, its hook overlapping the red postmark trace in the box.
6. **Row 3, *önnek*:** no dots visible over o; four strokes read nn (2+1+1 spacing). The ö of *jönne* and ő of *dőltek*/*összedőltek* are normalized; *evel* → evvel; *osze* → össze.
7. **Address, *Szépreményű*:** it stands right of the printed divider, above *Tóth Jolánka*, and belongs to the address, as sister cards HCP1245, 1252, 1259 and 1261 show in clear. Its first letters run under the postmark and are read by shape and from those cards. It is not cipher text. **Row 16, *vel[e]*:** the card has one sign of two bars between the wave l and the chevron v, so literal `vela viszontlatasra`, a merge of *vele a*; the e is editorial.
8. Accents are mostly omitted or faint and are supplied in normalization. Sentence division is editorial, including the break after *keresztlányunkat*.
9. "Our goddaughter" is the literal sense of *keresztlányunkat*; who she was is not stated. The sender is identified only as Feri; I claim no identity with a Feri of other cards beyond the shared key and closing style. Date 1912-08-11 is from the portal file name; the postmark shows "12 AU… 11", which agrees.

## Why it is correct

- A key taken unchanged from finished sister cards yields connected Hungarian across all 16 rows and the stamp box. The key is unchanged, but the reading does supply something: row 9 lacks one stroke, *menn[ék]* lacks its ending, and *vel[e]* lacks its e. Only row 14's end group has no reading: it is the one unread group, and the sentence around it reads.
- Long passages admit no choice: *keresztlányunkat*, *a reményei összedőltek*, *szeptember 7-én lesz egy szüreti mulatság is*, *Isten vele, a viszontlátásra*, *üdvözlöm a távolból*.
- Repeated words decode identically: *mulatság* ×3, *okvetlen* ×2, *kedvesem*/*édesem*. The text is thematically coherent, since a September harvest ball is a natural event, and it uses the family's formal address.

## Response to review 1

Verdict REVISE. I re-read every contested spot on the hi-res scan (reviewer's crops plus mine, `work/crops/rv_*.png`). All eight findings are accepted and fixed. No key change; the reading is not substantially changed.

1. **Szép reményű in the address: fixed.** It stands right of the divider above *Tóth Jolánka* (`review/work/plain3.png`). Removed from the message in Hungarian, English, Slovak and `work/normalized-opus.txt`; address line added in all languages; uncertainty 7 rewritten.
2. **Row 10 first sign a: fixed.** Two bars, clearly unlike the three-bar e on the same row. Ledger `A`; literal `akorestereokvet`. *Akor* = *akkor*; *menn[ék]* marked as supplied; uncertainty 2 rewritten.
3. **Row 9 strokes: fixed.** I confirm four strokes between a and e, plus a real three-bar e (its top bar stands high; `work/crops/rv_r9end.png`). Ledger now `A | M E N N`, literal `hadeluta{|}menn`. Uncertainty 2 says the missing stroke rests on word sense.
4. **Row 16 phantom sign: fixed.** One two-bar sign between l and v (`review/work/b6R.png`). Ledger `L A V`; literal `istenvelaviszontlatasra`; normalized *vel[e]*; listed in uncertainty 7. The ledger header stays true now, and "without adjustment" is gone.
5. **Row 14 gy: fixed.** Ledger `*GY`; uncertainty 1 kept as the headline caveat. I also checked *ha* for the first two signs and record it as a word-sense suggestion: the ledger stays `N A`, and the normalization shows *na/ha*.
6. **Row 15 *az*: fixed.** Normalized *a(z)*; uncertainty 3 allows an overwritten or struck sign.
7. **Row 11 p: fixed.** Ledger `*P`, header lists it.
8. **"Why it is correct": fixed.** Updated, and "without adjustment" removed.

`python3 -I ciphers/hcp-1276/work/decode_opus.py` re-run after the fixes: four hashes OK, and the output equals the literal block above.
