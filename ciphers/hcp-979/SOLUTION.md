# hcp-979 – Solution (round 1)

Card: HC Portal cryptogram 979, `cpc_1909-09-10_DE_Dortmund_DE_Hier_fritzlehmann-08`, T. Schrödel collection.
Address side: Germania 5 Pf stamp (still affixed), postmark FREIBURG (SCHLESIEN) 10.9.09 1-2N (the "Dortmund" in the portal file name
is not what the postmark shows); addressed in plain Kurrent pencil "Herrn Fritz Lehmann, Hier", followed by a street line and a house number that are
partly covered by the collection stamp and are left unread (not part of the cipher). The message is a 10-line pencil block of
dotted numbers written sideways on the left half. Picture side: printed photo card "Gretchen" with the caption "Wie sollte mir die Kette
stehen?" (publisher number 4034-2, same Faust "Gretchen" series as hcp-1045, 4034-6); no handwriting on it or along its edges. The stamp
is still on the card, so whatever might be under it cannot be seen; nothing protrudes from under it.
Portal status: Not solved; no transcription or solution attached. Transcription and decipherment are my own (Claude Opus 5.5,
2026-11-03) from the high-resolution scan in work/hires/. No earlier work existed in this directory. No web search for a published
solution was made. The key is the one established on the Lehmann sister cards hcp-1134, hcp-1113, hcp-1050 (accepted in review and now FINAL) and
hcp-1045 (accepted in review), all to the same recipient; I transferred it and checked it against every number here.

## Cipher type and key

Number substitution (MASC), German. The 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |

Dots separate numbers, dashes separate words. A dark cross or slash stroke over the first number of a word (12 L of Lieber, 7 F of Fritz
and Fieber, 9 H of Heut twice, 2 A of Abend, 19 S of Sollte) marks a capital, as on hcp-1045 and hcp-1113; it does not change the letter.
ß is written SZ. The final "1/2 VIII" (a fraction I over II, then Roman VIII with an overbar) is written plainly, not enciphered.
Numbers used: 2 3 4 5 6 7 8 9 10 11 12 14 15 18 19 20 21 23 26 – all decode under the one table.

## Transcription (work/transcription.txt; x = capital stroke)

```
12x.10.6.3.6.18 - 7x.18.10.20.26 - !
9x.6.21.20 - 8.6.9.20 - 6.19 -
23.10.6.5.6.18 - 3.6.19.19.6.18
23.6.10.19.26 - 2.3.6.18 14.15.4.9 -
14.10.4.9.20 - 23.10.6 - 6.19 - 9x.6.21.20 -
2x.3.6.14.5 - 19.6.10.14 - 23.10.18.5 -
8.6.19.20.6.18.14 - 9.2.20.20.6 -
10.4.9 - 19.20.2.18.11.6 -
7x.10.6.3.6.18 - 19x.15.12.12.20.6 -
10.4.9 - 14.10.4.9.20 - [1/2 VIII]
```

## Command (from repo root)

```
python3 -I ciphers/hcp-979/work/decode.py
```

It checks the SHA-256 of both source scans and both hi-res originals, then decodes work/transcription.txt with the key above.

## Plaintext

As decoded:
LIEBER FRITZ ! HEUT GEHT ES WIEDER BESSER WEISZ ABER NOCH NICHT WIE ES HEUT ABEND SEIN WIRD GESTERN HATTE ICH STARKE FIEBER SOLLTE
ICH NICHT 1/2 VIII

German, normalised (punctuation mine): "Lieber Fritz! Heut geht es wieder besser, weiß aber noch nicht, wie es heut Abend sein wird.
Gestern hatte ich starke[s] Fieber. Sollte ich nicht ½ 8 [Uhr da sein, ...]"

English: "Dear Fritz! Today it is going better again, but I don't know yet how it will be this evening. Yesterday I had a high fever.
Should I not [be there] at half past seven [...]" – i.e. "if I am not there at 7.30, that is why".

Slovak: "Milý Fritz! Dnes je to už zase lepšie, ale ešte neviem, ako to bude dnes večer. Včera som mal(a) vysokú horúčku. Keby som
nebol(a) o pol ôsmej [tam] ..."

