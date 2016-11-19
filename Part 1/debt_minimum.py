balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

total = 0.0

for month in range(1,13):
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(round(balance * monthlyPaymentRate,2))
    total += balance * monthlyPaymentRate
    ubalance = balance - balance * monthlyPaymentRate
    balance = ubalance + annualInterestRate / 12.0 * ubalance
    print 'Remaining balance: ' + str(round(balance,2))

print 'Total paid: ' + str(round(total,2))
print 'Remaining balance: ' + str(round(balance,2))