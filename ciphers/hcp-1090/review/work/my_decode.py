# Independent reviewer decode of hcp-1090 (Claude Opus 5.5, review round 1).
# Transcription typed by the reviewer from rotated hi-res crops (review/work/rot.png, rows = writer's lines,
# top row = rightmost column). '/' separates letters; '?' = the grey Kurrent letter (not Morse).
rows = [
 ".-.. .. . -... . .-. . .-. -. ... -",
 ".-- .. . --. . ..... - . ... -.. .. .-.",
 "--- .-- .-.- .-. . ... - -.. ..-",
 "-.. --- ---- ..... .. . .-. .-- .. .",
 "... ---- ---. -. .-- .- .-. . ...",
 "...- --- .-. ...- .. . .-. --.. . ..... -.",
 "- .- --. . -. ..- -. -.. .--- . -",
 "--.. - .. ... - . ... -- .. .-. ...",
 "--- .-.. .- -. --. .-- . .. .-..",
 ".. --. -.- --- -- -- . -... .-",
 ".-.. -.. .. ---- ..-. .-. . ..- . -- .. ----",
 "... --- ... . ..... .-. .- ..- ..-. -.. .-",
 "... .-- .. . -.. . .-. ... . ..... . -.",
 ".. ---- --. .-. ? ..... ... . -.. .. ----",
 "..... . .-. --.. .-.. .. ---- -.. . .. -. .",
 ".- -. -. .-",
]
STD = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I',
 '.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S',
 '-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','.-.-':'Ä','---.':'Ö',
 '..--':'Ü','----':'CH','.....':'5'}
out=[]
for r in rows:
    s=''.join(STD.get(t,'[%s]'%t) if t!='?' else '(u)' for t in r.split())
    out.append(s); print(s)
print('\nSTREAM:', ''.join(out))
import collections
print('symbol counts:', collections.Counter(t for r in rows for t in r.split()).most_common(8))
