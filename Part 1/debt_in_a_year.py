balance = 320000
annualInterestRate = 0.2

balance_init = balance
mir = annualInterestRate / 12.0
guess = 0.01
debt = 0

while True:
    for month in range(12):
        debt += guess
        balance = balance - guess
        balance = balance + mir * balance
    if balance <= 0 and debt > balance_init:
        break
    else:
        guess += 0.01
        debt = 0
        balance = balance_init

print 'Lowest Payment: ' + str(guess)