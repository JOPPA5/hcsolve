from pathlib import Path
import json
p=Path(__file__).resolve().parent
x=json.loads((p/'followup-trace.json').read_text())
def letter(v): return chr(91-v)
for g in x['uncertain_groups']:
 out=[]
 for v in g['values']:
  out.append('['+'/'.join(letter(n) for n in v)+']' if isinstance(v,list) else letter(v))
 print(g['where']+': '+''.join(out))
 print('  '+g['reason'])
print('These are literal visual candidates/alternatives, not accepted phrase completions.')
