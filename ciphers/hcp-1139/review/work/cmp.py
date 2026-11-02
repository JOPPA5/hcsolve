# compare the reading block in SOLUTION.md with the block printed by decode.py, ignoring glosses and line breaks
import re,subprocess
b='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1139/'
s=open(b+'SOLUTION.md',encoding='utf8').read()
s=s[s.index('Kedves Margitkám!'):s.index('Address (open)')]
s=re.sub(r' \[= [^\]]*\]','',s)
o=subprocess.run(['python3','-I',b+'work/decode.py'],capture_output=True,text=True).stdout
o=o[o.index('Reading text:'):]; o=o[o.index('Kedves'):o.index('Address (open)')]
n=lambda t:' '.join(t.split())
print(n(s)==n(o))
