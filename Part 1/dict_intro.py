animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

animals['e'] = ['donkeya']
animals['e'].append('dogb')
animals['e'].append('dingoc')

test = {}

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for key in aDict:
        count += len(aDict[key])
    return count

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    size = []
    for key in aDict:
        size.append(len(aDict[key]))
    size.sort()
    
    for key in aDict:
        if len(aDict[key]) == size[-1]:
            return key
            break