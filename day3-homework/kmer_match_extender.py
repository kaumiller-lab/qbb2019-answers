#!/usr/bin/env python3

from fasta import FASTAReader
import sys
#to run: ./kmer_matcherpy <target.fa> <query.fa> <k>

target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

target_dict = {}
target_name = {}
final_list = []

for ident, sequence in target:
    sequence = sequence.upper()
    target_name[ident] = sequence
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer in target_dict:
            target_dict[kmer].append((ident, i))
        else:
            target_dict[kmer] = [(ident, i)]

for ident, sequence in query:
    sequence = sequence.upper()
    # print("here")
    for j in range(0, len(sequence) - k + 1):
        # print("here")
        kmer = sequence[j:j+k]
        if kmer in target_dict:
            for target_sequence_name, target_start in target_dict[kmer]:
                # print("here")
                query_start = j
                i = target_start
                target_sequence = target_name[target_sequence_name]
                query_length = len(sequence)
                target_length = len(target_sequence)
                extend_right = True
                extended_kmer = kmer 
                # print(target_sequence_name, target_start, query_start, kmer)
    
                while True:
                    if query_length <= (j + k + 1) or target_length <= (i + k + 1):
                        extend_right = False
                    if extend_right:
                        # print(query_length)
                        # print(target_length)
                        # print(j+k+1)
                        # print(i+k+1)
                        if sequence[j + k + 1] == target_sequence[i + k + 1]:
                            i += 1
                            j += 1
                            extended_kmer += sequence[k + j + 1]
                        else:
                            extend_right = False
                    else:
                        final_list.append((len(extended_kmer), target_sequence_name, target_start, query_start, extended_kmer))
                        break
                        
for len_,target_sequence_name, target_start, query_start, extended_kmer in sorted(final_list, reverse = True):
    print(len_,target_sequence_name, target_start, query_start, extended_kmer, sep = "\t")                        

    











