# hcp-1133 — Solution (round 1)

Solver: Claude Opus 5.5, 2026-11-03. No earlier work exists on this number (directory and scans were captured today by the orchestrator). No published solution was found: the portal status is "Not solved" with no solution attached, and a web search for the names on the card (Márthé Ilona, Richter Antal, Temesvár) found nothing.

## The card

- Photo postcard (actress photo, "SARONY"), picture side written over in ink, Hungarian.
- Address side: "Levelező lap. Szépreményű Márthé Ilona kisasszonynak, Helyben, Jr.(?) Eötvös utcza 7 sz." ("To the promising Miss Ilona Márthé, local, Eötvös Street No. 7"). The district abbreviation before "Eötvös" looks like "Jr." or "Gy."; I give it as it stands. The 4-filler Turul stamp (Magyar Kir. Posta) is still on the card. The postmark reads "902 DEC 18" (it is upside down). Nothing can be seen under the stamp, so whether something is hidden there cannot be checked from the scans. No writing was found along the edges or elsewhere in the picture apart from what is listed here.
- Picture side, rotated 90° counter-clockwise: dateline "Kelt Temesvár 1900 év December hó 17 napján". The last digit of the year looks like 0, though the postmark says 1902; I report it as written. Below that come plain Hungarian text in a left column, a right column and a bottom block, with two Morse passages in the right column. It is signed "Üdvözlettel Richter Antal".

## Cipher type and key

**Morse code** written with dots and dashes. A slanted stroke "/" ends every letter, and words are not separated. The key is International Morse plus two accented letters:

- É = `..-..` (the standard Hungarian sign)
- Á = `.-.--`. This is the writer's own sign; the standard one is `.--.-`. It occurs twice (vÁrtam, délutÁn), both times confirmed by the word.
- Ú is written as plain U (lesUjtott).

Register type label: **MASC/Morse**.

## Command

From the repo root:

```
python3 -I ciphers/hcp-1133/work/decode.py
```

The command checks the SHA-256 of all four scans and decodes `work/morse_transcription.txt`, which holds my sign-by-sign transcription of every Morse line on the card. Output:

```
B1 joined: VISELKENÉSELESUJTOTTTELJESEN
B2 joined: REGGELVÁRTAMDÉLUTÁNHOGYÉRTSEMEZTKÉREMIRJONAZONNALAZÉGREKÉREMIRJONEGYLEVELET
```

## Plaintext

Morse passage B1 (right column, after "napján"):
`viselkenése [= viselkedése] lesújtott teljesen`

Morse passage B2 (right column, after "vádat ellenem"):
`reggel vártam délután, hogy értsem ezt. Kérem írjon azonnal, az égre kérem, írjon egy levelet`

The full card in reading order: left column, right column, bottom block. The Morse text is in capitals.

> Kelt Temesvár 1900 év December hó 17 napján.
> Azt kérem egészen nyugodtan elhiheti, hogy nem egyáltalában nem szoktam mondani sem most sem máskor, hogy már nem fogadom szívesen lapját. Én szokva vagyok mindent szívesen fogadni, és hogy beteg voltam, azt a legnagyobb lelki nyugalommal ismétlem.
> [right column] VISELKENÉSE LESUJTOTT TELJESEN, márpedig ezt nem hittem volna. Csoda, hogy nem találtak több vádat ellenem. REGGEL VÁRTAM DÉLUTÁN HOGY ÉRTSEM EZT. KÉREM ÍRJON AZONNAL, AZ ÉGRE KÉREM ÍRJON EGY LEVELET, levelezőlapot azt írta, már nem küld. Szépe(?) nagyon szép.
> De ne méltóztassék hinni, hogy én ily dolgokat egyhamar elfelejtek. Öles betűkkel irotatt [íratott] az bizonyos helyre.
> Üdvözlettel Richter Antal.

**English:** Dated Temesvár, 17 December 1900. I ask you: you may quite calmly believe that I am not at all in the habit of saying, now or at any other time, that I no longer gladly receive your card. I am used to receiving everything gladly, and that I was ill I repeat with the greatest peace of mind. YOUR BEHAVIOUR STRUCK ME DOWN COMPLETELY, and I would never have believed that. It is a wonder they did not find more accusations against me. I WAITED FROM MORNING TO AFTERNOON TO UNDERSTAND THIS. PLEASE WRITE AT ONCE, FOR HEAVEN'S SAKE, PLEASE WRITE A LETTER. As for a postcard, you wrote that you will not send one any more. Its (?) is very pretty. But please do not believe that I forget such things quickly. It was written in huge ("fathom-high") letters onto that certain place. With greetings, Antal Richter.

