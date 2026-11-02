#!/usr/bin/env python3 -I
"""Reviewer's independent transcription of HCP1208 as SIGN CLASSES (not letters), read from
work/hires on enlarged crops, decoded with the family table of hcp-1216/SOLUTION.md, and
diffed against the solver's work/ledger.txt.  Run: python3 -I review/work/redecode.py (from the cipher dir)."""
import difflib, os
KEY={'B2':'a','SIX':'b','LB':'c','TICK':'d','B3':'e','PLUS':'f','OPEN':'g','TS':'h','DOT':'i','INV':'j','FIVE':'k',
     'WAVE':'l','S3':'m','S2':'n','LOOP':'o','F':'r','RB':'s','GAM':'t','X':'u','CHEV':'v','DESC':'y','CROSS':'z'}
R="""01 RB CROSS B3 F B3 GAM B3 GAM B3 TICK B3 RB INV LOOP WAVE B2 S2 FIVE B2 S3
02 FIVE DOT CHEV B2 S2 LOOP S3 TS LOOP OPEN DESC B2 WAVE B3 OPEN INV LOOP SIX SIX FIVE B3 TICK
03 CHEV B3 SIX B3 S2 GAM B2 WAVE B3 WAVE INV B2 RB LOOP F B2 DOT S3
04 RB B2 INV S2 B2 WAVE LOOP S3 TS LOOP OPEN DESC B3 CROSS GAM B2 WAVE B2 TS LOOP GAM
05 FIVE B3 WAVE FIVE X WAVE TICK B3 S2 B3 S3 S3 B3 F GAM S3 B2 OPEN B2 DOT RB
06 OPEN LOOP S2 TICK LOOP WAVE INV B2 TS LOOP OPEN DESC CHEV B2 WAVE B2 S3 DOT
07 FIVE X WAVE LOOP S2 LOOP RB TICK LOOP WAVE LOOP OPEN B2 TICK GAM B2 B3 WAVE LOOP
08 S3 B2 OPEN B2 GAM RB B2 INV S2 B2 WAVE B2 GAM GAM B2 WAVE FIVE B3 WAVE GAM X
09 TICK B2 GAM S2 LOOP S3 B3 TICK B3 RB B3 S3 TS LOOP OPEN DESC B2 CHEV LOOP S2 B2
10 GAM X S2 FIVE B2 GAM WAVE B3 S3 LOOP S2 TICK INV B2 FIVE B3 RB DOT OPEN DESC
11 S3 LOOP RB GAM S3 B2 F S2 B3 S3 GAM X TICK LOOP S3 TS LOOP OPEN DESC
12 TS LOOP WAVE S2 B2 TS B2 CROSS B2 CROSS TS B3 S2 GAM B2 FIVE B2 S2
13 TICK B3 WAVE X GAM B2 S2 RB CROSS B2 SIX B2 TICK WAVE B3 RB CROSS B3 FIVE B3
14 B3 RB TS LOOP OPEN DESC B3 WAVE S3 B3 TS GAM B3 FIVE B3 S3 B3 OPEN
15 TS LOOP CROSS B3 TICK B3 RB B3 S3 S3 DOT CHEV B3 WAVE S3 B3 OPEN
16 S2 B3 S3 GAM X TICK LOOP S3 TS LOOP OPEN DESC TS LOOP CHEV B2
17 S3 B3 OPEN DESC X S2 FIVE B3 RB S3 DOT FIVE LOOP F INV LOOP
18 CHEV X S2 FIVE CHEV DOT RB CROSS RB CROSS B2 TICK B3 TS B2 WAVE B3
19 TS B3 GAM B3 WAVE S3 B3 OPEN DESC B3 FIVE B3 CROSS B3 WAVE
20 SIX B3 CROSS B2 F LOOP S3 RB LOOP F B2 DOT S3
21 S3 B2 F B2 TICK LOOP FIVE RB DOT F DOT FIVE TS X
22 FIVE B3 TICK CHEV B3 RB B3 PLUS B3 F DOT
S1 LB RB LOOP FIVE LOOP WAVE
S2 RB CROSS B2 S3
S3 GAM B2 WAVE B2 S2
S4 RB CROSS LOOP F
S5 PLUS B3 F DOT TICK"""
mine={}
for l in R.splitlines():
    k,*t=l.split(); mine[k]=''.join(KEY[x] for x in t)
sol={}
for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../work/ledger.txt'),encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        k,*t=l.split(); sol[k]=''.join(x.split(':')[0].lower() for x in t)
n=0;d=0
for k in mine:
    n+=len(mine[k])
    same=mine[k]==sol[k]
    print(k,mine[k],'' if same else '  <> solver '+sol[k])
    d+=sum(i>0 for i in [not same])
print('signs reviewer',n,'solver',sum(map(len,sol.values())),'rows differing',d)
print('letters used',''.join(sorted(set(''.join(mine.values())))))
