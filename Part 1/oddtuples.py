def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    bTup = ()
    for i in range(len(aTup)):
        if i%2 == 0:
            bTup += (aTup[i],)
    return bTup