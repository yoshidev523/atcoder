import re
import sys
import itertools

if __name__ == '__main__':
    N = input()
    S = list()
    c = 0
    d = {'M':0,'A':0,'R':0,'C':0,'H':0}
    for i in xrange(N):
        a = raw_input()[0]
        if a in d.keys():
            d[a] += 1
    if d['M'] > 0 and d['A'] > 0 and d['R'] > 0:
        c += d['M']*d['A']*d['R']
    if d['M'] > 0 and d['A'] > 0 and d['C'] > 0:
        c += d['M']*d['A']*d['C']
    if d['M'] > 0 and d['A'] > 0 and d['H'] > 0:
        c += d['M']*d['A']*d['H']
    if d['M'] > 0 and d['R'] > 0 and d['C'] > 0:
        c += d['M']*d['R']*d['C']
    if d['M'] > 0 and d['R'] > 0 and d['H'] > 0:
        c += d['M']*d['R']*d['H']
    if d['M'] > 0 and d['C'] > 0 and d['H'] > 0:
        c += d['M']*d['C']*d['H']
    if d['A'] > 0 and d['R'] > 0 and d['C'] > 0:
        c += d['A']*d['R']*d['C']
    if d['A'] > 0 and d['R'] > 0 and d['H'] > 0:
        c += d['A']*d['R']*d['H']
    if d['A'] > 0 and d['C'] > 0 and d['H'] > 0:
        c += d['A']*d['C']*d['H']
    if d['R'] > 0 and d['C'] > 0 and d['H'] > 0:
        c += d['R']*d['C']*d['H']
    print c
