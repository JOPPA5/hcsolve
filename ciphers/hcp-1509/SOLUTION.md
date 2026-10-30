# HCP 1509 / pc_hcp_190 — German love postcard, Lieblos, 5 April 1912 (round 1)

Portal status at capture (2026-10-26): **Not solved**; category Substitution,
language Unknown; no transcription or solution attached. No published
decipherment of this card was found or used.

**Credits.** The capture of the portal tabs and both scans (source/, SOURCES.md)
and a one-line triage ("dense numeral/fraction-like substitution, context
German") were made by an OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) on
2026-10-26; it produced no transcription or key. The transcription, the key and
the decipherment below are the work of Claude Opus 5.5 on 2026-10-30.

## Card and context

Address side: written in Kurrent, to (tentative reading) *Fräulein Elisabeth
Herb[?] in Wächtersbach, im Schloß, Kreis Gelnhausen*; German Reich 5-Pf.
Germania stamp; Bahnpost postmark "…SEN–GELNHAUSEN BAHNP[OST] ZUG 512"
(the Gießen–Gelnhausen railway). The message is written across the left half,
rotated 90°, headed in plain script **"Lieblos, 5.4.12."** (Lieblos, today part
of Gründau, Main-Kinzig-Kreis, Hesse, on that line). 5 April 1912 was Good
Friday; Easter Monday ("2. Feiertag") was 8 April 1912. Picture side: printed
German drinking/love verse "Es lebe der Wein und die Liebe…" — not cipher.
The address reading is not needed for the decipherment and is not claimed as
certain.

## Cipher type and key

Homemade **monoalphabetic substitution with digit-like signs** (a private
"number alphabet"), German, word divider `x`. Two plain numerals ("2." and
"100,000") and the farewell "Auf Wiedersehn" (Kurrent) are written in clear.

| sign on card | token | letter | sign on card | token | letter |
|---|---|---|---|---|---|
| fraction 16 over 1 | `16/1` | A | `11` underlined | `11_` | O |
| 6 | `6` | B | `11` underlined with two dots | `11_"` | Ö |
| small c/v hook | `c` | C | 7 (1 with hooked top) | `7` | R |
| h-shape | `h` | D | 4 | `4` | S/ß |
| 8 | `8` | E | plain 1 | `1` | T |
| S / long-s curve | `S` | F | colon | `:` | U |
| 9 with descender | `9` | G | colon with two dots above | `:"` | Ü |
| = with dot below | `=` | H | `11` double underlined | `11=` | V |
| single dot | `*` | I | 111 | `111` | W |
| 3 | `3` | K | h with hook on top | `hz` | Z |
| 1 with bar on top | `T` | L | `x` | `x` | word divider |
| Kurrent-M-like N | `N` | M | 11 | `11` | N |

Not used on this card: J, P, Q, X, Y. The key is fixed for the whole text (359
cipher signs); every value is attested several times except K (3: kommen,
kommst, Küsse — 3 times), Z (zu, ganz, Zuge), V (verliebt, viele), Ö/Ü (once each).

Files: work/transcription.txt (full token transcription, line by line),
work/key.json, work/decode.py.

## Command (run from the repository root)

    python3 -I ciphers/hcp-1509/work/decode.py

It verifies the SHA-256 of the three files in source/, decodes every token of
work/transcription.txt with work/key.json, prints the plaintext line by line
(plain-script lines marked `[plain]`) and reports unknown tokens (none).

## Plaintext

Literal output of the command (card lines; spellings exactly as written):

    [plain] Lieblos, 5.4.12.
    MEINE HEIS GELIETE ELISABETH
    HABE DEINEN LIEBEN HEUTE MORGEN
    ERHALTEN ABER MEINE FREUDE WAR GRÖSER
    ALS ICH MIR DACHTE DENNEWIE GERNE
    WARE ICH WIEDER EINMAL BEI DIR
    DENN ICH BIN ZU VERLIEBTEIN DICH
    ABER ICH HOFFE DOCH GANZ BESTIMMT
    DASS DU DENN 2. FEIERTAG KOMMEN
    WIRST SCHREIBE MIR MITEWELCHEM
    ZUGEDU KOMMST
    [plain] Auf Wiedersehn
    VIELE GRÜSE UND 100,000 KUSSE SENDET AN
    DICH MEINE HEIS GELIEBTE ELISABETH
    DEIN DIR AUF EWIG TREU BLEIBENDER
    BALD ANTWORTE
    HEINRICH

German (normalised spelling and punctuation; normalisations listed under
Uncertainties):

> Lieblos, 5.4.12. Meine heiß gelie[b]te Elisabeth! Habe deinen lieben [Brief / deine liebe Karte]
> heute Morgen erhalten, aber meine Freude war größer, als
> ich mir dachte, denn wie gerne wäre ich wieder einmal bei dir, denn ich bin zu
> verliebt in dich. Aber ich hoffe doch ganz bestimmt, dass du den 2. Feiertag
> kommen wirst. Schreibe mir, mit welchem Zuge du kommst. Auf Wiedersehn.
> Viele Grüße und 100.000 Küsse sendet an dich, meine heiß geliebte Elisabeth,
> dein dir auf ewig treu bleibender Heinrich. Bald antworte[n]!

English:

> Lieblos, 5 April 1912. My dearly beloved Elisabeth! I received your dear
> [letter] this morning, but my joy was greater than I had imagined, for how
> gladly I would be with you again, for I am too much in love with you. But I do
> hope very much that you will come on the second holiday [Easter Monday].
> Write and tell me which train you are coming on. Goodbye till we meet again.
> Many greetings and 100,000 kisses to you, my dearly beloved Elisabeth, from
> your Heinrich, who remains faithful to you forever. Answer soon!

Slovak:

> Lieblos, 5. 4. 1912. Moja vrúcne milovaná Alžbeta! Dnes ráno som dostal tvoj
> milý [list], ale moja radosť bola väčšia, než som si myslel, lebo ako rád by
> som bol zase raz pri tebe – som do teba príliš zaľúbený. Ale celkom určite
> dúfam, že prídeš na druhý sviatok [Veľkonočný pondelok]. Napíš mi, ktorým
> vlakom prídeš. Do videnia. Veľa pozdravov a 100 000 bozkov ti posiela, moja
> vrúcne milovaná Alžbeta, tvoj navždy verný Heinrich. Odpíš čoskoro!

## Uncertainties (all disclosed; none affects the meaning)

1. **GELIETE (line 1).** In the first "geliebte" the sign after the second E is
   a single tall 1 with a hooked top; no B sign (6) is present. Read literally
   as T (GELIETE); the same word in the closing line "DICH MEINE HEIS GELIEBTE ELISABETH" is complete (GELIEBTE). Either the
   writer omitted B or the hooked 1 is an unrecorded b+t ligature; not restored
   in the literal output.
2. **Extra E in DENNE·WIE, VERLIEBTE·IN, MITE·WELCHEM.** In these three places a
   clear 8 (E) stands between two words where no `x` divider is written. Read
   literally; the normalised German drops it. Possibly the writer used 8 as a
   divider here, or added a dialectal/erroneous e. In ZUGE·DU the E belongs to
   "Zuge" and only the divider is missing.
3. **R in "MIR" (line 4).** The R sign has its hooked top closed into a small
   loop, so it resembles a small 9; it lacks the long descender of the G sign
   (9) and is read as 7 = R. "mig" would make no sense; in every other place
   (dir ×2, mir in line 9) R is the open 7.
4. **1 vs 7.** The plain 1 (T) and the hooked 7 (R) are close at the scan's
   resolution (1024 px); each occurrence was checked at 6–8× and agrees with the
   word in every case (e.g. ABER, ERHALTEN, TREU, ANTWORTE).
5. **Stray mark in ALS (line 4):** two small ticks (,,) under the L sign;
   ignored (not a separate sign in the key; possibly an umlaut put on the
   wrong line or a pen slip).
6. **Writer's spellings kept literal:** HEIS (heiß), GRÖSER, GRÜSE (single s for
   ß), WARE (wäre, no umlaut), KUSSE (Küsse; an umlaut over this U is not
   visible, but the space above it is occupied by the Kurrent "Wiedersehn",
   so its absence cannot be established), DENN for
   "den" (2. Feiertag), "deinen lieben" without a noun, BALD ANTWORTE.
