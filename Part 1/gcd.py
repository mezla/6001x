def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < b:
        i = a
    elif a > b:
        i = b
    else:
        return a    
    while i > 1:
        if a % i == 0 and b % i == 0: return  i
        i -= 1
        if i == 1: return 1

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0: return a
    return gcdRecur(b, a % b)
