

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#Your code begins here

i = 1;
while i <= 12:
    balance = balance - (balance * monthlyPaymentRate);
    balance = balance + (balance * annualInterestRate/12.0)
    print ("Month", i, "Remaining balance: ", round(balance, 2));
    i = i + 1;
print("Remaining balance:", round(balance, 2))

