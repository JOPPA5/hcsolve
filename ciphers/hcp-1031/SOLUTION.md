# hcp-1031 — solution (round 1)

Card: HC Portal cryptogram 1031, `cpc_1904-03-22_AT_Wien_AT_Wien_` (T. Schrödel collection). Picture postcard, posted in Vienna on 22.3.1904 to "Wohlg. Fräulein Anna See, Wien XIX, Ruthgasse 21, Israelitisches Waisenhaus" (the address side is plain German Kurrent/Latin script). The ciphertext is written in pencil on the picture side: four lines along the left edge (card turned 90° counter-clockwise), then a five-line block top right, whose last line turns and runs downward beside the girl's hat.

Work: transcription, key reconstruction and decipherment by Claude Opus 5.5 (2026-11-03). No earlier work on this number, no solution or transcription attached on the portal (status Not solved). A short web search (Klausis Krypto Kolumne / Schrödel cards) found no published solution of this card.

## Cipher type and key

Monoalphabetic substitution (MASC) with invented signs (digits, Greek/Cyrillic-like shapes) for German. Umlaut dots are written over the sign of the base vowel. Punctuation and hyphenation at line ends are plain.

| plain | sign (code in work/transcription.txt) |
|---|---|
| a | + (cross) `+` |
| b | L-shaped hook, like ʟ `c` |
| c | plain stroke `C` (same shape as i; only in ch / ck) |
| d | inverted T ⊥ `Q` |
| e | lambda ʎ, also written with an h-hook or crossbar `L` |
| f | 7 with crossbar `7` |
| g | θ `T` |
| h | 8 `8` |
| i | plain stroke `i` |
| j | stroke with top flag (only in "Joh.") `j` |
| k | x `X` |
| l | 6 `6` |
| m | three legs under one bar `M` |
| n | two-legged Π `N` |
| o | 0 `0` |
| p | 9 `9` |
| r | 3 `3` |
| s | 5 with flat top bar `5` |
| t | 2/z-shaped sign with tail `Z` |
| u | u-shaped sign `U` |
| w | looped x-like sign (ꭓ/ж) `J` |
| z | round S without top bar `S` |

Not seen: q, v, x, y, ß. Kept literally: `VI.` (Roman numeral, read as Vienna district VI) and the digit `4` (house number in TR4; also the first sign of the last name in TR5, see uncertainties). Key in `work/key.json`.

## Command

From the repo root:

    python3 -I ciphers/hcp-1031/work/decode.py

It checks the SHA-256 of the four source images, deciphers `work/transcription.txt` line by line with `work/key.json`, and asserts that the word-divided reading below has exactly the same letters as the raw decipherment.

## Plaintext (German; word division and capitals added)

Liebstes Annerl. Sei so gut, gib mir bekannt wo wir uns Freitag treffen, um unsere zukünftige Lage besprechen zu können. Sollest du den Wortlaut des Abschiedsbriefes haben, so nim ihn mit. Näheres mündlich, sei so gut mit besten Gruss Joh. Wolf. VI. Engelgasse 4. Bäckerei 4ekninger.

Raw decipherment per card line:

    A    liebstesannerl.seisogut,gibmirbekannt
    B    wowirunsfreitagtreffen,umunserezukün-
    C    ftigelagebesprechenzukönnen.sollest
    D    dudenwortlautdesabschiedsbriefesha-
    TR1  ben,sonimihnmit.
    TR2  näheresmündlich,sei
    TR3  sogutmitbestengruss
    TR4  joh.wolf.VI.engelgasse4.
    TR5  bäckerei4ekninger.

English: Dearest Annerl. Be so kind as to let me know where we (shall) meet on Friday, so that we can discuss our future situation. If you should have the wording of the farewell letter, then take it with you. More in person; be good. With best regards, Joh. Wolf, (district) VI, Engelgasse 4, bakery "4ekninger".

Slovak: Najdrahšia Annerl. Buď taká dobrá a daj mi vedieť, kde sa v piatok stretneme, aby sme mohli prebrať našu budúcu situáciu. Ak by si mala znenie listu na rozlúčku, tak ho vezmi so sebou. Podrobnosti osobne, buď taká dobrá. S najlepším pozdravom Joh. Wolf, VI. (obvod), Engelgasse 4, pekáreň "4ekninger".

