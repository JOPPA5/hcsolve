# HCP1227 — Feri to Jolánka Tóth: how to find him on the train

**Status: main text read completely; the closing under the stamp reads as the family formula, with 8 signs restored (5 in the torn patch, item 1; 3 under the printed triangle, item 2). Review 1 verdict REVISE, findings addressed below.** Claude Opus 5.5, 2026-11-02. No earlier work on this number; the portal shows Not solved with no attached solution or transcription, and no published solution of this card turned up.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the Jolánka postcard family. The key was transferred, not invented, from the finished cards HCP1216 (table in its SOLUTION.md), 1301, 1243. Sign classes: two bars a; 6-shape b; opposed bowls cs; long stroke + tick d; three bars e; cross f; open loop with descender (4-like) g; tall stroke + tick h/p; dotted crossed curve i; inverted T j; section mark or S-curve k; wave l; three short strokes m; two short strokes n; cursive loop o; F-shape r; right bowl s; gamma t; x-cross u; chevron v; low descender y; crossed diagonal z. Dots over o/u give ö/ü. Digits are written as plain digits (as on HCP1301). On this card u and z are close; every call follows the word.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1227/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (my manual sign-by-sign transcription, one token per written sign) and prints the literal rows and the normalized text `work/normalized.txt`.

## Literal decipherment

```
01 szeretettedesjolankam          13 amelikazonavonalon
02 becsessoraitmegkaptammit       14 vanénanyugatioldalon
03 nagyörömmelfogadok             15 vagyokesarrakeremhogy
04 eskoszönöksorainnem            16 anemdohanyzoszakasz
05 tudokeligazodnihogy            17 bautazzonhogyeset
06 szombatongyönevagy             18 legkonyenmmegtalal
07 28ánmerezketöén                19 jamesedesemmerfel
08 hatehetamszombaton             20 atulvasutasruhatol
09 varomvalaholdehogy             21 anyirahogylatniseakar
10 holaztennemtudummeg            22 benn{|}epedigazelsotalalkozasomabalesz
11 jegyzemaztishogyen             23 merthasikerüavonatontalkoznicsakis
12 nemazonarakosonvagyok          24 abbaleszek
stamp: isten / veleede / [s][e][m]abol / [d][o]gvi / s[z][o][n]t / latasig / feri
```

Layout note: rows 22 to 24 run on along the bottom edge under the address. After *vonaton* the writer goes on at a higher level (*talkozni csakis*), and *abbaleszek* is squeezed below it, starting under *talkozni*. I take that order from the sense; the other order gives no text.

## Hungarian (normalized)

On the address side, in plain script: Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás. Cancels: Rákospalota-Újpest station box, circular date with day 26.

Szeretett édes Jolánkám! Becses sorait megkaptam, mit nagy örömmel fogadok és köszönök. Sorain nem tudok eligazodni, hogy szombaton jön-e vagy 28-án, mer[t] ez kettő. Én hát e héten szombaton várom valahol, de hogy hol, azt én nem tudom. Megjegyzem azt is, hogy én nem azon a Rákoson vagyok, amelyik azon a vonalon van, én a Nyugati oldalon vagyok, és arra kérem, hogy a nem dohányzó szakaszba utazzon, hogy esetleg könnyen megtaláljam. És édesem, mért fél a túl vasutas ruhától annyira, hogy látni se akar benne, pedig az első találkozásom abba[n] lesz, mert ha sikerü[l] a vonaton talá[l]kozni, csakis abba[n] leszek.

Under the stamp: Isten vele, éde[sem], a bol[do]g visz[on]tlátásig. Feri.

## English

My beloved sweet Jolánka! I received your esteemed lines, which I welcome with great joy and for which I thank you. I cannot make out from your lines whether you are coming on Saturday or on the 28th, because these are two [different things]. So I will wait for you this week on Saturday somewhere, but where, that I do not know. I also note that I am not on the Rákos that lies on that line; I am on the Nyugati [Western station] side, and I ask you to travel in the non-smoking section, so that I may perhaps find you easily. And, my sweet, why do you fear the all-too-railwayman clothes so much that you do not even want to see [me] in them? Yet my first meeting [with you] will be in them, because if we manage to meet on the train, I will be in nothing but those.
Under the stamp: God be with you, my sweet, until the happy reunion. Feri.

## Slovak

