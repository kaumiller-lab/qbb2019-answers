#!/usr/bin/env python3


import sys 
import matplotlib.pyplot as plt

dp = []
qual_score = []
frequency = []
summary_dict = {}
for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    field = line.rstrip("\n").split("\t")
    ref = field[3]
    alt = field[4]
    qual = int(float(field[5]))
    info = field[7]
    dp_split = info.split(";")[7]
    dp.append(dp_split.split("=")[1])
    qual_score.append(qual)
    
    frequency_split = info.split(";")[3]
    frequency.append(frequency_split.split("=")[1])
    
    summary_split = info.split(";")[41]
    summary_value = summary_split.split("=")[1]
    summary_score = summary_value.split("|")[1]
    if summary_score in summary_dict:
        summary_dict[summary_score] += 1
    else:
        summary_dict[summary_score] = 1

fig, ax = plt.subplots(4)
ax[0].hist(dp, bins=100)
ax[1].hist(qual, bins=100, range=[0,5000])
ax[2].hist(frequency, bins=100)

plt.bar(range(len(summary_dict)), list(summary_dict.values()), align = 'center')
plt.xticks(range(len(summary_dict)), list(summary_dict.keys()), rotation = 'vertical', size = 5)

ax[0].set_xlabel("Variants")
ax[0].set_ylabel("Depth Position")

ax[1].set_xlabel("Variants")
ax[1].set_ylabel("Quality")

ax[2].set_xlabel("Variants")
ax[2].set_ylabel("Allele Frequency")

ax[3].set_xlabel("Variants")
ax[3].set_ylabel("Summary of predicted effects")


ax[0].set_title("Graph1 Read Position")
ax[1].set_title("Graph2 Quality")
ax[2].set_title("Graph3 Allele Frequency")
ax[3].set_title("Graph4 Summary of predicted effects")
plt.tight_layout(rect=[1, 1, 1, 1])

fig.savefig("plots.png")
plt.close(fig)