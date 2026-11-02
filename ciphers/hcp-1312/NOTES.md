# Notes hcp-1312

2026-10-30: captured by Claude Opus 5.5 (orchestrator).

2026-10-30 (Claude Opus 5.5, solver) — PARTIAL, no marker.

Cipher: Jolánka-family Hungarian monoalphabetic substitution, key of hcp-1216 unchanged. Addressee Tóth Jolánka, plain "Szépreményű" on the address side; no sender name read. Ledger work/ledger-partial.txt; check with `python3 -I ciphers/hcp-1312/work/decode_partial.py` from the repo root. Enhancement scripts work/crop.py, enh*.py (red minus green removes brown foxing spots), crops in work/crops/.

Read (rows 1-12 from clean pixels, 13 mostly, 14 washed):
Kedves Jolánkám! Remélem, hogy a kedvében találja soraim. Nálunk nincs semmi újság. Hát önöknél, édesem? Valami újság? Most mást nem, csak az a verset, de ebbe a legjobb gondolatai[m] benne van. Én azt hiszem, édes kincsem, s az másképen is lehet, hogy minket az Úr Isten egymásnak teremtett. [?]látásra [row 15 unread]

English: Dear Jolánka! I hope my lines find you in good spirits. There is no news with us. And with you, my sweet? Any news? Now nothing else, only that verse, but my best thoughts are in it. I believe, sweet treasure, and it may well be otherwise too, that the Lord God created us for each other. [?]-látásra [unread row]
Slovak: Milá Jolánka! Dúfam, že Vás moje riadky zastihnú v dobrej nálade. U nás nie je nič nové. A u Vás, drahá? Niečo nové? Teraz nič iné, len tú báseň, ale sú v nej moje najlepšie myšlienky. Myslím si, sladký poklad, a môže to byť aj inak, že nás Pán Boh stvoril jeden pre druhého. [?]látásra [neprečítaný riadok]

"That verse" presumably means the printed verse on the picture side (Csak egy kislányt hagyok itthon...).

Why it stops:
- Row 15 (about 14 signs, y≈1178-1216 in 2000px display coordinates) was washed by water. Blurred pink shapes remain; only "= ll" (a n) is plausible. A faint ~ ≡ Λ + blob suggests "level-" (letter) but that is a guess and is NOT adopted. The closing or signature may be here, so this is not a small residual.
- Row 14: the sign after "teremtett" (a slanted stroke with a crossbar) is unread; "látásra" needs "viszont" but there is no room for it on the row. Whole row 14 is read from washed shapes, supported by sense; a reviewer should recheck it.

Open points in the read part:
- r4 "coraim" and r8 "cak": the left bowl (C, in r8 with a bar) stands where sense needs s (soraim) and cs (csak). Written as read; normalization is by sense. Not checked against sister ledgers.
- r9 "ebe" = ebbe; r6 "önknél" = önöknél; r10 "gondolatai" has an i whose dot lies under r9; final m absent, supplied in brackets. r10 first sign is a g variant with a hook, g by sense.
- r12 blot: h is a tall stroke under the blot, e has three bars seen faintly in the pink stain, so "lehet" is partly by sense. "s az ... is lehet" reads oddly (one might expect "nem is lehet"), kept as written. h/p in "másképen" by sense; "-pem" is read as written, 3rd stroke faint, so m/n is unsure.
- Plain text in the stamp box is smeared: roughly "Édes angyalom csók[o]lak szám/talanszor" (Sweet angel, I kiss you countless times); not fully verified. Plain address line "úrleánynak" and the town line are washed out; cancellation date unread.

2026-11-02 (Claude Opus 5.5, solver, second attempt ordered by the human).

Re-read every row from work/hires (crops work/rev2/, scripts work/rev2*.py). Blue minus green is the channel that matters: keeps washed ink, drops foxing (r-g from 2026-10-30 did not). Rows 14 and 15 then separate cleanly.
- Row 14: egymasnakteremtet; one final t, not two.
- Row 15 (y~2040-2090, rising at the end): i s t e n v e l e a v i s z o n t, then l a t a s r a at y~2010 across the divider. The crossbar sign at x~1567 hires is the t of viszont. Dead idea withdrawn: "level-" (2026-10-30 note), and the "no room for viszont" objection, which assumed the text sat in row 14.
- Row 12 h and e of lehet are visible: stem + short stroke under the blot, three bars in the pink stain.
- Hires x: Isten 150-530; vele 569-910; a 950-1000; v 1030-1100; i 1115-1207; s z 1235-1345; o 1430-1470; n 1490-1530; t 1567. Foxing/crack over x~1345-1420 is an outline in b-g, not ink.
- Kept: másképem (3 strokes, third short) and no "nem" supplied.
Ledger work/ledger-rev2.txt, decoder work/decode_rev2.py, normalized text work/normalized-rev2.txt supersede the *-partial files. Whole card now meets the completeness rule; DONE1 created.

2026-11-02 (Claude Opus 5.5, solver): review 1 ACCEPT, five minor findings addressed (see SOLUTION.md, Response to review 1). Ledger marks 8 restored row 15 signs with ^. Report and register entry written.
