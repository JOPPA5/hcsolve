# HCP1298 — Feri to Jolánka Tóth: New Year's card, pencil instead of ink

**Status: complete reading. Every sign is transcribed and the key is complete; the one word-level gap left is the verb of row 11, which stays tentative (*behozta* or *be[h]ozatta*; Uncertainty 1), while the sense of its clause is clear from the postman and the dates. Reviews 1 and 2 (both REVISE) are addressed in the last sections.** Claude Opus 5.5, 2026-10-30. No earlier work exists on this number. The portal shows *Not solved* with no attached transcription or solution; no published solution of this card was found or used. The key comes from the finished family cards (HCP1216 and sisters, whose earlier passes were by the OpenAI GPT solver and Claude Opus 5.5).

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs, the "Jolánka" postcard family (same key as HCP1216). Numerals are written in clear. The key is `work/key.json`:

| sign class (ledger code) | letter | sign class | letter |
|---|---|---|---|
| two bars (2BAR) | a | section mark S (SECTION) | k |
| six (SIX) | b | wave (WAVE) | l |
| left bowl ( (LBOWL) | c | three strokes (3STROKE) | m |
| c + s, written () (LRBOWL) | cs | two strokes (2STROKE) | n |
| long stroke + tick (TICKSTROKE) | d | cursive loop (LOOP) | o |
| three bars (3BAR) | e | tall stroke + tick or dot (HP) | h / p |
| cross + (CROSS) | f | F shape (FSIGN) | r |
| hooked ς (SHOOK) | g | right bowl ) (RBOWL) | s |
| ς + separate y-shaped sign, sometimes touching (GYLOOP) | gy | Γ (GAMMA) | t |
| dotted crossed curve (DOTLOOP) | i | plain X (XCROSS) | u (with double mark ű) |
| inverted T (INVT) | j | chevron Λ (CHEVRON) | v |
| | | tailed crossed x (TAILX) | z |

On this card d and h/p are separable by shape: in d a short stroke or tick stands on the left of the long stroke (rows 4, 10), in h/p on the right (rows 5, 23). h and p are one sign: p is only separated from h by word sense (*Pesztoriné, lapját, kaptam, posta, lapot, vasárnap, napján*). Accents are mostly not visible and are supplied in normalization. The ledger shows the sign as `h` wherever it is h or p.

## Layout, in reading order

26 rows in the left block; then the text turns the corner: bottom margin (left to right), right edge (upward), top margin (card turned 180°, right to left, ending next to the end of row 1); finally six short rows in the stamp place. These lay under the stamp, whose perforated remains and torn corner are still on the card; only the pre-printed green triangle is written over. The top margin is **not** a continuation of row 1: its faint signs only read when rotated.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1298/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/sign-ledger.txt` (622 tokens; GYLOOP and LRBOWL each count as one token for two written elements) with `work/key.json`, prints the literal rows, and prints `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the hi-res address side (`work/rows.py`, `work/m.py`, `work/crops/`), not OCR.

## Literal decipherment

```
01 kedvesjolankamnagyon
02 kivanomhogyalegjobbegesz?
03 segbentalaljasoraim·
04 kedvesemszivesenelmenek
05 ahesztorinehoznemme
06 hetekelmertugyelvagyok
07 foglalvakedvesemami
08 engemilletcsakmegvagyok
09 esegesegesvagyokazuj
10 evilahjatedesemeloszo?r
11 3ikanbeozat?t?aahostasesen
12 5ikenkahtamkezhezesaz
13 ertnemvalaszanedesemugy
14 hamarabbigaz
15 elvagyokr?oglalvahogy
16 nemtunikefelmaganek
17 edesemhogymindigcsak
18 cz?eruzavalirokdeazt
19 csakanakkovetkeztesse
20 edesemhogyotiromso?ra
21 i?maholnemlehetten
22 tetszereznikedvesemkah
23 tamatothilonkatolegyla
24 hotujevremasnakneisju
25 tottameszibekedvesem
26 hogymulatotvasarnah
B1 megavizkesztnahjanvolte
R1 valaholmulatsagbanmostmagok
T1 nalmindigcsakennemmulathat?·
S1-6 csokol / jaszam / sirig / hűked / vesse / feri
```

Reading of the end of row 11, by word division only: *a postás és én* = `a hosta+s | es | en` (h stands for the h/p sign).

## Hungarian (normalized)

