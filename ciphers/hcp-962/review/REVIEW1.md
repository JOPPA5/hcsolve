ACCEPT

# HCP 962 – Review round 1

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-28.
Object: `SOLUTION.md` / `work/decode.py` / `work/transcript.json` as of DONE1 (`2026-10-28T18:07:50Z OpenAI GPT-6 Codex`).

## Summary

The solver's literal reading of all 117 Pigpen glyphs is correct. I re-read every glyph on the scan independently and decoded it with my own script. My reading agrees with the solver's in every position, including the literal `HORGEN` (the first glyph really is the dotted bracket open to the left, H, not the dotted bracket open to the right, M) and the umlauted `Ü` in `ZURÜCK`. The plaintext is natural German of c. 1900. The postmarks confirm the editorial correction to `MORGEN` and the reference to Sunday. The findings below are all minor and concern context and wording. None affects the decipherment.

Confirmed literal plaintext:

```
LIEBER ENGEL!
DIR ZU GEFALLEN
KOMME HORGEN
ZURÜCK. BIS SONN=
TAG NACH DER MESSE VERBLEIBE UNTER HERZLICHEM
GRUSS UND KUSS DEIN DICH LIEBENDER M
```

Reading: *Lieber Engel! Dir zu Gefallen komme [morgen] zurück. Bis Sonntag nach der Messe. Verbleibe unter herzlichem Gruß und Kuß dein dich liebender M.*

## What I verified and how

1. **Reproduction command.** I ran `python3 -I ciphers/hcp-962/work/decode.py` without `--write-transcript`, so nothing in `work/` was rewritten. Its output matches the plaintext claimed in `SOLUTION.md` exactly: rows r1–r6, `117/117 glyphs decoded and re-encoded; immutable source hashes match`. The unattested cells it lists are P, Q, W, X and Y.
2. **Independent decoder.** `review/work/review_decode.py` does not import any solver code. It uses its own notation: grid cells 1–9 by position, `*` for a dot, and v > < ^ for the wedges. It builds the key from the pair-filled grid AB/CD/EF/GH/IK/LM/NO/PQ/RS (J omitted), then TU/VW/XY/Z on the wedges, and decodes my own transcription. `python3 -I ciphers/hcp-962/review/work/review_decode.py` gives exactly the six rows above, with **117 cipher glyphs** and 21 distinct signs. The unused cells are ⊓, ⊓·, <, <· and >·, that is P, Q, X, Y and W, the same set the solver lists.
3. **Key consistency.** It is one fixed key for the whole card. Each sign has a single value everywhere: ┘/┘· = A/B, ⊔/⊔· = C/D, └/└· = E/F, ⊐/⊐· = G/H, □/□· = I/K, ⊏/⊏· = L/M, ┐/┐· = N/O, ┌/┌· = R/S, v/v· = T/U, > = V, ^ = Z. This is the standard tic-tac-toe grid read row by row with two letters per cell, so it is a regular alphabet and not fitted word by word. It covers every glyph on the card. Nothing is skipped and nothing is unread.
4. **Sign-by-sign reading of the scan.** I made upscales of the original `source/picture.jpg` with ffmpeg (lanczos, 4–12×) into `review/work/`:
   - row 1: `r1.png`, `r1w1.png`, `r1w2.png`
   - row 2: `r2.png`, `r2a.png`, `r2b.png`
   - row 3: `r3.png`, `r3a.png`, `r3b.png`
   - row 4: `r4.png`, `r4a.png`, `r4b.png`
   - row 5: `r5a–c.png`, `z5a–d.png`, `der.png`
   - row 6: `r6a–b.png`, `z6a–c.png`, `gruss_ss.png`, `kuss_ss.png`

   I read every glyph from these crops before comparing my reading with `decode.py`. Points I checked specifically:
   - **HORGEN** (`r3b.png`): the first glyph has a top bar, a right vertical and a bottom bar, opens to the left, and has a dot inside. That is ⊐· = H. The two M's of KOMME just before it (`r3a.png`) are ⊏· and open to the right. The literal H is real, so this is a writer's mirror slip and not a misreading. The solver discloses it correctly and does not normalize it in the literal text.
   - **ZURÜCK** (`r4a.png`): the fourth glyph is a v with one dot inside and two dots above it, so Ü. The glyph after it is ⊔ = C, then □· = K, followed by an ordinary full stop.
   - **DER** (`der.png`): the first glyph is ⊔ with a clear interior dot, so D. The ink blob on the following └ does not change it.
   - **GRUSS / KUSS** (`gruss_ss.png`, `kuss_ss.png`): all four S's are ┌ with a dot. The text reads SS, not SR or RS.
   - **Squares** in LIEBER, DIR, VERBLEIBE and others: no black interior dot, so I and not K. The faint grey marks in some of them are watermark or paper and lie under the ink.
   - **Dot placement.** On this card the dot of ┐· (O) in KOMME and HORGEN sits just *above* the top bar, not inside the corner. The dot of v· (U) in UNTER, GRUSS, UND and KUSS also sits above the v, whereas in ZU it is inside. This is writer style. Every one of these signs is still clearly dotted, and the solver's readings are right.
