A simple set metric to discriminate between trees and dependency graphs.

The basic idea is that if a set of three genomes are the leaves of a tree, then their total intersection (intersection of all three) will be covered by their pairwise intersections.  On the other hand, if a dependency graph, then quite likely they can have large pairwise intersections and no total intersection.

The metric is applied to the Lempel-Ziv dictionaries generated from binary 'genomes'.  Assuming `d1`, `d2` and `d3` are dictionaries generated from three distinct genomes, the metric is calculated as follows using Python3 for notation.
```
a = d1 & d2 & d3
b = (d1 & d2) | (d2 & d3) | (d1 & d3)
c = d1 | d2 | d3
j = len(a)/len(b)
k = len(b)/len(c)
metric = (j-k)/k
```
The script `dag.py` contains the metric calculation.

There are a couple scripts simulating different theories of how genomes are generated.

The `evolve.py` script evolves a set of genomes so they share a common tree.

The `cobble.py` script creates a set of independent sub sequence dictionaries, and then constructs a genome from each pair of dictionaries.  For instance, if there are 4 dictionaries, then there will be (4*3)/2 genomes.

If the metric works, then `evolve.py` genomes should score around 0 and `cobble.py` genomes should score around -1.

Here are some example runs confirming the prediction.
```
$ python evolve.py 0.01 0.5 10000 3 | python lzd.py | python dag.py
0.0715963943579
$ python evolve.py 0.01 0.5 10000 3 | python lzd.py | python dag.py
0.0898123710524
$ python cobble.py 2 100 3 4000 | python lzd.py | python dag.py
-0.931217139487
$ python cobble.py 2 100 3 4000 | python lzd.py | python dag.py
-0.934955415614
```
