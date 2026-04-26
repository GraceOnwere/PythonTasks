import random 

count = 0

user_guess = int(input('Enter a number between 1-100: '))

while user_guess > 0:

    computer_guess = random.randint(1,100)

    count = count + 1

    if user_guess > computer_guess:
        print('lower')

    elif user_guess < computer_guess:
        print('higer')

    elif user_guess == computer_guess:
        print('correct!')
        break

    user_guess = int(input('Enter a number: '))

print(f"You guessed {count} times")