## Uncertainties

1. TR5 last word, after "Bäckerei": signs `4 L X N i N T L 3` = "4ekninger" — a proper name (presumably the bakery's owner). The first sign looks like a 4 with a left curl (compare the clean 4 at the end of TR4); it is not in the key otherwise and I could not identify the letter, so the name is reported literally. My first transcription (work/trans_v0.txt) read this sign as the t sign, giving "Tekninger"; on enlargement it does not match the 2-shaped t used elsewhere, so "T-" stays only an alternative. The name is unread. The X sits at the corner where the line turns down; the remaining "ninger." runs vertically beside the hat (read top to bottom; the reverse orientation gives no signs of the key).
2. `VI.` and the `4` of "Engelgasse 4" are taken as plain Roman numeral / digit (district and house number); they are not cipher signs elsewhere. I did not check whether an Engelgasse existed in Vienna VI in 1904.
3. i and c share one plain-stroke shape; c is read only before h (ch: besprechen, Abschieds-, mündlich) and k (Bäckerei). That c/i split rests on word sense. The j of "Joh." is a stroke with a flag at the top; that it is j, not i, also rests on word sense.
4. e is written with three slight variants of the lambda sign (plain, with an h-like hook, with a crossbar). I treat them as one sign; every one of them reads e.
5. In TR2 the m of "mündlich" is drawn with its first leg apart from the barred pair, and there is a dot-like pen start above it; I read it as one m sign, not "i" + n (which would give "Näheres inündlich").
6. Between "gut" and "mit" in TR3 there is a thin lambda-like mark in the printed plant stalk; it is lighter and thinner than the pencil, and I take it as part of the picture. "Sei so gut" then stands on its own before the greeting.
7. "so nim ihn mit": either a single-m spelling of "nimm", or an m-doubling bar that cannot be told apart from the m sign's own bar. "Sollest" is the writer's form of "Solltest".
8. Steganography check: the stamp on the address side is still attached and the scan cannot show what is under it; the picture side shows no further pencil writing except the message above. The address side is plain. What lies under the stamp was not inspected (not possible from the scans), so a hidden message there cannot be ruled out.

## Why I believe it is correct

- All 222 key signs on the card (226 signs in all, counting the literal V, I and two 4s) decode with one 22-sign key into grammatical, coherent German, including long words that check the key many times (Abschiedsbriefes, besprechen, zukünftige, Wortlaut, treffen, Freitag).
- Umlaut dots sit on exactly the signs that decode to a, o, u (Näheres, zukünftige, können, mündlich, Bäckerei).
- The key has no contradictions: each sign has one value, apart from the i/c stroke shared as disclosed.
- The content fits the card: a young man (Joh. Wolf) writing to Anna See ("Annerl", the Viennese pet form of Anna) at the Jewish orphanage, arranging a secret Friday meeting about "our future situation" and a "farewell letter"; that would explain the cipher.
- Residuals: one unread proper name (the bakery's), plus the c/i and j calls, which rest on word sense.

## Response to review 1

Verdict ACCEPT. No change to the transcription, the key or the reading. `python3 -I ciphers/hcp-1031/work/decode.py` re-run on 2026-11-03: hashes OK, output and assert unchanged.

1. First sign of the bakery name: agreed. Uncertainty 1 now names the earlier reading "Tekninger" from work/trans_v0.txt, says why it was dropped (the sign is a 4 with a curl, not the 2-shaped t; see work/crops/z_tr5sig.png) and states that the name is unread. One proper name only; the rest of the card reads.
2. TR3 mark between "gut" and "mit": no change needed; already disclosed (uncertainty 6), and the reviewer agrees it belongs to the printed stalk.
3. "nim" / "nimm": agreed; uncertainty 7 softened as proposed.
4. j and c on word sense: no change needed; already disclosed (uncertainty 3).
5. Under the stamp: agreed. Uncertainty 8 and the report now say plainly that the space under the stamp was not inspected and a hidden message there cannot be ruled out. I checked both scans again: no pencil around the stamp edges or elsewhere on the address side; the only pencil on the picture side is the message. The register type therefore stays MASC (not "MASC + Steganography").
6. Engelgasse 4 not checked: no change; disclosed (uncertainty 2) and repeated in the report.
