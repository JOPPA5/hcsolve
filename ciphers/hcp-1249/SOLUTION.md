# HCP1249 — Feri to Jolánka Tóth: invitation to a July ball

**Status: reading of all signs complete; two isolated words keep an unresolved form (rows 1 and 23, Uncertainties 1–2), and stamp row S3 is tentative. Revised after review 1.** Written 2026-11-01 by Claude Opus 5.5.

Credit: all reading on this card is by Claude Opus 5.5. The key was not invented: it is the Jolánka-family key established on finished cards HCP1216, 1212, 1213, 1217, 1218, 1243, 1301 (earlier passes by the OpenAI GPT solver, GPT-6 Astra / GPT-6.1 Sol, completed by Claude Opus 5.5). No earlier work exists on this number. The portal shows status *Not solved* with no transcription or solution; no published solution was found.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka postcard family, same key as HCP1216). Digits and word spacing are plain. Word division is mostly absent or unreliable.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | S shape, short | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three strokes | m | gamma (Γ) | t |
| long stroke + short stroke, crossed or joined | d | two strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + tick (near d) | h / p | low descender | y |
| hooked S with long descender | g | dotted loop | i | cross with long tail | z |
| inverted T (often tilted) | j | opposed bowls | cs | | |

Marks: tick over bars = é; tick or dots as written on o/u give ö, ő, ü, ű. Most other accents are not written and are supplied in normalization.

