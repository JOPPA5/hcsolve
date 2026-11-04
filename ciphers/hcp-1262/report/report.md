# HCP 1262: to Jolánka Tóth, "not that kind of dancing school"

Human solver: Tomáš Pavuk

**Status: deciphered in full (18 main rows and 7 rows under the stamp; one letter restored); independent review 1 verdict ACCEPT, no word changed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1262 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1262), portal name cpc_1912--15_HU__HU_Jasz Arokszalas_jolanka-100, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The portal gives a link to a HistoCrypt paper (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), which was not consulted for this reading.

The picture side is a tinted photograph of a young man playing a mandolin to a woman, with a printed Hungarian verse beginning Hej cigány, hallod-e? It carries no cipher. The address side is written in red ink. The address is in clear: approximately Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás ("to the young lady of fair promise, Jolánka Tóth, Jászárokszállás"). The left half holds 18 rows of cipher. A further 7 rows sit in a small ruled box in the stamp corner, where the stamp was stuck over them; they were written in wet ink and are blurred. Two postmarks show parts of the town name (JÁSZ…, …ROKS…) but no legible date. The card has no signature, so the sender and date stay unknown; the portal's file name suggests 1912 to 1915.

The card belongs to the family of Hungarian cipher postcards addressed to Jolánka Tóth, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1273, 1301). No link to a particular sender in that family is claimed.

