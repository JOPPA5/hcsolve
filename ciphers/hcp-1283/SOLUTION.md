# HCP1283 — Feri to Jolánka Tóth (Jászárokszállás), bored and short of money

**Status: every sign on the card transcribed and decoded; two isolated words not understood (items 1, 2 below). Everything else reads. Revised after review 1 (see the last section).** Solver: Claude Opus 5.5, 2026-11-01. No earlier work on this number. The portal shows *Not solved* with no transcription or solution attached; no published solution of this card was found. The card's own message is enciphered on the address side (left half, bottom edge, under the stamps). The picture side is a printed song text. The address (plain): *Szépreményű Tóth Jolánka írnőnek, Jász-Árokszállás*.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the Jolánka family key taken unchanged from hcp-1216 (see its key table): two bars a, six b, left bowl c, short+long stroke d, three bars e, upright cross f, open loop with descender g, long stroke+short tick h/p, dotted crossed curve i, inverted T j, section mark k, wave l, three strokes m, two strokes n, cursive loop o, F r, right bowl s, gamma t, plain cross u, chevron v, loop with long tail y, crossed diagonal z, opposed bowls cs. On this card gy is written g + y (as in *tanya* n + y). Dots over a sign give é, ö, ü, í; two dots ö/ő.

## Reproduction (one command, repo root)

```sh
python3 -I ciphers/hcp-1283/work/decode.py
```

It checks SHA-256 of the four images, decodes `work/ledger.txt` (hand transcription from enlarged crops, one token per sign) and prints the literal rows and `work/normalized.txt`. The ledger is manual: decoding by the key was done while reading, so it is not blind.

## Literal decipherment

