#!/usr/bin/env python3

"""
Usage: ./homework_ex1.py <metadata.csv> <ctab_dir>

    <ctab_dir> e.g. ~/qbb2019-answers/results/stringtie

create all.asv with FPKMs

    t_name. gene_name, sample1, ..., samplen
"""

import sys
import os
import pandas as pd

metadata = sys.argv[1]
ctab_dir = sys.argv[2]

fpkms = {}
for i, line in enumerate(open(metadata)):
    if i == 0:
        continue
    fields = line.strip("\n").split(",")
    srr_id = fields[0]
    srr_sex = fields[1]
    srr_time = fields[2]
    srr_join = srr_sex + "_" + srr_time
    ctab_path = os.path.join(ctab_dir, srr_id, "t_data.ctab")
    
    df = pd.read_csv(ctab_path, sep="\t", index_col = "t_name")
    fpkms["gene_name"] = df.loc[:, "gene_name"]
    fpkms[srr_join] = df.loc[:,"FPKM"]
    
df_fpkms = pd.DataFrame(fpkms)

pd.DataFrame.to_csv(df_fpkms, "all.csv")    