Word-sense calls (signs that do not settle the letter alone):
- **k/g**: the writer's short S and hooked S overlap in *hogy* (row 2), *meg*, *Árokszállás*, *alig* and *lánynak* (row 3); I took the value from the word. The k of *lánynak* rests on word sense alone: pixels do not separate it from g.
- **h/p**: one sign, split by word sense: h in *hogy, ha, ahol, hívom, hamar, hozom, elülhet, hű*, and p only in *percz* (stamp row S6). The sign's long first stroke separates it from n, whose two strokes are equal. This is a pixel contrast, and it is what changed row 2 and S6 in review.
- **d/n**: *idő, gondol, áldozat, kedves, maradok, megfordítva, minden, édesebb, hidd* rest partly on word sense where the d is written with two near-parallel strokes.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1249/work/decode.py
```

It checks the SHA-256 of the two source images and two hi-res originals, decodes the 602-sign ledger `work/ledger.txt` (28 main rows, 7 rows under the stamp) and prints the literal rows, then `work/normalized.txt`. The ledger is a manual transcription from enlarged crops (`work/crop.py`, `stampcrop.py`, `st2.py`, `st3.py`; output in `work/crops/`). The rows under the lifted stamp were read in the blue channel, which suppresses the blue printed triangle. `[x]` in the output means read through damage.

## Literal decipherment

```
01 meretségmertnemugyvan          S1 csokjai[t]
02 minarokszalasbahogyha          S2 alig[v][a]
03 nincsegylanynakismerős         S3 [r][o][m][h][i][d][d]
04 selelülhe[t]reggeligés         S4 edeseb
05 amiatestvéreitillet            S5 anal[a]
06 azoknaksemkifogasokel          S6 percz
07 lén[e]merttelégtekin           S7 n[é]lferi
08 téjesmulatsagbahivom
09 aholnemmindenkifor
10 d[u]lnatmeskülömbenis
11 mégleszidőmegondolas
12 rametcsakjulius24és25
13 énleszkedvesemene[r]anem
14 isakarokgondolnihogy
15 nemjönelmerthamarmeg
16 hozomazanyagialdozatot
17 mulatisszetnékkedvem
18 remutné[{s|k}]azmarne[m]iskel
19 irnomhogy[o]terzemjol
20 magamaholmaga[i][s]otvan
21 kedvesemremélemhogy
22 mégarokszálasbavi
23 szontfukegybiztosat
24 nemirhatokmertnekem
25 mindenmegforditva
26 téljesülmiténisalig
27 varokezelbezaromsoraim
28 maradoksirighűkedveseferi
```

## Hungarian (normalized; square brackets = supplied or unresolved)

[Meretség], mert nem úgy van, mint Árokszállásba, hogy ha nincs egy lánynak ismerőse, [l]elülhet reggelig, és ami a testvéreit illeti, azoknak sem kifogások ellene, mert elég tekintélyes mulatságba hívom, ahol nem mindenki fordul[h]at me[g]. Különben is még lesz idő meg[g]ondolásra, me[r]t csak július 24 és 25-én lesz. Kedvesem, én er[r]e nem is akarok gondolni, hogy nem jön el, mert hamar meghozom az anyagi áldozatot. Mulat[n]i is sze[re]tnék kedvemre, mu[la]tnék (or mut[at]nék), az már nem is kel[l] írnom, hogy ott érzem jól magam, ahol maga is ot[t] van. Kedvesem, remélem, hogy még Árokszállásba viszont[...]uk. Egy biztosat nem írhatok, mert nekem minden megfordítva teljesül, mit én is alig várok. Ezzel bezárom soraim. Maradok sírig hű kedvese Feri.

Under the stamp: Csókjait alig várom, hidd, édesebb annál a percznél. Feri.

## English

[Meretség: unresolved, perhaps "a daring thing"], because it is not as in Árokszállás, where if a girl has no acquaintance she can sit there until morning; and as for your brothers and sisters, they too [can have] no objections to it, because I am inviting you to quite a respectable ball, where not everybody can turn up. Besides, there will still be time to think it over, because it will only be on July 24 and 25. My dear, I do not even want to think that you will not come, because I will soon make the financial sacrifice. I would like to enjoy myself to my heart's content too, I would make merry (or: I would show [it]); there is no need for me to write that I feel well where you are too. My dear, I hope that we will still [see each other?] again in Árokszállás. I cannot write anything certain, because for me everything comes true the other way round, which I too can hardly wait for. With this I close my lines. I remain, faithful unto the grave, your sweetheart Feri.

Under the stamp: I can hardly wait for your kisses; believe me, [they are] sweeter than that moment. Feri.

## Slovak

[Meretség: nevyriešené, azda „odvážna vec"], lebo to nie je ako v Árokszállási, kde ak dievča nemá známeho, môže tam presedieť do rána; a čo sa týka vašich súrodencov, ani tí proti tomu [nemôžu mať] námietky, lebo vás pozývam na dosť úctyhodnú zábavu, kam sa nedostane hocikto. Okrem toho bude ešte čas na rozmyslenie, lebo to bude až 24. a 25. júla. Drahá moja, ani nechcem myslieť na to, že neprídete, lebo tú finančnú obeť čoskoro prinesiem. Aj ja by som sa rád zabavil do sýtosti, zabával by som sa (alebo: ukázal by som [to]); to už ani nemusím písať, že sa dobre cítim tam, kde ste aj vy. Drahá moja, dúfam, že sa ešte v Árokszállási [uvidíme?]. Nič isté nemôžem napísať, lebo mne sa všetko plní naopak, čoho sa aj ja sotva dočkám. Týmto končím svoje riadky. Ostávam váš do hrobu verný milý Feri.

Pod známkou: Sotva sa dočkám vašich bozkov; ver mi, [sú] sladšie než tá chvíľa. Feri.

## Uncertainties

Signs are transcribed as written; the normalization is editorial.

Unresolved words (all signs read, form not settled; each is isolated and the sentence around it reads):

1. **Row 1 `meretség`**: all eight signs are clear (m e r e t s é g). No Hungarian word of this exact form is known to me. *merészség* ("daring") would fit if the writer dropped letters, as he does elsewhere, but this is a guess. No salutation precedes it. The reviewer found no better word.
2. **Row 23 `viszontfuk`**: the signs are clear (f = upright cross, u, k). *viszont[lát]juk* ("we see again") or *viszont[látni] fog[j]uk* is the obvious sense; both need dropped letters, and neither is on the card. The next word *egy* then starts the following sentence; *egy biztosat* is my division.

Readings that rest on word sense and on disclosed writer's slips:

3. **Rows 3–4 `lanynak ismerős|selelülhet`**: *ha nincs egy lánynak ismerőse, elülhet reggelig*, "if a girl has no acquaintance, she can sit there until morning". This needs three calls: k rather than g (Word-sense calls above); s doubled across the row break (*ismerősse*, as the writer's *kedvesse* on HCP1248); and one surplus l, so `lelülhet` stands for *elülhet* or *leülhet* ("can sit down"), the sense being the same. I reject *ismerőssel elülhet*: a comitative has no place in a "has no …" clause.
4. **Rows 9–10 `kifor|dulnat mes`**: word division *mindenki fordulhat meg*, "not everybody can turn up" (*megfordul valahol*). The signs are as transcribed: the pair in `dulnat` is near equal, so n and not h, and the sign in `mes` is the s bowl, not g. So the reading needs two slips (n for h, s for g). An alternative is *fordulna[t] me[g]*, "would turn up", which keeps n and drops a stray t: also two slips, same sense.
5. **Row 18 `mutné[{s|k}]`**: a blotted hook on a stain, s or k, read k. *mu[la]tnék* ("I would make merry", following *Mulatni is szeretnék*) and *mut[at]nék* ("I would show [it]") need the same size of omission; I give both and prefer neither firmly. The first is printed first only because it needs no unstated object. The m of *nem* in that row has one stroke blotted.
6. **Row 26 `mit`**: the antecedent of *mit* is not stated (the reunion, or what he cannot promise); the clause reads but its link is loose.

Damage:

7. **Stamp rows.** The stamp is lifted and its gum carried ink away. **S3 is the weakest row**: through the blot I see r, o, m, then an h/p sign and a dotted i, and only one clear d-like sign, so *hidd* is tentative, chosen for sense. *alig vá|rom* is supported by S2 and the sense. The last sign of S1 is a faint Γ. The a of S5 sits on the triangle print. The first vowel of S7 is a blurred blob with a tick: read é because *percz* takes a front-vowel suffix, and the blob itself does not decide it; *-nál* would be a slip.
8. **Row 7, ink blot** after *lén*: a dark overwrite on a lighter loop, with a double tick above that stays unexplained. I read e, giving *lén[e]*. With the end of row 6 the literal is *kifogasokel|léne*, normalized *kifogások ellene* ("objections to it"). *kifogásuk lenne* is an alternative; the sense does not change much. No verb is written in that clause.
9. **Row 13 `ene[r]a`**: blotted, heavy r. Literal *én erá*, normalized *én erre* (a vowel differs); this is an editorial fit.
10. **Row 19**: the blot before Γ is read o (*ot* = ott). **Row 20**: *is* in *maga is* has no visible dot and a blotted s; read from context. **Row 4 t**: heavy blot on Γ shape.
11. Writer's spellings normalized: *min* → mint, *arokszalasba* (single l; inessive -ba as spoken), *ismerősse* → ismerőse, *megondolas*, *met* → mert, *mulatis* → mulatni is, *szetnék* → szeretnék, *kel* → kell, *ot* → ott, *ezel* → ezzel, *mertt* (row 7, doubled t) → mert, *tekintéjes* → tekintélyes (phonetic), *külömben* (period spelling), *téljesül* → teljesül, *édeseb* → édesebb, *anal* → annál, *percz* (period spelling). The dropped syllables show that the writer skips letters often, which is why rows 1 and 23 stay open rather than being forced.
12. Address, outside the cipher: *Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás*. The postmark shows *BU…* and *914 MÁR*, which fits the portal's date 1914-03-25; the rest of the date is not legible enough. 24 and 25 July 1914 were a Friday and a Saturday. That is the only date check available and it neither supports nor contradicts the text. The sender field on the portal says Unknown; the card is signed Feri twice. I do not prove that this is the Feri of HCP1216, though key, hand style, addressee and the closing formula agree.
13. Plain-language oddity: the writer uses both *maga* (row 20) and *hidd* (stamp, informal, if that reading holds). This is an extra reason to treat *hidd* as tentative.

## Why it is correct

- The family key, unchanged, turns all 602 signs into Hungarian. No sign needed a new value.
- Nothing about the key was fitted to this card. The text brings its own checks: *Árokszállás* (twice, matching the address), *július 24 és 25* with digits, *testvéreit*, *tekintélyes mulatság*, *anyagi áldozat*, *meggondolás*, and the formula *maradok sírig hű kedvese Feri*, which matches HCP1216's stamp text.
- Repeated words decode identically: *hogy* ×4, *kedvesem* ×2, *nem* ×6, *Árokszállás* ×2, *alig* ×2.
- The content is coherent: he invites her to a respectable ball in July, answers the family's likely objections, and offers to bear the cost.

## Response to review 1

Verdict REVISE. I re-read every disputed place on the reviewer's enlargements (`review/work/z_*.png`, `g5.png`, `g5b.png`, `g6.png`). No finding touches the key. `python3 -I ciphers/hcp-1249/work/decode.py` was re-run after the edits: four hashes OK, 602 signs, output as printed above.

1. **Row 2 `na` → `ha`: fixed.** In `z_r2.png` the first stroke is about twice the second, unlike the equal strokes of n in `z_r3.png`. Ledger `N A` → `H A`; the former Uncertainty 10 is gone.
2. **Rows 3–4: fixed.** Ledger G → K in row 3, marked as resting on word sense. *ha nincs egy lánynak ismerőse, [l]elülhet reggelig*. The reviewer asked me to choose: `ismerősse` + surplus l, not *ismerőssel*, because the comitative has no place in that clause (Uncertainty 3).
3. **Rows 9–10: fixed, with one addition.** Division changed to *mindenki fordul[h]at me[g]*; signs unchanged, both slips disclosed. I add *fordulna[t] me[g]* as an alternative that keeps the written n; the sense is the same (Uncertainty 4).
4. **Stamp S6–S7: fixed.** In `z_s6.png` the S6 sign has a long first stroke and the n of S7 below has two equal ones. Ledger `P E F C Z` (new token P for the h/p sign read p). *annál a percznél*. S7's vowel is now é, still read through damage. The earlier claim that no word needs p is withdrawn.
5. **Row 26 `mot` → `mit`: fixed.** The dot is separate and in the normal position (`z_r26.png`, `g6.png`). Ledger O → I; *mo[s]t* removed.
6. **Row 20: fixed.** One Γ in `z_r20.png`; the tail after the blot belongs to the o. Ledger `O T V A N`, 602 signs; normalized *ot[t]*.
7. **Row 18: fixed.** Both *mu[la]tnék* and *mut[at]nék* are given (Uncertainty 5).
8. **Small errors: fixed.** Row 22 `A:acute` (tick confirmed in `g5.png`); row 24 is a (two bars, `g6.png`); *min* → mint added to the spellings; *hogy* ×4. I also corrected *nem* ×7 to ×6: a raw string count of 7 includes the false hit across *léne|mert*.
9. **Date check: done.** Friday and Saturday, in Uncertainty 12. I do not assert an Anna-day ball.

The reading of rows 2–4, 9–10, 26 and S6–S7 improved, but nothing changed in the key, the subject or the rest of the text, and I dispute none of the reviewer's readings. As the review says, these fixes need no new round. Rows 1 and 23 stay isolated and open; the batch rule treats this as a complete card.
