#print("from text editor")
average = 0
for number in range(2,100):
    #value = int(input('Enter an integer: '))

    if number % 2 == 0:
        print(number)
    #else:
       # print(f'{value} is odd')
        average +=number
print(average)
