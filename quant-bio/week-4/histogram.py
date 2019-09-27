#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

BYxRM = open(sys.argv[1])

freq = []

for line in BYxRM:
    if line.startswith("#"):
        continue
        
    fields = line.rstrip("\t").split()
    column = fields[7]
    allele_freq = column.split("=")[1]
    
    if "," in allele_freq:
        allele_freq = float(allele_freq.split(",")[0])
        
    else:
        allele_freq = float(allele_freq)
        
    freq.append(allele_freq)

    
fig,ax = plt.subplots()
ax.hist(freq, bins=1000, density = True)
ax.set_xlabel("Allele")
ax.set_ylabel("Frequency")
ax.set_title("Allele Frequencies")
fig.savefig("afs.png")
plt.close()


