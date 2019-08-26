#!/usr/bin/env python3

f = open("SRR072893.sam")
counter = 0

for i, line in enumerate(f):
    counter += 1

print(counter)