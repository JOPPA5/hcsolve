# HCP1291 — Feri to Jolánka Tóth: excuses for writing so rarely (31 Aug 1913)

**Status: complete reading of all cipher text on the card, with the small residual points listed below. Corrected after review 1 (REVISE); see the last section.** Claude Opus 5.5, 2026-10-30.

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1291 (status *Not solved*, category Substitution, language Unknown, no transcription or solution attached). The orchestrator's AI-register check of 2026-10-30 found no record for this number. No published solution of this card was used or seen. There is no earlier work on this number. The key comes from the finished sister cards (HCP1216, 1212, 1301 and others), whose work is credited in their own directories; it was not re-invented here, and every sign on this card was read afresh.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the Jolánka family). The key is unchanged from HCP1216:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | left bowl | c | right bowl | s |
| tall + short stroke | h / p (see below) | wave | l | gamma/corner | t |
| three bars | e | three short strokes | m | plain cross x | u |
| upright cross + | f | two short strokes | n | chevron | v |
| open loop with descender | g | cursive loop | o | low descending curve | y |
| dotted crossed curve | i | inverted T | j | crossed diagonal (x with tail) | z |
| short + tall stroke | d | | | | |

Digraphs are spelt with two signs (gy = g+y, sz = s+z, ny = n+y). Accents are marks over the sign and are mostly faint. On this card d is a short high stroke followed by a long stroke running below it (rows 1, 4, 6, 15, 22, S2, S3, S5 and, less extremely, 13); h and p are a tall stroke followed by a short one. So **d against h/p is decided by shape; only h against p rests on word sense** (p in *laphoz* and *nap*, h elsewhere). n is a level pair of about equal strokes. The one exception to the d shape is row 18 (uncertainty 3). The d of row 13 is less extreme than the others and is confirmed by the word (uncertainty 10).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1291/work/decode.py
```

It checks the SHA-256 of both `source/` images and both `work/hires/` originals, decodes the manual sign ledger `work/ledger.txt` (22 main rows, 6 rows on the former stamp position), and prints the literal text and the normalized text (`work/normalized.txt`). The ledger is a manual reading of enlarged crops, not OCR. The crop helper is `work/z.py`.

## Literal decipherment

{x} = value depends on word sense; {a?} = probable faint sign; [x] = restoration.

```
01 szeretettedesjolankam           15 edesemlegyenelne
02 egyetlenremenyemkivanom         16 zesselirantammert
03 hogy{a?}legjobbegessegbenes     17 jobbanszeretnekin
04 kedvebentalaljasoraim           18 kabbmin{d}{e+n}apirnimi{n}t
05 neharagu{j}onhogyijenrit        19 hogykenytelenvagyok
06 anirokdeugyelvagyok             20 ijenritkanirni
07 foglalvahogynemju               21 kivanokjomulatast
08 tokhozzamostsok                 22 szeretökedvessefer
09 katonavonatvaesugy              S1 istenve
10 elvagyokfglavahogy              S2 leedesem
11 aligvarohogyle                  S3 maradok
12 fekheehezalaphozis              S4 sirig
13 marnegyedszefogokhoz            S5 hukedves
14 zaazertkerem{m}agat             S6 s[e]fer{i}
```

## Hungarian (normalized)

Szeretett édes Jolánkám, egyetlen reményem! Kívánom, hogy {a} legjobb egészségben és kedvében találja soraim. Ne haragudjon, hogy ilyen ritkán írok, de úgy el vagyok foglalva, hogy nem jutok hozzá. Most sok katonavonat va[n], és úgy el vagyok f[o]gla[l]va, hogy alig váro[m], hogy lefekhe[ssek]. Ehhez a laphoz is már negyedsze[r] fogok hozzá. Azért kérem magát, édesem, legyen elnézéssel irántam, mert jobban szeretnék inkább mindennap írni, minthogy kénytelen vagyok ilyen ritkán írni. Kívánok jó mulatást. Szerető kedvese, Fer[i].

Under the stamp: Isten vele, édesem! Maradok sírig hű kedvese, Feri.

## English

My beloved sweet Jolánka, my only hope! I wish that my lines find you in the best of health and spirits. Do not be angry that I write so rarely, but I am so busy that I cannot get round to it. There are many troop trains now, and I am so busy that I can hardly wait to be able to lie down. Even this card I am setting about for the fourth time already. So I ask you, my darling, to be indulgent with me, for I would much rather write every day than be forced to write so rarely. I wish you a good time. Your loving sweetheart, Feri.

Under the stamp: Farewell, my darling! I remain, faithful unto the grave, your sweetheart, Feri.

## Slovak

Moja milovaná, sladká Jolánka, moja jediná nádej! Želám si, aby Vás moje riadky zastihli v najlepšom zdraví a nálade. Nehnevajte sa, že píšem tak zriedka, ale som taký zaneprázdnený, že sa k tomu nedostanem. Teraz je veľa vojenských vlakov a som taký zaneprázdnený, že sa sotva dočkám, kedy si budem môcť ľahnúť. Aj k tomuto lístku sa púšťam už štvrtýkrát. Preto Vás prosím, drahá, buďte ku mne zhovievavá, lebo oveľa radšej by som písal každý deň, než by som bol nútený písať tak zriedka. Želám Vám dobrú zábavu. Váš milujúci milý, Feri.

Pod známkou: S Bohom, drahá! Zostávam do hrobu verný, Váš milý, Feri.

## Uncertainties

Sign-level points:

1. **Row 3 `hogy{a?}legjobb`**: the gap between *hogy* and *legjobb* is wide enough for one sign and holds two faint grey marks one above the other, where a pale two-bar a would stand. They may be ink or staining. *Hogy a legjobb egészségben* is the better idiom, but the text reads without it. Probable, not certain.
2. **Row 5 `haragu{j}on`**: the sign after u is a horizontal bar with a stem above and a very short stem below, touching the x. By shape it lies between inverted T (j) and cross (f). Read j by sense: *haragujon* is a phonetic spelling of *haragudjon* (d not written). f gives no word.
3. **Row 14 `{m}agát`**: three strokes, the first with a crossbar (a correction or a pen slip). Read m by sense (*kérem magát*).
4. **Row 18 `min{d}{e+n}ap`**: one heavily overwritten sign, two heavy stems with two crossbars, read as e and n fused. Only one n of the compound can be present. The sign before it is tall-then-short, the shape of h/p and not of d; *mindennap* is not in doubt, and this is probably part of the same correction. Both calls are by sense.
5. **Row 18 `mi{n}t`**: the strokes after the second i are faint and could be counted as two or three (the i's crossbar runs into them). Read n by sense (*mint* + *hogy* in row 19 = *minthogy*).
6. **Row S6 `s[e]`, restoration**: the row starts with a right bowl s, then a gap covered by the remnant of the stamp and the postmark, then *fer…*. The main text writes *kedvesse* in row 22, and S5 ends *kedves*, so one hidden sign e gives the same form. This is the only restoration of a physically hidden sign; the other brackets supply letters the writer did not write (items 8 to 12).
7. **Row S6 final sign**: an unlooped hook, not the usual i sign. Read i by sense (*Feri*, the signature of HCP1216). Row 22 ends *Fer* with clean paper after r, so there the name is really cut short; the final i is supplied in brackets.

Writer's text, normalized editorially (the literal text is above):

8. **Row 9 `va és`**: *van* is written without n: chevron, two bars, then e with accent, s. Normalized *va[n]*.
9. **Row 10 `fglava`** = *foglalva* with o and l omitted; row 7 spells it fully. All signs are clear.
10. **Row 13 `negyedsze`**: the sign before `sz` is a short high stroke and a longer stroke below it, as d, though with a ratio of lengths (about 0.75–0.83) less extreme than the cleanest d's (0.25–0.5). The shape favours d and the word settles it: *már negyedszer fogok hozzá*, "I am setting about it for the fourth time already", with only the final r omitted.
11. **Row 11 `varo`**: the writer left out the final m; there is no three-stroke sign between o and the h of *hogy*. Normalized *váro[m]*.
12. **Rows 11–12 `lefekhe`**: the sign after *fek* is plainly tall-then-short, so h or p and not d. I read *lefekhe[ssek]* ("that I may lie down"), cut short by the writer, and the next sentence starts with *ehez*. The ending is not on the card. The alternative first proposed, *lefek[üdjek]. De ehhez…*, would need this sign to be an off-shape d, and it is the only sign in the sentence that would need that. The English and Slovak hardly change either way.
13. Other spellings: *egessegben* → egészségben, *ijen* → ilyen, *ritán* (row 5–6) → ritkán (row 20 has the k), *ehez* → ehhez, *kedvesse* → kedvese, *hu* → hű (no double mark seen). Most accents are not visible and are supplied. Row 1 `szeretett`: the bars of the first letters are faint at the top of the card, but the word is secure.

Context: the sender is taken to be the Feri of HCP1216 and sister cards only from the matching first name, closing formula, key and addressee. The address in plain writing reads, as far as I can make out, *Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás*; the first word is overlaid by the postmark and is not secure. The card has two postmarks. The round date stamp in the middle shows …SZAPÁTI (Jászapáti) 913 AUG 31. A second, larger strike sits at the stamp position, with `BU…` and `913` legible; its place and day are not. So 31 August is the date of the Jászapáti strike, and I cannot say whether that is the day of sending, transit or arrival. The printed picture-side verse is ordinary Hungarian, not ciphertext. I make no claim about what the troop trains or the writer's job were.

## Why it is correct

- The key transfers unchanged from finished cards (with the d shape stated more exactly for this hand) and turns every sign into Hungarian, and no sign is left without a value. Faint or damaged signs are listed under Uncertainties.
- The text is coherent, idiomatic Hungarian with formal address (*találja, haragudjon, kérem magát*), and has one continuous argument: an apology for writing rarely, the reason, and a request for indulgence.
- Repeats decode identically: *hogy* ×6, *el vagyok f…a* ×2, *ilyen ritkán* ×2, *kedves-* ×3, *édesem* ×2, *szeret-* ×3.
- The closing *sírig hű kedvese ... Feri* matches HCP1216.

## Response to review 1

Verdict REVISE. I checked each finding on `review/work/` crops and on my own new crops of the hires address scan (rows 3, 4, 11 and 18, and the stamp corner) and accept all eight. No sign's key value changed, and the message and both translations stand apart from one clause reworded to match (*lefekhe[ssek]*). `work/ledger.txt`, `work/decode.py` and `work/normalized.txt` are updated, and the reproduction command runs with all hashes OK.

1. **Row 11, m not on the card: fixed.** On a crop of the whole row, o is followed directly by the tall+short h and the next o. My earlier m was forced from context. Literal `aligvarohogyle`; normalized *váro[m]* (uncertainty 11). The claim "the only restoration on the card" now applies only to physically hidden signs.
2. **Row 13, n to d: fixed.** The sign is a short high stroke and a longer one below it; the two n's of the card are level pairs. Reading *negyedsze[r]*. The superfluous syllable in `négy(en)sze[r]` is gone, and that reading meant "four times", not the "fourth time" of my own translation. The review's caveat about the less extreme length ratio is recorded (uncertainty 10).
3. **d is not a homograph of h/p: fixed.** The key section now gives short-then-tall for d and tall-then-short for h/p, and only h/p rests on word sense. Row 12: the sign after `fek` is tall-then-short, so I changed the ledger to h and the reading to *lefekhe[ssek]. Ehhez a laphoz is…*. The review offered this as an alternative to be listed beside the old one; I went further and made it the main reading, because it needs no off-shape sign and *lefekhet* is the regular potential form of *lefekszik*. *lefek[üdjek]. De ehhez* is kept as the alternative (uncertainty 12). Row 18: the sign is now `{d}` by sense and is part of uncertainty 4.
4. **Row 4, omitted l: fixed.** The crop shows gamma, two bars, wave, two bars, wave, inverted T: `talalja`. The ledger, literal block and spelling list are corrected; *talaja* was my error, not the writer's.
5. **Row 3, faint sign: entered** as `A?`, displayed `{a?}`, with uncertainty 1. My enlargement (7x) shows the two grey marks; I cannot tell ink from staining either, so it stays a probable sign.
6. **Row 21, slash: fixed.** The slash is the stem of the t, whose bar starts at its top. The token, `{|}` and the old uncertainty item are removed. Literal `mulatast`.
7. **Second postmark: added** to the context paragraph, with the consequence for the date. I could read no more of it than the review did.
8. **Knock-on edits: done** in the ledger comments, literal block, normalized text, the "Why it is correct" section, NOTES.md and both translations.
