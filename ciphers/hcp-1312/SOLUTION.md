# HCP1312 — To Jolánka Tóth: "the Lord God created us for each other"

**Status: complete reading, review 1 verdict ACCEPT. The earlier attempt of 2026-10-30 was partial; see "Revision 2026-11-02".** Solver: Claude Opus 5.5.

No sender name appears on the card. The portal shows status Not solved and attaches no transcription or solution; the orchestrator's AI-register check of 2026-11-02 found no record of this card. No published solution was used. The whole transcription and decipherment are by Claude Opus 5.5 (2026-10-30 and 2026-11-02); the key was transferred from the finished card hcp-1216 and earlier finished Jolánka-family cards (the first passes on hcp-1216 were by the OpenAI GPT solver).

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the Jolánka postcard family). Key of hcp-1216, unchanged; `KEY` in `work/decode_rev2.py` gives it as sign class to letter:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | long slash + short tick | d | right bowl | s |
| six | b | three bars | e | gamma | t |
| left bowl | c | open loop, descender | g | plain cross x | u |
| opposed bowls (barred left bowl + right bowl) | cs | joined loop + descender | gy | chevron (Λ) | v |
| tall + short stroke | h / p | crossed dotted curve | i | crossed diagonal | z |
| inverted T | j | section mark | k | wave | l |
| three strokes | m | two strokes | n | cursive loop | o (dots: ö) |
| F-like | r | | | | |

