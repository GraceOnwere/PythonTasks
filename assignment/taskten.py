number = int(input('Enter a number in seconds: '))

hours = number // 3600

remaining_seconds = number % 3600

minutes = remaining_seconds // 60

seconds_left = remaining_seconds % 60

print(number,'seconds = ', hours ,'hours', minutes ,'minutes', seconds_left, 'seconds')
