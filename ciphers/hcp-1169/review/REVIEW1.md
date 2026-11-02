ACCEPT

# Review 1, hcp-1169 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands. I re-read all 271 cipher signs on the hires scan and could not refute it. The findings are all minor and concern disclosure and the open text, not the decipherment. Findings 1 and 2 touch the text and should be fixed before FINAL.

## What I verified and how

- Command: `python3 -I ciphers/hcp-1169/work/decode.py` from the repo root. Hashes OK, 271 signs, 2 by sense, assertion passes. The accented text it prints is hard-coded (as SOLUTION.md says); the decoded line is computed and agrees with it letter by letter after folding.
- Independent decoder: `review/work/decode_rev.py`, key typed afresh from the hcp-1174 table plus the four card-specific values. Same letters, 271 signs, 30 distinct sign tokens, no sign outside the table apart from the two `~` tokens, which are disclosed.
- Pixels: `review/work/crops.py`, `crops2.py`, `crops3.py`, `crops4.py` cut every row of the panel from `work/hires/*adr.jpg` at about 2.7x to 4x (output in `review/work/crops/`, `row00`-`row12` plus close-ups). I read rows 0 to 12 sign by sign before comparing with `work/transcription.txt`, and the last two lines from `end1.jpg`, `end2.jpg`, `closing.jpg`. No digit or mark differs from the transcription, apart from the shape call in finding 3. Commas that hang into the next row are assigned correctly. The solver's early trap (`1: 5,` in `elhozta`) is right: the comma under the first 5 is the one that reaches towards `3.` in the row below.
- Key: the values `4` f (4 uses), `4.` gy (5), `6` j (7) are each carried by several independent words. `5.` ly has only 2 uses (`melyet`, `oly`). The conflict with `5.` = l in hcp-1178 and hcp-1179 is disclosed. Plaintext is unaffected either way, since `5.` only occurs where l-sound/ly is required.
- Language: continuous Hungarian with the idiom `esik le szívemről egy malomkő` and a developed simile. The misspellings (`akor`, `hejébe`, `fügni`, `tojássait`) are the unforced kind and are disclosed; `akor` also occurs on hcp-1175 according to the hcp-1178 notes. Names and place fit hcp-1174/1178/1179. English and Slovak translations checked; they are faithful.
- Open text: `Most pedig`, `Boldog ujévet kivánok mindnyájatoknak még a kis haragos Mariskónak is nemigen`, the date and `Mezőkövesd` all confirmed on `note1`, `note2`, `note3`, `year`, `row12`.

## Rulings the solver asked for or left open

- `megfektel`: every letter is visible and `nemigen` reads. This is one un-understood word; the sentence before it is complete. Under the rule for this run the card counts as complete and may get a register entry, provided the word stays marked as not understood. This is a judgement call: the short clause has no other content word.
- `esik`: the dot beside the 1 is real and sits where the á dot sits (`row06.jpg`, third strip). Literal `esák` is not a word. Keeping it as a sense call is right.
- `Árpád`, final 3: a long stroke runs from under the 3 up across the red divider (`fin3.jpg`). It is comma-shaped in direction but about three times the length of a normal comma and starts far to the right of the digit. Treating it as a flourish is acceptable; the name matches hcp-1174.
- `téged)`: the `)` and the short stroke beside it are darker than the neighbouring digits (`end1.jpg`). Punctuation is the right call.

## Findings

1. **minor: the address is misread.** SOLUTION.md gives `Szomolya-Bogács / (Borsod megy.)`. On `addr.jpg` and `borsod.jpg`, after `Borsod` there is `m`, one tall crossed stroke with a long descender, then `u p.`. There is no `e` or `g` visible, and `u. p.` was dropped. hcp-1174 has the same form `Szomolya / u. p. Bogács`. Suggested: `(Borsod m[...] u. p.`, with the stroke after m marked unclear, and the `)` after `Szomolya` noted. Also `Szépreményü` has a two-dot ü on the card. It does not change the reading of the message, but the address is part of the card.

2. **minor: the printed greeting is mis-stated.** SOLUTION.md gives printed `Boldog újévet!`. The print has no accent on the u: `Boldog ujévet!` (`printed.jpg`). The reasons section uses the accented form too.

3. **minor: `szívű`, the mark is a comma in shape.** On `sz7.jpg` the mark under the 7 has a head and a short tail, the same form as the comma on the neighbouring `6,` only shorter. It is unlike the round dots of `7.` in `szívemről` and `fészkében`. The honest transcription is a short `7,`, literal `sívű`, with `szívű` as a correction of a slip or a shortened mark. "Neither a clean dot nor a long comma" is softer than the pixels. The reading itself is safe. Also, `work/crops/r4d.png`, cited there, should be replaced if it does not show this sign: the sign is at the end of the row beginning `6, 1 1, 0 5,`.

4. **minor: `megfektel`, the t is not preferred by the pixels.** The second crossed stroke goes below the line like the first f (`megf.jpg`), while the t of `atoknak` stands on the line (`tt.jpg`). `megfekfel` is at least as good a letter reading as `megfektel`. SOLUTION.md says "t or f", but the plaintext prints only t. Print `megfek[t/f]el` or say so in the plaintext. The suggestion `megfektél` rests on the t, which should be stated. I also tested j for the k (that would give `megfejtel`, "decipher"); the letter has an ascender and no descender, so that is out.

5. **minor: `Mariskónak` has two vowel bodies.** On `kona.jpg` there is an `o` and then a second small vowel under the arch, before `nak`, so "the o carries a mark" understates it. It looks like a correction or a doubled vowel. The name is not in doubt. Note it as written.

6. **minor: the one-dot `:1` is not only in `szabadulás`.** `:1` in `újévet` also shows one dot, left and low (`uj.jpg`). The others (`fügni`, `-vű`, `hű`, `üdvözölve`) show two. So one-dot `:1` is a real variant: uncertainty 4 can be firmer, and `újévet` should be listed.

7. **minor: the postmark says a little more than stated.** "Mostly lost" is fair for the day and month, but `9 1` plus a hook that fits 5 is visible below the wheel (`stamp.jpg`). This supports the year against the overwritten third digit in the handwritten date. Worth a clause.

8. **minor: "each recur in several independent words" overstates `5.`**, which has two words on this card.

## What I could not verify

- The HistoCrypt article linked by the portal: not opened by me either, so I cannot exclude that it discusses this card. The solver disclosed this.
- The sense of `megfektel` and the stroke after `m` in the address.
- The day and month of the postmark.
- From what the writer expected `szabadulás`; the card does not say, and the translation rightly leaves it open.
