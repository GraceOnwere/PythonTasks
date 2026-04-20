number = int(input('Enter a number of seconds: '))

hours = number // 3600

remaining_seconds = number % 3600

minutes = remaining_seconds // 60

seconds_left = number % 60

print(number,'seconds', '=',hours,"hours",minutes,"minutes", seconds_left, "seconds")
