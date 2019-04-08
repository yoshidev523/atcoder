if __name__ == '__main__':
    N, M = map(int , raw_input().split())
    d = 0
    for i in range(M):
        for j in range(N):
            c = 1
            if i+1 < M and j+1 < N:
                c += 1
            if i+1 < M:
                c += 1
            if i+1 < M and j-1 >= 0:
                c += 1
            if j+1 < N:
                c += 1
            if j-1 >= 0:
                c += 1
            if i-1 >= 0 and j+1 < N:
                c += 1
            if i-1 >= 0:
                c += 1
            if i-1 >= 0 and j-1 >= 0:
                c += 1
            if c % 2 == 1:
                d += 1
    print d
