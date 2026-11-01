"""Reviewer's own reading of hcp-1247, typed row by row from enlarged crops of the hi-res address side.
One char = one written sign. Run: python3 -I review_decode.py
Glyph codes: = two bars, 6 six, ( left bowl, / short+long stroke, E three bars, + cross, g descending curve,
I long+short stroke (h/p), i crossed/2-like curve, T inverted T, S section mark, ~ wave, M three strokes,
N two strokes, o loop, F F-sign, D right bowl, G gamma, X cross-x, V chevron, Y low descender, Z crossed diagonal,
' ' row word gaps ignored, ? unread, 5 0 digits, . point, [ ] hidden sign restored"""
import re,sys,difflib,unicodedata
K=dict(zip('=6(/E+gIiTS~MNoFDGXVYZ','abcdefghijklmnorstuvyz'))
R={ '01':'DZEFEGEGE/EDToN~=NS=MEgYEG'.replace('DZEFEGEGE/ED','DZEFEGEGE/ED'),}
R={
'01':'DZEFEGEGE/EDTo~=NS=MEgYEG','02':'~ENFEMENYEMNEI=F=gX/ToN','03':'IogYEgYEDDoF=iGV=~=DZ',
'04':'NE~SX~I=gYG=M/EN=gYoNE~','05':'V=gYoS+og~=~V=XgYE6=F','06':'E/EDEMMiTENgYoFD=NGE',
'07':'~iS=Zi/ogoN/o~oMIogY','08':'DZE/(DoMo~EIEGD=TN=~oM/E','09':'MEgEgYEN~oFENEMGX/oMMEg',
'10':'iFNiIogYM=g=MENYiGSX~','11':'/oGMiIETF=EFESFogGoN','12':'oDZEo~V=DoMEDMEgiFoM.',
'13':'E/EDEM=Mi=MX~=GD=goGi~E','14':'GiEN(D=SXgYMENGEMVo~','15':'N=I=M=g=V=~MX~=G=MVo~',
'16':'N=MEFGI=M=g=V=~NEMGo~G','17':'IEGEMEL=SoFNEMEF/EMED'.replace('L','~'),'18':'So~GENi~EgSEVEDE66=~E',
'19':'SE?V=gY50S.N=6=iNS=6~EMoN','20':'/oS=FEN/EZoDEgFo~M=T/','21':'I=+E~ToNE/EDEMM=g=V=~MX',
'22':'~=GI==SoFX~MENYESENgE/iS','23':'=ZGIiDZEMM=g=iDDZoF=SoZNiToN+E~IigYTEE~E/EDEM',
'24':'ENDZEFEGNEMM=F~EgTo66=NI=V=DXG=DNEV=gYTo6EN','25':'MoN/=ZEN','26':'',
}
R['25']='MoN/=ZENE/EDSiD+E~EDEgENESMoN/I=GNEM.EZG'
R['26']='~=IoGSEGN=IigiFG=MgoN/o~I=GT=MENYiFE'
R['B']='GEN V E ~ E E / E D E M'.replace(' ','')
def dec(s):
    return ''.join(K.get(c,c) for c in s)
led={}
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l[:2] in ('# ',) or not l.strip(): continue
    p=l.split(); 
    led[p[0]]=''.join(unicodedata.normalize('NFD',t.split(':')[0]).lower().replace('[','').replace(']','').replace('x','u') for t in p[1:])
for r in [f'{i:02d}' for i in range(1,27)]:
    me=dec(R[r]); so=led[r].replace('p','h').replace('gy','gy').replace('cs','cD'.lower())
    so=so.replace('cd','cs')
    if me==so: print(r,'same',len(me))
    else:
        print(r,'DIFF');print('  me ',me);print('  led',so)
