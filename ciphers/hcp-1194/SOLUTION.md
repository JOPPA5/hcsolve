# hcp-1194 — Solution (round 1, Claude Opus 5.5, 2026-11-03)

Card: postcard, Tepl/Teplá (Bohemia) 17 June 1900 → Herrn Anton Schönfelder, Wien IV, Favoritenplatz 7(?), Th. 29. Picture side "Franz. Künstler Karten No 3" carries the cipher in pencil, written along the left edge (card turned 90°). Address side is plain handwriting (no cipher). No earlier work, no attached or published solution (portal: Not solved; short web search 2026-11-03 found nothing for this card).

## Cipher type and key

Simple monoalphabetic substitution (MASC) with rune-like signs (a home-made "runic" alphabet loosely based on the futhark; not a standard futhark mapping: e.g. the ᚾ-like cross is E and the inverted-y Λ-like sign is N). Word gaps and full stops are written. The same alphabet appears on the sister card hcp-1195 (same recipient, Tepl, Feb 1900), which was not used for this reading.

| sign (shape name in work/key.json) | letter |
|---|---|
| asterisk ᚼ (star) | H |
| cross with slanted bar ᚾ-like (cross) | E |
| R-shape ᚱ (rune_r) | R |
| down-arrow ↓ / ᛦ-like (arrow_down) | Z |
| stem with two crossing bars ǂ (crossbar2) | D |
| diagonal stroke meeting a stem ᛅ-like (diag) | A |
| stem with leg down-right, Λ-like (lam) | N |
| stem with one up-right branch ᚴ-like (branch1) | K |
| stem with two up-right branches ᚠ (f2) | F |
| ᚠ written very heavily (f2heavy) | W (see uncertainties) |
| Γ with short right leg / Π, ᚢ-like (u_hook, u_pi) | U/Ü |
| B ᛒ | B |
| plain stem ᛁ | I |
| arrow-up ᛏ | T |
| stem with hook down-right at top ᛚ | L |
| stem with closed loop / flag ᚦ/ᚹ-like (p_closed) | G |
| lightning ᛋ (bolt) | S |
| ᛘ fork | M |

18 letters written with 17 distinct shapes: W is not a separate shape but the F shape (ᚠ) written very heavily, so F/W is a homograph resolved by word sense (uncertainty 2). Every sign on the card is covered (corrected after review 1, finding 1).

## Command (from repo root)

    python3 -I ciphers/hcp-1194/work/decode.py

It checks the SHA-256 of the source images and decodes work/transcription.txt (own transcription from work/hires/...pic.jpg; enlarged crops crop_all.png, w5w6.png, w6.png, sig5.png, l4.png etc. in work/). Output:

    HERZ. DANK FUR BRIEF. ERWARTE FEILERN
    ANGESAGTEN.
    INNIGEN GRUSS U. KUSS
    STIMMUNG ANHALTEND.
    DEI(N) RASA

## Plaintext (German, U normalised to Ü where needed)

Herz. Dank für Brief. Erwarte Feilern angesagten. Innigen Gruss u. Kuss. Stimmung anhaltend. Dein Rasa.

Line order: lines 1–2 run along the top; "Innigen Gruss u. Kuss" is the indented third line; "Stimmung anhaltend." runs along the bottom edge and the signature stands at the bottom right beside it, so "Stimmung anhaltend." may also be read before the greeting. The order does not change the content.

English: "Heart [= dear heart]. Thanks for the letter. Expecting Feiler as announced. Fond greeting and kiss. Mood lasting [i.e. my good mood continues]. Your Rasa."

Slovak: "Srdce. Vďaka za list. Očakávam Feilera, ako bolo ohlásené. Vrúcny pozdrav a bozk. Nálada trvá. Tvoj/Tvoja Rasa."

## Uncertainties

1. "FEILERN": all seven signs are read (F E I L E R N; the L is the hook-sign, distinct from T). The meaning is not certain: the best reading is the surname Feiler in the old-fashioned accusative with -n ("erwarte Feilern" = I expect Feiler), with "angesagten" telegraphic for "as announced / the announced [one]". It is the one word whose sense is a hypothesis.
2. W in ERWARTE: the sign is an ᚠ-shape (as F) written extremely heavily, perhaps overwritten; W rests on word sense. F in FÜR is also a bold two-branch sign, so F and W may not be distinguished by the writer.
3. Signature: the fourth sign is overwritten (a G-like sign with a caret/Λ-shaped N drawn over and above it); "DEIN" rests on word sense. The name reads R-A-S-A (both A's are the diag sign); it is reported literally — possibly a nickname or a misshaped O (Rosa), not resolved.
4. First sign of line 2 (A of ANGESAGTEN) is faint but visible; first sign of line 4 (S of STIMMUNG) is at the cut card edge, partly lost, its bolt shape still visible.
5. U and Ü share one sign (FÜR, GRUSS, KUSS, STIMMUNG).
6. Steganography check: the picture side has no other writing (inspected work/picture_rest.png); the stamp on the address side is intact, so nothing under it can be seen from the scan (work/stampbox.png). No hidden text was found, but under-stamp writing cannot be excluded.

## Why it is correct

Every sign on the card decodes under one 18-sign key into German that reads: HERZ, DANK FÜR BRIEF, ERWARTE, ANGESAGTEN, INNIGEN GRUSS U. KUSS, STIMMUNG ANHALTEND, DEIN. Repeated signs behave consistently across independent words (G in ANGESAGTEN/INNIGEN/GRUSS/STIMMUNG; D in DANK/ANHALTEND/DEIN; K in DANK/KUSS; A in DANK/ERWARTE/ANGESAGTEN/ANHALTEND), and the content suits a 1900 love/friendship card.

## Credit

Transcription, key reconstruction and decipherment: Claude Opus 5.5 (2026-11-03). No earlier work existed.

## Response to review 1

Verdict ACCEPT, four minor findings, no change to the decoded letters. The reproduction command `python3 -I ciphers/hcp-1194/work/decode.py` was re-run on 2026-11-03: the three SHA-256 checks print OK and the output is unchanged.

1. (17 shapes for 18 letters) Agreed and fixed: the summary line under the key table now says 18 letters with 17 distinct shapes, W being the heavy F shape (homograph F/W resolved by sense), in line with uncertainty 2 and work/key.json (f2, f2bold, f2heavy).
2. (FEILERN ... ANGESAGTEN) Agreed. The seven signs are certain (the L is the hook sign, as in ANHALTEND); the sense "erwarte Feilern angesagten" = "I expect Feiler, as announced" (surname with old accusative -n) is a hypothesis. The report gives the literal reading and marks the interpretation as tentative. It is the only word whose sense is uncertain; the rest reads.
3. (DEIN vs. DEINE) Agreed, added as a note: if Rasa is a woman, "Deine" would be expected; the overwritten fourth sign of the signature (a G-like sign with a Λ-shaped N written over it) may hide a correction. DEIN rests on word sense; RASA is given literally. The translations keep "your" / "Tvoj/Tvoja" neutral.
4. (FUR for FÜR) Agreed: the cipher has one sign for U and Ü; the report shows "für" in the normalised plaintext and keeps FUR in the literal output.

Steganography (human remark relayed in this run about the Jolánka series): checked again on this card. The 5-heller stamp on the address side is intact and cancelled TEPL 17.6.00 (work/stampbox.png); no writing shows around or through it, and the picture side has no writing besides the cipher, the printed series line and the "SuS B." logo. Nothing hidden was found, so the type stays MASC, not "MASC + Steganography"; writing under the stamp cannot be excluded from the scan alone.
