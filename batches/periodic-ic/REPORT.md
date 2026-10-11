# New unknown-step periodic-ring control

Mathematical separation: if d_i=R[i modT]+floor(i/T)S, projected frequency concentrations within each residue class are independent of unknownR. Search outputalphabet O using sum of26-symbol frequencyconcentrations acrossTstrata, then alignstrata using globalconcentration, fit inputalphabetby language, jointly refineO/input/R. This explores unknownstepoffsets, extending fixed17step search.

Independent385-letter held-out control, two randomly permutedrings,20random periodicsteps, knownT20/totalS5 only.500×10000O proposals retain100; each20×5000phasealignment+8×30000MASC; languagehighest seed jointlyrefined8×100000 withouttruthselection. CandidateO matches atmost11/26 up torotation. Fullpipeline didnotrecoverwholecontrol; see pipeline-control-report.json. NO target attempted. Cannotexclude anyKryha model. Seed/key were used onlyto generatecontrol anddiagnose finalperformance. No watcher/reviewer. MainmodelOpenAI GPT.

Reproduce: `python3 batches/periodic-ic/control.py` followedby `batches/periodic-ic/align_language ciphers/hcp-350/work/ring-4grams.tsv batches/periodic-ic/control-cipher.txt 20 5 batches/periodic-ic/control-candidates.txt > batches/periodic-ic/align-control-result.txt` . PublishedGerman52-stop/word-J memo iscontext, not thismodel's actualSlovakadoption evidence.
