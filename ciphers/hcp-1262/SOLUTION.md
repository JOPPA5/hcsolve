# HCP1262 — to Jolánka Tóth: "not that kind of dancing school"

**Status: complete reading; review 1 verdict ACCEPT, five minor disclosure points addressed, no word changed (see the response at the end).** Solver: Claude Opus 5.5, 2026-11-01. No earlier work exists on this number. The portal (rendered capture 2026-11-01) shows status *Not solved*, with no attached transcription or solution; I met no published solution. The transcription is my own, made from enlarged crops of the hi-res original `work/hires/*_adr.jpg` (`work/crops/`). It is not OCR.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (MASC): the "Jolánka" postcard family. The key was transferred unchanged from HCP1216 (also 1212, 1213, 1217, 1218, 1243, 1301).

Type note (2026-11-03): the card also carries a hidden message in the cipher signs in the stamp box, under the (now lifted) stamp, so the register type is now "MASC + Steganography".

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl (with bar) | c (probably row 5, see uncertainty 6) | three short strokes | m | gamma/corner (stem may overrun the bar) | t |
| tick on the left + long stroke | d | two short strokes | n | long crossed diagonal | z |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + tick on the right | h / p | dotted crossed curve | i |
| open loop with descender | g | inverted T | j | opposed or joined bowls | cs |
| g + low descender, joined or adjacent | gy | | | | |

