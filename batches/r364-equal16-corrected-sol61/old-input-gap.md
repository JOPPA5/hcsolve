# Prior input gap

The old equal16 sweep explicitly sets group12 to `ercuv`, and calls `solve(q+"?",...)` with an unknown suffix filler. It therefore does not test corrected `EXCUV`/`EXCVU` with an extraX at an arbitrary boundary. The corrected review runner covers only37 cases at widths21/19/20; the corrected double runner covers two stages only.

Exact old lines:

```python
  if errors==0:g[7]='tsnnd';g[9]='eloen';g[11]='ercuv'
  ct=''.join(x for i,x in enumerate(g) if i!=2);out=solve(q+'?',ct,ws,20000,errors,ns);out.update(mode='conditional_target',source_quote_is_assumed=True,reading=kind,omitted_group=3,alignments=ns,alignment_is_hypothesis=True);record(out);print('target',n,kind,out['status'],round(out['seconds'],3),flush=True)
```
