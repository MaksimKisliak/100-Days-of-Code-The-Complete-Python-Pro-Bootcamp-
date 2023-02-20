# This implementation takes inputs for the number of letters, symbols, and numbers you'd like in your password. 
# Then, it generates a password string by combining randomly chosen letters, symbols, and numbers. 
# Finally, it shuffles the characters in the password string randomly to create a more secure password.

import random
import string

def password_manager():
    letters = int(input("How many letters would you like in your password? "))
    symbols = int(input("How many symbols would you like? "))
    numbers = int(input("How many numbers would you like? "))

    password = ''.join(random.choice(string.ascii_letters) for i in range(letters))
    password += ''.join(random.choice(string.punctuation) for i in range(symbols))
    password += ''.join(random.choice(string.digits) for i in range(numbers))

    password = ''.join(random.sample(password, len(password)))

    return password

print("Your password is: ", password_manager())
