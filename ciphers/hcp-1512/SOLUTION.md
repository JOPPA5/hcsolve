# HCP 1512 / pc_hcp_193 — substitution, corrected after review 1

## Origin and context

HC Portal cryptogram 1512, **pc_hcp_193**, is a postcard in the portal's
private collection. All three rendered tabs were inspected on 26 October
2026: its status was **Not solved**, category Substitution, date 23 May 1905,
language Unknown, sender Unknown and recipient E. Barnard. The description
was “HCPortal cryptographic postards collection.” Only the two image sides
were attached; no supplied transcription or solution was used.

The picture is Norwich in Tuck's “English Cathedrals” series. That is the
pictured place, not the dispatch town. The address reads Miss E. Barnard,
6 Chancellors rd, Hammersmith, London. The postmark reads **IPSWICH**, with
month/year MY … 05; its day appears 2? and the hour may be 11 PM. The exact
day and hour are uncertain because the stamp design overlaps the digits.
The portal date, 23 May 1905, was a Tuesday and agrees with “Tuesday night”
in the message, but the scan alone does not establish the exact date/time.
FRED is the signature, not an independently identified historical person.

## Method and key

This is a monoalphabetic substitution written in letter-like and numeral-like
shapes, preserving letter order. The separate header and repeated WILL WRITE
suggested the key. Distinguishing the eta-shaped N from fork-shaped S and
the open curled C-code from closed-bowl R-code completed the reading.
Independent review then corrected one word, POSTING, and identified one
retraced A variant.

The table uses manual identifiers for shapes, not claims that every shape
is an ordinary printed Latin character. N denotes the eta/n form, Y the
fork; c denotes the open curl, Q the closed loop with descender.

```text
glyph: P I c 2 R 3 S 4 T 5 6 V N W 8 Q Y 0 Z A B J E
plain: A B C D E F G H I J L M N O P R S T U V W Y Z
```

A further visual ID `%` records the Phi-shaped overwritten/retraced A in
EARLY and also decodes A. Thus there are **281 cipher positions, 24 observed
visual IDs and 23 base glyph types / distinct plaintext letters**. K, Q and
X are unobserved plaintext letters; no key entries are invented for them.
The apparent overwrite on the final E of INSIDE is recorded as a visible
alteration of its usual R-code rather than a new base letter.

## Full literal reading and translation

The separate header is:

```text
I HAVE BEEN INSIDE HERE
```

The twelve body lines, with source punctuation, are:

```text
MY OWN DARLING OF COURSE I
WILL WRITE TO YOU WHILEI AM
ON MY HOLIDAY. IF I CAN GET
AWAY FOR A TOUR I WILL WRITE
EVERY NIGHT JUST TO GIVE
YOU A SHORT ACCOUNT OF
THE DAY'S DOINGS. I AM POSTING
THIS ON TUESDAY NIGHT WECAUSE
I WANT TO HAVE A GOOD LONG
SNOOZE TOMORROW MORNING AND
I WANT TO START RIDING EARLY ON
THURSDAY, YOUR LOVING FRED
```

WHILEI is continuous in the diplomatic transcript and reads WHILE I.
WECAUSE is deliberately literal: its B-shaped cipher glyph means W in the
rest of the message. Intended BECAUSE is an interpretation, not a silently
corrected transcription. INSIDE is one word; its final E is overwritten.
The apostrophe in DAY'S and the displayed stops and comma are visible ink,
not editorial additions.

Slovak translation (interpreting WECAUSE as BECAUSE):

„Tu som bol vnútri. Moja najdrahšia, samozrejme ti budem písať počas
svojej dovolenky. Ak sa mi podarí vyraziť na výlet, budem písať každý večer,
aby som ti stručne opísal, čo som cez deň robil. Posielam to v utorok večer,
pretože sa chcem zajtra ráno poriadne dlho vyspať a vo štvrtok vyraziť na
jazdu skoro. Tvoj milujúci Fred.“

The vehicle or kind of riding is not established by the cipher; a bicycle
would be contextual speculation and is not asserted in this translation.

