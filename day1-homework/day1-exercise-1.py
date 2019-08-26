#!/usr/bin/env python3

f = open("SRR072893.sam")
counter = 0

for i, line in enumerate(f):
    fields = line.split("\t")
    if line.startswith("@"):
         continue
    if fields[2] == "*":
         continue
    counter += 1

print(counter)