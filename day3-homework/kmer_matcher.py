#!/usr/bin/env python3

from fasta import FASTAReader
import sys
#to run: ./kmer_matcherpy <target.fa> <query.fa> <k>

target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

target_dict = {}

for ident, sequence in target:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in target_dict:
            target_dict[kmer].append((ident, i))
        else:
            target_dict[kmer] = [(ident, i)]

for ident, sequence in query:
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in target_dict:
            for target_sequence_name, target_start in target_dict[kmer]:
                query_start = i
                
                print(target_sequence_name, target_start, query_start, kmer)
          




