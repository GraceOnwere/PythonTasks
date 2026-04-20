'''
initialize variables
collect input from user
use a loop to show the muliplication table
'''
count = 0
number = int(input('Enter a number: '))

for value in range (1,11):
    count = count + 1
   
    muliplication = number * count

    print(f"{number} x {count} = {muliplication}")
     
       

    
