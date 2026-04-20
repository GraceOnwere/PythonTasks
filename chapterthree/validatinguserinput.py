passed = 0
failure = 0
count = 0
   
for number in range(10):
    input_collector = int(input('Enter a number: '))     
    count = 1
    while True:
        if input_collector == 1 or input_collector == 2:
           # print('passed')
            passed = passed + 1
            break  
        else:
           # print('Try again') 
            failure = failure + 1  
            break
total_passed = passed
total_failed = failure
print(f'You passed {passed} times and tried again {failure} times')
