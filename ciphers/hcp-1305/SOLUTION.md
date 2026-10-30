# HCP1305 — Fery to Jolánka Tóth: the Catholic Young Men's ball on the 20th

**Status: the whole card is read, with every sign given a value; one word (*tustkantek*, row 15) is transcribed but not understood, and a few small points rest on word sense (see Uncertainties). Review 1 verdict REVISE; findings addressed below, 2026-10-30.**

Credit: the whole reading is by Claude Opus 5.5 (2026-10-30), from the key of the finished Jolánka cards (HCP1216 and sisters, whose earlier work is by the OpenAI GPT solver and Claude Opus 5.5). There was no earlier work on this number. The portal shows *Not solved* and attaches no transcription or solution; no published solution of this card was found or used.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" family key, unchanged. Sign classes are those in `ciphers/hcp-1216/SOLUTION.md`:

two bars a · six b · left bowl c · long stroke + short tick d · three bars e · upright cross f · open loop with descender g · tall stroke + short tick h/p · dotted crossed curve i · inverted T j · section mark k · wave l · three strokes m · two strokes n · cursive loop o · F-like r · right bowl s · gamma t · plain cross u · chevron v · low descender y · crossed diagonal with tail z.

Dots over o/u give ö/ü; a tick over a vowel gives the acute (often absent). On this card *gy* and *ny* are written as two signs (g+y, n+y), not with the joined gy sign. "20 án", "Koth. Leg." and the address are in plain Latin script. The bars are the main reading risk: the third bar of e often sits far below the other two.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1305/work/decode.py
```

It checks the SHA-256 of both scans in `source/` and both originals in `work/hires/`, decodes the sign ledger `work/ledger.txt` (hand transcription from enlarged crops, not OCR) and prints the literal rows, then `work/normalized.txt`.

## Literal decipherment (as printed)

```
01 cszeretetedesjo              12 korlemivelakor
02 lankamkivanomhogy            13 akarjolánkahest
03 alegjobkedveben              14 remigydazénre-
04 talaljasoraimhogy            15 menyeimtustkantek
05 mulatharasztin               16 meginthétfonéj
06 esmiujsagmagok               17 jelvoltegykis
07 feléamam{a|e}haza            18 tüzünkismostmastnemírhatokmint
08 jöttemartudatom              19 hogyirjonmagaisistenveleaviszont
09 édesemhogy[Koth.Leg.]egy-    20 l{a|e}tasra  (up the right edge)
10 letimulatság[20án]           stamp: üdvöz / lome / tavol / bol / hüked / vesefery
11 leszamielégrocz
```

## Hungarian (normalized)

Szeretet[t] édes Jolánkám! Kívánom, hogy a legjob[b] kedvében találja soraim. Hogy mulat Harasztin? És mi újság magok felé, a mama haza jött-e már? Tudatom, édesem, hogy Kath. Leg. egyleti mulatság 20-án lesz, ami elég ros[s]zkor le[sz?], mivel ak[k]or akar Jolánka Pestre, mi így d[e] az én reményeim [tustkantek] megint. Hétfőn éjjel volt egy kis tüzünk is. Most mást nem írhatok, mint hogy írjon maga is. Isten vele, a viszontlátásra.

Under the stamp: Üdvözlöm e távolból. Hű kedvese, Fery.

Address (plain script, not enciphered): Szépreményű Tóth Jolánka úrleánynak, Jász Árokszál[l]ás.

## English

My beloved sweet Jolánka! I wish that my lines may find you in the best of spirits. How are you enjoying yourself at Haraszti? And what is new over your way, has mother come home yet? I let you know, my sweet, that the Catholic Young Men's Association ball will be on the 20th, which is rather badly timed, since Jolánka means [to go] to Pest then, so my hopes [word not understood; sense unknown, perhaps something like "came to nothing"] again. On Monday night we had a small fire as well. I cannot write anything else now, except that you should write too. God be with you, until we meet again.

Under the stamp: I greet you from this distance. Your faithful sweetheart, Fery.

Address: To the promising Miss Jolánka Tóth, Jászárokszállás.

## Slovak

Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky našli v tej najlepšej nálade. Ako sa zabávate v Haraszti? A čo je nové u Vás, vrátila sa už mama domov? Oznamujem Vám, drahá, že zábava Katolíckeho spolku mládencov bude 20., čo je dosť nevhodne, lebo vtedy chce Jolánka [ísť] do Pešti, takže moje nádeje [slovo nepochopené; zmysel neznámy, možno niečo ako „vyšli navnivoč"] zase. V pondelok v noci sme mali aj malý požiar. Teraz nemôžem napísať nič iné, len aby ste napísali aj Vy. S Bohom, dovidenia.

Pod známkou: Pozdravujem Vás z tejto diaľky. Váš verný milý, Fery.

Adresa: Nádejnej slečne Jolánke Tóthovej, Jászárokszállás.

## Uncertainties

Everything is transcribed as written; the normalization is editorial.

1. **Row 15 `tustkantek` is not understood.** All ten signs are clear: t u s t k a n t e k, with no dots on the u and two bars after k. It is no Hungarian word I can identify. Its sense is unknown. Its place in the sentence (*reményeim … megint*, "my hopes … again") would fit something like *füstbe mentek* ("went up in smoke") or *tönkrementek* ("were ruined"), but each needs several signs changed, so these are guesses at the sense only, and neither is in the plaintext. Word division with *megint* is also open: *… megint.* or *Megint hétfőn …*.
2. **Row 5 `harasztin` → *Harasztin*.** All signs are clear, and the F-like r has both arms (`work/crops/x5.png`). The sign is the h/p sign of *hogy*, read h, so no letter is changed. It is taken as the place name Haraszti with the locative -n, "at Haraszti". The capital and the identification as a place name rest on word sense; which Haraszti is meant cannot be shown (Dunaharaszti in Pest county is one example). Sister card HCP1310 row 18 has `darasztin`, with d as the first sign, which its solver gives as a probable parallel: that supports one recurring name but does not settle it.
3. **Row 13 `hest` → *Pest*:** p by word sense on the h/p sign (*hest* is no word). The sentence has no verb: *akar Jolánka Pestre* is taken as "wants [to go] to Pest", and *Jolánka* in the third person of the addressee herself is a polite usage or another person of that name; I cannot decide which.
4. **Row 12 `le` (before *mivel*)**: two clear signs l, e with no word of their own. Taken as an unfinished *lesz*; this is a guess.
5. **Row 14 `d` in *d az én*:** the sign is d (tick on the left of the stroke). Normalized *d[e] az én*, assuming the e is elided; not confirmed. *mi így* is read with a dotted i; *megy* is excluded by the dot.
6. **Row 1, first sign:** the card shows `( ) z` where the family writes `) z` for *sz*. Literal *csz*; opposed bowls are the family's sign for *cs* (HCP1216), so the pair may be that digraph sign written by mistake, or a false start. The normalization *Szeretet[t]* is the same either way. Row 11 has the same left bowl in `rocz` where *rossz* is needed (normalized *ros[s]z*); the writer seems to have confused the two bowls.
7. **Row 7 `mam{a|e}`:** the bars after the second m have a retraced top, so two or three bars are possible; normalized *mama*, by sense.
8. **Bottom-right corner:** the end of row 18 and the start of the edge row overlap. Row 18 ends in a thick stroke with a thin arm running right from near its top: a gamma, so the t of *mint* is seen and not only supplied by context. The strokes left over for the edge row are three (one long and thin, two short), so the vowel of *l_tásra* may be literally e, a slip for á; I keep `{a|e}` because the strokes cross and the long one is unlike a normal bar. *látásra* is by word sense. In row 19, the n of *viszont* has widely spaced strokes, and faint dots above its second stroke are unexplained.
9. **Row 18 `hatok`:** the sign after h is a heavily struck-over loop with two thick bars on top, read as a correction to a. The next signs are overlapped by the portal stamp but legible. Extra small ticks on two three-stroke m signs (*most*, *maga*) are read as pen slips; *maga* rests partly on that.
10. **Stamp row 2:** a smear covers the second sign; the loop is read as o (*lom*, normalized *lö-m*, i.e. *üdvözlöm*) and the three strokes are faint. The top-left ü is blotted, its dots seen as blots. *Fery*: final sign read y.
11. **Row 17, first sign** is j (inverted T, bar near the foot, as in rows 3, 8 and 13), not f (upright cross, rows 7 and 16), giving *éjjel* across the row break 16/17. The ledger first had f (*éjfél*); see the response to review 1.
12. Word-division hyphens stand on the card after `egy` (row 9) and `re` (row 14) and are printed. Dots and accents missing on the card are supplied in the normalization (*hétfőn* for `hétfon`, and others); *Koth.* in the plain script is taken as *Kath.* (a/o of that hand are not clearly distinct) and expanded as *Katholikus Legény[egylet]*. The date is not established: the file name says 1912 and the postmark is only partly legible (I can see "9 12"-like figures on one cancel, not a full date).

## Why I believe it is correct

- The family key, used unchanged, turns all ciphertext on the card into Hungarian: 19 rows, the edge row and the 6 rows under the stamp, with no sign left without a value.
- The opening agrees with the family's formula (HCP1218: *Kívánom, hogy a legjob[b] kedvében … találja soraim*, with the same dropped b; HCP1217/1218: *hogy mulat…*), as do the close (*Isten vele*, *viszontlátásra*) and signature (*kedvese*, HCP1216).
- Long unforced words come out: *tudatom*, *egyleti mulatság*, *reményeim*, *viszontlátásra*, *távolból*. The ciphertext "egyleti" joins across the Latin "Kath. Leg." (Katholikus Legényegylet), which is independent evidence for the reading.
- Repeated words decode identically (*hogy* ×4, *mulat-* ×2, *akor/kor*).
- Independent check: the reviewer's own sign-by-sign reading, decoded with the family key file, differed from the first ledger in one sign of 345 (row 17, now corrected).

**Note on the reading process:** the reading was not blind to expected formulas, and the word-sense calls above are listed so that the reviewer can test them.

## Response to review 1

Verdict REVISE. I rechecked every finding on the review crops. Findings 1 to 7 are all addressed; the only sign changed in the ledger is the one in finding 1 (finding 4 removes a query, finding 6 adds two hyphens). Decoded plaintext words that changed: *éjfél* → *éjjel* and *parasztin* → *Harasztin*. The command was re-run after the fixes: all four hashes OK, and the rows match the table above. The reviewer's `review/work/my_decode.py` now reports 0 differences over 345 signs; its only remaining messages are the two hyphens, which its reading omits.

1. **Row 17 j, not f: fixed.** `review/work/crops/z_jf_compare.png` and `r17a.png` show the stem coming down to a bar near the foot, with only a tiny stub below it; the f signs of rows 7 and 16 are crosses with a long stem below the bar. Ledger now `J E L …`; the reading is *Hétfőn éjjel volt egy kis tüzünk is*, "On Monday night we also had a small fire". Uncertainty 11 rewritten; normalized text and translations updated.
2. **Row 5 place name: accepted.** *Hogy mulat Harasztin?*, "How are you enjoying yourself at Haraszti?", with no change of letter. Normalized text, translations and uncertainty 2 updated, and the identification is stated as word sense. One correction to the review: it says this is the only Jolánka card with the name, but HCP1310 row 18 has `darasztin` in its own SOLUTION.md, with its first sign read d. I record that as a parallel in uncertainty 2. Row 13 *Pest* stays p by word sense.
3. **`tustkantek`: fixed.** "Probably" and *asi* are gone from the translations; uncertainty 1 says the sense is unknown and names both *füstbe mentek* and *tönkrementek* as guesses only.
4. **Corner: accepted in part.** On `review/work/crops/z_corner.png` I see the thick stroke with the arm as a gamma, so `{t?}` is now plain t in the ledger. I keep `{a|e}` for the edge-row vowel: three strokes remain, but they cross and the long one is unlike a normal bar, so I record e as possible and do not commit to it. *látásra* is unaffected.
5. **Row 1 `( )`: fixed.** Uncertainty 6 now names the opposed-bowls *cs* sign of HCP1216.
6. **Hyphens: fixed.** Confirmed on `review/work/crops/r09b.png` and `r14b.png`. Both are now `=-` tokens in the ledger, so the table and the command output agree.
7. **Status line: fixed.** Header rewritten, and the independent reviewer comparison added to the reasons for confidence.

The reading is not substantially changed: the review's single sign difference is corrected, and the reviewer stated that no second round is needed for these fixes.
