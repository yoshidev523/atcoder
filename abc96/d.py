prime = [2]
for i in range(10000):
    if i == 0 or i == 1 or i == 2:
        continue
    a = True
    for p in prime:
        if i % p == 0:
            a = False
            break
    if a == True:
        prime.append(i)
n = input()
a = []
for p in prime:
    if p % 5 == 1:
        a.append(p)
        if len(a) == n:
            break
b = ''
for c in a:
    b += str(c) + ' '
b = b[:-1]
print b
