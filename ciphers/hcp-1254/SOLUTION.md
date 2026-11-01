# HCP1254 — to Jolánka Tóth: "I arrived safely", Jászárokszállás, March 1912

**Status: PARTIAL as a card. The whole enciphered message (15 rows) is read, with the small residual points listed below, but four lines of the separate unenciphered note under the stamp are rubbed out and unread (Uncertainties, item 1). Review 1 verdict ACCEPT. No register entry is written; see Response to review 1, finding 1.**

Credit: transcription and decipherment by Claude Opus 5.5, 2026-11-01. There is no earlier work on this number. The key was not recovered here: it was transferred from the finished Jolánka cards, chiefly HCP1216. The portal shows status Not solved and attaches no transcription or solution. I found no published solution, but I ran no separate web search; the orchestrator's AI-register check of 2026-11-01 has no record of this card.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (the Jolánka postcard family). The key is the HCP1216 key, unchanged:

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S, usually with a dot below) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c (not on this card) | three short strokes | m | gamma/corner | t |
| short stroke + long stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f (not on this card) | tall stroke + short stroke | h / p | low descender | y (not on this card) |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

Digraph sz is written right bowl + crossed diagonal. Acute accents are ticks and dots near the sign, and they are supplied in normalization. A double mark over the loop gives ö/ő.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1254/work/decode_opus.py
```

It checks the SHA-256 of the four captured images, decodes the sign ledger `work/ledger-opus.txt` with the key, prints the literal rows, and prints the normalized text `work/normalized-opus.txt`. The ledger is a manual transcription from enlarged crops (`work/crops/`). It is not OCR and it is not blind: the key was known, and word sense guided the calls listed below.

## Literal decipherment (as printed by the command)

```
01 kedvesjolankam
02 tudatomhogysze
03 rencsesenmeger
04 keztemigaz{+}hogy
05 egykicsszaladni
06 kelletdeazert
07 aboldogsagert
08 sokkalnagyobb
09 [deleted]aldozatokra
10 iskepeslannek
11 istenveleedesem
12 gondoljonneh
13 remkiönttisz
14 taszivebolimad
15 {j?}aatavolbol
```

## Hungarian (normalized; [ ] = supplied or corrected letter)

Kedves Jolánkám! Tudatom, hogy szerencsésen megérkeztem; igaz, hogy egy kics[it] szaladni kellett, de azért a boldogságért sokkal nagyobb áldozatokra is képes l[e]nnék. Isten vele, édesem! Gondoljon néh[a] r[á]m, ki Önt tiszta szívéből imádja a távolból.

Unenciphered, under the stamp: Csókolom [four lines rubbed out] számtalanszor, édesem.

## English

My dear Jolánka! I inform you that I arrived safely; true, I had to run a little, but for that happiness I would be capable of far greater sacrifices too. Farewell, my sweet! Think of me sometimes, who adores you with a pure heart from afar.

Under the stamp: I kiss [... rubbed out ...] countless times, my sweet.

## Slovak

Moja milá Jolánka! Oznamujem Vám, že som šťastne dorazil; pravda, musel som trochu bežať, ale pre to šťastie by som bol schopný aj oveľa väčších obetí. Zbohom, moja milá! Myslite niekedy na mňa, ktorý Vás čistým srdcom zbožňuje z diaľky.

Pod známkou: Bozkávam [... zotreté ...] nespočetnekrát, moja milá.

## Uncertainties

1. **Note under the stamp (unenciphered, not fully read).** The first line *csókolom* and the last three *számta / lanszor / édesem* are legible. Between them four lines were rubbed out while the ink was wet, and they sit under the printed wreath. Green-channel and sharpened crops (`work/crops/stamp_g.png`, `stamp_us.png`) give only the line ends -d, -on, -is and -at. I do not restore these lines. The blot on the first letters of *édesem* also makes that word a reading from shape and sense. The lost text is plain writing, not cipher, and the surviving frame looks like a closing kiss formula, but its content is unknown. The reviewer should judge whether this gap is acceptable.
2. **Row 4, the sign between *igaz* and *hogy*.** A small cross-like sign, close to the f sign but lighter. At 3x its bar runs up to the head of the tall stroke of the h of *hogy*, so it may be a false start of that h, or a slip or a punctuation mark. *igazf* is no word, so it is left without a letter value (`{+}`). The normalized text ignores it.
3. **Row 5, *kics*.** The signs are plainly i + opposed bowls, followed directly by s-z of *szaladni*. Normalized as *kics[it]*, an abbreviated or slipped word. *egy kis szaladni* ("a bit of running") would mean the same but does not match the opposed-bowls sign, which also stands for cs in row 3 (*szerencsésen*).
4. **Row 9, deleted word.** The writer scored through about four signs before *áldozatokra*. They are not read and are not part of the text.
5. **Row 10, *lannék*.** The sign after l is clearly two bars (a); normalized to *lennék* as a slip. A small dot of ink sits in the wave sign and is taken as a stray mark.
6. **Row 12, *néh*.** The row ends in the h sign and no a is written, here or at the start of row 13; *néh[a]* supplies a letter that was never written (not a hidden sign). The same phrase *gondoljon néha rám* occurs on HCP1217.
7. **Row 13, *rám*.** The middle sign is e: its third bar is short, like the short third bar of ordinary e in row 1, and accents in this hand go above a sign, not below. The literal is therefore *rem*, normalized *r[á]m* as a writer's slip, by sense.
8. **Row 15, first sign (j of *imádja*).** A heavy overwritten sign with crossing strokes; its shape does not establish j. j is a call from word sense alone: *imád* + ? + a. The following two two-bar signs give *a a*, read *imádja a távolból*. The second carries a small tick that the article *a* does not need; it is a stray or misplaced mark, perhaps meant for the *á* of *imádja*.
9. **Rewritten signs read through.** Row 2: the o of *tudatom* is overwritten, with a trailing stroke, and the h of *hogy* has a blotted short stroke. Row 12: the two n of *gondoljon néha* are heavy overwritten strokes, each followed by a clean stroke. These calls rest partly on sense.
10. **h/p.** *képes* (row 10) and the h of rows 2, 4, 12 use near-homographs, separated by word sense only.
11. **Accents.** All acutes in the normalized text are editorial; only the double mark on *Önt* (seen above the row 13 sign) is recorded in the ledger.
12. **Sender and date.** The card is unsigned in the legible text. The sender is unknown, so the masculine Slovak forms assume a male writer, as on the family's other cards; family cards to this addressee are signed Feri, which is context and not a reading of this card. The date 1912-03-27 is the portal file name. The Jászárokszállás cancel, turned 180°, shows `91`, a damaged digit space, MÁR and day digits beginning with 2 and compatible with 27, partly under the ink: year 1912 and March are supported by the card, the exact day is not confirmed. A second partial cancel beside the stamp is unread.
13. **Picture side.** A tinted photograph with a printed Hungarian verse; no handwriting and no cipher.

## Why it is correct

- The key was transferred unchanged from finished sister cards and gives continuous Hungarian across all 15 rows. Only the sign in item 2 has no value. The sign in item 8 rests on sense alone, and the written *rem* (item 7) and *lannék* (item 5) are normalized by sense as slips.
- The recipient (address in clear: *Szépreményű Tóth Jolánka úrleánykának, Jászárokszállás*) matches the family. So do the formal *Ön* address, *Isten vele, édesem* and *gondoljon néha rám*, which recur on HCP1217 and HCP1216.
- Repeated signs behave consistently: the words *hogy* ×2, *-ért* ×2 and *-ból/-ből* ×2 decode identically, and the unusual *Önt* carries a visible double mark.
- The text is idiomatic and specific, not a set of isolated words: a short arrival note ending in a declaration.

## Response to review 1

Verdict ACCEPT, seven minor findings. I checked findings 2, 3, 5 and 6 on the reviewer's crops (`review/work/z_r13.png`, `z_r04end.png`, `z_r15.png`, `pm1.png`) and the picture side on `source/picture-large.jpg`; I agree with all of them.

1. **Lost plain lines and the register. Decided: partial, no entry.** No more text could be recovered; the reviewer's green and blue channels confirm that. The reviewer left the call to the human. The batch rule says a whole unread clause is partial, and four lost lines are more than a clause. The rule speaks of the card, and the same-batch cards HCP1272 and HCP1280 were treated as partial for a smaller loss in the plain note. So `register-entry.txt` is not written. The cipher text alone is complete, so a human may decide otherwise.
2. **Row 13: fixed.** The sign is e. Ledger token changed from `E?` to `E`, the unused key entry removed from `work/decode_opus.py`, literal now *rem*, normalized *r[á]m* in `work/normalized-opus.txt` and above; Uncertainties item 7 and "Why it is correct" updated.
3. **Row 4 cross: fixed.** "Joined to nothing" removed; a possible false start of the h is stated in item 2. The text is unaffected.
4. **-ból/-ből: fixed.** ×2, not ×3.
5. **Postmark: fixed.** Item 12 now states what the cancel shows, and the second, unread cancel.
6. **Tick in row 15: fixed.** Noted in item 8 as a stray or misplaced mark.
7. **Sender and picture side: fixed.** Items 12 and 13.

Re-run after the edits: all four SHA-256 checks print OK and the output matches the literal and normalized text above. The only changed decoded character is row 13, *{e|a}* to *e*, which leaves the reading unchanged. 194 ledger tokens.
