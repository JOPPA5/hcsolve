# HCP1282 — Feri to Jolánka Tóth: news of Ilona and Irma, a word of honour

**Status: complete sign-by-sign reading, revised after review 1. One word in rows 8-9 and one in row 19 are not understood (uncertainties 1 and 2); the rest reads.** Solver: Claude Opus 5.5, 2026-11-01. No earlier work on this number. The portal shows *Not solved* and attaches no transcription or solution; no published solution was found or used. Key taken from the finished family cards, chiefly HCP1216 (legend) with HCP1301, HCP1243.

## Cipher type and key

**Type (2026-11-03): MASC + Steganography.** The cipher text is MASC; the closing in clear is hidden in the stamp box under the (now lifted) stamp, see "Stamp-box message (2026-11-03)".

Hungarian, monoalphabetic substitution with invented signs, the Jolánka family key unchanged (same recipient, same hand and red ink, "Feri"). Sign classes as in `ciphers/hcp-1216/SOLUTION.md`: a two bars, b six, c left bowl, d long+short stroke, e three bars, f cross, g open loop with descender, h/p tall stroke + companion (near-homographs), i dotted crossed curve, j inverted T, k section mark, l wave, m three strokes, n two strokes, o cursive loop, r F-like, s right bowl, t gamma, u x-cross, v chevron, y low descender, z crossed diagonal, gy joined.

