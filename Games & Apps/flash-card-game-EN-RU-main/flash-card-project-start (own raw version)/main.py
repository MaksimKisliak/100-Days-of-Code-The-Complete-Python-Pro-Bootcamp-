from tkinter import *
import time
import pandas
from tkmacosx import Button
from random import choices, randint, choice

# TODO -----------------------CONSTANTS--------------------------------------------------------------------------------

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = 'Ariel 40 italic'
FONT_WORD = 'Ariel 60 bold'
TIME_TO_COUNT_DOWN = 3
DICT_FOR_GAME = pandas.read_csv('data/english_words.csv', error_bad_lines=False, sep=';')
SAMPLE_NUMBER = 3
REPS = 0
RANDOM_SET = DICT_FOR_GAME.sample(SAMPLE_NUMBER)


# TODO -----------------------CARD MECHANISM---------------------------------------------------------------------------

def take_the_card_out():
    """
    This function removes a card from the deck and updates the text of the English word on the card to the next word in the deck.
    """
    global REPS
    try:
        if not RANDOM_SET.empty:
            RANDOM_SET.drop(RANDOM_SET.index.tolist()[REPS], axis=0, inplace=True)
            REPS -= 1
            flash_card_canvas.itemconfig(english_word_text, text=RANDOM_SET.iloc[REPS, 0])
        else:
            flash_card_canvas.itemconfig(original_language_text, text="Press reset button\nto take another set of words")
            flash_card_canvas.itemconfig(english_word_text, text="")
    except IndexError:
        if RANDOM_SET.empty:
            flash_card_canvas.itemconfig(original_language_text, text="Press reset button\nto take another set of words")
            flash_card_canvas.itemconfig(english_word_text, text="")
        # REPS = randint(0, REPS-1)
    finally:
        if not RANDOM_SET.empty:
            flash_card_canvas.itemconfig(original_language_text, text="English")
            flash_card_canvas.itemconfig(1, image=flash_card_canvas_image)
            print(REPS)
            print(RANDOM_SET)
            reset_button.configure(bg='#ffffff', highlightbackground='#ffffff')
            count_down(TIME_TO_COUNT_DOWN)


def keep_the_card_in_the_deck():
    """
    This function keeps a card in the deck and updates the text of the English word on the card to the next word in the deck.
    """
    global REPS
    try:
        REPS += 1
        flash_card_canvas.itemconfig(english_word_text, text=RANDOM_SET.iloc[REPS, 0])
    except IndexError:
        REPS = randint(0, SAMPLE_NUMBER-1)
    finally:
        flash_card_canvas.itemconfig(1, image=flash_card_canvas_image)
        reset_button.configure(bg='#ffffff', highlightbackground='#ffffff')
        flash_card_canvas.itemconfig(original_language_text, text="English")
        count_down(TIME_TO_COUNT_DOWN)


def flash_card_canvas_flip():
    """
    This function changes the appearance of the flash card on the canvas by updating its text and image. 
    It uses the global variables reset_button and REPS to accomplish this. 
    It first sets the image of the flash card to the back side using flash_card_canvas.itemconfig(1, image=flash_card_canvas_image_back). 
    It then sets the text of the timer to an empty string using flash_card_canvas.itemconfig(timer_text, text=''). 
    If the RANDOM_SET is not empty, it sets the text of english_word_text to the value of the second column (RANDOM_SET.iloc[REPS, 1]) 
    in the current row REPS of the RANDOM_SET. If an IndexError occurs, it sets the REPS to a random integer between 0 and SAMPLE_NUMBER - 1. 
    Finally, it sets the text of original_language_text to "Russian" and changes the background color and highlightbackground color of 
    the reset_button to '#a4cebc'.
    """
    global reset_button
    global REPS
    flash_card_canvas.itemconfig(1, image=flash_card_canvas_image_back)
    flash_card_canvas.itemconfig(timer_text, text='')
    if not RANDOM_SET.empty:
        try:
            flash_card_canvas.itemconfig(english_word_text, text=RANDOM_SET.iloc[REPS, 1])
        except IndexError:
            REPS = randint(0, SAMPLE_NUMBER - 1)
    flash_card_canvas.itemconfig(original_language_text, text='Russian')
    reset_button.configure(bg='#a4cebc', highlightbackground='#a4cebc')


# TODO -----------------------TIMER-------------------------------------------------------------------------------------

def count_down(count=TIME_TO_COUNT_DOWN):
    """
    The function counts down from a specified time (default is 3) and updates the countdown in the canvas.
    Parameters:
    count (int, optional): The time to start the countdown from. Defaults to TIME_TO_COUNT_DOWN.
    """
    global REPS
    try:
        flash_card_canvas.itemconfig(original_language_text, text="English")
        flash_card_canvas.itemconfig(english_word_text, text=RANDOM_SET.iloc[REPS, 0])
    except IndexError:
        REPS = 0
        print(REPS)
    finally:
        print(REPS)
        print(RANDOM_SET)
        flash_card_canvas.itemconfig(timer_text, text=count)
        if count > 0:
            window.after(1000, count_down, count - 1)
        else:
            flash_card_canvas_flip()


# TODO -----------------------DICTIONARY SAMPLE------------------------------------------------------------------------

def reset():
    """
    The function resets the flashcard game by generating a new set of words from the dictionary and updating the canvas.
    """
    global RANDOM_SET
    global REPS
    REPS = 0
    flash_card_canvas.itemconfig(original_language_text, text="")
    flash_card_canvas.itemconfig(english_word_text, text="")
    RANDOM_SET = DICT_FOR_GAME.sample(SAMPLE_NUMBER)
    print(RANDOM_SET)

# TODO -----------------------UI---------------------------------------------------------------------------------------

# Window
window = Tk()
window.title('Flashy')
window.config(padx=20, pady=30, bg=BACKGROUND_COLOR)

# Images
check_mark_button_image = PhotoImage(file='images/right.png')
deny_button_image = PhotoImage(file='images/wrong.png')
flash_card_canvas_image = PhotoImage(file='images/card_front.png')
flash_card_canvas_image_back = PhotoImage(file='images/card_back.png')
start_button_image = PhotoImage(file='images/on-off-on.png')
reset_button_image = PhotoImage(file=
                                'images/pngegg.png')

# Canvas
flash_card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card_canvas.create_image(400, 262, image=flash_card_canvas_image)

# Text
original_language_text = flash_card_canvas.create_text(400, 150, text="English", fill="black", font=FONT_LANGUAGE)
english_word_text = flash_card_canvas.create_text(400, 263, fill='black', font=FONT_WORD, text="")
timer_text = flash_card_canvas.create_text(400, 450, text="stand by", fill="black", font=(FONT_WORD, 35))

# Buttons
check_mark_button = Button(image=check_mark_button_image, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR,
                           borderless=1, width=100, height=100, command=take_the_card_out)
deny_button = Button(image=deny_button_image, bg=BACKGROUND_COLOR,  highlightbackground=BACKGROUND_COLOR, borderless=1,
                     width=100, height=100, command=keep_the_card_in_the_deck)
start_button = Button(image=start_button_image, bg=BACKGROUND_COLOR, borderless=1, width=178, height=81,
                      command=count_down)

reset_button = Button(image=reset_button_image, bg='#ffffff', highlightbackground='#ffffff',
                           borderless=1, width=50, height=50, command=reset)


# Grids
check_mark_button.grid(column=4, row=2)
deny_button.grid(column=2, row=2)
flash_card_canvas.grid(column=2, row=1, columnspan=3)
start_button.grid(column=3, row=2)
reset_button.place(x=375, y=35)


window.mainloop()
