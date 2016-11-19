def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    elif aStr.rindex(aStr[-1]) == 0:
        if char == aStr:
            return True
        else:
            return False
    elif char == aStr[len(aStr)/2]:
        return True
    else:
        if char < aStr[len(aStr)/2]:
            print aStr[:len(aStr)/2]
            return isIn(char, aStr[:len(aStr)/2])
        else:
            print aStr[len(aStr)/2:]
            return isIn(char, aStr[len(aStr)/2:])