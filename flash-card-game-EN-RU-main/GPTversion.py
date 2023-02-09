# This code creates a flashcard program that displays the English word on one side of the card and the Russian translation on the other. 
# The show_card function is called to display the English word, and then the flip_card function is called 3 seconds later to display the Russian word.
# The current_word variable keeps track of the current word being displayed, and when all the words have been displayed, 
# it starts over again from the beginning.

import tkinter as tk
import time

def show_card():
    global current_word
    if current_word == len(words):
        current_word = 0
    label.config(text=list(words.keys())[current_word])
    root.after(3000, flip_card)

def flip_card():
    global current_word
    label.config(text=words[list(words.keys())[current_word]])
    current_word += 1
    root.after(3000, show_card)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Flashcard")

# Create a dictionary to store the English and Russian words
words = {
    "dog": "собака",
    "cat": "кошка",
    "bird": "птица",
    "fish": "рыба"
}

# Create a Label widget to display the words
label = tk.Label(root, text="", font=("Helvetica", 36))
label.pack()

current_word = 0
show_card()

# Start the Tkinter event loop
root.mainloop()
