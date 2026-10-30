# HCP1469 – Reg to Gertrude Forrest, London → Bristol, 11 Nov 1907 (complete reading)

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1469 (`pc_hcp_150`). Status on the
portal when captured (2026-10-26): *Not solved*; no transcription or solution attached.
The transcription is the solver's own (`work/transcription.txt`), made from
`source/address-large.jpg` (1024 × 674 px, the only resolution available in `source/`).
No published solution of this card was found or used (orchestrator AI-register check
2026-10-29: no record).

## Credit

- Source capture and first triage (no key, no reading): OpenAI GPT solver, 2026-10-26.
- Cipher identification, key, transcription and complete reading: Claude Opus 5.5, 2026-10-30.

## Cipher type and key

English, **monoalphabetic substitution with invented signs**, in which four letters are written
as dot patterns and the rest as simple strokes. Word spaces are mostly kept. No sister card in the
repo uses this alphabet.

| Letter | Sign | Code | Letter | Sign | Code |
|---|---|---|---|---|---|
| a | circle `O` | O | n | caret `∧` | V |
| b | three-shape `3` | 3 | o | circle with bar `θ` | Q |
| c | rounded arch `∩` | C | p | bracket `⊐` with top bar | P |
| d | right bowl `ↄ` / `)` | ) | q | circle with centre dot `⊙` | X |
| e | **one dot** | . | r | seven-shape `7` | 7 |
| f | gamma corner `Γ` | F | s | two-shape `2` | 2 |
| g | **two dots falling** (high-left, low-right) | G | t | inverted T `⊥` | T |
| h | **two dots rising** (low-left, high-right) | H | u | T on its side `⊢` | U |
| i | **two dots vertical** `:` | : | v | angle `>` | > |
| j | hook `⅃` | J | w | caret `∧` (same sign as n) | V=w |
| k | angle `<` / `ʞ` | K | y | caret with central stem `↑` | Y |
| l | box `□` (sometimes with a divider, `◫`) | L | m | left bowl / bar `(` | M |

Not attested: x, z. The caret `∧` is used for both **n** and **w**; I could not find a consistent
shape difference at this resolution (tall and low carets occur for both).

## Plaintext (English; line labels as in the transcription)

Body (left panel, below the date `11.11.07`):

```text
B01 my own dearest girlie it is now almost
B02 half past five and i shall soon
B03 be clearing out and shall
B04 not be sorry either i was
B05 dredful glad to get your
B06 letter this morning it came
B07 in time for me to read it at
B08 breakfast time it was quite
B09 foggy this morning and
B10 train was a bit late every
B11 time we have fog signals now
B12 makes me think of our journeys
B13 up together the fog cleared
```

Continuation in the top margin (lines T1–T7, written above and beside "POST CARD"):

```text
T1 a good bit and it has been a fairly decent day
T2 goodbye for the present only four days now to wait
T3 i hope i have a
T4 letter from home tonight
T5 reg sends you dredful lots
T6 of love and is always your
T7 own boy reg
```

Punctuated: “My own dearest girlie, it is now almost half past five and I shall soon be
clearing out, and shall not be sorry either. I was dreadful glad to get your letter this morning;
it came in time for me to read it at breakfast time. It was quite foggy this morning and [the]
train was a bit late. Every time we have fog signals now [it] makes me think of our journeys up
together. The fog cleared a good bit and it has been a fairly decent day. Goodbye for the present,
only four days now to wait. I hope I have a letter from home tonight. Reg sends you dreadful lots
of love and is always your own boy, Reg.”

Slovak: „Moje najdrahšie dievčatko, je skoro pol šiestej a čoskoro sa odtiaľto poberiem, a ani mi
nebude ľúto. Strašne som sa potešil tvojmu listu dnes ráno; prišiel včas, aby som si ho prečítal
pri raňajkách. Ráno bola dosť hmla a vlak trochu meškal. Zakaždým, keď teraz počujeme hmlové
signály, spomeniem si na naše spoločné cesty hore [do mesta]. Hmla sa poriadne rozplynula a bol to
celkom slušný deň. Zatiaľ zbohom, už len štyri dni čakania. Dúfam, že dnes večer budem mať list
z domu. Reg ti posiela strašne veľa lásky a je navždy tvoj chlapec, Reg.“

