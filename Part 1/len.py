def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    count = 0
    for s in aStr:
        if s.isalpha(): count += 1
    return count

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    global count
    try:
        count
    except NameError:
        count = 0
 
    if aStr == '':
        return 0
    elif aStr.rindex(aStr[-1]) == 0:
        res = count
        count = 0
        return res + 1
    else:
        count += 1
        return lenRecur(aStr[1:])