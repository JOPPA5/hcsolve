# HCP1238 — Feri to Tóth Jolánka: toothache and a bad year (PARTIAL)

**Status: PARTIAL. No DONE marker.** Claude Opus 5.5, 2026-11-02. No earlier work on this number; portal status Not solved, no attached solution.

## Cipher and key
Hungarian simple monoalphabetic substitution with graphic signs, the Jolánka family key as on FINAL card hcp-1216 (table there), transferred unchanged. Calls resting on word sense: h/p/d (stroke plus tick) throughout; loop-shaped i versus o in "pedig"; "dogozun" third letter.

**Type note (2026-11-03, Claude Opus 5.5):** cipher type is **MASC + Steganography**: the stamp has been torn away (only the green frame remnant is left) and a seven-row message in the cipher signs is written in the stamp box, where the stamp hid it (see "Stamp-box message (2026-11-03)"). This card has no register entry; none is created.

## Reproduction
`python3 -I ciphers/hcp-1238/work/decode.py` checks the scan hashes and prints the row ledger `work/ledger-opus.txt` (a manual transcription made from enlarged pixels; earlier-family key known, not blind).

## Hungarian (normalized; [...] = unread)
Szeretet[t] édes Jolánkám! Kívánom, hogy a legjobb egészségben és kedvében találja soraim. Hogy telt el az új eszt[end]ő első napja? Nekem a legjobban telt, mert éjfél után [5?/k?] percz el[?]kezdet[t] a fogam fájni, és azóta fo[l]yton fáj. Már vet[t]em fo[g]cseppet is, és nem akar kiálni. Nó de bízunk az Istenb[en], talán [unread, about four signs] jobban fog [row 11 unread, about 14 faint signs] [m]últ évétől. [Letiörülök — sense uncertain, contains "örülök"], hogy e mert hogy [je- / ledene: not understood] nagyon rossz esztendő volt, sok nélkülözés, semmit nem felejtek el soha, kedves Jolánkám. Már negyedszer fogok hozzá ez írás[hoz], hisz úgy el vagyok foglalva, hogy meg[-meg]halni se érek rá, és nem tudok mit írni, mivel nincs semmi újság, csak do[l]gozun[k] fo[l]yton, se ünnep, se vasárnap. Lapot sem kaptam, mer[t] lassan két hete, pedig nagyon várom. Ezzel bezárom soraim, maradok szerető kedvese Feri.

Under the stamp: Csókol[om] számtalanszor [row hidden by the printed triangle] hű kedvese Feri.

Plain pencil, address side: "Szépen kérem" (partly under the postmark, reading tentative); Tóth Jolánka úrleánynak; place line (Jászárokszállás per the portal file name, the scrawl itself not verified letter by letter).

## English
Beloved sweet Jolánka! I wish that my lines find you in the best of health and spirits. How did the first day of the new year pass? For me it went best of all, because a few minutes after midnight my tooth started to ache, and it has ached constantly since. I have already bought tooth drops too, and it will not stop. Well, we trust in God, perhaps [unread] better [unread] last year. [Unclear words, including "I am glad"] that it was a very bad year, much hardship; I will never forget anything, dear Jolánka. This is already the fourth time I set about this writing, for I am so busy I have no time even to die, and I do not know what to write, since there is no news, we just work constantly, neither holiday nor Sunday. I have received no card either, for nearly two weeks, though I wait very much. With this I close my lines; I remain your loving sweetheart, Feri. Under the stamp: kisses countless times [hidden], your faithful sweetheart, Feri.

## Slovak
Milovaná sladká Jolánka! Želám, aby Vás moje riadky našli v najlepšom zdraví a nálade. Ako prešiel prvý deň nového roka? Mne najlepšie, lebo pár minút po polnoci ma začal bolieť zub a odvtedy bolí stále. Už som si kúpil aj kvapky na zuby a neprestáva. No dôverujeme v Boha, možno [nečítané] lepšie [nečítané] minulý rok. [Nejasné slová, medzi nimi „teším sa“], že to bol veľmi zlý rok, veľa strádania; nikdy na nič nezabudnem, drahá Jolánka. Už po štvrtý raz sa dávam do tohto písania, veď som taký zaneprázdnený, že ani umrieť nemám čas, a neviem, čo písať, lebo nie je nič nové, len stále pracujeme, ani sviatok, ani nedeľa. Ani lístok som nedostal, už skoro dva týždne, hoci veľmi čakám. Tým končím svoje riadky, ostávam Váš milujúci milý Feri. Pod známkou: bozkáva nespočetnekrát [zakryté], Váš verný milý Feri.

## Stamp-box message (2026-11-03)

Checked by Claude Opus 5.5 on 2026-11-03 from `work/hires/*_adr.jpg` (crops at 2x and 4x, with a blue-ink suppression pass, in `work/stamp-2026-11-03/`). State: stamp lifted (torn; green frame fragments remain at the edges), with writing under it. Script: cipher signs only, same Jolánka key; no plain Hungarian in the box. A blue triangular ink impression (eye in rays) was put on the box over the pencil and covers the middle of it.

Literal (one line per written row, as in `work/ledger-opus.txt` S1-S7):
```
S1 {c}sokol      S2 omsza      S3 mtalan      S4 szor
S5 ?????         (under the blue triangle; only stray stroke ends show left and right of it)
S6 hukedv-       S7 (v)ese{..}feri   (the v of kedvese begins S7; one or two signs between "ese" and "feri" are under a green frame fragment)
```

- Hungarian (normalized): Csókolom számtalanszor [one row unread, hidden by the triangle] hű kedvese, Feri.
- English: I kiss you countless times [one row unread] your faithful sweetheart, Feri.
- Slovak: Bozkávam Vás nespočetnekrát [jeden riadok nečítaný] Váš verný milý, Feri.

Unread: row S5 (about four to five signs) lies under the dense blue ink and cannot be separated from it in this scan (channel separation and blue suppression tried). The parallel card hcp-1216 has "sírig" ("unto the grave") in the same place; that is a plausible restoration of a whole word, not one hidden letter, so it is **not** claimed. The reproduction script was not changed; the stamp rows are read by eye (they are already in the ledger as S1-S7).

## What stops completeness
1. Row 10 middle and all of row 11: rubbed pencil. A whole clause is unread, so this is partial.
2. Rows 12-13: "letiörülök" and "ledene/jelede" not understood; signs themselves are clear.
3. Row 5 under stamp: hidden by the printed triangle (S5); "sírig" as on hcp-1216 is possible but not claimed.
4. Row 6 sign before "percz" could be k (két, "two") or digit 5. Row 3 "találja" is literal "talalja" with one extra wave-like smudge possible. Row 4 "eszt-ő" has no visible -end-.
5. Row 16-17 "ez irs / hiz" and row 25 stroke counts (nagyom, stray stroke) are literal; the normalized forms are editorial. Row 8 "focsepet" as fo[g]cseppet rests on sense. Row 14 "nélkülözésemmit" is divided as nélkülözés / semmit with one s shared, by sense. The date is not read from the postmark.

## Why the read part is right
The unchanged family key gives continuous, idiomatic Hungarian over about 95 percent of the signs, repeated forms agree ("fojton" twice, "hogy", "Jolánkám" twice), the closing matches the Feri signature on hcp-1216, and the New Year topic is self-consistent. Sender Feri is the same first name as on hcp-1216; identity is not proven.
