a , b, c = map(int,raw_input().split())
k = input()
d = max(a,b,c)
e = a + b + c - d
for i in range(k):
    d *= 2
print e + d
