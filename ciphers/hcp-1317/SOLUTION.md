# HCP1317 — Feri to Jolánka Tóth: the photograph, and wanting to be nearer

**Status: complete reading of all cipher text on the card, with the small disclosed residual points below (one unresolved word, row 10). Review 1 (REVISE) addressed; see the end of this file.** Claude Opus 5.5, 2026-10-30.

Credit: all work on this number is by Claude Opus 5.5. The key comes from the finished Jolánka family cards (HCP1216 and sisters), whose earlier work is credited in their own directories. The portal shows status *Not solved* with no transcription or solution attached; no published solution of this card was found; the orchestrator's AI-register check (2026-10-30) found no record of it.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the Jolánka family key, unchanged from HCP1216. Words are mostly spaced; accents are written as ticks and dots over the base sign.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S-shaped) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma | t |
| short + long stroke, tick on the left | d | two short strokes | n | heavy plain cross | u, with dots ü |
| three bars | e | cursive loop | o, with dots ö/ő | chevron | v |
| upright cross | f | long stroke + tick on the right | h / p (near-homograph) | low descender loop | y |
| hooked sign with descender | g | dotted crossed curve | i | thin crossed diagonal with tail | z |
| inverted T | j | | | | |

The family's gy is written here as two signs, g + y.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1317/work/decode.py
```

It checks the SHA-256 of both source scans and both originals, decodes the sign ledger `work/ledger.txt` (one token per written sign, 491 signs) with the key above, prints the literal rows, then prints the normalized text `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the original in `work/hires/`, not OCR.

## Literal decipherment (as printed by the command)

```
01 szeretetedesegyetlenre        14 miteloreisköszö
02 menyemkivanomhogya            15 nökedesemmostgyak
03 legjobbkedvebentalalja        16 ranjarokujvarba
04 soraimedesesjolankama         17 majnemmindigot
05 miafenykehetileti             18 vagyokszetnekmar
06 csakküldjeelakarsikerül       19 hatvanbaismenni
07 akarnemmarcsakazert           20 marazerzesijjol
08 ishogyazilonkaisraj           21 esnehogyközel
09 tavanmertirnikene             22 volnekmagahoz
10 kiheaztvaromhogy              23 edesembarakoris
11 afenykehetmegkahjam           24 elegmeszevolnek
12 tehatkeremedesem              25 ezzezaromsoraimmaradoksirighükedvesse  (along the whole bottom edge)
13 kuldjeminelelöbb              26 feri  (bottom right, above row 25)

Under the stamp: is[t]enve | leedes[e]m | csokol | szamta | lanszor | [i]madoja | [f][e]ri
```

## Hungarian (normalized)

Szeretett édes egyetlen reményem! Kívánom, hogy a legjobb kedvében találja soraim, édes Jolánkám. Ami a fényképet illeti, csak küldje el, akár sikerül, akár nem, már csak azért is, hogy az Ilonka is rajta van. Mert írni kéne {kihe|kipe}, azt várom, hogy a fényképet megkapjam. Tehát kérem, édesem, küldje minél előbb, mit előre is köszönök. Édesem, most gyakran járok Újvárba, majdnem mindig ott vagyok. Sze[re]tnék már Hatvanba is menni, már az érzés i[s] jól esne, hogy közel volnék magához, édesem, bár akkor is elég messze volnék. Ezze[l] zárom soraim, maradok sírig hű kedvese Feri.

Under the stamp: Isten vele, édesem! Csókol számtalanszor imádója Feri.

## English

My beloved sweet only hope! I wish that these lines of mine find you in the best of spirits, sweet Jolánka. As for the photograph, just send it, whether it turned out well or not, if only because Ilonka is in it too. For I ought to write [one unresolved word], I am waiting to get the photograph. So I ask you, my darling, send it as soon as you can, for which I thank you in advance. My darling, I go to Újvár often now, I am there nearly all the time. I would like to go to Hatvan now too; the feeling alone would do me good, that I would be near you, my darling, although even then I would be quite far away. With this I close my lines, and remain, faithful unto the grave, your sweetheart Feri.
Under the stamp: Farewell, my darling! Your adorer Feri kisses you countless times.

## Slovak