Kedves Jolánkám! Nagyon kívánom, hogy a legjobb egészségben találja soraim. Kedvesem, szívesen elmennék a Pesztorinéhoz, [de] nem mehetek el, mert úgy el vagyok foglalva, kedvesem. Ami engem illet, csak megvagyok és egésséges vagyok. Az újévi lapját, édesem, először 3-ikán behozta? a postás, és én 5-ikén kaptam kézhez, és azért nem válasz[oltam], édesem, úgy hamarabb. Igaz, el vagyok foglalva. Hogy nem tűnik-e fel magának, édesem, hogy mindig csak ceruzával írok, de azt csak annak következtesse, édesem, hogy ott írom soraim, ahol nem lehet tentet szerezni. Kedvesem, kaptam a Tóth Ilonkától egy lapot újévre, másnak ne is jutottam eszébe. Kedvesem, hogy mulatott vasárnap, meg a vízke[re]szt napján? Volt-e valahol mulatságban most maguknál? Mindig csak én nem mulathat[ok].

In the stamp place: Csókolja szám. Sírig hű kedvese, Feri.

## English

Dear Jolánka! I wish very much that my lines may find you in the best of health. My dear, I would gladly go to Mrs Pesztori's, [but] I cannot go, because I am so busy, my dear. As for me, I am just getting by and I am healthy. Your New Year's card, my sweet, the postman brought in [verb tentative] first on the 3rd, and I received it on the 5th, and that is why I did not answer, my sweet, any sooner. True, I am busy. Has it not struck you, my sweet, that I always write only in pencil? But conclude from that only, my sweet, that I write my lines there, where no ink can be had. My dear, I got a New Year's card from Ilonka Tóth; nobody else even thought of me. My dear, how did you enjoy yourself on Sunday, and on the day of Epiphany? Were you at some party there at your place just now? Only I never get to have fun.

In the stamp place: My mouth kisses you. Your sweetheart, faithful unto the grave, Feri.

## Slovak

Milá Jolánka! Veľmi si želám, aby Vás moje riadky našli v najlepšom zdraví. Moja milá, rád by som išiel k Pesztoriovej, [ale] nemôžem ísť, lebo som taký zaneprázdnený, moja milá. Čo sa mňa týka, ako tak sa držím a som zdravý. Váš novoročný pohľad, moja sladká, priniesol poštár [sloveso neisté] najprv 3., a ja som ho dostal 5., a preto som neodpovedal, moja sladká, skôr. Pravda, som zaneprázdnený. Nenapadlo Vám, moja sladká, že vždy píšem len ceruzkou? Ale z toho usudzujte len to, moja sladká, že svoje riadky píšem tam, kde sa nedá zohnať atrament. Moja milá, dostal som od Ilonky Tóthovej novoročný pohľad, inému som ani nezišiel na um. Moja milá, ako ste sa zabávali v nedeľu a na deň Troch kráľov? Boli ste teraz u Vás niekde na zábave? Len ja sa nikdy nemôžem zabávať.

Na mieste známky: Bozkávajú Vás moje ústa. Váš do hrobu verný milý, Feri.

## Uncertainties

Not established at word level (all signs are transcribed), only item 1:

1. **Row 11 `beozat?t?a`, tentatively *behozta*, alternatively *be[h]ozatta*.** The stretch is crowded and retraced: bold b; a dark hooked stroke with a faint lowest bar, read e; a loop with a hooked arm, read o; a retraced tailed x, read z, with faint bars after it, read a; then a Π-like group, a Γ with a short stroke under the bar, a long stroke from the bar's end and a further faint stroke; then two bars. The faint bars after z and the extra faint stroke look like correction, so *behozta* ("brought in"), with those strokes as a corrected false start, is at least as good as *be[h]ozatta* ("had brought in"), and it is the commoner word with a postman as subject. I print *behozta?*. Reading Π as two fused t, or as Γ + n, stays open. Neither word has a visible h. A reader who rejects both loses the verb of the clause, not its sense: the postman and the dates frame it. **This is the only word-level gap on the card.**
2. **Row 11 end, *a postás és én*, confirmed by review 2.** The signs ) ≡ ) ≡ || are clean, with no sign changed from the earlier "unknown word" `sesen`: `posta|s es en`. *És* is spelled the same in rows 9 and 12, and the clause runs on into *5-ikén kaptam kézhez*. A heavy tick above the last e could be the accent of *én* or a stray stroke; it is weak evidence either way.
3. **Rows 20–21 *soraim*, resolved in review 2.** The earlier `szra|oma` came from two mistranscribed signs. The row 20 sign after `)` has no tail below a crossing, so it is not the tailed z but a sign of the loop class; the row 21 first sign has the long top bar of the i form, undotted as on *feri* (S6) and the i of row 3 *soraim*. The result `s o r a | i m` matches row 3 sign for sign. **What rests on what:** "not z" and "loop class" rest on shape; the o / i call within that class rests on word sense, so both tokens carry `?`. That no dot was written, rather than lost, cannot be shown.
3a. **Row 11 first sign, 3 or 8.** It has a flat top bar, a diagonal and a closed lower loop, so the shape alone does not decide, and *-ikán* fits both (*harmadikán*, *nyolcadikán*). I read 3 because the sentence then runs in order (the postman on the 3rd, received on the 5th), and because a card posted in reply on a day 8 (the round cancel, weakly read, month illegible) can hardly report the 8th as past before the 5th. The reading 8 leaves the dates illogical. This is a choice, not a shape proof. Round 1 printed 8.

