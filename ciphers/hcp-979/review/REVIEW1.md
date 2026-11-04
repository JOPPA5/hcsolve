ACCEPT

# Review 1 – hcp-979 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Solver command. `python3 -I ciphers/hcp-979/work/decode.py` (from repo root): all four SHA-256 checks print OK and the output
   is exactly the claimed plaintext "LIEBER FRITZ ! HEUT GEHT ES WIEDER BESSER WEISZ ABER NOCH NICHT WIE ES HEUT ABEND SEIN WIRD
   GESTERN HATTE ICH STARKE FIEBER SOLLTE ICH NICHT 1/2 VIII".
2. Independent decoder. `review/work/indep_decode.py` (own regex parser, table A=2 … Z=26 without J) on work/transcription.txt
   gives the same ten lines word for word. The body holds 114 numbers (counted with grep, matching the solver's figure); every
   value is in {2..12, 14, 15, 18, 19, 20, 21, 23, 26}; no number falls outside the table and nothing is left over.
3. Key provenance. The same table is in hcp-1134/SOLUTION.md; hcp-1134, 1113, 1045, 1050 (same recipient Fritz Lehmann) all
   carry REVIEWED1 with verdict ACCEPT. Transfer of the key is disclosed.
4. Transcription against pixels. I cropped the block from work/hires/..._adr.jpg (x 250–1600, y 600–2100), rotated it 90°
   clockwise (review/work/block_rot.png) and read all ten rows myself, then enlarged the ending (review/work/end.png), the end of
   row 5 (l5end.png) and rows 9–10 (l9.png). My reading agrees number for number with work/transcription.txt, including the
   capital strokes (crossed 12, 7, 9, 2, 7, 19), the missing dash between 2.3.6.18 and 14.15.4.9 in row 4, and the "+"-shaped
   separator after FIEBER. The fraction "I over II" followed by "VIII" with an overbar is plainly visible and is not enciphered.
5. Language and context. Fluent colloquial German of the period (Heut, weiß written WEISZ, "starke Fieber" for "starkes
   Fieber"); the content (illness, uncertain evening appointment, "½ 8") is coherent. Postmark FREIBURG (SCHLESIEN) 10.9.09 is
   legible on the address scan; same town as hcp-1134. Picture side (Gretchen, "Wie sollte mir die Kette stehen?", 4034-2)
   shows no handwriting; stamp still affixed, nothing protrudes.
6. Disclosure. Portal status Not solved, no attached solution; solver states no web search was made and the reading is
   his own with a transferred key. Uncertainties (elliptical ending, 5/8 and 18/19 calls, plain address) are listed.

## Findings

1. (minor) End of row 5: the last number of the second HEUT (9x.6.21.20) runs into the printed blue "Briefkaart" line; the
   "2" is visible but the "0" is largely covered by the print (review/work/l5end.png). The reading 20 = T is forced by HEUT
   and by the identical word in row 2, but this word-sense restoration is not listed among the uncertainties. Add it.
2. (minor) The final clause "SOLLTE ICH NICHT ½ VIII" is fully read (no unread signs), so this does not make the card
   partial; but the translation's bracketed completion "[be there]" / "that is why" is interpretation and should be kept
   clearly marked as such in the report, as SOLUTION.md already does. Also consider the alternative reading "should I not
   [come] at half past seven" without the implied excuse.
3. (minor) Wording: SOLUTION.md calls hcp-1134/1113/1045 "finished" cards and the key "already proven". These cards are at
   REVIEWED1/ACCEPT, not FINAL. Say "accepted in review" instead.
4. (minor) The address street ("Alte B…straße") is reported loosely; it is outside the cipher and partly hidden by the
   collection stamp, so this is acceptable, but the report should say it is unread rather than suggest a name.

Note on the user's Jolánka steganography remark (stamp-box messages): not applicable to this Lehmann card; the stamp is
affixed and the type label MASC (number substitution) is correct. No steganography is visible.

## What I could not verify

- Whatever might be under the affixed stamp.
- The writer's identity ("Susi" is only a likely attribution from sister cards; the card is unsigned).
- Whether a published solution exists (I did no web search either).
