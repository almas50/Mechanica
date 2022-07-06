import random
import csv


import numpy as np


n_num, m_num = map(int, input().split())

vectors = []
for i in range(n_num):
    vector = []
    for j in range(m_num):
        vector.append(random.uniform(-1, 1))
    vector_np = np.array(vector)
    vectors.append(vector_np)

with open('vectors.csv', 'w', newline='\n') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(vectors)
