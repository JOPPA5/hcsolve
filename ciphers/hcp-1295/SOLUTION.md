# HCP1295 — Letter to Jolánka Tóth about a song evening, Úrnapja 1912 (PARTIAL)

**Status: PARTIAL (revised 2026-11-02). No marker created.** Every sign is transcribed and most of the text reads as clear Hungarian. The second attempt closed the main gap (rows 20-22) and rows 15-16, but four spots stay unread: the opening of row 8, the words around *a gyászt* in row 10, the words before *ember* in rows 20-21, and *bö-vében* in rows 22-23. Worked by Claude Opus 5.5, 2026-10-30 and 2026-11-02. No published solution found; the portal shows Not solved and attaches none.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented signs: the Jolánka family key, unchanged from `ciphers/hcp-1216/SOLUTION.md` (family cards 1212, 1213, 1217, 1218, 1243, 1301). It was tested here, not assumed: it produced Hungarian at once from row 1. Accents appear as marks over o/u (ö, ü, ő) and are otherwise unwritten. The left panel is one block, read first; the top-right block follows; a bottom line runs across the whole card; the stamp space holds "Isten vele édesem" in **clear** script, then enciphered closing words.

Card-specific sign notes:
- i and o are near-homographs (both loop signs); they differ by a dot, which is sometimes missing (row 12 *igazán*, rows 13 and 16). Those calls rest on word sense.
- The tall stroke + tick group covers h, p and d here (*hogy*, *kapja*, *mondja*). Which letter is meant rests on word sense in every case. The ledger writes h unless the word is clear.
- Section sign k often has a dot below it (rows 3, 18, T1, S1): a variant, no separate value.
- A tilted cross with marks stands for ü in row 8 (*örülök*).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1295/work/decode_rev2.py
```

It checks the SHA-256 of both source files and both hires originals, validates and prints the sign ledger `work/ledger-rev2.txt` (the signs have no ASCII form, so the ledger stores key values; it is a manual reading from pixels), then prints `work/normalized-rev2.txt`.

## Hungarian (normalized; {…} = unresolved, literal letters)

Édes egyetlen reményem! Becses sorait köszön[e]ttel megk[aptam], mely nagy örömömre szolgált. De ha azt írta volna, hogy eljön, sokkal jobban örültem volna. Magáról, édese[m], megfe[led]kezni én nem tudok. {h.oks?ö?ha} annak i[s] örülök, hogy a meghívó örömére szolgált. {e..ö} a gyászt {öletö}, én csak dalestélyre hívtam Önt, édesem. Igazán sajnálom, hogy vasárnap várt rám, amint írtam, is nem mehettem le, kedves Jolánka. Azt nagyon rosszul teszi, ha valamit adnak és nem fogadja el. Én azt gondolom, ha valaki valakit őszintén szeret, attól elhódítani nem lehet, ha megérdemli. {azéri a tel}ember egész bátran elfogadhatja, ha vasárnap {bö-vében}, ak[k]or majd meglátom, hogy használ a falusi levegő. Tisztel(i) a kedves szüleit.

Ha idejében megkapja soraim, mondja meg Moczárnak: holnap, Úrnapja délután 3 ór[akor] lesz a nyugdíjegylet fiókjának alakulása, jöjjön e[l]. Jó mulatást kív[án].

Isten vele, édesem! *(clear script)* Csókolom számtal[an]szor, viszontlátásra.

## English (readable parts)

My sweet, only hope! I received your esteemed lines with thanks; they gave me great joy. But if you had written that you were coming, I would have been far happier. I cannot forget you, my darling. {...} I am also glad that the invitation gave you joy. {...} the mourning {...}, I only invited you to a song evening, my darling. I am truly sorry that you waited for me on Sunday; as I wrote, I could not come down, dear Jolánka. You do very wrong if something is given to you and you do not accept it. I think that if someone sincerely loves someone, that person cannot be won away from them, if they deserve it. {...} a person can quite boldly accept it, if on Sunday {...}, then I will see how the country air is doing you good. [He] respects your dear parents.

If you get my lines in time, tell Moczár: tomorrow, Corpus Christi, at 3 in the afternoon, the branch of the pension association is being founded, let him come. [He/I] wish(es) a good time.

Farewell, my darling! I kiss you countless times, until we meet again.

## Slovak (čitateľné časti)

Moja sladká jediná nádej! Vaše vzácne riadky som s vďakou dostal a urobili mi veľkú radosť. Ale keby ste boli napísali, že prídete, bol by som sa tešil oveľa viac. Na Vás, drahá, zabudnúť neviem. {...} Teší ma aj to, že Vám pozvánka urobila radosť. {...} smútok {...}, ja som Vás, drahá, pozval len na spevácky večer. Naozaj ľutujem, že ste ma v nedeľu čakali; ako som písal, nemohol som prísť dole, milá Jolánka. Veľmi zle robíte, ak Vám niečo dajú a neprijmete to. Myslím si, že ak niekto niekoho úprimne miluje, nedá sa mu ten človek odlákať, ak si to zaslúži. {...} človek to môže celkom smelo prijať, ak v nedeľu {...}, potom uvidím, ako Vám prospieva vidiecky vzduch. [Pozdravuje] Vašich milých rodičov.

Ak moje riadky dostanete včas, povedzte Moczárovi: zajtra, na Božie telo, o 3. popoludní bude založenie pobočky penzijného spolku, nech príde. Praje dobrú zábavu.

S Bohom, drahá! Bozkávam Vás nespočetnekrát, dovidenia.

## Why this stopped short on 2026-10-30 (superseded where the revision below says so)

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

## Revision 2026-11-02

By Claude Opus 5.5, on the human's order. I deskewed the left panel by 3.2 degrees (`work/rev2/e.py`) so each row sits level, and made new crops at 2-4x, in colour and in the green channel (`work/rev2/`). The first ledger had misaligned rows at the slope; that caused most of the old gaps. New ledger: `work/ledger-rev2.txt`. The earlier `ledger-opus.txt` and `decode_opus.py` are kept as the record.

**Changed:**

- **Rows 21-22 (old main gap).** Eleven signs of row 21 were missing from the first ledger. The row runs on past *egész*: `b a t r [struck blot] a n e l f o`, and row 22 begins `g a d h a t j a`. So: **egész bátran elfogadhatja**, "can quite boldly accept it". The blot after r is a cancelled sign on my reading; the two bars after it are a. The e l at the row end overlap (the wave runs across the top of the bars) and f is the upright cross. The last sign of *fogadhatja* has two strokes, so a, not e. Row 21 begins with a two-bar a at the card edge, not s.
- **Row 15.** The sign after n has two strokes: a, not e. *Azt ne gyön rosszul* is **Azt nagyon rosszul teszi**. No repeated *rosszul* is needed, so the old doubled reading is withdrawn.
- **Row 16.** `a d H a k e s` is **adnak és**, "they give and". H has the two strokes of n plus a crossbar: n read on word sense, the bar unexplained. The d is the h/p/d group, on word sense.
- **Row 7 end.** The row continues past the panel rule: `d`, an unclosed cursive loop, then a clear k. So **tudok**, not *tudom*. The unclosed loop as o rests on word sense. The old row 8 opening is not part of this word.
- **Row 19.** `a t o l e l` is **attól el(hódítani)**, not *a tőle el*; no sign changed. One t for tt.
- **Row 22.** The last sign is a small arc against the panel rule, not a full wave: the old *böl* is not secure.

**Still unread (why the card stays partial):**

1. **Row 8 opening:** `h . o k {) with inner tick} o {blot} h a`, about 8 signs, then *annak*. Read on the new crops; no word found. The tall sign under the blot may be h/d or part of a t whose roof is hidden; I do not guess.
2. **Row 10:** `e , I {blot} o` before *a gyászt*, and `o l e t o` after it. The first group may be a word like *ehhez* in a dialect form (*ehhö*), but the blot hides a sign. *öltö* (from *gyászt ölt*, "to put on mourning") and *letö[lti]* (to serve out) were both considered; neither fits the letters as written, so neither is adopted. hcp-1237 speaks of *letelik a gyász*, which supports the topic only.
3. **Rows 20-21:** `a z e r i a t e l e m b e r`. *ember* is clear from the sense of what follows, and *az ember* would be the natural subject, but the letters are *a t e l* with no z. *azér[t] a ...* is possible; *tel* is not explained. *az értelmes ember* does not fit the signs.
4. **Rows 22-23:** `b ö {arc} / v e b e n`, after *ha vasárnap*. If the arc is only a line-end stroke this is *bővében* ("in plenty"), which gives no clear sense here; if it is a cut-off l, *bölvében* is no word I can find. Not adopted.

These are four separate spots, one a whole unread opening, so the completeness rule is not met: no DONE1, no register entry. The smaller points listed earlier still stand, except those the changes above replace.

**Parallels used:** hcp-1237 for the mourning topic only. A grep of the family's SOLUTION.md files for *bátran*, *bővében* and *elfogadhat* found nothing useful. No reading here was taken from a sister card.
