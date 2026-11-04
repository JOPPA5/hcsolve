# Notes hcp-1035

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 Claude Opus 5.5 (solver) - PARTIAL, no marker

Card: picture side of a 1902 view card (Cismar -> Hamburg, recipient "Gustav"). The whole message is on the
picture side in brown ink: 11 lines across the bottom, two vertical lines up the right margin (ending in a
signature, read as 12.1.17.19.8.1 = MARTHA), and one vertical line on the left margin starting in plain
script "Quentin Durward" followed by digits (8.1.2.5 9.3.8 1.20.18.7.5.11.5.18.5.13 ... = HABE ICH AUSGELESEN ...).
No sister family in this repo uses it; key established from the text itself.

Cipher: numeric monoalphabetic substitution, A=1 ... Z=25 with I/J merged (9), dots between letters,
hyphens between words. A few things are written in clear (A.S., Kh.S., Kh., a plain Q in QUAELGEIST,
a capital B in the right margin). An overline over a number doubles it (MUSSTE written 12.20.18-overlined.19.5).
Hand: 7 is written like a crossed 4; 25 (Z) is a loop-2 + 5; 13 has a Z-shaped 3.

Pixel reading of the main block: work/transcription_partial.txt; decoder (checks hashes):
  python3 -I ciphers/hcp-1035/work/decode.py
Reads (lines 1-10 of 11): MEIN LIEBER GUSTAV! HEUTE MORGEN EMPFING ICH VON DIR A.S. UND Kh.S. EINE KARTE.
DU BIST SCHRECKLICH UNARTIG. WIE KANNST DU VON MIR EINEN BRIEF VERLANGEN, WAS SOLL ICH DIR ERZAEHLEN?
WENN ICH IN HAMBURG BIN, IHR SEH(T) EUCH Kh. WOHL ... BEI NACHT AN(?). MORGEN GEHE ICH ZU BALL, WAS WUERDE
ICH AUSGEBEN, WENN ICH DICH ALTER QUAELGEIST BEI MIR HAETTE. DER BALL IST IM OBIGEN HOTEL UND GEHT VON
DAHME AUS. HEUTE BIN ICH AUF JASEN(?) HUSFRAU, SIE SIND ALLE IN KIEL UND JETZT MUSS ICH PFANKUCHEN BACKEN,
ABER ERST MUSSTE ICH DICH JA BEFRIEDIGEN. DU ... EINMAL ... HERZLICHE ...

Why it stops (whole clauses unread, so partial per run rules):
- line 5 end: group 22.14.8.11.?.?.5.11 - two signs under the Cismar postmark; "Kh. WOHL ..EL" not understood.
- line 5: SEHI / AN (1.13) read from pixels but the clause "IHR SEHI EUCH ... BEI NACHT AN" is not secure.
- line 11 (bottom edge): 2.9.13.19 (BINT?) / 12.5.9.3 (MEIC?) / 21.5.17.25.20.?.3.8 (VERZ?UCH) - written
  without separating dots; segmentation ambiguous; closing groups after HERZLICHE run into the worn edge.
- right margin (two lines, GRUESSE UND ... VIEL VERGNUEGEN ... VON GANZEM ... DEINE MARTHA) and left margin
  (Quentin Durward HABE ICH AUSGELESEN ...) only partly read; several groups under the stamp/postmark and
  the margin edge not transcribed.
- word-sense calls: DIR in line 4 (middle sign faded), F in PFANKUCHEN (ink blot), first sign of WIE (blot),
  HE of HEUTE in line 8 (retraced).
Steganography note: the stamp side was not examined beyond the overview (address-side scan); nothing hidden
was established. If continued: transcribe both margins sign by sign from work/hires (rotate 90 deg), then
resolve the last line with 5x crops.
