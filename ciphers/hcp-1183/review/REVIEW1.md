ACCEPT

# Review 1 – hcp-1183 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Ran the solver's command from the repo root: `python3 -I ciphers/hcp-1183/work/decode.py`. All three SHA-256 checks print OK and the output is exactly the plaintext claimed in SOLUTION.md (9 lines, RECEIVED YOUR POSTAL CARD … GAY AND FESTIVE. / CIDER).
2. Wrote my own decoder `review/work/indep_decode.py` with a key typed from my own reading of the hi-res scan (not loaded from work/key.json) and ran it on the solver's transcription: identical plaintext. It also counts 163 cipher signs, 21 distinct sign types, a one-to-one sign/letter mapping, no unknown token.
3. Checked the transcription against the hi-res message scan (`work/hires/*_pic.jpg`, 3468x2298) with my own crops in `review/work/`: every line in two halves (`L1_0.png` … `L6_1.png`), the bottom line (`L8.png`, `gayand.png`), the watermark corner (`br.png`, `initials2.png`, `cider.png`, `cider2.png`), the end of line 6 (`goodnight.png`, `gn2.png`), and an autocontrast montage of the one-bar/two-bar signs (`LN_montage.png`). Lines 1–6 match the transcription sign by sign. Specific checks:
   - L/N: WENT, SENT and AND (line 5) clearly show two bars on the enhanced montage; LAST shows one bar. The solver's L/N split holds.
   - D vs E: the X-with-horizontal-bar ends of RECEIVED, CARD (×2), HEARD, HURRIED, GOODNIGHT's D and the X-with-vertical E's are drawn as transcribed.
   - F (plain circle with tick) in OF and FESTIVE, distinct from G (circle with dot) and H (circle with bar).
   - GOODNIGHT under the watermark: ⊙ ┐ ┐ X-bar ≠ ϕ ⊙ θ □ visible; the dot under ϕ is the watermark's separator dot, not pencil.
   - Initials: ┐ . / arch with feet and a dot inside . / + . are visible through the watermark (the W's dot is close to watermark letters "it)" but the arch with feet is pencil).
   - GAY AND FESTIVE.: legible; the faint extra stroke beside N in AND is disclosed (uncertainty 2).
   - CIDER: C, I and D are visible; E's vertical bar and the R's shape are partly masked by watermark letters, as the solver discloses (uncertainty 3).
4. Plaintext: natural 19th-century American English, a reply about a postal card that the writer collected and sent on "over to the mountains by Aunt Lucy". It fits a US one-cent postal card (1873-type indicium) posted at Santa Clara to San José. No forced words.
5. Steganography check (the human's note about hidden messages under stamps on the Jolánka series): this card is a pre-printed US postal card with an imprinted indicium, so there is no adhesive stamp to hide anything under. On the hi-res address side I saw only the printed text, postmark, killer, the address, the pencil "51" and some faint pencil traces at lower left (no letters or signs). The message side has nothing outside the cipher text. I agree no steganography is present; the type is MASC, not "MASC + Steganography".
6. Sources: SOURCES.md records the portal capture (status Not solved, no attached solution) and a web search with no published solution. I found nothing that contradicts this.

## Findings

1. (minor) SOLUTION.md says "Twenty letters occur; J, K, Q, X, Z do not." The key has 21 letters (A B C D E F G H I L M N O P R S T U V W Y) and my count finds 21 distinct signs used. The list of absent letters is right; the number "Twenty" should be 21 (and the report should repeat the corrected number).
2. (minor) CIDER: E and R partly rest on word sense under the watermark. Disclosed; I could not see the E's vertical bar more clearly than the solver did. The reading should stay marked as uncertain in the report.
3. (minor) The meaning of the closing "Gay and festive." / "Cider" is unclear, but every letter decodes to real English words, so this is not an unread clause; the solver's disclosure is adequate.
4. (minor) Address side: besides "51" there are faint pencil traces at the lower left of the address panel (not letters). Could be mentioned in the steganography note for completeness.

## What I could not verify

- The year of posting (the postmark has no year); the 1873–1881 date range rests on the indicium type, which I did not check against a philatelic catalogue.
- The addressee's surname (Brimblecom vs portal "Brimblecone"); not part of the cipher.
- The identity behind "O. W. L.".
