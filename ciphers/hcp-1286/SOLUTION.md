# HCP1286: Feri to Jolánka Tóth, Budapest, 10 January 1914

**Status: PARTIAL. Key and most of the card are read, but rows 7 to 8 hold a clause whose signs are read and whose sense is open, and row 16 has one un-understood word (`külvesben`). Review 1 verdict REVISE, all findings addressed (see the end). No register entry.** Claude Opus 5.5, 2026-11-02. This revises the partial reading of 2026-10-30, also by Claude Opus 5.5 (see NOTES.md). No earlier GPT work exists on this card. No published solution was found; the portal shows Not solved, with no transcription or solution attached, and the orchestrator's register check (2026-11-02) found no record.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the Jolánka family key, unchanged from finished card hcp-1216 (table in `ciphers/hcp-1216/SOLUTION.md`). The transcription was made by me from the pixels of `work/hires/...adr.jpg`, not OCR. Additions this card supports:

- The cursive loop takes dots for ö, as in `belöle`, `fölidézem`. Undotted, the o and i signs are close; the i usually, not always, shows its dot. Calls resting on word sense: row 7 `ol` (o, not i) and row 8 `mi`.
- Plain numerals are used: **1** (row 18, written with a flag like a 7) and **2** (row 22) stand before the two parts of the love poem. The "two questions" (két kérdést) of rows 16 and 17 are the two `Mikor` lines, each ending in a plain `?`, both under numeral 2; part 1 asks nothing, so the role of the numerals is left open.
- The opposed bowls cs are confirmed in `csokba`, `csokolom`.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1286/work/decode_rev2.py
```

It checks the SHA-256 of the scans, decodes `work/ledger-rev2.txt` (one token per sign) and prints the literal text and the normalized text in `work/normalized-rev2.txt`. In the output, h stands for the h/p sign, `[x]` is a hidden sign and `{|}` a stray stroke. The image crops are made with `work/rev2c.py` and `work/rev2e.py`, run with the runtime named in NOTES.md.

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb egészségben találja soraim. Ami engem illet, csak megvagyok. E héten voltam a Sándornál, és ezt hallottam róla, hogy {bajosa|zeszebbolvalami}, hogy még ők, édesem, feljön[n]ek Pestre; hát így kezdtem örülni: közeljövőben gyakrabban láthatjuk egymást. De amint látszik, nem lesz belőle egyhamar. Írjo[n], édesem: lehe[t]-e még reményem, hogy feljönnek Pest[re]? Édes Jolánkám, {külvesben} két kérdést, de mondja kettőre feleletet.

1. Ha magamba[n] vagyok, fölidézem képed, mert is szeretlek én ojan nagyon téged.
2. Mikor hoz már veled össze egy boldog szép óra? Mikor forr az ajkunk össze üdvösséges csókba?

Jó mulatást kívánok, vasárnap soráit várom. Maradok szerető kedvese, Feri.

Under the stamp: [Iste]n vele, [éd]esem. Ma[ra]dok sze[re]tő ked[v]ese, Feri. Csókolom számtala[n]szor. X

Address side, plain handwriting, not cipher: Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás ("To the promising young lady Jolánka Tóth, Jászárokszállás"). The postmark is BUDAPEST 62, 914 JAN 10. The picture side has printed verse and a photograph, no cipher.

## English

My beloved sweet Jolánka! I wish that my lines find you in the best of health. As for me, I am just getting by. This week I was at Sándor's and heard this about it: that [rows 7 to 8 unread], that they, my sweet, are coming up to Pest after all; so I began to be glad that in the near future we can see each other more often. But as it seems, nothing will come of it soon. Write, my sweet: may I still hope that they are coming up to Pest? Sweet Jolánka, [külvesben, not understood] two questions, but give me an answer to both.

1. When I am alone, I call up your image, because I love you so very much.
2. When will a happy, lovely hour at last bring me together with you? When will our lips melt together in a blissful kiss?

I wish you a good time; I await your lines on Sunday. I remain your loving sweetheart, Feri.

Under the stamp: [God be] with you, [my sw]eet. I remain your loving sweetheart, Feri. I kiss you countless times. X

## Slovak

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky zastihli v najlepšom zdraví. Čo sa mňa týka, len tak žijem. Tento týždeň som bol u Šándora a počul som o tom toto: že [riadky 7 až 8 neprečítané], že predsa len oni, moja drahá, prídu hore do Pešti; tak som sa začal tešiť, že sa v blízkej budúcnosti budeme vídať častejšie. Ale ako sa zdá, tak skoro z toho nič nebude. Napíšte, drahá: môžem ešte dúfať, že prídu hore do Pešti? Sladká Jolánka, [külvesben, nerozumiem] dve otázky, ale dajte mi odpoveď na obe.

1. Keď som sám, vyvolávam si Váš obraz, lebo Vás tak veľmi ľúbim.
2. Kedy ma už spojí s Vami šťastná, krásna hodina? Kedy sa naše pery spoja v blaženom bozku?

Želám Vám dobrú zábavu, v nedeľu čakám Vaše riadky. Zostávam Váš milujúci milý, Feri.

Pod známkou: [Boh] s Vami, [drah]á. Zostávam Váš milujúci milý, Feri. Bozkávam Vás nespočetnekrát. X

## Uncertainties

1. **Row 16 `külvesben`: not understood.** All nine signs are clean (k, u with a dot, l, v, e, s, b, e, n). The sentence seems to need a verb here. Candidates such as `küldésben`, `külön levélben` and `levélben` do not fit the signs, so none is adopted. With rows 7 to 8 it is one of two un-understood places on the card.
2. **Rows 7 to 8 are an unread clause.** Literal: `bajosa{|}zeszebbolva[l]a` on row 7, `mi` opening row 8. The signs are read; the sense is open, and no translation is offered.
   - The first sign is a faint tall stroke whose bowl is not clear, so b is not firm. The isolated stroke between a and z has no letter value.
   - The o after `szebb` is an undotted loop that could be i. In `vala|mi` the l has only its lower half visible, under the cancel line.
   - The earlier `oly` is withdrawn: there is no sign between l and v. `bájos az, és szebb ... valami`, `bajos`, `bajosan`, `ha jó az idő`, `az eszébe` and `olvasni` were tried and none gives a sentence that fits every sign, so none is adopted.
3. **Row 8 `hogy még ők, édesem`**: the sign after e is a hook with a descender, partly covered by the J of the date, g or gy. `megy ő kedesem` is an alternative division of the same signs. The o shows no dots, so `ők` is supplied by sense, and `ők édesem` against `ő kedesem` is word sense too. Since row 7 is open, this reading is a proposal; `feljönnek Pestre` is secure.
4. **Row 6 `hal[lott]am`**: h, a, l and final a, m are seen; the middle lies under the postmark dome and shows only faint strokes. Word sense.
5. **Row 9 `[r]e hát így`**: under the date frame and the 62 frame. The e, h, t and gy are seen in parts, the r only as a stroke under the Hh corner. `Pestre` and row 15 `Pest` agree. Word sense for the row as a whole.
6. **Row 5 `S[á]ndor` and row 11 `lát[hat]juk`**: signs under postmark letters or the 62, one to two letters, word sense. The name agrees with hcp-1216 and hcp-1217.
7. **Row 18 `1` and row 22 `2`**: read as numerals by parallel with each other. The 1 could be some other mark, without effect on the sense. Row 18 `ha`: the h/p sign is called h by word sense (p gives nothing), and its second sign is two bars with a very faint separate mark below, so three bars cannot be fully excluded.
8. **Under the stamp**: the first signs of the top two rows are on paper lost in the torn stamp. `[Iste]n` (4 signs) and `[éd]esem` (2 signs) are restorations by formula (hcp-1216 `isten vele`); only `n vele` and `esem` are on the card. `[ra]` of `ma|[ra]dok` and `[re]` of `sze|[re]tő` belong to the same case: rows S3 and S4 start at the torn edge, so these signs are taken as lost with the paper, not as spelling omissions. This is more than one letter per word, but the word ending and the formula leave no competing reading.
9. **Under the stamp, rows 4 and 5**: `ked|es9e` has no v sign. `ked[v]ese` is taken as a spelling omission, though a v lost at the start of row S5 cannot be excluded; row 27 writes `kedvese` in full. The 9-shaped sign before its last `e` is unexplained and may be a false start. The final X is taken as a kiss mark, not a letter.
10. **Writer's spellings** (literal in the ledger, normalized above): `iletcsak` illet, `kedesem`/`edes`, `irjo` írjon, `lehe e` lehet-e, `jönek` jönnek, `magamba` magamban, `ojan`, `egessegben`, `Pest` Pestre (row 15), `ketöre` kettőre, `monda` mondja, `talaszor` számtalanszor. `mert is` in the poem is written as such. Row 16 repeats `-la-` in `Jo|lalánkám`. Rows 13 and 14 give `lehe e` with three-bar e signs, so the earlier `lapa e` is withdrawn. Accents are mostly invisible and are supplied.
11. **`feljönnek` is plural** on rows 8 to 9 and 15, so it is translated "they" (Jolánka's family or party, unnamed). A polite "you" would be singular `feljön`; a loose plural for Jolánka herself cannot be excluded.
12. The picture side has no cipher; it was viewed by the reviewer and by me.

## Why it is correct

The key is the established family key with no change, and it covers every sign in the ledger. Rows 1 to 6 and 9 to 27 read as continuous Hungarian in this writer's voice (formal address, misspellings, the name Sándor, the formula `csókolom számtalanszor`, `szerető kedvese Feri`). The poem rhymes at képed/téged, which a forced reading would not give, and the card's Budapest postmark agrees with the correspondence. The signs under the postmarks and frames on rows 5, 6, 9 and 11 were not seen individually: those restorations rest on word sense. The card remains partial because rows 7 to 8 and `külvesben` are not understood.

## Revision 2026-11-02

This section is the pre-review history; where it differs (for example `ol[y]`), the Response to review 1 below prevails.

Tried: new crops from the original scan at 3 to 7x, with colour saturation boosted (`work/rev2e.py`), which proved best at separating violet pencil from black postmark; also B minus R and B minus G channels and a red-channel mask (`rev2c.py`, `rev2d.py`, `rev2b.py`), which added little. The earlier sign ledger was dropped and rows re-read.

Changed:
- Row 7, previously unread: now `bajos a{|}z és szebb ol[y] vala-` with `mi` on row 8. The two b are confirmed by their bowls; the three bars before s are e, not a; the hidden-topped sign is l, giving `valami`. Sense is offered, weakest point of the card.
- Row 8: an extra o was found before k. `megy kedesem` becomes `még ők, édesem`.
- Row 9: `Pestre hát így` now has its signs, though still partly hidden.
- Row 14: `lapa e` withdrawn; it is `lehe e` = `lehet-e`.
- Row 16: first word now reads letter by letter as `külvesben`, still not understood.
- Row 18 `7` and row 22 `2` explained as verse numbers, and `?` at the verse ends as literal question marks.
- Rows 22 to 27 cleaned of all doubtful marks: the poem and closing are fully read. Row 27 confirmed to run along the card's bottom edge to the signature `feri`.

## Response to review 1

Verdict REVISE. After the corrections below I re-ran `python3 -I ciphers/hcp-1286/work/decode_rev2.py`: all three hashes OK, and the literal output now shows rows 7, 8, 17, 18, S3 and S4 as corrected. New crops: `work/rev3.py`, output in `work/rev3/`.

1. **Row 7/8 unread: accepted.** A fresh look at row 7 at 5x (`work/rev3/r7a.png`, `r7b.png`, `r7c.png`) confirmed the sign sequence and produced no reading. Status lowered to partial, the row is given as signs read, the English and Slovak leave it untranslated, and no register entry is written.
2. **`y` of `oly`: fixed.** `work/rev3/r7c.png` shows the l running across the postmark rim and the v directly after it, with no sign between. `[Y]` removed from the ledger, `oly` from the text.
3. **Row 8 ledger: fixed.** Now `M I H O GY M E G? O K E D E ) E M + E L`; `gy m e` come from the command output. The m at hires x about 530 is visible in `work/rev3/a.png`.
4. **Row 18 `ha`: fixed.** On `review/work/c/z1.png` the first sign is a long stroke with a separate short tick to its right, the h/p form, followed by two bars. Ledger, Hungarian, English and Slovak changed.
5. **Row 17 and spellings: fixed.** One T removed; the card has k, e, t, ö, r. `ketöre` and `monda` added to the spelling list.
6. **Under-stamp brackets: fixed.** `számtala[n]szor`. `[ra]` and `[re]` are stated as lost at the tear and added to the ledger as bracketed signs; `ked[v]ese` is stated as a probable spelling omission, with loss at the tear not excluded. See uncertainties 8 and 9.
7. **Two questions: fixed.** They are the two `Mikor` lines; the role of the numerals is left open.
8. **Restorations: accepted.** "Why it is correct" no longer treats those signs as seen; it says they rest on word sense.
9. **Address side: fixed.** The plain text is recorded after the Hungarian.

One further correction of mine: `feljönnek` is plural, so "you are coming up" on row 15 became "they" in English and Slovak (uncertainty 11).
