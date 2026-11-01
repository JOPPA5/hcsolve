# HCP1279 — Feri to Jolánka Tóth: saving for a home, and wanting to live only for her

**Status: reading of the whole visible card, with disclosed residual points (below). Reviews 1 and 2 (both REVISE) addressed.** Solved 2026-11-01 by Claude Opus 5.5 (no earlier work on this number; key transferred from finished cards). The portal shows status *Not solved*, with no transcription or solution attached; no published solution of this card was found or used.

## Cipher type and key

Hungarian, monoalphabetic substitution with invented graphic signs: the Jolánka family key of HCP1216 and its sisters, used unchanged. Register type label: MASC.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S-shape) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| long stroke + short, joined tick | d | two strokes | n | plain cross x | u |
| three bars | e | upright cross + | f | chevron | v |
| open loop with descender | g | tall stroke + short tick | h / p | low descender | y |
| loop or curve with dot above | i | cursive loop | o | crossed diagonal with tail | z |
| inverted T | j | left + right bowl | cs | | |

The dot is the working difference between i and o: several i signs are closed loops too, and a loop with no dot is o. The h/p sign has one shape for two letters. It was split by word sense in all cases: h in *hogy*, *láthassam*, *ruhát*, *ha*; p in *pénz*, *percz*, *pedig*. Dots or ticks over o and u give ö/ő and ü/ű. Acute marks are mostly not visible and are supplied. The writer writes gy as g+y and usually writes double consonants once.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1279/work/decode.py
```

It checks the SHA-256 of the source scans, decodes `work/ledger.txt` (647 written signs, one token each) with the key, and prints the literal rows and `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the hi-res address side (`work/crops/`, made by `work/crop.py`, `crop2.py`, `crop3.py`, `crop4.py`, `greenmask.py`). It is not OCR, and the portal attaches no transcription, so the transcription is mine.

## Literal decipherment (as printed by the command)

```
01 nezhogyacsalditüzhely{a|e}t            16 elniahogymagakivanja
02 megszerezemadigkelsokat                17 vagyjobbanmondvacsak
03 küzdenem[s]okszorelvesz                18 maganakesszolgalatom
04 tetüremhogymiertnem                    19 nakfogomelnibarmar
05 [r]endelkezemmárlegalab                20 itvol{x}aazaherczhogy
06 [{a|e}][n]yihénzelamierre              21 lathassamamiaszüle
07 debizomazistenbe                       22 imetilletiegygyen
08 hogymegezismegelem                     23 lörenemküldommegmert
09 egyszerugyörulokéde                    24 masrakelahenzmertmost
10 semhogymarcsak[h]erom                  25 akaruhat{o|i}scsinaltat
11 {n|h}evalasztelattolhogy               26 nieshedigkeszhenzer
12 viszontlathessemhogy                   27 dehamagakivanjaakorelkuldömdomelsejenezcsakma
13 leszakivezereljen                      28 gatolfügdeenszeretnekelöbatöltözniezel
14 eskitöjotanacsokatker                  29 bezaromsoraimmaradokszeretökedveseferi
15 jekmertencsakugyakarok                 stamp: og | csokjai | év{a|e}gyo | kedvesse | feri
```

Rows 27 to 29 run across the bottom of the card under the address. The five stamp rows stand below and beside the stamp at upper right.

## Hungarian (normalized)

Néz[d], hogy a családi tűzhelyet megszerez[z]em, ad[d]ig kel[l] sokat küzdenem. Sokszor elveszte[m] türe[lme]m[et], hogy miért nem rendelkezem már legalább [a/e]n[n]yi pénzel, ami erre [kell], de bízom az Istenbe[n], hogy még ez[t] is megélem egyszer. Úgy örülök, édesem, hogy már csak [h]árom hé[t] (?) választ el attól, hogy viszontláthassam, hogy lesz, aki vezéreljen, és kitő[l] jó tanácsokat kérjek, mert én csak úgy akarok élni, ahogy maga kívánja, vagy jobban mondva csak magának és szolgálatomnak fogom élni. Bár már it[t] volna az a percz, hogy láthassam! Ami a szüleimet illeti, egygyenlőre nem küldöm meg, mert másra kel[l] a pénz, mert most akar[ok] ruhát is csináltatni, és pedig készpénzér[t], de ha maga kívánja, ak[k]or elküldöm elsején. Ez csak magától függ, de én szeretnék előb[b] átöltözni. Ezel bezárom soraim[at], maradok szerető kedvese Feri.

