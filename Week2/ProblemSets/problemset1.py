#Interest Program
def remainingbalance(balance,annualInterestRate,monthlyPaymentRate):
    '''
    Works out the pays the minimum monthly payment required by the credit card company each month.
    '''
    monthlyInterestRate = annualInterestRate/12
    minimumMonthlyPayment = monthlyPaymentRate*balance
    monthlyUnpaidBalance = balance-minimumMonthlyPayment
    return monthlyUnpaidBalance+(monthlyInterestRate*monthlyUnpaidBalance)
    
#Variables
balance = 7600
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#Program Start
count = 0
while (count < 12):
   balance = remainingbalance(balance,annualInterestRate,monthlyPaymentRate)
   count = count + 1
   
print("Remaining Balance: ",round(balance,2))
