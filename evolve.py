import sys
from random import randint
from random import random

split_prob = float(sys.argv[1])
mutate_rate = float(sys.argv[2])

genome = [randint(0,1) for _ in range(int(sys.argv[3]))]
population = [genome]

while len(population) < int(sys.argv[4]):
    for genome in population:
        if random() < split_prob:
            new_genome = [i for i in genome]
            population.append(new_genome)
        for i in range(len(genome)):
            if random() < mutate_rate:
                genome[i] = 1-genome[i]

for genome in population:
    print(''.join([str(i) for i in genome]))
