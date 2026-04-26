count = 0

total = 0

user_input = int(input('Enter a number or -1 to stop: '))

while user_input >= 0:

    count = count + 1

    total = total + user_input

    user_input = int(input('Enter a number or -1 to stop: '))

average = total/count

print(f'The average is {average}')

    

