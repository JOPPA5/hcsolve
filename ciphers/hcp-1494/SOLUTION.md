# HC Portal 1494 (pc_hcp_175) — solution, round 1

Postcard, Houston Avenue, Crookston, Minn.; postmarked Crookston and Fertile,
Minn., 18 Feb 1915; to Miss Elvira Jungleseth [surname reading uncertain],
Fertile, Minn. Portal status: Not solved (checked 2026-10-26); no transcription
or solution attached; no published solution of this card found.

Credit: symbol inventory, key and first transcription by the earlier OpenAI GPT
solver (GPT-6 Astra / GPT-6.1 Sol, 2026-10-26, left as partial; files
work/transcription.txt, work/decode.py). Claude Opus 5.5 (2026-10-29) re-read
every sign on enlarged crops, corrected three readings (TIME, ALLTOGETHER,
final word), wrote work/transcription-v2.txt and work/decode_v2.py.

## Cipher type and key
Simple monoalphabetic substitution (one sign per letter, no nulls, no
homophones), with digits and keyboard-like signs as cipher symbols. Part of the
message is in plain English handwriting: "since", "I am still at my old Place",
"and", "?", "715 Hunter St." and a plain-cursive closing word above the
signature. Word division is kept by the writer. No sister card in the repo.

| letter | sign | letter | sign | letter | sign |
|---|---|---|---|---|---|
| A | 1 | H | 8 | R | T-like stroke (id `R`) |
| C | c / C | I | 7 | S | # |
| D | 2 | K | 4 | T | % (`pct`) |
| E | ε (`eps`) | L | 5 | U | u |
| F | = (`eq`) | M | 9 (`q`) | V | V/U-shape |
| G | + (`plus`) | N | 6 | W | cursive-D shape (`W`) |
| O | 0 | Y | − (`minus`) | | |

Unseen letters (B, J, P, Q, X, Z) are unknown. Key file: work/key.json.

## Single command (from the repository root)
```
python3 -I ciphers/hcp-1494/work/decode_v2.py
```
It checks SHA-256 of source/address-large.jpg, source/picture-large.jpg and
source/metadata.md, then prints the literal sign-by-sign decode and the
normalised plaintext (115 cipher signs). The transcription is my own; no
transcription was attached on the portal.

## Plaintext (literal decode)
```
DEAR D
IT IS A LONG TIMH AGO
since I HEARD FROM
YOU HAVE YOU FORGGOTT
EN ME ALLTOG[A|I]GTHER ?
I am still at my old Place
and WORKING EVERY DAY
LET ME HEAR FROM YOU
IF YOU WANT T[O|M]  <two 9-like marks below the last word>
715 Hunter St.
<plain closing word, probably "Yours">
CLARENCE
```

## Plaintext (normalised)
Dear D: It is a long time ago since I heard from you. Have you forgotten me
altogether? I am still at my old place and working every day. Let me hear
from you if you want to. 715 Hunter St. [Yours?] Clarence

English is the original language (the card is in English).

Slovak: Milá D., je to už dávno, čo som od teba počul. Zabudla si na mňa
úplne? Stále som na svojom starom mieste a pracujem každý deň. Ozvi sa mi,
ak chceš. Hunter St. 715. [Tvoj?] Clarence

## Uncertainties (all disclosed)
1. Greeting "DEAR D": the second sign is clearly a 2 (= D), but written
   without the initial loop the writer gives his other 2s. It is reported
   literally as the initial D; the addressee's name on the card is Elvira, so
   D may be a nickname/initial. Not resolved.
2. TIME: the fourth sign is a closed 8 (= H), not the open ε; read as a writer
   slip for E (ε and 8 look alike in this hand). Literal TIMH.
3. FORGGOTTEN: two distinct + signs (G) are written; literal FORGGOTTEN,
   normalised forgotten. Writer error.
4. ALLTOGETHER: the signs are 1 5 5 % 0 + [dark flagged stroke] + % 8 ε T.
   The dark, heavy stroke (apparently re-inked) resembles 1 (A) or 7 (I), not
   ε; together with the second + it stands where E is expected. Normalised as
   ALLTOGETHER (writer's spelling for "altogether"); the exact intent of these
   two signs is a writer slip/correction and is not read as anything else.
5. Final word: % 0 = TO. The 0 has a faint curved tail, so it could be taken
   as 9 (M) (the earlier partial read WANTTM); the body is the writer's 0 and
   "if you want to" fits. Below the word there are two 9-like marks (one
   under the %, one forming the faint tail) that I do not decode; they may be
   a later addition or a correction. Reported, not read.
6. The plain closing word above the signature is cursive and only partly
   legible (probably "Yours"); it is not cipher.
7. CLARENCE is the decoded signature; no historical identification made. The
   recipient's surname is read from the plain address and is uncertain.

## Why I believe it is correct
- One fixed 20-letter key decodes all 115 cipher signs into English words
  with the writer's own word division; only four signs are slips/extras, all
  in words whose identity is certain from context.
- The same sign gives the same letter throughout (e.g. 8 = H in HEARD, HAVE,
  HEAR, TOGETHER; = stands for F in FROM ×2 and IF; − stands for Y in YOU ×4,
  EVERY, DAY).
- The cipher text interlocks with the plain-hand words ("since I heard from
  you", "I am still at my old place and working every day"), which were not
  used to derive the key beyond confirming it.
- Content (a man asking a woman why she has not written) fits a 1915 private
  postcard between two small Minnesota towns.

## Response to review 1
Verdict ACCEPT; all five findings were minor. The decoded reading is unchanged.

1. Key size. Fixed: the key has 20 letters (A C D E F G H I K L M N O R S T U V W Y),
   not 21. "Why I believe it is correct" now says "20-letter key".
2. Garbled sentence. Fixed: it now reads "= stands for F in FROM ×2 and IF; − stands
   for Y in YOU ×4, EVERY, DAY".
3. Question mark. Agreed. On the enlarged crop (review/work/qm.png) the mark is a hook
   with a flat foot and no dot, much like the writer's 2. It stands at the end of a
   question and outside the cipher word, so it is read as a plain "?", not as cipher D.
   A comment saying so was added to the header of work/transcription-v2.txt. Header
   lines are skipped by the decoder, so the output does not change.
4. Recipient's surname. Agreed. On the address side the first letter can equally be
   read as F or I, so "Fugleseth" (a Norwegian surname, which fits Fertile, Minn.) or
   "Ingleseth" are alternatives to the portal's "Jungleseth". The portal's form is
   kept for reference, and the report gives the alternatives. Uncertainty 7 stands.
5. "DEAR D" against the addressee Elvira. This stays open (uncertainty 1). The report
   lists it as unresolved.

Re-run after the edits: `python3 -I ciphers/hcp-1494/work/decode_v2.py` prints the
same literal and normalised text as before: 115 cipher signs, 2 with alternative
readings, 4 slips or extra signs, and source hashes OK.
