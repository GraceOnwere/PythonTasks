'''
1. declear and initialize the customers total
2. the customers discounted amount is dependent on how high the spending amount is
3. so if total is between 1000 - 10000, it receive a 5%
else if total is between 10000 - 15000, it receive a 10%
else the total receives a 20 % discount
'''

total_purchase_amount = int(input('Enter your purchase amount: '))

if total_purchase_amount >= 1000 and total_purchase_amount <= 10000:
    discounted_amount_one = total_purchase_amount * 0.05
    print('Your final amount is ', total_purchase_amount - discounted_amount_one)

elif total_purchase_amount >= 10000 and total_purchase_amount <=50000:
    discounted_amount_two = total_purchase_amount * 0.1
    print('Your final amount is ', total_purchase_amount - discounted_amount_two)

elif total_purchase_amount >50000:
    discounted_amount_three = total_purchase_amount * 0.2
    print('Your final amount is ', total_purchase_amount - discounted_amount_three)
