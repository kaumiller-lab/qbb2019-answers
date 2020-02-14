#!/usr/bin/env python3


from __future__ import print_function, division
import numpy as np
import sys
# #              A     C     G     T
# sigma = [ [   91, -114,  -31, -123 ],
#           [ -114,  100, -125,  -31 ],
#           [  -31, -125,  100, -114 ],
#           [ -123,  -31, -114,   91 ] ]
#
#
# gap = 300

seq1 = open(sys.argv[1])
seq2 = open(sys.argv[2])

pt ={'match': 300, 'mismatch': -300, 'gap': -300}
def mch(alpha, beta):
    if alpha == beta:
        return pt['match']
    elif alpha == '-' or beta == '-':
        return pt['gap']
    else:
        return pt['mismatch']
def needle(s1, s2):
    m, n = len(s1), len(s2)
    score = np.zeros((m+1, n+1))
    #Initialization
    for i in range(m+1):
        score[i][0] = pt['gap'] * i
    for j in range(n+1):
        score[0][j] = pt['gap'] * j
    #Fill
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = score[i-1][j-1] + mch(s1[i-1], s2[j-1])
            delete = score[i-1][j] + pt['gap']
            insert = score[i][j-1] + pt['gap']
            score[i][j] = max(diag, delete, insert)
    print('score matrix = \n%s\n' % score)
    align1, align2 = '', ''
    i,j = m,n
    #Traceback
    while i > 0 and j > 0:
        current_score = score[i][j]
        diagonal = score[i-1][j-1]
        left = score[i][j-1]
        up = score[i-1][j]
        print('current_score: ',current_score)
        print('diagonal:',diagonal)
        print('left:',left)
        print('up:',up)
        if current_score == diagonal + mch(s1[i-1], s2[j-1]):
            print('diag')
            a1,a2 = s1[i-1],s2[j-1]
            i,j = i-1,j-1
        elif current_score == up + pt['gap']:
            print('up')
            a1,a2 = s1[i-1],'-'
            i -= 1
        elif current_score == left + pt['gap']:
            print('left')
            a1,a2 = '-',s2[j-1]
            j -= 1
        print('%s ---> a1 = %s\t a2 = %s\n' % ('Add',a1,a2))
        align1 += a1
        align2 += a2
    while i > 0:
        a1,a2 = s1[i-1],'-'
        print('%s ---> a1 = %s\t a2 = %s\n' % ('Add',a1,a2))
        align1 += a1
        align2 += a2
        i -= 1
    while j > 0:
        a1,a2 = '-',s2[j-1]
        print('%s --> a1 = %s\t a2 = %s\n' % ('Add',a1,a2))
        align1 += a1
        align2 += a2
        j -= 1
    align1 = align1[::-1]
    align2 = align2[::-1]
    seqN = len(align1)
    sym = ''
    seq_score = 0
    ident = 0
    for i in range(seqN):
        a1 = align1[i]
        a2 = align2[i]
        if a1 == a2:
            sym += a1
            ident += 1
            seq_score += mch(a1, a2)
        else:
            seq_score += mch(a1, a2)
            sym += ' '
    ident = ident/seqN * 100
    print('Identity = %2.1f percent' % ident)
    print('Score = %d\n'% seq_score)
    print(align1)
    print(sym)
    print(align2)
if __name__ == '__main__':
    needle(str(seq1),str(seq2))