By the stamp: [row lost under the stamp ...]og. Csókjaié[rt] vagyo[k] (?) kedvese Feri.

Printed on the picture side: *Miért is vagyok szegény* ("Why am I poor, after all"), with a verse on a poor suitor. The letter answers this theme. Address, in clear: *Szépreményű Tóth Jolánka úrleánynak, Jász Árokszállás*. Cancelled Budapest, 12 April 1914.

## English

See, until I obtain the family hearth I have to struggle a great deal (free: the card has *hogy* ... *addig*, "that I may obtain ..., until then"). I often lose my patience over why I do not yet have at least [so] much money as this needs, but I trust in God that I shall live to see this too one day. I am so glad, my darling, that only three weeks (?) now separate me from seeing you again, so that there will be someone to guide me and someone from whom to ask good advice; for I want to live only as you wish, or better said, I shall live only for you and for my work. If only the moment were already here when I can see you! As for my parents, for the time being I am not sending it, because the money is needed for something else: now I want to have clothes made as well, and for cash at that. But if you wish it, I will send it on the first. That depends only on you, but I would like to get newly dressed first. With this I close my lines and remain your loving sweetheart, Feri.
By the stamp: [row lost] ... For your kisses I am (?) your sweetheart, Feri.

## Slovak

Pozrite, kým nezískam rodinný krb, musím veľa bojovať (voľne: na lístku *hogy* ... *addig*). Často strácam trpezlivosť, prečo ešte nemám aspoň [toľko] peňazí, koľko je na to treba, ale dôverujem v Boha, že sa aj toho raz dožijem. Tak sa teším, moja drahá, že ma už len tri týždne (?) delia od toho, aby som Vás znova videl, aby bol niekto, kto ma povedie, a od koho si môžem pýtať dobré rady; lebo ja chcem žiť len tak, ako si Vy želáte, alebo lepšie povedané, budem žiť len pre Vás a pre svoju prácu. Kiežby už tu bola tá chvíľa, keď Vás uvidím! Čo sa týka mojich rodičov, zatiaľ to neposielam, lebo peniaze treba na iné: teraz si chcem dať ušiť aj šaty, a to za hotové. Ale ak si to želáte, pošlem to prvého. To závisí len od Vás, ale ja by som sa chcel najprv nanovo obliecť. Týmto končím svoje riadky a zostávam Váš milujúci milý, Feri.
Pri známke: [riadok stratený] ... Za Vaše bozky som (?) Váš milý, Feri.

## Uncertainties

Restorations (signs physically hidden):

1. **Row 3, `[s]okszor`.** A heavy ink blot covers one sign. Only *s* gives *sokszor*.
2. **Row 5, `[r]endelkezem`.** The first sign lies under the black BUDAPEST postmark letter E. Green traces are visible but the shape is not. Only *r* gives the word.
3. **Row 6, `[a/e][n]yi`.** The row start lies under the postmark. Two signs are hidden; the green remains (`work/greenmask.py` did not separate them) are too poor to read. The third and fourth signs are read as y and i, with the i crossed by the postmark. *annyi* and *ennyi* are both possible, so this restoration is **not unique**; it rests on the sense "so much money".
4. **Stamp row S0.** Two signs (o, g or y) stand at the right end of the stamp. The rest of that row is under the stamp and physically lost, so it is lost text, not an unread word. **At most one short row is gone.** The first sign of S3 crosses the blue triangle cancel and is read as k.

Conjectural readings (marked (?)):

