if __name__ == '__main__':
    n = input()
    a = 0
    b = 0
    while(a < 15):
        b = 0
        while(b < 26):
            if(7 * a + 4 * b == n):
                print 'Yes'
                quit()
            b += 1
        a += 1
    print 'No'
