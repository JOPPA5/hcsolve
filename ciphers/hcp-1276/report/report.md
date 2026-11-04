# HCP 1276 (cpc_1912-08-11_HU__HU_Jasz Arokszalas_jolanka-30): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered, with one unread group of about six signs in row 14; the rest of the message reads. Independent review 1 verdict REVISE; all eight findings addressed, no change of key or of the sense of the message.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1276 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1276), part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt paper https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was found.

The picture side is a tinted studio photograph of a couple in evening dress about to kiss (printed number 3071/72); it carries no cipher text. Everything is on the address side, in red ink. The letter opens in ordinary handwriting, and the cipher starts on the same line, right after the word köszönetemet. It runs to 16 rows, with five more short cipher rows inside the stamp box, written where the stamp would cover them; the stamp has since been lifted, leaving the hidden message visible. The address is in clear: Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás. The postmark shows "12 AU 11", matching the date 1912-08-11 in the portal's file name, a Sunday.

The card belongs to the "Jolánka" family of Hungarian cipher postcards, several of which are deciphered in this repository (for example HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). They share one key. This card was therefore read with a **known, transferred key**, not by a new key recovery.

![Address side with the plain opening, the cipher rows and the stamp box (source/address-large.jpg)](../source/address-large.jpg)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

All work on this number was done by Claude Opus 5.5; no earlier pass exists. The solver recognised the family from the address, took the key from HCP 1216 and read every sign on 3–5× enlargements of the un-converted scan, recording one token per written sign in a ledger (272 tokens). The transcription is manual, not OCR. A script checks the source hashes and turns the ledger into letters:

```text
python3 -I ciphers/hcp-1276/work/decode_opus.py
```

The script proves only that the ledger and the text agree. The evidence for the reading is the sign-by-sign comparison with the scan, made independently by the reviewer. Blots were checked on the green channel with raised contrast.

## Key

**Cipher type: MASC + Steganography** (updated 2026-11-03). Simple monoalphabetic substitution with invented graphic signs, unchanged from the family, with a further cipher message hidden under the stamp. The descriptions are names for handwritten shapes.

| Plain | Sign | Plain | Sign |
|---|---|---|---|
| a | two bars | m | three short strokes |
| b | shape like 6 | n | two short strokes |
| c | left-open bowl | ny | n + y |
| d | long stroke + short tick | o | cursive loop |
| e | three bars | r | F-like sign |
| f | upright cross | s | right-open bowl |
| g | open loop with descender | sz | s + z |
| gy | joined loop + descender | t | gamma / corner |
| h, p | tall stroke + short (near-homographs) | u | cross x |
| i | dotted crossed curve | v | chevron |
| j | inverted T | y | low descender |
| k | section mark | z | crossed diagonal |
| l | wave | ö, ü | o, u with marks above |

The numeral 7 in row 12 stands in clear. Acute accents are not written, so they are supplied in the normalized text.

## Plaintext

Literal decipherment. `{|}` is one stroke with no value of its own (see uncertainty 2).

```text
01 igazansaj              09 hadeluta{|}menn
02 nalomakeresztla        10 akorestereokvet
03 nyunkatonnekedesem     11 lenszeptember
04 evelahalallal          12 7enleszegyszü
05 aremenyeiosze          13 retimulatsagis
06 döltekkedvesem         14 deszeretnemnahogykan
07 amulatsagbaok          15 feljonneazmulatsagba
08 vetlenlemegyek         16 istenvelaviszontlatasraferi
stamp box: üdvöz | lomata | volbol | hükedves | ceferi
```

Normalized Hungarian. Brackets `[ ]` mark supplied letters, `{ }` the unread group. Word division and punctuation are editorial.

**Plain script:** Szeretett Édes Jolánkám! Becses sorait megkaptam, melyért fogadja köszönetemet.

**Cipher:** Igazán sajnálom a keresztlányunkat. Önnek, édesem, evvel a halállal a reményei összedőltek. Kedvesem, a mulatságba okvetlen lemegyek; ha délután menn[ék], ak[k]or estére okvetlen. Szeptember 7-én lesz egy szüreti mulatság is, de szeretném, {na/ha hogy kan} feljönne a(z) mulatságba. Isten vel[e], a viszontlátásra! Feri.

