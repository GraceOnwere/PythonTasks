principal = int(input("Enter the amount: "))

rate = int(input("Enter the rate: ")) /100 

time = int(input("Enter the number 0f years: "))

simple_interest = principal * rate * time

total_amount = principal + simple_interest

print('The total amount is ',total_amount)