## Reproduce (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1469/work/decode.py
```

It checks the SHA-256 of the three files in `source/` against `work/source-sha256.json`, then
decodes every line of the manual sign transcription `work/transcription.txt` with the key above
and prints the plaintext line by line and as one string (saved output: `work/decoded.txt`).
The pixel-to-sign step is manual; the script does not OCR the scan.

## Uncertainties and editorial decisions

1. **n / w share one sign.** The caret `∧` stands for n in most places and for w in *own, now,
   was, we, wait, always*. Where w is meant is decided by context and marked `V=w` in the
   transcription. Every such word has only one sensible reading.
2. **“dredful” (twice, B05 and T5).** Both times the word is written d-`∧`-e-d-f-u-l, the caret
   standing where r is expected. Read as *dredful* = colloquial *dreadful* (“dreadful glad”,
   “dreadful lots of love”); the decoder prints this letter as upper-case `R` to flag it. Because
   it is spelt the same way twice, this is most likely the writer's own slip or habit, not a
   transcription error.
3. **Dot letters.** e, g, h and i are written only as dots, which are small and sometimes faint
   at 1024 px. Each group was checked on enlarged crops (`work/crops/z1.png`, `z2.png`, `z11.png`,
   `v1.png`–`v5.png`, `T4c.png`, `T7b.png` etc.), and for line B01 also by a connected-component
   listing of the dots. In *together* (B13) the e's are faint third dots (`z11.png`). The
   orientation of the two-dot signs (vertical i, falling g, rising h) is sometimes only a few
   pixels. Everywhere the reading gives the only English word, but a higher-resolution scan
   would settle the faint dots better.
4. **Glyph variants.** l is drawn as a plain box or a box with a divider (both in *shall*); k as
   `<` (*makes*) or `ʞ` with a stem (*breakfast, think*); t sometimes with a hooked foot; the s in
   *is* (T6) has an extra lead-in stroke. None of these changes the reading.
5. **Printed crest and a blotted sign in T2.** The printed crown crest of “The Wellington Series”
   lies under the word *only* in T2 (its y-sign touches the crown), not under *now*. The w of
   *now* further right is a dark, blotted caret over the grey watermark band; its caret outline
   and the context (*four days now to wait*) agree. (Corrected after review 1, finding 2.)
6. **Order of the margin text.** The body ends at the bottom of the panel with “the fog cleared”;
   the text then continues in the top margin (T1 “a good bit …”) down to the signature. This
   order is the only one that gives continuous sentences. NOTES' earlier triage mentioned an
   “inverted continuation”; there is none – all text is written upright.
7. **Sender and words left out.** The writer signs himself *Reg* (also in the third person, “Reg
   sends you …”). The missing words “the” (before *train*) and “it” (before *makes*) are not on
   the card and are added only in the punctuated version, in brackets.

## Why I believe it is correct

- Every sign on the card is used; the whole text (body + margin: 20 lines, 120 words, 456 sign
  tokens, counted by the decoder's STATS line) decodes to continuous, grammatical English of a
  1907 love letter, without gaps or unknown signs.
- The key was found statistically, not by guessing: an English quadgram hill-climb on a rough
  first transcription in which dot groups were counted (1 dot vs 2 dots) produced readable English
  (“my own dearest … your letter this morning came in time for me to read it at breakfast …”)
  straight away; the transcription was then redone on enlarged crops. That first transcription
  and the quadgram model were scratch files and were not kept, so this discovery step is **not
  reproducible** from the repository. The reading does not depend on it: the kept transcription
  and key are checked by the decoder and give 120 coherent English words.
- The content fits the card: written in London on 11.11.07 (London postmark, day and year legible as 11 … 07), sent to
  Miss Gertrude Forrest at Westbury-on-Trym, Bristol; fog in London in November; “only four
  days now to wait” before seeing her.
- The key is consistent: the same sign always gives the same letter, apart from the disclosed
  n/w sign and the two “dredful” spellings.

## Response to review 1

Review 1 (Claude Opus 5.5, separate session) gave the verdict **ACCEPT** with four minor findings.
No sign, key entry or plaintext word was changed.

1. **Sign count overstated – fixed.** `work/decode.py` now prints a `STATS` line; re-run
   (`python3 -I ciphers/hcp-1469/work/decode.py`) gives `20 lines, 120 words, 456 sign tokens,
   unknown=0, caret read as w=11, caret read as r=2`, matching the reviewer's independent count.
   “About 500 signs” above is replaced by these numbers. Apart from the added STATS line the
   output is identical to the previous `work/decoded.txt` (checked with diff), which was
   regenerated.
2. **Over-printed word described wrongly – agreed and fixed.** On the reviewer's crops
   `review/work/t2m.png` (crown crest under *only*, the y-sign of *only* touching it) and
   `review/work/now_T2.png` (the w of *now* is a dark blotted caret over the grey band) the
   reviewer is right. Uncertainty 5 is rewritten; the reading *now* is unchanged.
3. **Key-discovery step not reproducible – agreed.** The rough first transcription and the
   quadgram model were scratch files and are gone. SOLUTION.md (and the report) now say plainly
   that this step is not reproducible and that the reading rests on the kept transcription and
   key, not on that step.
4. **n/w ambiguity only partly tested – noted.** I re-looked at carets for n and w on the same
   crops (e.g. *own* B01 and T7, *now* B01/B11/T2, *and* B02/B03, *in* B07): no stable size or
   shape difference at 1024 px, the same result as the reviewer's. All eleven w readings (own ×2,
   now ×3, was ×3, we, wait, always) are forced by context; the report says this was checked.
