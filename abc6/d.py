# coding: utf-8

import bisect
a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 4

insert_index = bisect.bisect_left(a, x)

print insert_index

N = input()
C = [input() for i in range(N)]
