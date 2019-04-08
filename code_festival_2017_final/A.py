# -*- coding: utf-8 -*-
def update(A,keta,count):
    for k in xrange(keta):
        if count > (2**(keta - k - 1)):
            A[2*k] = 'A'
            count -= 2**(keta - k - 1)
    return A

S = raw_input()
if len(S) > 9:
    print 'NO'
elif S == 'AKIHABARA':
    print 'YES'
else:
    count = 0
    while(count < 2**(len(S)+1)):
        A = ['' for i in xrange(len(S)*2+1)]
        for i in xrange(len(S)):
            A[2*i+1] = S[i]
        A = update(A,len(S)+1,count)
        tmp = ''
        for a in A:
            tmp += a
        #print tmp
        if tmp == 'AKIHABARA':
            print 'YES'
            quit(0)
        count += 1
        #print count
    print 'NO'
