# hcp-1321 (pc_hcp_2): solution

Solver: Claude Opus 5.5, 2026-10-30. No earlier work exists on this number. The portal attaches no solution or transcription; I transcribed the card myself (`work/transcription.txt`).

## Summary

The card is mostly in clear English. Three lines in the middle are enciphered in a home-made shape-and-dot substitution. They read **SON & HEIR ARRIVED LAST NIGHT**.

## The card

Picture side: printed coloured view, "6073 The Lake. Chislehurst." No handwriting. Address side: Edward VII halfpenny stamp, addressed to Miss S. E. Fortescue (the portal says J. E.; the first initial has the same form as the S of "St." on the next line, so the evidence leans to S, though there is no J by this hand on the address to compare), South St. House, Meopham, Kent. The message is written sideways on the left half. Postmark: only fragments are legible; I could not read a place or date. The stamp dates the card to about 1902 to 1911.

Clear text, with the cipher block in place:

    Dear P. If fine will come
    [struck-out word] 6.40 (it's not altered.)
    (Tomorrow Friday evening)
    [cipher lines 1 to 3]
    All news later
    With love to you all
    Y[?] etc.  [monogram, perhaps A. B. or J. B.]

## Cipher type and key

Monoalphabetic substitution with geometric signs. The shape gives a block of the alphabet, and a dot inside the shape picks the letter. 23 signs, 13 distinct. Blocks run in alphabet order.

| Shape | Dot | Letter |
|---|---|---|
| Square | top left | A |
| Square | bottom right | D |
| Triangle | top | E |
| Triangle | lower right | G |
| Circle | top | H |
| Circle | left | I |
| Angle `<` | vertex | L |
| Angle `<` | lower arm | N |
| Angle `<` | upper arm | O |
| Diamond | top | R |
| Diamond | centre | S |
| Diamond | bottom | T |
| Caret `V` | no dot | V |

Only these 13 are attested. B, C, F, J, K, M, P, Q, U, W, X, Y, Z do not occur, and I do not assign them signs. The gaps suggest the missing corners and dots, but that is inference.

Transcription (card turned so the handwriting is upright): see `work/transcription.txt`.

    square/dot codes                                  plaintext
    DI:C AN:U AN:D  &  CI:T TR:T CI:L DI:T            SON & HEIR
    SQ:TL DI:T DI:T CI:L VE:0 TR:T SQ:BR              ARRIVED
    AN:V SQ:TL DI:C DI:B                              LAST
    AN:D CI:L TR:LR CI:T DI:B                         NIGHT

## Plaintext

Original (English): **Son & heir arrived last night**

English: a son and heir was born last night.

Slovak: Syn a dedič prišiel na svet včera večer. (Literally: "Syn a dedič dorazil včera v noci.")

The full card in Slovak: Drahá P. Ak bude pekne, prídem [prečiarknuté slovo] o 6.40 (nie je to zmenené.) (Zajtra, v piatok večer.) Syn a dedič prišiel na svet včera večer. Všetky novinky neskôr. S láskou vám všetkým, Y[?] atď. [monogram]

## Reproduce

From the repo root:

    python3 -I ciphers/hcp-1321/work/decode.py

It verifies the SHA-256 of all four image files, decodes `work/transcription.txt` with `work/key.json`, and prints the structure check below.

## Uncertainties

1. **The "&" is a reading, not a decipherment.** Line 1 has a thin looped scribble between the groups (crop `work/crops/amp.png`). It is not one of the shape signs. Its form and the set phrase "son and heir" make "&" the natural reading, but this rests on word sense. It could instead be a cancelled sign. Removing it leaves SON HEIR, so no enciphered letter depends on it.
2. **Sign identity in three places rests partly on the writer's slant.** I treat these pairs as one sign: circle with dot at upper right (line 1) and at top (line 3); triangle with dot at upper right (line 1) and at top (line 2); and the tilted diamond closing line 1 with the two top-dotted diamonds in line 2. Tilted shapes put "top" at upper right. The decoding confirms all three merges, but that is a consistency argument, not an independent reading.
3. **Sign 2 of LAST** is drawn as a parallelogram rather than an upright square. Its dot is top left, as in the A of ARRIVED, so I read it as the same sign.
4. **Single-use signs.** The caret `V` occurs once and shows no dot; its value comes from ARRIVED alone. The vertex angle L also occurs once: *arrived past night* fits every constraint, including the alphabet blocks (N, O, P as the angle block), and only idiom selects LAST. D (ARRIVED), G (NIGHT) and O (SON) are single-use as well. O is partly controlled: *sol* fails because the same angle sign is N in NIGHT, and the *sol ... light* strings are nonsense.
5. **Clear text.** The struck-out word before 6.40 is unreadable. The word before "etc." (perhaps "Y.W." or a form of "Yours") and the monogram are not firmly read. I do not know who "P." is or who signed.
6. **Postmark and date** are not read.

## Why I believe it

- Every one of the 23 signs decodes to a common English word, with no sign left over and no restoration.
- All 13 letters fall into unbroken alphabet blocks by shape: A D / E G / H I / L N O / R S T / V. A random assignment does this about 3.3e-05 of the time (computed by `decode.py`). This is a check on the key given the reading, not a language-free test: the letter values come from the English reading, it was computed after the key suggested it, and it relies on the three merges in uncertainty 2. It is still strong evidence.
- The order came from the text first: the search for a word with a doubled 2nd and 3rd sign found ARRIVED, and the block pattern then predicted the rest. Square A and D at opposite corners suggested the alphabet blocks, and HEIR, LAST and NIGHT followed.
- I searched the three merges in uncertainty 2 both ways. The merged reading is the one that gives the full sentence. `work/search2.py` reads a session corpus that is not in the repo, so that run cannot be repeated from this directory; the reviewer's `review/work/filter.py` covers the same ground independently and found no rival sentence.
- The content fits the card: "All news later" follows straight on from a private birth announcement.

Not checked: I did not search the web for a published solution of this card. The orchestrator confirmed there is no AI-register record, and the portal shows Not solved.

## Response to review 1

Verdict ACCEPT, six minor findings. I rechecked findings 1, 5 and 6 on the reviewer's crops of `work/hires/pc_hcp_2_adr.JPG`. The cipher reading, key and transcription did not change. `python3 -I ciphers/hcp-1321/work/decode.py` still gives SON & HEIR / ARRIVED LAST / NIGHT, 23 signs, 13 distinct.

1. **Brackets: fixed.** `review/work/paren.png` shows a closing bracket after "altered." and a second one after "evening"; `work/crops/msg2x.png` shows the opening bracket before "Tomorrow" on the printed "only". The clear text and the Slovak now show two separate asides.
2. **Single-use L: fixed.** Uncertainty 4 now names L, the *past night* alternative, and D, G and O.
3. **Block check wording: fixed.** It is now described as a check on the key given the reading.
4. **`work/search2.py` reproducibility: disclosed.** The corpus was a session scratch file and no longer exists here, so I do not claim the run can be repeated. "Why I believe it" now says so and points to the reviewer's `filter.py`.
5. **Slovak closing: fixed.** It now reads `Y[?] atď.`, matching the English. `review/work/sig.png` shows Y plus one more letter, then "etc."
6. **Addressee initial: fixed.** In `review/work/initials.png` the initial matches the S of "St.", so the text now says the evidence leans to S. This is not proven, and the portal's J. E. is still noted.

I did not address the items the reviewer could not verify, because the scans do not settle them: postmark place and date, the struck-out word, the second letter after Y, the monogram, the scribble as "&", and the identities of P. and the sender. No web search for a published solution was made.
