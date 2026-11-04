# HCP 1057 (cpc_1917-07-12_DE_lendorf_DE_Erbenschwang_zwick-01): a soldier's digit-cipher postcard from Aulendorf, 1917

Human solver: Tomáš Pavuk

**Status: deciphered in full (92 of 92 digit signs); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1057 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1057), portal name cpc_1917-07-12_DE_lendorf_DE_Erbenschwang_zwick-01, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Georg Zwick, with no transcription or solution attached. The portal links the HistoCrypt article on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166) but gives no reading of this card, and no published solution of it was found.

The picture side is a coloured view "Aulendorf, Kirche und neues Schloss" (Atelier E. Felle, Isny); the address side is printed as Künstlerkarte "Mondnacht", 1910, Verlag Rud. Schilling, Aulendorf. The whole message is written in pencil in German Kurrent on the left half of the address side.

The card went by Feldpost (military mail, no stamp) and was cancelled AULENDORF. Sender: "Abs. M. Zwick, Musketier(?), Ers. Batl. 247, 3. Komp." (Ersatz-Bataillon 247, a Württemberg reserve battalion; Aulendorf is in Württemberg); two further sender lines are physically covered by the postmark. Address: "Feldpost. An Herrn Georg Zwick, Erbenschwang, Post Ingenried b. Schongau (Bay.)" - the writer's father in Upper Bavaria. The card is dated 12 July 1917.

It belongs to a small family of cards from the same writer to his parents (HCP 910, 1056 and 1057), which use the same digit key.

![Address side with the message (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: Aulendorf, church and new castle; no writing (source/picture-large.jpg)](../source/picture-large.jpg)

**Hidden writing.** Many postcards of the period hide a message under the stamp or in the picture. This card has no stamp at all (Feldpost): the stamp box shows only its printed dotted frame with the number 21352 and the postmark. The picture side carries no handwriting, and nothing is written along the edges. The cipher is therefore only in the message itself.

## Method

The transcription is manual, read from the high-resolution scan of the address side with enlarged crops. The message begins and ends in plain Kurrent; between them, ten lines mix digits with ordinary Kurrent letters. Only some letters are enciphered.

The key falls out of pattern words. The groups 23727 and 23728 have the shapes ABCAC and ABCAD, which fit "einen" and "einem": 2 = e, 3 = i, 7 = n, 8 = m. Then d32 = die, b238 = beim, 16620 = alles (1 = a, 6 = l, 0 = s), z59 = zur (5 = u, 9 = r), 74ch = noch (4 = o), and T917sp49t = Transport confirms them all. The resulting key was applied to every digit on the card, with no exception and no unused or conflicting digit.

The reviewer built the key independently from the same pattern words, applied it to its own reading of all ten cipher lines, and got the same key and the same German text. The sister card HCP 1056 reached exactly the same key independently.

## Key

Partial monoalphabetic substitution: the five vowels, then five frequent consonants, are replaced by digits; every other letter is written plain.

| digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| plain | a | e | i | o | u | l | n | m | r | s |

ä is written as 1 with umlaut dots. The ligatures ch, ck, ß and St are left plain. The writer is not consistent with s: he writes 0 in ist, alles and nächstens, but a plain Kurrent s in Bis and Transport.

## Plaintext

Cipher lines as transcribed (Latin letters are the plain Kurrent letters; 1" is the dotted 1):

```text
H1tt2 g291d2 73cht              Hatte gerade nicht
82[h]9 d32 z23t 83ch z5 b2-     mehr die Zeit mich zu be-
d17k27, d1 85ßt2                danken, da mußte
G2f17g272 3ch g623ch            Gefangene ich gleich
1b h4627                        ab holen
83t 23728 T917sp49t.            mit einem Transport.
B3s z59 St57d2 30t 74ch         Bis zur Stunde ist noch
16620 b238 16t27.               alles beim Alten.
S27d2 71"ch0t270                Sende nächstens
23727 B93f                      einen Brif
```

The full card in German (plain parts and deciphered part; the bold part is the enciphered section):

Aulendorf, den 12.7.17. Liebe Eltern! Habe Eure werte Postkarte mit Freuden erhalten, meinen besten Dank dafür. **Hatte gerade nicht mehr die Zeit, mich zu bedanken, da mußte Gefangene ich gleich abholen mit einem Transport. Bis zur Stunde ist noch alles beim Alten. Sende nächstens einen Brif** [nebst?]. 10000 (possibly 1000) Grüße sendet Euer Sohn M. Zwick.

**English.** Aulendorf, 12 July 1917. Dear parents! I received your kind postcard with joy, my best thanks for it. I just did not have time any more to thank you, because I had to go at once and fetch prisoners (of war) with a transport. Up to this hour everything is still the same as ever. I will send a letter soon [nebst?]. 10000 greetings from your son M. Zwick.

**Slovak.** Aulendorf, 12. 7. 1917. Milí rodičia! Vašu milú pohľadnicu som s radosťou dostal, srdečná vďaka za ňu. Práve som už nemal čas poďakovať sa, lebo som musel hneď ísť s transportom po zajatcov. Až do tejto chvíle je všetko po starom. Čoskoro pošlem list [nebst?]. 10000 pozdravov posiela Váš syn M. Zwick.

## Uncertainties

1. The single plain word after "Brif" is unclear. Its strokes fit Kurrent "nebst" (n, e, b, long s with t), which most naturally joins the closing ("a letter, along with 10000 greetings ..."), but this is a guess. The message is complete without it.
2. The closing number: a 1 followed by four loops, most likely 10000; two loops run together, so 1000 is possible.
3. "Brif" is the writer's spelling of Brief and is kept as written.
4. Calls resting partly on word sense: the 3 of 73cht (nicht), whose nearly closed top resembles an 8; the h of mehr, a loop ligatured under the 2 of 82[h]9; the Kurrent capitals H, G, T, St, B and S in Hatte, Gefangene, Transport, Stunde, Bis, Brif and Sende.
5. The word order "da mußte Gefangene ich gleich abholen" is literal (dialect-coloured); "ab holen" is squeezed in at the right between two lines.
6. Sender block: the rank word is probably "Musketier"; the third and fourth sender lines lie under the postmark and are not read. They are address details, not message text.

## Why the reading is right

- The key is derived from the text itself and then applied without exception to all 92 digit signs; every one decodes into an ordinary German word.
- The key is systematic (a e i o u, then l n m r s), a typical home-made scheme, and is the same on the sister cards from the same writer.
- The content fits the card: a soldier of a Württemberg reserve battalion, stationed at Aulendorf in July 1917, writes to his parents that he was sent to escort a transport of prisoners of war - routine duty for such units.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the reproduction script, decoded the card with its own script and its own key derivation, checked every cipher line against the high-resolution scan, and checked the stamp box and picture side for hidden writing. Verdict: **ACCEPT**, with four minor findings:

1. The closing number looks like 10000 rather than 1000 - accepted; now read "10000 (possibly 1000)".
2. The last plain word ("nebst") stays a single marked guess - kept as uncertain.
3. The two sender lines under the postmark should be described plainly as hidden address details - done.
4. The 3 in "nicht" looks almost like an 8 and rests partly on word sense - added to the uncertainties.

No digit, key entry or decoded word changed.

## Credits

Transcription, key reconstruction and decipherment by Claude Opus 5.5 (Anthropic); independent review by a separate Claude Opus 5.5 agent. Reproduction: `python3 -I ciphers/hcp-1057/work/decode.py` from the repository root.
