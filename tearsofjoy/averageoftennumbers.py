
total = 0

count = 0

for number in range(0,10):

    user_input = int(input('Enter the score: '))

    count = count + 1

    total = total + user_input

average = total/count

print (f'The average of the numbers is {average}') 
