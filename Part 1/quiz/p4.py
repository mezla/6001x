def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if x == 0:
        return float('nan')
    power = 1
    while True:
        if b**power > x:
            return power-1
        else:
            power += 1