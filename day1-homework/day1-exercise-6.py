#!/usr/bin/env python3

f = open("SRR072893.sam")
counter = 0

for i, line in enumerate(f):
    fields = line.split("\t")
    if line.startswith("@"):
        continue
    if fields[2] == "*":
        continue
    if fields[2] != "2L":
        continue
    if int(fields[3]) <= 20000 and int(fields[3]) >= 10000:
        counter += 1
    
print(counter)