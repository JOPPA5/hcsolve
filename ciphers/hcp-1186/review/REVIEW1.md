ACCEPT

# Review 1 of hcp-1186 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Solver command, from repo root: `python3 -I ciphers/hcp-1186/work/decode.py`. Output: "source hashes OK (4 files)",
   then the eight lines IT IS SUCH A LONG / TIME SINCE I SENT YOU / A CARD THAT I NEARLY / FORGOT HOW TO WRITE BUT /
   AS LONG AS I HAVE NOT / FORGOTEN HOW TO KISS & / HUG HOPE TO SEE YOU AT WEYMOUTH THIS AFTERNOON / NAN. This matches
   the plaintext claimed in SOLUTION.md word for word. The script asserts the key is one-to-one.

2. Independent transcription and decode: `python3 -I ciphers/hcp-1186/review/work/my_decode.py`. I read every sign
   myself from enlarged crops of the un-converted address-side scan (work/hires/..._adr.jpg, 3468x2298), crops in
   review/work/ (l1a..l6b at 1.6x, l6left, l7_9, z_time, z_you, z_card, z_write at 3x, z_addr, z_addr2, z_stamp).
   I used my own sign codes and derived the key from my own reading. The decode gives the same eight lines. Sign counts
   (my reading): 3 x12, Y x12, 6 x9, 8 x9, 4 x8, a x8, 9 x7, u x6, 5 x5, R (overbar) x5, 1 x4, 2 x3, w x3, e x3,
   j x2, o x2, and one each of n, d, E, K, Z, &. All 37 cipher groups decode; no sign is left over.

3. Row-by-row check against the pixels:
   - Line 1 `4Y.4a.a1wu.6.2385`: clear; matches.
   - Line 2 `Y4?9.a48w9.4.a98Y.i31`: the M sign (z_time) is a 1-like stroke with a hook at the top left and a foot
     curling right, plainly different from 1 (U) and 2 (L). The I in the third group is very faint but present.
     The Y sign of YOU (z_you) is an open iota/6-like stroke with a detached dot well above it; the same sign ends
     NEARLY on line 3. Matches.
   - Line 3 `6.w65̄n.Yu6Y.4.8966̄2i`: in CARD the R is a 5-like hook with a short overbar (z_card); in NEARLY the R
     is a 6 with an overbar. Matches.
   - Line 4 `o∂6̄53Y.u3e.Y3.e6̄4Y9.k1Y`: the second sign of FORGOT is a rounded d/∂-like blot, not a clear 3, as the
     solver says (uncertainty 4). The R of WRITE is faint but has its overbar (z_write). Matches.
   - Line 5 `6a.2385.6a.4.u6d9.83Y`: the V of HAVE is an a with a tall right stem (d-like), distinct from round a
     (S). Matches.
   - Line 6 `o31̄53Y98.u3e.Y3.E4aa.&`: I checked the left margin (l6left): nothing precedes the F sign. Eight signs,
     one T: FORGOTEN as written. K is a heavy hooked E-like sign. Matches.
   - Line 7 `u15,` then plain English "hope to see you, at / Weymouth this afternoon", signature `,868,`. Matches.

4. Key consistency: one-to-one, 19 letters plus &; the repeats LONG (x2), HOW TO (x2), AS (x2), FORGOT/FORGOTEN all
   use the same signs. The R signs always carry the overbar on a varying base (5, 6, 1), which is what keeps them apart
   from G = 5, A = 6 and U = 1; letter counts confirm the bar plus base is one sign.

5. Language and context: natural Edwardian English, a short affectionate note; Weymouth is about 8 miles from
   Dorchester; the halfpenny stamp and DORCHESTER / DORSET postmark of 12 OC 04 (afternoon time, "3.30 PM" as far as I
   can read it) fit "this afternoon". The cipher is a simple MASC mixing digits and letter-like signs, ordinary for
   period lovers' postcards.

6. Steganography: the stamp is still attached and shows no writing around it (z_stamp); the picture side (sailing
   ships at sunset) shows no writing at any edge or inside the picture at the available resolution. The solver says
   this honestly. Nothing suggests a hidden message here, so `MASC` remains the right register type label (not
   `MASC + Steganography`).

7. Sources: portal status Not solved, no attached transcription or solution; SOLUTION.md says none was found. I
   found nothing that contradicts this.

## Findings

1. (minor) Address side only partly read. SOLUTION.md uncertainty 7 leaves the second address line unread and the
   addressee as "Mr A. E. Hayward" with "Hay" faint. The address is not part of the message, so this does not affect
   completeness, but two small improvements are possible: "H. E. St" is very likely High East Street, Dorchester (a
   real street), which supports the place; and the "Mr" carries a raised letter that could be "Mrs" or "Mr." – state
   that it is uncertain. The second line (something like "County ... 7 Col. Su..") may stay unread, but say plainly
   that it is part of the address.

2. (minor) The postmark time is given only as "afternoon". As far as I can read, the postmark shows a time of about
   3.30 PM; please state the time you read (or say it is unclear) since the content says "this afternoon" and the
   reader will want to know whether the card could arrive in time (Dorchester local delivery the same day was normal
   in 1904).

3. (minor) The sign description for V ("a with raised right stem") is accurate but the sign actually looks like a
   cursive d; mention that, so a reader does not confuse it with D (which is the n-shaped sign).

4. (minor) The Slovak translation uses feminine forms (poslala, zabudla), which assumes the writer "Nan" is a woman.
   Plausible (Nan is a usual diminutive of Ann/Agnes), but say it is an assumption.

No blocker or major finding. Every cipher sign is read, the key is consistent over the whole text, and the plaintext
is coherent English that runs straight into the plain clause.

## What I could not verify

- Whether anything is written under the stamp (the stamp is attached; only a scan was available).
- The identity of A. E. Hayward and of "Nan"; the second address line.
- The postmark time beyond my reading of a blurred cancel.
