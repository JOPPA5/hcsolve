from pathlib import Path
p=Path(__file__).resolve().parent
key={"--":"M","---":"O","-.":"N","-..":"D",".-":"A","-.--":"Y",
"...":"S",".--":"W",".":"E","-":"T","....":"H",".-.":"R"}
for line in (p/"opening-morse.txt").read_text().splitlines():
    print("".join(key[t] for t in line.split()))
print("Opening only; manual transcription; body not yet decoded.")
