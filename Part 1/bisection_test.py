# lecture 3.6, slide 2
# bisection search for square root

x = 25
epsilon = 0.5
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
        print 'low = ' + str(low)
    else:
        high = ans
        print 'high = ' + str(high)
    ans = (high + low)/2.0

print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))