**Stamp box:** Üdvözlöm a távolból, hű kedvese, Feri.

**Address, plain script:** Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás.

### English

Beloved sweet Jolánka! I have received your esteemed lines, for which please accept my thanks.

I am truly sorry about our goddaughter. For you, my sweet, your hopes have collapsed with this death. My dear, I will certainly go down to the party; if I went in the afternoon, then by evening for certain. On 7 September there will also be a harvest ball, but I would like [unresolved: na/ha hogy kan; probably "if …"] you to come up to the ball. God be with you, until we meet again! Feri.

Stamp box: I greet you from afar, your faithful sweetheart, Feri.

Address: To the young lady of fair hopes, Miss Jolánka Tóth, Jászárokszállás.

### Slovak

Milovaná sladká Jolánka! Vaše vzácne riadky som dostal, za čo prijmite moju vďaku.

Naozaj ľutujem našu krstnú dcéru. Vám, drahá, sa touto smrťou zrútili nádeje. Moja milá, na zábavu určite prídem; ak by som šiel popoludní, tak do večera určite. Siedmeho septembra bude aj oberačková zábava, ale chcel by som [nevyriešené: na/ha hogy kan; asi „keby …“], aby ste prišli hore na zábavu. S Bohom, dovidenia! Feri.

V rámčeku na známku: Pozdravujem Vás zďaleka, Váš verný milý, Feri.

Adresa: Slečne krásnych nádejí Jolánke Tóthovej, Jászárokszállás.

## Uncertainties

- **Row 14, end, unread (the main caveat).** After szeretném the row climbs and is cramped. It has two strokes (n, or h since the second is shorter), a; then a 2-shaped sign with a crossbar found nowhere else on the card; a large O; a blotted sign with a descender and a rising tail; section mark k; a; two strokes n. Hogy is a guess from the outline, and ka-n has no identified meaning. Ha would give the normal construction szeretném, ha … feljönne, leaving one unread word, but that is word sense only. The sense "I would like … you to come up" does not depend on the group.
- **Rows 9–10.** Between the a of -uta- and the e of menn the card has four strokes where délután + menn needs five, so the writer ran the words together or dropped a stroke. This rests on word sense, as does the nn of menn, whose strokes are uneven. Mennék has a supplied ending, and estére okvetlen has no verb on the card.
- **Blotted signs read through the ink.** Row 9 u, row 11 p, row 13 s, row 15 u. The row 15 sign read z of az has a closed loop that is not part of z. It may be a slip or a struck sign, so a(z).
- **h/p calls by word sense.** Row 4 h of halállal; row 11 p of szeptember.
- **Row 16.** The card has one two-bar sign between l and v, literal `vela viszontlatasra`, so the e of vel[e] is editorial.
- **Stamp box, `kedves | ceferi`.** A right bowl ends row 4 and a left bowl opens row 5. Normalized kedvese, the family's closing formula; this is a reading of an odd spelling. In row 3 the b is rounded and open, and word sense helps.
- **Row 3 önnek.** No dots are visible over o; accents and doubled letters (evel → evvel, osze → össze) are normalized.
- **Address.** The first letters of Szépreményű run under the postmark and are read by shape and from sister cards with the same address in clear.
- **People and events.** Who the goddaughter was, and what the party of rows 7–8 was, are not stated. The sender is known only as Feri.

## Review and what changed

A separate Claude Opus 5.5 agent reviewed the card, re-ran the command, made its own sign-by-sign transcription with its own key table, and read the whole text on its own enlargements. It agreed on 17 of 21 rows and returned **REVISE**: the reading stands, with four major and four minor findings. All were accepted after rereading the scan.

- Szépreményű had been spliced into the plain letter; it belongs to the address, as sister cards show.
- Row 10 first sign is a, not e, so akor = akkor and the ekkor option goes.
- Row 9 had two strokes too many in the ledger; it now shows only the four on the card, and the shortfall is disclosed.
- Row 16 had a phantom e sign; vel[e] is now marked editorial.
- Minor: blot markings aligned for the row 14 gy and row 11 p, az relaxed to a(z), and the claim of "no adjustment" withdrawn, since a stroke and two letters are supplied.

The key did not change, and neither did the sense of the message. After the review the solver also noted ha as a possible start of the row 14 group, as a suggestion only; the reviewer has not assessed this note.
