s = 'bobobobobobobobobobobobob'

count = 0
bob = 'bob'
end = len(s)

if s.find(bob) != -1:
    pos = s.find(bob)
    count += 1
    while True:
        if s.find(bob,pos+2,end) != -1:
            pos = s.find(bob,pos+2,end)
            count += 1
        else:
            break

print 'Number of times bob occurs is: ' + str(count)