5. **Rows 10-11, `[h]erom {n|h}e` = *három hé[t]*, "three weeks".** The frame *már csak X választ el attól, hogy viszontláthassam* is secure and requires a span of time; the words are not secure. What supports it: (a) the mark after *csak*, which the first version called a stray tick, is a long rising green stroke with a short green mark at its upper end, lying under the postmark line (`work/crops/x10.png`); it fits the h/p sign but the postmark prevents a firm call, so it stands in the ledger as restored `[H]`; (b) the first sign of row 11 has two strokes, the first apparently taller (`work/crops/x11.png`), but it is crossed by the postmark and n against h is **not settled** from the pixels: h comes from word sense; (c) the same family has `haromhetmulva` on HCP1297 (1912) and *3 hét múlva* on HCP1263 (1913). These cards are from earlier years than this one (April 1914), so they support the phrase only, not this event or this number. What it costs: e for á (three clear bars) and a dropped t. The writer drops final consonants on this card (*készpénzér[t]*, *kitő[l]*, *kel[l]*) and writes e for á in the family (*szétvélasszon*, *bérmijen*, HCP1251). The number itself is the weakest point. If this fails, X is one unread word in a sentence whose sense survives.
6. **Stamp rows S1-S2, `csokjai` + `év{a|e}gyo` = *csókjaié[rt] vagyo[k]*, "for your kisses I am".** The signs of S2 are: e with an accent tick above, v, a top bar over a black blot with two lobes, g, y, o. Sign 3 is undecidable (two or three bars; a lower bar under the blot cannot be excluded), so it stands as `AE`. The first reading follows the same family's formula on HCP1308, `csokjaiert / vagyo / ...`, normalized there *Csókjaiért vagyo[k] sírig hű imádója, Feri*: the same `vagyo` without k at the end of a stamp row. Here S3 even begins with k. It needs *-rt* dropped after é and the final k lost. **Alternative:** *csókjaié[rt] vágyó [...] kedvese*, "longing for your kisses, your sweetheart". A separate tick at the upper right of sign 6 (`review/work/crops2/s2z.png`) is the one point in its favour, if it is an accent on ó rather than stray. Either way the verb stem stands and the letters do not change; the choice between the two words is not proven.

Sign calls and writer's forms:

7. **Row 1:** `Néz` as *Nézd* is a guess. The final vowel of `hely{a|e}t` has its top bar lost in the descender. `csaldi` is *családi* with the accent unmarked.
8. **Row 4:** `tetürem` after `elvesz` is split *elveszte[m] türe[lme]m[et]*, with a whole syllable omitted by the writer. This is interpretive.
9. **Row 14:** `kitö` is taken as *kitől*, with the l dropped.
10. **Row 18:** `esszolgalatom`: the sign after o is an unusual q-shaped loop with descender, read as l from the word; the o of *-tom* is merged into the t and y-like stroke, so it is the weakest letter in the word. The e's mark and a stained right bowl give *és*.
11. **Row 20:** `itvol{x}aaza`: after *itvol* one sign is scribbled out, then two bars, two bars, z, two bars. Every other letter of *volna az a* is on the card and the scribble stands where the n belongs. Whether it hides an n is not read; the n comes from sense.
12. **Row 22:** the first i is smeared; the fourth `gy` is written with a dark, narrow g.
13. **Row 25:** `akaruhat{o|i}s`: the r of *akar* and of *ruhát* is written once; the loop before s has no visible dot, normalized *is*. `akar` is normalized *akar[ok]*, first person, because the sentence ends *de én szeretnék előbb átöltözni*; the ending is lost.
14. **Row 27:** `elkuldömdom` has a repeated *-dom*, dropped as dittography (this writer repeats, cf. HCP1216 `hig higgyje`); unproven. `elsején` then means "on the first".
15. **Row 28:** `függ de en`: the d is immediately after g; I read *függ, de én*.
16. **Stamp S3:** `kedvesse` has a doubled s, for *kedvese*.
17. Word division, punctuation and accents are editorial. The final *Ezel bezárom* (row 28 end to row 29) is *Ezzel bezárom*.
18. **Rows 6-7:** *ami erre [kell]*: the bracketed *kell* is not on the card, which runs directly `amierre | de`. It is supplied for sense; the writer may have left the clause elliptic.

The sender signs Feri. The sentiment and addressee match HCP1216, but identity with senders of other cards is not claimed beyond the same name and key.

## Why it is correct

- The key was transferred unchanged from reviewed cards. All 647 signs get a value except one scribbled sign; four are hidden signs restored from sense or left undecided, and the [H] of row 10 is read under the postmark.
- Long passages read without any freedom: *hogy miért nem rendelkezem már legalább*, *de bízom az Istenbe*, *ami a szüleimet illeti*, *nem küldöm meg mert másra kell a pénz*, *hogy lesz aki vezéreljen és kitől jó tanácsokat kérjek*, *csak úgy akarok élni ahogy maga kívánja*, *ezzel bezárom soraim maradok szerető kedvese Feri*.
- The content fits the context: the picture is about being poor, and the letter is about lacking money for a home; the addressee is Jolánka, and the closing formula matches the family.
- Repeated words decode identically (*hogy* ×8, *mert* ×3, *pénz* ×3, *csak* ×4, *maga* ×4, *kívánja* ×2).

## Credit

Key: the Jolánka family cards, with earlier work by the OpenAI GPT solver and Claude Opus 5.5 (see HCP1216). Transcription and reading of this card: Claude Opus 5.5.

## Response to review 1

