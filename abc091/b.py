if __name__ == '__main__':
    n = input()
    s = {}
    for i in range(n):
        a = raw_input()
        if a not in s.keys():
            s[a] = 1
        else:
            s[a] += 1
    m = input()
    t = {}
    for i in range(m):
        a = raw_input()
        if a not in t.keys():
            t[a] = 1
        else:
            t[a] += 1
    m = 0
    for a in s.keys():
        if a in t.keys():
            m = max(m, s[a] - t[a])
        else:
            m = max(m, s[a])
    print m
