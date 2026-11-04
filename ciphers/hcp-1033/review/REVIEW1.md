ACCEPT

# Review 1 – hcp-1033 (cpc_1906-08-23_DE_Munsterlager_DE_Ahlden_)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. Round 1, on DONE1.

## What I verified and how

1. Solver command. `python3 -I ciphers/hcp-1033/work/decode.py` (from the repo root): all four SHA-256 checks print OK.
   The key it prints and the plaintext lines match SOLUTION.md word for word, down to "ukss" and "grusse".
2. Independent decoder. In `review/work/my_decode.py` I wrote the key out as a literal string
   (1..25 = VWXYZ QRSTU LMNOP FGHIK ABCDE), not built from the solver's block rule, and wrote my own tokeniser.
   `python3 -I review/work/my_decode.py work/transcription.txt` gives the same text:
   MEINE LIEBE HERTHA FÜR DEINE LIEBE KARTE MEINEN BESTEN DANK BLEIBT DENN DEINE MUTTER AUCH SO LANGE DORT WIE DU
   ODER IST SIE WEGEN DEINES HEIMWEHS DORTHINGEKOMMEN GESTERN HABE ICH MICH MIT DEM OBERLEUTNANT VERTRAGEN UND
   AUSGESÖHNT NÄHERES DARÜBER WERDE ICH DIR NÄCHSTENS BRIEFLICH MITTEILEN WIE GEHT ES DIR DA DRÜBEN HERZLICHEN GRUSS
   UND INNIGEN UKSS DEIN OTTO / GRUSSE BITTE DEINE MUTTER VON MIR.
   It counts 330 numbers, 21 distinct values, and 3, 4, 6, 15 unused, as the solver says. Every number maps to a
   letter. There is no residue apart from the swapped KUSS, which is disclosed.
3. Transcription against the pixels. I rotated the hires address scan 90 degrees (`review/work/rot.jpg`,
   `body_full.jpg`), cut it into tiles `review/work/r00`…`r51.jpg` at 1.3x and made 3–4x zooms (`z_*.jpg`). Results:
   - Ordinary rows. I read every body row against the tiles: lines 1–17 and the signature. The numbers agree with
     work/transcription.txt, including the umlaut dots on 10 (FÜR, DARÜ, DRÜBEN), 14 (GESÖHNT) and 21 (NÄHERES,
     NÄCH). The stray "." before 17 on line 8 is really on the card, and the decoders ignore it.
   - The writer's sign shapes are consistent. 25 is "2" plus a hooked ſ or i-form (for example in ODER, `z_deines.jpg`
     row "14.24.25.7", and DEINES "24.25.19.13.25.8"). 21 is "2" plus a plain "1" (LANGE, `z_ist.jpg`).
     12 often looks like "1ł" (MITTEILEN, MUT).
   - Word-sense calls the solver disclosed:
     - BER (`z_ber.jpg`): the middle sign is written as a plain 21, not 25. The reading BER is word sense, as disclosed.
     - DRÜBEN (`z_druben.jpg`): the 4th number is in fact a fairly clear 22, so it is better than the solver says.
       The last number is two short strokes that look like 11, and N rests on sense, as disclosed.
     - MUT (12 vs 11) and TER (25 vs 21) in the postscript (`ps0.jpg`, `ps1.jpg`): both are ambiguous as the solver
       says, and their readings rest on sense.
     - UKSS (`r50.jpg`): "10.20.8.8" is clearly 10 then 20, so the writer swapped them.
   - IST: the middle sign of "19.8.9" is squashed, but S is the only letter that fits.
   - Postscript (upside down above "Postkarte") and signature "14.9.9.14" (`sig.jpg`): both are read correctly.
4. Steganography and hidden writing (relevant because of the human's note that Jolánka-series cards often carry a
   stego message under the stamp). The picture side (`source/picture-large.jpg`) has no writing. The stamp box
   (`review/work/stamp.jpg`): the stamp is intact and fully attached, with no writing around it. What lies under it
   cannot be checked from scans, and the solver says so. This card is a German 1906 Munsterlager card, not one from
   the Jolánka series. Nothing I can see justifies a "MASC + Steganography" label here.
5. Context. The date (23.8.06), the Munsterlager postmark (the army training ground) and the mention of the
   Oberleutnant fit a soldier writing to his sweetheart. The recipient's name on the address side (Hertha) is the
   opening crib, and the text is natural German of the period (Heimwehs, Gruss, brieflich mitteilen).
6. Key structure. The 25-letter alphabet without J is cut into blocks of five, and the blocks are numbered in reverse.
   The rule is simple and regular, and it fits all 21 letters that occur. The four unused values cannot be confirmed
   (finding 3).

## Findings

1. (minor) Five calls rest on word sense, not on the pixels: BER (written 21), DRÜBEN (final 13 looks like 11), MUT
   (12 looks like 11), TER (25 looks like 21) and the UKSS slip. All of them are disclosed in SOLUTION.md and marked
   {n} in the transcription. One detail is slightly off: in DRÜBEN the "22" is clear on the scan, so only the last
   number is uncertain. Each call is a single sign inside a word that otherwise reads, so the completeness rule is met.
2. (minor) Published-solution check. The portal's only reference is Schrödel, "Cryptographic postcards", HistoCrypt
   2021 (ecp.ep.liu.se article 166). SOURCES.md / SOLUTION.md do not say whether that paper was read. Its abstract
   is a survey and does not mention this card. I could not read the full PDF, so I cannot rule out that the paper
   prints this card's key. The solver should add one line saying what was checked.
3. (minor) The key values for X, Y, Q and P (3, 4, 6, 15) are taken from the block rule and are not seen on the
   card. SOLUTION.md already lists them as not used. The report should present those four as rule-derived.
4. (minor) GRUSSE vs GRÜSSE in the postscript is still open. Either way the sense is the same.

## Register / type

MASC (number substitution) is right for the register. I found no evidence of steganography on this card, so I see
no reason to use "MASC + Steganography". The card is complete (no unread clause), so a register entry is
appropriate once the minor points are addressed.

## Could not verify

- What lies under the stamp (the stamp has not been lifted on the scan).
- The full text of the HistoCrypt 2021 paper, and therefore whether this card is published there.
- The surname (Tesche vs portal "Tesohe") and "Gastwirth" in the plain address. These are not part of the cipher.