Moja milovaná, sladká Jolánka! Vaše vzácne riadky som dostal, čo s veľkou radosťou prijímam a ďakujem za ne. Z Vašich riadkov sa neviem vyznať, či prídete v sobotu alebo 28-ho, lebo to sú dve [rôzne veci]. Budem Vás teda čakať tento týždeň v sobotu niekde, ale kde, to neviem. Podotýkam tiež, že nie som na tom Rákosi, ktorý je na tej trati, som na strane Západnej stanice, a prosím Vás, aby ste cestovali v nefajčiarskom oddelení, aby som Vás prípadne ľahko našiel. A, drahá, prečo sa tak bojíte toho príliš železničiarskeho oblečenia, že ma v ňom ani nechcete vidieť? Veď moje prvé stretnutie [s Vami] bude práve v ňom, lebo ak sa nám podarí stretnúť sa vo vlaku, budem jedine v ňom.
Pod známkou: S Bohom, moja sladká, do šťastného zvidenia. Feri.

## Uncertainties

1. **Closing under the stamp (the largest point; changed after review).** Lines S3 and S4 lie in a patch where the stamp tore the paper surface and where the black station box and a printed green triangle overlie the ink. Readable: S3 ends `a b o l`, S4 ends `g` before `v i`. Division `éde|[sem] a bol|[do]g vi|szont|látásig` gives *Isten vele, éde[sem], a bol[do]g viszontlátásig*, the family closing (HCP1205 "Isten vele, édesem, a boldog viszontlátásra"). s, e, m, d, o are **restored from that formula, not read**: neither solver nor reviewer could confirm them on the pixels, and their number is estimated (faint traces left of the a in S3 decide nothing). The sense of the closing is complete, and every visible sign fits it; my first division into "…ból" and "…g" was wrong.
2. **Restored:** S5 `[zon]`: only the first s and final t stand clear; z, o, n lie under the printed letters of the triangle. *viszontlátásig* is supported by *vi* before it and *látásig* after it, but it is a restoration of three signs, not a reading. In S6 the t stem is visible and its bar runs along the triangle's base line.
3. **S7 Feri:** the first sign is a tilted cross (f as on HCP1216, tilted cross there too; u is the other shape possibility), e and r are faded. *Feri* rests partly on the family's signature; compare HCP1216.
4. **Row 7 `28-án`:** the first two signs are read as digits 2 and 8, not cipher signs: 2 has no match in the key, and the a carries a visible accent, giving the regular date ending *-án*. This reading rests on sense. It also explains the next words *mer ez kettő* (Saturday and the 28th are two different days). Row 13 has a similar 8-like sign, read as k in *amelik*; the two uses differ by context only.
5. **Row 7 `kető`:** the k, e, t and ö are retraced or overwritten; the k is blotted with the e. The reading *ez kető* (= kettő) is the best word fit, but the overwritten layer is not separable.
6. **Row 8 `hetam`:** corrected after review: the sign before m is two bars with a hooked top bar, clearly not the three-bar e. The literal is `hat e hetam szombaton`. Normalized *e héten* ("this week") is an **emendation of two signs** (a for e, m for n), chosen because it is the idiomatic form and *hetem* or *hetam* gives no case fit. *e hét ám szombaton* (with the particle ám, "this week, mind you, on Saturday") needs no sign change but is less idiomatic. The sense "this week on Saturday" holds either way. h/p: *hat* and *hetam* as h, *pedig* (row 22) as p, *kaptam* (row 2) as p, all from word sense; d in row 9 *de* rests on sense too: the sign has ticks on both sides of the stem and is retraced.
7. **Rows 10 and 18:** row 10 has six strokes before *eg*: m of *tudum* + m of *meg*. Row 18 has after *könyen* also six strokes before *eg*, so one m is superfluous (`konyen m meg`): false start or dittography, dropped in normalization. Row 10 has a small tick under the third stroke, ignored.
8. **Row 19 first sign:** it is blotted with an F-like flag over a heavy base. Read as j (inverted T with a thick base, like row 11) because *megtalál|jam* needs it; r gives no word. Contextual.
9. **Row 15 `arra`:** a, then two touching and overwritten r signs, then a. Read from shape plus sense.
10. **Row 20 `túl`:** `a t u l` is clear; the phrase *túl vasutas ruha* ("too railwayman-like clothes") is my interpretation. Reading *vasutas ruha* as a railway uniform is also an inference.
11. **Row 22 `benn|e`:** five strokes between e and e; four give *benne*, one stray stroke is ignored. Writer's omission: *sikerü[l]* row 23, *talkozni* for *találkozni*, *aba*/*abba* for *abban*, *mer* for *mert*, *amelik*, *anyira*, *konyen*; *gyöne* for *jön-e* (dialect spelling, normalized); *tudum* for *tudom*. *mér* in row 19 is taken as *mért* ("why"), not *mert*: no t is written and the question fits; with *mert* the sentence has no main clause.
12. Rows 4 and 18 have o without visible dots in *köszönök*, *könnyen*; supplied in normalization. Accents are otherwise mostly unmarked and supplied.
13. **Plain address word Szépreményű:** it is partly under the black box; *…reményű* is clear, *Szép* is my reading of the first letters.
14. **Picture side:** the printed gold lines read Szerelmi üzenet / Hozzád sietek angyalom! / Égek a vágytól, hogy viszontlássalak. A further faded gold line near the right edge (rotated 90°) is probably a worn printed caption: it is in the same gold italic style as the others and shows no cipher signs. Neither solver nor reviewer can read it.
15. On the cancel only the day 26 is readable; no month and no year stand clear. The month IX comes from the portal file name alone, and I do not use it for dating. So the 28th cannot be tested against a calendar. Whether Feri is the same man as on other family cards is suggested by the name and Rákospalota cancel, not proved.
16. **`találkozásom` (row 22):** literally "my meeting"; the translations add "[with you]". *mér* = *mért* and *túl vasutas ruha* remain interpretive (items 10, 11).

