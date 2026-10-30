# HCP 1294 (cpc_1912-03-26_HU__HU_Jasz Arokszalas_jolanka-12): Feri to Jolánka Tóth, "why take on so much work?"

Human solver: Tomáš Pavuk

**Status: PARTIAL. All 209 cipher signs are transcribed and decoded and 200 give a clear message, but one 9-sign word in row 8, literally `oszeholad`, is not understood. Independent review 1 verdict REVISE; no sign misread, findings addressed. No register entry is made for this card.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1294 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1294), part of Tobias Schrödel's cryptographic postcards collection. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, date 1912-03-26, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The orchestrator's check of the AI Decipherment Register on 2026-10-30 found no record for it, and no published solution was seen.

The cipher text is on the address side, in red-pink ink, in 15 rows. The address itself is in plain writing: *Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás* (roughly "To the promising young lady Jolánka Tóth, Jász-Árokszállás", Hungary). Under the place of the lost stamp there is a short plain message in Latin script, signed Feri. The picture side has a printed Hungarian verse (*Szebb a pipacsos mezőn…*), which is not cipher text.

The card belongs to a family of Hungarian postcards from Feri (Holes Feri on other cards) to his sweetheart Jolánka. Others are deciphered in this repository, for example HCP 1212, 1213, 1216, 1217, 1218, 1243 and 1301.

