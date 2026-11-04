# HCP1214 — Feri's farewell to Jolánka Tóth

**Status: complete reading, small disclosed residual points; review 1 verdict REVISE, all findings addressed (see the end of this file).** Claude Opus 5.5, 2026-11-02.

Credit: decipherment and transcription by Claude Opus 5.5 from the pixels of this card. No earlier work exists on this number. The key is the shared Jolánka key from the finished sister cards (HCP1216, 1212, 1213, 1217, 1218, 1243, 1301). Portal status Not solved, no transcription or solution attached; no published solution of this card was found.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (MASC); accents as marks over the base sign. The key is transferred unchanged from HCP1216:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| long stroke + short tick on its left | d | two short strokes | n | plain heavy x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + tick on its right | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

In the ledger, `GY` is the joined gy sign (`G Y` on row 13 is the same digraph read as two parts), and `C )` is cs, written as two opposed bowls. Neither affects the plaintext.

The plain-language address reads: Szépreményű Tóth Jolánka kisasszonynak, Helyben ("To the promising Miss Jolánka Tóth, Local"). The picture side has only printed matter (no. 2541) and the collection stamp. The postmark date is not legible; the stamp is in place, and nothing shows under or around it.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1214/work/decode.py
```

It checks the SHA-256 of all four image files, decodes the manual sign ledger `work/ledger.txt` (18 rows) and prints `work/normalized.txt`. The ledger is a manual transcription, made knowing the sister key and with sense guiding the reading of the h/p signs; it is not OCR.

## Literal decipherment

```
01 kedvesjolanka            10 kerülnihafa{j}
02 marlatomközel             11 {d}alommegkel
03 alokahozhogy              12 tenemsziböl
04 kiutasitnakhazok          13 kivanomlegy{e}n
05 bolbocsasonmeg            14 boldogboldogit
06 nekemmerta[z]t            15 saazatud[a]thogy
07 önitudja{#}hogy           16 megtörtegy
08 mijnehezemre              17 szivetistenvele
09 esikbecsehazokot          18 voltkedvesseferi
```

## Hungarian (normalized)

Kedves Jolánka! Már látom, közel állok ahhoz, hogy kiutasít[a]nak házukból. Bocsásson meg nekem, mert azt Ön i[s] tudja, hogy mily nehezemre esik becse[s] házukat kerülni, ha, fájdalom, meg kell tennem. Szívből kívánom, legyen boldog, boldogítsa az a tudat, hogy megtört egy szívet. Isten vele! Volt kedvese, Feri.

## English

Dear Jolánka! I see now that I am close to being turned out of your family's house. Forgive me, for you too know how hard it is for me to keep away from your esteemed house when, alas, I must do so. I wish with all my heart that you be happy; may the knowledge that you have broken a heart make you happy. Farewell! Your former sweetheart, Feri.

## Slovak

Milá Jolánka! Už vidím, že som blízko k tomu, že ma vykážu z vášho domu. Odpusťte mi, lebo aj Vy viete, ako ťažko mi padne vyhýbať sa vášmu ctenému domu, keď to, žiaľ, musím urobiť. Zo srdca Vám želám, aby ste boli šťastná; nech Vás teší vedomie, že ste zlomili jedno srdce. S Bohom! Váš bývalý milý, Feri.

## Uncertainties

Calls that rest on word sense rather than on the sign shape:

1. **Row 10–11 "ha, fájdalom"** is the weakest point. The last sign of row 10 is an upright T with its bar on top, unique on this card and unlike both the inverted T j (rows 1, 7, 8) and the gamma t, whose bar runs only to the right. The first sign of row 11 is a stem with a tick on the right, the h/p shape, not the d shape. Reading j and d gives *fájdalom*, spelled out on HCP1216 as *fajdalmam*. Read strictly by shape the letters are *hafat halom*, which makes no sentence; *ha fáj, hallom* ("if it hurts, I hear") with a j is grammatical but pointless. So two signs here are read by sense. *fájdalom* is taken as the literary interjection "alas"; that use comes from language knowledge and was not checked against a period source. If it is the noun instead, the letters are unchanged and the clause is only looser.
2. **Row 10 "ha"**: under the two bars of the a, about twice the bar spacing lower, stands a third short stroke at the same x, which does not belong to row 11. The sign could be taken as an uneven three-bar e (*he fá...*), which gives no word. a is chosen by sense.
3. **Rows 3, 4, 8, 9, 15**: h vs p is chosen by word sense (*ahoz*, *hazok-*, *nehezemre*, *hogy*).
4. **Row 1 end**: the name is read *Jolánka*. Two strokes stand after the final a, but they lie low, directly over the o of *köz-* in row 2, and that o has no other marks; the row 12 ö carries the same pair of ticks. They are therefore the diaeresis of that ö, not a letter. The writer's *Jolánkám* on HCP1216 and HCP1217 is a comparison only and is not on this card.
5. **Row 6 *azt***: the z is under a heavy ink blot; only its crossed outline shows. Restoration; only z gives a word (*azt*). The a before it has its lower bar in the same blot.
6. **Row 15 *tudat***: the a is blotted, its top bar visible; restoration (same phrase on HCP1216).
7. **Row 7**: after *tudja* a thick diagonal stem is written through an 8-like form, and to its right stands one short notched stroke. The ledger gives `#` (no value) then `H`, but the heavy stem may itself be the h stem and the right stroke its tick, so the two tokens may be one corrected sign. Either way the word is *hogy*: the rest of it follows complete.
8. **Row 13 *legyen***: the last vowel touches the tail of the y and its bar count is unclear; e by sense. The second sign of *kívánom* is thick and z-like, but a separate dot stands over it, so it is read i.
9. **Writer's spellings normalized**: *i* → i[s] (s is not on the card), *becse* → becse[s] (likewise), *kiutasitnak* → kiutasít[a]nak, *házok-* → házuk- (*házokból, házokot*; literally the plural-looking dialect form; "their house" is an interpretation), *alok, ahoz, kel, tenem, bocsason* with single consonants, *mij* → mily, *szíböl* → szívből (v dropped), *kedvesse* → kedvese (two s signs clearly written). Accents are mostly not visible and are supplied.
10. Word division is editorial; *megtört egy* is written as one run of letters, with the *egy* at the row end joining *szívet*. The subject of *megtört* is read as you: the verb form itself is third-person ("that one broke a heart"), and my translation assumes the addressee.
11. Sender Feri is the signature here; identity with the Feri of HCP1212/1213/1216 is likely by key and addressee but is not proven. Date unknown.

## Why it is correct

- The unchanged family key turns all 18 rows into continuous Hungarian with no free key choice; only the points listed above needed sense.
- The text is coherent and specific: a break-up note, with *Ön* address as in the family, the *Isten vele* close, and the signature *Feri* appearing unprompted in the final signs.
- Repeated items decode identically: *hazok-* in rows 4 and 9, *boldog* twice, *hogy* in rows 3, 7, 15.

## Response to review 1

Verdict REVISE. I re-examined the reviewer's enlargements (`review/work/m5.png`, `umlauts.png`, `m3.png`) myself. Findings 1 to 6 are all accepted; none changes the key or the sense of the letter.

1. **Row 1 final m (major): fixed.** On `umlauts.png` the two strokes sit directly over the row 2 o and match the row 12 ö pair, and that o has no other marks. `M?` removed from row 1 of `work/ledger.txt` and from the decoder; the salutation is now *Kedves Jolánka!* in the literal block and `work/normalized.txt`. Uncertainty 4 rewritten.
2. **"ha fájdalom" (minor): adopted.** The sentence now runs over the row break as *kerülni, ha, fájdalom, meg kell tennem*, "when, alas, I must do so"; Hungarian, English and Slovak changed. The disclosure of the two sense-based signs stays, and the interjection sense is marked as unchecked against a period source. The h/p shape of the row 11 first sign is now stated plainly.
3. **Third stroke under row 10 a (minor): disclosed** as uncertainty 2. I see the stroke on `m5.png`; the reading does not change.
4. **Row 7 overwritten sign (minor): disclosed** in uncertainty 7. The ledger tokens stay as they are, with the possibility that they are one corrected sign stated there; the word is *hogy* either way.
5. **Row 14 second d (minor): fixed.** On `m3.png` it has its tick on the left, like the first d of the row. `D!` removed from row 14 and the old uncertainty 2 deleted; the h/p-shaped d remains only on row 11. The key table now states which side the tick is on, since the family distinguishes them that way.
6. **Key table against tokens (minor): fixed.** gy and cs added to the table, and a note explains `GY`, `G Y` and `C )`. The ledger header says the same.

Re-run after the fixes: `python3 -I ciphers/hcp-1214/work/decode.py` passes all four hashes and prints the block above (233 ledger tokens, 18 rows). The changes are one dropped letter, one flag removed, and punctuation and translation of one clause, so the reading is not substantially changed and no second review round is needed.

## Stamp-box audit (2026-11-03)

Checked by Claude Opus 5.5 on the original `work/hires/..._adr.jpg` (crops at 2x to 5x, red channel and blue-minus-red separations in `work/stamp-2026-11-03/`). The green 5 fillér Turul stamp is **still in place**, not lifted. It is torn and thinned right of the crown (a hole about 1 x 1 cm); through and at the edge of that hole a curved bluish stroke and a short hooked bluish stroke are visible (`tear_5x.png`, `thinned_rgb_4x.png`). They are too small to identify: they may be part of a second cancellation or printed card matter, or the edge of writing under the stamp. No letter or cipher sign can be read from them, and the rest of the box is covered. The dark marks over the stamp left of the crown match the black postmark ink and are not writing.

**Result: stamp in place; any hidden message is unknowable from this scan. No stamp-box message is added. Type stays MASC** (2026-11-03: not changed to MASC + Steganography, because no writing under the stamp can be shown). If the card is ever examined with the stamp lifted, this should be revisited.
