#!/usr/bin/env python3

import sys
import statistics as stats

class FASTAReader(object):
    
    def __init__(self, fh):
        self.fh = fh
        self.last_ident = None
        self.eof = False
    
    def next(self):
        
        if self.eof:
            return None, None
        elif self.last_ident is None:
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\n")
        else:
            ident = self.last_ident
            
        sequences = []
        while True:
            line = self.fh.readline()
            if line == "":
                self.eof = True
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n")
                break
            else:
                sequences.append(line.strip())
        
        sequence = "".join(sequences)
        return ident, sequence
        
for i in range(1,len(sys.argv)):
    contig_file = open(sys.argv[i])
    contig_reader = FASTAReader(contig_file)
    
    contig_counter = 0
    contig_lengths = []
    
    while True:
        ident, sequence = contig_reader.next()
        if not ident is None:
            contig_counter += 1
            contig_lengths.append(len(sequence))
        else:
            break
            
    min_contig = min(contig_lengths)
    max_contig = max(contig_lengths)
    ave_contig = stats.mean(contig_lengths)
    
    contig_lengths.sort()
    print(min_contig)
    print(max_contig)
    print(ave_contig)
    
def N50(counter):
    middle_point = sum(contig_lengths) / 2

    counter = 0
    for contig_length in contig_lengths:
        counter += contig_length
        if counter >= middle_point:
            n50 = contig_length
            
      
