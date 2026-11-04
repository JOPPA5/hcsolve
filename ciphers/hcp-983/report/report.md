# HCP 983 (cpc_--___DE_Endsee_): a Bavarian field-post Easter card with a number-cipher signature

Human solver: Tomáš Pavuk

**Status: deciphered in full (21 of 21 cipher numbers); plain verse read in full; independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 983 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/983), portal name cpc_--___DE_Endsee_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient "Lina Botch", with no transcription or solution attached. The portal links the general HistoCrypt article on the collection (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), which does not give a reading of this card.

The picture side is a printed Easter card, "Beste Ostergrüsse", showing a soldier in a spiked helmet (Pickelhaube) with a girl, publisher mark R 5204/3. There is no handwriting on the picture side.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address side is written in Latin cursive (lateinische Schreibschrift) with two German habits: the long ſ in daß, Gruß and Kuß, and the bow over u. It is addressed to **Fräulein Lina Botsch bei Herrn Geisendörfer in Endsee, Post Steinach a/E**. Endsee is a village in Middle Franconia (Bavaria) near Rothenburg ob der Tauber; "a/E" is most likely "an der Ens", since Steinach an der Ens is its post office. The card bears no stamp: the stamp box holds only a printed red triangle and a black field-post mark beginning "K.B." (Königlich Bayerisch), so this is a Bavarian soldier's field-post card from the First World War (1914–1918; the unit and date in the postmark ring are not legible).

![Address side (source/address-large.jpg)](../source/address-large.jpg)

The message is written sideways along the left half of the address side: three lines of plain German verse, then two lines of dotted numbers. Someone later pencilled block capitals above the numbers (a later reader's attempt, partly wrong; see below).

## Method

All work was done by Claude Opus 5.5 from the high-resolution scan of the address side (3469 × 2298 pixels), turned 90° counter-clockwise and enlarged two to four times. No earlier solver worked on this card, and no published solution was found or used.

1. The plain verse was read word by word. It is a stock postcard rhyme, which also confirms the few doubtful letters.
2. The 21 numbers were read one by one; the 7 with a hook (in both 17s) was compared with the crossed 4 (in 14 and the last 4), and the v-shaped 2 in the last word with the other 2s on the card.
3. Plain A1Z26 (A=1 … Z=26) gives nonsense ("INH HEQBRS / RCHQEIBE BAKD"). The usual German school alphabet with I and J sharing one number gives German at once. Every number decodes; none is left over.

![Start of the two cipher lines with the later pencil capitals above them (work/numA.png)](../work/numA.png)

![End of the two cipher lines (work/numB.png)](../work/numB.png)

The pencil capitals (J O H / H E R B S T and S C H T E J B E B T L D) are in a different medium and hand. The first line agrees with the key; the second has T for 17 (should be R) and B T L D for 2.1.11.4 (should be B A L D). They were not used for the reading.

## Key

Number substitution (monoalphabetic), alphabet numbered with I and J merged:

| A | B | C | D | E | F | G | H | I/J | K | L | M | N | O | P | Q | R | S | T |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |

Only the values 1 to 19 occur on the card, so the numbering after T is not attested. Dots separate the numbers; wider gaps separate words.

## Ciphertext and plaintext

Ciphertext (from the pixels):

```text
9.14.8.  8.5.17.2.18.19.
18.3.8.17.5.9.2.5.  2.1.11.4.
```

Decoded:

```text
I/J O H   H E R B S T          ->  JOH. HERBST
S C H R E I/J B E   B A L D    ->  SCHREIBE BALD
```

Full message in German (plain verse plus deciphered part):

"Zum Zeichen daß ich dein gedenke, / Ich dir dieses Kärtchen sende, / Gruß und Kuß sendet Dir **Joh. Herbst. Schreibe bald.**"

English: "As a sign that I think of you, I send you this little card. Greetings and a kiss are sent to you by Joh[ann] Herbst. Write soon."

Slovak: "Na znak, že na teba myslím, posielam ti túto kartičku. Pozdrav a bozk ti posiela Joh[ann] Herbst. Napíš čoskoro."

The sender thus hid only his name and his plea "write soon", and wrote the rest of the card in plain.

The reading can be reproduced from the repository root with

```text
python3 -I ciphers/hcp-983/work/decode.py
```

which checks the SHA-256 hashes of the four scans and decodes work/transcription.txt with the key above.

## Steganography check

The stamp box, the picture and the edges were inspected for hidden writing. The card never carried a stamp (field post), so nothing can be hidden under one; the box holds the printed red triangle, the "K.B." postmark and a few green specks that form no letters. The picture side has only print. The type is therefore plain MASC (number substitution), not MASC + Steganography.

![Stamp box: printed red triangle and K.B. field-post mark, no stamp (review/work/stamp.png)](../review/work/stamp.png)

## What remains uncertain

- Number 9 stands for both I and J; J in "Joh." and I in "Schreibe" are chosen by word sense.
- "Joh." is an abbreviation, most likely Johann (or Johannes); the full name is not written.
- "Gruß" and "Kuß" are written with a bow over the u and can look like "gräß"/"Käß" in the scan; word sense and the stock verse fix them. The final "ke" of "gedenke" is written below the line.
- The recipient's surname shows "Bot" + an overwritten letter + "ch" (Botsch or Botach); the portal gives "Botch". It is not part of the cipher.
- The field-post unit and the exact date (1914–1918) cannot be read from the postmark.
- The identities of Joh. Herbst and Lina Botsch are not known.

## Review and what changed

An independent Claude Opus 5.5 reviewer re-read all 21 numbers from its own rotated crops, decoded them with its own script (both plain A1Z26 and the I/J-merged alphabet), checked the plain verse, the pencil annotation, the stamp box and the picture side, and gave the verdict **ACCEPT**. Its five minor findings and the responses:

1. The handwriting was first described as German Kurrent; it is Latin cursive with long ſ and the u-bow. The description was corrected.
2. "Post Steinach a/E" is now expanded as most likely "an der Ens" (Steinach an der Ens, post office for Endsee).
3. The decoding script listed an unattested key tail after T; it now stops at T. The command was re-run with unchanged output.
4. The surname uncertainty (Botsch/Botach) stays disclosed.
5. The I/J choices and the expansion of "Joh." stay disclosed as word-sense decisions.

None of these changed the decoded text.