Moja milovaná, sladká, jediná nádej! Želám si, aby Vás moje riadky našli v najlepšej nálade, sladká Jolánka. Čo sa týka fotografie, len ju pošlite, či sa vydarila, alebo nie, už len preto, že je na nej aj Ilonka. Lebo by som mal napísať [jedno nerozlúštené slovo], čakám, že fotografiu dostanem. Prosím Vás teda, drahá, pošlite ju čím skôr, za čo Vám vopred ďakujem. Drahá, teraz často chodievam do Újváru, som tam takmer stále. Chcel by som už ísť aj do Hatvanu, už len ten pocit by mi dobre padol, že by som bol blízko Vás, drahá, hoci aj tak by som bol dosť ďaleko. Týmto končím svoje riadky a zostávam až do hrobu Váš verný milý Feri.
Pod známkou: S Bohom, drahá! Bozkáva Vás nespočetnekrát Váš ctiteľ Feri.

## Uncertainties

1. **Row 10 `kihe` / `kipe` — unresolved.** After *írni kéne* (end of row 9) come the clear signs k, dotted i, the long-stroke-plus-right-tick sign (h/p), three bars e, then a gap and *azt*. No fitting word was found, so it stays literal and untranslated. Guesses such as a miswriting of *kép-* ("picture") are not adopted. A further unadopted hypothesis (from review 1) is *írni kéne [ne]ki, de azt várom* ("I ought to write to her, but I am waiting…"), which suits the sentence about Ilonka but costs two writer's errors: *ne* dropped at the row break, and the tick of d put on the wrong side. The sign itself is h/p, not d, so this stays a hypothesis. The sentence around it (*Mert írni kéne … azt várom…*) is therefore uncertain in its link; everything else in it is clear.
2. **Under the stamp: restorations.** The text lies under the removed stamp; three tear patches hide signs, and the ink is faint. Restored: row S1 *t* of *isten* (wholly under the tear); S2 the *e* before *m* in *édesem* (under the tear, some bar traces); S6 the *i* of *imádója* (only its dot is visible above the tear); S7 *f* of *Feri* (wholly hidden) and *e* (two bar ends show at the tear edge). In each case one letter gives the word. Also faint and read with word sense: the first sign of S1, the third sign of S2 (only two short bars are visible, so literally a, *leadesem*; read as e of *vele édesem*, assuming a lost faint bar or a slip), the z of S4, *la* of S5, the last sign of S5 (top bar and stem visible, no mid-bar, so literally t; read as r of *számtalanszor*, assuming a lost bar), the last sign of S7 (a cross, taken as i, whose dot is not seen; the sense relies on the signature in row 26). In S3 no *-om* follows *csókol*: there is clean paper after the l, so it is third person, *csókol … imádója Feri*.
3. **Row 12 `t` of *tehát*:** the sign is a tall gamma whose stem crosses the bar, close to a cross. Read as t from word sense; the f value would give no word.
4. **Row 26 `r` of *Feri*:** an F with a curled stem and no straight stem. Read as r from word sense and from the family signature (HCP1212, 1216). The first sign is a tilted cross, partly over the portal stamp, as at HCP1216 row 21.
5. **h/p calls resting on word sense:** *fényképet* (rows 5, 11), *megkapjam* (row 11) take p; *hogy, tehát, Hatvanba, magához, hű, kihe?* take h. **u/z:** the heavy cross and the thin tailed cross are normally distinct, but the calls were also confirmed by sense (*azért, az, érzés, közel, magához, messze* against *küldje, sikerül, Újvár*). Row 13 *küldje* shows no dots on the cross; the ü is supplied.
6. **Row 4:** *édes* is followed by *es*. The s of *édes* is an over-inked blot, apparently rewritten, and the writer restarted: literal *edeses*, normalized *édes*.
7. **Row 25 start, corner:** the first e and the second z are cut by the rounded corner or smudged, but their outlines are visible. Literal *ezze*: the l of *ezzel* is not on the card. The word break *ezze(l) zárom* is editorial.
8. **Row 18 `szetnek`:** the signs are clear; I normalize to *sze[re]tnék* (writer dropped *re*). This is an interpretation of a misspelling; *szeretnék* fits the sentence, and I found no better word.
9. **Row 20 `ijjol`:** normalized *i[s] jól*, taken as a writing slip (s dropped, j doubled); no phonetic explanation is claimed. Word boundary and sense (*már az érzés is jól esne*) are editorial.
10. Other normalizations: *szeretet edes* → szeretett édes, *ileti* → illeti, *majnem* → majdnem, *ot* → ott, *meszevolnek* → messze volnék, *barakoris* → bár akkor is, *kedvesse* → kedvese (two right bowls written, the second looking the same as the first). The two *már* of rows 18 and 20 belong to different clauses: *szeretnék már … menni*, then *már az érzés is jól esne* ("the very feeling would do me good"); there is no repetition. Accents are supplied where ticks are not clear; the ledger does not transcribe them.
11. **Places and people.** *Újvár* is not identified (several Hungarian towns carry the name). *Hatvan* is near the addressee's Jászárokszállás, which fits *közel*. *Ilonka* is otherwise unidentified. No identification of Feri beyond the family's sender is claimed.
12. **Not enciphered, for the record.** Address side, plain cursive: *Szépreményű / Tóth Jolánka / úrleánynak / Jászárokszállás* (the first and last read at reduced confidence, the last partly under the portal stamp). Cancellation: year ending *913*; a clear B and a following stroke at the top of the right-hand cancellation and an F at the bottom are visible, but no place name is claimed. Picture side, printed: *Szerelem törvénye. 5. §.* and *Csókolni nem bűn-engem!*; no cipher there.
13. **Small writing accidents.** Row 12 has a short fourth stroke after the three of *m*, not in the ledger; it may be a comma-like mark. The k of row 11 *megkapjam* is a heavy blot and the o of row 24 *volnék* is overwritten; both remain readable.

