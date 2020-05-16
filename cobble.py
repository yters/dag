import sys
from random import randint
from random import sample
from itertools import combinations

d_size = int(sys.argv[1]) 
w_len = int(sys.argv[2]) 
d_count = int(sys.argv[3])

ds = []
for _ in range(d_count):
    d = []
    for _ in range(d_size):
        w = [randint(0,1) for _ in range(w_len)]
        d += [w]
    ds += [d]

g_len = int(sys.argv[4])
population = []
for d1, d2 in combinations(ds, 2):
    g = []
    for _ in range(g_len):
        g += sample(d1 + d2, 1)[0]
    population += [g]

for g in population:
    print(''.join([str(i) for i in g]))
