def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n <= 5: return False
        
    c = n/20
    b = n/9
    a = n/6
    
    if n%20 == 0 or n%9 == 0 or n%6 == 0: return True
    
    while True:
                
        if n%20 == 0:
            return True
        elif (n%20) % 9 == 0:
            return True
        elif (n%20) % 6 == 0:
            return True

        if n/20 > 0:
            c = n/20 - 1
            n = n - 20
        
        if n%9 == 0:
            return True
        elif (n%9) % 6 == 0:
            return True
        
        if n/9 > 0:
            b = n/9 - 1
            n = n - 9
        
        if n%6 == 0:
            return True
        
        if n/6 > 0:
            a = n/6 -1
            n = n - 6
        
        print a
        print b
        print c
        print n
        
        if c <= 0 and b <= 0 and a <= 0: return False