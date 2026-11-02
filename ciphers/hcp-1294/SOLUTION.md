# HCP1294 — Feri to Jolánka Tóth: thanks for her letter, "why take on so much work?"

**Status: PARTIAL. Every sign of the card is transcribed and has a value, and 200 of 209 signs give a clear message, but one stretch of 9 signs in row 8, literally `oszeholad`, is read sign by sign and NOT understood as a word. It is reported literally and not translated, and the clause it stands in cannot be fully translated. No register entry is written for this card.** By Claude Opus 5.5, 2026-10-30. No earlier work exists on this number. Portal status Not solved, no attached transcription or solution; the orchestrator's AI-register check (2026-10-30) found no record. No published solution was seen. Revised 2026-11-02: still PARTIAL, the word stays unread; see "Revision 2026-11-02".

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family, same key as finished cards HCP1212, 1213, 1216, 1217, 1218, 1243, 1301 (see the sign table in `ciphers/hcp-1216/SOLUTION.md`). The key was taken from those cards, not derived here; this card confirms it on every value it uses:

a two bars, b six, cs opposed bowls, d short tick + long stroke, e three bars, g open loop with descender, h/p tall stroke + short tick (one homograph), i crossed curve with dot, j inverted T, k section mark, l wave, m three short strokes, n two short strokes, o cursive loop, r F-like, s right bowl, t gamma, u plain cross, v chevron, y low descender, z crossed diagonal with long tail. Sz is written s + z. Dots or two short strokes over o give ö/ő.

