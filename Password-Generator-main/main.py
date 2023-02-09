#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
list_nr_letters = list(range(nr_letters))
for letters_password in list_nr_letters:
    list_nr_letters[letters_password] = random.choice(letters)
list_nr_symbols = list(range(nr_symbols))
for symbols_password in list_nr_symbols:
    list_nr_symbols[symbols_password] = random.choice(symbols)
list_nr_numbers = list(range(nr_numbers))
for numbers_password in list_nr_numbers:
    list_nr_numbers[numbers_password] = random.choice(numbers)
password = list(list_nr_numbers + list_nr_letters + list_nr_symbols)
random.shuffle(password)
split_password = ''.join(password)
print(split_password)
