#!/usr/bin/env python3

from fasta import FASTAReader
import sys
#to run: ./kmer_matcherpy <target.fa> <query.fa> <k>

target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

target_dict = {}
target_name = {}
final_dict = {}

for ident, sequence in target:
    sequence = sequence.upper()
    target_name[ident] = target_sequence
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in target_dict:
            target_dict[kmer].append((ident, i))
        else:
            target_dict[kmer] = [(ident, i)]

for ident, sequence in query:
    sequence = sequence.upper()
    for j in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in target_dict:
            for target_sequence_name, target_start in target_dict[kmer]:
                query_start = j
                
                target_sequence = target_name[ident]
                query_length = len(sequence)
                target_length = len(target_sequence)
                extend_right = True
                extended_kmer = kmer 
                print(target_sequence_name, target_start, query_start, kmer)
    
                while True:
                    if extend_right:
                        if sequence[j + k + 1] == target_sequence[j + k + 1]:
                            i == 1
                            j == 1
                            extended_kmer += sequence[i + j +1]
                        else:
                            extend_right = False
                    else:
                        break #this is where I would add the extension to ny dictionary
                        
                    if query_length == (j + k) or target_length == (j + k):
                        extended_right = False











