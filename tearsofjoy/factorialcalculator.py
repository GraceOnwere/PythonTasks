#10

user_input = int(input('Enter a number: '))

multiplication = 1



for number in range (1,user_input + 1):
    multiplication = multiplication * number
    
print(f'The factorial of {user_input} is {multiplication}')
