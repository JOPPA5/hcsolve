REVISE

# Review 1 of HCP1214 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading of the card stands: key, cipher type, 18 rows, a break-up note signed Feri. One letter in the salutation is not on the card and must be removed (finding 1). The other findings are disclosure and translation fixes. After they are made, the card counts as complete: the only sense-based spot is two signs of one word (fájdalom), and the rest reads.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1214/work/decode.py`: all four SHA-256 hashes OK; output is identical to the literal block in SOLUTION.md, and the normalized text matches.
- **Independent transcription and decode.** `review/work/my_decode.py` is my own sign-class transcription (237 signs including 2 blots and the overwritten sign), keyed from the HCP1216 table, made from `work/hires/*adr.jpg` and diffed against the ledger. There is 1 row difference: row 14 second d (finding 5). The ledger's row 1 last sign is the other disagreement, since I did not count it as a sign (finding 1). Every other sign agrees.
- **Key coverage.** All signs fall in the HCP1216 classes except the upright T at row 10 end, which the solver discloses. No key letter was changed for this card.
- **Pixels.** I checked rows 1 to 18 on the solver's deskewed bands, then on my own enlargements of the hires scan (`review/work/m1.png` to `m5.png`, `umlauts.png`, `zoom.py`, `zoom2.py`, `diaeresis.py`). That covered every disclosed point (rows 1, 6, 7, 10, 11, 13, 14, 15), row 2, row 12, row 14 to 17 and the signature.
- **Restorations confirmed.** Row 6 z of *azt*: only an X outline shows out of the blot, and the a's top bar and a blob for the lower bar are visible; correctly disclosed. Row 15 a of *tudat*: one bar above the blot; disclosed. Row 17 t of *isten*: clear gamma. Row 18 *Feri*: f r i all clear, with the i dot present. *kedvesse*: two same-facing bowls, so ss rather than cs, as the solver reads it.
- **Other side and address.** Picture side: only no. 2541 and the collection stamp. Address: Szépreményű Tóth Jolánka kisasszonynak, Helyben, as claimed. The postmark is not legible on my 4x crop either; only arc fragments show.
- **Language and context.** Period Hungarian with this writer's habits (single consonants, dropped letters, as on HCP1216). *nehezemre esik*, *Ön* address and *Isten vele* match the family. Portal: Not solved, no attachment. No published solution is used.

## Findings

1. **major: row 1 "Jolánkám": the final m is not supported; the marks are the diaeresis of ö in row 2.** Evidence: `review/work/m5.png` (top) and `review/work/umlauts.png` (panel 1 row 2, panel 4 row 12).
   - The marks at row 1 end are exactly two strokes, a longer one and a shorter one with a blob, not three. SOLUTION says "two or three"; a two-stroke sign would be n, and only the family habit gives m.
   - They sit low, directly above the o of *köz-* in row 2, and that o has no other marks. The ledger token `O:` in row 2 has no other dots to rest on, so the ledger spends the same two strokes twice (M? and the dots of O:).
   - The row 12 ö carries the same pair of ticks in the same arrangement, long then short with a blob, up and right of the loop. Row 2's pair is somewhat larger (about 45 against 30 hires pixels). The other umlauts on the card are round dots (rows 7, 10).
   - Fix: drop `M?` from ledger row 1, read **Kedves Jolánka!**, and update the literal block, normalized text and uncertainty 4. The English and Slovak already read "Jolánka". Note the writer's Jolánkám on sisters as a comparison only. If the solver keeps a letter here it must say why row 2 ö then has no marks; "m by the family" is a sister-card completion, not a reading.

2. **minor: "ha fájdalom" is probably not "loose syntax", and the translation should change.** *fájdalom* is also, to my knowledge, a literary interjection, "alas". This gives an ordinary sentence running over the row break: *mily nehezemre esik becses házukat kerülni, ha, fájdalom, meg kell tennem*, "how hard it is for me to keep away from your esteemed house when, alas, I must do so". The semicolon and "painful though it is" split one sentence in two. Offer this as the preferred reading, with the Slovak changed to match (e.g. "keď to, žiaľ, musím urobiť"). The sign calls stay sense-based: the T at row 10 end has its bar on top and the row 11 first sign is stem + right tick, exactly the h/p shape (`m2.png`). The disclosure of those two signs in uncertainty 1 is honest and correct, and should stay. It is what keeps this from being a stronger claim. Interjection sense is my own language knowledge, not checked against a period source.

3. **minor: row 10 "ha": a third stroke under the a is undisclosed.** `m5.png` (bottom): the two bars of the a are followed, about twice the bar spacing lower, by a third short stroke at the same x; it does not belong to row 11's e or g. So the sign can be taken as an uneven three-bar e (*he fá...*). a is chosen by sense. Add it to the uncertainties; the reading does not change.

4. **minor: row 7 overwritten sign is described too confidently.** `m5.png` (middle): a thick diagonal stem is written through an 8-like form, and to the right stands one short stroke with a small notch, where the normal h is stem + separate tick. Solver: "has no value and *hogy* follows complete". The heavy stem may be the h stem and the right stroke its tick, so the ledger's separate `#` then `H` may split one corrected sign in two. Say that either way the word is *hogy*.

5. **minor: row 14 second d is over-flagged.** SOLUTION item 2 and ledger `D!` say it has the h/p shape. On `m3.png` it has its tick on the left of the stem, which is the d arrangement HCP1216 describes, as opposed to h with its tick on the right. Read it as plain d; only row 11 first sign is a true h/p-shaped d. Remove `D!` from row 14.

6. **minor: key table does not match the ledger's tokens.** The ledger uses `GY` (rows 3, 7, 15, 16) as a joined unit, and row 13 uses `G Y`, but the table in SOLUTION lists no gy; HCP1216 lists gy and cs. Add gy to the table or split the tokens consistently, and state that `C )` is written as two bowls. This does not affect the plaintext.

## Not findings, checked and agreed

- Uncertainties 3, 5, 6, 8, 9, 10 and 11 are correct and adequately disclosed.
- *kiutasitnak*, *hazok-*, *mij*, *sziböl* and *becse* are transcribed as written and normalized openly.
- The second person as subject of *megtört* is an interpretation and is labelled as one.
- Row 13 second sign: thick and z-like, with a separate dot above; i by the dot, as disclosed.

## Could not verify

- Identity of this Feri with the Feri of HCP1212/1213/1216 (shared key and addressee only), and the place behind "Helyben".
- The date: the postmark is illegible. The 5 fillér stamp could bound it, but I did not research this.
- Faint speck groups between rows 16 and 17 above the z of *szívet*: I take them as paper marks, not signs, but I could not prove it.
- Whether marks under the stamp exist: the stamp is in place, and nothing shows at its edges.
