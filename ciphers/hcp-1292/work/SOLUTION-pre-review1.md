# HCP1292 — Feri to Jolánka Tóth: rumour of a railwayman's daughter (whole card read; one lone word open)

**Status: complete reading submitted for review (DONE1), revised 2026-11-02.** Claude Opus 5.5 (2026-10-30, revised 2026-11-02). No earlier work exists on this number; no external plaintext was used; the portal shows Not solved with no attached solution.

## Cipher and key
Hungarian, monoalphabetic substitution with invented graphic signs: the Jolánka family key, unchanged from HCP1216, 1212, 1213, 1217, 1218, 1243, 1301 (see the table in `ciphers/hcp-1216/SOLUTION.md`). The small ring is cs, as on HCP1301. Under the torn-off stamp there is a nine-row signed block. The picture side is print only ("Két szív ha földobog", and the verse "Tavasszal szép minden virág …"). The address (Szépreményü Tóth Jolánka úrleánynak, Jász Árokszállás, a courtesy formula "of fair promise") is plain handwriting; the top line "Szépreményü" was overlooked on 2026-10-30. The postmark is partly legible (…GALÁNTA).

## Reproduction
```sh
python3 -I ciphers/hcp-1292/work/decode.py
```
It checks the source hashes, then prints `work/ledger.txt` (31 rows and 9 stamp rows, one letter per sign, manual reading of the pixels, not blind to the family key) and `work/normalized.txt`.

## Plaintext (normalized; square brackets = editorial)
From `work/normalized.txt`:

> Szeretett édes Jolánkám! Becses sorait megkaptam, melynek nagyon megörültem, édesem. Igazán örülök, hogy még önt enyémnek mondhatom. Higgye el, édesem, mennyire fájdalmat okozott az a tudat, hogy el kell vesztenem. [Megát?], édes, én is borban kerestem a vigasztalást, és majdnem az életembe került, mert tegnap éjjel egy kicsit mámoros fejjel mentem szolgálatba, és elaludtam a féken, és az Isten őrzött, hogy a kocsi alá nem kerültem. De azt hagyjuk, mert nem panaszkodni akarok, hanem inkább örömemet kifejezni, hogy újra boldogít az a tudat, hogy remélhetek még, édesem. [Higgye] el, hogy semmiféle vasutasnak a lányáról nem tudok, és semmiféle lányról. Már sokszor fogadtam hűségem[et] becsületszóval, de úgy [l]átom, az [blacked out] már nem ér semmit, de így meg azt hiszem, nem vesztettem el becsületemet ön előtt, de annál többet ér az ön becsületszavánál előttem. Hogyha esetleg cserbe hagy, ezt a levelet fo[go]m szóról szóra, no de csak esküvője napján, mert addig nem vonom kétségbe szavát, és ezt kérdem: mivel bizonyíthatom be szerelmemet?
> Under the stamp: Isten vele, édesem. Mara[do]k továbbra is kedvese és sírig hű imádója, Feri.

## English
My beloved sweet Jolánka! I received your valued lines, which made me very glad, my darling. I am truly happy that I can still call you mine. Believe me, darling, how much pain the knowledge caused me that I must lose you. [?], sweet one, I too sought consolation in wine, and it nearly cost me my life, for last night I went on duty a little tipsy and fell asleep on the brake, and God preserved me from falling under the wagon. But let us leave that, for I do not want to complain but rather to express my joy that the knowledge makes me happy again that I may still hope, my darling. Believe me that I know of no railwayman's daughter of any kind, nor of any girl at all. I have already many times sworn my fidelity on my word of honour, but I see that [blacked out] is no longer worth anything, yet even so I believe I have not lost my honour before you, and that [honour] is worth all the more to me than your word of honour. If you should happen to abandon me, this letter I shall [hold / keep to; no other verb is written] word for word, well, but only on your wedding day, for until then I do not doubt your word, and I ask this: how can I prove my love?
Under the stamp: God be with you, my darling. I remain still your sweetheart and your admirer faithful to the grave, Feri.

## Slovak
Moja milovaná, sladká Jolánka! Vaše vzácne riadky som dostal a veľmi som sa im potešil, drahá. Naozaj sa teším, že Vás ešte môžem nazývať svojou. Verte mi, drahá, akú bolesť mi spôsobilo vedomie, že Vás musím stratiť. [?], milá, aj ja som hľadal útechu vo víne, a takmer ma to stálo život, lebo včera v noci som išiel do služby trochu podnapitý a zaspal som na brzde, a Boh ma ochránil, že som sa nedostal pod vozeň. Ale nechajme to, lebo sa nechcem sťažovať, ale skôr vyjadriť radosť, že ma opäť oblažuje vedomie, že ešte smiem dúfať, drahá. Verte mi, že o nijakej dcére železničiara neviem, ani o nijakom dievčati. Už mnohokrát som na čestné slovo sľúbil vernosť, ale vidím, že [začiernené] už nemá žiadnu cenu, no aj tak si myslím, že som pred Vami nestratil česť, a tá má pre mňa o to väčšiu cenu než Vaše čestné slovo. Ak by ste ma náhodou opustili, tento list si budem [držať; iné sloveso nie je napísané] slovo od slova, no ale len v deň Vašej svadby, lebo dovtedy nespochybňujem Vaše slovo, a pýtam sa: čím môžem dokázať svoju lásku?
Pod známkou: S Bohom, drahá. Zostávam naďalej Váš milý a do hrobu verný ctiteľ, Feri.