Value rests on word sense:

4. Row 2 final sign is a tailed loop, unlike the usual z; read z for *egész|ség-*.
5. Row 3 ends in an isolated S-like flourish after a tick (`·`), given no value. It could be a k, or a false start of row 4's *kedvesem*.
6. Row 6: the literal is `hetek`, so *mehetek* is exactly as written (round 1 wrongly claimed an F and a slip). The normalized `[de]` in the same sentence is editorial.
7. Row 10: the d of *édesem* is a short stroke set left of a long one, the same form as the d of row 4 *kedvesem*, so it rests on shape and no longer carries `?` (this corrects my round 2 note that it looked like n). Round 1 printed *én édesem*, which added a word; that is withdrawn. *Előszőr*: the second o is very faded, almost lost; it is read from the visible blob and the word.
8. Row 15 `r?oglalva`: the first sign is a long-barred F, here read as a slip or variant for f (*foglalva*, spelled correctly with the + in row 7).
9. Row 18: `c`, then a retraced dark sign with the long diagonal and crossing tail of the tailed x (`TAILX?`), then *eruzával*, which suggests the old spelling *czeruzával*. The word is secure.
10. Row 18 *de* and rows 15/16 are otherwise clean. Row 16 *magának* is spelled `maganek`.
11. Row 26: the literal is `mulatot`, *mulatott* with the writer's usual single t (round 1 wrongly had an s here, and the alternative *mulatsz ott* is withdrawn). The final h/p of row 26 is a looped, 8-like form unlike every other h/p on the card; *vasárnap* is secure from the word.
12. T1 last letter: the sign after *mulatha* is a dark, angular sign plus a tick next to the end of row 1. Inverted it is an L shape, not a clean Γ, and its ink is darker than the rest of the margin. Read t from *mulathat*, so *mulathat* itself rests partly on word sense; it could be an unrelated mark. *-ok* is supplied.
13. S2–S4 run across the printed triangle in the stamp place; S4 needed the green removed to see the signs. *szám* ("my mouth") is literal; it could be an abbreviated *számtalanszor*, the closing of HCP1216 ("I kiss you countless times"), but *csókolja* + *szám* reads as it stands.
14. Writer's spellings normalized: *elmenek* → elmennék, *válaszan* → válasz[oltam] (this one is an interpretation: the word is cut short), *anak* → annak, *ot* → ott, *vízkeszt* → vízkereszt, *kedvesse* → kedvese, *eszibe* → eszébe, *magok* → maguk, *egeseges* → egésséges, *talalja* → találja, bare accusative *soraim* in rows 3 and 20–21 (dropping the s of *és egésséges* would not change the sense: the literal is *es egeseges*).
15. The sender is "Feri", as on HCP1216, in a like hand; I do not claim that they are the same man beyond the matching family, closing formula and addressee. The upside-down rectangular cancel ends *-TA-ÚJPEST P.U.*, the Rákospalota-Újpest station cancel named on HCP1288 (the start of the name is restored); the round cancel shows an 8, the year is not legible. The plain address reads, in violet: Szépreményű (under the cancel, as on HCP1243) Tóth Jolánka úrleánynak, Jász-Árokszállás. The picture side has printed Hungarian verse only, no cipher.

## Why I believe it is correct

- The family key, unchanged, turns all 622 tokens into Hungarian, in a path around the card that was not known in advance (top margin read only after rotation, and it joins *magok|nál* across the corner).
- Long stretches read without any choice: *nem tűnik-e fel magának … hogy mindig csak ceruzával írok … ahol nem lehet tentet szerezni*, *kaptam a Tóth Ilonkától egy lapot újévre*, *a vízkeszt napján volt-e valahol mulatságban*.
- Internal coherence: he explains the pencil by the lack of ink, and the sense is unforced. Repeated words decode the same (*édesem*, *kedvesem*, *hogy*, *vagyok*, *foglalva*). Tóth, the addressee's surname, appears naturally for Ilonka.
- It closes with the family's formula (*sírig hű kedvese, Feri*).
- The same six signs *soraim* occur in rows 3 and 20–21, and *ott … ahol* becomes a plain correlative.
- Weak point: the tentative verb of row 11, the only word-level gap.

