import csv

import numpy as np


n_num, m_num = map(int, input().split())

vectors = np.random.uniform(-1, +1, (n_num, m_num))

with open('vectors.csv', 'w', newline='\n') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(vectors)
