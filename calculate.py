import csv

import numpy as np

max_dist = {'len': 0, 'vec1': 0, 'vec2': 0}
min_dist = {'len': 10000, 'vec1': 0, 'vec2': 0}


def calculate_dists(vectors: list):
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            if i != j:
                if (dist := np.linalg.norm(vectors[i] - vectors[j])) > max_dist['len']:
                    max_dist['len'] = dist
                    max_dist['vec1'] = i + 1
                    max_dist['vec2'] = j + 1
                elif dist:
                    min_dist['len'] = dist
                    min_dist['vec1'] = i + 1
                    min_dist['vec2'] = j + 1


vectors = []

with open('vectors.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        vector = np.array(list(map(float, row)))
        vectors.append(vector)

calculate_dists(vectors)

print(max_dist)
print(min_dist)
