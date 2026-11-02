# HCP1292 — Feri to Jolánka Tóth (PARTIAL: letters read, one clause not understood)

**Status: partial, no state marker.** Claude Opus 5.5, 2026-10-30. No earlier work exists on this number; no external plaintext was used; the portal shows Not solved with no attached solution.

## Cipher and key
Hungarian, monoalphabetic substitution with invented graphic signs: the Jolánka family key, unchanged from HCP1216, 1212, 1213, 1217, 1218, 1243, 1301 (see the table in `ciphers/hcp-1216/SOLUTION.md`). The small ring is cs, as on HCP1301. Under the torn-off stamp there is a nine-row signed block. The picture side is print only ("Két szív ha földobog", verse). The address (Tóth Jolánka úrleánynak, Jász Árokszállás) is plain handwriting; the Galánta postmark is partly legible.

## Reproduction
```sh
python3 -I ciphers/hcp-1292/work/decode.py
```
It checks the source hashes, then prints `work/ledger.txt` (31 rows and 9 stamp rows, one letter per sign, manual reading of the pixels, not blind to the family key) and `work/normalized.txt`.

## Plaintext (normalized; brackets = unresolved)
See `work/normalized.txt`, which is the Hungarian text:

> Szeretett édes Jolánkám! Becses sorait megkaptam, melynek nagyon megörültem, édesem. Igazán örülök, hogy még önt enyémnek mondhatom. Higgye el, édesem, mennyire fájdalmat okozott az a tudat, hogy el kell vesztenem. [Megated?] és én is borban keresem a vigasztalást, és majdnem az életembe került, mert tegnap éjjel egy kicsit mámoros fejjel mentem szolgálatba, és elaludtam a féken, és az Isten őrzött, hogy a kocsi alá nem kerültem. De azt hagyjuk, mert nem panaszkodni akarok, hanem inkább örömemet kifejezni, hogy újra boldogít az a tudat, hogy remélhetem. Hetek még, édesem, hogy [unresolved, rows 21–23] már sokszor fogadtam hűségem[et] becsületszóval, de úgy [l]átom, az [blacked out] már nem erősít, de így meg azt hiszem, nem vesztettem el becsületemet ön előtt, de annál többet ér az önbecsület [szeveen] előttem. Hogyha esetleg cserbe hagy, ezt a levelet fo[go]m szóról [szororno], de csak esküvője napján, mert addig nem vonom kétségbe szavát, és ezt kérdem: mivel bizonyíthatom be szerelmemet?
> Under the stamp: Isten vele, édesem. Maradok továbbra is kedvese, sírig hű imádója, Feri.

## English
My beloved sweet Jolánka! I received your valued lines, which made me very glad, my darling. I am truly happy that I can still call you mine. Believe me, darling, how much pain the knowledge caused that I must lose you. [?] and I too seek consolation in wine, and it nearly cost me my life, for last night I went on duty a little tipsy and fell asleep on the brake, and God preserved me from falling under the wagon. But let us leave that, for I do not want to complain but rather to express my joy that the knowledge makes me happy again that I may hope. Weeks yet, my darling, that [unresolved] I have many times sworn my fidelity on my word of honour, but I see that the [blacked out] no longer strengthens, yet even so I believe I have not lost my honour before you, but self-respect is worth all the more [?] to me. If you should happen to abandon me, this letter I shall [?] word for word [?], but only on your wedding day, for until then I do not doubt your word, and I ask this: how can I prove my love?
Under the stamp: God be with you, my darling. I remain still your sweetheart, faithful to the grave, your admirer, Feri.

## Slovak
Moja milovaná, sladká Jolánka! Vaše vzácne riadky som dostal a veľmi som sa im potešil, drahá. Naozaj sa teším, že Vás ešte môžem nazývať svojou. Verte mi, drahá, akú bolesť mi spôsobilo vedomie, že Vás musím stratiť. [?] a aj ja hľadám útechu vo víne, a takmer ma to stálo život, lebo včera v noci som išiel do služby trochu podnapitý a zaspal som na brzde, a Boh ma ochránil, že som sa nedostal pod vozeň. Ale nechajme to, lebo sa nechcem sťažovať, ale skôr vyjadriť radosť, že ma opäť oblažuje vedomie, že smiem dúfať. Ešte týždne, drahá, že [nevyriešené] už mnohokrát som na čestné slovo sľúbil vernosť, ale vidím, že [začiernené] už neposilňuje, no aj tak si myslím, že som pred Vami nestratil česť, ale o to viac má pre mňa cenu sebaúcta [?]. Ak by ste ma náhodou opustili, tento list [?] slovo od slova [?], ale len v deň Vašej svadby, lebo dovtedy nespochybňujem Vaše slovo, a pýtam sa: čím môžem dokázať svoju lásku?
Pod známkou: S Bohom, drahá. Zostávam naďalej Váš milý, do hrobu verný ctiteľ, Feri.

## Why it stops at partial
1. **Rows 21–23 (main gap):** signs read as `jelhogysen{?}ifelvasztesnak {a}lanyovolnemtudokésém / [blot]nifelelanyrol`. Only *hogy*, *nem tudok* and *-ról* are sure; I could not form a sentence and do not force one. One sign in row 21 lies in a stain, the first sign of rows 22 and 23 are unclear.
2. **Row 8 `megated-`** before *és én is*: no word found.
3. **Rows 28–29 `szeveenel-lötem`:** *előttem* ("to me") is likely; `szeveen` (signs clear) is unexplained, perhaps a form of *szavánál*. Rows 29–30 `fom szorol szorornö`: *fo[go]m szóról szóra* is a guess and the verb is missing.

## Smaller points
- Writer's slips kept in the ledger, normalized editorially: *Jolakám* (n omitted), *inkam* for *inkább*, *hihetom*-type `bizonyihetom`, *fajezni*, *sokzor*, *vom* for *vonom*, *ers-emit* for *erősít* (word sense), *feken* = *féken* (word sense; fits railway duty with *kocsi*).
- Under stain, read from traces or word sense: g in row 2, z in row 4, v in row 27, r in row 17 (faint). Blot before *-am/-em* in row 9. Row 25 `{l}`: an o-like loop with a long stroke, read l by word sense. Chevron/gamma (t/v) calls rest on word sense in rows 5, 18. h/p and d/n calls rest on word sense throughout (*kaptam*, *panaszkodni*, *de*).
- Row 24 has an extra stroke after *hűségem*. Row 25 ends in a thoroughly blacked-out word.
