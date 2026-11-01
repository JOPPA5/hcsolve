REVISE

# Review 1 of hcp-1283 (Claude Opus 5.5, reviewer, 2026-11-01)

Summary: the key, the transcription of about 525 of 532 signs and most of the letter are correct. One sentence is misread (its subject and mood are wrong), one ledger sign is wrong and creates a false spelling claim, one written sign is dropped from the text on a doubtful call, and accent dots are omitted from the ledger. These are concrete fixes; the reading as a whole stands.

## What I verified and how

- `python3 -I ciphers/hcp-1283/work/decode.py`: all four SHA-256 hashes OK; prints 31 rows, 532 signs. Output equals the literal block in SOLUTION.md.
- `review/work/verify.py` (run with `python3 -I`): own key dict written from the hcp-1216 table, not imported from the solver. It decodes `work/ledger.txt` and compares it row by row with SOLUTION.md: 0 mismatches, 0 unmapped tokens. The key covers the whole ledger; the only tokens outside the key are `!` and `?`.
- Transcription against pixels: `review/work/strips.py` sheared the hi-res address scan by 0.035 and cut enlarged strips (`s00a` to `s05b`, 2x). I read all 25 main rows sign by sign on these. `z.py`/`z2.py` give 3x to 5x crops (`z_*.png`) of every doubtful spot, the bottom row, and the stamp field.
- Restorations judged on pixels: stamp row 1 `[Ist]`: only sign bottoms show (a tail, a bowl foot, a stem), compatible, disclosed. Stamp row 6 `[l]`: a solid blot, sense-only, disclosed. Stamp row 4 n: one stroke only, disclosed. All acceptable.
- Sampled spots confirmed: row 11 m has 3 strokes across the strip seam; row 12 has 3 b and opens with two bars (a, so the dittography in item 8 is real); row 17 m has 3 strokes; rows 14 and 15 and stamp row 5 all have cs as left bowl + right stroke or bowl; row 9 e with blotted top bar; row 8 blot over the sign in *bár*.
- Picture side: printed song *Sokszor úgy szeretnék sírni...*, no cipher. Plain address agrees.
- Family parallels: hcp-1305 (FINAL) *Hogy mulat Harasztin?* and *a legjob[b] kedvében találja soraim*; hcp-1265 (no FINAL yet, used only as a hypothesis) *Az jó, hogy kiment Harasztira, legalább szívja ezt a jó tanyai levegőt, bár igaz, hogy Árokszállásba[n]...*. Recurring words agree (hogy ×4, jobban ×2, nekem ×2, mulat ×2, gondol- ×2 all counted).
- Plaintext is real period Hungarian with this writer's habits (single for double consonants, j for ly, dropped final letters). Nothing looks forced apart from finding 1.

## Findings

1. **major: rows 17-18 are misread; the sentence is a question to Jolánka, not Feri's plan.** Literal signs, which are not in dispute: `kimegye|harasz|tira|sziva e még a tanya|i levegöt`. The solver has to invent letters in both verbs: *kimegye[k]* adds a k, and *szívom meg* replaces a, e with o, m and drops the written e silently. Reading with the question particle *-e* needs neither: **Jövő héten kimegy-e Harasztira? Szív[j]a-e még a tanyai levegőt?** ("Will you go out to Haraszti next week? Will you still be breathing the farm air?"). Only the j is supplied, and j-loss in this cluster is minor beside the writer's other omissions. Support: the writer uses particle *-e* twice more nearby (*járnak-e*, *gondol-e*, both already adopted), the *Ön* third-person form fits *kimegy* and *szívja*, and the Haraszti stays are Jolánka's on sisters hcp-1305 and hcp-1265, the latter with *szívja ... a ... tanyai levegőt* almost word for word. Fix the normalized text, all three translations, and items 10 and 11. English now says "I am going out to Haraszti", which reverses who travels.

