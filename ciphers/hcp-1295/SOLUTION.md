# HCP1295 — Letter to Jolánka Tóth about a song evening, Úrnapja 1912 (PARTIAL)

**Status: PARTIAL. No marker created.** Every sign on the card is transcribed and about 90% of the text reads as clear Hungarian, but one clause (rows 20–22) and four shorter spots do not yet yield words. Worked by Claude Opus 5.5, 2026-10-30. No earlier work on this number. No published solution found; the portal shows Not solved and attaches none.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented signs: the Jolánka family key, unchanged from `ciphers/hcp-1216/SOLUTION.md` (family cards 1212, 1213, 1217, 1218, 1243, 1301). It was tested here, not assumed: it produced Hungarian at once from row 1. Accents appear as marks over o/u (ö, ü, ő) and are otherwise unwritten. The left panel is one block, read first; the top-right block follows; a bottom line runs across the whole card; the stamp space holds "Isten vele édesem" in **clear** script, then enciphered closing words.

Card-specific sign notes:
- i and o are near-homographs (both loop signs); they differ by a dot, which is sometimes missing (row 12 *igazán*, rows 13 and 16). Those calls rest on word sense.
- The tall stroke + tick group covers h, p and d here (*hogy*, *kapja*, *mondja*). Which letter is meant rests on word sense in every case. The ledger writes h unless the word is clear.
- Section sign k often has a dot below it (rows 3, 18, T1, S1): a variant, no separate value.
- A tilted cross with marks stands for ü in row 8 (*örülök*).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1295/work/decode_opus.py
```

It checks the SHA-256 of both source files and both hires originals, validates and prints the sign ledger `work/ledger-opus.txt` (the signs have no ASCII form, so the ledger stores key values; it is a manual reading from pixels), then prints `work/normalized-opus.txt`.

## Hungarian (normalized; {…} = unresolved, literal letters)

Édes egyetlen reményem! Becses sorait köszön[e]ttel megk[aptam], mely nagy örömömre szolgált. De ha azt írta volna, hogy eljön, sokkal jobban örültem volna. Magáról, édese[m], megfe[led]kezni én nem tudom. {h.oksoh…} annak i[s] örülök, hogy a meghívó örömére szolgált. {e…ö} a gyászt {letö?}, én csak dalestélyre hívtam Önt, édesem. Igazán sajnálom, hogy vasárnap várt rám, amint írtam, is nem mehettem le, kedves Jolánka. Azt ne {gyön} rosszul; [rosszul] teszi, ha valamit {a-h-H-akes} nem fogadja el. Én azt gondolom, ha valaki valakit őszintén szeret, a tőle el hódítani nem lehet, ha megérdemli. {azér is telember egész ga-II-hatje} ha vasárnap {bölvében}, akkor majd meglátom, hogy használ a falusi levegő. Tisztel[i] a kedves szüleit.

Ha idejében megkapja soraim, mondja meg Moczárnak: holnap, Úrnapja délután 3 ór[akor] lesz a nyugdíjegylet fiókjának alakulása, jöjjön e[l]. Jó mulatást kív[án].

Isten vele, édesem! *(clear script)* Csókolom számtal[an]szor, viszontlátásra.

## English (readable parts)

My sweet, only hope! I received your esteemed lines with thanks; they gave me great joy. But if you had written that you were coming, I would have been far happier. I cannot forget you, my darling, {…}. I am also glad that the invitation gave you joy. {…} the mourning {…}, I only invited you to a song evening, my darling. I am truly sorry that you waited for me on Sunday; as I wrote, I could not come down, dear Jolánka. {…} you do wrong if you do not accept {…}. I think that if someone sincerely loves someone, that person cannot be won away from them, if they deserve it. {…} if on Sunday {…}, then I will see how the country air is doing you good. [He] respects your dear parents.

If you get my lines in time, tell Moczár: tomorrow, Corpus Christi, at 3 in the afternoon, the branch of the pension association is being founded, let him come. [He/I] wish(es) a good time.

Farewell, my darling! I kiss you countless times, until we meet again.

## Slovak (čitateľné časti)

Moja sladká jediná nádej! Vaše vzácne riadky som s vďakou dostal a urobili mi veľkú radosť. Ale keby ste boli napísali, že prídete, bol by som sa tešil oveľa viac. Na Vás, drahá, zabudnúť neviem, {…}. Teší ma aj to, že Vám pozvánka urobila radosť. {…} smútok {…}, ja som Vás, drahá, pozval len na spevácky večer. Naozaj ľutujem, že ste ma v nedeľu čakali; ako som písal, nemohol som prísť dole, milá Jolánka. {…} zle robíte, ak neprijmete {…}. Myslím si, že ak niekto niekoho úprimne miluje, nedá sa mu ten človek odlákať, ak si to zaslúži. {…} ak v nedeľu {…}, potom uvidím, ako Vám prospieva vidiecky vzduch. [Pozdravuje] Vašich milých rodičov.

Ak moje riadky dostanete včas, povedzte Moczárovi: zajtra, na Božie telo, o 3. popoludní bude založenie pobočky penzijného spolku, nech príde. Praje dobrú zábavu.

S Bohom, drahá! Bozkávam Vás nespočetnekrát, dovidenia.

## Why this stops short of complete

Unresolved, all signs transcribed but no word found; nothing was forced:

1. **Rows 20–22** `azeristeleembere...`: literal *a z e r i s t e l e m b e r e g e s z g a {II} h a t j e*. *azér is* (= azért is) and *ember egész* are visible but the clause does not parse; the first sign of row 22 is smeared and the two strokes after it are unclear. This is the main gap (about 30 letters).
2. **Row 8 opening** `h.ok{s?}oh{box}`: a tall+tick sign with a dot, then o k, a sign like ) with an inner tick, o, a tall+tick sign in a blot, and a bar sign in a stain. No word found.
3. **Row 10 opening** `e II I [o]`: blot hides part; the loop sign under it is seen only by its base and tail. *a gyászt* is clear, the following *letö* is not explained (*letette?* not on the card).
4. **Row 16** `a h H a k e s`: H is a heavy double stroke with a bar, possibly two h/p/d signs run together. No word found.
5. **Rows 22–23** `hab..` *ha vasárnap bölvében*: *ha vasárnap* is clear. Then *bölvében* (or *dölvében*, *hölvében*) may be a place name or a miswriting; not identified. Row 22 *vasarnah* has the h/p sign for the p.

## Smaller points

- Row 7, end: **`{II}{m-curs}`** after *tu*: two short strokes, then a joined cursive m-shape past the panel rule. *tudom* is taken from sense; the signs do not match the key cleanly. Row 7 also has *ennen* = én nem (n for m, word division mine).
- Row 7: the sign after *edese* is under a blot with one final stroke showing. **Restoration** m (*édesem*).
- Row 3 *megk* stops at k; *megkaptam* is expansion, not on the card.
- Row 5: a pink i-sign under a red inverted T: the writer overwrote; read j (*eljön*).
- Row 6: *l* of *volna* is written above the o (interlinear).
- Row 8: only one sign between *annak* and *örülök*, read i; s supplied.
- Row 9 literal *hivoromore*: read *meghívó örömére* (one o shared across the word break, ö for é). *örömömre* is the alternative.
- Row 12 literal *igezan*, no dot on the i; row 14 literal *mehatem*, *kadves*.
- Row 15 literal *gyön*: *azt ne gyön rosszul* does not parse as written (*azt ne vegye rosszul?*). The first *rosszul* / *teszi* division is mine.
- Rows 19–20: *tőle l hódítani*: one l-e for *tőle el*. Row 20: the sign read d of *megérdemli* is a tall pair.
- T3: **`3 {8} or`**: 3, then a heavily inked 8-like sign (a figure or a corrected o?), then *ór*; *3 órakor* is my reading. The ~ sign after it is partly in a tear; the row is smeared by pink ink but *lesz a nyugdíj* can be followed on the green channel (`work/crops/sm3.png`).
- T5: `jö jö e -`: after e a stroke runs into the postmark. *jöjjön el* is interpretation.
- T6: *kív* is clear, then faint strokes in the postmark smear: *án* partly seen, **restoration**.
- S2: `szantal` then ink smear: *számtal[an]szor* is a restoration; n for m is as written.
- Bottom line: *szüleit* is written below the line, under *levegő*, not after *kedvas*; order from sense. The small + after *meglátom* (row 23) has no value assigned (punctuation?). *Tisztel* lacks an ending: tiszteli/tisztelem not decided. The end of *kedvas* has pink streaks across it.

## Why the readable part is believed

- The key was taken unchanged from finished cards and yields continuous Hungarian across the card, including rare words (*nyugdíj*, *alakulása*, *őszintén*, *megérdemli*).
- **Independent date check:** Úrnapja (Corpus Christi) 1912 fell on Thursday 6 June (Easter 7 April + 60 days, computed), the portal's date for this card. The text says *holnap, Úrnapja*, so it was written about the 5th; this was not assumed in advance.
- *Moczár* also appears on another Jolánka card in this repo (found by grep after the reading).
- Address in clear: Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás.
