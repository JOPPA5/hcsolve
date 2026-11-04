ACCEPT

# Review 1 — hcp-1031 (cpc_1904-03-22_AT_Wien_AT_Wien_, to Anna See, Wien XIX)

Reviewer: Claude Opus 5.5, 2026-11-03. I tried to refute the reading and could not. The decipherment is correct. Only minor points remain.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1031/work/decode.py` (from the repo root). All four SHA-256 hashes are OK, and the raw output per line is exactly the plaintext claimed in SOLUTION.md. The assert that compares the word-divided reading with the raw letters passes.
2. **Independent decoder.** `review/work/indep_decode.py` uses my own table, typed from my crops (a=+, b=ʟ-hook, c=stroke before h/k, d=⊥, e=λ, f=crossed 7, g=θ, h=8, i=stroke, j=flagged stroke, k=x, l=6, m=barred three-leg, n=Π, o=0, p=9, r=3, s=flat-topped 5, t=2/z with tail, u=u, w=looped ꭓ, z=round S). Run with `python3 -I review/work/indep_decode.py work/transcription.txt` (from the cipher directory). Its output (`review/work/indep_out.txt`) is identical, line by line, to the solver's output (`diff` empty). It counts 222 key signs plus the literals V, I and two 4s, which matches the solver's count. Each code has one value, and the frequency profile (e 35, s 22, n 22, i 17, t 13, r 13 …) is normal for German.
3. **Transcription against the pixels.** I cropped the hi-res original `work/hires/..._pic.jpg` at 1.5–5x, with autocontrast, into `review/work/`:
   - Left block, rotated so it reads correctly (`left_1/2/3.png`). I checked every sign of rows A–D against the transcription and found no difference. Examples: "ꭓ0ꭓi3 UN5 73LiZ+T" = wo wir uns Freitag, "SUXU¨N-" = zukün-, "SUX0¨NNLN" = zu können. In "Abschiedsbriefes", the c of "sch" is the plain stroke, as disclosed.
   - TR1 (`tr1.png`, `tr1_nim.png`): "cλΠ, 50ΠiM i8Π MiZ." = ben, so nim ihn mit.
   - TR2 (`tr2_m.png`, `tr2_mund.png`): the m of "mündlich" has its first leg slightly apart, but that leg's top touches the start of the bar. It reads as one m sign, as the solver says. "Π⊥6iC8,5λi" = ndlich, sei.
   - TR3 (`tr3_gutmit.png`): "50θU2 [mark] Mi2". See finding 2.
   - TR4 (`tr4.png`, `tr4_joh.png`): flagged stroke + 0 + 8 "." ꭓ067 "." VI "." λΠθλ6θ+55λ4 "." = Joh. Wolf. VI. Engelgasse 4.
   - TR5 (`tr5.png`, `tr5_color.png`, `tr5_name2.png`, `tr5v.png`, `right_col.png`): ʟ +̈ stroke X λ 3 λ stroke | 4-like sign | λ X, then running vertically down beside the hat Π, stroke, Π, θ, λ, 3, "." = Bäckerei ?ekninger. Read top to bottom, the vertical tail gives n-i-n-g-e-r. I agree with the solver's orientation.
4. **Umlauts.** The dots stand over the a, o and u signs only (Näheres, zukünftige, können, mündlich, Bäckerei). This confirms the key on its own.
5. **Language and context.** The plaintext is fluent German of about 1900 with Viennese colour ("Annerl", "Sei so gut", "Näheres mündlich", "Gruss"). The address side is in plain script, to Anna See at the Israelitisches Waisenhaus, Ruthgasse 21, Wien XIX, posted in Vienna on 22.3.04. A secret meeting about "our future situation" and a "farewell letter" fits a girl at an orphanage being written to in cipher.
6. **Sources.** No sister card in the repo (I grepped for Anna See, Ruthgasse and Engelgasse in ciphers/*/SOLUTION.md). The portal has no attached solution. The card is not in skip.txt or register-exclusions.json. I found no sign that a published solution was used.

## Findings

1. **minor — the first sign of the bakery name has an earlier reading the solver did not mention.** `work/trans_v0.txt` (the solver's first transcription) read this sign as Z (t), which gives "Tekninger". The final version reads it as a literal 4 and leaves it unread. In my crop (`tr5_name2.png`) the sign looks most like a 4 with a curl: an oblique stroke, a cross-bar and a down-stroke. It does not look like the 2-shaped t seen elsewhere, so I agree it is not a clear t. SOLUTION.md and the report should still mention the earlier "T-" alternative and say that the name is unread. This is a single proper name and the rest of the card reads, so it does not make the card partial.
2. **minor — the TR3 mark between "gut" and "mit".** There is a thin λ-like mark there. It lies on the printed plant stalk and is lighter and thinner than the pencil around it. I agree it is most likely part of the picture. Read as e it would give "gute mit", which does not work. The solver discloses this (uncertainty 6). Nothing to change.
3. **minor — "nim" might be "nimm".** In "nim" the m sign carries a slightly heavier top bar than the m in "mit" (`tr1_nim.png`). This could be the German doubling bar over m, but I cannot tell it from the barred form of the sign itself. The note "single-m spelling" (uncertainty 7) should be softened to "single m, or an m-doubling bar not distinguishable from the sign's own bar".
4. **minor — j and c rest on word sense.** In "Joh." the j is a stroke with a flag and no crossbar, distinct from the crossed 7 = f in "Wolf" and "treffen" (`tr4_joh.png`). The c/i shared stroke appears only in ch and ck. Both are disclosed correctly.
5. **minor — check for a hidden message.** On some series of cards in this collection, messages have been found under the stamp (reported for the Jolánka postcards). Here the stamp is still on the card. Neither scan can show what is under it, and I found no pencil writing round the stamp edges or elsewhere on the address side. On the picture side, the dark marks in the plant at the right edge (`right_col.png`) are part of the hand-coloured printed picture, not pencil writing. The solver says this (uncertainty 8). The report should state plainly that the space under the stamp was not inspected, and that a hidden message there cannot be ruled out.
6. **minor — the address is not checked.** "VI. Engelgasse 4" is taken as Vienna district VI and a house number. Neither I nor the solver checked that a street of that name existed in Mariahilf in 1904. This is disclosed.

## Could not verify

- What is under the stamp, if anything.
- The identity of the bakery's owner (the sign read as "4-ekninger") and the 1904 address.
- Who Joh. Wolf and Anna See were. I found no archival source.

Type for the register: MASC. That is the right label: there is no confirmed hidden writing, so "MASC + Steganography" does not apply on present evidence.