Verdict REVISE. I checked each disputed spot on the reviewer's crops and on my own zooms of the hi-res scan, then changed `work/ledger.txt`, `work/normalized.txt`, `work/decode.py` (token `NH`) and this file. `python3 -I ciphers/hcp-1279/work/decode.py` re-run: hashes OK, 647 signs, output as in the literal block above.

1. **Row 14 sign 8: fixed.** Closed loop with right tail and no dot (`review/work/crops/r14c.png`); the tick below belongs to the é of row 15. Now `jo tana`, *kitő[l] jó tanácsokat kérjek*. *kitöjitana*, *utána* and *csókot* are gone from all three languages.
2. **Rows 9-10: fixed.** Short stroke + long stroke = d; the accent on the e is recorded (`E:a`). Row-break word *édesem*; *ennek, semhogy* withdrawn.
3. **Rows 10-11: fixed, and taken further than the review.** *Ne választana* and "strength" are withdrawn, and the row-11 sign is disclosed as n/h undecided (ledger `NH`). The frame is translated. The review asked for X to stay unread and did not assert *három hé[t]*. I found one thing it had not weighed: the "stray tick" after *csak* is a green stroke under the postmark, so one of its three objections (the missing h) is weakened. I therefore propose *[h]árom hé[t]* with (?), see uncertainty 5. This adds a sign to the ledger (646 to 647) and is new, so it needs checking; this is why I am resubmitting instead of closing.
4. **Row 1 sign 10: fixed.** Two bars (`review/work/crops/r01.png`), `csaldi`. The "e for á" note is removed.
5. **Row 19 sign 9: fixed.** Three bars (`r19e.png`), `elni`; the *állni* note is removed.
6. **S3 sign 7: fixed.** Second right bowl (`S3.png`), `kedvesse`.
7. **Translations: fixed.** *akar[ok]* is first person, shown as a normalization, and "[someone]" is gone; *átöltözni* is "get newly dressed"; the *hogy* / *addig* freedom is stated; *Néz[d]* is marked as a guess.
8. **Figures: fixed.** Recounted on the decoded rows: *hogy* 8, *csak* 4 (and *maga* 4). The i entry of the key table now states the dot rule.
9. **Completeness: addressed, with one disagreement of wording.** S0 is lost under the stamp, not unread, so it should not count as an unread word (uncertainty 4). S2 now has a proposed reading (uncertainty 6): the third sign proved to have three bars, not two, so *vágyó* still needs e for á, and I say so. Neither (?) word is proven. If review 2 rejects both, X and S2 are two isolated spots and the card should be labelled partial, per the rule the review cites. Row 20 `vol{x}e` remains disclosed.

## Response to review 2

Verdict REVISE. I checked findings 1-3 on the reviewer's crops (`review/work/crops2/s2z.png`, `r20x.png`) and changed `work/ledger.txt`, `work/normalized.txt` and this file. `python3 -I ciphers/hcp-1279/work/decode.py` re-run: hashes OK, 647 signs, output as in the literal block above. The key and the body of the letter are unchanged.

1. **Stamp reading: fixed.** I had cited HCP1308 for `csokjaiert` and missed the `vagyo` that follows it there. "No alternative found" was wrong. *Csókjaié[rt] vagyo[k] (?) kedvese Feri* is now the first reading in all three languages, with *vágyó* as the named alternative (uncertainty 6).
2. **Row 20 sign 7: fixed.** `r20x` shows two bars after the scribble with clean paper between them, then two darker bars. Ledger E to A; row 20 is `itvol{x}aazaherczhogy`, and the "unaccounted three-bar sign" is gone (uncertainty 11). The scribble stays unread, and I say so.
3. **S2 signs 3 and 6: fixed.** Sign 3 is now `AE`; `s2z` shows a top bar and a two-lobed blot, so my "all three bars are visible" overstated it, and the e-for-á cost may not exist. The tick at sign 6 is recorded in the ledger header and in uncertainty 6. I also coded the accent tick on S2 sign 1, already described in uncertainty 6, as `E:a`, so the literal stamp row now shows é. Sign count unchanged.
4. **Same writer: fixed.** Uncertainty 5(c) now says "same family" and gives the years 1912 and 1913, which I checked against the portal names of those two cards; they support the phrase only.
5. **Supplied *kell*: fixed.** Added as uncertainty 18.

*Három hé[t]* (?) stays as a disclosed conjecture, as the review accepts. Review 2 leaned slightly further to h in row 11; I keep the ledger token `NH`, as it recommends. The remaining disclosed points are that one word, the stamp word with two named readings, and text physically lost under the stamp or postmark.
