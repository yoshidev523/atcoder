# -*- coding: utf-8 -*-
if __name__ == '__main__':
    N = input()
    K = input()
    result = 2**N
    for i in range(N):
        result = min(result, 2**i + K * (N - i))
    print result
