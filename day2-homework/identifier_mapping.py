#!/usr/bin/env python3

import sys

#map_file is the output text file from the first excersize (fly-parsed.out)

#c_tab_file is any .ctab file from ../results/stringtie/

#out_file is the file you want to print to

#not_found_input is the command used to determine what the script does when 
#confronted with gene identities from c_tab_file not found in mao_file.
    #if you want these values to be left blank, input "ignore" as not_found_input. 
    #input "default" to have these values set to "N/A"

#to run the script, input ./identifier_mapping.py <map_file> <c_tab_file> <out_file> <not_found_input>

map_file = open(sys.argv[1],"r")
c_tab_file = open(sys.argv[2],"r")
out_file = open(sys.argv[3],"w")
not_found_input = sys.argv[4] 

result = {}

for line in map_file:
    columns = line.rstrip("\n").split("\t")
    flybase_id = columns[0]
    uniprot_id = columns[1]
    result[flybase_id] = uniprot_id
    
for line in c_tab_file:
    columns2 = line.rstrip("\n").split("\t")
    gene_id = columns2[8]
    
    if gene_id in result:
        out_file.write("%s\t%s\n" %(line.rstrip(), result[gene_id]))
    elif sys.argv[4] == "ignore":
        continue
    elif sys.argv[4] == "default":
        out_file.write("%s\t%s\n" %(line.rstrip(), "N/A"))
    
    
map_file.close
c_tab_file.close
out_file.close