import pandas as pd
import random
from tkinter import *
from tkmacosx import Button
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog

# Constants
TIME_TO_COUNT_DOWN = 3

# Load dictionary files
DICTIONARY = pd.read_csv('data/english_words.csv', error_bad_lines=False, sep=';')

# Initialize variables
deck = []
current_card = None
cards_learned = []
cards_missed = []


# Functions
def get_sample_size():
    sample_size = None
    while sample_size is None:
        try:
            sample_size = simpledialog.askinteger(title="Flashy", prompt="How many words do you want to learn today?")
        except ValueError:
            pass
    return sample_size


def sample(sample_size):
    global deck
    deck = DICTIONARY.to_dict('records')
    random.shuffle(deck)
    deck = deck[:sample_size]
    check_marks.config(text=f"Cards learned: {len(cards_learned)}\nCards missed: {len(cards_missed)}\n"
                            f"Deck: {len(deck)}")
    flash_card_canvas.itemconfig(english_word_text, font=FONT_WORD)
    show_card()


def show_card():
    global current_card
    if len(deck) > 0:
        current_card = deck.pop()
        flash_card_canvas.itemconfig(english_word_text, text=current_card['English'])
        flash_card_canvas.itemconfig(original_language_text, text="English")
        flash_card_canvas.itemconfig(1, image=flash_card_canvas_image)
        count_down(TIME_TO_COUNT_DOWN)
    else:
        # End of deck, show results
        flash_card_canvas.itemconfig(original_language_text, text="")
        check_mark_button.config(state=DISABLED)
        deny_button.config(state=DISABLED)
        flash_card_canvas.itemconfig(english_word_text, text="Press start button press the start button to try again",
                                     font='Arial 30 italic')
        flash_card_canvas.itemconfig(timer_text, text="Great job!")
        check_marks.config(text=f"Cards learned: {len(cards_learned)}\nCards missed: {len(cards_missed)}\n"
                                f"Deck: {len(deck)}")
        if len(cards_missed) > 0:
            save_missed_words(cards_missed)
        messagebox.showinfo(title="Flashy", message="Click the start button to try again")
        start_button.config(state=NORMAL)
        cards_learned.clear()
        cards_missed.clear()


def count_down(count):
    check_mark_button.config(state=DISABLED)
    deny_button.config(state=DISABLED)
    start_button.config(state=DISABLED)
    flash_card_canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        flash_card_canvas.itemconfig(english_word_text, text=current_card['Russian'])
        flash_card_canvas.itemconfig(original_language_text, text="Russian")
        flash_card_canvas.itemconfig(1, image=flash_card_canvas_image_back)
        flash_card_canvas.itemconfig(timer_text, text='')
        check_mark_button.config(state=NORMAL)
        deny_button.config(state=NORMAL)


def mark_as_learned():
    cards_learned.append(current_card)
    check_marks.config(text=f"Cards learned: {len(cards_learned)}\nCards missed: {len(cards_missed)}\n"
                            f"Deck: {len(deck)}")
    show_card()


def mark_as_missed():
    cards_missed.append(current_card)
    check_marks.config(text=f"Cards learned: {len(cards_learned)}\nCards missed: {len(cards_missed)}\n"
                            f"Deck: {len(deck)}")
    show_card()


def save_missed_words(cards_missed_words):
    save = messagebox.askyesno("Flashy", "Do you want to save missed words?")
    if save:
        filename = filedialog.asksaveasfilename(initialdir='/', title='Save Missed Cards', defaultextension='.txt',
                                                filetypes=(("Text Files", "*.txt"),))
        if filename:
            with open(filename, 'w') as f:
                for card in cards_missed_words:
                    f.write(f"{card['English']}: {card['Russian']}\n")

# GUI
# Constants


BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = 'Arial 40 italic'
FONT_WORD = 'Arial 60 bold'

# Window
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Grids
check_mark_button = Button(image=PhotoImage(file="images/right.png"),  bg=BACKGROUND_COLOR,
                           highlightbackground=BACKGROUND_COLOR, borderless=1, width=100, height=100, state=DISABLED,
                           command=mark_as_learned)
deny_button = Button(image=PhotoImage(file="images/wrong.png"), bg=BACKGROUND_COLOR,
                     highlightbackground=BACKGROUND_COLOR, borderless=1, width=100, height=100, state=DISABLED,
                     command=mark_as_missed)
start_button = Button(image=PhotoImage(file="images/on-off-on.png"), bg=BACKGROUND_COLOR, borderless=1, width=178,
                      height=81,
                      command=lambda: sample(get_sample_size()))

flash_card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card_canvas_image = PhotoImage(file="images/card_front.png")
flash_card_canvas_image_back = PhotoImage(file="images/card_back.png")
flash_card_canvas.create_image(400, 262, image=flash_card_canvas_image)
original_language_text = flash_card_canvas.create_text(400, 150, text="English", fill="black", font=FONT_LANGUAGE)
english_word_text = flash_card_canvas.create_text(400, 263, fill='black', font=FONT_WORD, text="")
timer_text = flash_card_canvas.create_text(400, 450, text="stand by", fill="black", font=(FONT_WORD, 35))

check_mark_button.grid(column=3, row=2)
deny_button.grid(column=1, row=2)
flash_card_canvas.grid(column=1, row=1, columnspan=3)
start_button.grid(column=2, row=2)

# Check marks
check_marks = Label(text="", font=(FONT_WORD, 15), bg=BACKGROUND_COLOR)
check_marks.grid(column=2, row=4)

window.mainloop()
