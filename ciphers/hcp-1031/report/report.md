# HCP 1031 (cpc_1904-03-22_AT_Wien_AT_Wien_): a secret meeting note to Anna See, Vienna 1904

Human solver: Tomáš Pavuk

**Status: deciphered (222 of 222 cipher signs read with one key; one proper name at the very end left unread); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1031 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1031), portal name cpc_1904-03-22_AT_Wien_AT_Wien_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Anna See, with no transcription or solution attached.

The address side is in plain handwriting: **Wohlg. Fräulein / Anna See / Wien XIX. / Ruthgasse 21. Israelitisches Waisenhaus** ("Miss Anna See, Vienna 19th district, Ruthgasse 21, Jewish orphanage"). It carries an Austrian 5-heller stamp cancelled in Vienna on **22.3.04** (22 March 1904) and a Vienna arrival mark.

The picture side shows a hand-coloured photograph of a young couple. The message is written in pencil over the picture in invented signs: four long lines along the left edge (read with the card turned 90 degrees counter-clockwise), then a five-line block at the top right, whose last line turns and runs downward beside the girl's hat.

![Picture side: the four cipher lines along the left edge and the five-line block at the top right (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Anna See, Wien XIX, Ruthgasse 21, Israelitisches Waisenhaus; stamp cancelled 22.3.04 (source/address-large.jpg)](../source/address-large.jpg)

No sister card addressed to Anna See was found in this repository, and a short web search found no published solution of this card. The reading below is new work.

## Method

The transcription is manual, made from the un-converted high-resolution scans (work/hires/) at 3 to 5 times enlargement. Each sign was given a code letter and the text was written into work/transcription.txt line by line (A to D for the left edge, TR1 to TR5 for the top-right block). No OCR was used and the portal supplied no transcription.

The key was found from repeated groups. The group read "sei so gut" occurs twice; "-en" endings, "treffen" (double f), "um unsere" and "wo wir uns Freitag" then gave most of the alphabet, and the rest of the text followed. Umlaut dots stand only over the signs that decode to a, o and u (Näheres, zukünftige, können, mündlich, Bäckerei), which confirms the key on its own.

Corrections made while checking the pixels, before handover: z is a separate round S-shaped sign (in "zu" twice), distinct from the flat-topped 5 used for s; in "mündlich" the stroke before "ündlich" is the detached first leg of the m, not an i.

The script work/decode.py checks the SHA-256 of the four scans, deciphers the transcription with work/key.json, and asserts that the word-divided reading has exactly the same letters as the raw decipherment. From the repository root:

    python3 -I ciphers/hcp-1031/work/decode.py

In review, a separate agent typed its own key from its own crops and decoded with its own script; its output was identical line by line.

## Key

Monoalphabetic substitution (MASC) with invented signs. The descriptions are names for the handwritten shapes.

| Plain | Sign | Plain | Sign |
|---|---|---|---|
| a | cross + | l | 6 |
| b | L-shaped hook | m | three legs under one bar |
| c | plain stroke (only in ch, ck) | n | two-legged Π |
| d | inverted T ⊥ | o | 0 |
| e | lambda (some with hook or crossbar) | p | 9 |
| f | 7 with crossbar | r | 3 |
| g | θ | s | 5 with flat top |
| h | 8 | t | 2/z-shaped sign with tail |
| i | plain stroke | u | u-shaped sign |
| j | stroke with a top flag | w | looped x-like sign |
| k | x | z | round S without top bar |

Not seen on the card: q, v, x, y, ß. Kept in plain: the Roman numeral VI and the digit 4 (district and house number). Umlauts are written as two dots over the base vowel's sign.

## Plaintext

Raw decipherment, line by line as on the card:

```text
A    liebstesannerl.seisogut,gibmirbekannt
B    wowirunsfreitagtreffen,umunserezukün-
C    ftigelagebesprechenzukönnen.sollest
D    dudenwortlautdesabschiedsbriefesha-
TR1  ben,sonimihnmit.
TR2  näheresmündlich,sei
TR3  sogutmitbestengruss
TR4  joh.wolf.VI.engelgasse4.
TR5  bäckerei4ekninger.
```

German, with word division and capitals added:

> Liebstes Annerl. Sei so gut, gib mir bekannt wo wir uns Freitag treffen, um unsere zukünftige Lage besprechen zu können. Sollest du den Wortlaut des Abschiedsbriefes haben, so nim ihn mit. Näheres mündlich, sei so gut mit besten Gruss Joh. Wolf. VI. Engelgasse 4. Bäckerei 4ekninger.

English:

> Dearest Annerl. Be so kind as to let me know where we (shall) meet on Friday, so that we can discuss our future situation. If you should have the wording of the farewell letter, then take it with you. More in person; be good. With best regards, Joh. Wolf, (district) VI, Engelgasse 4, bakery "4ekninger".

Slovak:

> Najdrahšia Annerl. Buď taká dobrá a daj mi vedieť, kde sa v piatok stretneme, aby sme mohli prebrať našu budúcu situáciu. Ak by si mala znenie listu na rozlúčku, tak ho vezmi so sebou. Podrobnosti osobne, buď taká dobrá. S najlepším pozdravom Joh. Wolf, VI. (obvod), Engelgasse 4, pekáreň "4ekninger".

"Annerl" is the Viennese pet form of Anna. The writer, Joh. (Johann) Wolf, gives his address as a bakery in Engelgasse 4 in Vienna's 6th district. He arranges a secret Friday meeting with a girl living at the Jewish orphanage, about "our future situation" and a "farewell letter", which would explain why he used a cipher.

## Uncertainties

1. **The bakery name.** After "Bäckerei" come the signs read "4ekninger". The first sign looks like a 4 with a curl; it is not the 2-shaped t used elsewhere, and it is not otherwise in the key. A first transcription read it as t ("Tekninger"); that remains only an alternative. The name is unread. It is a single proper name, and the rest of the card reads.
2. **c, i and j.** i and c share one plain-stroke shape; c is read only in ch and ck. The j of "Joh." is a stroke with a flag at the top. Both calls rest on word sense.
3. **"mündlich".** The m has its first leg slightly apart from the rest; it is read as one m sign, not "i" plus n.
4. **A mark between "gut" and "mit".** A thin lambda-like mark lies on the printed plant stalk; it is lighter and thinner than the pencil and is taken as part of the picture.
5. **"nim".** Either a single-m spelling of "nimm", or an m-doubling bar that cannot be told apart from the m sign's own bar. "Sollest" is the writer's form of "Solltest".
6. **Address.** VI. and 4 are read as Vienna district VI and a house number. Whether an Engelgasse existed in the 6th district in 1904 was not checked.
7. **Hidden writing.** The stamp is still on the card, so the space under it could not be inspected, and a hidden message there cannot be ruled out. No other pencil writing was found on the address side or elsewhere on the picture side. The type is therefore given as MASC, not MASC + Steganography.
8. Who Joh. Wolf and Anna See were is not known; no archival source was found.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) re-ran the command, decoded the transcription with its own key and script (identical output), checked every sign of the left block and the top-right block against its own enlarged crops, and judged the German to be fluent Viennese German of about 1900. Verdict: **ACCEPT**, with six minor findings.

Changes made in response: the earlier "Tekninger" reading of the bakery name is now named and the name is marked unread; the note on "nim" is softened; the report states plainly that the space under the stamp was not inspected. The other findings (the mark between "gut" and "mit", the word-sense calls for c and j, the unchecked address) were already disclosed and need no change. The transcription, key and reading did not change.

## Credits

Transcription, key reconstruction and decipherment by Claude Opus 5.5 (Anthropic), 2026-11-03; independent review by a separate Claude Opus 5.5 agent. No earlier AI work existed on this card.
