# HCP 1287 (cpc_1912-05-15_HU__HU_Jasz Arokszalas_jolanka-21): a funeral and a strike camp, to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (423 of 423 written signs, two of them restored under a blot); independent review 1 verdict REVISE, all findings addressed, no sign value changed.** Two word-sense questions remain open, see Uncertainties. Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1287 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1287), portal name cpc_1912-05-15_HU__HU_Jasz Arokszalas_jolanka-21, part of Tobias Schrödel's collection of cryptographic postcards (see https://ecp.ep.liu.se/index.php/histocrypt). When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date 1912-05-15, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side shows a kissing couple and swallows, with a printed verse beginning Fecském hova szállsz? ("My swallow, where are you flying?"). It carries no cipher text.

The address side holds the message: 22 rows of invented signs in red ink, covering the left half. In plain hand it is addressed to Szépreményű (under the postmarks) Tóth Jolánka úrleánynak, Jász-Árokszállás, "to the promising Miss Jolánka Tóth". A small word after úrleánynak is probably szeretettel, "with love", but it is not certain. In the stamp corner there is a short plain message (see Plaintext). The postmarks are JÁSZÁROKSZÁLLÁS 912 MA 15, which agrees with the portal date, and a second one showing only YÖN, possibly Gyöngyös (unverified).

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher rows, the postmarks and the plain text in the stamp corner (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth in Jászárokszállás, several of which are deciphered in this repository (for example HCP 1216, 1243 and 1301). They share one key, so this card was read with a **known, transferred key**, not by a new key recovery. No reading of this card was supplied or consulted.

## Method

The transcription is **manual**, by Claude Opus 5.5, with no earlier work on this number. The family key comes from the finished cards; their earlier passes were by an OpenAI GPT solver, with completion by Claude Opus 5.5. Every row was read on 2× and 4× crops of the original high-resolution address side and recorded as a sign ledger, one token per written sign. A short script checks the file hashes and decodes the ledger.

The writer spells phonetically: he drops and doubles letters, and acute accents are mostly faint. The literal decipherment is kept as written, and the normalized Hungarian is editorial.

In review, a separate Claude Opus 5.5 agent re-ran the command, enlarged all 22 rows of the same scan 3× (the disputed spots up to 5×) and decoded its own sign sequence with its own script. Its sequence agreed in all 423 positions. That check was not blind, because the reviewer had read the solution first.

## Key

Hungarian simple monoalphabetic substitution with invented signs. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark (top often closed) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| joined opposed bowls | cs | three short strokes | m | gamma / corner | t |
| short stroke left + tall stroke right | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short stroke right | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal (flagged) | z |
| inverted T | j | | | | |

One sign serves for both h and p, and only that choice rests on the word. The d (12 cases) and the h/p sign (8 cases) are separated by form on this card. The c of szerencsésen is a left bowl re-inked into a €-like shape, and it is the sign's only occurrence. Here gy is written as two signs, g + y, not as the joined form of HCP 1216. Dots over o and u give ö and ü, and two ticks give ő. Numerals stay in clear in this family.

## Plaintext

Literal decipherment, row by row (`{9|k}` = digit 9 or sign k; `[x]` = restored under a blot):

```text
01 kedvesjolankamtudatom        12 takenisotmaradtam{9|k}o
02 hogyszerencsesenmegerkez     13 raiasegedeklanyai
03 tünkeppenakortemetekezt      14 esfelesegeikelmulat
04 lanytijenszeptemetesmeg      15 tunkedesjolankammes
05 nemlatamdemegjolankam        16 ujsagotnemirhatok
06 seazudvarlojaötször          17 minthogynemtudom
07 ajultelutoljarais            18 medigtarastrajkdeami
08 bevitekatemtőkapol           19 eztiletinembajakarmedig
09 najabaatemetesutan           20 tartbecsessoraitvarva
10 elmentemasrrajktanya         21 istenveleaviszontlatas[i]g
11 raaholnagybatanszol          22 edese[m]
```

Hungarian (normalized):

> Kedves Jolánkám! Tudatom, hogy szerencsésen megérkeztünk. Éppen akkor temették ezt [a] lányt. Ilyen szép temetés[t] még nem láttam, de még Jolánkám se. Az udvarlója ötször ájult el, utoljára is bevitték a temető kápolnájába. A temetés után elmentem a sztrájktanyára, ahol nagy bát[r]an szóltak, én is ott maradtam 9 óráig(?). A segédek lányai[val] és feleségeikkel mulattunk. Édes Jolánkám, más újságot nem írhatok, mint hogy nem tudom, meddig tar[t] a sztrájk. De ami ezt illeti, nem baj, akármeddig tart. Becses sorait várva, Isten vele, a viszontlátásig, édesem.

English:

> Dear Jolánka! I inform you that we arrived safely. They were burying that girl just then. I have never seen such a beautiful funeral, and neither has my Jolánka. Her suitor fainted five times; the last time they even carried him into the cemetery chapel. After the funeral I went to the strike camp, where they spoke very boldly, and I too stayed there until 9 o'clock(?). We made merry with the journeymen's daughters and wives. Sweet Jolánka, I can write no other news than that I do not know how long the strike will last. But as far as that goes, it does not matter how long it lasts. Awaiting your esteemed lines, farewell, until we meet again, my darling.

Slovak:

> Milá Jolánka! Oznamujem Vám, že sme šťastne dorazili. Práve vtedy pochovávali to dievča. Taký krásny pohreb som ešte nevidel a ani moja Jolánka nie. Jej nápadník päťkrát omdlel, naposledy ho dokonca odniesli do cintorínskej kaplnky. Po pohrebe som išiel do štrajkového tábora, kde hovorili veľmi odvážne, a aj ja som tam zostal do 9 hodín(?). Zabávali sme sa s dcérami a manželkami tovarišov. Sladká Jolánka, inú novinu Vám nemôžem napísať, len že neviem, dokedy potrvá štrajk. Ale čo sa toho týka, to nevadí, nech trvá akokoľvek dlho. V očakávaní Vašich vzácnych riadkov, s Bohom, do videnia, drahá moja.

Plain text in the stamp corner, not enciphered (`csokolom / es csokol / tatom / aval akit / leg jo?on / szeret si / rig hü / kedvese`):

> Csókolom és csókoltatom avval, akit legjobban(?) szeret. Sírig hű kedvese.
>
> I kiss you and send kisses through the one you love best. Your sweetheart, faithful unto the grave.
>
> Bozkávam Vás a dávam Vás bozkávať po tom, koho máte najradšej. Váš do hrobu verný milý.

## Uncertainties

1. **Row 12, `{9|k}`.** Row 12 ends with a heavily inked sign and then `o`; row 13 starts `r a i`. The inked sign is either the digit 9 in clear or the k-sign, which has the same closed top and left-hooked foot on this card (row 8). 9 órái[g], "until 9 o'clock", with a dropped g, is the normalization chosen. Korai, "early", fits no clear construction. A dot up and to the right of the `o` could be an acute (ó), but it may be a stray mark. This call rests on word sense.
2. **Row 11, `nagybatan szoltak`.** The signs are certain; the word division is not. Preferred: nagy bát[r]an szóltak, "they spoke very boldly", with one dropped r, as in tar for tart. Alternative: nagybátyám szóltak, "my uncle called [me]", which needs three repairs and a polite plural for one's own uncle. This call rests on word sense.
3. **Restorations.** The final m of édesem (row 22) lies under a brown blot, with only a stroke on each side visible; the third stroke is inferred. The i of viszontlátásig (row 21) shows its dot and tail beside the blot.
4. **Row 10 `srrajk`.** The second r is a heavily re-inked sign, possibly a corrected t. Row 18 plainly has strajk, and the word is normalized sztrájk.
5. **Row 15 `mes`.** Normalized más, "other", from the context más újságot nem írhatok.
6. **h/p by word sense.** The sign is p in éppen, szép, kápol- and h in hogy, ahol, írhatok.
7. **Spelling.** The writer's forms are normalized, for example akor, latam, ijen, bevitek, temtő, najaba, medig, ileti. Missing endings are bracketed: temetés[t], lányai[val].
8. **Row 5–6 `de még Jolánkám se`.** Whether this means she has not seen such a funeral, or teases her, cannot be determined.
9. **Stamp corner.** The sense of legjobban is secure, but the letters read closer to jobon, so the form is marked as uncertain. Line 4 has aval.
10. **Persons.** The card is unsigned; kedvese gives no name. No identification with the Feri of HCP 1216 and 1304 is claimed, although the closing formula and a strike mention in HCP 1304 are in line with those cards. The second postmark is not established as Gyöngyös. The dead girl is not named.

## Why the reading stands

The family key, unchanged, turns every sign into Hungarian, and one sign class gives one letter throughout. The text is coherent and specific: arrival, funeral, the fainting suitor, the strike camp, the journeymen's families, and the family's usual closing Becses sorait várva … Isten vele. Words recur identically across the card (Jolánkám three times, strajk twice, temet- twice, meddig twice), and the plain text agrees with the family (sírig hű kedvese).

## Review and what changed

Review 1 (a separate Claude Opus 5.5 agent) returned REVISE. It confirmed the key, the 423-sign sequence and the overall sense, and raised five findings, all accepted.

| # | Severity | Finding | What changed |
|---|---|---|---|
| 1 | major | "My uncle called [me]" in row 11 was forced | nagy bát[r]an szóltak is now preferred in all three languages; the old reading stays as an alternative |
| 2 | major | The row 12/13 break was wrong, and the "wide gap" evidence for the 9 did not exist | The `o` moved to row 12; the argument was withdrawn; the dot near the `o` was recorded as suggestive only |
| 3 | minor | The d/h ambiguity was overstated | d and h/p are now separated by form; only h/p rests on word sense |
| 4 | minor | The stamp line `leg jobban` is not what the pixels show | Literal form now `leg jo?on`, normalized legjobban(?) |
| 5 | minor | Small errors in the supporting argument | Jolánkám count and the list of signs not read straight corrected |

No sign value changed, and the sequence of decoded letters is the same. The reviewer could not verify the second postmark, the small word after úrleánynak, the original signs under the re-inked places, or the sender.

## Reproduction

From the repository root (`ciphers/hcp-1287/work/` holds the ledger and script):

```sh
python3 -I ciphers/hcp-1287/work/decode_opus.py
```

It checks the SHA-256 of the four image files, decodes the ledger (423 signs) and prints the literal rows and the normalized text.
