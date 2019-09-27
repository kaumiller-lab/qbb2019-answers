#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

eigenvec = open(sys.argv[1])

pca1_lst = []
pca2_lst = []

for line in eigenvec:
    fields = line.rstrip("\t").split()
    pca1_lst.append(float(fields[2]))
    pca2_lst.append(float(fields[3]))

    
fig,ax = plt.subplots()
ax.scatter(pca1_lst, pca2_lst)
ax.set_ylabel("component 2")
ax.set_title("PCA Plot")
fig.savefig("pca.png")
plt.close()


