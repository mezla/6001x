def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    x = 1
    while True:
        if n%20 == 0:
            return True
        elif n%9 == 0:
            return True
        elif n%6 == 0:
            return True
        else:
            if (n%20)%9 == 0:
                return True
            elif (n%20)%6 == 0:
                return True
            else:
                if (n%9)%6 == 0:
                    return True
                else:
                    return False