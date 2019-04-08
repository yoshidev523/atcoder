# coding: utf-8

# 4
# 1148-1210
# 1323-1401
# 1106-1123
# 1129-1203
from datetime import datetime
if __name__ == '__main__':
    n = input()
    p = []
    q = []
    for i in range(n):
        a = map(int, raw_input().split('-'))
        p.append(a)
    p.sort()

    for i in range(n):
        p[i][0] = p[i][0] - p[i][0] % 5
        if p[i][1] % 5 != 0:
            p[i][1] = p[i][1] + (5 - p[i][1] % 5)
            # print p[i][1]
            if (p[i][1] - 60) % 100 == 0:
                p[i][1] += 40
                # print p[i][1]
    # print p
    for i in range(n - 1):
        # for j in range(i ,n):
        if p[i][1] - p[i+1][0] >= 0:
            if p[i+1][1] - p[i][1] >= 0:
                p[i+1] = [p[i][0], p[i+1][1]]
            else:
                p[i+1] = p[i]
        else:
            q.append(p[i])
    q.append(p[n-1])

    for a in q:
        print '{0}-{1}'.format(str(a[0]).zfill(4), str(a[1]).zfill(4))
    # print q
