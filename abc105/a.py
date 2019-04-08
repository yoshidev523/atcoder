if __name__ == '__main__':
    n,k = map(int,raw_input().split())
    if n % k == 0:
        print 0
    else:
        print 1
