import sys
from itertools import combinations

def j(i, u): return len(i)/float(len(u))

ds = []
for line in sys.stdin:
    ds.append(set(line.split(',')))

for d1, d2, d3 in combinations(ds, 3):
    c1 = d1 & d2 & d3
    c12 = d1 & d2
    c21 = d1 | d2
    c23 = d2 & d3
    c32 = d2 | d3
    c13 = d1 & d3
    c31 = d1 | d3
    c2 = c12 | c23 |c13 
    c3 = d1 | d2 | d3
    print((j(c1, c2)-j(c2, c3))/j(c2,c3))
