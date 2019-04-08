# -*- coding: utf-8 -*-

if __name__ == '__main__':
    N = raw_input()
    if int(N[0])+int(N[1])+int(N[2])+int(N[3]) == 7:
        print('{0}+{1}+{2}+{3}=7'.format(N[0],N[1],N[2],N[3]))
    elif int(N[0])+int(N[1])+int(N[2])-int(N[3]) == 7:
        print('{0}+{1}+{2}-{3}=7'.format(N[0],N[1],N[2],N[3]))
    elif int(N[0])+int(N[1])-int(N[2])+int(N[3]) == 7:
        print('{0}+{1}-{2}+{3}=7'.format(N[0],N[1],N[2],N[3]))
    elif int(N[0])+int(N[1])-int(N[2])-int(N[3]) == 7:
        print('{0}+{1}-{2}-{3}=7'.format(N[0],N[1],N[2],N[3]))
    elif int(N[0])-int(N[1])+int(N[2])+int(N[3]) == 7:
        print('{0}-{1}+{2}+{3}=7'.format(N[0],N[1],N[2],N[3]))
    elif int(N[0])-int(N[1])+int(N[2])-int(N[3]) == 7:
        print('{0}-{1}+{2}-{3}=7'.format(N[0],N[1],N[2],N[3]))
    elif int(N[0])-int(N[1])-int(N[2])+int(N[3]) == 7:
        print('{0}-{1}-{2}+{3}=7'.format(N[0],N[1],N[2],N[3]))
    elif int(N[0])-int(N[1])-int(N[2])-int(N[3]) == 7:
        print('{0}-{1}-{2}-{3}=7'.format(N[0],N[1],N[2],N[3]))
