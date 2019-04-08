# -*- coding: utf-8 -*-
if __name__ == '__main__':
    SS = raw_input()
    T = raw_input()
    S = ""
    start_index = -1
    end_index = -1
    t_index = 0
    state = 0
    if len(T) > len(SS):
        S = 'UNRESTORABLE'
    else:
        for index in range(len(SS) - len(T), -1, -1):
            for current_index in range(index, index + len(T)):
                if SS[current_index] == '?' or SS[current_index] == T[t_index]:
                    t_index += 1
                    if t_index == len(T):
                        start_index = index
                        end_index = current_index
                        state = 1
                        break
                else:
                    t_index = 0
                    break
            if state == 1:
                break
        if start_index == -1:
            S = 'UNRESTORABLE'
        else:
            for index, s in enumerate(SS):
                if index >= start_index and index <= end_index:
                    S += T[index - start_index]
                elif s == '?':
                    S += 'a'
                else:
                    S += s
    print S
