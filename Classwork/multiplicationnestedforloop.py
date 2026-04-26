'''
initialize variables
collect input from user
use a loop to show the muliplication table
'''

#number = int(input('Enter a number: '))

for number in range (1,10):
    print(number," ")
    for count in range(1,10):  
        multiplication = number * count

        print(f"{multiplication}", "|", end= " ")
     
       

