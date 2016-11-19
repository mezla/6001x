x = 5
epsilon = 0.5 # how close do i want to get?
step = 0.5
numGuesses = 0
ans = 0.0

while ( abs(ans**2-x) ) >= epsilon and ans <= x:
    # e.g. while abs ( 5**2 - 25 ) >= epsilon -> is 0 >= 0.1?
    # am i too far? have i exhausted all the steps?
    # and is answer less or equal to x -> am i done?
    print ans
    print abs(ans**2-x)
    ans += step
    numGuesses += 1
print 'result:'
print abs(ans**2-x)
print ans
print 'Number of guesses: ' + str(numGuesses)


#if abs(ans**2-x) >= epsilon:
#    print 'Failed to find square root of ' + str(x)
#else:
print str(ans) + ' is close enough to the root square of ' + str(x)