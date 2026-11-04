# hcp-1090 – Solution (round 1, revised after review 1)

Card: HC Portal cryptogram 1090, `cpc_1911-04-01_DE_Oppenau_DE_Goggingen_` (T. Schrödel collection).
Picture postcard "Titisee" (Black Forest), posted at Oppenau (Renchtal) on 1 April 1911, to
"Herrn Ernst Häusler (Eisenb. Assist.), Göggingen, Amt Meßkirch, Baden". Portal status: Not solved, no
transcription or solution attached. Solved by Claude Opus 5.5 on 2026-11-03; no earlier work on this
number, and a short web search found no published solution of this card.

## Cipher type and key

Morse code (German letter set: Ä `.-.-`, Ö `---.`, CH `----`), written in pen as vertical columns of
dots and dashes on the left half of the address side. Register label: `MASC/Morse`.

- Reading order: the writer turned the card 90° anticlockwise, so the text runs in 16 columns read
  **from the rightmost column leftwards, each column top to bottom**. The last column (c00) is a short
  signature written at the bottom left, beside the end of c01.
- Writer's own sign values: **H is written with five dots `.....`** in all six places where H occurs
  (HERZLICH, GEHT, HIER, VIERZEHN, SEHR, WIEDERSEHEN); the standard four-dot H never occurs.
  `.....` is the standard Morse sign for the digit 5, so the writer consistently used the sign for 5
  in place of H `....` (6 times, plus once more in GR_SSE, see uncertainty 1).
  `----` = CH (DOCH, SCHÖN, ICH, MICH, DICH, HERZLICH).
- Two letter groups were added later in grey ink inside insertion loops: `----` (CH of the first ICH in
  c05) and `.....` (H of VIERZEHN in c10). One letter is written in ordinary handwriting, not Morse
  (see uncertainties).
- No word spaces are visibly wider than letter spaces; word division is editorial.

Transcription: `work/transcription.txt` (one line per column, letters separated by spaces).

## Command

From the repo root:

```
python3 -I ciphers/hcp-1090/work/decode.py
```

It checks the SHA-256 of the four scans, decodes `work/transcription.txt` column by column, and prints
the literal letter stream and the edited plaintext.

## Plaintext (German)

Literal letter stream (word division editorial):

LIEBER ERNST WIE GEHT ES DIR O WÄREST DU DOCH HIER WIE SCHÖN WAR ES VOR VIERZEHN TAGEN UND JETZT IST
ES MIR SO LANGWEILIG KOMME BALD ICH FREUE MICH SO SEHR AUF DAS WIEDERSEHEN ICH GRuHSE DICH HERZLICH
DEINE ANNA

Edited (one emendation, GRuHSE → GRÜSSE; punctuation added):

> Lieber Ernst! Wie geht es dir? O wärest du doch hier! Wie schön war es vor vierzehn Tagen, und jetzt
> ist es mir so langweilig. Komme bald. Ich freue mich so sehr auf das Wiedersehen. Ich grüße dich
> herzlich, deine Anna.

Unenciphered note along the divider line (pen): "31. III. 11. ab. 9 U[hr]" = 31 March 1911, evening,
9 o'clock (the last letters are cut by the card edge). The postmark (Oppenau, 1.4.11) follows the next
day.

## English translation

Dear Ernst! How are you? Oh, if only you were here! How lovely it was a fortnight ago, and now I am so
bored. Come soon. I am looking forward so much to seeing you again. I greet you warmly, your Anna.
(Written 31 March 1911, 9 p.m.)

## Slovak translation

Milý Ernst! Ako sa máš? Ach, keby si tu bol! Aké to bolo krásne pred štrnástimi dňami, a teraz sa tak
nudím. Príď čoskoro. Tak veľmi sa teším na naše opätovné stretnutie. Srdečne ťa pozdravujem, tvoja Anna.
(Písané 31. 3. 1911 o 21. hodine.)

## Uncertainties (all disclosed)

1. **GRÜSSE (c02).** After G R the writer left a gap in which a small letter is written in grey ink in
   ordinary handwriting (it looks like "3s" in the card's normal orientation; in writing orientation it
   resembles a script u with a mark above it). On the pixels it is a Kurrent u with a single curl above
   (the u-hook), not two umlaut dots; it is read as ü only from sense (Kurrent ü is often written with the
   hook alone, and the writer apparently did not know the Morse for ü). The following groups are
   `.....` `...` `.`; since the writer uses `.....` (Morse 5) for H everywhere else, the literal reading is
   GRuHSE. GRÜSSE ("ich grüße dich herzlich") is certain
   from sense; the five-dot group for the first S is taken as a slip. This word rests on word sense.
   The grey mark could alternatively be an unrelated later annotation (e.g. a number "35"); the reading
   of the word would not change.
