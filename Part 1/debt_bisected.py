balance = 320000
annualInterestRate = 0.2

balance_init = balance
mir = annualInterestRate / 12.0
debt = 0

low = balance / 12
high = (balance * (1 + mir)**12) / 12.0
guess = (high + low) / 2.0

while True:
    for month in range(12):
        debt += guess
        ubalance = balance - guess
        balance = ubalance + mir * ubalance
    if ubalance < -0.01:
        high = guess
    elif ubalance > 0:
        low = guess
    else:
        break
    guess = high - ( ( high - low ) / 2.0 )
    debt = 0
    balance = balance_init

print 'Lowest Payment: ' + str(round(guess,2))