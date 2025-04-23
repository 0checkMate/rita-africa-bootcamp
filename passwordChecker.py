# checking for password strength 

password = str(input('Enter a password: '))

has_uppercase = any(c.isupper() for c in password)
has_lowercase = any(c.islower() for c in password)
has_digit = any(not c.isalnum() for c in password)
length = len(password)

# printing the password message

if length >= 8:
    if has_uppercase and has_lowercase and has_digit:
        print('Strong password')
    else:
        print('Moderate password. Consider adding more complexity')
else:
    print('Weak password. It should be at least 8 characters long')