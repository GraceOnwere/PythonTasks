#print("Welcome to Python Programming!!!")
total = 0
count = 0
score = 0

while score != -1:
    total += score
    print(total)
    score = int(input('Enter Score or -1 to stop: '))
    count += 1
    print(count)

average_score = total /count
print(f"The average score is", {average_score})
