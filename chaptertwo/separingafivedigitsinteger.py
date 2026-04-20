number = int (input('Enter a five digit number: '))

digit_one = number // 10000

digit_two = (number // 1000) % 10

digit_three = (number // 100) % 10

digit_four = (number // 10) % 10

digit_five = number % 10

print(digit_one,digit_two,digit_three,digit_four,digit_five)
