# hcp-1095 (cpc_1905-06-23_USA_Fultonville, NY) - solution, round 1

Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. No earlier solver work exists on this number;
the orchestrator (Claude Opus 5.5) captured the portal tabs and scans the same day.
No published solution was found or used: the portal status is "Not solved" with no transcription or
solution attached, and a web search ("Raymond Donaldson" Fultonville 1905 postcard Morse) found nothing.

## The card

- Address side: "PRIVATE POST CARD", 1-cent Franklin stamp (1902 series), postmark FULTONVILLE N.Y.
  Addressed in clear cursive: "Raymond Donaldson, Fultonville, New York." Pencil "119" and "Box 15" are
  later collector/dealer notes. The stamp is in place; nothing shows around or through it, so what may
  lie under it cannot be checked from the scans. No other writing on the address side.
- Picture side: printed view "M. E. CHURCH, FULTONVILLE, N.Y." (no writing in the picture). Right half,
  in ink: plain dateline "June 23-'05  Fultonville N.Y.", six lines of Morse, the plain cursive closing
  "Yours without a shuddr," (sic, = shudder; the "r" is crowded against the edge), then two lines of
  Morse (the signature).

## Cipher type and key

**American Morse code** (the 1844 "railroad" Morse used on US landlines), written with pen dots and dashes.
No secret key. Writer's conventions:

| mark | meaning |
|---|---|
| dot / short dash | Morse dot / dash |
| long dash | American Morse L |
| comma-shaped stroke | end of letter |
| tall slash `/` | end of word |
| curl with a dot below | question mark (written in clear) |
| very large dots | emphasis (the word YES) |

What proves American (not International) Morse: the spaced letters, with a wide gap inside the letter,
occur and decode only in American Morse: R `. ..` (DEAR, RAYMOND, ANSWER, AGREE, CAROLYNN),
O `. .` (RAYMOND, CAROLYNN), Y `.. ..` (RAYMOND, MY, YES, CAROLYNN), C `.. .` (CAROLYNN), and L is a long dash
(SHALL, LET, CAROLYNN, WHAL). In International Morse none of these give words.

Register type label: MASC/Morse.

## Command (from repo root)

    python3 -I ciphers/hcp-1095/work/decode.py

It checks the SHA-256 of all four scans and decodes `work/transcription.txt` (my sign-by-sign
transcription of every Morse group on the card, with comments on individual signs). Output:

    [1] DEAR RAYMOND
    [2] MY ANSWER WHAT
    [3] SHALL IT BE? SHA-
    [4] LL I AGREE WIT-
    [5] H THEE? THEN LET
    [6] IT BE YES
    [7] CAROLYNN
    [8] WHAL
    PLAINTEXT: DEAR RAYMOND MY ANSWER WHAT SHALL IT BE? SHALL I AGREE WITH THEE? THEN LET IT BE YES CAROLYNN WHAL

## Plaintext (English, original) with the plain parts

    June 23-'05   Fultonville N.Y.
    [Morse] Dear Raymond, my answer - what shall it be? Shall I agree with thee? Then let it be YES.
    [plain] Yours without a shuddr [shudder],
    [Morse] Carolynn Whal[?].

Slovak translation:

    23. júna 1905, Fultonville, N.Y.
    Drahý Raymond, moja odpoveď - aká má byť? Mám s tebou súhlasiť? Tak nech je to ÁNO.
    Tvoja bez zaváhania (doslova: bez zachvenia),
    Carolynn Whal[?].

The message reads as a girl's playful acceptance of a proposal (or invitation) from Raymond, in a
rhymed form ("what shall it be? / shall I agree with thee?"); the closing "without a shudder" fits that.

## Uncertainties (all disclosed)

1. Surname. After W, four dots are spaced pair-gap-single-gap-single, not evenly like the H in
   WHAT/WITH/THEE; read as H, giving WHAL; Y (WYAL) or C+E with a missing comma are possible.
   The name ends with a long dash (L, drawn short and extended with a lighter stroke), then a slash
   overwritten by a heavy blot, then a full stop. WHAL may be a truncated or abbreviated surname
   (Whalen?); I report it literally. The first name is clearly CAROLYNN (double N as written).
2. The two L in the first SHALL (line 3) are drawn no longer than a T dash; L rests on word sense.
   The L in the second SHALL, LET, CAROLYNN and WHAL are clearly long.
3. I vs O depends on the gap between two dots; IT (twice) and I in "SHALL I" have gaps of ~100 px
   (at 2x) against ~150-195 px for the O's; the "I" of "SHALL I" (130 px) also rests on word sense.
4. Separator details: in RAYMOND (A|Y) and WITH (W|I) the separator is a slash overwritten by a
   heavy blot (read as a corrected letter separator, since the words run on); in ANSWER the A|N
   separator lies on an abraded spot and looks tall like a slash.
5. The question-mark curls (after BE and THEE) are read as written "?" with their dot below; they
   could be read as an extra E only by ignoring the curl, which gives no better text.
6. Nothing can be checked under the stamp (scan only).

## Why I believe it is correct

- Every Morse group on the card (8 lines, 77 letters plus 2 question marks) is transcribed and decoded by one standard
  alphabet with no free parameters; there is no unread sign apart from the doubtful H in the surname.
- The text is fluent English of the period, rhymed, addresses the card's addressee by name
  (Raymond, matching the clear address "Raymond Donaldson"), and is joined coherently by the
  plain closing "Yours without a shuddr,".
- The American Morse spaced letters (R, O, Y, C) and long-dash L appear exactly where the words need
  them, which fits a writer in New York State in 1905.

## Response to review 1

Review 1 verdict: ACCEPT (reviewer: separate Claude Opus 5.5 agent; independent transcription and
decoder `review/work/my_decode.py` agree letter for letter). No letter of the reading changes.
`python3 -I ciphers/hcp-1095/work/decode.py` re-run after this response: hashes OK, same eight lines.

1. Surname WHAL (minor) - agreed and now stated explicitly: besides the uneven H (pair/gap/single/gap/
   single), the final L of the signature is L only with its lighter tail (solid part about 57 px vs about
   42 px for the A dash before it); read as T it would give WHAT, which is not a name, so the final L
   rests partly on sense. The speck between that A dash and its comma is not a sign. WHAL is the single
   uncertain word on the card; everything else reads.
2. First SHALL (minor) - agreed; already disclosed as uncertainty 2 (L rests on word sense).
3. Question marks (minor) - agreed; already disclosed as uncertainty 5. The curl is a plainly written "?",
   and reading its dot as an extra E (BEE, THEEE) gives no text.
4. "shuddr" (minor) - accepted. On the scan (review/work/closing.png) "shudd" is followed by a short "r"
   squeezed against the right edge with a comma below; there is no room for a visible "e", so the word
   may be "shudder" written cramped rather than a misspelling. The report gives it as "shudd(e)r".
5. Register (minor) - accepted: type MASC/Morse, short role
   "transcription, decipherment by Claude Opus 5.5; independent AI review" (standard American Morse,
   no key reconstructed).

Stamp/hidden writing: both solver and reviewer inspected the stamp box, the picture and the edges; no
hidden writing is visible. What may lie under the (unremoved) stamp cannot be checked from the scans.
