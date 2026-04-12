principal = int(input('Enter the principal amount: '))

annual_interest_rate = int(input('Enter the annual interest rate: ')) / 100

duration = int(input('Enter the duration in years: ')) * 12 

monthly_rate = annual_interest_rate / 12 

monthly_payment = principal * ((monthly_rate * (1 + monthly_rate) ** duration) / ((1 + monthly_rate) ** duration - 1))

print('Your monthly paymenet is $',monthly_payment)