Not used on this card: c alone, f, plain-letter stretches.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1294/work/decode.py
```

It checks the SHA-256 of the two source files and the two hires originals, decodes the ledger `work/ledger.txt` (one token per written sign, 15 rows, 209 signs) and prints the literal rows and the normalized text. The ledger is a manual transcription from enlarged crops (`work/crop.py`, `work/zoom.py`, output in `work/crops/`), not OCR.

## Literal decipherment

```
01 kedvesjolankam
02 becsessoraitkö
03 szönettelmegkap
04 tamsajnalatalol
05 vasomolysokat
06 dolgolgozik
07 minekvalalannyi
08 munkatoszeholadȯk
09 vetlenelmegyek
10 barnagyonroszidö
11 vancsakholnaprajo
12 idölennenajdszo
13 valbövebbenisten
14 veleaviszontlatas
15 ra
```

Plain Latin under the (lost) stamp, not enciphered: `csokolja szamtalan szor hű[n?] kedvese Feri`. Address side, plain: *Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás*. The printed picture-side verse (*Szebb a pipacsos mezőn…*) is ordinary Hungarian, not ciphertext.

## Hungarian (normalized)

Kedves Jolánkám! Becses sorait köszönettel megkaptam. Sajnálat[t]al olvasom, oly sokat dolgozik. Minek vál[l]al annyi munkát ‹oszeholad› okvetlen elmegyek, bár nagyon ros[s]z idő van, csak holnapra jó idő lenne. Majd szóval bővebben. Isten vele, a viszontlátásra.

Under the stamp: Csókolja számtalanszor hű[n?] kedvese, Feri.

## English

My dear Jolánka! I received your esteemed lines with thanks. I read with regret that you work so much. Why do you take on so much work ‹oszeholad, not understood› I shall certainly go, although the weather is very bad; if only there were good weather tomorrow. More by word of mouth later. Farewell, until we meet again.

Under the stamp: Kissed countless times by your faithful sweetheart, Feri.

## Slovak

Moja milá Jolánka! Vaše vzácne riadky som s vďakou dostal. S ľútosťou čítam, že tak veľa pracujete. Načo si beriete toľko práce ‹oszeholad, nezrozumené› určite pôjdem, hoci je veľmi zlé počasie, len keby bolo zajtra pekne. Ostatné podrobnejšie ústne. S Bohom, dovidenia.

Pod známkou: Nespočetnekrát Vás bozkáva Váš verný milý, Feri.

## Uncertainties

1. **Row 8 `oszeholad` (main open point).** The signs are clear on `work/crops/z8.png` and `z8b.png`: loop o, s, tailed z, three bars e, tall stroke + short tick (h/p), loop o, wave l, two bars a, tick + long stroke d. The first loop has an extra lead-in stroke from the left, which fits no sign in the key. No Hungarian word was found for this string. The word boundary is also an assumption: the following `ok` is taken into *okvetlen*, which is what makes row 9 a phrase, so the string might end differently. The h/p, d/n and o/ö variants were tried (`szep…`, `…olan`) and gave nothing. *Ha szabad* ("if free") and *leszaladok* ("I run down") were considered and rejected: they do not match the signs. What the word does in the sentence is not known, and it may attach in either direction: *Okvetlen elmegyek* is a complete sentence on its own, so the word could close the remark about too much work as well as open the clause about the trip. The normalized text therefore puts no punctuation on either side of it. Leads, none adopted (tests in `work/row8_test.py`; all rest on word sense, none on the signs):
   - **Prefix *össze-*.** This writer spells *össze* with one sz: HCP1288 row 22 has literal `ö s z e h ö ? z e h o z`, normalized *összehoz*. So `osze-` is probably *ösze-* = *össze-*, with the ö dots omitted or perhaps replaced by the lead-in stroke on the first loop. *Összehoz* itself does not fit: the sign after o is a clear wave l, not z.
   - **Tail *holnap* ("tomorrow").** `holad` is one letter short of *holnap* with a final d for p; compare `csak holnapra` three rows below, and literal `holna` on HCP1319. It would give "… tomorrow I shall certainly go", which suits the sense well, but it needs two slips (n dropped; d, whose tick is on the other side, for p), and it leaves `osze` unexplained.
   - ***Összeolvad* ("melts together")**, perhaps thinking of the thaw and the bad weather: needs a dropped v and an unwanted h.
   - The family vocabulary (6149 distinct word forms in the Jolánka SOLUTION.md files) has no closer match. No Hungarian dictionary was available.
2. **Dot over the last loop of row 8** (`ȯ`): a single dot stands over the o of *ok-*. No word needs ö here, and the normalization ignores it. The dot under the k at the end of row 8 is no evidence of punctuation: most k-signs on this card have a dot just under them (7 of 11, by the reviewer's count: row 1 second k, rows 2, 3, 5, 6, row 8 last k, row 9), rows 2, 3 and 6 with no i or ö below, so it is a habit of this writer with k. In rows 5 and 9 two dots stand there, one of the k and one the i-dot of the row below.
3. **Word-sense calls among near-homographs.** h vs p: *megkaptam* (row 3), *holnapra* (row 11, both h and p) are fixed by the word, not the shape; in `oszeholad` it is undecided. d vs n: the n of *minek* (row 7) and of *-len* in *okvetlen* (row 9) are written with unequal strokes, a shape leaning to d; n is by word sense. These are marked `n*` in the ledger.
4. **Row 12 `najd` → *majd*.** Two strokes stand before the bars: `n`, not the three of m. The normalization to *majd* ("later") is a correction of a writer's slip (one stroke short), resting on *majd szóval bővebben*, a natural phrase; the alternative is not excluded by the pixels of that one sign.
5. **Row 12, j under an ink blot.** The blot has the inverted-T outline, read as j; this is a reading of a damaged sign, and the word sense agrees.
6. **Row 14, a under a blot.** The upper bar is under the blot; its base and the lower bar remain. Word sense (*viszontlátásra*) agrees.
7. **Row 10 and row 13, damaged but legible.** The a of *bár* has its lower bar swollen into a blot, and the ö of *bővebben* is thickened or overwritten, with its two strokes clear above. Both still read as stated, and word sense agrees.
8. **Row 5 `oly`**: the wave and the y are joined; *oly sokat* is taken as written. The alternative *(h)ogy sokat* would need the writer's separate g + y sign (rows 9, 10), so it is not preferred. The sense is the same.
9. **Writer's spellings, normalized:** `dolgolgozik` → dolgozik (a repeated `-olg-`, as written), `valal` → vállal, `sajnalatal` → sajnálattal, `rosz` → rossz, *el megyek* written as usual. Acutes are mostly invisible and are supplied; ö/ő marks are transcribed where seen (rows 2/3, 10, 12, 13). Row 12 `szo` is normalized *szóval*.
10. **Under the stamp** the third line ends in `hű` plus a short further stroke at the torn edge, so `hűn` is possible. The stamp was removed, the paper is torn there, and the text is in plain Latin.
11. The date 1912-03-26 is the portal's; the postmark was not used to verify it. The sender's cancel is partly lost.

## Why it is correct

- The key comes unchanged from the finished family cards and turns all 15 rows into Hungarian with no sign lacking a value, with the exception of the row 8 word, which has values but no meaning.
- 200 of 209 signs make idiomatic text in the family's voice. *Becses sorait köszönettel megkaptam* parallels HCP1212, and *okvetlen … megyek* parallels HCP1301. The plain signature Feri and the addressee agree with the family.
- Sign behaviour is consistent: *idő* twice, with the two strokes each time; the opposed-bowls cs in both *becses* and *csak*; z in *köszönettel, dolgozik, rosz, szóval, viszont* always the tailed cross, u in *munkát* the plain one.
- The failed word in row 8 was left literal rather than forced.

## Response to review 1

Verdict REVISE; all six findings are addressed. `python3 -I ciphers/hcp-1294/work/decode.py` was re-run after the fixes: four SHA-256 checks OK, 209 signs, no sign without a value. No sign of the ledger changed. The only change to the text is that the normalization has lost the question mark before the row 8 word (finding 3).

1. **Card partial but not labelled (major): fixed.** The status line now says PARTIAL, *Why it is correct* names the exception, and no `register-entry.txt` is written, as README step 7 requires.
2. **Spelling lead *össze-* (major): tested, recorded, not resolved.** I agree with the lead. `work/row8_test.py` compares the word and the tails `holad/polad/holan/polan` with the family vocabulary. Only the *össze-* forms of HCP1288 come near, and *összehoz* is excluded by the clear l, re-checked on `work/crops/z8b.png`. The prefix and two further leads (*holnap*, *összeolvad*) are in uncertainty 1, none adopted. I did not force a reading.
3. **Unsupported function (minor): fixed.** Uncertainty 1 now says the attachment is unknown in both directions; the normalized text and the translations have no punctuation at the word.
4. **Dots under k (minor): fixed.** Uncertainty 2 is rewritten and the claim in NOTES.md corrected. I checked the row 9 case on `review/work/crops/r09_2.png`: two dots stand there, as the reviewer says. The count of 7 of 11 is the reviewer's; I did not recount every k.
5. **Undisclosed damage (minor): fixed.** New uncertainty 7, checked on `work/crops/r10_a.png` and `r13_a.png`.
6. **Ledger header (minor): fixed.** The header now lists the tokens actually used (H, P, plain d).

## Revision 2026-11-02

Second attempt by Claude Opus 5.5, ordered by the human. Status unchanged: PARTIAL. No sign of the ledger, no reading and no translation changed. The only unread passage is row 8 `oszeholad`.

What was tried:

1. **New crops from the original** (`work/crop2.py`, `crop3.py`, `crop4.py`, output in `work/crops2/`): every row at full scale, row 8 in the green channel with contrast at 3x, and the stamp box in the blue channel at 2x.
2. **o against i, a new test.** The second loop of the word has a narrow slit, so it might have been the i-sign, and the dotted sign before the k might have been a dotted i (which would give `-hilad` or `-adik`). The gallery `work/crops2/loops.png` compares five o and five i from this card with the three loops of row 8. On this card o has a round arch and a tail ending in a downward hook, and i has a straight top and a straight tail. All three row 8 loops have the arch and the hook, so all three are o. The earlier reading stands, independently of the old ledger.
3. **The other signs of the word** were re-read and agree: right bowl s, tailed z, three bars e, tall stroke + short (h/p), wave l, two bars a, short tick + long stroke d. The final sign leans to d but n is not excluded by shape alone. The lead-in stroke on the first loop is real and separate in origin from the t before it. I cannot tell whether it is a dash, a stray pen stroke or a mark on the o.
4. **Family formulae.** "okvetlen lemegyek" usually has a time word before it (HCP1255 *vasárnap*, HCP1264 *csütörtökön*), or a place (HCP1264, 1276 *a mulatságba*). No day or place name fits these signs. HCP1254, dated one day later, begins *szerencsésen megérkeztem*, so the trip probably took place, but it does not mention this word. A search of all family SOLUTION.md files for the stems `szehol, sepol, holad, polad, ehola` found only this card.
5. **New leads, none adopted** (all rest on word sense):
   - A verb in -ad, third person as the formal address of *dolgozik, vállal*: "why take on so much work, you will [wear out]". This shape suits the sentence, but the verbs that carry that sense do not match the signs: *összeroskad* (r, s, k against h, o, l), *összehorpad* (no rp), *összeomlad* (h extra, m missing). *Összehullad* would need o for u and one l, and I could not confirm the word exists.
   - `o szép olan`, with the h/p sign as p, d as n, and *olan* for *olyan*: "[?] nice like that". The writer spells this word with y or j elsewhere, and the first o stays unexplained; *ha szép* ("if it is fine") would suit the weather talk but h, a are not on the card.
   - *e hó* ("this month") inside the string: nothing usable follows it.
6. **Dictionary check.** No Hungarian word list exists on this machine, and one web search for *összehalad, összeholad, összehullad* found no entry for any of them. That is no proof of absence; the regional dictionary ÚMTSz. was not consulted.

Why this stays partial: the rule allows a card with an un-understood word only if the word is alone, and it is not established here that the word is alone. The string has no divider, the prefix lead suggests a compound or two words, and its function in the sentence is unknown, so it may be a clause of its own. Nothing in the reading has improved since review 1, so there is no ground to raise the status. No DONE2 and no register entry.

Under the stamp, the blue-channel crop confirms `csokolja / szamtala[n] / szor hű… / kedvese / Feri`; the torn end of line 3 stays as in uncertainty 10.

## Credit

Solver: Claude Opus 5.5. The family key was established by earlier work on the sister cards (OpenAI GPT solver, GPT-6 / GPT-6 Astra / GPT-6.1 Sol; HCP1216 completed by Claude Opus 5.5).
