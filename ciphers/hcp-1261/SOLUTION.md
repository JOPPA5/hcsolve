# HCP1261 — Feri to Jolánka Tóth: "if only the letter could fly" (March 1912)

**Status: whole message read; small disclosed points below; review 1 (REVISE) addressed, see the last section.** Written 2026-11-01 by Claude Opus 5.5. No earlier work exists on this number. The portal shows status *Not solved* and attaches no transcription or solution; no published solution was used. The transcription is my own (none attached). The key is transferred from finished sister cards.

## Cipher type and key

Hungarian (the portal says language Unknown), simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family, same key as HCP1216 (fullest legend; also 1212, 1213, 1217, 1218, 1243, 1301). No key element was changed and no new sign value was needed.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S) | k | F-like | r |
| six | b | wave | l | hook ")" | s |
| six + hook (opposed bowls) | cs | three strokes | m | gamma | t |
| tick left + long stroke | d | two strokes | n | plain x | u (dots ü) |
| three bars | e | cursive loop | o (dots ö) | chevron | v |
| upright cross | f | long stroke + tick right | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | g + y joined | gy | | |

Reading order: rows 1–19 on the left half; then the column **down the left edge** (*b. sorait*), which turns the corner into the **bottom edge** (*várva … Feri*); then the stamp box.

