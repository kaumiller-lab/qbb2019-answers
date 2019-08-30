#!/usr/bin/env python3

"""
Usage: ./homework_ex2.pv <gene_name> <FPKMs.csv>

Boxplot all transcripts for a given gene
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df = pd.read_csv(fpkm_file, index_col="t_name")
#print(df)

goi = df.loc[:,"gene_name"] == gene_name

fpkms = df.drop(columns="gene_name")

male = df.iloc[:, 1:9]

female = df.iloc[:, 9:18]

fig, (ax1,ax2) = plt.subplots(2)

male_trans = np.log2(male+1)
female_trans = np.log2(female+1)

ax1.boxplot(male_trans.loc[goi,:].T)
ax2.boxplot(female_trans.loc[goi,:].T)

ax1.set_title("male box plot")
ax1.set_ylabel("log2 FPKM")
ax1.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"], rotation = 45)
ax2.set_title("female box plot")
ax2.set_ylabel("log2 FPKM")
ax2.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"], rotation = 45)

plt.subplots_adjust(hspace=0.7)
fig.savefig("hw_boxplot.png")
plt.close(fig)
