# SOLUTION hcp-1057 (Zwick to his parents, Aulendorf, 12 July 1917)

Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. No earlier work on this number; no published solution found
(portal status Not solved, no attached transcription or solution). The portal attaches no transcription, so the
transcription is my own (work/transcription.txt), read from the high-resolution scan
work/hires/cpc_1917-07-12_DE_lendorf_DE_Erbenschwang_zwick-01_adr.jpg.

## Cipher type and key

Partial monoalphabetic substitution (MASC) in German Kurrent handwriting: ten letters are replaced by digits,
all other letters are written plain in Kurrent. The key is systematic - the five vowels, then five frequent consonants:

| digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| plain | a | e | i | o | u | l | n | m | r | s |

ä is written as 1 with umlaut dots (n1"chstens). Ligatures ch, ck, ß, St are left plain. The writer is not fully
consistent with s: he writes 0 in ist, alles, nächstens (twice) but a plain Kurrent round s in Bis and Transport.

Register type label: MASC. No steganography: the card went by Feldpost, no stamp was ever affixed (the stamp box is
empty apart from the postmark), and the picture side (Aulendorf, Kirche und neues Schloss) carries no handwriting.

## Command (run from repo root; checks source hashes, prints the decipherment line by line)

    python3 -I ciphers/hcp-1057/work/decode.py

## Full text of the card (German)

Plain part (not enciphered):
Aulendorf, den 12.7.17. Liebe Eltern! Habe Eure werte Postkarte mit Freuden erhalten, meinen besten Dank dafür.

Enciphered part (deciphered):
Hatte gerade nicht mehr die Zeit, mich zu bedanken, da mußte Gefangene ich gleich abholen mit einem Transport.
Bis zur Stunde ist noch alles beim Alten. Sende nächstens einen Brif [one plain word, tentatively "nebst"].

Plain closing: 10000 (possibly 1000) Grüße sendet Euer Sohn M. Zwick.

Sender (plain, top right): Abs. M. Zwick Musketier(?), Ers. Batl. 247, 3. Komp., then two lines largely under the
Aulendorf postmark: "K... [hidden]" and "zur Zeit [hidden] ... Nr.(?) 1".
Address: Feldpost. An Herrn Georg Zwick, Erbenschwang, Post Ingenried b. Schongau (Bay.).

## English translation

Aulendorf, 12 July 1917. Dear parents! I received your kind postcard with joy, my best thanks for it. I just did not
have time any more to thank you, because I had to go and fetch prisoners (of war) at once with a transport. Up to this
hour everything is still the same as ever. I will send a letter soon [nebst?]. 10000 greetings from your son M. Zwick.

## Slovenský preklad

Aulendorf, 12. 7. 1917. Milí rodičia! Vašu milú pohľadnicu som s radosťou dostal, srdečná vďaka za ňu. Práve som už
nemal čas poďakovať sa, lebo som musel hneď ísť s transportom po zajatcov. Až do tejto chvíle je všetko po starom.
Čoskoro pošlem list [nebst?]. 10000 pozdravov posiela Váš syn M. Zwick.

## Uncertainties

1. The short word after B93f (last cipher line) is written in plain Kurrent with no digits and I cannot read it with
   confidence; the stroke sequence fits "nebst" (n, e, b, ſt-ligature) but that is a guess. It is a single word; the
   sentence "Sende nächstens einen Brif" is complete without it.
2. "Brif" (B-9-3-f) is the writer's spelling of Brief (no e written); read from the pixels, not corrected.
3. Calls resting partly on word sense: in 73cht (nicht) the 3 has a nearly closed top, close to an 8; in 82[h]9 (mehr) the h is a loop ligatured under the 2; in S27d2 (Sende) the
   capital is a Kurrent S (long loop with top hook) and the 2 is written with a closed top and a foot, and the 7 is the
   open, crossed form the writer also uses in St57d2 (Stunde); the Kurrent capitals H (Hatte), G (Gefangene), T
   (Transport), St (Stunde), B (Bis, Brif) are Kurrent forms identified by sense.
4. Word order "da mußte Gefangene ich gleich abholen mit einem Transport" is literal; "ab holen" is squeezed in at the
   right between two lines, after "ich gleich". The natural order would be "da mußte ich gleich Gefangene abholen".
5. Sender block: the rank word after the name is probably "Musketier" (letters compressed); the third and fourth
   sender lines are physically hidden under the postmark and are not restored.

## Why this is correct

- The key falls out of the text itself (23727/23728 = einen/einem; b238 = beim; 16620 = alles) and is then used with
  no exceptions over every digit on the card: 92 digit signs, all of which decode into ordinary German words.
- The key is systematic (a e i o u, then l n m r s) - a typical home-made scheme.
- The content fits the card: written from Aulendorf (Württemberg) in July 1917 by a soldier of an Ersatz-Bataillon
  to his parents in Erbenschwang (Bavaria); escorting prisoner-of-war transports was routine duty for such units.

## Response to review 1

Review 1 verdict: ACCEPT, four minor findings. All are disclosure/wording points; no digit, key entry or decoded word
changed. Re-ran `python3 -I ciphers/hcp-1057/work/decode.py` after the edits: all four hashes OK, output unchanged.

1. Closing number (minor) - agreed. On a fresh 2x autocontrast crop of the hires scan (x 100-800, y 1640-1800) I see
   a 1 followed by four loop shapes (closed o, open v-like loop, a squeezed loop, closed o), so the number is most
   likely 10000; the second and third loops run together. Closing now read "10000 (possibly 1000) Grüße".
2. Last plain word (minor) - kept as the single uncertain word. On a 2x crop (x 1000-1450, y 1520-1800) the strokes are
   Kurrent n (two humps), a small e, a tall b stroke and a long-s + t ligature: "nebst" fits every stroke. The most
   natural sense links it to the closing on the next line ("einen Brief, nebst 10000 Grüßen ..."), with the writer
   then starting the closing formula afresh; either way the message is complete without it. Marked uncertain.
3. Sender lines 3-4 (minor) - agreed; they are address details physically covered by the Aulendorf postmark, not
   message text. Stated plainly in the sender line below and in the report.
4. The 3 in 73cht (minor) - agreed; it has a nearly closed top and looks close to an 8. "nmcht" is not a word, so
   3 = i here rests partly on word sense; added to uncertainty 3.

Corrections to the text above: closing read "10000 (possibly 1000) Grüße sendet Euer Sohn M. Zwick"; translations
"10000 greetings" / "10000 pozdravov"; uncertainty 3 extended by the 3 of 73cht.

Steganography check (human note about messages under stamps on postcards): no stamp was ever affixed (Feldpost, the
stamp box holds only the printed frame "21352" and the postmark); the picture side (Aulendorf, Kirche und neues
Schloss, Atelier E. Felle, Isny) has no handwriting; nothing along the edges. Type stays MASC.
