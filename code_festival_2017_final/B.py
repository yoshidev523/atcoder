# -*- coding: utf-8 -*-
S = raw_input()
Q = set()
for i in xrange(len(S)):
for a in Q:
    Q.remove(a)
    for b in Q:
        Q.remove(b)
        for c in Q:
            Q.remove(c)
            for d in Q:
