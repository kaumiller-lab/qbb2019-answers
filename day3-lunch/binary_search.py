#!/usr/bin/env python3

#genome is a .gtf file
#search_pos is the nucleotide you want to conduct a binary search for

#to run: ./<genome> > <output file>

import sys
import numpy

genome = open(sys.argv[1])

gene_list = []
search_pos = 21378950

#sorts protein-coding genes on chromosome 3R in gene_list
#gene_list stores the start and end points of each gene as well as the name
for line in genome:
    if line.startswith("#!"):
        continue
        
    fields = line.rstrip("\n").split()
    chrom = fields[0]
    seq_type = fields[2]
    seq_start = fields[3]
    seq_end = fields[4]
    gene_name = fields[13]
    
    if chrom != '3R' or seq_type != 'gene' or 'gene_biotype "protein_coding"' not in line:
        continue
        
    gene_list.append((int(seq_start), int(seq_end), gene_name))
        
#binary search for gene closest to search_pos
    
lo = 0
hi = len(gene_list)-1
mid = 0
iterations = 0

while (lo <= hi):
    if hi - lo == 2:
        first_start = abs(gene_list[0 + lo][0] - search_pos)
        first_end = abs(gene_list[0 + lo][1] - search_pos)
        second_start = abs(gene_list[1 + lo][0] - search_pos)
        second_end = abs(gene_list[1 + lo][1] - search_pos)
        first = min(first_start, first_end)
        second = min(second_start, second_end)
        if first < second:
            print(gene_list[0 + lo][2])
        else:
            print(gene_list[1 +lo][2])
        break
        
    mid = int((hi + lo) / 2)
    iterations = iterations + 1
    if (search_pos < gene_list[mid][0]):
        hi = mid
    elif (search_pos > gene_list[mid][1]):
        lo = mid
    else:
        break
print(gene_list[mid], iterations)

    
        
    
    
        