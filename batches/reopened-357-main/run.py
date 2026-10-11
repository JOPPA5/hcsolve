from pathlib import Path
import json,subprocess
B=Path(__file__).parent;rows=[]
for case in json.loads((B/'manifest.json').read_text())['cases']:
    for family in ['myszkowski','amsco']:
        D=Path(f'batches/{family}-main')
        out=subprocess.check_output([str(D/'search'),str(D/'keywords.txt'),'ciphers/hcp-350/work/ring-4grams.tsv','ciphers/hcp-350/work/ring-5grams.tsv',case['input']],text=True)
        stem=Path(case['input']).stem;file=B/f'{stem}-{family}-candidates.tsv';file.write_text(out)
        best=out.splitlines()[0].split('\t')
        rows.append(dict(**case,family=family,candidates_file=str(file),best_score=float(best[0]),best_keyword=best[1],best_plaintext=best[-1]))
        (B/'results.json').write_text(json.dumps(rows,indent=2)+'\n')
        print(family,stem,best[0],best[-1],flush=True)
