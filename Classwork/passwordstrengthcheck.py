'''
1. Get input from user
2. check the length of the password
3. if password length is < 8 display weak
else if password length is 8 display weak
else if password length is >= 8 and <= 16 display strong
else display strong
'''

password_length = input("Enter password: ")

if len(password_length) < 8:
    print('Very weak')
elif len(password_length) == 8:
    print('Weak')
elif len(password_length) >= 8 and len(password_length) <= 16:
    print('Strong')
elif len(password_length) > 16:
    print('Very Strong')
