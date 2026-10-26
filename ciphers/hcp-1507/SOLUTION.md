# Portal1507 / pc_hcp_188 — full numeric-message candidate

The portal showed **Not solved** on2026-10-26. This is a solver candidate
awaiting independent review, not an accepted final solution.

## Type, key and reproduction
Monoalphabetic number substitution. Observed key:
|Number|Letter|Number|Letter|Number|Letter|
|---|---|---|---|---|---|
|1|M|3|E|4|R|
|6|L|7|O|8|T|
|9|P|10|S|11|F|
|12|A|13|G|14|K|
|16|U|17|I|18|D|
|20|C|21|W|22|H|
|24|X|25|N|26|Y|

Run from the repository root:
`python3 ciphers/hcp-1507/work/decode.py`

This verifies hashes of both original scans and metadata, then decodes the own
manual image transcription in work/transcription.txt. There is no attached
transcription. The program does not OCR the source; inverse-key roundtrip
verifies the mapping, not independent correctness of manual pixel readings.

## Literal plaintext
```
MY DEAR LEAH
I EXPECT TO
SEE YOU IN
TOWN Sat. Eve. DEAR
DOR ME
A RIDE W ILL DO
YOU GOOD HONEY
I WILL LOOK FOR
YOU SWEETHEART
Good. N IGHT
```
Sat. Eve. and Good. are unencrypted cursive words, explicitly braced in the
transcription. W ILL and N IGHT join to WILL and NIGHT without changing
letters. DOR remains the literal output, not silently replaced by FOR.

Natural reading, with one proposed correction:
“My dear Leah, I expect to see you in town Sat. eve. Dear, [for?] me a ride
will do you good, honey. I will look for you, sweetheart. Good night.”
Punctuation is editorial; wording around “for me” is awkward, even with that
correction. A more idiomatic rewriting is not presented as recovered text.

## Slovak translation
„Moja drahá Leah, očakávam, že sa uvidíme v meste v sobotu večer. Drahá,
[pre mňa?] jazda ti prospeje, miláčik. Budem ťa vyzerať, drahá. Dobrú noc.“
The bracketed segment retains the unresolved DOR/FOR issue.

## Scope and uncertainty
Every numeric position in the main message is mapped with one key, with no
per-word exceptions. DOR corresponds to visible18.7.4; intended FOR is a
hypothesis requiring18→11. Review should specifically inspect that word.
The numeric message contains93 encrypted positions, all mapped. Hash and
inverse-key roundtrip checks passed using the saved decoder.
The date, nonalphabetic cross marks, and cursive signature are not counted
as encrypted text. Signature identification is not claimed. The plain margin
request reads “Please come to the store first thing”.
Continuous English, repeated key agreements, and image checks support the
candidate; related-card evidence alone is not proof of decipherment.
No attached/published solution was used. Fresh110-record register snapshot
has no URL/name match; no historical-priority claim.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT, 2026-10-26. The reviewer read all
93 numeric signs without the solver's file and agrees token for token (apart
from one dash-marked word break in MY). An independent decoder with no code
from `work/` gives the same text. Transcription, key and plaintext are
unchanged.

1. **SEE not certain at sign level (minor).** Accepted as a disclosure. The
   second digit of the first token on line 3 lies between this writer's `0`
   and top-loop `8`. As `18.3.3` the word would read DEE. Context fixes SEE
   (`10.3.3`). It is now listed in the report's uncertainties.
2. **DOR, possible readings (minor).** The literal `18.7.4` = DOR stays. The
   report now gives two guesses, both labelled as guesses: FOR (needs 18→11;
   the reviewer confirms the sign is the writer's 18, not 11) and DO plus a
   stray `4` ("Dear, do me…"). Neither is put into the recovered text.
3. **Header date (minor).** Accepted. The written date reads `5-10-13` (one
   day digit overwritten, 10 over 9 or the reverse). It agrees with the
   postmark KNOXVILLE MAY 10 1913 and the portal date 1913-05-10. The report
   gives it as the date of the card. The earlier "not confidently
   transcribed" remark is superseded for the date. The cursive signature
   remains unread.
4. **Cross-card evidence (minor).** Recorded in the report as supporting
   evidence. HCP 1506 (pc_hcp_187) has the same recipient (portal: Leeah
   Doane) and uses the same key, and its header group `24.24.24` decodes to
   XXX with this card's 24=X. HCP 1506 is still in its own review round, so
   it is cited as corroboration, not as an accepted solution.

Metadata note: the portal catalogue spells the recipient "Leeah Doane". The
address side reads "Miss Leah Doane, Little Marsh, Pa.", and the cipher
greeting reads LEAH. The report records this as a catalogue spelling
discrepancy; `source/metadata.md` is unchanged.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
