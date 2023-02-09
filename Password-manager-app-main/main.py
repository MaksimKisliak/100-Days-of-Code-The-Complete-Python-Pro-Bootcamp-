# Importing required libraries
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# Constants defining the letters, numbers, and symbols to be used for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Function to generate the password
def password_generate():
    # Creating a list of random letters, symbols, and numbers of random lengths
    password_list = ([choice(letters) for char in range(randint(8, 10))] +
                    [choice(symbols) for char in range(randint(2, 4))] +
                    [choice(numbers) for char in range(randint(2, 4))])
    
    # Shuffling the password list
    shuffle(password_list)
    # Joining the password list to create a string
    password_to_display = "".join(password_list)
    # Clearing the password entry and inserting the generated password
    password_entry.delete(0, END)
    password_entry.insert(0, password_to_display)
    
    # Copying the password to the clipboard
    pyperclip.copy(password_to_display)

# Function to save the password
def save_password():
    # Checking if the website entry is empty
    if len(website_entry.get()) == 0:
        # Showing a warning message if the website entry is empty
        messagebox.showwarning(title='Please fill in all the details',
                               message='You\'ve left website box empty. Please enter a website name to proceed')
    # Checking if the email/username entry is empty
    elif len(email_username_entry.get()) == 0:
        # Showing a warning message if the email/username entry is empty
        messagebox.showwarning(title='Please fill in all the details',
                               message='You\'ve left e-mail box empty. Please enter an e-mail address to proceed')
    # Checking if the password entry is empty
    elif len(password_entry.get()) == 0:
        # Showing a warning message if the password entry is empty
        messagebox.showwarning(title='Please fill in all the details',
                               message='You\'ve left password box empty. Please enter a password to proceed')
    else:
        is_ok = messagebox.askokcancel(title=f'Website: {website_entry.get()}',
                                       message=f'These are the details entered:\nEmail: {email_username_entry.get()}\n'
                                               f'Password: {password_entry.get()}')
        if is_ok:
            with open(file='data.txt', mode='a') as file:
                file.write(f'{website_entry.get()} | {email_username_entry.get()} | {password_entry.get()}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# TODO ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title('Password Manager')
window.config(padx=60, pady=50)

# Canvas and Image
canvas = Canvas(width=200, height=200, highlightthickness=1)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)

# Labels
website_label = Label(text='Website:')
email_username_label = Label(text='Email/Username:')
password_label = Label(text='Password:')

# Entries
website_entry = Entry(width=35)
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.insert(0, 'makskislyak@gmail.com')
password_entry = Entry(width=20, show='*')

# Buttons
generate_password_button = Button(text='Generate Password', width=11, command=password_generate)
add_button = Button(text='Add', width=34, command=save_password)

# Grids
website_entry.grid(column=2, row=2, columnspan=2)
add_button.grid(column=2, row=5, columnspan=2)
email_username_label.grid(column=1, row=3)
generate_password_button.grid(column=3, row=4, columnspan=2)
email_username_entry.grid(column=2, row=3, columnspan=2)
password_label.grid(column=1, row=4)
password_entry.grid(column=2, row=4, columnspan=1)
website_label.grid(column=1, row=2)
canvas.grid(column=2, row=1)

window.mainloop()