![Address side with the 15 cipher rows (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, printed verse, no cipher (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The key was **transferred unchanged from the finished family cards**, not derived here. The sign table of HCP 1216 fitted at once: row 1 gave *kedves Jolánkám*, row 2 *becses sorait*. Earlier work on the sister cards was done by an OpenAI GPT solver (GPT-6 / GPT-6 Astra / GPT-6.1 Sol), with HCP 1216 completed by Claude Opus 5.5. This card had no earlier work. Claude Opus 5.5 read it from enlarged crops of the unconverted hires scan, sign by sign and without OCR, into a ledger of 209 tokens, and decoded the ledger with a short script that also checks the SHA-256 of the scans.

From the repository root the reading is reproduced with:

```sh
python3 -I ciphers/hcp-1294/work/decode.py
```

In review a separate Claude Opus 5.5 agent made its own crops, transcribed all 15 rows as shape names, took values from the family table and decoded with its own script. Its reading differs in 4 places only, all of them the disclosed h/p and d/n homographs, where it kept the shape value.

## Key

Monoalphabetic substitution with invented graphic signs.

| Plain | Sign | Plain | Sign |
|---|---|---|---|
| a | two bars | l | wave |
| b | six-like | m | three short strokes |
| cs | opposed bowls | n | two short strokes |
| d | short tick + long stroke | o | cursive loop |
| e | three bars | r | F-like |
| g | open loop with descender | s | right bowl |
| h / p | tall stroke + short tick (one homograph) | t | gamma |
| i | crossed curve with dot | u | plain cross |
| j | inverted T | v | chevron |
| k | section mark | y | low descender |
| z | crossed diagonal with long tail | | |

Sz is written s + z. Dots or two short strokes over o give ö/ő. Acute accents are not written.

## Plaintext

Literal decipherment, row by row:

```text
01 kedvesjolankam
02 becsessoraitkö
03 szönettelmegkap
04 tamsajnalatalol
05 vasomolysokat
06 dolgolgozik
07 minekvalalannyi
08 munkatoszeholadȯk
09 vetlenelmegyek
10 barnagyonroszidö
11 vancsakholnaprajo
12 idölennenajdszo
13 valbövebbenisten
14 veleaviszontlatas
15 ra
```

**Hungarian (normalized; `[ ]` supplies letters, ‹ › marks the unread word):**

Kedves Jolánkám! Becses sorait köszönettel megkaptam. Sajnálat[t]al olvasom, oly sokat dolgozik. Minek vál[l]al annyi munkát ‹oszeholad› okvetlen elmegyek, bár nagyon ros[s]z idő van, csak holnapra jó idő lenne. Majd szóval bővebben. Isten vele, a viszontlátásra.

Under the stamp, plain: Csókolja számtalanszor hű[n?] kedvese, Feri.

**English:**

My dear Jolánka! I received your esteemed lines with thanks. I read with regret that you work so much. Why do you take on so much work ‹oszeholad, not understood› I shall certainly go, although the weather is very bad; if only there were good weather tomorrow. More by word of mouth later. Farewell, until we meet again.

Under the stamp: Kissed countless times by your faithful sweetheart, Feri.

**Slovak:**

Moja milá Jolánka! Vaše vzácne riadky som s vďakou dostal. S ľútosťou čítam, že tak veľa pracujete. Načo si beriete toľko práce ‹oszeholad, nezrozumené› určite pôjdem, hoci je veľmi zlé počasie, len keby bolo zajtra pekne. Ostatné podrobnejšie ústne. S Bohom, dovidenia.

Pod známkou: Nespočetnekrát Vás bozkáva Váš verný milý, Feri.

## Uncertainties

**The row 8 word `oszeholad`.** The signs are clear (below), but no Hungarian word was found, and it is not known whether the word closes the remark about work or opens the clause about the trip, since *Okvetlen elmegyek* is a complete sentence on its own. The boundary before `ok` is also an assumption, made because `ok` + `vetlen` gives *okvetlen*. The first loop has an extra lead-in stroke that fits no sign of the key. Three leads are recorded, none adopted, all resting on word sense:

- Prefix *össze-*: this writer spells it with one sz (HCP 1288 has *összehoz* so spelled). *Összehoz* itself does not fit, because the sign after o is a clear l, not z.
- Tail *holnap* ("tomorrow"): it suits *csak holnapra* three rows below, and HCP 1319 has literal `holna`, but it needs two slips (n dropped, d for p) and leaves `osze` unexplained.
- *Összeolvad* ("melts together"), perhaps of a thaw: it needs a dropped v and an unwanted h.

![Row 8, end of the row: o with lead-in stroke, s, z, e, h/p (work/crops/z8.png)](../work/crops/z8.png)

![Row 8, continued: o, l, a, d, dotted o, k (work/crops/z8b.png)](../work/crops/z8b.png)

**Other points.**

- h/p are one sign and d/n differ only in stroke length, so these calls rest on word sense: p in *megkaptam* and *holnapra*, n in *minek* and *okvetlen*. In the row 8 word h/p is undecided.
- Row 12 literally has `najd`, two strokes where m has three; *majd* is a correction of a slip.
- Ink blots cover the j of *majd* (row 12), a of *viszontlátásra* (row 14), a of *bár* (row 10), and the ö of *bővebben* (row 13) is thickened or overwritten. All remain legible and word sense agrees.
- A single dot stands over the o of *okvetlen*; no ö is needed there and it is ignored. Dots under k-signs are a habit of this writer and are not punctuation.
- Row 5 *oly* has wave and y joined. *(H)ogy* is not preferred, since the writer uses a separate g + y elsewhere; the sense is the same.
- The writer's spellings are normalized: `dolgolgozik` to *dolgozik*, `valal` to *vállal*, `sajnalatal` to *sajnálattal*, `rosz` to *rossz*. Accents are supplied by the editor.
- Under the stamp the third line ends in `hű` plus a short stroke at the torn edge, so *hűn* is possible.
- The date 1912-03-26 is the portal's. Neither postmark's date could be read, so it was not verified.

## Review

Review 1 (a separate Claude Opus 5.5 agent, verdict REVISE) re-ran the command, decoded independently, checked every sign against the pixels and found no misread sign. Its findings, and what changed:

1. The card was not labelled partial. It now is, and no register entry is written.
2. A spelling lead was missed: the writer's one-sz *össze-*. It was tested with `work/row8_test.py` against the 6149 word forms of the family's solutions and recorded; it does not resolve the word.
3. The word's function was claimed without support. The attachment is now stated as unknown, and the punctuation at the word was removed.
4. The dots under k were misdescribed. Corrected as above.
5. Two damaged signs (rows 10, 13) were undisclosed. Now disclosed.
6. The ledger header listed unused tokens. Corrected.

No sign reading changed. The reviewer could not verify the row 8 word, the date, or the accents. Family cards 1285–1319 were compared only through their solutions' vocabulary, and no Hungarian dictionary was available.