## Reproduce

From the repository root run:

```text
python3 ciphers/hcp-1512/work/decode.py
```

The command checks SHA-256 digests of both original scans and the immutable
metadata, then decodes `work/transcription.txt` using `work/key.json`. It
prints all thirteen lines, checks coverage and re-encrypts to the normalized
manual transcript. The explicit `%` variant is canonicalized to the normal
P-shaped A-code for that comparison. It does not recreate overwritten pen
strokes. The test establishes mapping consistency, not OCR or independent
pixel validation; that evidence comes from inspecting the scans and the
reviewer's separate transcription. Source images and metadata are unchanged.

## Evidence and limits

The corrected key covers all 281 manually transcribed positions. The
reviewer independently read the scan glyph by glyph and confirmed the rest
of the reading after identifying POSTING. Remaining visual qualifications
are the Phi-shaped A in EARLY, overwritten E in INSIDE, close C/R forms and
uncertain word spacing in WHILE I. These do not leave an undecoded letter
in the current reading; the original state of overwritten pen strokes is
not recoverable. WECAUSE remains the literal spelling. The postmark's exact
day/hour and Fred's identity are unproved.

Address, postmark, stamp, printed matter and watermark are outside the
281-position cipher count. No handwritten cipher was observed on the picture
side. English is established by the reading, not attributed to the portal's
Unknown language field. No attached or published solution was encountered.
The saved register snapshot had 110 entries and no exact source/name match;
this is no claim of priority or an exhaustive publication search.

## Response to review 1

Independent reviewer: Claude Opus 5.5, 26 October 2026, verdict REVISE. The
review explicitly permits closure after these corrections without another
round. All six findings have been addressed or acknowledged:

1. **POSTING, not WRITING (major).** Comparing the original scan with
   `review/work/z-posting.png` confirms `8WY0TNS`, not `BQT0TNS`. Added `8=P`,
   corrected the manual transcript, literal plaintext and Slovak translation
   to “Posielam”. P is no longer called unobserved. Counts are recomputed:
   281 positions, 24 visual IDs including the A variant, 23 base types.
2. **Phi-shaped A in EARLY.** Added explicit `%` in the manual transcript
   and key; `R%Q6J` reads EARLY. This is treated as an overwritten/retraced
   A variant, not an independent base substitution symbol. The decoder now
   checks injectivity of the 23 base glyphs and canonicalizes this one
   disclosed variant when re-encrypting.
3. **Punctuation.** Preserved the raised apostrophe in DAY'S, stops after
   HOLIDAY and DOINGS, and comma after THURSDAY in transcript and output.
   Removed the incorrect claim that there was no apostrophe. These marks
   are excluded from the letter-position count.
4. **INSIDE and header overwrite.** Removed the unsupported internal word
   division IN SIDE. Disclosed the vertical overwrite on the final E-code
   of INSIDE. WHILEI is left continuous in the diplomatic transcript with
   WHILE I explained as a reading-space interpretation.
5. **Context.** Added the scan-derived IPSWICH postmark reading to SOURCES
   and this account, keeping both day and hour uncertain. Norwich names the
   cathedral picture, not the postmark. The Tuesday/date agreement supports
   the reading but is not independent proof of the obscured stamp digits.
6. **Watcher protocol.** No watcher was started because the user's prior
   instruction explicitly overrides that repository default. The review and
   immutable source files have not been edited. Final PDF and marker work
   remain the coordinating solver's separate closing step.


## Finalization - 2026-10-26

The coordinating solver verified the item-by-item review response, reran the
corrected decoder with original-source hash checks, and produced the report
PDF. All rendered pages were visually inspected after final typography
corrections. The review explicitly permits closure after the specified local
corrections without another round. Remaining reading uncertainties are
preserved; no new independent ACCEPT verdict is claimed.

The local register-entry.txt is prepared with solver TODO because no solver
name was supplied for the entry. Nothing was submitted externally. Original
source files and review files were left unchanged. FINAL records closure
after these review conditions and report checks.
