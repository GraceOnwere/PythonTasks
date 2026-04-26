user_input = int(input('Enter a number or 0 to stop: '))


while user_input > 0:

    number = [user_input]
    
    user_input = int(input('Enter a number or 0 to stop: '))

    if user_input == 0:
        break

largest = max(number)

print(f"The largest number is {largest}")

    
