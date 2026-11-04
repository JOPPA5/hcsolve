# hcp-904 — solution (Claude Opus 5.5, 2026-11-03)

Card: picture postcard "Gruss aus Leipzig — Reichsgericht" (W. Hagelberg, Berlin), posted Leipzig 1902 (postmark "..1.02 5-6 N"), to Herrn Martin Laibelein, Wolferode b/ Eisleben, Pfarre. T. Schrödel collection. Portal status Not solved, no attached transcription or solution. No published solution was looked up or used; all work is my own (no earlier solver work exists on this number).

## Cipher type and key
German written in Greek letters (alphabet substitution, MASC). The writing is a straightforward letter-for-letter transliteration:

| sign | letter | sign | letter |
|---|---|---|---|
| α / Α | a / A | ν (written like a Latin r) | n |
| β / Β | b / B | ο | o |
| γ (μ-like with long tail) / Γ | g / G | ρ (written like ς/ρ) | r |
| δ / Δ | d / D | σ (several S-like forms) | s |
| ε | e | τ (hooked t with top bar) | t |
| ζ | z | υ (v-shaped) | u; also w in "beantuorten" |
| ʽ (rough breathing) | h | φ | f (also v in "fier" = vier) |
| ι (written as a small c) / Ι | i / J | χ | ch |
| κ / Κ | k / K | Ϝ (digamma, F-shaped) | W |
| λ / Λ | l / L | μ / Μ | m / M |

## Command (run from repo root)
    python3 -I ciphers/hcp-904/work/decode.py
It checks the SHA-256 of the four scans and prints the plaintext from work/transcription.txt (my own transcription; the portal attaches none).

## Plaintext (German, literal; [x] = restored under an ink blot)
    [L]. M. Konnte leider Dein lieben Brief
    nicht mehr beantuorten. fier Wochen sind
    abe[r] lang, kannst Du mir keine ande[r]
    Adr. angeben? sonst must Du Dich schon so lange ge-
    duldigen. habe mich sehr uber Deinen Brief gefreut.
    herzlichen Gruss u Kuss Deine tr. Je??i.

Normalised: "L[ieber] M[artin]! Konnte leider Deinen lieben Brief nicht mehr beantworten. Vier Wochen sind aber lang, kannst Du mir keine andere Adr[esse] angeben? Sonst musst Du Dich schon so lange geduldigen. Habe mich sehr über Deinen Brief gefreut. Herzlichen Gruss u[nd] Kuss, Deine tr[eue] Je..i."

English: "Dear M.! Unfortunately I could no longer answer your dear letter. But four weeks is long — can't you give me another address? Otherwise you will have to be patient for that long. I was very pleased with your letter. Warm greetings and a kiss, your faithful Je..i."

Slovak: "Milý M.! Žiaľ, nestihla som už odpovedať na tvoj milý list. Štyri týždne sú však dlhé, nemôžeš mi dať inú adresu? Inak sa budeš musieť tak dlho obrniť trpezlivosťou. Tvoj list ma veľmi potešil. Srdečný pozdrav a bozk, tvoja verná Je..i."

## Uncertainties
1. First sign of line 1 is covered by a heavy ink blot (it can look like "4", Δ or Λ). Read as Λ: "L. M." = "Lieber Martin" (recipient is Martin Laibelein). This expansion rests on context; the abbreviation itself is certain only for "M.".
2. "abe[r]": the last sign is blotted; r restored from word sense (only letter making "aber").
3. "ande[r]" at the right edge: last sign blotted/at edge, ρ-like trace; read r. Whether an e followed ("andere") cannot be seen; the meaning is not affected.
4. Signature: Ι ε + two signs (an n-like sign with a cross stroke, then a δ/ϑ-like loop) + ι. Reported literally as "Je??i" (a girl's pet name such as Jenni/Jetti is possible, not established). "tr." read as "treue" (abbreviation).
5. "beantuorten": the writer rendered w as υ before o; "fier" for vier uses φ. Non-standard "Dein lieben Brief", "must", "geduldigen" (dialect/older form of "sich gedulden") are transcribed as written.
6. Address-side: plain Kurrent address, no cipher found; the stamp was not lifted, so nothing under it can be checked. No other hidden writing seen on the picture side.

## Why it is correct
Every sign of the six lines decodes with one consistent Greek-letter key into grammatical, coherent German that fits a 1902 private postcard to a man named Martin; only the blotted signs and the signature are open, all disclosed.

## Response to review 1
Review 1 (Claude Opus 5.5, verdict ACCEPT) confirmed the reproduction command, an identical independent transcription and decryption, and the Greek-letter key over all six lines. All five findings are minor and are taken over below; no decoded letter changes. The command `python3 -I ciphers/hcp-904/work/decode.py` was re-run on 2026-11-03 after this edit: all four hash checks OK and the same six lines printed.

1. **Line-1 initial (blot): agreed.** The first sign of line 1 is under a solid triangular ink blot (review/work/blot1.png; on the scan it looks like a "4"). Its outline fits Λ, but a filled-in Δ cannot be excluded. Readings: [Λ]. M. = "L[ieber] M[artin]" (preferred, because the recipient is Martin Laibelein), or [Δ]. M. = "D[ein] M..." or similar. The expansion "Lieber Martin" is editorial and rests on context. Only "M." is read directly.
2. **Smudged start of line 5: agreed.** The first three signs of δυλδιγεν (δ, υ, λ; review/work/l5start.png, work/crops/l5a.png) are smudged and overwritten, and the λ is almost solid ink. They can still be read as δ υ λ, but the reading is partly supported by word sense ("ge-|duldigen", which continues the "ge-" at the end of line 4). work/transcription.txt is left unchanged, because its letters do not change; this note is the disclosure.
3. **Variant sign shapes: agreed; key-table notes added.** The Γ of Γρυσσ (line 6) is drawn T-shaped and could be taken for τ/Τ. The word "Gruss" decides it, and it is the only capital G on the card. The ʽ (h) of ʽερζλιχεν is a free-standing hook with a dot above it, the same large hook as in ʽαβε (line 5), and should not be read as ι or ε. Other occurrences of ʽ (μεʽρ, σεʽρ) are smaller hooks inside the word.
4. **Signature: agreed; still unresolved.** Ι ε + an η/ν-like sign with a cross stroke + a ϑ/δ-like loop + ι (review/work/sig.png). It is kept as "Je??i". Any name (Jenni, Jetti, ...) is a guess and is not offered as a reading. This is a single unread word (a name); the rest of the card reads.
5. **Register type: agreed, MASC.** The question of steganography was checked again for this run, because hidden messages under the stamp occur on other card series. The address side carries only the plain Kurrent address. The stamp was not lifted, so the scan shows nothing under it. The picture-side marks in the sky are smudges or printing, not letters. Nothing hidden was found, so the type stays MASC and not "MASC + Steganography". The possibility of writing under the stamp is listed as unverifiable.
