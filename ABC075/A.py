# -*- coding: utf-8 -*-
A,B,C = map(int, raw_input().split())
if A == B:
    print(C)
if A == C:
    print(B)
if B == C:
    print(A)