## Revision 2026-11-02 (Claude Opus 5.5)
New crops from `work/hires/…adr.jpg` (red channel, autocontrast, 3 to 6x; `work/rev2/`). The old files are kept as `work/ledger-2026-10-30.txt`, `work/normalized-2026-10-30.txt`, `work/SOLUTION-2026-10-30.md`. All three earlier gaps are closed except one lone word.

What changed:
1. **Rows 21–23.** The old `vasztesnak` was misread: the crossed sign is plain x = u (the z sign has a tail), and the bars after t are two = a, giving v-a-s-u-t-a-s-n-a-k, *vasutasnak* (of a railwayman), which fits the writer's own job. Old `sen{?}i`: a pale third stroke stands in the stain after the two strokes, spaced like the others, so the sign is three strokes m: *se-m-i-fél*, a one-m spelling of *semmiféle* with the final e dropped. Old `lanyovol`: at 5x this sign has a stem and two arms and is F = r, not the chevron: *a lanyorol*, normalized *a lányáról* (the o for á is editorial). Row 22 end: two separate bowls, *és sem-*, not `ésém`. Row 23: the blot sits on the first stroke and two strokes show after it. **Restoration of a physically hidden sign:** three strokes m, giving *[m]i-fele*, with the row break *sem|mi-fele lányról*. The parallel *semmiféle … semmiféle* supports it.
2. **Row 20.** `hetam hetek` is a self-correction after *remél-*: normalized *remélhetek még*, not "Hetek még". So the earlier "Weeks yet" is withdrawn.
3. **Rows 20–21 `hogy jel`.** The sign before g-y is an undotted o (checked at 5x), and the next signs are j e l. In the same position, row 5 has *higyje el*. I normalize **[Higgye] el** as a writer's slip. This rests on word sense and the row-5 parallel, not on the sign. Literal text: *hogy jel, hogy*.
4. **Row 8.** Old `megated és` was divided wrongly: m e g á t | é d e s | é n i s, so *… édes, én is*. Row 9's first sign (old blot) is a stained t with two bars, *keres|tam* = *kerestem* (past tense; the a for e is editorial).
5. **Row 26.** `ersemit` is *ér semmit* ("is worth anything"), not *erősít*.
6. **Row 28.** `szeveen` is z with two bars, then the chevron under the stamp imprint, two bars, é, n, e, l: `szavaénel`, read with the unbroken *ön* as *az ön becsületszavánál* (than your word of honour), replacing "önbecsület". The chevron stays visible through the stamp imprint; the -é- is an unexplained extra sign. The ending *-nél* for *-nál* is normalized.
7. **Rows 29–30.** The grey sign before *de* is undotted o, not ö: *szor-or no de csak*. Read as **szóra, no de csak** ("word for word, well, but only …"): *no de* is an ordinary Hungarian interjection, and the F in place of a in *szora* is treated as a slip. Word division and that slip are interpretation.
8. **Under the stamp.** Row 6 is *se és si-*, so *kedvese és sírig hű imádója*; the old text dropped *és*. Row 3 *marak* is normalized *mara[do]k*; row 4 has e, not a (*vebra* for *-ábbra*).
9. **Address side.** The top line in plain handwriting is *Szépreményü*, not recorded before.

## What stays open
- **`megát` (row 8)** is the one un-understood word, all signs clear and alone in a clause that otherwise reads. *Magát* with the writer's e for a (compare *szevét* = *szavát*, row 31) was considered and not adopted.
- **Rows 29–30** have no separate main verb: *fom* = *fo[go]m* (the writer often drops letters) stands alone, so the clause means "I shall hold/keep this letter word for word" at most. The intended act on the wedding day is not stated, and a word may have been left out by the writer. No sign is unread here.
- **Row 25** ends in a word thoroughly blacked out by the writer; its letters are not recoverable and it is not needed for the syntax (*az … már nem ér semmit*).

## Smaller points
- Writer's slips kept in the ledger, normalized editorially: *Jolakám* (n omitted), *inkam* for *inkább*, *bizonyihetom*, *fajezni*, *sokzor*, *vom* for *vonom*, *feken* = *féken* (word sense; fits railway duty with *kocsi*), *szevét* = *szavát*.
- Under stain, read from traces or word sense: g in row 2, z in row 4, t in row 9, v in row 27, r in row 17 (faint), first a of row 22, l of *lanyorol* (wave crossed by a stain). Row 25 `{l}`: an o-like loop with a long stroke, read l by word sense. Chevron/gamma (t/v) calls rest on word sense in rows 5, 18. h/p and d/n calls rest on word sense throughout (*kaptam*, *panaszkodni*, *de*).
- Row 24 has an extra stroke after *hűségem*.

## Why it is correct
The family key is unchanged, every row yields Hungarian with the writer's usual letter drops, and the revised readings came from sign-level corrections (x = u, F = r, three strokes = m) that the key already defines. Content agrees across the card: railway duty and brake (rows 11–13), *vasutasnak* (row 21), fidelity and word of honour (rows 24–28), the wedding-day threat (rows 29–30). The farewell matches *sírig hű* on HCP1216. The ledger is manual and not blind to the family key.
