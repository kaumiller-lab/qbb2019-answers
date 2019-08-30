#!/usr/bin/env python3

"""
Usage: ./homework-ex4.py <ctab1> <ctab2>
"""


import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm = {name1 : ctab1.loc[:,"FPKM"],
        name2 : ctab2.loc[:,"FPKM"]}

df = pd.DataFrame(fpkm)
df += 1

r = df.loc[:,name1]
g = df.loc[:,name2]

m = np.log2(r/g)
a = 0.5 * np.log2(r*g)

fig, ax = plt.subplots()
ax.scatter(a,m, alpha = 0.7, s = 0.3)

plt.xlabel("log2 average expression")
plt.ylabel("log2(SRR072893/SRR072894)")
plt.suptitle("M-A plot")
fig.savefig("hw4_MA-plot.png")