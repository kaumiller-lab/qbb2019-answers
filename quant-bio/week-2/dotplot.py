#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

start = []
end = []

for line in open(sys.argv[1]):
    if "#" in line:
        continue
    col = line.rstrip("/n").split()
    if col[7] != "-":
        start.append((int(col[4])-int(col[3])))
        end.append(int(col[8]))

fig,ax = plt.subplots()

ax.plot()
fig.suptitle("Genome Assembly")
ax.scatter(x=start, y=end, alpha=0.4)
ax.set_xlabel("K21 Contigs Length (bp)")
ax.set_ylabel("Reference Length (bp)")
fig.savefig("K55scaffolds.png")
plt.close(fig)

plt.plot()