Observed on this card, not in the legend: (a) a plain cross stands twice where the sense needs **j** (*újság*, *gondoljön*); (b) the capital of *Ilona* and *Irma* is either a clear cursive capital I (cf. the J of "Jolanka" in the address) or the family y sign used as a capital (the shapes are close, and the names stand either way); (c) *k* looks like a cursive S; (d) three short free strokes (rows 7, 10, 14) and one blob (row 12) stand at sentence breaks and carry no letter. They are recorded as `|` and `·`, and are most likely punctuation; only their position suggests that.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1282/work/decode.py
```

It checks the SHA-256 of all four images, decodes `work/ledger.txt` (manual sign transcription, one token per sign, 21 rows; `[t]`, `[e]` mark signs restored under the row 19 blot) and prints `work/normalized.txt`. The ledger was made by eye with knowledge of the key and the emerging sense, so it is not blind. Crops: `work/crop.py`, `work/crops/`.

## Literal decipherment

```
01 kedvesegyetlenremenyem        12 lökeajövőtitka·a
02 kivanomhogyalegjobb           13 miminketiletmaskülöm
03 kedvebentalaljaso             14 benegessegekvagyunk|en
04 raimhogytelikideje            15 dezintulboldognaker
05 miujsagönnökfelemi            16 zemmagammertbizel
06 köztünknagyvaltozas           17 metbiromonnekedesem
07 törtent|Ilonaholnap           18 becsületszavamadomiras
08 megyvarnielőszörvar           19 banishogynemrbennemis[t][e]n
09 iegyelokelövarroda            20 veleedesemgondoljön
10 ba|Irmapedigmasamod           21 neharamakiönreepedőszivvelgondol
11 leszhogymileszbelő            stamp box, in clear: see below
```

## Hungarian (normalized)

Kedves egyetlen reményem! Kívánom, hogy a legjobb kedvében találja soraim. Hogy telik ideje? Mi újság önnök felé? Mi köztünk nagy változás történt. Ilona holnap megy varrni, először vári {?} egy előkelő varrodába. Irma pedig masamód lesz. Hogy mi lesz belőlök, [ez] a jövő titka. Ami minket illet, máskülömben egészségek vagyunk. Én de [e]zintúl boldognak érzem magam, me[r]t bizelmét bírom Önnek, édesem. Becsületszavam adom írásban is, hogy nem {r} bennem. Is[te]n vele! Édesem, gondoljön néha rám, aki Önre epedő szívvel gondol.

In clear in the stamp box: csókolom számtalanszor hű [lines 4-6 tentative] Feri.

## English

My dear only hope! I wish that my lines find you in the best of spirits. How is your time passing? What news on your side? Among us a great change has happened. Tomorrow Ilona goes to sew; first [*vári*: not understood] to a distinguished dressmaking workshop. And Irma will be a milliner. What will become of them is the secret of the future. As for us, otherwise we are healthy. But from now on I feel happy, because I have your trust, my sweet. I give my word of honour in writing too, that not [one word missing or not understood; a guess: that you will not be disappointed] in me. God be with you! My sweet, think sometimes of me, who thinks of you with a yearning heart.

Stamp box: I kiss you countless times. Your faithful [word uncertain], Feri.

## Slovak

Moja milá jediná nádej! Želám si, aby Vás moje riadky našli v najlepšej nálade. Ako Vám plynie čas? Čo je nové u Vás? U nás sa stala veľká zmena. Ilona ide zajtra šiť; najprv [*vári*: nerozumieme] do významnej krajčírskej dielne. A Irma bude modistkou. Čo z nich bude, to je tajomstvo budúcnosti. Čo sa nás týka, inak sme zdraví. Ale odteraz sa cítim šťastný, lebo mám Vašu dôveru, drahá. Dávam čestné slovo aj písomne, že nie [jedno slovo chýba alebo mu nerozumieme; odhad: že sa nesklamete] vo mne. S Bohom! Drahá, myslite občas na mňa, ktorý na Vás myslí s túžiacim srdcom.

V rámčeku na známku: Bozkávam Vás nespočetnekrát. Váš verný [slovo neisté], Feri.

## Uncertainties

1. **Row 19, `hogy nem r bennem`.** The F-like sign after *nem* and *bennem* are both clear (`review/work/z19m.png`), but the clause has no verb and {r} makes no word. It may be a false start or an abbreviation. "That you will not be disappointed in me" is what the context suggests, and it is a guess only.
2. **Rows 8–9, `var|i`.** The signs are secure, the word is not understood. It may be a slip for *varni* (the writer's own spelling of *varrni* in the same row), or the adjective *vári* ("of the Vár"); neither is proven, so the translations leave it open. The first *varni* is normalized *varrni* (one r written).
3. **Rows 9–10, `varroda|ba`.** The d rests on the sign class and the sense; d/h/p are near-homographs. Its long stroke runs into the right leg of row 8's v above it, and the short stroke is thick. The a after it shows two bars, with ink drips and the ruled line through it; a third bar is not visible. The sign after b in row 10 also shows two bars (`review/work/z10.png`), so it is a, not e.
4. **Rows 18–19 blot.** Of the final s of *írás* only the top hook shows. *Is[te]n vele* is a restoration, probable and not proven: i and the first part of s are visible; t rests on a stem leaving the blot down and to the left, as gamma stems do; e on two bars, a top bar falling inside the blot; n is visible. The sentence end before a gap and the family's usual close support it. Rejected alternative: *is van vele*, which makes no sense. The right leg of a v would run the other way.
5. **Rows 14–16, `en | dezintul`.** Normalized *Én de [e]zintúl*. The z is a heavy forked stroke, not a clean crossed diagonal (`review/work/q15.png`). *ezentúl* needs two emendations (e added, i for e). *szintúl* ("likewise") is a possible alternative; the sense "I feel happy" is not affected.
6. **Crosses as j**, rows 5 and 20: value rests on word sense; the family value f gives no word. The row 20 one may be a sloppy inverted T.
7. **Row 10 `masamod`** (*masamód*, milliner): the sign after m has a small extra arc under it, which may be a third bar or a mark; two bars read as a, on sense. **Row 21**: the *h* of `neha` is a heavy sign plus a thin stroke with a mark above; *néha rám* rests on sense. The heavy sign before *ki* is read a (e gives *eki*). An ink blob after *önre* is no letter. **Row 16 `bizel`**: i under a pink wash, visible.
8. Row 8 first sign m: one stroke is under the printed "Brömüra" imprint.
9. Writer's spellings kept and normalized: *met* (mert), *bizelmet* (bizalmát), *egessegek* (egészségesek), *ilet* (illet), *e a* (ez a), *belőlök*, *máskülöm-ben*, *önnök*. h/p and d/n calls throughout rest on word sense (*holnap, pedig, epedő*). Acutes are not transcribed. The first o of *először* carries one tick and is taken as ő; the second has two dots.
10. **Stamp box (clear Hungarian, not cipher)**: written under the printed P.R.A. wreath. *csókolom számtalanszor* and *Feri* are clear, *hű* is good. Lines 4–6 were read with the teal print subtracted (`work/crops/stamp_red.png`). What follows *hű* is not secure: line 5 begins with a letter closer to m/n than r, and line 6 has two letters with an ascender before *Feri*. A form of *szerelmes* or *kedvese* (HCP1216) can be neither confirmed nor excluded, so the translation leaves it open.
11. Postmark Jászárokszállás, apparently 11 April (file name "-04-11"); year illegible. The picture side has a printed verse only. The identity of Ilona and Irma is unknown.

## Why it is correct

The family key, unchanged, turns all 21 rows into Hungarian, with every letter sign given a value; only the two words of uncertainties 1 and 2 stay without sense. Long specific words come out unforced: *becsületszavam, változás, varrodába, masamód, előkelő, boldognak, epedő szívvel*. Repeats agree (*hogy* ×4, *gondol* ×2, *lesz* ×2, *édesem* ×2). The closing *epedő szívvel* also occurs on HCP1301, the sender Feri on HCP1216, Ilona on HCP1259 and HCP1265, and *Isten vele* on HCP1216 and HCP1259.

## Response to review 1

Verdict REVISE. All ten findings were checked on the reviewer's crops and accepted; `work/ledger.txt`, `work/normalized.txt` and `work/decode.py` were changed and the command re-run (all four hashes OK, output as above).

1. **`varrodába`: fixed.** `review/work/q9.png` shows the short thick stroke plus the long stroke and two bars. I go one step further than the review: its own decoder still gives `be` in row 10, but the sign after b there has only two bars (`review/work/z10.png`, `b4L.png`) against three in the *pe* of *pedig* on the same row. So the ledger now has `B A`, and *varrodába* is literal, with no vowel-harmony slip to explain. Uncertainty 3 and the word list updated.
2. **Phantom K: fixed.** `review/work/z14.png` shows `n | k | short stroke | e | n`. Now *vagyunk. Én*; the invented "[S]" is gone. The strokes in rows 7 and 10 (`z7.png`, `z10.png`) and the blob in row 12 (`work/crops/r12R.png`) are in the ledger as tokens `/` and `*`, and the claim "no sign left without a value" is withdrawn.
3. **`Is[te]n vele`: adopted.** On `z19a.png` and `z19b.png` the stem slants as the review says, and two bars show below the blot. My earlier argument from channel separation proved nothing. Marked as a restoration in the ledger (`[T] [E]`), with *is van* as the rejected alternative.
4. **Uncertainty restated: done** (uncertainty 1, translations, status). The word stands alone and the rest reads, but the guess at sense stays labelled as a guess.
5. **`vári`: fixed.** No verb gloss any more; marked not understood, with both candidates named as unproven.
6. **Diacritics row 8: fixed.** Ledger now has `O"` and `O:`, literal *először*.
7. **Capital: softened** in the key section and the ledger legend.
8. **Row 15 `z`: disclosed** with *szintúl* as an alternative (uncertainty 5).
9. **English of the close: fixed.** *Ami minket illet* is now the normalized spelling.
10. **Stamp box: fixed.** The inconsistent *sze[r]elmese* is withdrawn; lines 4–6 are stated as tentative (uncertainty 10).

