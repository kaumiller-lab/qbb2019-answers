#!/usr/bin/env python=3

import os
import matplotlib.pyplot as plt
import numpy as np
#os.listdir on os.gitcwb
colors = ['#ffe119', '#469990']
for file_name in os.listdir (os.getcwd()):
    if file_name.endswith('.qassoc'):
        pval_by_chr = {}
        qassoc_file = open(file_name)
        for i, line in enumerate(qassoc_file):
            if i == 0:
                continue
            fields = line.rstrip("\n").split()
            chromo = fields[0]
            p_val = fields[-1]
            if p_val == 'NA':
                continue
            pval_by_chr.setdefault(chromo,[])
            pval_by_chr[chromo].append(-1*np.log10(float(p_val)))
        fig, ax = plt.subplots()
        plt.tick_params(axis= "x", which= "both", bottom=False, top=False, labelbottom=False)
        previous_points = 0
        for i, chromo in enumerate(pval_by_chr):
            ax.scatter([x+previous_points for x in range(len(pval_by_chr[chromo]))], pval_by_chr[chromo], color = colors[i%2])
            previous_points += len(pval_by_chr[chromo]) 
        ax.set_xlabel("chromosome")
        ax.set_ylabel("Frequency")
        ax.set_title("file_name")
        fig.savefig("phenoassoc.qassoc"+'.png')
        plt.close()





