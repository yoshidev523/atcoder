# -*- coding: utf-8 -*-
class Timeblock():
    start_time = 0.0
    end_time = 0.0
    state = ''
if __name__ == '__main__':
    N = input()
    T = map(float, raw_input().split())
    V = map(float, raw_input().split())
    timeblocks = []
    start_time = 0.0
    end_time = 0.0
    now_time = 0.0
    now_state = 'up'
    for index, t in enumerate(T):
        timeblock = Timeblock()
        timeblock.start_time = now_time
        timeblock.state = now_state
        now_time += V[index]
        if T[index] - now_time > 0.0:
            timeblock.end_time = now_time
            timeblocks.append(timeblock)
        else:
            print
    timeblock = []
