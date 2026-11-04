ACCEPT

# Review 1 – hcp-1050 (Fritz Lehmann card, Schweidnitz 17.3.1910)

Reviewer: Claude Opus 5.5, 2026-11-03. Round 1 (DONE1).

## What I verified and how

1. Ran the solver's command from the repo root: `python3 -I ciphers/hcp-1050/work/decode.py`. All four SHA-256 checks print OK;
   the output is identical to the plaintext claimed in SOLUTION.md (17 lines, run-on text "LIEBER FRITZ ENDLICH EIN ... GRUSZ KUSZ MINNA").
2. Independent decryption: review/work/my_decode.py holds my own transcription, typed from my own crops of the hi-res address scan
   (work/hires/..._adr.jpg), and its own decoder (A=2 ... I=10, no J, K=11 ... Z=26). Output:
   `LIEBER FRITZ ENDLICH EIN LEBENS ZEICHEN VOIN DIR UND FREUE MICH SEHR DAS ES SCHON BESSER GEHT VIELEICHT KÖNTEN WIER SONTAG
   WIEDER ZUSAMMEN SEIN WAS IST DENN SO PLÖTZLICH ÜBER DICH GEKOMMEN? GUTE BESSERUNG BALDIGEN WIEDERSEHN GRUSZ KUSZ MINNA`.
   The only difference from the solver is the umlaut on KÖNTEN (finding 1).
3. Key: the same table is the one in ciphers/hcp-1134/SOLUTION.md (sister Lehmann card, reviewed). Every one of the 200 numbers on
   this card (not "about 95") decodes with it; numbers used are 2–16, 18–23, 26; no number is left over and no number is out of range.
4. Transcription against the scan: I read all 17 lines in six full-resolution strips (review/work/strip0–5.png) and enlarged 3x the
   disputed places: review/work/so.png (SO), besse.png (BESSE=), gute.png (GUTE: third number is 20 in this hand's open-zero form,
   not 26), ueber.png (tick over 21 present), konten.png (tick over 15), l9marks.png (specks above line 9 are paper noise, not ticks).
   The bars over 13 in ZUSAMMEN and GEKOMMEN are clearly visible in strip3/strip5. VOIN = 22.15.10.14 is clearly written with 10.
5. Plaintext: natural colloquial German of 1910 with typical lay misspellings (wier, Sontag, vieleicht, Gruß/Kuß as SZ); a girlfriend
   (Minna) writes to Fritz Lehmann that she is glad he is better and proposes Sunday. Coherent with the address (Königszelt, near
   Schweidnitz) and the Schweidnitz return address. Translations (EN, SK) are faithful.
6. Picture side (review/work/pic_small.png) shows only printed text ("Kommt ein Vogel geflogen!", verse, 3309/6). Stamp is still affixed;
   nothing visible at its edges. I agree nothing more can be checked for steganography on these scans.
7. Return-address note (upside down, review/work/topnote*.png): I read the same skeleton "Abs. M. ?. b. Fr. Sch...ke / Schweidnitz
   Gr?benstr. / N. 3 II Hof". The second initial and the landlady's surname are not firmly legible to me either; the solver discloses this.

## Findings

1. (minor) KONTEN has an umlaut tick. In konten.png a clear double tick stands above the 15 of 11.15.14.20.6.14 (line 8), just like
   the ticks over 15 in PLÖTZLICH and 21 in ÜBER. SOLUTION.md uncertainty 1 says "KONTEN (no umlaut ticks)". Transcription should read
   `11.15".14.20.6.14` and the decoded text KÖNTEN (still = "könnten", single T kept as written).
2. (minor) SOLUTION.md says "about 95 numbers"; the card carries 200 numbers. Correct the count in the "Why I believe" section.
3. (minor) SO (line 12): the second number is overwritten (it looks like a 13 or 1+B retraced into 15). 15 = O rests on word sense;
   the solver disclosed this correctly. Keep the disclosure in the report.
4. (minor) Sender note: second initial, the surname after "b. Fr." and the vowel in "Gr?benstr." remain uncertain. These are names
   in an address line, and the remainder (Abs., Schweidnitz, ...str., N. 3, II, Hof) reads; I do not count this as an unread clause.
   The report should present it as uncertain, as SOLUTION.md already does.

## Register

Type label `MASC` is appropriate (number substitution). The card shows no steganography that can be checked (stamp affixed,
picture side printed only), so `MASC + Steganography` is not supported here.

## What I could not verify

- Underneath the affixed stamp (not visible on the scans).
- The exact surname and second initial in the sender note.
- Whether an earlier published solution exists beyond the solver's one web search; I found none in the repo or on the portal page record.
