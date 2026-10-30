# HCP 1396 / pc_hcp_77 — partial Caesar reading

**Partial, no DONE1.** The coordinator read all three rendered portal tabs
on 2026-10-26: Not solved, no supplied transcription or solution. Both original
scans were personally inspected by the solver. Portal date: 1907-04-21. The
address appears Mr. Abbott, White[?]lake Farms, Chudleigh, Devon; exact farm
spelling is not established. Preserved portal recipient field is W. Abboú.
The picture is printed All Saints Church, Branksome; no handwritten cipher
continuation was observed there.

## Ordinary writing

In the original upper-left corner, separately oriented ordinary text reads
approximately **“Fearfull weather to day.”** Fearfull appears to end with two
l strokes; the second l is less secure. This is not processed with the cipher
key. After rotating the scan 270 degrees clockwise, the ordinary message
heading reads **Sunday. C./G. H.** Its first initial is ambiguous. These two
ordinary fields are recorded separately in work/transcription.json.

## Cipher and recovered text

The coordinator supplied Caesar−1 as a hypothesis from nearby Abbott cards.
It is independently confirmed here by tusbohf→STRANGE, bmjlf→ALIKE,
Joufsjps→INTERIOR and uibolt→THANKS, among other whole words. Encryption
advances one position in the ordinary Latin alphabet; decryption uses:

```text
Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain:  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Exactly **58 frozen alphabetic positions** decode to these fragments:

```text
MY [probable DEAREST] HOW
STRANGE WE ARE BOTH
ALIKE WITH THIS
INTERIOR THANKS FOR
[unresolved 2-like sign + word] [unresolved initials/suffix] OWN
[unresolved short form] GIRL
```

The unusual wording STRANGE WE ARE BOTH ALIKE WITH THIS INTERIOR is retained
literally; it has not been rewritten into more idiomatic English. Displayed
word spaces are manual visual decisions. The faint Efbsftu→DEAREST greeting
is provisional and excluded from the 58 frozen positions.

## Remaining ink

- After THANKS FOR is a 2-like sign and a q…-like connected word. The pen
  strokes cross descenders from the line above. The exact letters and whether
  the first mark is a numeral are not frozen. No “two postcards” expansion
  was inserted from context.
- The next initial-like field resembles M/N & L, followed by a small suffix
  and a large curved brace. Its exact letters and whether this shorthand was
  encrypted are unresolved. A Caesar interpretation and an ordinary-initial
  interpretation must remain separate; no love-and-kisses expansion is
  asserted.
- Before GIRL there is an N/M-like main character and a raised 1/l-like
  narrow stroke. It is not silently normalized to No1, a personal name or
  the different E-like prefix on other cards.
- The ordinary weather spelling, heading initial and exact farm name retain
  their uncertainty. Original metadata has not been changed.

## Reproduction

```sh
python3 ciphers/hcp-1396/work/decode.py
```

The command checks immutable source hashes, reads the manual transcript and
applies the fixed key to the 58 frozen alphabetic positions. It prints the
ordinary comments unchanged, labels the provisional greeting, and preserves
unclassified fields. It does not recognize letters from pixels. Inspection
copies include work/body-large.jpg and an explicitly enhanced red-channel
view work/red-channel.png; enhancement adds no source detail.

Slovak translation of recovered fragments:

> Môj/moje [pravdepodobne najdrahší/najdrahšia], aké zvláštne, obaja sme si
> podobní s týmto interiérom. Ďakujem za [neprečítané]. Vlastné ... dievča.

The awkward sentence follows the literal recovered words; the unfinished
closing is not translated as a complete sentence. No external corpus or
published solution was used. No reviewer, watcher, PDF, register entry or
FINAL was created.

## Update 2026-10-29 (Claude Opus 5.5) — still PARTIAL, no DONE1

Re-checked on enlarged crops (work/z-body-rot90.png, work/z-2group-red.png,
work/z-closing.png). Lines 1–4 and `Pxo.` / `Hjsm` confirmed. `Efbsftu`
(DEAREST) is legible at 6x and can be treated as read rather than provisional.
The group after `uibolt gps. 2` remains unread: a p-shaped first sign (stem
above and below, bowl to the right), a closed bowl, a d-like sign and a t-like
exit (literal guess `p?dt` → O?CS). "2 PCS" (cipher `qdt`) fits the context but
not the pixels well enough to assert. The shorthand `M & L.s` and the `M`+raised
sign before GIRL are reported literally (L & K.s / L[t] only if enciphered).
Earlier transcription and Caesar −1 identification were by the OpenAI GPT solver
(2026-10-26); this pass verified them. See NOTES.md 2026-10-29.
