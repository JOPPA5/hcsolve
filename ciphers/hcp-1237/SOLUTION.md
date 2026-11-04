# HCP1237 — Feri to Jolánka Tóth: the word "not interested", the cards, the end of mourning

**Status: complete reading, review 1 ACCEPT, closed.** Claude Opus 5.5, 2026-11-02. No earlier work exists on this number. The portal shows status Not solved and attaches no transcription or solution; no published solution of this card was found or used. The key comes from the finished Jolánka cards (HCP1216 and sisters).

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka family, register type MASC). Key transferred unchanged from HCP1216/1243. All ciphertext is on the address side (left block, a line along the whole bottom edge, and five rows on the stamp area). The picture side has only a printed poem and no handwriting.

2026-11-03 type note: register type is now **MASC + Steganography**. The stamp has been lifted (only a torn remnant stays at the top of the box) and the five cipher rows sit in the stamp box below it, where the stamp would have covered them; a faint ring of the cancel shows across them. Re-checked on new crops `work/stamp-2026-11-03/box_2x.png` and `row1_3x.png`..`row5_3x.png`: the hidden message is in the cipher signs only (no plain Hungarian), already read in full above (*Üdvözlöm a távolból. Hű kedves[e].*), no letter changed; the last sign stays `[?]`.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section/S mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three strokes | m | gamma | t |
| short + long stroke | d | two strokes | n | plain X | u, ü |
| three bars | e | hump loop with down tail | o, ö, ő | chevron | v |
| upright cross | f | long + short stroke | h / p | low curve | y |
| open loop with descender | g | crossed curve with long straight bar | i | crossed diagonal with tall stem | z |
| joined loop + descender | gy | inverted T | j | | |

On this card the stroke order separates d (short then long) from h/p (long then short) consistently. The i and o forms are also distinct: i has a long straight crossbar, o a hump that turns down.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1237/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (one token per written sign, a manual transcription from enlarged crops, not OCR) and prints the literal rows and `work/normalized.txt`. Crops are in `work/crops/`; `crops/shear.png` is a deskewed left half.

## Literal decipherment (as printed)

```
01 kedvesjolankameso            13 ke'ntszoktamkuldeni
02 rokkalege'szitemkiso         14 e'shakesonkapomso
03 raime'desehigyjeelhogy       15 raitnkoregykicsito'sze
04 nagyonroszu'lesetez          16 jo'ne'smiti'rjakoly
05 aszo'neme'rdekli             17 su'ru'nanakigazano'rulo'k
06 pedighigyeeledesem           18 hogyletelikagyasz
07 maganakmindenmozdu           19 igazanmilygyorsan
08 latjaerdekelami              20 elteltezido'mint
09 lapokatiletiaranem           21 hamostletvolnaezelbezaromsoraim
10 lehetpanaszamerthet          22 maradosirihukedvesse
11 elejenku'ldo'kketto't        23 feri
12 esaharmadikatvalasz          stamp: u'dvoz | loma | tavol | bolhu | kedve[?]
```

An apostrophe marks an accent or dot seen on the card; other accents are supplied in normalization. Row 21 is the long line along the bottom edge.

## Hungarian (normalized)

Kedves Jolánkám! E sorokkal egészítem ki soraim, édese[m]. Higgye el, hogy nagyon rosszul esett ez a szó: „nem érdekli”, pedig higgye el, édesem, magának minden mozdulatja érdekel. Ami lapokat illeti, arra nem lehet panasza, mert hét elején küldök kettőt, és a harmadikat válaszként szoktam küldeni, és ha későn kapom sorait, [a]‹n›kor egy (‹n›: the card has n where *akkor* needs k) kicsit összejön, és mit írjak oly sűrűn. Annak igazán örülök, hogy letelik a gyász. Igazán, mily gyorsan eltelt ez idő, mintha most lett volna. Ezzel bezárom soraim, maradok sírig hű kedvese, Feri.

In the stamp area: Üdvözlöm a távolból. Hű kedves[e].

## English

Dear Jolánka! With these lines I complete my lines, my sweet. Believe me, this word hurt me very much: "does not interest you", when, believe me, my darling, your every movement interests me. As for the cards, you can have no complaint on that score, because at the start of the week I send two, and the third I usually send as a reply, and if I get your lines late, then they pile up a little, and what should I write so often? I am truly glad that the mourning is coming to an end. Truly, how quickly this time has passed, as if it were only now. With this I close my lines; I remain, faithful to the grave, your sweetheart, Feri.

In the stamp area: I greet you from afar. Your faithful sweetheart.

## Slovak

Milá Jolánka! Týmito riadkami dopĺňam svoje riadky, drahá. Verte mi, že veľmi ma zabolelo toto slovo: „nezaujíma Vás”, a pritom mi verte, moja milá, že ma zaujíma každý Váš pohyb. Čo sa týka pohľadníc, na to sa nemôžete sťažovať, lebo na začiatku týždňa posielam dve a tretiu zvyčajne posielam ako odpoveď, a keď Vaše riadky dostanem neskoro, tak sa to trochu nazbiera, a čo mám písať tak často? Naozaj sa teším, že sa končí smútok. Naozaj, ako rýchlo prešiel tento čas, akoby to bolo len teraz. Týmto končím svoje riadky, ostávam až do hrobu Váš verný milý, Feri.

