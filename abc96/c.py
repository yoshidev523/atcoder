h,w = map(int,raw_input().split())
s = []
a = True
for i in range(h):
    s.append(raw_input())
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if i - 1 >= 0 and s[i-1][j] == '#':
                continue
            if i + 1 < h and s[i+1][j] == "#":
                continue
            if j - 1 >= 0 and s[i][j-1] == '#':
                continue
            if j + 1 < w and s[i][j+1] == '#':
                continue
            a = False
if a == True:
    print 'Yes'
else:
    print 'No'                
