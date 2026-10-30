# HCP 1432 / pc_hcp_113 — Morse code postcard, 12 Aug 1907

The whole message is read. All 42 Morse groups on the card are transcribed and
decoded. Three groups are written irregularly by the writer and are read from
context. All three are disclosed below. Review 1 (REVISE) addressed; see the
response at the end.

**Credit.** The earlier OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) did the
following on 2026-10-26: the portal capture (all three tabs, both scans and
their hashes), the 180-degree orientation, a 42-group inventory, the readings
KINDNESS ON SATURDAY / VERY TIRED / REA{.-.-}HED HOME, the cursive context, and
the anomaly and code-variant checks (`work/audit-anomaly.py`,
`work/historical-code-check.md`). It stopped short of a complete claim because
of the `.-.-` group.

On 2026-10-29 Claude Opus 5.5 re-read every group on enlarged crops of
`source/address.jpg`, including colour and pixel-value checks where ink crosses
the printed "POST CARD" lettering. It corrected the closing group (see U2),
wrote `work/transcription-full.txt` and `work/decode_full.py`, and made this
claim.

**Context.** Portal status "Not solved", tags Postcard HCPortal collection /
Morse code. The portal attaches no transcription or solution. Postmark
TOTTENHAM (posting office), 11.15 AM, 12 AU 07. Addressed to Mrs. G. Groves,
90 Westbourne Rd, Barnsbury N. (Islington, north London). The address was
misread as "90 West Green Rd(?), Tottenham" in round 1 and corrected after
review 1. The picture side (Virginia Water, falls) carries no cipher. The
sister card hcp-1433 (same addressee, 2 Aug 1907) is also Morse, and its Morse
contains the name LOUIE; this card is signed "Louie" in cursive. (hcp-1433
leaves open whether LOUIE there is the writer's signature or the addressee's
pet name.) I found no
published solution of this card.

## Cipher and key

- **Type:** International Morse code, written as pen dots and dashes. Each
  letter is closed by a long slanted stroke (`/`). No word spaces are marked.
  The Morse words are embedded in an ordinary cursive English letter.
- **Key:** the standard International Morse alphabet A–Z. Only letters occur.
- **Orientation:** rotate `source/address.jpg` by 180 degrees. The message is
  on the right half.

## Transcript (`work/transcription-full.txt`, literal pen strokes)

```
thanks-1  -.- / .. / -.                                KIN
thanks-2  -.. / -. / . / ... / ... / --- / -. / ...    DNESSONS
thanks-3  .- / - / ..- / .-. / -.. / .- / -.--         ATURDAY
tired-1   ...- / .(-) / .-. / -.-- / - / ..            VARYTI (read VERYTI)
tired-2   .-. / . / -..                                RED
home-1    .-. / . / .- / .-.- / .... / . / -.. / ....  REA{.-.-}HEDH
home-2    --- / -- / .                                 OME
closing   - / -. / ..- / .                             TNUE
```

## Plaintext

Morse parts are in capitals. Lower case marks the three editorial readings.

- KINDNESS ON SATURDAY
- VeRY TIRED (literal: VARY TIRED, the dash of the A is crossed by the slash)
- REAcHED HOME (literal: REA{.-.-}HED HOME)
- TrUE (literal: TNUE)

The full card, with the cursive given as context (the cursive is not
ciphertext):

```text
My D. S.[initials uncertain] Thank you
dear for all your KINDNESS ON SATURDAY
evening I am A.1. this
a.m I trust you were
not VERY TIRED when you
REACHED HOME I am so
fearfully lazy. hope
you are well Your
[faint cursive] TRUE Friend
Louie
```

- **English:** "My D. S. Thank you, dear, for all your kindness on Saturday
  evening. I am A1 (in fine form) this morning. I trust you were not very tired
  when you reached home. I am so fearfully lazy. Hope you are well. Your true
  friend, Louie."
- **Slovak:** „Môj/moja D. S., ďakujem ti, drahá/drahý, za všetku tvoju
  láskavosť v sobotu večer. Dnes ráno som na tom výborne. Dúfam, že si nebol(a)
  veľmi unavený(á), keď si prišiel/prišla domov. Som taký(á) strašne lenivý(á).
  Dúfam, že sa máš dobre. Tvoj(a) verný(á) priateľ(ka) Louie.“

## Command (run from the repo root)

```sh
python3 -I ciphers/hcp-1432/work/decode_full.py
```

It checks the SHA-256 hashes of all files in `source/` against
`work/source-sha256.json`. It then decodes every group of
`work/transcription-full.txt` literally (a dash crossed by the closing slash,
written `(-)`, counts as a dash). A non-alphabet group is printed as
`{...}`. Finally it prints the reading with the three disclosed editorial
letters in lower case.

## Uncertainties

