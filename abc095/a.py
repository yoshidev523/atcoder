if __name__ == '__main__':
    S = raw_input()
    count = 0
    for s in S:
        if s == 'o':
            count += 1
    print 700 + count * 100
