#!/usr/bin/env python3
"""Reviewer's independent decode of HCP1304: own key table and own reading of the
card (from review/work crops, in a descriptive stroke alphabet), compared with
the solver's ledger. Run: python3 -I ciphers/hcp-1304/review/work/my_decode.py"""
import os,re,difflib
H=os.path.dirname(os.path.abspath(__file__))
# my own stroke names -> plaintext
K=dict(aa='a',ee='e',six='b',cc='c',dd='d',plus='f',gg='g',hp='h',ii='i',jt='j',kk='k',wv='l',mm='m',nn='n',
 oo='o',rr='r',ss='s',tt='t',uu='u',ch='v',yy='y',zz='z',oe='ö',ue='ü',CS='cs')
R="""ss zz ee rr ee tt ee tt ee dd ee ss jt oo wv aa nn
kk aa mm six ee CS ee ss ss oo rr aa ii tt mm ee gg
kk aa hp tt aa mm mm ee wv yy ee tt kk oe ss zz oe
nn oe kk ss zz ee hp ee nn ii gg aa zz aa nn mm ee gg
hp aa tt ss oo rr aa ii mm ii six oe wv wv aa tt oo mm
mm ii wv yy nn ee mm ee ss ss zz ii ch ee ch aa nn oe nn
nn ee kk ee dd ee ss jt oo wv aa nn kk aa mm aa mm ii tt tt aa
wv aa nn nn ee mm ii ss ee rr dd ee mm wv ee kk mm ee gg
mm aa rr mm aa gg aa mm ii ss rr ee ss tt ee wv ee mm hp oo gg yy
ii gg yy wv ee ch aa gg yy oo kk ee gg ch ee hp aa mm oo
cc zz aa rr ee kk nn ee mm six ii zz tt aa tt nn aa nn aa kk
mm uu nn kk aa ch aa wv ee gg yy ss zz ee rr ue ee nn uu gg yy
tt ee nn nn ee kk mm ii nn tt hp aa mm ee ss ss zz ee ch oo wv
nn ee kk jt oo wv aa nn kk aa tt oo wv uu gg yy ee nn
ee wv mm ee nn ee kk aa ch aa rr oo ss six oo wv hp aa
ss oo rr oo zz aa ss nn ee mm wv ee nn nn ee aa zz tt
mm ee gg kk ee wv ch aa rr nn oo mm mm ee gg ee zz
aa tt oe mm ee gg ss zz tt rr aa jt kk ii ss aa kk aa dd aa jt oo zz
aa kk ee dd ch ee ss mm aa mm aa jt aa ee wv oo tt rr ee ss
tt ee wv wv ee mm mm aa gg aa mm hp aa zz uu dd nn ii
nn ee mm tt uu dd oo kk ii gg yy jt oo wv aa nn kk aa ii ss
tt uu dd jt aa hp oo gg yy nn ee hp ee zz aa hp ee jt zz ee
tt ee mm mm oo cc zz aa rr mm ee gg nn ee mm ii rr tt
tt aa wv aa hp aa zz tt gg oo nn dd oo wv tt aa hp oo gg yy
ch aa ss aa rr wv ee mm ee gg yy ee kk dd ee nn ee mm mm ee rr tt ee mm mm ee rr tt gg yy ue wv ee ss ch oo wv tt aa tt oe
mm ee gg ss zz tt rr aa jt kk mm ii aa tt tt aa mm aa zz tt hp ii ss zz ee mm kk ee dd ee nn kk ee zz dd oo dd ii kk hp aa ch aa
wv aa mm ii tt hp aa wv mm oo cc zz aa rr ee kk nn aa ii rr oo aa mm ee gg
ii ss tt ee nn ch ee wv ee
ee dd ee ss ee mm
ss ii rr ii gg hp ue
kk ee dd ch ee ss ee
plus ee rr ii"""
mine=[''.join(K[t] for t in l.split()) for l in R.splitlines()]
import subprocess,sys
root=os.path.join(H,'..','..','..','..')
out=subprocess.run([sys.executable,'-I','ciphers/hcp-1304/work/decode.py'],cwd=root,capture_output=True,text=True).stdout
sol=[m.group(1) for m in re.finditer(r'^\s*(?:\d\d|M|S\d) (\S+)$',out,re.M)]
print(len(mine),len(sol),'signs mine',sum(len(l.split()) for l in R.splitlines()))
for a,b in zip(mine,sol):
    print('=' if a==b else '!',a, '' if a==b else '| solver: '+b)
