
user_input = int(input('Enter a number or 0 to stop: '))

total = 0

while (user_input > 0):
    total = total + user_input

    user_input = int(input('Enter a number or 0 to stop: '))

    if user_input <= 0:
        break

print(f'The total number entered is {total}') 

    
