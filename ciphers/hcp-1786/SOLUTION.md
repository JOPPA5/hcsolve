# hcp-1786 / pc_hcp_467 — solution (Claude Opus 5.5, 2026-10-30; revised after review 1)

Status: **the enciphered message on the address side is read in full; a faint pencil note on the picture side is NOT read** (see Uncertainties). No published solution was found and the portal attaches none. No earlier work exists on this number. Own decipherment.

## Cipher type and key

A home-made Czech substitution, close to an abugida: digits and a few letter-like signs for consonants, with vowels shown as marks on or after the sign. Word spaces and punctuation are kept.

| Sign | Value | Sign | Value |
|---|---|---|---|
| 0 | l (a bare 0 at word start = o, in one word) | 8 | ch, h |
| 1 | d, t (ď, ť) | 9 | k |
| 2 | n | x | z, ž |
| 3 | m | ζ-shaped sign (`j`) | j |
| 4 | r, ř | e-shaped sign (`c`) | c, č |
| 5 | s, š | v | v |
| 6 | b, p | a | a (only as a word-initial letter) |

Vowels:

- `-` = e/é; `·` = i/í/y/ý; `··` = u/ú/ů; a caron over a dash = ě.
- **A stroke through a sign adds o** (crossed 1 = to/do, crossed 4 = ro, crossed 9 = ko, crossed 8 = ho, crossed 2 = no, crossed 6 = po, crossed 5 = so, crossed 0 = lo).
- **A heavy pen stroke on a sign adds a/á.** Twelve of the 15 a's are written this way; two are the sign a ("ale", "a"); the one remaining, "až", is a bare x with a ring. The other signs of the same words stay plain. The signal is not clean: crossings also look thick and blots exist, so heavy status was judged by eye together with the reviewer's stroke-width map. The 0 of "chladna" and the 4 of "krásu" are the weakest cases. The same rule was found independently on hcp-1787.

A small caron or ring over a sign gives ř, š, ž, č, ť. Voiced and voiceless pairs share a sign (b/p, d/t).

## Plaintext (Czech, normalised)

Přijměte prozatím tímto díky za psaníčko, nesmíš se, zlatíčko, zlobiti, vždyť jsem ti psal, že jsou to klepy. Dnes jsem v Kutné Hoře, pro řepové semeno. Zaseto již máme, ještě kousek řepy a bude hotovo. Těším se, až přijedete dříve domů. Jsou zde chladna, ale zlaté sluníčko přece otevírá rychle krásu přírody.

The sign-by-sign transcription is the block `T` in `work/decode.py`, line by line.

## English

Accept for now, with this, my thanks for the little letter. You must not be cross, little darling; after all I wrote to you that it is gossip. Today I am in Kutná Hora, for beet seed. We have it sown already, one more bit of beet and it will be finished. I look forward to your coming home sooner. There are cold spells here, but the golden sunshine is nevertheless quickly opening up the beauty of nature.

## Slovak

Prijmite zatiaľ touto cestou vďaku za listček. Nesmieš sa, zlatíčko, hnevať, veď som ti písal, že sú to klebety. Dnes som v Kutnej Hore, kvôli repnému semenu. Zasiate už máme, ešte kúsok repy a bude hotovo. Teším sa, až prídete skôr domov. Sú tu chladná, ale zlaté slniečko predsa rýchlo otvára krásu prírody.

## Command

```bash
python3 -I ciphers/hcp-1786/work/decode.py
```

It checks the four source hashes, decodes the 53 words of `T` mechanically with no free vowel insertion, prints the literal text, compares each word with the reading after folding b/p, d/t, h/ch, i/y and accents, and exits 1 on any mismatch outside five listed exceptions. It reports 0 mismatches. Replacing a reading with the old "To seto"-type form makes it fail.

## Uncertainties

1. **Picture-side pencil note, unread.** About five faint lines in pencil over the sky and the church, partly under the portal watermark. It runs on a baseline in joined strokes, unlike the separate signs of the cipher, so it looks like ordinary handwriting, but I cannot prove that. Only one word looks like "Tebe". The lower-right block has a large open O followed by tall stems, which resembles the signature "Otta" on the picture side of hcp-1787; that is a hypothesis only. The cipher text on the address side ends in a full stop and reads as complete without the note.
2. **Five words differ from the literal decoding** (listed by the command): "zlat(í)čko" has no written í; "dnes" has a dot after the 1, so the literal is "dines", a slip or stray; "Hoř(e)" has no written e, only a comma-like stroke; "(a)ž" is a bare x with a ring and no heavy stroke; "otevírá" starts with a bare 0, the same glyph as l.
3. **Calls that rest on word sense:**
   - x and crossed 1 are near-homographs here, both X shapes of similar height. "za", "Zaseto", "to", "tímto", "do(mů)" and "hotovo" rest partly on sense. In "Zaseto" the first sign could only be z with heavy a: "za" is the only reading that yields a word.
   - "hotovo": the last sign is read as crossed v.
   - "vždyť": the first sign lies between 0 and v in shape.
   - The bare 0 in "otevírá" (item 2).
