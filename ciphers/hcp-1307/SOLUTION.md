# HCP1307 — Feri to Jolánka Tóth: her card came late, please write on Sunday

**Status: complete reading of all ciphertext (591 written signs). One sign is hidden and restored; three further letters or words are supplied by the editor (all listed below). Review 1 addressed.** Claude Opus 5.5, 2026-10-30.

Credit: reading and decoding by Claude Opus 5.5. There was no earlier work on this number. The key was not invented here: it is the Jolánka-family key of finished cards HCP1216, 1212, 1213, 1217, 1218, 1243 and 1301, whose earlier work was done by the OpenAI GPT solver and Claude Opus 5.5. The portal shows status *Not solved* with no attached transcription or solution; no published solution of this card turned up. No external plaintext was used.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (Jolánka postcard family). Accents are marks over the base sign. No nulls, no homophones.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section-mark S | k | F-shape | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three strokes | m | gamma | t |
| long stroke, tick at upper left | d | two strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + short stroke at right (one sign for h and p) | h / p | low descender (after g: gy) | y |
| zigzag with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | | | | |

Marks: acute tick for á, é, í, ó, ú; two dots or ticks for ö, ü, and also for ő (not told apart in this hand). Most acutes are not written.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1307/work/decode.py
```

It checks the SHA-256 of both `source/` scans and both `work/hires/` originals, decodes `work/ledger.txt` (one token per written sign, a manual reading, not OCR) with the key, prints the literal rows, then prints the normalized text `work/normalized.txt`. The normalization is editorial and is not computed from the ledger.

## Literal decipherment (as printed by the command)

```
01 szereretetédesjolan            14 korérziazemberhogy
02 kámvarvavártsorait             15 menyireszeretemma
03 megkahtammitnagyon             16 gátédesemmérazagondo
04 széhenköszönökédesem           17 latiselkeseritetanyira
05 ojannehezenmégnemvartam        18 hogynemvoltkedvemsem
06 soraitmintmostédesem           19 mihezistenmentsarra
07 ugyjajtszivemangyalom          20 nemismerekgondolnide
08 hogymégkedensemkahtam          21 magátelvesztenémbiz
09 megsoraitmintrende             22 toshalálomlennekérem
10 senmindjartarragondol          23 magátédesemnemkiva
11 tamédesemhogymeghara           24 noktöbetcsaklegalabb
12 gudothogynemmentem             25 egylahotitjonvasárnahmerthatudnamijennehezen
13 leigazanédesemcsakijen         26 váromensoraiteztakérésemteljsitenifogja
in the stamp box: csokolo[m] / szamta / lanszor / szeretö / kedvese / feri
```

Rows 25 and 26 run on along the bottom edge of the card, below the address.

## Hungarian (normalized)

Szeretett édes Jolánkám! Várva várt sorait megkaptam, mit nagyon szépen köszönök, édesem. Olyan nehezen még nem vártam sorait, mint most, édesem, úgy fájt szívem, angyalom, hogy még kedden sem kaptam meg sorait, mint rendesen. Mindjárt arra gondoltam, édesem, hogy megharagudott, hogy nem mentem le. Igazán, édesem, csak ilyenkor érzi az ember, hogy mennyire szeretem magát, édesem, mer[t] az a gondolat is elkeserített annyira, hogy nem volt kedvem semmihez. Isten ments, arra nem is merek gondolni, de [ha] magát elveszteném, biztos halálom lenne. Kérem magát, édesem, nem kívánok többet, csak legalább egy lapot írjon vasárnap, mert ha tudná, milyen nehezen várom én sorait. Ezt a kérésem telj[e]síteni fogja.

Under the stamp: Csókolo[m] számtalanszor. Szerető kedvese, Feri.

## English

My beloved sweet Jolánka! I have received your long-awaited lines, for which I thank you very much, my darling. I have never waited for your lines as anxiously as now, my darling; my heart ached so, my angel, that I had still not received your lines by Tuesday, as I usually do. I thought at once, my darling, that you were angry because I did not go down. Truly, my darling, only at such times does one feel how much I love you, my darling, for even that thought embittered me so much that I had no heart for anything. God forbid, I dare not even think of it, but [if] I were to lose you, it would surely be my death. I ask you, my darling, I wish for nothing more, only at least to write me a card on Sunday, for if you knew how anxiously I wait for your lines. This request of mine you will fulfil.
Under the stamp: I kiss you countless times. Your loving sweetheart, Feri.

## Slovak

Moja milovaná sladká Jolánka! Dlho očakávané riadky som dostal, za čo veľmi pekne ďakujem, drahá. Ešte nikdy som na Vaše riadky nečakal tak úzkostlivo ako teraz, drahá, tak ma bolelo srdce, anjel môj, že som Vaše riadky nedostal ani v utorok ako obyčajne. Hneď som si pomyslel, drahá, že sa hneváte, že som neprišiel dolu. Naozaj, drahá, len v takej chvíli človek cíti, ako veľmi Vás milujem, drahá, lebo aj tá myšlienka ma tak roztrpčila, že som nemal chuť do ničoho. Chráň Boh, na to sa ani neodvážim pomyslieť, ale [keby] som Vás stratil, bola by to moja istá smrť. Prosím Vás, drahá, nežiadam viac, len aby ste mi aspoň napísali lístok v nedeľu, lebo keby ste vedeli, ako ťažko čakám na Vaše riadky. Túto moju prosbu splníte.
Pod známkou: Bozkávam Vás nespočetnekrát. Váš milujúci milý, Feri.

## Uncertainties

Restored (one sign, the only one that is physically hidden):

1. **Stamp box, row 1, final m of *csókolom*.** After the last o only one stroke is visible, at the torn edge of the stamp paper; the rest is hidden. Ledger token `3^`, shown as [m].

Supplied by the editor (not on the card, and nothing is hidden there; these are the writer's omissions, so they have no ledger token):

- **[e] in *telj[e]síteni*, row 26.** The card has the inverted T followed directly by the right bowl, with clean paper between them: literal *teljsiteni*.
- **[t] in *mer[t]*, row 16.** Literal *mér*, with a clear tick on the e. Colloquial *mér* "why" does not fit: the clause explains the preceding statement (*csak ilyenkor érzi az ember ...*) and there is no question. The causal sense is the better reading. The writer spells *mert* in full in row 25; HCP1216 has *mer*.
- **[ha], row 21.** See item 6.

Calls that rest on word sense, not on a clean sign:

2. **Row 1, last sign of *szeretet*.** A faint gamma with a small mark, close to the F-shape. Read t. The word as written is literally *szereretet*, a repeated *-re-* and a single t, normalized *szeretett*. The fifth sign, the e of the repeated *-re-*, is much fainter than its neighbours and may be a wiped slip; the normalized word is the same either way.
3. **Row 2, r of *várt*.** A dark F written over an earlier sign. The chevron's long leg still runs into it from the left, so the writer began a v and corrected it to r; one short low bar under the F has no value. The acute above the a of *vá-* was first taken for a comma at the end of row 1.
4. **Row 7, *fájt*.** Both signs of *jajt* are clearly the inverted T (j); neither is the upright cross of *fogja* (row 26). Literal *úgy jajt szívem* gives no verb, so *fájt* is an emendation of a writer's slip. If j is kept, the sense of this clause is lost, not the rest of the card.
5. **Row 19, e of *mihez*.** It looks two-barred with a smudge, so a is not excluded by shape; *mihez* decides.
6. **Row 21, t of *magát*.** The sign lies in a brown smear and could be gamma or F. Read t: *magát elveszteném* makes sense and *magár* does not. **[ha]** before it is my supply; the card reads only *de magát elveszteném*.
7. **Row 25, *írjon*.** The sign after i is a clear gamma (t), literal *itjon*. Normalized *írjon*, a writer's slip for r. The context (*egy lapot ... vasárnap*) leaves no other word.
8. **Homograph h/p.** One sign serves both, as across the family: p in *kaptam, szépen, lapot, vasárnap*; h in *nehezen, hogy, megharagudott, mihez, halálom, ha*. Each choice rests on the word. In row 5 *nehezen* the long stroke lies under a dark blot and only the tick is clean, so word sense decides it; the same word is clean in row 25. In *megharagudott* and *halálom* the short stroke is unusually long, near a two-stroke n; *menaragudott* and *nalálom* are not words.
9. **g and k.** Zigzag (g) and section-mark (k) can look alike, most of all in the stamp box (*csókolom*, *kedvese*), where the k is small. Word sense confirms them there.
10. **Row 26, *én*.** Literal *en*; read as the emphatic pronoun. *e[z]* is not excluded by sense but would need an omitted letter.
11. **ő of *szerető*.** The two ticks could equally be ö marks; the word decides.

Writer's spellings normalized: *ojan* → olyan, *ijen* → ilyen, *mijen* → milyen, *keden* → kedden, *menyire* → mennyire, *anyira* → annyira, *elkeseritet* → elkeserített, *megharagudot* → megharagudott, *töbet* → többet, *mér* → mer[t], *teljsiteni* → telj[e]síteni. Most accents are supplied; the ledger marks only those seen. Word division is mine; the card has none.

Not cipher, not part of the decipherment:

- Address in clear: *Tóth Jolánka urleányok(?) Jász Árokszállás*; the line after the name reads literally like *urleanyok*, presumably for *úrleánynak*.
- One handwritten word in clear, above the Rákospalota cancellation, begins *Szép…*; I could not read the rest with confidence (it runs through the cancel).
- Printed on the picture side: a four-line verse beginning "Én édes párom", with the title "Édes párom szállj velem…".
- The date is not legible. The round cancel is almost blank; the portal gives Date Unknown.

## Why it is correct

- The family key, taken over unchanged, gives Hungarian for all 591 signs in the 26 main rows and 6 stamp rows. No sign is left without a value and no key change was needed.
- Repeated words decode identically: *édesem* ×6, *hogy* ×5, *sorait* ×4, *magát* ×3, *mint* ×2.
- The text is continuous, coherent love-letter prose with the formal address of the family (*magát, írjon, tudná*) and the writer's typical *j* for *ly* (*ojan*, as on HCP1216).
- Context agrees: signature Feri and closing formula *csókolom számtalanszor ... kedvese, Feri* as on HCP1216; Rákospalota cancel and Jászárokszállás address as on that card. The sender identity is an inference from these parallels.
- The checks are not independent of sense: the same reader made the ledger knowing the key and the emerging text. The reviewer should re-read the items above on the pixels.

## Response to review 1

Verdict REVISE, all four findings accepted after checking each on the pixels (`review/work/crops/t.png`, `r26a.png`, `r1a.png`, `r5.png`; my own crop `work/crops/rev-r25s.png`). The reading of the card does not change; only the record of what is written.

1. **major, phantom e in row 26: fixed.** At 6x, the inverted T runs directly into the right bowl with clean paper between them. Token deleted from `work/ledger.txt`. Literal now *teljsiteni*, normalized *telj[e]síteni* in `work/normalized.txt` and above. Count corrected from 592 to 591 in this file; `decode.py` recounts by itself. Listed under Uncertainties, and in the writer's spellings.
2. **minor, acute of *várom* in row 26: fixed.** Row 26 now starts `V =' R`, literal *várom*. Checked before accepting it, because the stroke lies among the signs of row 25, between the g and the y of *egy*: it could have been part of them. It is not: in *hogy* (for example row 14) the same two signs stand together with no such stroke, and the stroke sits directly above the a. It is rather longer than this writer's usual acute, so the call is good but not perfect; it affects no word.
3. **minor, "one restored sign" understated: fixed.** Header and Uncertainties now separate the one hidden sign ([m]) from the editor's supplied items ([e], [t], [ha]). *Mér* "why" is ruled out in a line.
4. **minor, two soft spots: fixed.** The faint fifth sign of row 1 is noted in item 2, and the blotted h/p of row 5 *nehezen* in item 8.

Verification: `python3 -I ciphers/hcp-1307/work/decode.py` re-run after the fixes, all 4 hashes OK, 591 signs, and its output agrees with the literal block and the normalized text above. The reviewer's independent `review/work/mine.txt` agrees with the corrected ledger (result recorded in NOTES.md).