7. **Plain parts:** "Lieblos, 5.4.12." and "Auf Wiedersehn" are in clear Kurrent;
   the first word of the farewell is read "Auf" (Kurrent A), not "Mit". The
   address reading (surname, place) is tentative and not part of the claim.
8. **Final T of BESTIMMT (line 7):** the last plain 1 (T) is written onto
   the second N (M) right at the trimmed edge of the card; read as T, which
   the word requires.
9. Placement: the cipher signature HEINRICH is written below and right of the
   last line ("Bald antworte"); reading order as given.

## Why it is correct

- One fixed key of 23 signs converts all 359 cipher signs on the card into
  continuous, grammatical German with no unknown tokens; the key was derived
  from the first words (MEINE … ELISABETH) and then held unchanged.
- Strong internal checks: the opening "Meine heiß geliebte Elisabeth" recurs
  in the closing formula, deciphering identically; ö/ü appear only as the O and
  U signs with diacritics; V is a variant of O (double vs single underline).
- Context fits exactly: the card is dated Lieblos 5.4.12 (Good Friday); the
  writer asks Elisabeth to come "den 2. Feiertag" (Easter Monday) and to tell
  him which train — and the card itself went by the Gießen–Gelnhausen Bahnpost
  serving Lieblos; the recipient's address is in the Gelnhausen district.
- A typical 1910s love postcard formula ("Viele Grüße und 100.000 Küsse sendet
  … dein dir auf ewig treu bleibender …").

## Response to review 1

Review 1 (Claude Opus 5.5, 2026-10-30) gave the verdict **ACCEPT** with four
minor findings. All four are addressed; no decoded letter changed.

1. **KUSSE umlaut (minor) – agreed, fixed.** On review/work/z_kusse2.png the
   Kurrent "Wiedersehn" runs directly above the `3 :` signs, so two dots over
   the colon could not be told apart from those strokes. Uncertainty 6 now says
   the umlaut is "not visible; its absence cannot be established". Meaning
   unaffected (Küsse).
2. **Final T of BESTIMMT (minor) – agreed, added.** On review/work/z_bestimmt.png
   the last `1` is written onto the second N at the trimmed card edge. Added as
   uncertainty 8; the reading T stands (the word requires it).
3. **"zu verliebt" (minor) – agreed, fixed.** The English now reads literally
   "for I am too much in love with you", matching the Slovak "príliš zaľúbený".
4. **Presentation of GELIETE / "deinen lieben" (minor) – agreed, fixed.** The
   normalised German now shows "gelie[b]te" and "deinen lieben [Brief / deine
   liebe Karte]", with the restorations bracketed; the PDF report does the same.

Re-run after the edits (the transcription, key and decoder are unchanged):
`python3 -I ciphers/hcp-1509/work/decode.py` → three hashes OK, the same 17
output lines as in "Plaintext" above, "cipher signs decoded: 359; unknown
tokens: none".