2. **G of TAGEN (c09):** the first dash of `--.` ends in a heavy ink blot. There is no gap between dash
   and blot, so it is read as one dash (G); a split into `-.` `-.` (TANNEN) would need a gap that is not
   there. TAGEN is also required by "vor vierzehn Tagen".
3. **R of DIR (c14):** written to the left of the column foot, beside the final I, because the column
   reached the card edge.
4. **Last CH of MICH (c05):** the fourth dash sits right at the bottom edge, short but visible.
5. **Signature ANNA (c00):** letters are crowded (inner gaps up to 23 px, letter gaps 38–47 px on the
   hi-res scan); `.- -. -. .-` is the only split that gives a name. The sender's surname is not given.
6. Word division and punctuation are editorial. "Komme bald" is read as written (KOMME).
7. The picture side (Titisee view) shows no hidden writing. Nothing is written around or along the edges
   of the stamp (Germania 5 Pf., intact on the scan); what may lie under the stamp could not be examined,
   since only scans are available.
   The address and the date note are plain handwriting.

## Why I believe it is correct

- Every Morse mark on the card is used; there are no leftover groups. One tiny faint speck (about a fifth
  of a dot) just before the five-dot H of GEHT in c14 was judged a pen touch and not counted; counting it
  would give six dots, which is no Morse sign. All 16 columns decode to
  continuous, grammatical German of the period, a typical love/friendship postcard, with the expected
  opening (Lieber Ernst), closing (ich grüße dich herzlich, deine Anna) and signature.
- Independent check: `work/blobs.py` detects ink marks automatically on the hi-res scan and
  `work/verify_marks.py` compares them column by column with the hand transcription
  (`python3 -I ciphers/hcp-1090/work/verify_marks.py ciphers/hcp-1090/work` with a Python that has
  numpy). Eight columns (c15, c13, c12, c11, c07, c04, c01, c00) match mark-for-mark with all
  letter gaps larger than all inner gaps; the remaining differences were each inspected on enlarged
  crops and are detector artefacts (a blotted dash read as one long mark, a large round dot classed as
  a dash, the grey insertion loops, the printed publisher logo and "Titisee" imprint crossing c02, c03
  and c05, the card edge). Details in NOTES.md.
- The two grey insertion loops supply exactly the letters missing at those points (ICH, VIERZEHN),
  which confirms both the reading order and the writer's five-dot H.
- Context fits: Oppenau and Titisee are in the Black Forest (Baden), the addressee is a railway
  assistant in Göggingen (Amt Meßkirch, Baden), and the date note agrees with the postmark.

## Response to review 1

Review 1 verdict: ACCEPT, four minor findings. All four addressed; the reading is unchanged.

1. **Nature of the five-dot sign (minor) – fixed.** Agreed: `.....` is the standard Morse digit 5. The key
   section now says the writer consistently used the sign for 5 in place of H (6 times, plus once in GR_SSE).
2. **Grey letter is u, not ü, on the pixels (minor) – fixed.** Agreed after looking at the reviewer's
   enlargement (review/work/z_mark2.png): a single curl above a Kurrent u, no two dots. work/decode.py now
   prints the literal stream as GRuHSE (u for the plain-script letter), the transcription legend says so,
   and the emendation is GRuHSE → GRÜSSE, resting on word sense (uncertainty 1). Re-ran
   `python3 -I ciphers/hcp-1090/work/decode.py`: hashes OK, literal stream ends ICH GRuHSE DICH HERZLICH
   DEINE ANNA, emended plaintext unchanged.
3. **Stray speck before H of GEHT (minor) – fixed.** Disclosed in "Why I believe it is correct": judged a pen
   touch (about a fifth of a dot, much fainter), not counted.
4. **Stamp (minor) – fixed.** Uncertainty 7 now states plainly that nothing is written around or along the
   stamp edges (review/work/z_stamp.png: Germania 5 Pf., only the Oppenau cancellation crosses it) and that
   under the stamp cannot be examined from the scans.
