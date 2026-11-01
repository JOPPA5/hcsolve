# HCP1248 — Feri to Jolánka Tóth: invitation to the railwaymen's vintage ball, 5 October

**Status: complete reading; review 1 verdict REVISE, all findings addressed (see the last section).** Claude Opus 5.5, 2026-11-01.

Credit: all reading of this card is by Claude Opus 5.5 on 2026-11-01; there was no earlier work on this number. The key is transferred unchanged from finished Jolánka cards (HCP1216, 1213, 1217, 1218, 1243, 1301), whose earlier passes were by the OpenAI GPT solver and Claude Opus 5.5. The portal shows status Not solved and attaches no transcription or solution (source/metadata.md); no published solution of this card was found or used. The date 1913-09-13 comes from the portal file name (`cpc_1913-09-13_…`), not from my reading of the postmark.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka family). Same sign classes as HCP1216:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S-shape | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| long stroke + tick upper left | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + tick right (h/p near-homograph) | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

On this card *gy* is written as two signs, g + y. Dots over o/u give ö/ü. *Okt* and the numbers 5 and 15 are not enciphered: *Okt* is in Latin letters and 15 is plain digits; the 5 has the same shape as the writer's k sign, and it is read as a digit because *5-én* ("on the 5th") is the only sense and it matches the 5 of 15.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1248/work/decode.py
```

It checks the SHA-256 of both scans in source/ and both originals in work/hires/, decodes `work/ledger.txt` (616 tokens: one per written sign, 25 main rows and 7 rows in the stamp box) with the key above, and prints the literal letters row by row and then `work/normalized.txt`. The ledger is a manual transcription from enlarged crops (`work/crops/`), not OCR.

## Literal decipherment (as printed by the command; h stands for the h/p sign)

```
01 edesegyetlenreményemnetün      14 latságlesznekvagyezren
02 jonfelhogyegyszetrekét         15 isnagyo[blot].onszeretnemha
03 lahotisirokdehirtelenjöt       16 eljonnemertugysemmulat
04 egyjóötletemnagyonorül         17 hatunkmáskéhegyütmert
05 nekhamaganakismegtetszene      18 itnagyonnehézszabadidőt
06 <Okt><5>énleszavasutasoknaka   19 kahnimostiscsakugykahnék
07 szüretimulatságéshamaga        20 rendezölennéktehatke
08 nakkedvevolnaeljönniak         21 remhogygyorsangondol
09 korbeléhnékrendezönekazt       22 jamegadolgotmert<15>
10 elöreigégremhogyojjan          23 igbekeljelentenihogy
11 mulatsagbamégnemvolt           24 rendezöakaroklenniezelbezatomsoraim
12 ésfogalmasincsrorahogy         25 maradokb.soraitvarokedvesseferi
13 mijenlehetegyhestimu
stamp box: istenve | leédesem | aboldog | viszont | latasr | hűkedves | seferi
```

## Hungarian (normalized)

Édes egyetlen reményem! Ne tűnjön fel, hogy egyszerre két lapot is írok, de hirtelen jött egy jó ötletem. Nagyon örülnék, ha magának is megtetszene. Okt. 5-én lesz a vasutasoknak a szüreti mulatság, és ha magának kedve volna eljönni, akkor belépnék rendezőnek. Azt előre ígérem, hogy olyan mulatságban még nem volt, és fogalma sincs róla, hogy milyen lehet egy pesti mulatság; lesznek vagy ezren is. Nagyon szeretném, ha eljönne, mert úgy sem mulathatunk másképp együtt, mert itt nagyon nehéz szabadidőt kapni. Most is csak úgy kapnék, ha rendező lennék. Tehát kérem, hogy gyorsan gondolja meg a dolgot, mert 15-ig be kell jelenteni, hogy rendező akarok lenni. Ezzel bezárom soraim, maradok b[ecses] sorait váró kedvese, Feri.

Stamp box: Isten vele, édesem, a boldog viszontlátásr[a]! Hű kedvese, Feri.

## English

My sweet only hope! Don't be surprised that I am writing two cards at once, but a good idea has suddenly come to me. I would be very glad if you liked it too. On 5 October the railwaymen are holding their vintage ball, and if you felt like coming, I would sign up as a steward. This I promise you in advance: you have never been to such a ball, and you have no idea what a Pest ball can be like; there will be as many as a thousand people. I would very much like you to come, because we cannot have fun together any other way, since it is very hard to get free time here. Even now I would only get it if I were a steward. So I ask you to think it over quickly, because by the 15th I have to report that I want to be a steward. With this I close my lines, and remain, awaiting your [dear] lines, your sweetheart, Feri.

Stamp box: God be with you, my sweet, until our happy meeting! Your faithful sweetheart, Feri.

## Slovak

Moja sladká jediná nádej! Nečudujte sa, že píšem naraz dva lístky, ale náhle mi prišiel dobrý nápad. Veľmi by som sa potešil, keby sa páčil aj Vám. 5. októbra bude vinobranecká zábava železničiarov a ak by ste mali chuť prísť, prihlásil by som sa za usporiadateľa. Vopred Vám sľubujem, že na takej zábave ste ešte neboli a nemáte potuchy, aká môže byť peštianska zábava; bude tam aj okolo tisíc ľudí. Veľmi by som chcel, aby ste prišli, lebo inak sa spolu aj tak nemôžeme zabaviť, keďže tu je veľmi ťažké dostať voľný čas. Aj teraz by som ho dostal, len keby som bol usporiadateľom. Prosím Vás teda, aby ste si to rýchlo rozmysleli, lebo do 15. treba ohlásiť, že chcem byť usporiadateľom. Tým končím svoje riadky a zostávam, čakajúc na Vaše [milé] riadky, Váš milý, Feri.

V rámčeku na známku: S Bohom, moja sladká, do šťastného zhľadania! Váš verný milý, Feri.

## Uncertainties

The writer drops and repeats letters; the ledger keeps what is written and normalization is editorial.

Calls that rest on word sense, not on a clean sign match:

1. **h/p**: the same sign is read h in *hogy, hirtelen, ha, lehet, nehéz, hatunk, tehát, hű* and p in *lapot, belépnék, pesti, másképp, kapni, kapnék*. All are decided by the word.
2. **Row 9 `azt`**: the sign after the two bars is a heavy, apparently overwritten crossed sign with a tail. It looks partly like an A. Read as z from context (*Azt előre ígérem*); the crop is `work/crops/z_r9.png`.
3. **Row 18 *szabadidőt***: the z of *sza-* is a tilted cross, between the f-cross and the z class, read z by the word. Row 18 ends `…adidőt`. After *ad* comes a faint, overwritten-looking sign: it has a flat arm to the right with no descending curl and a dot high above it, which fits the i sign, not the o, whose arm curls down. **The i is probable, not certain.** Next comes a short stroke leaning on a long one, crossed by the printed blue line, read d (shape not fully clear under the line), then o with two marks above (ő) and t. If the faint sign were a corrected o, the row would read `…adodot`, a repeated *szabadot kapni*; the sense, "get time off", is the same either way.
4. **Row 19 first *kapni***: the tick of the p sign sits low beside the stroke, unlike the usual upper position. Read p by the word.
5. **Row 24, k of *akarok***: the first k has its lower half on a pale abraded spot; the upper part fits the k sign. Exactly one letter gives the word, so this is a partial restoration.
6. **Missing i dots**: in row 13 and in the stamp box (*isten*) the i sign has no visible dot.
7. **Row 25 `b.`**: a 6 with a dark blot inside it, followed by a dot, before *sorait*. Expanded *b[ecses]* ("your dear lines"), a common letter formula. **The expansion is my conjecture**; the card shows only b and a dot. The rest of the formula does not depend on it.
8. **Row 15**: after *nagyo* a sign is deliberately blotted out with a dot beside it, then *on* is written. I take this as a corrected slip; nothing is read from the blot.
9. **Stamp box row 6 *hű***: the h is faint, and the marks above the cross are one small tick and a trace; ű is chosen by the formula *hű kedvese* (HCP1216 has *sírig hű kedvese*).

Writer's spellings normalized: *egyszetre* → egyszerre and *bezatom* → bezárom (t written for r both times, clear signs); *rora* → róla (r for l, clear sign); *igégrem* → ígérem (an extra g); *ojjan* → olyan (j for ly; compare *mijen* on this card and *ojan* on HCP1216); *it* → itt; *jöt* → jött; *mijen* → milyen; *kel* → kell; *ezel* → ezzel; *másképegyüt* → másképp együtt; *mulatságba* → mulatságban; *orülnék/eljonni* have no visible dots in places; *kedvesse* (twice, rows 25 and S6–S7) → kedvese; *latasr* → látásr[a], final a not written. Row 25 shares one k: *várokedvesse* = *váró kedvese*.

## Why it is correct

- The key, transferred unchanged, turns all 616 signs into Hungarian; no sign lacks a value except the writer's own blot.
- Repeats decode the same at different places: *hogy* ×5, *mert* ×3, *mulat-* ×4, *rendező-* ×3, *nagyon* ×3, and *kedvese Feri* in both closings, with the same *ss* spelling.
- The content is specific and hangs together: a railwaymen's vintage ball in Pest, the need for leave, the steward's post that would get it, and a deadline. The signature Feri, the formal address and *hű kedvese* match HCP1216, where Feri passes through Vámosgyörk on the railway.
- External checks: 5 October 1913 was a Sunday, a natural day for a ball. If the portal's date of 13 September is right, the deadline of the 15th explains *gyorsan* ("quickly") only if it means 15 September, two days later; the card does not name the month, so this is an assumption.

## Response to review 1

Verdict REVISE. I checked each finding on the reviewer's 5x crops (`review/work/z_*.png`) and on my own `work/crops/z_r18.png`. I accept all six. `work/ledger.txt`, `work/normalized.txt`, this file and `NOTES.md` are updated, and the command was re-run: all four hashes OK, 616 signs, output equal to the blocks above. The key is unchanged.

1. **Row 10 *ojjan* (major): fixed.** `z_r10_ttan.png` shows two clear inverted T signs after *hogy o*, the family's j, and not the gamma t. My `O T T A N` was a misreading. *ojjan* = *olyan*. The ledger, literal block, normalized text and all translations are corrected, and the paragraph calling rows 10–11 the weakest sense point is deleted. The clause is one complete sentence.
2. **Row 12 *és* (minor): fixed.** `z_r12_first.png` shows three separate strokes and a separate dot above them. The ledger now has `E:a`, and the wrong description in uncertainty 6 is gone. The note on missing i dots in row 13 and the stamp box stays, because it is independent.
3. **Row 18 *it* (minor): fixed.** `z_r18_itt.png` shows one gamma; the grey smudge at the end of its arm has no ink stroke. The ledger now has `I T N A`, 616 tokens, and *it* → itt is on the spelling list.
4. **Row 20 *lennék* (minor): fixed.** `z_r20_lann.png` shows three bars. The ledger now has `L E N N`, and the *lannék* note is removed.
5. **Row 18 end *szabadidőt* (minor): accepted.** In `z_r18_end.png` the faint sign has the flat right arm of the i and a dot high above, and it has no o curl. The ledger now has `D I D O:da T`. It looks overwritten, so uncertainty 3 calls the i probable and gives *szabadot* as the fallback with the same sense.
6. **Wording (minor): fixed.** The claim "every word is read clearly" is removed, the token counts are updated, and `NOTES.md` records the misread j.