Diacritics: dots over the loop give ö. Acute marks are mostly faint and are supplied in normalization. The plain-cross u of the family does not occur on this card. On this card ly is written j (*mejért*, *ojan*).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1262/work/decode.py
```

It checks the SHA-256 of all four image files, decodes the sign ledger `work/ledger.txt` (one token per written sign, 18 main rows plus 7 rows inside the stamp box) and prints the literal letters and then the normalized text `work/normalized.txt`.

## Literal decipherment (as printed by the command)

```
01 kedvesjolankambe            10 nemkivanjahogyakor
02 csessoraitmegka{d|p}tam         11 gondolhasakmagara
03 mejertfogadjaköszö          12 amikormagakivan
04 netemekedvesemez            13 j{e|a}mikornekemnincs
05 nemojantan{c|cs}zisko           14 ojanoramhogynegon
06 lamintjolankamgo{m|n}       15 dolnekönreezelbe
07 d{ol}jaideholgyeknem        16 zaromsoraimeniske
08 jarnakcsakferfiak           17 remhogygondojonram
09 kedvesjolankamcsak          18 tisztelemakevesmamaj{e|a}t
in the stamp box: istenvele | aviszont | latasra | holnap | csokolo[m] | szamta | lanszor
```

## Hungarian (normalized)

Kedves Jolánkám! Becses sorait megkaptam, melyért fogadja köszönetem[et]. Kedvesem, ez nem olyan táncziskola, mint Jolánkám gondolja, ide hölgyek nem járnak, csak férfiak. Kedves Jolánkám, csak nem kívánja, hogy akkor gondolhassak magára, amikor maga kívánja, mikor nekem nincs olyan órám, hogy ne gondolnék önre. Ezzel bezárom soraim. Én is kérem, hogy gondoljon rám. Tisztelem a ke[d]ves mamáját.

Under the stamp: Isten vele, a viszontlátásra holnap! Csókolo[m] számtalanszor.

## English

Dear Jolánka! I have received your esteemed lines, for which please accept my thanks. My dear, this is not the kind of dancing school you think it is, Jolánka: no ladies come here, only men. Dear Jolánka, surely you do not want me to be able to think of you only when you wish it, when I have not a single hour in which I do not think of you. With this I close my lines. I too ask you to think of me. My respects to your dear mother.
Under the stamp: God be with you, until we meet tomorrow! I kiss you countless times.

## Slovak

Milá Jolánka! Vaše vzácne riadky som dostal, za čo prijmite moju vďaku. Moja milá, toto nie je taká tanečná škola, ako si Jolánka myslí, sem dámy nechodia, iba muži. Milá Jolánka, veď predsa nechcete, aby som na Vás mohol myslieť len vtedy, keď si to Vy želáte, keď nemám ani jednu hodinu, v ktorej by som na Vás nemyslel. Týmto končím svoje riadky. Aj ja Vás prosím, aby ste na mňa mysleli. Pozdravujem Vašu milú mamu.
Pod známkou: S Bohom, dovidenia zajtra! Bozkávam Vás nespočetnekrát.

## Uncertainties

Calls that rest on word sense, not on the shape alone:

1. **Row 7 *hölgyek*.** The first three signs are smudged in wet ink. They read tall stroke + shorter stroke (h), loop, wave. No dots are visible over the loop, so the ö is supplied. The k is overwritten several times and is a dense double loop; its value is inferred from the word. The double negative *hölgyek nem járnak, csak férfiak* then makes sense.
2. **Row 7, opening *d{ol}ja*.** After the d there is a compound: a pale looped stroke, a small closed loop on the bar of an inverted T. I take it as *o, l, j* squeezed together or corrected, giving *gondolja*. The o and l are not separate clean signs; the word is certain from context (*mint Jolánkám gondolja*).
3. **Row 6 end `go{m|n}`.** After *go* there are two short strokes and one taller one, which is the m sign as written; *gon-dolja* needs n. Either the third stroke is a false start of the d that opens row 7, or m is written for n.
4. **Row 2 *kaptam*, literal `ka{d|p}tam`.** The sign has its tick on the left, like d, not on the right as on the h/p sign. *kadtam* is not a word; p is chosen from sense.
5. **Row 13 first word, `j{e|a}`.** The sign after j has three strokes, the upper two converging. *kívánja* needs a, so this is either an e-sign written in error or two bars with an accent stroke. Row 10 has the same word with a clean a.
6. **Rows 5 and 9, closed bowl, literal `tan{c|cs}zisko`.** In row 9 two bowls joined at the base give cs, *csak*; row 8 writes *csak* with separate bowls. The row 5 sign has a different build: an angular left bowl with a long lower bar and a hook coming down from above it. HCP1273 writes the c of *tancz* as a left bowl with a bar, so this may be c, not cs, which gives the period spelling *táncziskola* directly. The word is the same either way.
7. **Row 14 *ne*.** The first sign of *ne* is heavily overwritten and has a stray crossbar. Read as n from the sense *hogy ne gondolnék*.
8. **Row 17 `gondojon`.** Written with a j that has a small tick at the base of its bar. There is no wave for l; the tick may be an abbreviated l. Normalized *gondoljon*.
9. **Stamp box, wet-ink damage.** Rows S1–S3 are blurred. S1: the l and final e overlap in one blot. S2: the i is a smudged cross with no visible dot, read from *viszont*. S3: signs 1–3 are blurred, read from *látásra*; the sign count (7) agrees.
10. **Restoration, S5 `csokolo[m]`.** The m is hidden by the large ink blot at the end of the row, and the last o shows only its top hook. *Csókolom* is restored from the family's formula with *számtalanszor*; a text search finds *csókolom* in 28 other hcp-12xx solutions and *csókolok* in none. *Csókolok* is a possible word, so this is a judgement, and the m is not read from pixels.
11. **S4 *holnap*.** The signs are h/p, o, wave, n, a, tall stroke + tick. The first and last are the h/p homograph, so *holnap* is chosen from sense. Attaching it to *a viszontlátásra* ("until tomorrow") is editorial; it could start a new phrase (*Holnap csókolom…*, "tomorrow I will kiss you…"). The order of the stamp text after the main text is assumed from sister cards.
12. **Row 4 literal `netemekedvesem`.** The card has *köszönetem e kedvesem*, with one extra three-bar sign after *köszönetem*. I normalize to *köszönetem[et]. Kedvesem*, taking it as an unfinished *-et*. A plain false start of *kedvesem* is equally possible; the sense is the same.
13. **Writer's spellings normalized:** *mejért* → melyért, *ojan* → olyan, *akor* → akkor, *gondolhasak* → gondolhassak, *ezel* → ezzel, *keves* → ke[d]ves (no d on the card; *kevés* "few" gives no sense, so this is a correction of the writer, not a reading). The small tick at the end of row 15 (*be-*) is taken as a line-break mark. Accents are supplied.
14. **Register shift:** the writer moves between *maga/magára*, *Jolánkám* in the third person and *önre*, all from the card.
15. **Sender and date:** the card has no signature that I can find, and no legible date. The sender stays unknown; no link to Feri (HCP1216) or other senders is claimed. The address in clear reads approximately *Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás*. The picture side has a printed Hungarian verse (*Hej cigány, hallod-e?…*), unrelated to the message.

16. **Row 18 *mamáját*, literal `mamaj{e|a}t`.** After j there are two clean bars and then a third, overwritten scribble of at least one more stroke, so the shape as it stands is e with a correction, not a. The a is from word sense (*mamáját*, accusative of *mamája*).
17. **Small sign notes, none in doubt.** Row 13: the i of *mikor* has no visible dot, like the one in S2; the key's "dotted" is the normal form, not a rule. Row 11: the final a has its upper bar doubled by overwriting. Row 14: the j stem runs slightly through its bar, a variant that the key otherwise notes only for t. S7: the final o and r overlap. Row 2: the third stroke of the final m is very pale but real.

## Why it is correct

- The key was taken unchanged from finished sister cards and gives continuous Hungarian across all 25 rows; no sign is left without a value.
- Long unforced stretches decode cleanly: *becses sorait megkaptam*, *fogadja köszönetem*, *nem kívánja hogy akkor gondolhassak magára amikor maga kívánja*, *mikor nekem nincs ojan órám hogy ne gondolnék önre*, *ezel bezárom soraim*, *tisztelem a … mamáját*, *számtalanszor*.
- Repeated words decode identically: *kedves Jolánkám* (rows 1, 9), *hogy* (rows 10, 14, 17), *kivan-* (rows 10, 12), *csak* (rows 8, 9), *gondol-* (rows 6–7, 11, 14–15, 17).
- The content is coherent: a reply to a jealous question about a dancing school, in the polite address and closing formulas (*Isten vele, a viszontlátásra, csókolom számtalanszor*) of the family.

## Response to review 1

Verdict ACCEPT. I reread each sign on the reviewer's enlargements (`review/work/crops/`). All five findings are accepted; no word of the reading, the translations or `work/normalized.txt` changed. The fixes are in `work/ledger.txt`, `work/decode.py` and this file. `python3 -I ciphers/hcp-1262/work/decode.py` was rerun: all four hashes OK, and the output matches the literal and normalized text above.

1. **Fixed.** Row 18: `r18endb` shows two clean bars and a third overwritten scribble between j and t. Ledger token is now `E?`, printed `{e|a}`; added uncertainty 16.
2. **Fixed.** Row 2: `m1R` and `r02end` confirm the tick on the left, the same shape as the d of row 3. Ledger token is now `D?`, printed `{d|p}`. The ledger header and decoder heading now say that H and P are one sign class told apart by word sense.
3. **Fixed.** Item 10 no longer says no other letter makes a word; it rests on the family formula and says *csókolok* is possible.
4. **Fixed.** All noted in uncertainty 17; `r13i` and `r11endb` confirm the row 13 i and row 11 a.
5. **Fixed.** `r05top` and `r09cs` do show different builds, so row 5 is now `C?`, printed `{c|cs}`. Uncertainty 6 and the key table are reworded; the table no longer says c is unused.

## Stamp-box message (2026-11-03)

Audit by Claude Opus 5.5 on the human's request of 2026-11-03. The stamp is lifted, and the ruled stamp box holds 7 rows of writing in the cipher signs (no plain Hungarian). The second postmark runs partly over the box. I re-checked the box on new 3x crops of the hi-res original (work/stamp-2026-11-03/box_top_3x.png, box_bot_3x.png). The 2026-11-01 reading is already complete and agrees with the pixels, so no letter changed.

- Literal (ledger rows S1-S7, decoded by work/decode.py): istenvele | aviszont | latasra | holnap | csokolo[m] | szamta | lanszor
- Normalized Hungarian: Isten vele, a viszontlátásra holnap! Csókolo[m] számtalanszor.
- English: God be with you, until we meet tomorrow! I kiss you countless times.
- Slovak: S Bohom, dovidenia zajtra! Bozkávam Vás nespočetnekrát.

Unread: no clause. One letter is restored: the final m of csókolo[m] lies under an ink blot (uncertainty 10). Rows S1-S3 are blurred by wet ink, and some signs there are read from the word (uncertainty 9). The stamp rows were already in the ledger, and the reproduction command already prints them.