The changes touch a handful of words and leave the key and the content of the letter as it was, so the card goes to FINAL and not to a second review round.

## Stamp-box message (2026-11-03)

Audit by Claude Opus 5.5 on the human's order. The stamp is lifted: the box shows the printed P.R.A. wreath, the edge of the Jászárokszállás postmark at its right, and six short lines of the same red ink, written where the stamp sat. The writing is plain Hungarian, not cipher signs. Crops of the hi-res original: `work/stamp-2026-11-03/` (`box_2x.png` whole box; `l1`–`l6` lines at 5–7x, `*_rg.png` with the teal print suppressed by red-minus-green).

Literal, line by line:

```
1 csokolom
2 szamta
3 lanszor
4 hű s?.. -        (hyphen at line end is clear)
5 ?e?[m/n]es       (first letter two arches, m/n-like; -es clear)
6 ?? Feri          (two letters: an s-like sign, then a letter with an ascender)
```

- Normalized Hungarian: *Csókolom számtalanszor. Hű [unread word, broken by a hyphen over lines 4–5] [two unread letters] Feri.*
- English: I kiss you countless times. Your faithful [unread], Feri.
- Slovak: Bozkávam Vás nespočetnekrát. Váš verný [neprečítané], Feri.

What stays unread: the word after *hű* (lines 4–5) and the two letters of line 6. The new observation is the hyphen at the end of line 4, so lines 4–5 hold one word ending in *-es*, and the letter count fits *sze-relmes* ("lover", *hű szerelmes* "faithful lover"). It is not adopted: line 5's first letter has two arches like m/n and does not match this writer's r (closed loop, as in *lanszor*), and the line 4 letters sit on the teal wreath. The family formula *hű kedvese* (HCP1216) does not fit the *-es* ending of line 5. Line 6 may be an abbreviation (e.g. *s.k.*), not proven. So the clause after *hű* stays unread; *csókolom számtalanszor* and *Feri* are secure. The stamp text is read by eye; `work/decode.py` and the ledger do not cover it and were not changed.

Type note (2026-11-03): writing under the lifted stamp, so the card is typed **MASC + Steganography** (register entry updated, type field only).
