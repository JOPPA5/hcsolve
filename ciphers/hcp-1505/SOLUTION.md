# hcp-1505 (pc_hcp_186) — solution, round 1

Portal status at capture (2026-10-26): Not solved; no transcription or solution
attached. No published solution of this card was found or used.

Credit: the source capture, the identification of the key (reversed numeric
alphabet) and a first, partial transcription with 7 ambiguous digits were made
by an OpenAI GPT solver on 2026-10-26 (work/transcription.txt, work/decode.py).
Claude Opus 5.5 (2026-10-29) re-read every sign from enlarged crops of
source/address-large.jpg, resolved the ambiguities and wrote
work/transcription-v2.txt and work/decode2.py.

## Cipher type and key

Monoalphabetic substitution by numbers, reversed alphabet ("A1Z26" reversed):

    A=26 B=25 C=24 D=23 E=22 F=21 G=20 H=19 I=18 J=17 K=16 L=15 M=14
    N=13 O=12 P=11 Q=10 R=9  S=8  T=7  U=6  V=5  W=4  X=3  Y=2  Z=1

Words are separated by spaces; two-digit numbers are mostly (not always)
underlined on the card, which separates e.g. 12 (O) from 1.2. The key is fixed for the whole text.

## Command (run from the repository root)

    python3 -I ciphers/hcp-1505/work/decode2.py

It checks the SHA-256 of the files in source/, decodes all 102 numbers of
work/transcription-v2.txt, and prints the literal decryption and a normalised
line in which only the sender's R-slip (below) is corrected.

## Plaintext

Clear text on the card (not enciphered): "Scotland Sat. noon" / "Dear Ethel" /
signature "Fred." 24 March 1917 (portal date) was a Saturday, matching
"Sat.". Address side: Barnsley, Yorks, England (addressee's name not used).

Literal decryption (lower case = restored sign):

    I AM GOING / FOR MY SUIT TO NIGHT SO / WILL NOT HAVE TIME TO /
    WRITE BUT WILL SEND A / LETTEI TOMOIIOW HAVE / A GOOD DA lOVE TO BOTH /
    YOUR OWN

English (normalised): "I am going for my suit to-night, so will not have
time to write, but will send a letter tomorrow. Have a good DA[?]. Love to
both. Your own [Fred]."

Slovak: „Dnes večer idem po svoj oblek, takže nebudem mať čas písať, ale
zajtra pošlem list. Maj sa dobre / Prajem pekný DA[?]. Pozdravujem oboch
(s láskou obom). Tvoj Fred."

## Uncertainties

1. **R written as 18 (sender's slip).** In LETTER and TOMORROW (3 times) the
   number written for R is 18, which in this key is I (literal LETTEI,
   TOMOIIOW). 18 is R's forward alphabet position. Elsewhere R is correctly 9
   (FOR, WRITE, YOUR). The 18s are clearly underlined two-digit numbers; this
   is the writer's error, not a reading problem. Only the normalised line
   corrects it.
2. **"DA" after "HAVE A GOOD".** Read 23.26 (D A); both numbers underlined,
   followed by a full stop. The first number could alternatively be 22 (E,
   giving EA); 23 is preferred by comparison with 23 in GOOD. Neither gives an
   obvious English word. "day" with Y omitted is a possible intent but is
   **not** asserted; the group is left as read. A faint pale stroke after it
   is a stray pencil line, not a digit. Between "23 26." and the faded first
   sign of LOVE lies a gap of room for 2-3 numbers inside the same abraded,
   lighter patch of paper that took the 1 of 15; a lost sign there (e.g. 2 = Y,
   giving DAY) cannot be excluded, although the full stop directly after 26
   argues against it.
3. **First sign of LOVE (restoration).** The sign is faded: only a 5 and an
   underline survive. The underline marks a two-digit number, and 15 (L) is the
   only value that makes a word (5.12.5.22 = VOVE). Restored as 15, disclosed.
4. I and AM are written as separate groups (18 / 26.14).
   "TO NIGHT" is written with a dash (to-night).

Earlier GPT ambiguities resolved on the pixels: 13.12.7 NOT and 7.12 TO
(the writer's 7 has a hooked top and a descender; his 4 sits on the line and
has none, cf. WILL, WRITE, OWN); 22.? after GOOD is 23.26, not 22.4/22.24.

## Why it is correct

The fixed reversed-alphabet key turns 101 of 102 numbers into continuous,
idiomatic English with no per-word adjustments; the only anomalies are a
consistent, explainable sender slip (R→18) and one short group. The content
(a soldier or worker in Scotland writing on Saturday noon to "Ethel" in
Barnsley, going for his suit tonight, promising a letter tomorrow) fits the
plain header, date and address.

## Response to review 1

Verdict ACCEPT, three minor findings; all accepted, the reading is unchanged.

1. **Possible lost sign before LOVE.** Agreed. On review/work/patch.png the gap
   between "23 26." and the faded 5 of LOVE is wide and lies in the same
   abraded patch. Uncertainty 2 now names the gap and the possibility of a lost
   sign (e.g. Y, giving DAY), while DA stays the literal reading.
2. **"IAM as one group".** Agreed. On review/work/iam.png the space between 18
   and 26 equals the space between 14 and 20. work/transcription-v2.txt line 1
   is now `18 / 26.14 / 20.12.18.13.20`, the "IAM"->"I AM" replacement was
   removed from work/decode2.py, and uncertainty 4 is corrected. Re-run of
   `python3 -I ciphers/hcp-1505/work/decode2.py`: source hashes OK, 102 signs,
   1 restored, first line now "I AM GOING"; all other lines unchanged.
3. **Underlining not systematic.** Agreed (the 14 of TOMORROW is not
   underlined, patch.png). The key section and the transcription header now say
   "mostly underlined". No reading depended on it.
