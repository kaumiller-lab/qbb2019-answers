#!/usr/bin/env python3

#map_file is the fly entry Uniprot file (fly.txt)
#out_file is the file you want to print to

#to run the script: input ./parse-mapping.py <map_file> <out_file> in Unix

#my version of fly.txt was made by me copying and pasting the text into a new doc. I accidentally hit space prior to pasting so every line starts with a space. I had to use .strip to account for this

import sys

map_file = open(sys.argv[1],"r")
out_file = open(sys.argv[2],"w")

start_map_test = False

for line in map_file:
    if line.strip().startswith("_"):
        start_map_test = True
    else:
        if start_map_test:
            if line.strip().startswith("-"):
                start_map_test = False
                continue
            fields = line.strip().split()
            if len(fields) != 4 or "DROME" not in line:
                continue
            out_file.write("%s\t%s\n" %(fields[3], fields[2]))
map_file.close()
out_file.close()


        