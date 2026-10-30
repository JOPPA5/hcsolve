# HCP1303 — Feri to Jolánka Tóth: out of work in Pest, home by 10 April for the draft

**Status: complete reading of all ciphertext; review 1 verdict REVISE, findings addressed below; the cipher reading did not change.** Solver: Claude Opus 5.5, 2026-10-30. There was no earlier work on this number. The portal shows status *Not solved* and attaches no transcription or solution; the orchestrator's AI-register check of 2026-10-30 found no record. No published solution was seen, and I did not search further.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family, same key as HCP1212, 1213, 1216, 1217, 1218, 1243, 1301 (transferred from the legend in `ciphers/hcp-1216/SOLUTION.md`, not re-derived). The key is known from those cards; only the reading of this card is new.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S-curve | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls ( ) | cs | three short strokes | m | gamma/corner | t |
| short + long stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron (1-shaped) | v |
| upright cross + | f | tall stroke + short tick | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | | | | |

There is no separate gy sign on this card: *gy* is g + y, and in *Gyöngyös* an enlarged g joined to an ordinary y. Dots over the x and the loop give ü, ö; a tick over a sign marks an accent. Word spaces are not written. The card also has plain (unenciphered) parts: the address side's address, `10 er` in row 10, and the two bottom pencil lines.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1303/work/decode.py
```

It checks the SHA-256 of all four image files, decodes the manual sign ledger `work/ledger.txt` (16 rows plus the 5 rows in the stamp box) and prints the literal rows, then prints `work/normalized.txt`. The ledger is a manual reading from enlarged crops of the original scan, not OCR; it was made while reading for sense, so it is not blind. Literal output (`h` = the h/p sign, `<...>` = written in plain):

```
01 szeretetedesjo          09 sétalokegyhar
02 lankakivanom            10 hetigahr.<10><er>haz.a
03 hogyalegjobb            11 megyekmertsoro
04 kedvebentalálja         12 zasleszegeszelfe
05 soraimenmost            13 lejtetemakonyvet
06 hestentartoz            14 hatehtiküljbeszüleimnekhavalaki
07 kodommunkaaz            15 bemegygyöngyosremíujságárokszá
08 itsincsheazert          16 lasonhavanírjon
stamp box: isten | vele | edesem | imado | jaferi
```

## Hungarian (normalized)

Szeretett édes Jolánka! Kívánom, hogy a legjobb kedvében találja soraim. Én most Pesten tartózkodom. Munka az itt sincs, de azért sétálok egy pár hétig. Ápr. 10-ér[e] hazamegyek, mert sorozás lesz. Egész elfelejtettem: a könyvet, ha teh[e]ti, küld[je] be szüleimnek, ha valaki bemegy Gyöngyösre. Mi újság Árokszálláson? Ha van, írjon.

Plain pencil, bottom: Cím: Holes Fe[...], [4 or 8] Népszínház u. 16, Asztalosok szak[...]

Stamp box: Isten vele, édesem! Imádója, Feri.

Address side, plain: Szépreményű Tóth Jolánka urileánynak, Jász-Árokszállás.

## English

My beloved sweet Jolánka! I hope my lines find you in the best of spirits. I am now staying in Pest. There is no work here either, but I shall still stroll about for a couple of weeks. By 10 April I am going home, because there will be the draft (army conscription). I quite forgot: the book, if you can, please send it in to my parents when someone goes in to Gyöngyös. What is new in Árokszállás? If there is anything, write.

Address: Holes Fe[...], [4 or 8] Népszínház utca 16, Joiners' [trade] sec[tion...].

Farewell, my darling! Your adorer, Feri.

Address: To the promising young lady Jolánka Tóth, Jász-Árokszállás.

## Slovak

Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky zastihli v tej najlepšej nálade. Teraz sa zdržiavam v Pešti. Práca nie je ani tu, ale aj tak sa ešte pár týždňov poprechádzam. Do 10. apríla idem domov, lebo bude odvod (branci). Celkom som zabudol: knihu, ak môžete, pošlite mojim rodičom, keď niekto pôjde do Gyöngyösu. Čo je nové v Árokszállási? Ak je niečo, napíšte.

Adresa: Holes Fe[...], [4 alebo 8] Népszínház u. 16, stolári, odb[or...].

S Bohom, drahá! Váš ctiteľ Feri.

Adresa: Nádejnej slečne Jolánke Tóthovej, Jász-Árokszállás.

## Uncertainties

Calls resting on word sense, not on the shape alone:

1. **h/p sign.** Taken as p in *Pesten* (r6), *pár* (r9) and *ápr.* (r10), as h elsewhere (*hogy, hétig, haza, ha, teheti, havan*).
2. **Row 8 *de*.** The first sign is a tall stroke with a short tick (the h/p class), not the short + long d of *édes* or *kedvében*. *De azért* is the only sense. The same irregularity is disclosed on HCP1216.
3. **Row 14 first sign.** The tall stroke has a hooked top, a variant of the h sign, read h from *ha teheti*.
4. **Row 13 *elfelejtetem*.** The sign before *a könyvet* is two strokes plus a short tick; read as m. The n in *könyvet* is heavily overwritten (a dark blot of two strokes); it is read from the word, and the o shows no dots. These are readings of the visible but damaged signs.
5. **Row 16 first sign.** A wave joined to a long low descender, not a plain l: either a variant l or an l + y merge. It is read as l of *Árokszá|láson*. The place name fixes the sense either way; the normalization restores the double l.
6. **Row 16 *írjon*.** The j is overstruck with a crossed correction; its base stroke and foot are visible. Read from the word (*ha van, írjon*).
7. **Row 15, signs under the portal watermark.** The a of *Árok-* sits inside the printed O, and the *h* of *ha valaki* (row 14) and the r, o, k, s, z, a of *Árokszá* are crossed by the printed letters. The pencil strokes remain visible through them. In *Árok-* the bar count (a versus e) is partly under the O and rests on the name.
8. **Both f signs on this card rest on word sense.** Neither is the upright cross of the key table. The f of *elfe-* (r12) is a slanted x with an added right arm; the f of *Feri* (stamp box, s5) is a tilted cross of the same kind. Both differ from the plain x (u) of r7 only by that arm or tilt. Each is read from its word. **Stamp box, other signs.** The first sign of *Imádója* is faint and shows no dot. The bottom bar of the e of *Feri* is broken into a dash and a dot.
9. **Editorial normalizations:** *szeretet* → szeretett, *it* → itt, *haz.a* → haza (stray dot), *egesz* → egész, *lejtetem* → -ttem, *tehti* → teh[e]ti (e missing), *külj* → küld[je] (written k-ü-l-j; I take it as a phonetic *küldj*, and the imperative form is not certain), *mí* → mi. Accents are often not visible and are supplied. *10 er* is written in plain, at least *10 ér*: there is a tail after the r running into the next sign and a dot above that may be an accent or a stray. The final e of 10-ér[e] is supplied, not clearly written.

Plain text not fully read (this is not ciphertext):

10. **Bottom plain lines.** *cím* is clear. The surname is read as *Holes*, capital uncertain: it has a crossbar and a foot stroke, closer to this writer's J in *Jolánka* than to an obvious H, and the following *oles* is clear. The next word, under the portal stamp, begins with a crossbar capital of F type and a looped e, then runs on for several letters: *Fe[...]*, plausibly *Ferencz* or similar, ending not legible. The next line begins with a closed upper triangle over a lower loop, a 4 or 8, before *Népszínház u. 16*. Népszínház utca lies in Budapest's district VIII (general knowledge, not checked in a source), so 8 as the district is a candidate, not established. *Asztalosok* is clear; the following word is overwritten and reads *szakosz…* or similar (a trades section is plausible, not established). A further short plain word runs up the right edge (capital T, o, a letter with a descender, then uncertain letters, approximately "Toy…"); it is unresolved. Whether it continues the previous word is unknown.

Context:

11. The portal gives no date and the text has none beyond *Ápr. 10*. The card itself has two postmarks. The round postmark at the upper centre, rotated 180°, reads …ÁROKSZÁ… in the ring (the Jász-Árokszállás office, so struck there) and shows a clear `13` at the right end of the date band; the rest of the band is under the pencil *Szépreményű*. A second, separate, heavy cancellation rings the torn stamp, with an E-like letter and a stroke in the lower arc and an A in the upper arc; its office is not established. `13` may be a year (1913) or a day; the pixels do not decide it. The portal name `cpc_--13_…` points to a day: sister names put the date in that slot as year-month-day (`cpc_1912-05-17_…`, `cpc_1913--_…`), so `--13` looks like a catalogue reading of day 13 with year and month blank. That is the cataloguer's reading, not proof. A 1913 year would fit the 1913 of HCP1213, and conscription and the Pest setting fit the family's years (HCP1212 and 1243 are dated 1912), but no year is claimed. The sender is "Feri"; the same name signs HCP1212, 1213, 1216. Identity of the writers is suggested, not proved. HCP1309 has in cipher, in the same *cím* formula with a plain return address (*Rákos Palota*), the signature *Holes Feri*, its first letter open there between d/h/p; so Holes is in all likelihood the writer's own surname, and this card's plain word and that card's cipher support each other. This is a cross-reference, not proof.

## Why it is correct

- The family key, unchanged, gives Hungarian for every sign in all 16 rows and the stamp box; no sign is left without a value.
- The text is coherent and specific: a job-seeker in Pest, the draft in April, a book to go via Gyöngyös (a real town near Jász-Árokszállás). The name *Árokszáláson* in cipher agrees independently with the plain address on the same card.
- The closing *Isten vele* and *Imádója Feri* match the family's formulas (HCP1213 *Imádja Feri*).
- Repeated words agree: *hogy*, *ha* ×3, *édes-*, *Pest/Gyöngyös* use the same signs; word breaks across rows (*Jo|lánka, tartóz|kodom, soro|zás, elfe|lejtettem*) join into real words.

## Response to review 1

Verdict REVISE, no sign of the cipher reading challenged. I viewed the reviewer's crops for every finding. The reading is unchanged; `python3 -I ciphers/hcp-1303/work/decode.py` still passes all four hash checks and prints identical literal rows after the ledger change.

1. **Postmarks (major): fixed.** `review/work/crops/pm1rot.png` and `pm_c.png` show ÁROKSZÁ in the ring and a clear `13`; `pm2.png` shows the second cancellation. My statement that the card has no date evidence was false and is withdrawn. Item 11 now describes both postmarks and keeps `13` open between year and day, adding one point the review did not make: the portal name `cpc_--13_` has the shape of a date with only the day filled in.
2. **Surname (minor): fixed.** Item 11 now cites HCP1309 *Holes Feri* as a cross-reference. HCP1309's response cites this card for the H in turn, so the two are mutual support, not independent proof of the H.
3. **Word after Holes, capital of Holes (minor): fixed.** `crops/name.png` shows a crossbar capital with a foot stroke, and *Fe…* after it. Item 10 and the normalization now give *Holes Fe[...]*, capital uncertain.
4. **4-like mark (minor): fixed.** `crops/p2.png` shows the closed triangle over a loop. Item 10 gives 4 or 8, with the district VIII idea as an unverified candidate.
5. **f of *elfe-* (minor): fixed.** `crops/r12tail.png` shows the x with a right arm. Item 8 now covers both f signs and calls them sense-based. The ledger keeps F.
6. **GY (minor): fixed.** `crops/d2.png` shows an enlarged g joined to an ordinary y. The ledger now has G Y, the key table no longer lists a gy sign, and the decoded text is the same.
7. **Plain *10 er* (minor): fixed.** `crops/r10er.png` shows the tail after the r. Item 9 says so, and the normalized text is now *10-ér[e]*.

Also corrected in passing: `work/normalized.txt` had *haza[ ]megyek* against *hazamegyek* in this file; both now read *hazamegyek*.
