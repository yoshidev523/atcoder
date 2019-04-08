# coding: utf-8

if __name__ == '__main__':
    deg, dis = map(float, raw_input().split())
    # print deg, dis
    v = dis / 60
    if v < 0.25:
        print 'C 0'
        exit()
    if deg < 112.5:
        degs = 'N'
    elif deg < 337.5:
        degs = 'NNE'
    elif deg < 562.5:
        degs = 'NE'
    elif deg < 787.5:
        degs = 'ENE'
    elif deg < 1012.5:
        degs = 'E'
    elif deg < 1237.5:
        degs = 'ESE'
    elif deg < 1462.5:
        degs = 'SE'
    elif deg < 1687.5:
        degs = 'SSE'
    elif deg < 1912.5:
        degs = 'S'
    elif deg < 2137.5:
        degs = 'SSW'
    elif deg < 2362.5:
        degs = 'SW'
    elif deg < 2587.5:
        degs = 'WSW'
    elif deg < 2812.5:
        degs = 'W'
    elif deg < 3037.5:
        degs = 'WNW'
    elif deg < 3262.5:
        degs = 'NW'
    elif deg < 3487.5:
        degs = 'NNW'
    else:
        degs = 'N'

    if v < 1.55:
        w = 1
    elif v < 3.35:
        w = 2
    elif v < 5.45:
        w = 3
    elif v < 7.95:
        w = 4
    elif v < 10.75:
        w = 5
    elif v < 13.85:
        w = 6
    elif v < 17.15:
        w = 7
    elif v < 20.75:
        w = 8
    elif v < 24.45:
        w = 9
    elif v < 28.45:
        w = 10
    elif v < 32.65:
        w = 11
    else:
        w = 12
    # print v
    print '{0} {1}'.format(degs, w)