![Address side, with the 18 main cipher rows on the left and the box of 7 rows in the stamp corner (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The key was **transferred** unchanged from the finished sister cards; this is not a new key recovery. The transcription is **manual**: the solver read each row sign by sign on enlarged crops of the unconverted high-resolution original, and recorded 353 sign tokens in a ledger (work/ledger.txt). No OCR was used. Green-channel thresholding helped in the blurred stamp box. Early attempts at the smudged row 7 (nagyon, nem, ahol gyakran) were dropped when the enlargement showed e after gy and a third stroke of m under the postmark.

No earlier work exists on this number; all of it is by Claude Opus 5.5. A short script (work/decode.py) verifies the image hashes, decodes the ledger and prints the literal and normalized text.

## Key

Simple monoalphabetic substitution with invented graphic signs, plus a hidden message written in the cipher signs in the stamp box, under the stamp (register type MASC + Steganography; type updated 2026-11-03). The labels are conventional names for the handwritten shapes.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark S | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl (with bar) | c (probably row 5) | three short strokes | m | gamma/corner (stem may overrun the bar) | t |
| tick on the left + long stroke | d | two short strokes | n | long crossed diagonal | z |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + tick on the right | h / p | dotted crossed curve | i |
| open loop with descender | g | inverted T | j | opposed or joined bowls | cs |
| g + low descender, joined or adjacent | gy | | | | |

Dots over the loop give ö. Acute marks are mostly faint and are supplied in normalization. On this card ly is written j (mejért, ojan). The h and p are one sign, told apart only by word sense.

## Plaintext

Literal decipherment, row by row. In `{x|y}`, x is the value of the shape as written and y the value the word needs; `{ol}` is a squeezed compound; `[m]` is restored, not read.

```text
01 kedvesjolankambe            10 nemkivanjahogyakor
02 csessoraitmegka{d|p}tam     11 gondolhasakmagara
03 mejertfogadjaköszö          12 amikormagakivan
04 netemekedvesemez            13 j{e|a}mikornekemnincs
05 nemojantan{c|cs}zisko       14 ojanoramhogynegon
06 lamintjolankamgo{m|n}       15 dolnekönreezelbe
07 d{ol}jaideholgyeknem        16 zaromsoraimeniske
08 jarnakcsakferfiak           17 remhogygondojonram
09 kedvesjolankamcsak          18 tisztelemakevesmamaj{e|a}t

stamp box: istenvele | aviszont | latasra | holnap | csokolo[m] | szamta | lanszor
```

### Hungarian (normalized)

Kedves Jolánkám! Becses sorait megkaptam, melyért fogadja köszönetem[et]. Kedvesem, ez nem olyan táncziskola, mint Jolánkám gondolja, ide hölgyek nem járnak, csak férfiak. Kedves Jolánkám, csak nem kívánja, hogy akkor gondolhassak magára, amikor maga kívánja, mikor nekem nincs olyan órám, hogy ne gondolnék önre. Ezzel bezárom soraim. Én is kérem, hogy gondoljon rám. Tisztelem a ke[d]ves mamáját.

Under the stamp: Isten vele, a viszontlátásra holnap! Csókolo[m] számtalanszor.

### English

Dear Jolánka! I have received your esteemed lines, for which please accept my thanks. My dear, this is not the kind of dancing school you think it is, Jolánka: no ladies come here, only men. Dear Jolánka, surely you do not want me to be able to think of you only when you wish it, when I have not a single hour in which I do not think of you. With this I close my lines. I too ask you to think of me. My respects to your dear mother.

Under the stamp: God be with you, until we meet tomorrow! I kiss you countless times.

### Slovak

Milá Jolánka! Vaše vzácne riadky som dostal, za čo prijmite moju vďaku. Moja milá, toto nie je taká tanečná škola, ako si Jolánka myslí, sem dámy nechodia, iba muži. Milá Jolánka, veď predsa nechcete, aby som na Vás mohol myslieť len vtedy, keď si to Vy želáte, keď nemám ani jednu hodinu, v ktorej by som na Vás nemyslel. Týmto končím svoje riadky. Aj ja Vás prosím, aby ste na mňa mysleli. Pozdravujem Vašu milú mamu.

Pod známkou: S Bohom, dovidenia zajtra! Bozkávam Vás nespočetnekrát.

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1262/work/decode.py
```

The command checks the SHA-256 of the four image files, decodes the ledger and prints the literal rows and the normalized text.

## Uncertainties

These readings rest on word sense or restoration, not on the shape alone.

- **Restored letter.** S5 csókolo[m]: the m lies wholly under an ink blot and is not read from pixels. It comes from the family's closing formula; csókolok is also a word but does not occur in the sister cards.
- **Shape differs from the letter the word needs.** Row 2 kaptam has a tick-left sign like d. Row 6 ends in an m shape where gondolja needs n. Rows 13 and 18 have a three-bar shape where kívánja and mamáját need a; in row 18 the third bar is an overwritten scribble.
- **Row 5 closed bowl.** It may be c or cs; the word táncziskola is the same. Its build differs from the joined bowls of row 9 and resembles the c of tancz on HCP 1273.
- **Row 7.** hölgyek: the first three signs are smudged, the k is overwritten, and no dots are visible over the o. In gondolja the o and l are a squeezed, possibly later, compound.
- **Row 14 ne.** The n is heavily overwritten, with a stray crossbar.
- **Row 17 `gondojon`.** There is no wave for l, only a small tick on the j; it may be an abbreviated l.
- **Row 4.** One extra e after köszönetem, taken as an unfinished -et; a false start of kedvesem is equally possible. The sense is the same.
- **Stamp box.** Rows S1 to S3 are blurred, and signs there are partly read from the word. S4 holnap has the h/p sign at both ends. Attaching it to a viszontlátásra is editorial; it could open the next phrase ("tomorrow I will kiss you"). The placing of the stamp text after the main text is assumed from sister cards.
- **Writer's spelling, normalized.** mejért, ojan, akor, gondolhasak, ezel, and keves for kedves (no d on the card; kevés "few" makes no sense here). Accents are supplied. The small tick at the end of row 15 is taken as a line-break mark.
- **Small sign variants, none in doubt.** The i in row 13 has no visible dot, as in S2; the row 11 final a is overwritten; the j stem in row 14 runs through its bar; the o and r of S7 overlap; the third stroke of the row 2 final m is very pale.
- **Register shift.** The writer moves between maga, third-person Jolánkám and önre; this is on the card.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, 2026-11-01. Verdict **ACCEPT**. The reviewer tried to refute the reading sign by sign. It reran the command, compared the output with the claimed text, and made its own row-by-row transcription into sign classes (356 signs, 25 rows) with its own enlargements, mapping them through the HCP 1216 key directly. That check was not blind, because the reviewer had read the solution first. Of the 25 rows, 22 agreed exactly; the other 3 differed only at signs where the shape and the needed letter differ (rows 2 and 18, and the h/p sign in S4). It also confirmed that nothing outside the 25 rows carries cipher and that the portal shows no published solution.

The review had five minor findings and no blocker. All were accepted; no word, translation or normalized text changed:

- Row 18: the sign before final t is an e shape with a correction, so it is now printed `{e|a}` and disclosed.
- Row 2: the tick-left sign is now printed `{d|p}`, and the note on h and p was corrected.
- The restoration of csókolo[m] now rests on the family formula, not on the claim that no other letter makes a word.
- Small sign variants are now listed.
- The row 5 closed bowl may be c, so it is now printed `{c|cs}`.

The reviewer could not verify the hidden m, any dots in hölgyek, how holnap attaches, or the sender and date.

## Credits

Source capture by the orchestrating Claude Opus 5.5 agent; transcription, key transfer and decipherment by Claude Opus 5.5; independent review by a separate Claude Opus 5.5 agent. The family key comes from the finished sister cards (HCP 1216 and others), whose earlier work was done by the OpenAI GPT solver and completed by Claude Opus 5.5. Human solver: Tomáš Pavuk.

## Sources

- HC Portal record 1262: https://crypto.hcportal.eu/dashboard/cryptograms/1262
- Both sides of the card as served by the portal (source/), and the unconverted originals (work/hires/); URLs and hashes in SOURCES.md.
- Key: ciphers/hcp-1216 and the other Jolánka cards named above.
