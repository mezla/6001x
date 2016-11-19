def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    if not s1 or not s2:
        if not s1:
            return s2
        else:
            return s1
    
    lace = ''
    count = 0
    for char in s1:
        try:
            lace += s1[count] + s2[count]
        except ValueError:
            break
        else:
            count += 1
    
    if count < len(s1):
        lace += s1[count:]
    elif count < len(s2):
        lace += s2[count:]
    
    return lace