Not cipher: address in plain hand: *Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás*. Picture side, printed verse: *Örömest jöttünk ki az éjszakába, / Nem háborgat minket a hold világa. / Jer közelebb drágám ülj ide, / Hadd nézzek gyönyörű szemedbe.* Postmarks: one with 912 and a Roman month, partly lost; one with 912 MAR 7, agreeing with the date in the portal file name. The last words of the stamp box are in plain cursive.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1261/work/decode_opus.py
```

It checks the SHA-256 of all four scans, decodes `work/ledger-opus.txt` (one token per written sign, 19 rows + edge + bottom + 6 stamp rows, 445 tokens: the cipher signs, 2 dots, 1 valueless blot and 1 plain M), prints the literal letters and then `work/normalized-opus.txt`. The ledger is a manual transcription from enlarged crops of the hi-res original (`work/crops/`), not OCR. (`work/make_ledger.py` is the one-off that expanded my row list to tokens.)

## Literal decipherment (as printed; * = blotted or ambiguous sign, [#] = blot without a value, ^ = plain letter)

```
01 neharagudjonertehogy          12 pomsoritugyszeretnem
02 ijsürünküldömalapo            13 harepülnealev*elerepülö
03 katdeennemagygondol           14 gepetszerzekbehogygy
04 kozommintönenekem             15 orsabanjönnebecseslapjai
05 jolesikhaönnelbeszel          16 m^idengondolatnal
06 hetekedesjolankammert         17 atettlegtöbbeter
07 enmikorsoraimirom             18 igytes*zkicsókotad
08 ö[#]nn*ekugyerzemmagammint      19 snempediglenker
09 habeszlgnekedesjolankam       edge    b.sorait
10 elsemtudjakepzelaimily        bottom  varvamaramaradokszivenekrabszolgajaferi
11 hoszuidöazmegmegka            stamp   istenvele / atavolb. / olcsoko / ljaszam / talanszo / r [plain:] egy igaz / sziv
```

## Hungarian (normalized)

Ne haragudjon érte, hogy ily sűrűn küldöm a lapokat, de én nem [úgy] gondolkozom, mint Ön. Énnekem jól esik, ha Önnel beszélhetek, édes Jolánkám, mert én, mikor soraim írom Önnek, úgy érzem magam, mintha beszélgetnék, édes Jolánkám. El sem tudja képzelni, mily hosszú idő az, még megkapom sorait. Úgy szeretném, ha repülne a levele; repülőgépet szerzek be, hogy gyorsabban jönne becses lapjai. Minden gondolatnál a tett legtöbbet ér. Így tesz, ki csókot ad, s nem pediglen kér. B[ecses] sorait várva maradok szívének rabszolgája, Feri.

Stamp box: Isten vele! A távolból csókolja számtalanszor egy igaz szív.

## English

Do not be angry that I send you cards so often, but I do not think the way you do. It does me good when I can talk with you, my sweet Jolánka, because when I write my lines to you I feel as if I were talking [with you], my sweet Jolánka. You cannot imagine what a long time it is until I get your lines. How I wish your letter could fly; I will get an aeroplane so that your esteemed cards come faster. Above every thought, the deed is worth the most. So does he who gives a kiss and does not merely ask for one. Awaiting your esteemed lines, I remain the slave of your heart, Feri.

Stamp box: God be with you! From afar one true heart kisses you countless times.

## Slovak

Nehnevajte sa, že Vám tak často posielam pohľadnice, ale ja [tak] nezmýšľam ako Vy. Mne dobre padne, keď sa môžem s Vami rozprávať, sladká moja Jolánka, lebo keď Vám píšem svoje riadky, cítim sa, akoby som sa rozprával, sladká moja Jolánka. Ani si neviete predstaviť, aký dlhý je to čas, kým dostanem Vaše riadky. Tak by som chcel, aby Váš list letel; zaobstarám si lietadlo, aby Vaše vážené pohľadnice prichádzali rýchlejšie. Nad každú myšlienku má najväčšiu cenu čin. Tak robí ten, kto bozk dáva, a nie ten, kto oň prosí. Čakajúc na Vaše vážené riadky, zostávam otrokom Vášho srdca, Feri.

V rámčeku na známku: S Bohom! Z diaľky Vás nespočetnekrát bozkáva jedno verné srdce.

## Uncertainties

Calls that rest on word sense:

1. **Row 3 *nem agy gondolkozom*.** The signs before *gy* are clearly two bars (a); the sense wants *úgy* ("I do not think that way"). I print the sign as written and supply [úgy] editorially. This is a writer's slip by interpretation, not a reading. *[n]agy* would not make sense; the clause reads either way as "I do not think as you do".
2. **Row 8 *ö[#]nn*ek*.** Six written signs: ö, a heavy blot (an overwritten sign), two strokes, a two-stroke sign whose second stroke is longer, nearer d than n, three bars, k. Taken as *önnek* ("to you"). The word needs only five signs, so the blot is treated as a discarded false start and gets no value; the last n is read against its shape. All of this rests on word sense.
3. **Row 13 *lev*ele*.** The fourth sign is a heavy overwritten blot with a chevron-like right arm; v rests on shape plus sense. The n of *repülne* has the wave l written above the line.
4. **Row 13 *a levele, repülőgépet*.** The signs are l e v e l e r e p ü l ö and the writer leaves no word spaces. I divide *levele* ("your letter", possessive), which adds or changes no sign and agrees with *sorait* and *becses lapjai*. Rejected in review: *a levél: e repülőgépet* ("this aeroplane"), because the picture side shows a couple by moonlight, with nothing for *e* to point at, and *er[r]e repülőgépet*, which needs an added sign. *Repülőgép* in 1912 is apt: the *be* of *szerzek be* and the *hogy* are clear.
5. **Row 18 *te*sz*.** The third sign is an overwritten blot, read s on word sense (*így tesz, ki csókot ad*).
6. **h/p sign:** taken as p in *lapo-, megkapom, repül, gépet, képzel, lapjai, pediglen*, as h elsewhere, on word sense only; the sign is the same. d (tick left) versus h/p (tick right) is also not cleanly kept: *édes* in rows 6, 9 and *pedig* show a near-identical stroke pair. *pediglen* is a genuine older emphatic form of *pedig*.
7. **Row 10 *képzel a i*:** the sign where *képzelni* needs n is two horizontal bars (a), a writer's slip; normalized *képzelni*.
8. **Writer's omissions, printed as written, restored only in normalization:** *beszlgnek* → beszélgetnék (row 9), *sorit* → sorait (row 12), *Miden* → Minden (row 16), *hoszu* → hosszú, *orsaban* → gyorsabban, *ij* → ily (cf. *ojan* on HCP1216), *még* for *míg*. Row 14 has *gy gy* at the row end: *hogy* + the *gy* of *gyorsabban*. *jönne* with plural-sense *lapjai* is left singular as written.
9. **Bottom edge *várva mara maradok*:** the writer began *mara* and restarted; the first three-stroke sign is unevenly spaced. Normalized *maradok* once.
10. **Left edge *b.*:** six followed by a dot; expanded *b[ecses]* because *becses lapjai* occurs in row 15. This is an interpretation: the same six + dot ends stamp row S2 in the middle of *távol-b.-ól*, where it cannot be an abbreviation, so this writer's dot after 6 need not mark one. The column reads downward and its final t sits at the corner, directly before *várva*.
11. **Stamp box:** heavy ink. S2's first sign is a filled loop read as a (*a távolból*); it is not the usual two bars and could be the loop o, but only *a* gives sense. S4's second sign is a heavy inverted T with bars read j (*csókolja*). The closing *egy igaz szív* is plain cursive, heavily inked; the last word looks like *sziv/szin*, and *szív* is chosen on sense.
12. **Unread plain line:** a short line of plain cursive stands below *úrleánynak* in the address, partly under the collection stamp: approximately *sz·n/v·t g/f·e … e e e t e*. I could not read it. It is outside the cipher text and is not part of the message; it is reported, not forced.
13. **Row 16, first sign:** a plain Latin cursive capital M, not the three-stroke cipher sign; the rest of the word is in cipher. So apart from the closing words of the stamp box and the address, this one letter is also plain.
14. Sender: the signature on the bottom edge reads *feri*. No surname is claimed. Acute accents are mostly invisible and are supplied in normalization.

## Why it is correct

- The family key, unchanged, gives continuous Hungarian across all rows, the edge column, the bottom row and the stamp box. No value was invented; every cipher sign has a value (the one blot in row 8 is taken as a false start).
- The reading order was discovered from the text: *…nem pediglen kér* / *b. sorait* (edge) / *várva maradok…* (bottom) runs through the corner as one sentence.
- Repeated words decode identically (*édes Jolánkám* rows 6 and 9; *beszél-* rows 5 and 9; *sorait/soraim* ×4; *becses* row 15 and *b.*).
- The content fits the family: formal Ön address, longing for letters, *rabszolgája*, the Feri signature, and the stamp-box closing formula (*számtalanszor*), as on HCP1216 and HCP1264. The address and recipient agree with the portal.

Credit: transcription and decipherment by Claude Opus 5.5; the key comes from earlier finished family cards (first worked out with the OpenAI GPT solver, see HCP1216 notes).

## Response to review 1

Verdict REVISE. All five findings accepted; the reading was re-checked on the crops. `python3 -I ciphers/hcp-1261/work/decode_opus.py` re-run after the fixes: all four hashes OK, output matches the sections above.

1. **Major, row 13 division: fixed.** Crop `review/work/crops/r13.png` shows l e v e l e r e p ü l ö, so *levele* changes no sign. Normalized text, English, Slovak and uncertainty 4 now read *a levele; repülőgépet szerzek be*. The old division stays only as a rejected alternative. The ledger letters of this row did not change. The change is one word division, not a change of signs or key.
2. **Minor, row 8 count: fixed.** Crop `work/crops/r8l.png` confirms six written signs. The ledger now has `#!`, a blot with no value, printed `[#]`; the total is 445 tokens, not 444. *Önnek* stands, on word sense (uncertainty 2).
3. **Minor, plain M in row 16: fixed.** Crop `review/work/crops/a5.png` shows a Latin cursive capital. Ledger token `M^`, printed `m^`; disclosed as uncertainty 13. The value is unchanged.
4. **Minor, dot after 6: fixed.** Uncertainty 10 now mentions the S2 dot in *távol-b.-ól*. *B[ecses]* is kept as the best expansion, marked as an interpretation.
5. **Minor, English row 9: fixed.** "talking [with you]" is now bracketed, since the Hungarian has only *beszélgetnék*.

`work/make_ledger.py` was updated in step with the ledger and regenerates it exactly.
