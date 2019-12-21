#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np

er4 = {}
g1e = {}

f1= (open(sys.argv[1]))

for line in f1:
    col = line.rstrip("\n").split("\t")
    er4.setdefault(col[3], 0)
    er4[col[3]] += 1
    
f2 = (open(sys.argv[2]))
for line in f2:
    col = line.rstrip("\n").split("\t")
    g1e.setdefault(col[3], 0)
    g1e[col[3]] += 1

gained = 0
lost = 0

f3= (open(sys.argv[3]))
f4= (open(sys.argv[4]))

for line in f3:
    gained += 1
    
for line in f4:
    lost += 1

x_value = np.arange(len(er4))
width = 0.3

fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(20, 10))
axes = axes.flatten()
axes[0].bar(x=["Lost", "Gained"], height = [lost, gained])
axes[0].set_xlabel("CTCF Binding Sites")
axes[0].set_ylabel("Number of Sites")
axes[1].bar(x= x_value - width/2, height = list(er4.values()), width = width, color = "blue", label = "ER4")
axes[1].bar(x= x_value + width/2, height = list(g1e.values()), width = width, color = "red", label = "G1E")
axes[1].set_xticks(x_value)
axes[1].set_xticklabels(er4.keys())
axes[1].legend()
axes[1].set_xlabel("Features")
axes[1].set_ylabel("Number of Sites")

fig.savefig("feature-overlapping.png")
plt.close(fig)