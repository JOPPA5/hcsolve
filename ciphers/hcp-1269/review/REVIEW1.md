REVISE

# HCP1269, review round 1 (Claude Opus 5.5, reviewer, 2026-11-01)

The solution stands: right key, right language, right sense of the card from start to finish. But the ledger has six concrete sign errors, and two of them are presented in SOLUTION.md as a "correction" and as writer's spelling. One of these (row 23) is a major misreading of a clause that is actually plain. The ledger must be corrected before FINAL. No re-review is needed if only these fixes are made and no further reading changes.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1269/work/decode_opus.py`: all four SHA-256 checks OK; the output equals the literal block in SOLUTION.md row for row (row 27 differs only by how `{?}` is written).
- Wrote my own decoder with a separately typed key, `review/work/verify.py`: 38 rows, 781 ledger signs, 2 unknown tokens (row 27 blot, stamp row 3). Same literal text. It also applies my corrections below.
- Key: table agrees with the HCP1216 family as stated. No sign is left outside the key, apart from the two disclosed unknown tokens.
- Transcription: my own crops of `work/hires/*_adr.jpg` in `review/work/` (L0–L4, R0–R4, b1–b4, edge, stamp, z*.png, 2–6x). I read rows 1–13 and 26–32 and the stamp sign by sign against the ledger; rows 14–25 were checked at 2.4x, with zooms only on the signs named below.
- Language: connected, idiomatic period Hungarian love-letter prose in the *Ön* form. Formulas and names fit the Feri/Jolánka family (*ha feljön* on HCP1213, 1247, 1311; *feljönne* on 1276; *Pestre* on 1217, 1246, 1267, 1305). No sign of forcing onto noise.
- No published solution: portal status Not solved per `source/metadata.md`; nothing in the files suggests outside use. I did not consult the HistoCrypt article either.

## Findings

1. **major: row 23 is misread; the text is *ha fel-jön*, not `a h e z a l jönek`.** Crop `review/work/z23.png`. After *róla* the signs are: h/p sign, two bars with a hook (a), an upright cross with short arms (+ = f, like *Feri* on the stamp, not the long-barred z of row 15 in `z15.png`), three strokes (e), wave (l). Literal `rolahafeljönek hest|re`: *róla, ha feljön(ne/k) Pestre*, "if you come up to Pest". This is the family's standing phrase (HCP1311 *ha feljön Pestre*). The ledger's `H E Z A L` and uncertainty 4's "*el* is a correction" and "*hez* or *ha ez* is not settled" should go. Normalize *feljön(ne)* and translate "come up to Pest"; the verb ending `jönek` stays a disclosed oddity.
2. **minor: row 30 `vanek k-` is `vanak`, with one k only.** Crop `z30vanek.png` shows: wave-less chevron v, two bars, n, **two bars**, one section mark, then the loop with ticks over it, z, t. The ledger's `V A N E K K O Z T` has a wrong E and a K that is not on the card. Literal `vanakőztünk`: *vanak* + *[k]öztünk*, one k doing duty for both words (or a dropped k). The "ö/ő" over the loop is also visible and is unrecorded in the ledger. Item 11 "*vanek* → vannak" is therefore not the writer's spelling. Text unchanged, *vannak köztünk*, but say that a k is restored.
3. **minor: row 28 *már* is spelled correctly.** Crop `z28mer.png`: the sign is two bars plus an acute tick, i.e. á, not e. Ledger `M E F` should be `M A F`; remove "*mer* → már" from item 11. Compare the three-bar e with tick in row 6 (*téved*).
4. **minor: row 15 has no e between z and n.** Crop `z15.png`: `) z n e k`. The ledger inserts an E; the writer wrote *egésznek* correctly. Remove from item 11.
5. **minor: stamp row 5 has five signs, the ledger four.** Crop `stamp.png`, `zS5.png`: chevron, bars, right bowl, right bowl, bars, literal `vesse` (*kedvesse* for *kedvese*). One sign is omitted, and "every sign" in the "Why it is correct" section is not literally true until it is added. Disclose it as a doubled s, or a slip.
6. **minor: row 32 cross is z, not `{z|f}`.** Crop `z32cross.png` matches the row-15 z of `z15.png` stroke for stroke (hooked left arm, stem, long rising bar) and differs from the f of the stamp and of row 23. The open word is then `…tehate lez`, ending in z. This narrows item 1 and gives some weight to *…tételez* with a false start or slip, but the word stays unread. Leave as disclosed; state the sign as z. I have no better reading.
7. **minor: row 30 `i` in *ha i két…*.** Item 3 says "no visible dot". A separate dot stands right above the sign (`z30iB.png`), at the foot of the m of row 29, at normal dot distance; it is not a stroke of the m. So i is supported. The small word remains unexplained and the *két[ke]dések* restoration remains a guess, which is correctly disclosed. The dot deserves a mention.
8. **minor: the plain word above the address is *Szépreményű*, not a name.** Crop `plain.png`: S-z-e-p (long descender) r-e-m-é-n-y-ü. It is a courtesy epithet before *Tóth Jolánka úrleánynak*, and the same word occurs on other family cards (for example HCP1212, 1244, 1245). Item 13 "Szemerényi or similar" should be corrected.
9. **minor: small ledger and claim slips.**
   - Rows 5 (*köszönő-*) and 20 (*lő-*) have two ticks, not dots, over the o (`L0.png`, `L3.png`). No effect on the text.
   - Row 18 has a written point after *ra*, omitted from the ledger, though the header says a written point is a token.
   - "*édesem* 6 times" is 5 in the literal text; `becses` occurs once in full (`verify.py`) and row 3 only as `b.`, so neither supports "decode identically" as stated. *hogy* (11) is correct.
10. **minor: the ledger records values, not shapes, as SOLUTION.md itself says.** That is the likely cause of findings 1–5: the transcription is steered by the expected word. Findings 2–4 went the other way, though, so the errors are not forced fits of a wanted reading. After the fixes, recheck the e/a calls of rows 14–25, which I did not zoom on, especially row 17 `emerek` (*érek*) and row 28 end `idegenen`, where the penultimate vowel in `z28end.png` is two bars, as item 2 suspects: write A in the ledger.

## Restorations checked

- Row 27 blot after *ha o*: dark stain, no readable sign; *ot[t]* is disclosed as restoration. Fair.
- Stamp row 3, sign under the triangle: not legible as l or s; disclosed. Fair.
- Row 1 overwritten third sign, row 22 first sign, row 22/23 S-like sign in *meggyőződik*: as described.
- Row 31 `roszsta` (`z31rosz.png`): r o s z s t a as the ledger says, order slip disclosed.
- Rows 28–31 and the upward row 32: order and direction correct; plain *folyt. köv.* present ("fost kön" to the eye), rightly left out of the ciphertext.

## Status of the card

Rows 31–32 contain one unread word, and *ha i két[ke]dések* a doubtful phrase, but the clauses read. The orchestrator's standard (a lone un-understood word, rest reads) is met. Register type MASC is appropriate.

## Could not verify

- The open word in rows 31–32 and the true form of `ketdesek`.
- The sign under the stamp triangle and the row 27 blot.
- Postmark place and date (illegible at this resolution); the card stays undated.
- Rows 14–25 were not all checked at zoom level; see finding 10.
- The picture side's printed verse was not read by me.
