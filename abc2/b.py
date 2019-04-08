# coding: utf-8
if __name__ == '__main__':
    w = raw_input()
    s = ''
    for i in range(len(w)):
        if w[i] not in 'aiueo':
            s += w[i]
    print s
