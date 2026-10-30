# hcp-1340 (pc_hcp_21) — solution

Status: complete reading (a few disclosed points below). All work by Claude Opus 5.5, 2026-10-30. No earlier work, no attached solution; no published solution of this card was found in the repo or portal.

## Cipher type and key

Monoalphabetic substitution of German letters by digits and invented signs (word spaces kept, cipher written by the sender; 1905). One sign has two values (d/t). The transcription in `work/transcription.txt` uses a token for each sign:

| Plain | Sign on the card | Token |
|---|---|---|
| a | slash with a dot on the right and a dot or tick on the left (see note) | A |
| b | slash with a dot on the right only | B |
| c | c-shaped (only in ch, sch) | C |
| d, t | 0 | D |
| e | # (two bars crossed by two) | E |
| f | 4 | F |
| g | 8 | G |
| h | 1 | H |
| i | 2 | I |
| k | slashed 0 | K |
| l | 3 | L |
| m | ### (three bars crossed by one long stroke) | M |
| n | 6 | N |
| o / ö | 9 / 9 with two ticks | O, O: |
| p | p-shaped (once) | P |
| r | two ticks ,, | R |
| s | 7 with hook and bar | S |
| u / ü | 5 / 5 with two ticks | U, U: |
| v | v-shaped (once) | V |
| w | W-shaped | W |
| z | looped a-like sign with a foot, only after 0 (twice) | Z |

ä and äu are written with e and eu (literal keltet, breutchen).

Note on a and b: the left mark is the only difference, and it is not always visible. In "war" of adr8 it merges with the tail of the W, and in the corner "war" of the picture side it is only a small kink on the slash. Those two a signs rest on the word as well as on the glyph; the reading is not in doubt.

## Command

From the repo root; it checks the source hashes and prints the whole plaintext twice: first the literal text (key plus a d/t choice, nothing else), then the edited reading, with the only four edits named on its header line:

    python3 -I ciphers/hcp-1340/work/decode.py

## Plaintext (German; reading)

Spelling as ciphered, except for the four edits named below; capitals and part of the punctuation are editorial.

Address side (below the plain date "Den 8. Juni 05."):

> Libste Rosa: Hast du meine Karte bekomen? Wie get es dir? Bist du wider gesund? Süsser Schatz. Ich ha[b]e mich ein bischen er=kältet und bekome einen kleinen Schnupfen. Macht aber nichts. War doch nett, gell süsses Bräutchen. Ob ich nun am Freitag kome, ist noch nicht sicher, da ich noch mals nach Triberg muss.

Picture side, top edge (running round the corner):

> Gell du bist mir nicht böse, weil ich Dinstag so unartig war.

Picture side, under the picture:

> Sei nun fest geküsst von deinem treuen Bubi.

Picture side, right margin (vertical):

> Gruss und Kuss dein Bubi.

The four edits against the literal output are: hae > ha[b]e, keltet > kältet, netz > nett, breutchen > bräutchen. Punctuation between sentences is partly editorial; the card has only ":", "?", ",", "." and "=" where the transcription shows them.

## English

Dearest Rosa: Did you get my card? How are you? Are you well again? Sweet treasure. I have caught a bit of a cold and am getting a little sniffle. It does not matter, though. It was nice after all, wasn't it, sweet little bride. Whether I shall come on Friday now is not yet certain, as I have to go to Triberg once more.
Don't be cross with me, will you, because I was so naughty on Tuesday.
Be kissed hard now by your faithful Bubi.
A greeting and a kiss, your Bubi.

## Slovak

Najdrahšia Rosa: Dostala si moju pohľadnicu? Ako sa máš? Si už zase zdravá? Sladký poklad. Trochu som sa nachladil a dostávam malú nádchu. To však nevadí. Veď bolo pekne, však, sladká nevestička. Či teraz prídem v piatok, ešte nie je isté, lebo musím ešte raz do Tribergu.
Však sa na mňa nehneváš, že som bol v utorok taký nezbedný.
Buď teraz pevne pobozkaná od svojho verného Bubiho.
Pozdrav a bozk, tvoj Bubi.

## Plain (uncoded) text on the card, for context

