import csv
from math import sqrt

import numpy as np
import matplotlib.pyplot as plt

max_dist = {'len': 0, 'vec1': 0, 'vec2': 0}
min_dist = {'len': 10000, 'vec1': 0, 'vec2': 0}


def calculate_dists(vectors: list):
    # max euclidean distance is sqrt(4m)
    results_dict = {i / 10: 0 for i in range(0, round(sqrt(4*len(vectors[0])))*10)}
    plt.figure()
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            if i != j:
                if (dist := np.linalg.norm(vectors[i] - vectors[j])) > max_dist['len']:
                    max_dist['len'] = dist
                    max_dist['vec1'] = i + 1
                    max_dist['vec2'] = j + 1
                elif dist < min_dist['len']:
                    min_dist['len'] = dist
                    min_dist['vec1'] = i + 1
                    min_dist['vec2'] = j + 1
                results_dict[round(dist, 1)] += 1
    plt.bar(list(results_dict.keys()), list(results_dict.values()), width=0.1)
    plt.show()


vectors = []

with open('vectors.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        vector = np.array(list(map(float, row)))
        vectors.append(vector)

calculate_dists(vectors)

print(f'min_vec1: {min_dist["vec1"]}, min_vec2: {min_dist["vec2"]}, euclidean distance: {min_dist["len"]}')
print(f'max_vec1: {max_dist["vec1"]}, max_vec2: {max_dist["vec2"]}, euclidean distance: {max_dist["len"]}')