## Uncertainties

1. The ending "SOLLTE ICH NICHT ½ VIII" is elliptical: every sign is read, but the writer leaves out the verb (most likely "da sein"
   / "kommen"), so the clause is an unfinished conditional ("should I not ... at half past seven"). The completion in brackets is my
   interpretation, not on the card. There is no signature. "½ VIII" is read as halb acht = 7.30 (German "halb 8"); the overbar on VIII
   is only a Roman-numeral bar.
2. 5 versus 8 in this hand: the 5 (D of WIEDER, ABEND, WIRD) is an open S-shape with a detached top flag; the 8 (G of GEHT, GESTERN)
   has a closed lower loop. The two 8s are distinct on the pixels (work/crops/d_vs_g.png), and DEHT / DESTERN would not be words, so
   word sense agrees.
3. 18 versus 19: the first number of STARKE (line 8) and of SOLLTE (line 9, with a capital cross through the 1) have the 9-form
   (closed top loop, straight tail), unlike the S-shaped 8 in 2.18 (R) of the same word; 18 would give RTARKE / ROLLTE. Pixel reading,
   supported by word sense.
4. The word-dash after FIEBER is written as a small "+" (dash with a stroke); taken as a word separator.
5. Writer's grammar kept: STARKE FIEBER (standard "starkes Fieber"), HEUT (= heute), WEISZ (ß as SZ).
6. Plain address: the street line and the number at the bottom right are partly covered by the collection stamp and are left
   unread; they are not part of the message.
7. Under the stamp: not inspectable (stamp still affixed); no writing protrudes.
8. End of row 5: the last number of the second HEUT (9x.6.21.20) runs into the printed blue "Briefkaart" line; the 2 of 20 is
   visible, the 0 is largely covered by the print (review/work/l5end.png). 20 = T is restored by word sense (HEUT) and by the
   identical word in row 2.

## Why I believe it is correct

- One fixed table (accepted in review on hcp-1134, hcp-1113, hcp-1045, hcp-1050 to the same recipient) turns all 114 numbers into fluent
  German with no leftover or forced sign.
- Context fits: same postmark town as hcp-1134 (Freiburg in Schlesien, signed Susi) and the same "Gretchen" photo series as hcp-1045
  (Susi, October 1909, which refers to "die Freude auf meine Gesundheit"); this card (September 1909) reports a fever and recovery,
  consistent with that later card. The writer's identity is not stated on this card, so "Susi" is only a likely attribution.

## Response to review 1

Verdict ACCEPT, four minor findings; the decoded letters are unchanged.

1. Row 5, final 0 of 20 under the printed line: agreed. I enlarged the spot (review/work/l5end.png): "9/6.21.2" is clear, the
   last digit sits under the blue print. Added as uncertainty 8: 20 = T rests on word sense (HEUT) and on the same word in row 2.
2. Bracketed completion of the ending: kept marked as interpretation. The card reads only "SOLLTE ICH NICHT ½ VIII"; the report
   gives the literal rendering ("should I not ... half past seven") first and both completions, "[be there / come]" with the
   implied excuse and the plain "should I not [come] at half past seven", as readings, not text.
3. "Finished" / "already proven": reworded. hcp-1134, 1113 and 1050 are now FINAL; hcp-1045 is at REVIEWED1 with ACCEPT. The text
   now says "accepted in review".
4. Address street: the suggested "Alte B...straße" is withdrawn; the street line and house number are now reported as unread
   (work/crops/street.png shows the pencil crossed by the collection stamp).

On the human's stamp-box remark (Jolánka series): I rechecked work/crops/stamp.png. The Germania 5 Pf stamp is still affixed and
postmarked across both card and stamp; no pencil emerges at its edges. The picture side has no handwriting. No steganographic
part is visible, so the type stays MASC; what lies under the stamp cannot be checked from the scans.

Reproduction re-run after the edits: `python3 -I ciphers/hcp-979/work/decode.py` prints four OK checksums and the same plaintext.