**Slovensky:** Dané v Temešvári 17. decembra 1900. Prosím, môžete celkom pokojne veriť, že vôbec nemám vo zvyku hovoriť, ani teraz ani inokedy, že už neprijímam Váš lístok rád. Som zvyknutý všetko prijímať rád, a že som bol chorý, to opakujem s najväčším duševným pokojom. VAŠE SPRÁVANIE MA ÚPLNE ZDRVILO, a to by som nikdy nebol veril. Div, že proti mne nenašli viac obvinení. ČAKAL SOM OD RÁNA DO POPOLUDNIA, ABY SOM TOMU POROZUMEL. PROSÍM, NAPÍŠTE HNEĎ, PROBOHA PROSÍM, NAPÍŠTE LIST. Korešpondenčný lístok vraj už nepošlete. Jeho (?) je veľmi pekný. Ale neráčte si myslieť, že také veci rýchlo zabúdam. Bolo to napísané obrovskými písmenami na isté miesto. S pozdravom Antal Richter.

## Uncertainties

1. **B1 "viselkenése" vs "viselkedése".** The pixels show `-.` (N) where the word needs `-..` (D). The dash and the single dot are clear, with nothing hidden, so this is a writer's slip of one dot. I report N as read and D as the intended letter.
2. **Faint dashes.** Seven marks consist of a faint thin tail ending in a dot or blob, the pen apparently starting dry. They are in B2 line 7 (the middle sign of the final R, kéR-em), line 9 (the dash of the first A and the first sign of Z), line 10 (first sign of N), line 11 (third sign of É and the start of G) and line 12 (the middle of R). I read them as dashes. Every one of them is confirmed by the word (kéRem, Azonnal, aZonnal, Nal, É, G, R). Read as dots, they would give no words. (List completed after review 1, finding 2.)
3. **H, S and Z.** In B2 line 5 (H `....`) and line 6 (S `...`), one dot is slightly elongated but far shorter than this writer's dashes. In B2 line 7 the fourth mark of Z `--..` (ezt) is a short blob about twice a dot and half a dash; read as a dash it would give Q (`--.-`, "eqt"). These three calls rest partly on word sense ("hogy", "értsem", "ezt"). (Z added after review 1, finding 1.)
4. **Word division and punctuation** in the Morse text are mine, because the writer does not separate words.
5. **Plain text, one-word points:** "irotatt" (most likely a slip for "íratott", "was written"), "Szépe(?)" (possibly "Szép-e?", "is it pretty?"), "szívesen" (the long-s and z ligature makes it look like "kivessem" in the left column), and "Jr./Gy." in the address (possibly an abbreviation of a Temesvár district such as Józsefváros; hypothesis only). Each is a single word and the clause around it reads.
6. **Year** "1900" in the dateline against the postmark 1902.
7. **The area under the stamp** cannot be inspected from the scans.

## Why I believe it is correct

- Every Morse sign on the card is transcribed (3 + 14 lines), and all of them decode under one key (International Morse plus É and the writer's Á). There are no unknown groups. The output is continuous Hungarian of the period that fits the plain text around it: the writer complains of being falsely accused, and the hidden lines carry the emotional core ("your behaviour struck me down completely ... for heaven's sake, write a letter at once").
- The Morse passages run on grammatically from the plain sentences ("...nem hittem volna" and "írjon egy levelet, levelezőlapot azt írta...").
- The writer's nonstandard Á is consistent in both occurrences.

## Response to review 1

Verdict ACCEPT, five minor findings. The decoded text is unchanged; `python3 -I ciphers/hcp-1133/work/decode.py` was re-run after the edits and still prints all four SHA-256 checks OK and the same B1/B2 strings.

1. **Z of "ezt" rests partly on word sense.** Agreed. Uncertainty point 3 now lists it together with H and S, and states that a dash reading would give Q ("eqt").
2. **Faint-dash list incomplete.** Agreed. Point 2 now lists all seven such marks, adding the middle sign of R at the end of B2 line 7 and the dash of A at the start of B2 line 9. Both are confirmed by the words; the reading does not change.
3. **Slovak translation of "az bizonyos helyre".** Fixed to "na isté miesto"; the English now says "onto that certain place", closer to the sublative -re.
4. **Address abbreviation "Jr.".** Added the reviewer's Józsefváros idea to point 5 as a hypothesis only; the abbreviation stays unexpanded.
5. **Steganography.** No change. The stamp is still attached, so the area under it cannot be inspected (point 7); nothing hidden is visible in the picture or along the edges. The card is not part of the Jolánka series (different writer, Temesvár, recipient Márthé Ilona), so the "MASC + Steganography" label reported for that series does not apply here. The type stays MASC/Morse.
