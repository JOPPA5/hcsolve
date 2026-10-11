#345 — unresolved

No key or deciphered plaintext is claimed. Manual65letter transcription matches the scanned body; possible inserted5letter indicator is not identified. Portal title and cover provide context, not known plaintext.

Contextual phrase inventory tests and exact single-columnar crib-placement tests are documented in NOTES.md. The exact algorithm recovers synthetic positive controls at widths16,19,22, but finds no occurrence of the tested long contiguous 'effektivnelei...kurierom' cribs for the actual text under any tested indicator removal. A separate language-score search fails its own exact-recovery controls, so its negative results are expressly weak.

The full body remains unresolved. R/XQ triple transposition is possible but unverified; no triple-key recovery achieved. There is no original-language plaintext/translation or command producing one. The analysis is reproducible via work/crib_irregular.py and companion scripts, not a decryption command. Sources preserved; no published target solution used, no marker/registerentry.

Further GPT-6.1 Sol analysis adds complete double-columnar enumeration for stage widths2–7 and all one-group omissions/full body. Independently seeded60/65-letter controls recover exactly, but all target best candidates remain incoherent. Exact monoalphabetic repeated-letter-pattern tests likewise reject only the literal tested Lei phrases, not the cipher family generally. Reproducible scripts and complete diagnostic candidates are in work/double_exact.cpp, double_exact.py, double7_sweep.py and substitution_crib_pattern.py. No full decipherment is established.

## Published original80102 now verified

The outside review suggested344, but that was not the original80102. MainbrowserGlobalFilter80102 found publicSolved486, whose Description explicitlysays80103repeats80102. Originalcipherandpublishedarchivalcleartext areattributedin batches/solved-context-main/486/SOURCES.md. Independentcompletecollation in batches/repeat345-486-sol61/REPORT.md confirms all65sourceletters match345and486exactly. This is a duplicate, notnewlydecipheredcontent.

Publishedquotedtelegram:

> dňa25.januára ide odtiaľ kurier,ktorým Vám pošleme effektívneLei.

English: On25January a courier leaves here, by whom we willsend you Lei in cash. The spellingskurier/effektívne belong to the publisheddraft. The originalcipherreceipt is19.I.1944, so486portal1943dateisdisputed, notsilentlyoverwritten.

Anexactconditionalpreparedpair exists: spell25as DVE PAT, preserveallotherlettersanddoubleF, stripspaces/accents/punctuation, omitfirstciphergroupHFEBM. The resulting60letters haveEXACTinventorymatchwith nofiller. This was theonlymatchin84declaredinventorycases, andH/Bonlyoccurinthefirstgroup. PreparationDVEandindicatoromission arehypotheses untilcryptographickeyvalidation. No day/indicatorpositionrule is inferredfromprefix1. TheolderIFATYindicatorguessisunmotivatedandsuperseded. Primary-sourceknownpairkeysearch nowuses this stronger input; publishedtextcannotbeclaimedasourownorregisteredasanewdecipherment.


## Conditional R key search

`batches/r345-knownpair-sol61/REPORT.md` records two independent exact formulations of the conditional 60-letter pair with widths 21/19/20. Known-key controls reproduce and invert all 60 letters, but independent blind controls time out; these checks therefore validate encoding without establishing efficient key recovery. An unrestricted target run also times out and remains UNKNOWN. The only UNSAT result is constant column-zero readout rank 1: each stage would preserve the input first letter D, whereas the selected ciphertext begins N. Header 165 does not establish that rank. A separate heuristic reaches only 45/60 letters on its control and was not used to infer a target key. No new key or new plaintext is claimed.
