from pathlib import Path
import json,math,shutil
p=Path(__file__).resolve().parent;repo=p.parents[1];shutil.copyfile(repo/'ciphers/hcp-350/work/ring-unigrams.tsv',p/'ring-unigrams.tsv');weights=sorted([float(line.split()[1]) for line in (p/'ring-unigrams.tsv').read_text().splitlines()],reverse=True);assert len(weights)==26
(p/'unigram-sorted-logprobs.txt').write_text(' '.join(map(str,weights))+'\n');folder=p/'control-m26';ct=(folder/'ciphertext.txt').read_text().strip();coords=json.loads((p/'wheel52.json').read_text())['unwrapped_effective_coordinates']
def counts(O,stops,phase):
 N=[0]*26;m=len(stops);origin=coords[stops[phase]-1]
 for i,c in enumerate(ct):D=coords[stops[(phase+i)%m]-1]+179*((phase+i)//m)-origin;N[(O[ord(c)-97]-D)%26]+=1
 return N
def profile(N):return math.lgamma(sum(N)+1)-sum(math.lgamma(n+1) for n in N)+sum(n*w for n,w in zip(sorted(N,reverse=True),weights))
key=json.loads((folder/'key.json').read_text());true=profile(counts(key['output_positions'],key['active_holes'],key['active_phase_index']));rows=[]
for r in json.loads((folder/'language-reranked.json').read_text()):
 N=counts(r['output_positions'],r['active_holes'],r['phase']);rows.append(dict(candidate_index=r['candidate_index'],profile_score=profile(N),IC=sum(x*x for x in N),language_score=r['language_score'],matches_diagnostic_only=r['matches_diagnostic_only']))
rows.sort(key=lambda r:r['profile_score'],reverse=True);report=dict(objective='multinomial histogram likelihood after optimal unknown input permutation: log(n!)-sum(log(N!))+sortedN dot sorted TRAIN log probabilities',training='frozen preparedSlovak first80percent completeUDsentences, noheldout or controlcounts used',true_profile_score=true,retained_false_candidates=len(rows),false_max=rows[0]['profile_score'],false_min=rows[-1]['profile_score'],false_ge_true=sum(r['profile_score']>=true for r in rows),rows=rows);(folder/'profile-diagnostic.json').write_text(json.dumps(report,indent=2));print(true,rows[0]['profile_score'],rows[-1]['profile_score'],report['false_ge_true'])
