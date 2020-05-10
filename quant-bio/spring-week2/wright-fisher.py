#!/usr/bin/env python3

import sys
import numpy as np
import scipy
import matplotlib.pyplot as plt

#for generating histogram (part I)
# n = 100
# p = 0.5
# sim = 1000
#
# hist = []
# num_alleles = 2 * n
# for s in range(sim):
#     fix = False
#     nextgenalleles = p * num_alleles
#     gen_count = 0
#     while fix == False:
#         gen_count += 1
#         freq = nextgenalleles / num_alleles
#         nextgenalleles= np.random.binomial(num_alleles, freq)
#         fix = nextgenalleles == 0 or nextgenalleles == num_alleles
#
#     hist.append(gen_count)
#
# fig, ax = plt.subplots()
# ax.hist(hist)
# fig.savefig("Histogram.png")
# plt.tight_layout()
# plt.close(fig)

#Plots Fixation time vs N (part II)
# n=200
#
# def fixation(n, p):
#     fixation_time = 0
#     next_gen_alleles = np.random.binomial(n,p)
#     p = next_gen_alleles/n
#     while next_gen_alleles !=0 and next_gen_alleles !=n:
#         next_gen_alleles = np.random.binomial(n,p)
#         p = next_gen_alleles/n
#         fixation_time += 1
#     return fixation_time
# trial = fixation(n, .5)
#
# pop=[100, 1000, 5000, 10000, 50000, 100000, 500000]
# #print(trial)
#
# avg_pops=[]
# pop_num=[]
#
# for n in pop:
#     pop_num.append(n)
#     multi_trials =[]
#     for j in range(10):
#
#         i=fixation(n, .5)
#         multi_trials.append(i)
#     avg_trials_per_popsize = sum(multi_trials)/len(multi_trials)
#     avg_pops.append(avg_trials_per_popsize)
#
# fig, ax = plt.subplots()
# plt.plot(pop_num, avg_pops)
# ax.set_xlabel("pop size",fontsize=16)
# ax.set_ylabel("generation to fixation",fontsize=16)
# ax.set_yscale("log")
# plt.tight_layout()
# fig.savefig("fix_vs_N.png")
# plt.close(fig)



#plots allele frequency vs number of generations to fix (part III)
def fixation(n, p):
    fixation_time = 0
    next_gen_alleles = np.random.binomial(n,p)
    p = next_gen_alleles/n
    while next_gen_alleles !=0 and next_gen_alleles !=n:
        next_gen_alleles = np.random.binomial(n,p)
        p = next_gen_alleles/n
        fixation_time += 1
    return fixation_time

multi_trials =[]
p_freq=[]
avg_pops=[]
std_pops=[]
p=.01
for i in range(99):
    p_freq.append(p)
    for j in range(1000):
        i=fixation(200, p)
        multi_trials.append(i)
    avg_trials_per_pfreq = sum(multi_trials)/len(multi_trials)
    std_trials_per_pfreq = np.std(multi_trials)
    avg_pops.append(avg_trials_per_pfreq)
    std_pops.append(std_trials_per_pfreq)
    p+=.01


fig, ax = plt.subplots()
plt.errorbar(p_freq, avg_pops,yerr=std_pops)
ax.set_xlabel("allele freq",fontsize=16)
ax.set_ylabel("generation to fixation",fontsize=16)
plt.tight_layout()
fig.savefig("freq_vs_gens.png")
plt.close(fig)



#plots selection coefficient over time (part IV)

# def fixation(n, p, s):
#     fixation_time = 0
#     p = (p+(p*s))/(1+(p*s))
#     next_gen_alleles = np.random.binomial(n,p)
#     while next_gen_alleles !=0 and next_gen_alleles !=n:
#         next_gen_alleles = np.random.binomial(n,p)
#         p = next_gen_alleles/n
#         p = (p+(p*s))/(1+(p*s))
#         fixation_time += 1
#     return fixation_time
#
# multi_trials=[]
# avg_pops=[]
# std_pops=[]
# sel_coef=[]
# s=.01
# for i in range(99):
#     sel_coef.append(s)
#     for j in range(100):
#         i=fixation(200, .5, s)
#         multi_trials.append(i)
#     avg_trials_per_sel_coef = sum(multi_trials)/len(multi_trials)
#     std_trials_per_sel_coef = np.std(multi_trials)
#     avg_pops.append(avg_trials_per_sel_coef)
#     std_pops.append(std_trials_per_sel_coef)
#     s+=.01
#
#
# fig, ax = plt.subplots()
# plt.errorbar(sel_coef, avg_pops,yerr=std_pops)
# ax.set_xlabel("selection coefficient",fontsize=16)
# ax.set_ylabel("generation to fixation",fontsize=16)
# plt.tight_layout()
# fig.savefig("Sel_over_time")
# plt.close(fig)
#
