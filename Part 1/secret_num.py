print 'Please think of a number between 0 and 100!'

epsilon = 1
step = 1
low = 0
high = 100
ans = (high+low)/2

while abs(ans**2-100) >= epsilon:
    print 'Is your secret number ' + str(ans) + '?'
    info = str(raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. '))
    if info == 'c':
        print 'Game over. Your secret number was: ' + str(ans)
        break
    elif info == 'l':
        low = ans
        ans = (high+low)/2
    elif info == 'h':
        high = ans
        ans = (high+low)/2
    else:
        print "Sorry, I did not understand your input."