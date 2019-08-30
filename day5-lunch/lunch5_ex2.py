#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt

ctab = sys.argv[1]

for i, line in enumerate(open(ctab)):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    
    if fields[2] == "+":
        prmtr_l = int(fields[3]) - 500
        prmtr_r = int(fields[3]) + 500
        
    else:
        prmtr_l = int(fields[4]) - 500
        prmtr_r = int(fields[4]) + 500
        
    if prmtr_l < 0:
        prmtr_l = 0
        
    print(fields[1] , str(prmtr_l), str(prmtr_r), fields[5], sep = "\t")
        
        


        
        
    
  
    
    