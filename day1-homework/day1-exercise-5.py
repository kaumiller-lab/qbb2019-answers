#!/usr/bin/env python3

f = open("SRR072893.sam")
counter = 0
col_5 = 0

for i, line in enumerate(f):
    fields = line.split("\t")
    if line.startswith("@"):
         continue
    if fields[2] == "*":
         continue
    counter += 1
    col_5 += float(fields[4])
    
mapq = col_5 / counter

    
print(mapq)