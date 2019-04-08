if __name__ == '__main__':
    n = input()
    a = '0'
    base = 1
    if n > 0:
        while(n > 0):
            a = a + str((n % (-2)) * base)
            print '{}'.format((n % (-2)) * base)
            n = n // -2
            base *= 10
    print a