2. **major: row 19 last sign is k, not g; item 12's "writer has g for k" is false.** The ledger has `... F O G`. See `z_r19e2.png`: a hook top with a smooth stem curling to a heavy foot at the left, the same form as the k ending row 20 `jarnak` (`z_r20e.png`). The g on this card (`z_r16dot.png`) has an angular waist and a straight diagonal tail. So the card has `arok|szalasba`, spelled correctly. Change G to K in the ledger, rerun, and delete the claim. The "Why it is correct" argument that the town is named in the cipher becomes stronger.

3. **major: row 15 `!e`: a written sign is dropped and the mark is probably d.** See `z_r15end.png`. The "exclamation mark" has a dark short stroke at upper left of the long stroke, which is the short+long d of the family, followed by a clear three-bar e. Reading **de lesz még ez jobban is** ("but this will get better yet") uses every sign and gives idiomatic Hungarian; the solver's reading discards the e with no explanation (item 9). Against: the short stroke touches the tail of the preceding l, and there is a dot under the long stroke, so `!` is not excluded. Re-examine and either adopt *de* (noting the dot and that the call rests partly on word sense), or justify the stray e. Do not simply drop it.

4. **minor: acute dots present on the card are missing from the ledger.** Row 16 *még* (`z_r16dot.png`, clear), row 18 *még* (`z_r18b.png`, clear; also `z_r17.png` shows it from above) and row 15 *nék* (`z_r14mid.png`, dot below row 14 above the e). The ledger has plain E, so the literal output says `meg`. Row 18's dot is itself evidence against *szívom meg*, since verbal prefix *meg* would have none. The normalized row 16 already says *még*, so literal and normalized disagree without disclosure. Add `:a`.

5. **minor: normalization *Árokszálláson* is not on the card.** The card has `...szalasba`, and sister hcp-1265 normalizes the same form as *Árokszállásba[n]*. Use that; a dialect -ba for -ban needs no -on.

6. **minor: `hejetz{?}` is less uncertain in one respect.** The "small hook" of row 25 (`z_b2.png`) is the flat-topped right bowl s as in row 1 *édes*, followed by a separate comma-like tick. Transcribe s plus a tick; the word stays unread (`hejetzs`), and it is alone, as is `cskavol`, so the completeness rule for isolated words is met.

7. **minor: small undisclosed points.** Row 10 *ettől* has an overwritten sign: a three-bar e under the o of *tö* and a heavily retraced first t (`z_r10.png`). Row 16 has a full stop after *is* and row 19 a dot beside the t of *levegőt*, not in the ledger. "26 written rows" in "Why it is correct" should be 25 main rows + 6 stamp rows.

8. **minor: item 10 says Haraszti is unidentified without citing the sisters.** Cite hcp-1305 (and hcp-1265 once final), and also note there that Haraszti is a place Jolánka stays at.

Suggestion, not a finding: in `a cskavol lehet`, the parallel with *senkivel* in the same sentence raises an instrumental *-val* ("if it can be with ...") with o for a; a name or pet form is possible. I checked the o: it is a clear loop, so nothing here can be adopted, and "not understood" is the honest status. The English frame "if ... is possible" should stay marked as tentative.

## Disclosure and honesty

Key source (hcp-1216) credited; no published solution claimed or used, as far as files show. `cskavol` and `hejetz?` are honestly left unread. *Jolánkám*, *vasárnap* p, *drága* d, *bár* are correctly flagged as resting on word sense. The single command is reproducible, and the ledger is correctly described as hand-made and not blind.

## What I could not verify

- The portal status and absence of attachments, and the register check: no re-fetch in this review; taken from `source/metadata.md` and the orchestrator.
- The date: portal filename only; the postmark is not legible to me either.
- Exact identity of Haraszti, Berek, and Feri with the Feri of other cards.
- The three signs hidden under the stamp, and the blotted l of stamp row 6, beyond compatibility with the sign remains.
