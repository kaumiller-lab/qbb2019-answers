#!/usr/bin/env python3

"""
Usage: ./lunch_ex2.py <ctab1> <ctab2>

compares two ctab files
"""

import sys
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

ctab1 = []
ctab2 = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    ctab1.append(float(fields[11]) + 1)

for i, line in enumerate(open(sys.argv[2])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    ctab2.append(float(fields[11]) + 1)
    
trans_ctab1 = np.log2(ctab1)
trans_ctab2 = np.log2(ctab2)    
coef = np.polyfit(trans_ctab1, trans_ctab2, 1)

def f(x, m, b):
    return (m * x) + b

xval = np.linspace(min(trans_ctab1), max(trans_ctab1),100)
yval = f(xval, coef[0], coef[1])

fig, ax = plt.subplots()
ax.plot(xval, yval, color = "red")

ax.scatter(x=trans_ctab1, y=trans_ctab2, alpha = 0.5, s = 0.3)
plt.suptitle("ctab1 vs. ctab2")
plt.xlabel("ctab1 FPKM")
plt.ylabel("ctab2 FPKM")
fig.savefig("lunch_ex2.png")
plt.close(fig)