## Why it is correct

- The HCP1216 key, unchanged, turns all 491 ledger signs (486 seen, 5 restored under the stamp tear, item 2) into Hungarian with no sign left without a value; only one word (row 10) has no meaning found.
- Repeated words decode identically in separate places: *hogy* ×4, *fényképet* ×2, *édesem* ×4, *soraim* ×2, *küldje* ×2, *már* ×3, *volnék* ×2.
- The prose is coherent and idiomatic for a 1913 love letter with formal address (*találja, küldje, magához*). Its formulas (*legjobb kedvében találja soraim*, *mit előre is köszönök*, *sírig hű kedvese*, *Isten vele*, *imádója*) match the family; the sense runs on across row breaks (*re|ményem, raj|ta, köszö|nök, gyak|ran*).
- The visible signs under the stamp give the family's usual closing formulas (*Isten vele*, *csókol*, *számtalanszor*, *imádója*), as on HCP1216 and HCP1213.

## Response to review 1

Verdict REVISE. I rechecked findings 1, 2, 3, 7 and 9 on the reviewer's crops of the hires original (`review/work/z_r16end.png`, `z_s2_e.png`, `z_s_s5.png`, `z_r11_12_end.png`, `z_pm.png`) and agree with all nine findings. The decoded reading is unchanged apart from one literal letter and one comma.

1. **Row 16 last sign (major): fixed.** The sign after the six has exactly two bars, so it is a. `work/ledger.txt` row 16 now ends `F B A`; the literal block says `ujvarba`; the false misspelling *Újvárbe* is gone from item 10. Normalized *Újvárba* stands and is now literal. I had misread it.
2. **S2 third sign (minor): disclosed** in item 2, and in the ledger header. Two short bars show; kept as e by word sense.
3. **S5 last sign (minor): disclosed** in item 2, and in the ledger header. Top bar and stem show, no mid-bar; kept as r by word sense.
4. **Comma rows 19-20 (minor): fixed** in `work/normalized.txt`, the Hungarian text and item 10: *…Hatvanba is menni, már az érzés i[s] jól esne*. The English and Slovak already meant this and stay as they are.
5. **`ijjol` (minor): fixed.** Item 9 now calls it a writing slip and claims no assimilation.
6. **Row 10 candidate (minor): recorded** in item 1 as unadopted, with its two costs. The word stays unresolved.
7. **Writing accidents (minor): recorded** as new item 13.
8. **Sign count (minor): fixed.** "Why it is correct" now says 486 seen and 5 restored.
9. **Cancellation (minor): fixed.** Item 12 states the visible B, stroke and F and claims no place name.

Re-run after the fixes: `python3 -I ciphers/hcp-1317/work/decode.py` passes all four hash checks, reports 491 signs and prints `ujvarba` in row 16.
