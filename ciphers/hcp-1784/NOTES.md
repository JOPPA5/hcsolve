# Notes hcp-1784

2026-10-30: captured by Claude Opus 5.5 (orchestrator).

## 2026-10-30 Claude Opus 5.5 (solver): PARTIAL, no marker

No earlier work on this number; everything below is my own reading of work/hires/pc_hcp_465_adr.JPG (3x and 5x crops in work/crops/). No published solution found; no web search made beyond the orchestrator's capture and register check.

**Card.** Real-photo postcard, "Christchurch Regatta Aug 10 1910" written in clear on the picture side; photographer stamp "W. Hazel, Bournemouth"; halfpenny stamp, Bournemouth postmark (only "6" and part of the date legible to me; the portal's 1910-08-15 is not independently confirmed). Clear address: Miss Maud Starks, "The Cottage", Southern Road, West Southbourne (portal's "Mand" is a misreading of Maud). Clear signature: Jack. The big ring/padlock over the scan is the portal watermark, not part of the card.

**Text.** Six lines written sideways on the left half (turn the card 90 degrees anticlockwise). Every sign is a separate cursive capital followed by its own dot. A ruled line separates line 4 from line 5. Transcription in work/transcription.txt:

    M S? A A W Y? D / Y? D B D / D K A D H H Y? / C? L L H // H M F? L A K Y? / E L S  Jack.

Sign calls and their limits:
- S? (line 1, sign 2): hook plus stem with no upper loop, unlike the looped S in line 6; S or I.
- Y? (4x): left hook, stem, long lower loop; Y or J. Not the same shape as the J of "Jack", which has no hook.
- F? (line 5, sign 3): the weakest sign; stem with narrow top loop, triangular foot, crossbar. F by shape and by sense; T or a variant L is not excluded.
- C? (line 4, sign 1): 6-shaped, unlike the E of line 6; C or G.
- H (L3_5, L3_6, L4_4, L5_1): two stems with a rightward loop. K (L3_2, L5_6): stem with lower-right bowl. W (line 1, sign 5): could be U.
- Line 3, signs 1 and 4 are overlapped by the watermark and read as D.

**Cipher type: initialism (first letter of each word), not a substitution.** Evidence:
- A dot after every letter is what abbreviation looks like. Sister card hcp-1475 (1910, England, FINAL) is the same device.
- The close parses as a love-letter formula: L A K = Love And Kisses, then Y E L S = Your Ever Loving Sweetheart, directly before the signature "Jack.". With H M F? in front, "Have My Fondest Love And Kisses" fits, but only L A K / Y E L S are close to compelling.
- The sign set is what first letters of affectionate English give (D, L, Y, H, A, K lead), not letter text. No vowel E/I/O in body.
- work/check.py: no Caesar shift gives English, and 40 hill-climbs over all substitutions give 40 different strings of fragments ("YANNUSESEREE...", "OMAASTITICII..."). At 32 letters that test cannot prove absence of a substitution, but nothing readable appears. Run: python3 -I ciphers/hcp-1784/work/check.py

**Why it stops.** An initialism has no key. The closing can be expanded from a fixed formula; the 22-letter body (M S? A A W Y? D Y? D B D D K A D H H Y? C? L L H) cannot. I tried it: "My Sweet Angel" and "Would You", "You Dear", "How Happy You Can" all fit their letters, but each is one of many fits and no continuous sentence stands out. Sample only; do not cite any of these as the message. Choosing one would be forcing words onto the letters, so there is no DONE1, no SOLUTION.md and no register entry.

**What could finish it:** another card from Jack to Maud Starks with a shared formula, or a clear-text copy. None is in the repo (metadata search for "Starks" finds only this card).