```
01 szeretetédesjolankankiva
02 nomhogyalegjobbkedveben
03 talaljasoraimhogymulat
04 vasarnapremelemjolle
05 galabbisjobbanmintén
06 makisementemazucza
07 raojunalmasnekemit
08 azéletbarigahogypesten
09 lehetmulatdemindenpez
10 bekerüesnekemettöltar
11 tozkodnomkelmegaza
12 alegnagyobbbajhogynem
13 erzemjolmagamsehol
14 hamegacskavollehetakor
15 nemcserélnéksenkivelde
16 leszmégezjobbanis.jö
17 vöhétenkimegyeharasz
18 tiraszívaemégatanya
19 ilevegöt.miujsagarok
20 szalasbajarnak
21 eberekbegondoe
22 néharamöntudom
23 unatkozikdeenra
24 erekhatgondolok
25 dragahejetzs,soraitvarvaimadojaferi
stamp: [i][s][t]envele | édesegy | etelen | remeny | emcsoko | [l]omferi
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb kedvében találja soraim. Hogy mulat vasárnap? Remélem, jól, legalábbis jobban, mint én. Ma ki se mentem az uccára, oly unalmas nekem itt az élet. Bár igaz, hogy Pesten lehet mulat[ni], de minden pé[n]zbe kerü[l], és nekem ettől tartózkodnom kell. Meg az a legnagyobb baj, hogy nem érzem jól magam sehol. Ha meg a ⟨cskavol⟩ lehet, akkor nem cserélnék senkivel, de lesz még ez jobban is. Jövő héten kimegy-e Harasztira? Szív[j]a-e még a tanyai levegőt? Mi újság Árokszállásba[n]? Járnak-e Berekbe? Gondol-e néha rám? Ön, tudom, unatkozik, de én ráérek, hát gondolok. Drága ⟨hejetzs⟩, sorait várva, imádója Feri.

Stamp field: [Ist]en vele, édes egyetlen reményem. Csókolom, Feri.

## English

My beloved sweet Jolánka! I wish that my lines find you in the best of moods. How are you enjoying yourself this Sunday? Well, I hope, at least better than I am. Today I did not even go out into the street, life here is so boring for me. True, one can have fun in Pest, but everything costs money, and I have to keep away from that. And the biggest trouble is that I do not feel well anywhere. But if ⟨unread word⟩ is possible (frame tentative), then I would not change places with anyone, but this will get better yet. Will you go out to Haraszti next week? Are you still breathing the farm air? What is new in Árokszállás? Do they go to Berek? Do you think of me sometimes? You, I know, are bored, but I have time, so I think [of you]. Dear ⟨unread word⟩, awaiting your lines, your adorer, Feri.
Stamp field: God be with you, my sweet only hope. I kiss you, Feri.

## Slovak

Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšej nálade. Ako sa zabávate v nedeľu? Dúfam, že dobre, aspoň lepšie ako ja. Dnes som ani nevyšiel na ulicu, taký nudný je tu pre mňa život. Pravda, v Pešti sa dá zabaviť, ale všetko stojí peniaze a ja sa tomu musím vyhýbať. A najväčšia bieda je, že sa nikde necítim dobre. Ak však môže byť ⟨neprečítané slovo⟩ (rámec vety je neistý), potom by som nemenil s nikým, ale ešte to bude lepšie. Pôjdete budúci týždeň na Haraszti? Dýchate ešte vzduch z majera? Čo je nové v Árokszállási? Chodia do Bereku? Myslíte niekedy na mňa? Vy sa, viem, nudíte, ale ja mám čas, tak myslím [na Vás]. Drahá ⟨neprečítané slovo⟩, čakajúc na Vaše riadky, Váš ctiteľ Feri.
Pole pod známkou: S Bohom, moja sladká jediná nádej. Bozkávam Vás, Feri.

## Uncertainties

1. **Row 14 `a cskavol` not understood.** All signs are clear: a, opposed bowls (cs), section mark k, a, v, o, l, followed by *lehet*. The wave l is written twice: once ending this word, once opening *lehet*. Word division and meaning are open; candidates such as *csókával* or *csak a vol[na]* need letters the card does not show, and none is adopted. An instrumental in *-val* (compare *senkivel* in the same sentence) would need a where the card has a clear o, so it is not adopted either. The word's grammatical role is unknown, so the English frame "if ... is possible" is tentative; "I would not change places with anyone" is secure.
2. **Row 25 `hejetzs`** after *drága*. Signs: h/p, e, j, e, t, z, flat-topped right bowl s (the form of row 1 *édes*), then a separate comma-like tick, then *sorait*. Possibly a misspelled adjective (*helyes*?) or a pet name; not adopted. The tick suggests the phrase ends there, so *Drága ⟨...⟩,* is taken as a form of address; that division is editorial. Also, the d of *drága* has nearly equal strokes (could be n; *drága* rests on word sense).
3. Row 1: the last sign of *Jolánkán* has two strokes (n), not three; normalized *Jolánkám* on word sense. *szeretet* has one t.
4. Row 4 *vasárnap*: the p is drawn short+long, the d-like order; p rests on word sense. Row 22/25 d, h, p calls likewise rest partly on stroke order and word sense.
5. Row 7 *ojunalmas* = *oly unalmas* (ly written j). *it* = itt.
6. Row 8 *bar*: bar sign over a blot, top bar seen, a or e not decidable; *bár* on word sense. *iga* = igaz, z not written.
7. Row 9 *mulat* = mulatni (ending missing); *pez* = pénz; row 10 *kerü* = kerül (l not written). Row 21 *gondoe* = gondol-e (l not written).
8. Rows 11/12: *a* is written at the end of 11 and again at the start of 12 (dittography, one dropped).
9. Row 15 end, `de`: the sign before the final e is read as d (short stroke upper left, long stroke right, the form of row 1 *édes* and row 9 *de*), giving *de lesz még ez jobban is*. The short stroke is darker ink and touches the tail of the preceding l, and a dot stands under the long stroke, unexplained. The first handover read this as an exclamation mark, which left the e unaccounted for. The d call rests partly on word sense. Row 23 *de* has the strokes in the opposite order (long+short), so stroke order is not a strict rule on this card.
10. Rows 17-18 *kimegye | sziva e*: read with the question particle, *kimegy-e* and *szív[j]a-e*, as *járnak-e* and *gondol-e* on the same card. Only the j is supplied. *Haraszti* is a place Jolánka stays at: hcp-1305 (FINAL) has *Hogy mulat Harasztin?*, and hcp-1265 (not final, hypothesis only) has *kiment Harasztira* and *szívja ezt a jó tanyai levegőt*. Which Haraszti is meant is not identified.
11. Row 18 *szívaemég*: the i is overwritten but its dot is clear. The e of *még* carries a clear dot, so it is *még* ("still"), not the verbal prefix *meg*.
12. Row 19 `arok` + row 20 `szalas` + `ba`: normalized *Árokszállásba[n]*, as the same form on hcp-1265; dialect or careless -ba for -ban. The first handover misread the k as g. Row 21 first sign is e, read as question particle *-e* of *járnak*. *Berek* is read as a place name (a river meadow or locality); not identified.
13. Row 12: y of *nagyobb* is inked over, still legible. Row 22: the u of *tudom* is a heavily inked blot with a cross shape. Row 10 *ettől*: overwritten, with a three-bar e under the o and a heavily retraced first t.
14. Row 22 opening *Ön*: o with clear two dots, then n. Row 25 sign after d in *imádója* lacks the usual right hook of o.
15. **Restorations:** Stamp row 1: the first three signs lie under the stamp edge, only their bottoms show; *Ist* restored from *en vele* (the family's closing formula). Stamp row 6: l is an ink blot with an arched outline; restored from *csókolom*. Stamp row 4: n of *reményem* shows only one stroke. All disclosed in the ledger by brackets, except the n.
16. Acutes other than é/í are mostly unmarked and are supplied in normalization. Pen marks ledgered: full stops in rows 16 and 19, tick in row 25; they do not count as signs (532 signs). The date is from the portal filename (1913-03-20), not from the cipher; the postmark date is not read here. The sender Feri is also on hcp-1216, but identity is not proved.

## Why it is correct

The family key was applied unchanged and yields connected, idiomatic Hungarian across 25 main rows and 6 stamp rows without any fitted value. The text fits the addressee (Árokszállás is spelled correctly inside the cipher, independent of the plain address), the *Ön* register, and the family formulas (*Isten vele*, *csókolom*). Words recur with the same signs: *hogy* ×4, *jobban* ×2, *gondol-* ×2, *nekem* ×2, *mulat* ×2.

## Response to review 1

All enlargements were re-read by the solver (review crops `z_*.png`, new crops in `work/resp/`). `python3 -I ciphers/hcp-1283/work/decode.py` was rerun after the fixes: all hashes OK, 31 rows, 532 signs, output as above. The key is unchanged.

1. **Rows 17-18 (major): accepted, fixed.** Now *Jövő héten kimegy-e Harasztira? Szív[j]a-e még a tanyai levegőt?*, with all three translations changed: Jolánka is the one who travels. The old reading invented letters; the new one supplies only the j. The full stop after *levegőt* (finding 7) also fits a sentence ending there.
2. **Row 19 last sign (major): accepted, fixed.** `z_r19e2.png` and `z_r20e.png` show the same hook top, smooth stem and heavy foot as the k ending row 20. The ledger now has K, and the false claim of g for k is deleted (item 12).
3. **Row 15 `!e` (major): accepted, fixed, with the caveat kept.** Compared with d in row 1 *édes* and row 9 *de* (`work/resp/cmp.png`), the short upper-left stroke plus long stroke fits d; reading *de lesz még ez jobban is* uses every sign. The dot under the stroke is not explained, and row 23 *de* has the reverse stroke order, so item 9 states that the call rests partly on word sense.
4. **Acute dots (minor): accepted, fixed.** Dots confirmed on the e of row 15 *nék* (`z_r14mid.png`, right end; the dot near the middle of that crop belongs to *cserél*, already ledgered), row 16 *még* and row 18 *még*. Added as `:a`.
5. ***Árokszálláson* (minor): accepted, fixed.** Now *Árokszállásba[n]*.
6. **`hejetz{?}` (minor): accepted, fixed.** The sign matches the s of row 1 (`work/resp/r25x.png`, `work/resp/cmp.png`). Ledger has `)` and a separate tick `,`; the word stays unread. I also treat the tick as closing a form of address, and say so in item 2. That changes the English from "your dear ... lines" to "Dear ..., awaiting your lines".
7. **Small points (minor): accepted, fixed.** Row 10 overwriting disclosed (item 13); full stops ledgered in rows 16 and 19 (`work/resp/r19d.png` shows a clear separate dot); the row count corrected.
8. **Haraszti (minor): accepted, fixed.** Item 10 cites hcp-1305 and hcp-1265, the latter as a hypothesis because it is not final.

Reviewer's suggestion on *-val*: considered and not adopted (item 1); the frame is marked tentative.

The changes are local: one sentence corrected, *de* added, spellings fixed. The key and the rest of the letter are unchanged, so no second review round was requested.
