if __name__ == '__main__':
    A, B = raw_input().split()
    c = 0
    while int(A) <= int(B):
        if A[0] == A[4] and A[1] == A[3]:
            c += 1
        A = str(int(A)+1)
    print c