## Response to review 1

Verdict REVISE. Every finding is addressed; I rechecked the contested signs on review/work/m26.png, r6a.png, r15f.png, y18.png, z11a.png, z11b.png, z12.png, v26.png, st.png and zhand.png, and agree with all of them.

1. **Row 26, fixed.** The crop shows `= Γ ∂ Γ Λ`, with no sign between Γ and the loop. RBOWL removed; item 11 rewritten; *mulatsz ott* withdrawn.
2. **Row 6, fixed.** Plain Γ, no middle arm. Token is now GAMMA; item 6 rewritten; the slip claim is gone.
3. **Row 15, fixed.** Two clean bars; token is now 2BAR, literal *foglalva*. Item 8 rewritten. The long-barred F stays disclosed.
4. **Row 18, fixed.** Token is now `TAILX?`; item 9 names *czeruzával*.
5. **Row 3, fixed.** Normalized to *találja soraim*, as on HCP1217; listed in item 14.
6. **Rows 14–15, adopted.** *Igaz, el vagyok foglalva.* English and Slovak changed ("True, I am busy"), with no *úgy* in that clause.
7. **Stamp, fixed** in the layout, translations and ledger header: the rows lay under the stamp, and only the green triangle is written over.
8. **Plain hand, fixed** in item 15: *Szépreményű* is visibly written and I do not need the sister card to read it; the cancel is given as Rákospalota-Újpest with the start restored.
9. **Ledger units, fixed.** Row 12 `5 [bar]` is one numeral (z12.png), so the bar is removed. Counts are now called tokens (622), and the key table describes GYLOOP and LRBOWL as two written elements. The looped final p of row 26 is flagged in item 11.
10. **Row 11, addressed and taken further.** The flat-topped sign is listed as 3 or 8 (item 3a), and I now print 3, for the reasons given there; this is a choice, not a shape proof. The Π stays open, with Γ + n named (item 1).
11. **Status, fixed.** The status line now says PARTIAL.

**Changes beyond the review (these are why this is DONE2):**

- Row 11 end: `sesen` is dissolved into *a postás és én* by word division (item 2), which gives the clause sense and needs no sign change.
- Row 11 first sign printed as 3 (item 3a), and *be[h]ozatta* offered tentatively (item 1).
- Row 10: *én édesem* withdrawn in favour of *édesem*, with the d flagged as resting on word sense (item 7). The reviewer did not raise this.

Reproduction command re-run after the edits: all four hashes OK, 622 tokens, literal rows as printed above.

**For review 2:** please test *postás és én*, the 3 / 8 call, and the d of row 10. Even if all hold, `szra|oma` remains unread, so on the family's practice (HCP1292, HCP1797) this stays partial and no register entry is proposed.

## Response to review 2

Verdict REVISE. I looked at review/work/r2/compare_soraim.png, w11.png, e10a.png and w5b.png and agree with every finding. The changes are the ones the review named, so per its closing paragraph this does not go to a third review.

1. **Rows 20–21, fixed.** The row 20 sign has no tail below the crossing, unlike the z of rows 4 and 5; the row 21 sign has the long top bar of the i form. Ledger now `… RBOWL LOOP? FSIGN 2BAR` / `DOTLOOP? 3STROKE 2BAR HP …`. Literal rows, normalized text, English, Slovak, uncertainty 3 and "Why I believe" are updated. My earlier claims that the signs were clear and that the word might be a place are withdrawn; where Feri writes from was never said on the card beyond "where no ink can be had".
2. **Status, reassessed.** Now a complete reading whose only word-level gap is the row 11 verb, and that verb's clause has clear sense. This follows the family practice for one unresolved word in a full reading (HCP1299, HCP1285), not the partial cards, where a clause (HCP1292) or the object of a sentence (HCP1797) has no sense. So a report and a register entry are written.
3. **No change needed.** *A postás és én* stands; the tick over the last e is mentioned in uncertainty 2 as weak evidence.
4. **Fixed.** The d of row 10 has no `?`; item 7 is rewritten.
5. **Fixed.** The key note now separates d from h/p by the side of the tick; only h against p needs word sense.
6. **No change needed.** 3 is kept and called a choice; item 3a now records that *-ikán* does not help.
7. **Fixed.** Both *behozta* and *be[h]ozatta* are offered in item 1. The normalization now prints *behozta?*, which agrees with the English "brought in".

Reproduction command re-run after these edits: all four hashes OK, 622 tokens, literal rows as printed above.
