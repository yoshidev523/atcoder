# coding: utf-8
if __name__ == '__main__':
    a = [1]
    b = 6
    while b <= 100000:
        a.append(b)
        b *= 6
    b = 9
    while b <= 100000:
        a.append(b)
        b *= 9
    a.sort()
    index = len(a) - 1
    n = input()
    count = 0
    while n > 0 :
        if n - a[index] >= 0:
            count += 1
            print a[index]
            n -= a[index]
        else:
            index -= 1
    print count
