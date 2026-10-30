# HCP1212 – Feri to Jolánka: love verse and a dinner (17 Feb 1912)

**Status: complete decipherment of all cipher text on the card, with small disclosed residual points. Review 1: ACCEPT; minor findings addressed below.**
Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1212 (status *Not solved* when captured, no transcription or solution attached). No published solution of this card was found (see NOTES.md; orchestrator AI-register check 2026-10-29: no record).

## Credit

- Setup, source capture, the key transfer from the sister cards HCP1301/HCP1243 and passes 1–5 of the reading (main text, verse, dinner clause, sign-off): OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-12/13.
- Pass 6 (2026-10-30, Claude Opus 5.5): re-checked every row on enlarged crops, corrected three rows of the ledger (rows 12, 14, 17), flagged a possible doubled t in row 4, and read the small address-side cipher annotation (N01), which had been left unresolved. New ledger `work/as-seen-pass6.txt`, new decoder `work/decode.py`.

## Cipher type and key

Hungarian **graphic monoalphabetic substitution** (one sign per letter, word spaces mostly kept, accents written as marks over the cipher signs). It is the same key as the other Tóth Jolánka cards from Feri (HCP1213, 1216, 1217, 1218, 1243, 1301).

| Sign | Letter | Sign | Letter |
|---|---|---|---|
| two bars `=` | a | wave `~` | l |
| six-like loop `6` | b | three short strokes `III` | m |
| left bowl `(` | c | two short strokes `II` | n |
| short + long stroke | d | cursive loop | o |
| three bars `≡` | e | tall + short stroke | p |
| upright cross `+` | f | F-like sign | r |
| open loop with descender | g | right bowl `)` | s |
| two tall strokes | h | corner / gamma `Γ` | t |
| dotted crossed curve | i | x | u |
| inverted T `⊥` | j | chevron `ʌ` | v |
| section-like sign `§` | k | low descender | y |
| crossed diagonal | z | | |

Accents: acute / diaeresis marks above the sign (á é í ó ö ő ú ü ű). Digraphs are spelt with two signs (gy = g+y, cs = c+s, sz = s+z, ly not used – the writer writes j). h and p are near-homographs at this scan resolution; d and n differ mainly by stroke length.

## Reproduction (one command, from the repo root)

```sh
python3 -I ciphers/hcp-1212/work/decode.py
```

It verifies the SHA-256 of `source/address.jpg` and `source/picture.jpg`, then decodes every row of the manual token ledger `work/as-seen-pass6.txt` (17 main rows + annotation N01). Output (also in `work/pass6-decoded.txt`):

```
01: édesjolánkámbecses
02: soraitkösönettelmeg
03: kaptammelyekörömemre
04: szolgaltakésazala{t?}ti
05: sorokbanvalaszolok.
06: kivelbizonyitsam,
07: hogytegedszeretlek
08: tanum,kialkotéanagy
09: mindenséget.
10: hogycsakértedélek
11: sértedszenvedek,
12: ésmindenneleföldön
13: jobbanszeretlek.
14: avacsoraélégkedéjes
15: volt,éshogymitadvissza
16: aztnemértem,istenvele
17: aviszontlatasraszeretetelferi
N01: {s?}ze{r?}etetel
```

The ledger was entered by hand from the scan (not OCR, not blind: earlier readings were known). The script does not read pixels.

## Hungarian text (editorial: spaces, punctuation, missing accents and `[ ]` restorations added)

Édes Jolánkám! Becses sorait kös[z]önettel megkaptam, melyek örömemre [szolgáltak], és az alatti sorokban válaszolok.

> Kivel bizonyítsam,
> hogy téged szeretlek?
> Tanúm, ki alkoté a nagy
> mindenséget.
> Hogy csak érted élek,
> s érted szenvedek,
> és mindennél e földön
> jobban szeretlek.

A vacsora elég kedélyes volt, és hogy mit ad vissza, azt nem értem. Isten vele! A viszontlátásra szeretet[t]el Feri.

Address-side annotation (right of “kisasszonynak”): probably szeretet[t]el (literal `{s?}ze{r?}etetel`; signs 1 and 4 uncertain, see uncertainty 1).

## English translation

My sweet Jolánka! I received your dear lines with thanks; they gave me joy, and I answer in the lines below.

> By whom shall I prove
> that I love you?
> My witness is He who created the great
> universe.
> That I live only for you
> and suffer for you,
> and love you more
> than anything on this earth.

The dinner was quite pleasant, and as for what it/he gives back, I do not understand that. Farewell! Until we meet again, with love, Feri.

Annotation by the address: (probably) with love.

## Slovak translation

Moja milá Jolánka! S vďakou som dostal Vaše vzácne riadky, ktoré ma potešili, a v nasledujúcich riadkoch odpovedám.

> Kým mám dokázať,
> že ťa ľúbim?
> Mojím svedkom je ten, kto stvoril veľký
> vesmír.
> Že len pre teba žijem
> a pre teba trpím,
> a viac než čokoľvek na tejto zemi
> ťa ľúbim.

Večera bola dosť príjemná, a čo vracia, tomu nerozumiem. S Bohom! Do videnia, s láskou Feri.

Poznámka pri adrese: (pravdepodobne) s láskou.

## Uncertainties and source spellings (all disclosed)

