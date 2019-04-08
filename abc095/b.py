if __name__ == '__main__':
    n,x = map(int,raw_input().split())
    m = []
    for i in range(n):
        m.append(input())
    m.sort()
    count = 0
    for a in m:
        x -= a
        count += 1
    while x > 0:
        x -= m[0]
        if x >= 0:
            count += 1
        else:
            break
    print count