Date "Den 8. Juni 05." Under the picture, in Kurrent, roughly: "Bitte auch freundliche Grüsse an deine lieben Eltern und an deinen lieben Bruder. Wie geht es deinem lieben Vater? Wünsche gute Besserung. Gruss Euer Hermann"; left margin, vertical, "Frohes Wiedersehen!" (corrected in review; the first reading "Liebes" was wrong). These were read only as context and are not part of the cipher; the word "Eltern" is less certain. A large pen flourish stands above "Fräulein" on the address side; it is not a cipher sign. Address: Fräulein Rosa Duffuer (portal spelling; possibly Duffner), Villa Waldlust, Schönwald, bad. Schwarzw.; postmark Schönwald (Baden) 9.6.05. Bubi is presumably the Hermann of the open text; that is an inference.

## Uncertainties

1. "ha[b]e" (adr5): the card has 1, the a sign, #, so literally "hae". No b sign is present (checked at 9x). Treated as a slip of the pen; no sign restored in the transcription.
2. Z is established by only two occurrences and they do not agree cleanly: Schatz fits z, but "nett" (adr8) is literally 6 # 0 Z, i.e. "netz". I read "nett", with Z there as a final t or a slip. The context forces the word, not the key. A faint separate stroke lies below that sign and has no value I can assign.
3. P and V occur once each, so their values rest on one word (Schnupfen, von).
4. R before Rosa: the two ticks after "Liebste" could belong to the previous word ("Liebster"); the addressee and the feminine "Rosa" settle it as Rosa. R stands where the sender wrote it, with no large gap either way.
5. Spellings as ciphered, not corrected: Libste (no e after the i: the card has 3, 2, b sign, 7, 0, #), bekomen, kome (one M for mm), get (no h), wider, Dinstag, noch mals. M could be read as a sign for mm, but "mir", "mich", "am", "meine" show it is plain m.
6. d/t is one sign; each is resolved by the word, through a closed list in decode.py that can only choose d or t. All 36 choices are visible in that table.
7. "muss" (adr13): the second 7 passes through the printed publisher's heart emblem; its stroke remains visible, and it is read, not restored.
8. Right-margin "Gruss" and "Kuss": no umlaut ticks are visible there, unlike "geküsst". The double 7 is sound in both words; the mark on the second 7 is the ordinary crossbar of the sign.
9. The order of the three picture-side blocks relative to the message is assumed (top line first, the running sense does not depend on it).
10. "Bräutchen" (sweet little bride) is an endearment; whether the pair were engaged is unknown.
11. The 0 in Bräutchen has a heavily inked left side. No bar runs through it, and k would give no word, so it stands as 0.

## Why I believe it is correct

- The key came from recurring words: #26#6 = einen, 62c10 = nicht, 2c1 = ich, 05 = du, 270 = ist; those values then read everything else without any change.
- 347 signs of 23 token types are read; one key, with no sign left unread, gives continuous German fitting a love letter of 1905: the salutation matches the addressee Rosa, Triberg (the Black Forest town, today Triberg im Schwarzwald) lies next to the Schönwald of the address, and the Dienstag/Freitag and date frame fits (8 June 1905 was a Thursday).
- "Bubi" comes out in two separate signatures on the picture side, and the message answers a card already sent in a way the plain family greetings on the same card do not contradict.

## Response to review 1

Verdict REVISE. All six findings accepted; I rechecked each on the reviewer's crops of the hires scan. No sign value and no token of the transcription changed.

1. Libste (major): fixed. The crop `review/work/adr_r01_0.png` shows 3, 2, b sign, 7, 0, #, with no # after the 2. "Liebste" was my restoration and I should not have put it under "spelling as ciphered". The plaintext now reads Libste, the table no longer inserts a letter, and it is listed in uncertainty 5. The sense ("Dearest") is unchanged.
2. decode.py's table: fixed. The table now holds only d/t choices per word and cannot change another letter. The output has two blocks: LITERAL (key plus d/t choice) and EDITED READING, and the four edits (hae, keltet, netz, breutchen) are in a separate named table and repeated in this file. The literal block is now what the key yields, including "netz" and "keltet".
3. Left margin: fixed. `review/work/z_leftmargin.png` plainly shows "Frohes Wiedersehen!". The flourish above "Fräulein" is now mentioned. Neither concerns the cipher.
4. Uncertainty 8: fixed. `review/work/z_gruss.png` shows the crossbar, not a side branch.
5. a/b distinction: fixed. `review/work/z_war.png` and `z_corner.png` confirm it; note added under the key.
6. Blotted 0: fixed. `review/work/z_braeut.png` confirms a heavy left side and no bar; added as uncertainty 11.

Re-run: `python3 -I ciphers/hcp-1340/work/decode.py` passes the hashes and gives 347 signs, 23 token types, as before. The reading is not substantially changed: one word's spelling only, so the card goes to FINAL.