5. **Search for untranscribed cipher.** The rest of both sides contains no other Pigpen. The other marks are:
   - the printed caption "Neue Rheinbrücke" and the publisher's imprint
   - the HCPortal watermark
   - a handwritten pencil **"Bonn"** directly above the inset text (see finding 1)
   - faint violet pencil traces at the top right of the picture, about x880–1010 / y160–300 (`purple.png`). These are cursive-like scribbles, illegible, and not Pigpen.
   - on the address side: *Fräulein Maria Peters, Aachen, Adalbertsteinweg 46.*, a departure circle stamp (`addr_stamp.png`, place illegible, `…03. 6-7 V.`, “1 m”), and an arrival stamp `AACHEN 1 ANKUNFT 6.6.03` (`addr_arrival.png`, printed upside down)
6. **Context.** 6 June 1903 was a **Saturday** (`python3 -I -c "import datetime; print(datetime.date(1903,6,6).strftime('%A'))"`). The card was posted on the morning of 6 June (`6-7 V.`) and arrived in Aachen the same day. "Komme morgen zurück" therefore means Sunday 7 June. That fits "bis Sonntag nach der Messe" exactly, and it independently supports the intended reading MORGEN over the literal HORGEN. The picture shows the Rhine bridge at Bonn, which matches the handwritten "Bonn" and the portal name `…_DE_Bonn_DE_Aachen_`. The recipient Maria Peters in Aachen matches the metadata.
7. **Honesty and sources.** The portal status is Not solved and no solution is attached (`source/metadata.md`). I found nothing to suggest a published solution was used without disclosure. The solver labels `MORGEN` as editorial and keeps `HORGEN` literal. It also discloses that the initial M is not expanded and that there was no blind test.

## Findings

1. **minor – Handwritten "Bonn" and other non-cipher writing not inventoried.** `SOLUTION.md` lists the printed caption, the imprint and the watermarks as non-cipher. It does not mention:
   - the handwritten pencil "Bonn" above the inset (picture x~760–815, y~385–405), which is the place of writing and supports the Bonn attribution
   - the faint violet pencil traces at the top right
   - the address details (Adalbertsteinweg 46) and the two postmarks

   None of these is cipher, but the report should list them so that the reader knows every mark was accounted for.
2. **minor – Weekday and postmark evidence not used.** The solver leaves `MORGEN` as a "likely" correction supported only by syntax. The arrival stamp *Aachen 6.6.03* and the departure time *6-7 V.* show the card was written on Saturday 6 June 1903. "Morgen" is then Sunday, the same day named in "bis Sonntag nach der Messe". This is strong contextual confirmation and should be stated in the solution and the report. It is still an editorial correction, and the literal form should stay `HORGEN`.
3. **minor – Parsing of "Bis Sonntag nach der Messe".** The translation runs this phrase into the closing formula: *"Until Sunday after Mass, I remain, with heartfelt greetings…"*. A more natural reading treats *Bis Sonntag nach der Messe* as a farewell of its own ("See you Sunday after Mass"). *Verbleibe unter herzlichem Gruß und Kuß dein dich liebender M.* is then the standard closing formula. The card has no punctuation after MESSE, so both parses are possible. The solver should give the farewell parse at least as an alternative, since it agrees with the weekday evidence in finding 2.
4. **minor – Wording of the dot convention.** `SOLUTION.md` says the second letter of a pair "receives an interior dot". On this card the dots of O (KOMME, HORGEN) and of most U's are written outside the sign, above it. The key is unaffected, but the report should say that the writer places dots loosely so that a reader comparing it with the scan is not confused.

## What I could not verify

- **The identity of "M".** The sender's initial is not expanded, and nothing on the card identifies the sender.
- **The departure postmark.** The town name and day digits on the departure circle stamp are illegible on this scan. The Bonn origin rests on the picture, the handwritten "Bonn" and the portal metadata.
- **Novelty.** I did not repeat the solver's bounded checks of the portal, the AI register and the Schrödel paper. I relied on `SOURCES.md` and `source/metadata.md` for those.
