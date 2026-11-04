# HCP1269 — Feri to Jolánka Tóth: "I do read your lines with joy"

**Status: complete reading of everything on the card, one word in the last clause not understood (item 1); review 1 verdict REVISE, findings addressed (see the last section).** Claude Opus 5.5, 2026-11-01. No earlier work exists on this number. No external plaintext used: the portal shows status *Not solved* with no attached transcription or solution; the orchestrator's AI-register check of 2026-11-01 found no record. The HistoCrypt article linked on the portal was not consulted.

The card ends with the plain words **"folyt. köv."** ("to be continued"), so the message itself continues on another card. What is on this card is fully transcribed.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (MASC): the Jolánka postcard family.

**Type note (2026-11-03):** register type changed to **MASC + Steganography**: the stamp was lifted and a six-row cipher message is written in the stamp box under it (see "Stamp-box message (2026-11-03)"). The key was transferred unchanged from HCP1216 (also 1212, 1213, 1217, 1218, 1243, 1301); no new sign values were needed.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl (only in opposed bowls here) | c | three short strokes | m | gamma/corner | t |
| long stroke + short tick | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | opposed bowls | cs |

Dots over o/u give ö/ü; two ticks give ő. Acute marks are mostly not written or not distinguishable and are supplied.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1269/work/decode_opus.py
```

It checks the SHA-256 of the two source images and the two hi-res originals, decodes the sign ledger `work/ledger-opus.txt` (32 rows plus 6 rows under the stamp) with the key, and prints the literal letters and the normalized text `work/normalized-opus.txt`. The ledger is a manual transcription from enlarged crops of `work/hires/*_adr.jpg`; it records signs by their value, not by independent shape codes.

## Literal decipherment

```
01 zseretetedesjolankam-           17 kormegegycsehetsemerek
02 kivanomhogyalegjobbeges         18 ra.edesemhiszaztenis
03 segbentalaljasoraimb.           19 szeretnemhogyminele
04 soraitmegkahtammelyet           20 lőbelmehessekcsakhogy
05 köszönőgszehen.edesemön         21 enfelattemmasrendel
06 tevedhaaztgondoljahogy          22 kezikmajdmeggyozö
07 becsessorainemszolgenak         23 dikrolahafeljönekhest
08 orömemrelegyenabbabar           24 rehogymenyiszabadom
09 mimertenmindigalegna            25 vanedesemnemakarom
10 gyobborömelolvasomso            26 munkajabazavarnivarhat
11 raitedesemigazansajnalom        27 magaakorishao{?}tvegzok.
12 hogytovabraisazonkelgon         28 csakmarotvolnek.edesemennemirtamaztalahotidegenan
13 dolkoznomhogymiindi             29 csakkerzeztemhogymitgondolthogyaztamegjegy
14 tottaarahogyaztirja             30 zestcsinaltaeshaiketdesekvanakőztünkabolnegon
15 mertazegesznekazazoka           31 doljonmindenroszstamitmarnemszabadtehate
16 hogyegyszerjobbanraermas        32 lezegymasrol (up the right edge)
stamp: üdvozli atavol bo{?}ze retőked vesse feri
```

Rows 28 to 31 run the full width of the card under the address. Row 32 runs up the right edge, followed there by the plain cursive *folyt. köv.* (written like "fost kön").

## Hungarian (normalized)

Szeretett édes Jolánkám! Kívánom, hogy a legjobb egészségben találja soraim. B[ecses] sorait megkaptam, melyet köszönök szépen. Édesem, ön téved, ha azt gondolja, hogy becses sorai nem szolgálnak örömemre. Legyen abban bármi, mert én mindig a legnagyobb örömmel olvasom sorait. Édesem, igazán sajnálom, hogy továbbra is azon kell gondolkoznom, hogy mi indította arra, hogy azt írja, mert az egésznek az az oka, hogy egyszer jobban ráér[ek], máskor meg egy csepet sem érek rá, édesem. Hisz azt én is szeretném, hogy minél előbb elmehessek, csak hogy én felettem más rendelkezik. Majd meggyőződik róla, ha feljön(ne) Pestre, hogy mennyi szabadom van. Édesem, nem akarom munkájába zavarni, várhat maga akkor is, ha ot[t] végzek. Csak már ott volnék. Édesem, én nem írtam azt a lapot idegen[?], csak kérdeztem, hogy mit gondolt, hogy azt a megjegyzést csinálta. És ha [i] két[ke]dések vannak köztünk, abból ne gondoljon minden rosszat, mit már nem szabad tehát [? *…tehate lez*, unread; feltételez(ni)?] egymásról.

*folyt. köv.* (plain)

Under the stamp: Üdvözli a távolból szerető kedvese Feri.

## English

My beloved sweet Jolánka! I wish that my lines find you in the best of health. I have received your d[ear] lines, for which I thank you very much. Darling, you are mistaken if you think that your dear lines do not give me joy. Whatever may be in them, I always read your lines with the greatest pleasure. Darling, I am truly sorry that I must keep wondering what prompted you to write that, for the cause of the whole thing is that at one time I have more leisure and at another not a drop of it, darling. Why, I too would like to get away as soon as possible, only someone else has charge of me. You will see for yourself, if you come up to Pest, how much free time I have. Darling, I do not want to disturb you at your work; you can wait until I finish there. If only I were there already. Darling, I did not write that card [? through / to a stranger], I only asked what you thought, that you made that remark. And if there are doubts between us, do not from that think every bad thing, which one must no longer [? assume] of each other.
*To be continued.*
Under the stamp: Greetings from afar from your loving sweetheart, Feri.

## Slovak

Moja milovaná sladká Jolánka! Želám si, aby Vás moje riadky našli v najlepšom zdraví. Vaše m[ilé] riadky som dostal, za čo veľmi pekne ďakujem. Drahá, mýlite sa, ak si myslíte, že Vaše milé riadky ma netešia. Nech je v nich čokoľvek, vždy čítam Vaše riadky s najväčšou radosťou. Drahá, naozaj ma mrzí, že musím stále rozmýšľať nad tým, čo Vás viedlo k tomu, aby ste to napísali, lebo príčina toho všetkého je, že raz mám viac času a inokedy ani kvapku, drahá. Veď aj ja by som chcel čo najskôr odísť, len nado mnou rozhoduje niekto iný. Presvedčíte sa o tom, ak prídete hore do Pešti, koľko mám voľna. Drahá, nechcem Vás rušiť pri práci, môžete počkať, kým tam skončím. Keby som tam už bol. Drahá, ten lístok som nenapísal [? cez cudzieho / cudziemu], len som sa pýtal, čo ste si mysleli, že ste urobili tú poznámku. A ak sú medzi nami pochybnosti, nemyslite si z toho všetko zlé, čo už nesmieme [? predpokladať] jeden o druhom.
*Pokračovanie nabudúce.*
Pod známkou: Pozdravuje Vás z diaľky Váš milujúci milý, Feri.

## Uncertainties

1. **Last clause, rows 31–32 (the one unread word).** Letters: `…szabad tehate | lez egymasrol`. *egymásról* ("about each other") is clear, and the cross before it is z (review finding 6: same strokes as the z of row 15, not the f of row 23 and the stamp). *szabad* and *tehát* read, but the remainder `e-le-z` gives no word I can confirm. *feltételez(ni)* ("to assume") fits the sense and the ending *-tel-ez* would suit a false start or slip, but the signs do not spell it, and the division *tehát* / *tételez* is itself uncertain. Treat the translation there as a guess.
2. **Row 28 `idegenan`**: signs clear (i d e g e n, two bars, n; review finding 10 confirmed the penultimate vowel is two bars). The stem *idegen* ("stranger") is secure; the ending and its role are not: "through a stranger", or a slip for *idegennek* ("to a stranger").
3. **Row 30 `haiketdesek`**: read *ha két[ke]dések* ("if doubts"), which assumes a dropped syllable. The sign `i` between *ha* and *két* has a separate dot above it, at the foot of the m of row 29, so i is supported (finding 7), but the small word is unexplained: a false start, or perhaps an unfinished *ily(en)* ("such"), which is only a thought. The restoration of *ke* is a guess. A tick over the e supports *két*.
4. **Row 23 `feljönek`**: the signs are clear (+ = f, three bars, wave, inverted T, ö, n, three bars, k; the k is partly on the card's dashed divider). *ha feljön* is the family's standing phrase (HCP1311 *ha feljön Pestre*); the ending `-ek` is an oddity, normalized as *feljön(ne)*.
5. **Row 27**: the sign after *ha o* is a dark ink-and-stain blot; *ot[t]* is a restoration on the model of row 28 *ot*. The verb is literally *vegzok* (normalized *végzek*). The h/p sign is taken as h here.
6. **Stamp row 3**: the sign between *bo* and *ze* lies under the postmark triangle. It should be l and/or s by *távolból szerető* ("from afar … loving"); restoration. Stamp row 2 has a, so *atavol* = *a távol-*. Stamp row 5 is literally `vesse`, a doubled s or a slip, normalized *kedvese*.
7. **Row 1 `zseretet`**: the first two signs are z then s (not s z), and the third sign is overwritten; *Szeretett*. The trailing dash is a mark, not a letter.
8. **Word-sense calls, h/p and d/n**: *megkaptam, szépen, csepet, Pestre, lapot* use the h/p sign as p. *Row 13 dolkoznom*, *rendel-kezik*, *mindig* took d from the stroke length; all are unambiguous words.
9. **Row 22/21 *rendel|kezik***: the first sign of row 22 is overwritten into a dark figure-8 shape; k is from the word.
10. **Row 22–23 `meggyozödik`**: the sign in the middle of the *ggy* group is written S-like (k/g class); read as part of *meggyőződik*, which the next row confirms.
11. **Writer's spellings normalized**: *köszönőg* → köszönök (g for k, the sign is the g shape), *szolgenak* → szolgálnak, *bar|mi*: the bars are a; *abba* → abban, *örömel* (row 10, four strokes for mm) → örömmel, *tovabra* → továbbra, *ara* → arra, *raer* → ráér[ek], *felattem* → felettem, *lőbel*: *minél előbb el-* with *e* at the end of row 19, *menyi* → mennyi, *akor* → akkor, *kerzeztem* → kérdeztem (z for d; a sense correction), *azta* with *hogy*: normalized *azt a*, *vanakőztünk* → vannak köztünk (one k serves both words, or a k is dropped; the n of *vannak* is also single), *abol* → abból, *roszsta mit* → rosszat, mit (order of letters).
12. **Row 3 final `b.`** is an abbreviation with its own point; *B[ecses]* comes from *becses sorai* in row 7.
13. **Not ciphertext**: the address (Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás; *Szépreményű* is the courtesy epithet found on HCP1212, 1244, 1245, not a name), and the printed title and verse on the picture side (*Ezüsttükrös kávéházban*, *Üldögélek elmélázva / Csendesen…*). The postmark date is not legible, so the card is undated.
14. **Over-marks**: the ledger writes the marks over the o loops of row 5 as dots for the first two and ticks for the third, but all three are short strokes on the 3.4x crop; ö/ő cannot be separated firmly in this hand, and acute ticks over vowels are not recorded in the ledger except where they change a sign class.

## Why it is correct

- The key comes unchanged from reviewed finished cards. It turns all 775 written letter signs of the 32 rows and the stamp block into Hungarian; only the blotted and hidden signs in items 5 and 6 have no read value (2 tokens).
- The text is coherent connected prose over long runs that could not be forced: *igazán sajnálom, hogy továbbra is azon kell gondolkoznom*, *felettem más rendelkezik*, *meggyőződik róla… hogy mennyi szabadom van*, *nem akarom munkájába zavarni*, *abból ne gondoljon minden rosszat*. Rendel|kezik and meggyőző|dik cross row breaks.
- Repeated words decode identically (*hogy* 11 times, *édesem* 5 times, *sorai-* several times).
- The family's formulas recur: *ha feljön… Pestre*, signature Feri, formal address, *kedvese* under the stamp as on HCP1216, Pest as on the family's other cards. The plain *folyt. köv.* fits a letter running beyond the card.

## Stamp-box message (2026-11-03)

Stamp-box audit by Claude Opus 5.5 on the human's instruction. The stamp is lifted; the stamp box (upper right of the address side, faint ruled outline) holds six short rows in the green-ink cipher signs, no plain Hungarian. A black postmark triangle lies over rows 3–5. Crops: `work/stamp-2026-11-03/` (3x of the whole box, 5x of row 3 with a green-minus-red channel separation). The reading already in the ledger and above was re-read sign by sign and stands unchanged:

- Literal: `üdvozli / atavol / bo{?}ze / retőked / vesse / feri`
- Hungarian (normalized): Üdvözli a távolból szerető kedvese Feri.
- English: Greetings from afar from your loving sweetheart, Feri.
- Slovak: Pozdravuje Vás z diaľky Váš milujúci milý, Feri.

Unread: one sign in row 3, under the postmark triangle. In the channel-separated crop it is a diagonal stroke with a short hook at the top, not matching a key sign with certainty; *távolból szerető* needs l and sz here, so the restoration is disclosed (item 6), and one sign cannot give both, so the writer also dropped a letter. Row 5 `vesse` is normalized *kedvese*. Nothing else in the box is unread. The reproduction script already decodes these stamp rows from the ledger; it was not changed.

## Response to review 1

Review verdict REVISE. I rechecked each finding on the reviewer's crops and on my own crops of the hi-res address scan (`work/crops/g*.png`, `h*.png`). All are accepted; the ledger, `work/normalized-opus.txt` and this file are corrected, `work/apply_review1.py` records the exact ledger edits, and the reproduction command was re-run: all four hashes OK, output equal to the block above.

1. **Row 23 (major): fixed.** The crop shows h/p, two bars, cross with short arms, three strokes, wave: *ha fel-*. Ledger `H E Z A L` → `H A + E L`. Text *ha feljön(ne) Pestre*, "come up to Pest". My earlier "*el* is a correction" and "*hez*" are withdrawn. `jönek` stays disclosed (item 4).
2. **Row 30: fixed.** Bars, section mark, ticked loop: literal `vanakőztünk`, one k. The wrong E and the extra K are removed, the ő added. Item 11 now says a k is restored.
3. **Row 28 *már*: fixed.** Two bars with a tick; `M A F`. Removed from item 11.
4. **Row 15: fixed.** `) Z N E K`, no e; *egésznek* is spelled correctly. Removed from item 11.
5. **Stamp row 5: fixed.** Five signs, literal `vesse`; disclosed in item 6. The sign count in "Why it is correct" now rests on the full ledger.
6. **Row 32 cross: fixed.** It is z, stroke for stroke as in row 15. Item 1 narrowed; the word stays unread.
7. **Row 30 i: fixed.** Dot recorded in item 3.
8. **Plain word: fixed.** *Szépreményű*, item 13. It is not a name.
9. **Small slips: fixed.** Rows 5 and 20: ticks written as ő (see item 14 on the limit of that call). Row 18 point added. Counts corrected: *édesem* 5, *hogy* 11, and *becses* dropped from the repeated words.
10. **Values not shapes; rows 14–25: rechecked.** The ledger's format stays a value ledger, as stated. I read rows 14–25 at 2.5x (`g1L`–`g4R`) and zoomed the row 17 end (`h17.png`: *érek* has three bars twice) and row 23 end (`h23b.png`: *Pest* has three bars; the k crosses the card's dashed line). No further sign changed. Row 28 end is now A (`idegenan`).

Effect on the reading: one clause wording changes (*eljön* → *feljön*, same sense) and the normalization of a few forms; no change to the key or to the sense of the card. No new round is needed, as the review itself states. I also read the printed picture-side verse, which the reviewer left unread; it is not cipher.
