if __name__ == '__main__':
    n,m = map(int, raw_input().split())
    a = map(int, raw_input().split())
    c = 0
    l = 1
    while(True):
        r = l
        while(True):
            b = a[l-1:r]
            print b
            if sum(b) % m == 0:
                c += 1
            r += 1
            if r > n:
                break
        l += 1
        if l > n:
            break
    print c
