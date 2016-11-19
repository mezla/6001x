s = 'azcbobobegghakl'

alpha = 'abcdefghijklmnopqrstuvwxyz'
longstr = ''
tempstr = ''
index = 0
start = 0
end = len(alpha)
count = 0

i = 0

while True:
    i += 1
    for c in s[start:end]:
        count += 1
        if alpha.index(c) >= index:
            index = alpha.index(c)
            tempstr += c
        else:
            index = alpha.index(c)
            start = count
            potential_str = tempstr
            tempstr = c
            if len(potential_str) > len(longstr):
                longstr = potential_str
            break
    if i == end: break

print "Longest substring in alphabetical order is: " + longstr