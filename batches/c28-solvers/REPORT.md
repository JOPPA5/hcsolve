# Conditional28-letter C orthography search

Primary source: Antal/Grošek/Zajac2020, VHÚ article p107; publication key retains Č and Š, alphabet28. Key enciphering/decrypting is bijective on28symbols. In source transcription a..z plus `{`=Č and `|`=Š; scoring folds Č→C and Š→S against unchanged frozen Slovak3/4/5gram model. Therefore dictionary scoring alone cannot disambiguate all diacritics. Unknownciphertext glyphs retain `.` and contribute no n-gram across that position. No guessed glyphs inserted.

Two independent invented115-letter Slovak calibration paragraphs, random independent28-symbol keys, were both recovered EXACTLY after orthographic folding (115/115). This is not a guarantee of unique28-symbol keys or diacritic restoration.40restarts×100000proposals each, samealgorithm ontargets.

Targets369,367,334,332 forward and reverse literal transcriptions all yielded incoherent whole messages. No plaintext/key claimed.332 full43includesTRC prefix as explicit alternative; it does not establish that prefix is encrypted. Controls are not published target solutions. Othertruncations/28lettersubstitution/unknownplaintextlanguages remain open.

Reproducecontrols: `python3 ciphers/hcp-369/work/c28-controls.py`
Reproducetargets: `python3 ciphers/hcp-369/work/c28-targets.py`
Sourceunchanged, noDONE. Main solver model attribution:OpenAI GPT.


Also applied the literalpublishedp107Ckey and all28relativeplaintextalphabetrotations (bothtable directions andbodyorders) to15unresolvedtranscriptions:1,680conditionaloutputs. `published-key-rotations.json`, language-bestperrecord `published-key-best.json`; nonecoherent. This is applicationofpublishedcontextualkey, explicitlynot a newlyrecoveredkey. Doesnotcoverarbitrarydailytablechanges orallciphertextalphabetrotations.
