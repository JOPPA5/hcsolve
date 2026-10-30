"""Apply the hcp-1447 digit key to a transcription line (partial work)."""
import sys
KEY = {'1':'a','2':'e','3':'i','4':'o','5':'u','6':'l','7':'m','8':'n','9':'r'}
def dec(s):
    return ''.join(KEY.get(ch, ch) for ch in s)
for line in open(sys.argv[1], encoding='utf-8'):
    if line.startswith('#'):
        print(line, end=''); continue
    print(dec(line), end='')