Not used on this card: f, y.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1312/work/decode_rev2.py
```

It checks the SHA-256 of both source scans, decodes the sign ledger `work/ledger-rev2.txt` with the key and prints the literal letters and the normalized text. The ledger is a manual transcription from pixels, one token per sign (not OCR, and rows 1 to 13 were re-read knowing the earlier reading). In the output, (x) is a washed or stained sign read from enhanced crops, and {x} is a restored sign where only stroke width and count fit and the value comes from the word and the family closing. In the normalized text, [x] is a letter the card does not have as written (omitted or replaced). Enhanced crops: `work/rev2/`, made with `work/rev2.py`, `rev2b.py`, `rev2c.py`, `rev2d.py`, `rev2e.py` from `work/hires/` (run inside `work/` with the runtime Python that has PIL).

## Literal decipherment

```
01 kedvesjolankam           09 setdeebealegjobb
02 remelemhogya             10 gondolataibennevan
03 kedvebentalal            11 enazthiszemedeskincsem
04 jacoraimnalunk           12 sazmaskepemisle(h)(e)t
05 nincssemmiujsag          13 hogyminketazuriste(n)
06 hatönkneledesem          14 (e)(gy)(m)(a)(s)(n)(a)(k)(t)(e)(r)(e)(m)(t)(e)(t)
07 valamiujsagmost          15 {i}{s}{t}(e)(n)(v)(e)(l)(e)(a)(v){i}{s}{z}{o}{n}(t)(l)(a)(t)(a)(s)(r)(a)
08 mastnemcakazaver
```

## Hungarian (normalized)

Kedves Jolánkám! Remélem, hogy a kedvében találja [s]oraim. Nálunk nincs semmi újság. Hát ön[ö]knél, édesem? Valami újság? Most mást nem, c[s]ak az[t] a verset, de eb[b]e[n] a legjobb gondolatai[m] benne van. Én azt hiszem, édes kincsem, s az másképe[n] is lehet, hogy minket az Úr Isten egymásnak teremtet[t]. Isten vele, a viszontlátásra.

Plain in the stamp box: Édes angyalom, csók[ol]lak számtalanszor.

Plain address: Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás.

## English

Dear Jolánka! I hope my lines find you in [good] spirits. There is no news with us. And with you, my sweet? Any news? For now nothing else, only that verse, but my best thoughts are in it. I believe, sweet treasure, and it may also be otherwise, that the Lord God created us for each other. God be with you, until we meet again.

Stamp box: Sweet angel, I kiss you countless times.

Address: To the promising young lady Jolánka Tóth, Jászárokszállás.

## Slovak

Milá Jolánka! Dúfam, že Vás moje riadky zastihnú v [dobrej] nálade. U nás nie je nič nové. A u Vás, drahá? Niečo nové? Teraz nič iné, len tú báseň, ale sú v nej moje najlepšie myšlienky. Myslím si, sladký poklad, a môže to byť aj inak, že nás Pán Boh stvoril jeden pre druhého. S Bohom, dovidenia.

V rámčeku na známku: Sladký anjel môj, bozkávam Ťa nespočetnekrát.

Adresa: Sľubnej slečne Jolánke Tóthovej, Jászárokszállás.

## Uncertainties (all disclosed)

1. **Row 15 is washed.** Clear on the enhanced crops: n of Isten, both Λ (v), the wave l, t, a bars, and the end l a t a s r a. Bar signs here do not firmly separate a from e, so the a/e values in *vele a* rest on the formula. The first three signs of *Isten* (i, s, t), and *i s z o n* of *viszont*, are shapes and sign counts that fit rather than clean signs: stroke groups at the right widths in the right number (5 and 5), the i groups showing crossbar over loop, partly behind a stain at x≈1340–1420 in the hires scan. These eight signs are marked {x} in the ledger and output. In *viszont*, the s and z cannot be separated (one merged mass at x≈1235–1345), the o and n were not told apart as signs (a bar over a lobe, then a rounded nearly closed form), and part of the tail near x≈1420 belongs to the row 14 e above. The word is still certain, because v…t + látásra leaves only *viszontlátásra*. The reading of these signs is helped by the family closing *Isten vele, a viszontlátásra* (hcp-1216, 1212, 1301), which is a disclosed use of a parallel.
2. **Row 14** is washed but its signs can be counted one by one. The middle t of *teremtet* has its stem only (a stain covers any bar), and its e shows three displaced bars between foxing spots. There is **one** final t (*teremtet*), normalized to teremtett; there is no room or trace for a second.
3. **Row 15's slanted sign** with a crossbar, formerly the unread sign after "teremtett", is the t of *viszont*: row 15 climbs at its end, so it and *látásra* lie above row 15's baseline. It is not a textbook gamma: its stem rises above the bar and it has a small protrusion to the left. It is read as t because no other value fits *viszont*. The earlier idea that it belonged to row 14 is withdrawn.
4. **Row 12 *másképe[n]***, written *másképem*: the last sign before *is* is three strokes, the third shorter with a wedge top; m as written, normalized *másképen*. The *h/p* tall-short sign here is p by sense; in *hogy*, *hát*, *hiszem*, *lehet* it is h by sense. *s az másképen is lehet* is odd: *nem* would give "and it cannot be otherwise either", but *nem* is **not** on the card and is not supplied. The translation keeps what is written.
5. **Word-sense calls on clear signs.** r3 has *a kedvében* with no *legjobb* or *jó*, against the family formula *a legjobb kedvében*, so "good" and "dobrej" are supplied in the translations. r4 *coraim* has a plain left bowl where sense needs s (*soraim*). r8 *cak* has a barred left bowl alone where sense needs cs (*csak*); it is the left half of the writer's own cs sign. r10 first sign is a hooked g variant, g by sense. d/n: d is the slash with a tick in *kedves*, *édes*, *de*, *gondolatai*.
6. **Normalized writer's spellings**: *önknél* → ön[ö]knél, *az a verset* → az[t] a verset, *ebe* → eb[b]e[n], *gondolatai* → gondolatai[m] (the i's dot lies under row 9; no m follows). Acutes are not written and are supplied.
7. **Plain parts.** Stamp box: *Édes an / gyalom / Csók / lak szám / talanszor*, the third line written over the printed stamp mark. Faint traces right of the k, at the edge of the stamp mark and into the foxing, may be *ol*, which would make the card's own spelling *csókol-lak* in full; they are too faint to confirm, so the letters stay in brackets. The normalized word is *csókollak* either way. The sister card hcp-1206 spells it *csokolak*. Address: *Szépreményű*, *Tóth Jolánka*, *úrleánynak* are clear. The town line is washed; *Jász* and the accent ticks can be seen, and the rest is supported by the scan's file name (Jasz-Arokszalas) and the family's address. The word *Szépreményű* is translated "promising". The postmark is not legible; the date 1912-04 comes only from the file name.
8. The sender does not sign, so no identification with Feri of hcp-1216 or other cards is claimed.

## Why it is correct

The key is unchanged from the family and yields 14 rows of continuous, grammatical Hungarian on clean or countable signs. The reading refers to the picture side: the card's printed verse (*Csak egy kislányt hagyok itthon...*) is "az a vers" he mentions. Row 15, previously thought lost, gives the family's ordinary closing, with its clear signs in the expected places and the same sign count.

## Revision 2026-11-02

Ordered by the human, done by Claude Opus 5.5. No marker existed before this revision.

Open on 2026-10-30: all of row 15; the sign after "teremtett"; row 14 read from washed shapes; "lehet" partly by sense; town line and stamp box only roughly.

Tried: new crops from `work/hires/`. The earlier red-minus-green method loses the washed ink. **Blue minus green** does better: the diluted pink ink stays while brown foxing and paper vanish, and rows 14 and 15 appear as separate lines of stroke groups (`work/rev2/s1–s4, t1–t3, u1–u5, v1`).

Changed:
- Row 15 read: *Isten vele a viszont-látásra*. The earlier row 14 "…? látásra" tail belongs to row 15.
- Row 14 ledger corrected to a single final t (*teremtet*).
- Row 12 *lehet*: now read from the pixels: tall stroke + its short stroke under the blot, and three bars visible in the pink stain.
- Row 13 final n of *Isten* confirmed, faint; r6 *önknél* confirmed.
- Row 4 and 8 c/cs points and *másképem* re-examined and kept as written.
- Stamp box and address read in full, town line with the limits stated above.

## Response to review 1

Verdict ACCEPT. All five findings are minor. Each is addressed below, and no letter of the reading changed. `python3 -I ciphers/hcp-1312/work/decode_rev2.py` was re-run after the changes and its output equals the literal block and the normalized text above.

1. **Row 15 restorations not marked: fixed.** The ledger has a new `^` suffix, and the decoder prints those signs as {x}. Marked: i s t of *Isten* and i s z o n of *viszont*, 8 of the 24 row 15 signs. The reviewer counted seven. I also mark the t of *Isten*, because uncertainty 1 already names it among the signs that only fit. Uncertainty 1 now says that s and z are merged and that o and n were not told apart as signs.
2. **Stamp box line 3: fixed.** The review's crops `d1.png` and `f1.png` and my `work/rev2/stamp.png` show a faint curl and a rising stroke right of the k, running into the foxing. That is compatible with *ol* but not firm. Uncertainty 7 says so. One correction to the finding: *ol* + *lak* is *csókollak* in full, so no bracket inside it would be needed if the traces are *ol*. The bracket stays only because the traces are unconfirmed.
3. **"good" supplied: fixed.** Now [good] and [dobrej] in the translations, with a note in uncertainty 5.
4. **Crossbar sign: fixed.** A new blue-minus-green crop (x 1100 to 1720, y 1960 to 2110) confirms the description: the stem rises above the bar. Uncertainty 3 now discloses this.
5. **Bracket convention: fixed.** The normalized text now has [s]oraim, c[s]ak and másképe[n], in SOLUTION.md and in `work/normalized-rev2.txt`. The words themselves are unchanged.