V mieste známky: Pozdravujem Vás z diaľky. Váš verný milý.

## Address (unenciphered)

Szép reményű Tóth Jolánka úrleánynak, Jász-Árokszállás ("To Miss Jolánka Tóth, of fair hopes"; the last word is read from the plain handwriting, partly under the collection stamp). The date 1912-06-30 is taken from the portal file name only; the postmarks are not legible enough to confirm it.

## Uncertainties

Letters resting on word sense rather than on the sign alone:

1. **h/p**: the same sign. p is chosen by sense in *pedig* (06), *lapokat* (09), *panasza* (10) and *kapom* (14).
2. **Row 15 `nkor`**: the signs are two strokes (set under the arm of the preceding t), k, o, r. Normalized *[a]‹n›kor*, that is *akkor*: the a is not on the card and the writer has n for the first k. This is the weakest word of the text, but the sentence needs "then" and no other word fits.
3. **Row 15–16 `osze jon`** is normalized *összejön* ("piles up"), with a single s. The o is the hump form, so *isze* is excluded, and it carries two marks (a tick and a dot, `work/crops/rv15end.png`), direct evidence for *ö*. The o of *jon* has two dots and the e of *es* a tick (`work/crops/rv16start.png`). The meaning in context (cards piling up) is my interpretation of a loose colloquial sentence.
4. **Row 5**: *ez a szó: „nem érdekli”*: I take the words as a quotation from her letter, but the card has no punctuation. Who is "not interested" (he in her, or the like) is inferred; the literal words are clear. The o of *szó* has the hump form and an acute tick.
5. **Row 7–8 *mozdu|latja***: the word is split over a line. The first sign of *mozdu* is three strokes, tall here, so it is read as m. The final u is partly over-inked and crosses a postmark line.
6. **Row 20 `ez`**: the z is a heavy blot with the crossed shape still visible; z versus u rests on sense.
7. **Row 19 `gyorsan`**: the y part of the gy is blotted; the g and the tail stay visible.
8. **Row 11 `elején`**: the j is overwritten with an extra top bar and a heavy foot; only *elején* gives sense ("at the start of the week").
9. **Row 14 `kapom`**: the k of *kapom* is blotted to a dark loop, read k from the shape and the word.
10. **Stamp row 5**: *kedve* is clear; the last sign is a pale smeared X-like form where s is expected, printed `[?]`, and the end is a restoration *kedves[e]* from the same phrase in row 22. The ink was blotted, so the form cannot be read strictly. No other word is affected.
11. **Writer's spellings normalized**: *roszul, eset* (esett), *ilet, ara, anak, marado siri* (maradok sírig: k and g omitted), *hu* (hű), *kedvesse* (kedvese, doubled s), *ezel* (ezzel), *letvolna* (lett volna), *sürün* (sűrűn), *higyjeel* row 3 and *higyeel* row 6 (higgye el; the spurious j in row 3 is also on HCP1216 row 5), *édese* in row 3 (final m missing, supplied in brackets), *igazan* twice (igazán). Accents are mostly unseen and supplied.

The printed poem on the picture side is a commercial text and is not part of the message. "Gyász" (mourning) is read clearly, but whose mourning is not stated.

## Why it is correct

- A key taken unchanged from other cards turns every sign in all rows into Hungarian; no key value was adapted to this card.
- Repeated forms decode identically: *hogy*, *igazan* ×2, *higgye el* ×2, *soraim*, *édesem*, *küld-* ×2.
- The text is coherent throughout, in formal address, and answers a specific complaint in her letter. The closing formula *sírig hű kedvese, Feri* is the one on HCP1216, with the same spelling habit in *higgyje el*.
- Reading was checked against sign shape rather than sense where they could clash: *szó* (not *szí*) and *ősze/össze* were corrected from the i/o form, and *gyász* came from the two-bar a in place of a first reading with e.

## Response to review 1

Verdict ACCEPT, four minor findings. All are fixed; no letter of the reading changed. `python3 -I ciphers/hcp-1237/work/decode.py` was re-run after the fixes: all four hashes pass and it prints the updated rows.

1. **Accents missing from the ledger: fixed.** I rechecked on new 3x crops of the hires address side (`work/crops/rv15end.png`, `rv16start.png`, script `work/crops/r1.py`). The tick and dot over the o of `osze`, the two dots over the o of `jon` and the tick over the e of `es` are all there. Ledger rows 15 and 16 now have `O:m`, `O:m`, `E:m`; the literal rows above are updated and Uncertainty 3 cites the marks.
2. **`eset` not listed: fixed.** Added to Uncertainty 11.
3. **Notation of `[a]kkor`: fixed.** The normalized text now has `[a]‹n›kor` with a short note, here and in `work/normalized.txt`.
4. **"Over the stamp": agreed and fixed.** No stamp remains over these rows, so "in the stamp area" is now used in the ledger, the normalized text and the translations. On the card only a torn remnant stands at the top of the box.
