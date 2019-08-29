#!/usr/bin/env python3

"""
Usage: ./01-histogram.py <ctab> <a> <mu_skew> <sigma_skew> <mu_norm> <sigma_norm>

plot FPKM
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fpkms = []

for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append(float(fields[11]))
        
my_data = np.log2(fpkms)

a = float(sys.argv[2])
mu_skew = float(sys.argv[3])
sigma_skew = float(sys.argv[4])

mu_norm = float(sys.argv[5])
sigma_norm = float(sys.argv[6])

x = np.linspace( -15, 15, 100)
y = stats.norm.pdf(x, mu_norm, sigma_norm)
z = stats.skewnorm.pdf(x, a, mu_skew, sigma_skew)

fig, ax = plt.subplots()
ax.hist(my_data, bins = 100, density = True)
ax.plot(x, y)
ax.plot(x, z)
plt.suptitle("fpkms")
plt.xlabel("log2(fpkms)")
plt.ylabel("percent sequences")
plt.figtext(x = 0.15, y = 0.8, s = "a = -10, mu_skew = 6, sigma_skew = 3.5")
plt.figtext(x = 0.15, y = 0.74, s = "mu_norm = 4, sigma_norm = 2")
fig.savefig("lunch_fpkms.png")
plt.close(fig)
    
