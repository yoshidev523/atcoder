import sys
import re
if __name__ == '__main__':
    n = input()
    A = map(int, raw_input().split())
    A.append(0)
    now = A[0]
    S = 0
    for a,index in enumerate(A):
        if index < len(A) - 1:
            S += abs(A[index] - A[index+1])
    
    for remove in A:
        for a in A:
            if a == remove:
                continue
            else:
                now =