## Why I believe it is correct

- The key comes unchanged from reviewed sister cards, and it turns all 24 main rows into running Hungarian. No key letter had to be changed; only digits and one stray stroke lie outside it. Editorial changes beyond spelling normalization are listed above, notably *héten* for literal `hetam` (item 6).
- The story is specific and self-consistent: a meeting on a train, a non-smoking section as a recognition aid, a uniform, the distinction between two places called Rákos, and the Nyugati (Western station) side. The Rákospalota-Újpest cancel fits.
- Repeated words decode identically: *hogy* ×6, *szombaton* ×2, *vagyok* ×2, *nem* ×4, *abba* ×2, *lesz* ×2, *találkoz-* ×2.

## Credit

Key from the finished Jolánka cards (GPT-6 Astra / GPT-6.1 Sol and Claude Opus 5.5 work recorded there). Transcription and decipherment of this card: Claude Opus 5.5.

## Response to review 1

Review verdict REVISE. I reread rows 3, 8, 9 and the stamp block on the reviewer's enlargements (review/work/r3.png, r8b.png, r9b.png, st.png, s3t.png, s4t.png, cancel.png). All nine findings are accepted.

1. **Row 3 phantom signs: fixed.** The enlargement shows two groups of three strokes, then one three-bar e, one wave l and the cross f, so there is no second `e l`. `work/ledger.txt`, the literal block, `work/normalized.txt` and both translations now have *fogadok*, "welcome"; Slovak *prijímam* stays in the sense of receive, not accept.
2. **Row 8 `hetam`: fixed.** Two bars with a hooked top bar, unlike the three-bar e's in the same row. Ledger and literal block corrected; item 6 restates the two-sign emendation and the alternative *e hét ám*.
3. **Row 9 `vala`: fixed.** Two bars, the lower with a split pen stroke. Ledger and literal block corrected; the undisclosed normalization is gone.
4. **Stamp closing: fixed.** The "…ból / …g" division and the bare "[...]" are replaced by *a bol[do]g viszontlátásig*, labelled in item 1 as a restoration from the family formula, not a reading. The ledger now holds [s] [e] [m] and [d] [o] in place of 4 + 3 lost positions; the counts of 3 and 2 are estimates. `work/decode.py` now counts restored signs.
5. **S5 restoration: no change needed.** `[zon]` stays labelled as restored.
6. **Status and Why sections: fixed.** Status now speaks of restored signs; Why names the *héten* emendation.
7. **Dating note: fixed.** Item 15 says the month comes from the portal file name alone; the cancel crop shows only the 26.
8. **Picture edge line: fixed.** Item 14 now calls it probably a worn printed caption.
9. **`találkozásom`: fixed.** Translations read "my first meeting [with you]" and item 16 notes the literal sense.

The reproduction command was re-run after the changes: all four hashes OK, and it prints 515 tokens, 8 of them restored, none lost without restoration. The reviewer's independent decoder (`python3 -I ciphers/hcp-1227/review/work/decode_review.py`) now shows no difference from the ledger on rows 1 to 24: 477 letters on both sides.