4. **Marks read through:** the í position in "přijměte" (a dot with a blot on top); the 6 of "přijedete" (a blot and a stroke, a real anomaly); a stroke on 5 in the second "se" of line 8. They are marked `*` in `T`. A stray accent stands above the e of "pové"; it fits é.
5. **"krásu"** is written above the line with a curled insertion mark, between "rychle" and "přírody". The insertion point is the writer's mark plus the sense.
6. **Mixed address:** "Přijměte" and "přijedete" are plural or polite; "nesmíš" and "ti" are singular. The readings are firm, so this is a feature of the text (perhaps the writer is addressing a household). It is kept in the translations. Note also that "chladna" as a plural noun (cold spells) is period usage.
7. **Omitted caron:** the first r of "přírody" has none. "nesmíš" and "že" do have theirs (the first version of this file said otherwise).
8. **Sender and date:** the sender is not named in the cipher. The printed imprint gives 1907, a printing date; the postmark is not legible enough to date the card.
9. **Address (plain):** "Spanilomyslné(?) Slečně / Marušce Pařezové, / (u p. Pařeza Pekařská ul. 12.) / Brno. / Morava." The first word is doubtful in the middle and is crossed by the postmark; the rest is clear.

## Why it is correct

- Every sign on the address side is used, in natural Czech sentences on a consistent farm and family subject (sowing, beet, weather, Kutná Hora, which is also the picture on the card).
- The decoder inserts no letters: 48 of 53 words come out of the written signs alone, and the five others are disclosed.
- Independent anchors: "v Kutné Hoře" on a Kutná Hora card; "dnes jsem", "jsem ti psal", "že jsou to klepy", "těším se, až přijedete", "ale zlaté sluníčko přece".
- The line-end double stroke falls inside "ře=pové", a real hyphenation at a syllable boundary.
- Control on hcp-1787, read-only: its plain "½ 7 hod" sits among signs that give "jest ½ 7 hod ráno, neděle". The same key, including the heavy a, was reached there by a separate solver. Both cards go to Maruška/Mařenka Pařezová in the same style of address ("Spanilé Slečně" on 1787). I have not tested the hand.

Credit: Claude Opus 5.5 only.

## Response to review 1

Verdict REVISE. All eight findings addressed. The method and all other words are unchanged, so this closes without a second round.

1. **"za psaníčko": accepted, fixed.** On z_x65.png the gap after x is plainly a word gap, and both x and 5 are heavy. The comma after the word is on the card too. T, plaintext, English and Slovak are changed; the old uncertainty is dropped.
2. **"Zaseto": accepted, fixed.** On z_seto.png the first stroke is the heaviest on the card and the gaps within the group are equal. T, plaintext and translations are changed. The homograph caveat is in uncertainty 3, and "hay or sowing" is gone from the reasons.
3. **Heavy stroke = a: accepted, fixed.** Key section rewritten with the limits; 12 heavy signs marked `#` in T; no longer called blots, except the genuine ones.
4. **Transcription: accepted, fixed.** T now has the dot in "dnes", `*` on the 5 of "se" and the 6 of "přijedete", the accent on "pové" and `+` for the insertion "krásu". The claim "no leftover signs" is replaced by the exception list.
5. **"nesmíš": accepted, fixed.** The curved mark is plainly there on z_nesmis2.png; T has `5^`. The caron on "že" is also present on the card, so the old statement that it was omitted was wrong too, and is corrected.
6. **Address: accepted, with one difference.** I read "ul. 12." at 4x (work/crops2/addr_street.png), not "ul.? č.? 12": the shape after "ul." is the number. Now given in uncertainty 9 with the link to hcp-1787.
7. **vy/ty: accepted.** Uncertainty 6; the translations keep the mix.
8. **Decoder: accepted, fixed.** `work/decode.py` is now a real decoder with no free vowels and a stated exception list, checked with a negative test. Run on 2026-10-30: hashes OK, 53 words, 0 mismatches, 5 of 5 listed exceptions.

The reviewer's further points are also taken: "vždyť" joins the word-sense list, and I tried the "Otta" comparison once (work/crop8.py), with the result in uncertainty 1.