- **U1, home-1 group 4 `.-.-`.** Four marks: dot, dash, dot, dash. The first
  is a heavy oval (about 9 px wide, larger than the other dots on the card) but
  is still a dot, not a dash; reading it as a dash gives `--.-` (Q), no better. This is
  not a Morse letter of the A–Z alphabet. (In Continental Morse it is Ä, which
  makes no sense here.) The writer reversed the elements of C (`-.-.`). The
  reading REACHED HOME is certain from context ("I trust you were not very
  tired when you ...ed home"), but the letter as written is not C. The earlier
  GPT checks remain valid: no historical code gives C = `.-.-`, and splitting
  the group with a missing slash gives no C either.
- **U2, closing group 2, read `-.` (N), not `.-.` (R).** The earlier transcript
  had `.-.`. On the pixels, the group lies inside the bowl of the printed
  reversed "P" of POST: a short dash, then a dot after the P stem, then the
  slash. I checked the left curve of the P bowl, where a leading dot would be,
  by luminance and hue. Its pixels are uniformly brown print. Where ink does
  cross print on this card (the slash through the "O"), the print shows
  measurably darker, and no such darkening is present here. So no leading dot
  is visible. The writer either dropped the dot or one is invisible on the
  print. Context ("Your ... Friend", with the cursive "Your" and "Friend"
  around it) gives TRUE. The writer's other four R's (SATURDAY, VERY, TIRED,
  REACHED) are all correct `.-.`, so this is a single slip.
- **U3, before the closing Morse** there is a faint, half-dry cursive scribble
  ("…ue"-like) partly under the printed "T"/"S". It is not Morse. It may be a
  false start of "true". I have not read it, and it is not part of the
  decipherment.
- **U4, tired-1.** A raised dot stands right after the cursive "not", higher
  than the Morse line. I read it as the cursive full stop or t-mark, not as a
  fifth element. Counting it would give `....-` (digit 4) instead of V and
  destroy VERY. The final S of thanks-2 has its third dot over the printed
  "S" of LANGSDORFF; that dot is visibly darker than the print.
- **U5, tired-1 group 2 (the E of VERY), crossed dash.** After the E-dot the
  writer drew a full dash (scan x 695–717, y 350–354 in the 180°-rotated
  frame) and then drew the letter-closing slash straight through it, so the
  mark looks like "†". No slash separates the dot from this dash. Taken
  literally the group is `.-` (A), giving VARY. Either the writer started an R
  or A by mistake and cancelled the dash with the slash, or simply miswrote.
  VERY is certain from the sentence ("not ... tired when you reached home")
  and the cursive context; I read E. This was missed in round 1 and added
  after review 1.
- **U6, thanks-3 group 3 (U of SATURDAY), faint dash.** The pen runs almost
  dry here (the T dash is also grey). The U dash is a very faint horizontal
  band with only a dot-sized dark end; without it the group would be `...`
  (S). The band is slightly bluer than the neutral grey watermark and runs
  horizontally, not along the watermark lines, so I read `..-` = U. SATURDAY
  confirms it.
- **Cursive context.** The salutation initials ("D. S."?), "A.1.", and the
  signature "Louie" are ordinary handwriting readings, not cipher results. The
  name Louie agrees with the sister card hcp-1433. The writer's and the
  addressee's genders are not established.

## Why I believe it is correct

- **Coverage.** The transcript accounts for every Morse run on the card. 39 of
  the 42 groups decode literally to the letters of correct English words. The
  other 3 are single-letter writer slips (`.-.-` for C, `.-` with a crossed
  dash for E, `-.` for R), and the surrounding letters fix the intended word
  in each case.
- **Coherence.** Each Morse word fills a grammatical gap in the cursive letter:
  "all your [kindness on Saturday] evening", "not [very tired] when you
  [reached home]", "Your [true] Friend".
- **Context.** The card is a 1907 Tottenham postcard to the same addressee as
  hcp-1433, which uses the same pen-Morse style (letters closed by slashes),
  and the cursive signature "Louie" matches the name in that card's Morse (whose
  role there, signature or pet name, is open).
- **Key.** The key is the standard International alphabet. Nothing is fitted
  to this card.

## Response to review 1

Verdict REVISE, five findings. All addressed; the plaintext is unchanged.

1. **major – crossed dash in VERY: fixed.** I confirmed the mark on my own
   enlargement of the rotated scan and on `review/work/t1z.png` /
   `cross.png`: dot, then a full dash with the closing slash drawn through
   it, and no slash between the dot and the dash. `work/transcription-full.txt`
   now records the group literally as `.(-)` with a header note. The decoder
   decodes it literally as A (`VARYTI`) and lists it as the third editorial
   reading (E). New uncertainty U5 explains both readings. The coverage claim
   is now 39 of 42 literal plus 3 disclosed slips. Re-run of
   `python3 -I ciphers/hcp-1432/work/decode_full.py`: `source hashes OK`, 42
   groups, 1 non-alphabet group, 3 editorial readings, literal
   `KIN | DNESSONS | ATURDAY | VARYTI | RED | REA{.-.-}HEDH | OME | TNUE`,
   reading `KINDNESSONSATURDAY / VeRYTIRED / REAcHEDHOME / TrUE`.
2. **minor – address: fixed.** On the address side in its own orientation
   (the message is written upside-down relative to it) the address reads
   "Mrs G. Groves, 90 Westbourne Rd, Barnsbury N." Tottenham is only the
   posting office in the postmark (TOTTENHAM, 11.15 AM, 12 AU 07). The
   context paragraph is corrected.
3. **minor – faint U dash in SATURDAY: disclosed** as U6 and noted in the
   transcript header. I agree with the reviewer's reading `..-`.
4. **minor – heavy first dot of `.-.-`: disclosed.** U1 no longer says "four
   clear marks"; it describes the heavy oval first dot and the `--.-` (Q)
   alternative. Conclusion unchanged.
5. **minor – hcp-1433 cross-reference: qualified.** Context and "Why I believe
   it is correct" now say that hcp-1433 leaves open whether LOUIE there is a
   signature or a pet name. The genders and roles remain open.
