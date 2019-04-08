# coding: utf-8
import random
import sys
import time

in_count = 0.0
out_count = 0.0
while True:
    x = random.random()
    y = random.random()
    if x*x + y*y <= 1.0:
        in_count += 1.0
    else:
        out_count += 1.0
    # print 'count: {}'.format(in_count+out_count)
    # print 'pi: {}'.format(in_count / (in_count + out_count) * 4.0)
    sys.stdout.write("\rcount:{0}, pi:{1}".format(int(in_count+out_count), in_count / (in_count + out_count) * 4.0))
    # sys.stdout.write("\rpi:{}".format(in_count / (in_count + out_count) * 4.0))
    sys.stdout.flush()
    time.sleep(0.01)
