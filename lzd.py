import sys

for line in sys.stdin:
    d = set()
    w = ''
    for c in line.strip():
        w += c
        if not w in d:
            d.add(w)
            sys.stdout.write(w + ',')
            w = ''
    sys.stdout.write('\n')
    sys.stdout.flush()
