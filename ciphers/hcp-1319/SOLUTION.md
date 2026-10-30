# HCP1319 — postcard to Jolánka Tóth: trip postponed, grape harvest, Sunday arrival

**Status: reading of the cipher complete in that all 157 signs in 13 rows are assigned, with the meaning of one word (*sorozat*) unverified; plain-hand stamp-field note only partly read. Review 1 addressed (see the end).** Claude Opus 5.5, 2026-10-30. No earlier work on this number. The portal shows *Not solved* and attaches no transcription or solution (see SOURCES.md); no published solution of this card was met. The key comes from the finished sister cards of the Jolánka family, above all HCP1216; the transcription is new and made from this card's pixels. It was not blind: the key was known and word sense guided the few calls listed below.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka postcard family, the same key as HCP1212, 1213, 1216, 1217, 1218, 1243, 1301). No new key was invented, and every letter value below is the family's.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| short + tall stroke | d | three short strokes | m | gamma/corner | t |
| three bars | e | two strokes | n | plain cross | u |
| joined hook + descender | gy | cursive loop, hooked tail | o | chevron | v |
| tall + short stroke | h / p | crossed curve, straight tail, dot | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

Signs not occurring here (c, f, g alone, y, cs) are not needed. Dots over the cross give ü.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1319/work/decode.py
```

It checks SHA-256 of the two scans in `source/` and the two originals in `work/hires/`, decodes the manual sign ledger `work/ledger.txt` (157 signs, row 9 counted as n + m) and prints the literal rows and the normalized text. Enlarged crops are in `work/crops/`.

## Literal decipherment

```
01 kedvesjolankam
02 tudatomhogyel
03 utzasonelhalasz
04 tottamegyhetel
05 kesobremostszü
06 retremegyekhol
07 naaso{r?}ozatra
08 vasarnapren{d?}es
09 id{o?}ben{m?}egyekle
10 mostsietekmar
11 istenvelea
12 viszontlatas
13 ra
```

## Hungarian (normalized)

Kedves Jolánkám! Tudatom, hogy elut[a]zásom[at] elhalasztottam egy hét[t]el későb[b]re. Most szüretre megyek, holna[p] a sorozatra, vasárnap rendes időben megyek le. Most sietek már. Isten vele! A viszontlátásra.

Square brackets mark letters the writer did not write.

## English

Dear Jolánka! I am letting you know that I have postponed my departure by a week. Now I am going to the grape harvest, tomorrow to the *sorozat* (tentatively: the army recruitment muster, normally *sorozás*; this sense is inferred, not attested), and on Sunday I am coming down at the usual time. I am in a hurry now. Farewell! Until we meet again.

## Slovak

Milá Jolánka! Oznamujem Vám, že som svoj odchod odložil o týždeň. Teraz idem na oberačku, zajtra na *sorozat* (predbežne: vojenský odvod, bežne *sorozás*; význam je odvodený, nie doložený) a v nedeľu prídem dolu v obvyklom čase. Teraz sa už ponáhľam. S Bohom! Do videnia.

## Uncertainties

Calls that rest on word sense, not on a clean sign match:

1. **Row 7, the sign and meaning of `so{r?}ozatra`** is the weakest point. A pale crossed sign (z class) is overwritten by a dark stem with a long top bar. The dark ink alone has no separate mid-bar, so by shape it is gamma (t class), with the pale z arm lying where a mid-bar would be. Only word sense makes it r: *sotozatra* is no word. The r is a conjecture from sense. The meaning is also unverified. Czuczor-Fogarasi (*sorozat*, https://czuczor.oszk.hu, checked 2026-10-30) gives only "series, list", with no recruitment sense, and two web searches found no attestation of *sorozat* = muster. The family cards use the regular word *sorozás* (HCP1303, HCP1304). I therefore keep the clause tentative: *sorozat* may be this writer's slip or colloquial form for *sorozás*, but that is inference. Date evidence is neutral to mildly favourable: HCP1303 has an April conscription (year not known here), while the 1912 main conscription was late (Debrecen: 12 to 19 August 1912, *A Város*, 3 Aug 1912, https://epa.hu/05500/05521/00374/pdf/EPA05521_a_varos_1912_031.pdf). A September date in the Jász district is not attested by this; it only shows a summer-autumn muster in 1912 is possible.
2. **Rows 6/7 `hol | na a`**: the signs are clear: h o l, then n a a. Normalized *holna[p] a* with a p missing. Alternative: *hol, na, a…* gives no sense here. The missing p is an editorial supplement.
3. **Row 8 `ren{d?}es`**: the sign has the tall + short order of h/p, not the short + tall order of d elsewhere on this card (rows 1, 2, 9). Read d because *rendes időben* is the only sense. HCP1216 has the same irregularity (*de*). The sign is printed as `d?`; the other h/p signs are resolved by sense: h in *hogy, hol, hét, halaszt-*, p in *vasárnap*.
4. **Row 9 `id{o?}ben`**: the first sign has the straight tail of i, and a dark dab up and to the right of it, at the end of a pale smear from the v-stem of row 8, sits where the i dots of rows 10 and 11 sit; I take it as the smeared i dot (corrected after review 1). The third sign has the same straight tail, not the hooked tail of o, and no marks at all, so by shape it is i class; *időben* (o/ő) rests on sense.
5. **Row 9 `ben{m?}egyek`**: after e come two strokes and then a narrow double stroke, four strokes in all where n + m would need five. Either n + compressed m (*időben megyek*, adopted) or a retraced m with n omitted (*időbe megyek*). The sense is the same.
6. **Row 3 `utzason`**: this word carries three editorial changes. (a) The card has five signs before o: cross, gamma, crossed diagonal, two bars, right bowl (u t z a s); there is no a between t and z, and the letter is supplied (*elut[a]zásom*). The writer drops letters elsewhere (*holna*, *hetel*, *kesobre*). (b) The sign after o has two strokes, n, where the word needs m (three); literal n is kept and the normalization treats it as a stroke omitted. (c) The case ending [at] is supplied.
7. **Row 3 `ha` and row 4 `-tam`**: blots lie over the first of these (a third bar could be hidden, a vs e). *halaszt-* and the two clear bars of row 4 favour a. The l of `halasz` has a heavy hooked start unlike the plain wave, and the s has a small left stem; both read from word sense.
8. **Rows 10 and 12**: row 12's t + a is crowded, with a short extra stroke at the top bar (possibly an accent), and two bars below. In row 10 *már*, the a's upper bar nearly joins the r.
9. **Accents** are mostly not seen and are supplied in normalization. The ü of row 5 is seen. The dark dot over row 4's o is grey, not the writer's ink, and is not read as ö. A small pale red speck stands over the first stroke of row 10 and is ignored. Spellings normalized: *hetel* → héttel, *kesobre* → későbbre.
10. **Stamp field (not cipher)**: two plain-hand lines in the same red ink. Line 1 reads *csókolom* (the middle has an ink blot). Line 2 is **unread**; perhaps *százszor*, but this is only a guess and is not part of the decipherment. It may also be a signature, so the sender is not established by this card; the key and the Jolánka address place it in the family, and Feri is the sender of its sister cards.
11. **Date**: the postmark shows **12 SEP** with the day unread, matching the 1912-09 of the scan's file name, and *szüret* fits September. The postal place name is not read.

Plain, not cipher: address *Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás*; printed picture-side verses (*Hulló falevél suttog, beszélget…*, *Szerelemről, boldogságról ábrándozunk Te, meg én*; rotated lines not fully transcribed, decorative print).

## Why it is correct

- The family key, unchanged, turns all 157 signs into Hungarian (row 9 counted n + m; the row has four strokes there, not five), with no sign left over and no sign without a value.
- The text is coherent, with the family's fixed opening and closing (*Kedves Jolánkám*, *Isten vele, a viszontlátásra*, also HCP1212/1216), and its formal address (*vele*) agrees with those cards.
- Long words come out letter by letter with no help from context, *elutazásom* excepted (item 6): *elhalasztottam*, *szüretre megyek*, *vasárnap*, *viszontlátásra*. Repeats agree: *most* ×2, *megyek* ×2, *-egy-* ×3.
- September grape harvest fits the 12 SEP postmark.

## Response to review 1

Verdict REVISE; all five findings accepted and addressed. The message is unchanged. Re-ran `python3 -I ciphers/hcp-1319/work/decode.py`: all four hashes OK, 157 signs, output matches the literal rows and normalized text above.

1. **Row 3 extra sign (major): fixed.** I checked `review/work/crops/z_r3utazas.png`: the card shows cross, gamma, crossed diagonal, two bars, right bowl, with nothing between gamma and z. My ledger's first A was an error, forced from the word. Removed from `work/ledger.txt`; literal row is now `utzasonelhalasz`; normalized *elut[a]zásom[at]* in `work/normalized.txt` and above; disclosed in Uncertainties item 6. The "long words" claim now excepts this word.
2. **Sign count (minor): fixed.** 157, row 9 counted n + m, with the four-stroke note. Status line, reproduction section and Why it is correct updated.
3. **Row 9 dot (minor): fixed.** On `z_r9start.png` the dab is there and in the expected position. First sign is now read `i` without a query mark in the ledger; item 4 reworded. The third sign stays on sense.
4. **sorozat (minor): addressed.** Now checked in a period dictionary: Czuczor-Fogarasi has no recruitment sense, so the sign-level and meaning-level doubts are both stated in item 1, with *sorozás* on HCP1303/1304. English and Slovak now mark the sense as inferred. The April objection is answered only in part: the 1912 main conscription ran in August at Debrecen, but no September muster in this district was found.
5. **"Complete reading" (minor): fixed** in the status line.
