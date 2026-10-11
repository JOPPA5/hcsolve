from pathlib import Path
import json, hashlib, subprocess, difflib, unicodedata, shutil, re
root=Path(__file__).resolve().parents[2]
out=Path(__file__).resolve().parent
for name in ('opening','86','231','date'):
    shutil.copyfile('/tmp/hcp351-review-'+name+'.png',out/('351-'+name+'.png'))
for n in (350,351):
    d=root/f'ciphers/hcp-{n}'; w=d/'work/kryha-decipherment'
    assert (d/'REVIEWED1').exists() and not (d/'FINAL').exists()
    for f in ('ciphertext.txt','prepared-plaintext.txt','key.json'):
        assert not (w/(f.rsplit('.',1)[0]+'-before-review1.'+f.rsplit('.',1)[1])).exists(), 'One-shot response already applied; preserve snapshots'
        shutil.copyfile(w/f,w/(f.rsplit('.',1)[0]+'-before-review1.'+f.rsplit('.',1)[1]))
    if n==351:
        ct=list((w/'ciphertext.txt').read_text().strip())
        edits=[(11,'r','p'),(12,'w','m'),(231,'l','i')]
        for pos,old,new in edits:
            assert ct[pos-1]==old; ct[pos-1]=new
        (w/'ciphertext.txt').write_text(''.join(ct)+'\n')
        manifest=json.loads((w/'pixel-manifest.json').read_text())
        manifest.append(dict(label='post-review1-default',reading_process='Prose-assisted source reinspection after review; agrees with pre-recovery blind Claude for 11,12,231. Not a new blind reading.',edits=[dict(position_one_based=p,before=a,after=b,confidence='moderate',evidence=e)for (p,a,b),e in zip(edits,[
            'Group3 has a printed P bowl; the apparent diagonal leg overlaps the blue stamp. P is preferred; R remains an obscured alternative.',
            'Group3 has vertical outer strokes consistent with M; the stamp crosses the middle. M is preferred; W remains an obscured alternative.',
            'Group47 first glyph is a straight I; the lower portion overlaps the blue stamp. Adopt I with blind-reader agreement, retain L alternative in pre-review snapshots.'])],retained=[dict(position_one_based=86,letter='r',alternative='p',evidence='Visible diagonal leg favors R. P is the blind-reader/lexically correct alternative; retained raw PSEDAVAIUCI is disclosed as a garble.'),dict(position_one_based=73,letter='o',alternative='u',evidence='Closed oval favors O; blind reader marked U uncertain.')]))
        (w/'pixel-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    hashes=json.loads((w/'transcription-hashes.json').read_text())
    for f in w.glob('ciphertext*.txt'):hashes[f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
    (w/'transcription-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    code=(w/'decrypt.py').read_text()
    code=code.replace("choices=['collated','strong','moderate','collated-moderate'],default='collated'","choices=['reviewed','collated','strong','moderate','collated-moderate'],default='reviewed'")
    code=code.replace("{'collated':'ciphertext.txt'","{'reviewed':'ciphertext.txt','collated':'ciphertext-before-review1.txt'")
    (w/'decrypt.py').write_text(code)
    raw=subprocess.check_output(['python3',str(w/'decrypt.py')],text=True).strip()
    (w/'prepared-plaintext.txt').write_text(raw+'\n')
    key=json.loads((w/'key.json').read_text());key['plaintext']=raw.lower();(w/'key.json').write_text(json.dumps(key,indent=2)+'\n')
    ed=(w/'editorial-reading.txt').read_text()
    norm=''.join(c for c in unicodedata.normalize('NFD',ed.lower())if 'a'<=c<='z')
    stripped=raw[5:].lower().replace('j','')
    diff=[dict(tag=t,raw_span=[a,b],editorial_span=[c,e],raw=stripped[a:b],editorial=norm[c:e])for t,a,b,c,e in difflib.SequenceMatcher(None,stripped,norm,autojunk=False).get_opcodes()if t!='equal']
    (w/'editorial-differences.json').write_text(json.dumps(dict(warning='Interpretative comparison only: removes first5 and literal J, not proof every J is a separator. Not exact historical plaintext.',removed_J_onebased_positions=[i+1 for i,c in enumerate(raw)if c=='J'],differences=diff),indent=2)+'\n')
    s=(d/'SOLUTION.md').read_text()
    s=s.replace(f'# HC{n} — proposed content decipherment; incomplete historical preparation',f'# HC{n} — reviewed content decipherment and working key')
    s=s.replace('A complete physical key is supplied','A complete working key in a mechanically consistent adjustable Kryha interpretation is supplied')
    s=s.replace('This is a partial decipherment pending independent Claude review, not a claim of error-free historical plaintext or a register-ready complete solution.','The connected message content and working key are recovered. Claude accepted350 and upheld351 subject to the source corrections addressed below. The exact historical preparation remains incomplete; this is not a claim of error-free archival plaintext or uniquely identified original machine settings.')
    start=s.index('The default `collated` variant')
    end=s.index('\n\n## Physical key',start)
    s=s[:start]+'''The default `reviewed` variant includes the post-review351 readings11 R→P,12 W→M and231 L→I, in addition to the earlier240 U→J correction. The source crops and reasoning are in `batches/kryha-review1-main/`; all are prose-assisted reinspection, not blind. Positions11/12/231 agree with Claude's independent pre-recovery blind transcription. Position86 retains visually preferred R despite the blind P alternative; raw PSEDAVAIUCI is not silently corrected. Position73 retains O. The numerical key is unchanged. `--variant collated` preserves the exact DONE1 default via `ciphertext-before-review1.txt`; `strong`, `moderate` and `collated-moderate` preserve their earlier snapshots, including disputed stamp readings. For350 all variants are identical. `--json` reports exact re-encryption. No language cleanup, I/J replacement, omission or indicator removal is performed.''' +s[end:]
    s=re.sub(r'(```text\n).*?(\n```)',lambda m:m[1]+raw+m[2],s,count=1,flags=re.S)
    s=s.replace('Its role is unknown. We do not invent a natural-language opening or declare a five-letter indicator. 350 text from position6 begins literal ZMNOHYCHMOZNOSTI;351 has the damaged ZMNOHZJHMOZNOSTTI.','It is probably an unenciphered indicator, an inference rather than a documented procedure: both cipher groups are identical although the two body keys give different displacements and different raw letters there. Its meaning is unknown. We do not invent a natural-language reading. 350 text from position6 begins ZMNOHYCHMOZNOSTI; the reviewed351 reading begins ZMNOHYCHMOZNOSTTI.')
    s=s.replace('Under the archived strong transcription the aligned interior had six literal discrepancies; the default correction351240J reduces this to five. Under collated-moderate (also231I) four remain.','Under the archived strong transcription the aligned interior had six literal discrepancies; the DONE1 default correction351240J reduced this to five. The reviewed default also adopts231I and has four:350 positions81,85,122,315 against351 positions82,86,123,316.')
    s=s.replace('These are solver-team audits; Claude\'s independent provider review is still pending.','These are solver-team audits. Claude\'s independent provider review is complete and addressed below.')
    s=s.replace('No register entry is justified for this incomplete claim.','No register entry is created for the unresolved historical preparation/first-group portion; the accepted content recovery is distinguished from a complete historical-procedure claim.')
    if n==350:
        response='''## Response to review 1

Claude Opus5.5 verdict **ACCEPT**. Its independent decoder reproduces all385 letters and re-encrypts them exactly. The review also compares a pre-recovery blind transcription: it agrees with all four350 corrections and independently supports the recovered content. The reviewer supplied the original paired-period lead and explicitly disclosed that limit on independence; the numerical key/content recovery was the solver team's work.

1. **Physical interpretation:** retained “mechanically consistent adjustable Kryha key”; the report distinguishes recovered rings/displacement increments from unverified original machine identification and hardware settings.
2. **SOSOL:** now described as probably an unenciphered indicator, explicitly an inference. Its meaning remains unknown and the decoder still covers all385 positions.
3. **One-stop difference:** the report notes as conjecture that replacing hole0 by48 could explain a repeat being unreadable under the other key. This is not a proven historical error.
4. **Garbles:** the report compares raw350 DRAAE/POPROT/PRISTUPIK with351 DRAHE/POPROS/PRISTUPIT, preserving all clear source letters. Also discloses350 PREDAVAIUCI versus351 PSEDAVAIUCI (sourceR/P alternative).
5. **Outcome:** now states content and working key recovered, while keeping original procedure, first group and rare-label ambiguity open. No register entry for the remaining partial historical claim. Earlier raw snapshots remain reproducible.
'''
    else:
        response='''## Response to review 1

Claude Opus5.5 verdict **REVISE**, expressly upholding the decipherment and requiring no second round unless the key changes. All numerical key fields are unchanged; only three source readings and documentation changed. The350 general findings are addressed in both reports.

1. **11/12:** source reinspection prefers PMQKK: printed P lacks a securely separate R leg and the outer strokes support M, while the blue stamp crosses both. Adopt11P/12M, agreeing with the independent pre-recovery blind reading. The raw opening becomes ZMNOHYCHMOZNOSTTI. R/W remain obscured alternatives in the DONE1 snapshot; this reinspection is not blind.
2. **86:** retain R because a diagonal leg is visible. Explicitly disclose P as the blind-reader and grammatical alternative: R gives PSEDAVAIUCI, P gives PREDAVAIUCI. The latter remains in the older moderate variant, not silently imposed.
3. **231:** adopt I as the reviewed default, with the straight stem and independent blind agreement; a lower-foot watermark leaves L as an alternative. Raw EXIITUIE becomes EXISTUIE under the unchanged key.
4. **73:** retain O: closed oval, raw SUVELMI. Blind U was uncertain and gives SLVELMI.
5. **Offset:** relative to350,351 has an extra T at position21 (MOZNOSTTI) and lacks E in final ROZHODNUTIE, giving ROZHODNUTI. This explains the +1 body alignment and return to alignment for final DOTROCHDNI. These are literal differences, not proof of where an error arose.
6. **Date:** source postmark reads −2 III44−23 and handwritten816/1229. Thus arrival appears2March1944, conflicting with portal1944-11-03; dispatch day is not thereby proved. SOURCES and report now state the conflict explicitly.
7. **Attribution:** earlier GPT-6 Astra produced unresolved attempts; GPT-6.1 Sol subagents recovered the cycle/working key/language and performed audits. Main OpenAI GPT integrated the result and selected rare-label semantics. Claude Opus5.5 supplied the paired-period lead and independent review. Historical NOTES header is clarified rather than relabeling earlier work.
'''
    s+='\n\n'+response+'''\nAdditional validation after DONE1, not rerun by Claude: `batches/kryha-endtoend-sol61/REPORT.md` preserves two fresh clean385-letter paired controls with the full cipher-only chain, supplied only period23, +1 pairing, geometry and generic TRAIN scores. Exact texts and both masks occur among the two predeclared6/7-gram winners in each control. No single objective passes both; automatic single-winner selection remains unvalidated. This supplements rather than replaces the review's actual blind-source check.
'''
    (d/'SOLUTION.md').write_text(s)
    notes=(d/'NOTES.md').read_text();notes=notes.replace(notes.splitlines()[0],f'# HC{n} solver log — historical Astra attempts; content recovery with GPT-6.1 Sol')
    notes+='\n\n## Review1 addressed\n\n'+response.split('\n\n',1)[1]+'\nPost-review source corrections and raw snapshots are explicit; no numerical key field changed. Final report retains the full literal output and uncertainties. No watcher/reviewer started.\n'
    (d/'NOTES.md').write_text(notes)
    if n==351:
        with (d/'SOURCES.md').open('a')as f:f.write('\n\n## Post-review source reinspection\n\nImmutable scan postmark reads −2 III44−23, handwritten816/1229. Arrival therefore appears2March1944; portal date1944-11-03 conflicts and dispatch date remains unproved. Original metadata is preserved. Positions11/12 favorPM overRW under the stamp;231 favorsI overL with foot ambiguity;86 retainsR withP alternative;73 retainsO over uncertainU. Crops and reasoning in batches/kryha-review1-main/, no sourcepixels edited. Claude pre-recovery blind reading is disclosed in review/REVIEW1.md; our reinspection is prose-assisted.\n')
    print(n,raw)
