user_input = int(input('Enter the number of rows: '))

for rowcounter in range(1,user_input + 1):
    for columncounter in range(1,rowcounter + 1):
        print(columncounter, end=' ')

    print()