1. **N01 annotation** (≈10 cramped signs under the grey portal watermark): signs 2–3 and 5–10 read clearly as z e … e t e t e l (corner+bars groups identical to the sign-off). Sign 1 is a straight hooked stroke, read as s (right bowl) by its position; sign 4 is an M-shaped cramped sign in the r position, not a clear F. The word is read as **szeretet[t]el** because the same writer spells the same word *szeretetel* in the sign-off (row 17) and on sister card HCP1218 (accepted reading “szeretet[t]el”). Literal `{s?}ze{r?}etetel` is kept in the decoder output.
2. **Row 4 alat{t?}ti**: a small corner-like stroke is squeezed in before the final t; it may be a second t (alatti, standard) or a start stroke of the same t. Either way the word is alat(t)i “below”.
3. **Row 3** the sign read as p (kaptam) and rows 7/10/15 h (hogy) rest on the h/p shape distinction plus language; both are unambiguous in context.
4. **Row 4 szolgaltak**, **row 5 valaszolok**, **row 17 viszontlatasra**, **row 12 mindennel** (three equal bars, no separate accent tick): accents not written; added editorially (mindennél).
5. **Source spellings kept literally, normalised in the edition**: *kösönettel* (köszönettel), *élég* (elég), *kedéjes* (kedélyes – ly written as j, as pronounced), *szeretetel* (szeretettel), *tanum* (tanúm), *alkoté* (alkotá / alkotta, archaic past – kept as written). *Kivel* (“by whom”) is kept; *mivel* (“with what”) would be the more expected wording, but the following lines name a witness, so kivel makes sense.
6. **Row 15 “mit ad vissza”**: the letters are clear; the card does not say who/what gives back what (presumably a reference to Jolánka’s letter), so the translation does not invent an object.
7. Accents over both a of Jolánkám (row 1) are visible and recorded in the ledger since review 1; other faint or missing accents (e.g. row 14 kedélyes) are supplied in the edition.
8. Plain-hand texts on the card are **not** cipher: the stamp-corner note, written in five short lines *számta / lanszor / csókol / szeretet / tel Feri* = “számtalanszor csókol szeretettel Feri” (“kisses you countless times, with love, Feri”; corrected after review 1 – note the plain-hand *szeretettel* with tt), the address “Szépreményű Tóth Jolánka kisasszonynak, Jász-Árokszállás” and the line above the postmark, probably “Egy kis nefelejcsnek” (“To a little forget-me-not”). They are not part of the decipherment.
9. Transcription was not blind: earlier GPT readings were known; every row was nevertheless checked on 4–10× crops in pass 6, which is how the corrections in rows 12, 14, 17 were found.

## Why the solution is believed correct

- The key is the established Jolánka/Feri key from accepted sister cards (HCP1213, 1218, 1243, 1301); no sign on this card needs a new value.
- The whole main text (17 rows, ≈330 signs) decodes with this key to fluent, grammatical early-20th-century Hungarian with only typical phonetic misspellings (kedéjes, kösönettel, szeretetel) of the same writer.
- The eight-line verse is metrically and grammatically coherent (rhyme szeretlek / szenvedek / szeretlek), the letter formula (Becses sorait köszönettel megkaptam … Isten vele … A viszontlátásra) matches Hungarian letter conventions of 1912, and the signature Feri matches the sister cards addressed to Tóth Jolánka in Jászárokszállás.
- The pass-6 corrections replaced non-words of the old ledger (mindenemél, szeretel) with real words read directly from the signs (mindennél, szeretetel), which is further evidence that the key is right and the ledger now matches the pixels.
- No published poem was found for the verse (GPT web search, NOTES.md); nothing was imported from outside.

## Response to review 1

Verdict ACCEPT, five minor findings. All were checked on the reviewer's enlargements (`review/work/*.png`) and on the scan; all are accepted. Ledger before the fix kept as `work/as-seen-pass6-before-review1.txt`; `python3 -I ciphers/hcp-1212/work/decode.py` re-run, hashes OK, output above and in `work/pass6-decoded.txt` updated.

1. **Row 12 `a földön` → `e földön` – fixed.** On `review/work/r12-efoldon.png` the sign before the upright cross has three bars of equal length (e), unlike the two-bar a. Ledger token changed A → E; edition now *és mindennél e földön*, translations "on this earth" / "na tejto zemi". Meaning unchanged.
2. **Row 12 no visible accent on `mindennél` – fixed.** `review/work/r12b.png` shows three plain bars after the two n's, no separate tick. Ledger token E:acute → E (literal `mindennel`); the accent is now listed as editorial in uncertainty 4.
3. **N01 qualification – fixed.** The edition line and both translations now mark the annotation as probable (signs 1 and 4 uncertain).
4. **Stamp-corner plain-hand note – fixed.** Rechecked on `review/work/topright.png`: five lines *számta / lanszor / csókol / szeretet / tel Feri* = "számtalanszor csókol szeretettel Feri". The line above the postmark reads (probably) "Egy kis nefelejcsnek". Uncertainty 8 corrected. The plain-hand *szeretettel* supports the restoration szeretet[t]el in row 17 and N01.
5. **Row 1 accents – fixed.** `review/work/band0.png` shows ticks over both two-bar signs of Jolánkám; recorded as A:acute in the ledger.

No change to the reading beyond `a` → `e` in row 12; the solution is otherwise unchanged.
