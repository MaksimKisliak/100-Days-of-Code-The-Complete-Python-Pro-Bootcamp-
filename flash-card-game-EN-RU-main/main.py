from tkinter import *
import time
import pandas
from tkmacosx import Button

# TODO -----------------------CONSTANTS--------------------------------------------------------------------------------

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = 'Ariel 40 italic'
FONT_WORD = 'Ariel 60 bold'
TIME_TO_COUNT_DOWN = 3
DICT_FOR_GAME = pandas.read_csv('data/english_words.csv', error_bad_lines=False, sep=';')


# TODO -----------------------CARD MECHANISM--------------------------------------------------------------------------------

def sample(number):
    global reps
    reps = 0
    global random_set
    random_set = DICT_FOR_GAME.sample(number)
    count_down(TIME_TO_COUNT_DOWN)


def take_the_card_out():
    pass


def keep_the_card_in_the_deck():
    pass


def flash_card_canvas_flip():
    flash_card_canvas.itemconfig(1, image=flash_card_canvas_image_back)
    flash_card_canvas.itemconfig(timer_text, text='')
    # flash_card_canvas.itemconfig(english_word_text, text=reps.Russian)
    flash_card_canvas.itemconfig(original_language_text, text='Russian')



# TODO -----------------------TIMER--------------------------------------------------------------------------------

def count_down(count):
    # flash_card_canvas.itemconfig(english_word_text, text=random_set.iloc[reps])
    global reps
    for (reps, row) in random_set.iterrows():
        flash_card_canvas.itemconfig(english_word_text, text=row.English)
    flash_card_canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)
        reps += 1
    else:
        flash_card_canvas_flip()
        if check_mark_button:
            pass
        elif deny_button:
            pass
        # marks = ""
        # work_sessions = math.floor(reps / 2)
        # for _ in range(work_sessions):
        #     marks += "✔"
        # check_marks.config(text=marks)


# TODO ---------------DICTIONARY---------------------------------------------------------------------------------------



# TODO -----------------------UI---------------------------------------------------------------------------------------

# Window
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
check_mark_button_image = PhotoImage(file='images/right.png')
deny_button_image = PhotoImage(file='images/wrong.png')
flash_card_canvas_image = PhotoImage(file='images/card_front.png')
flash_card_canvas_image_back = PhotoImage(file='images/card_back.png')
on_off_on_image = PhotoImage(file='images/on-off-on.png')

# Canvas
flash_card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card_canvas.create_image(400, 262, image=flash_card_canvas_image)

# Text
original_language_text = flash_card_canvas.create_text(400, 150, text="English", fill="black", font=FONT_LANGUAGE)
english_word_text = flash_card_canvas.create_text(400, 263, fill='black', font=FONT_WORD)
timer_text = flash_card_canvas.create_text(400, 450, text="stand by", fill="black", font=(FONT_WORD, 35))

# Buttons
check_mark_button = Button(image=check_mark_button_image, bg=BACKGROUND_COLOR,
                           highlightbackground=BACKGROUND_COLOR, borderless=1, width=100, height=100)
deny_button = Button(image=deny_button_image, bg=BACKGROUND_COLOR,
                     highlightbackground=BACKGROUND_COLOR, borderless=1, width=100, height=100)
start_button = Button(image=on_off_on_image, bg=BACKGROUND_COLOR, borderless=1, width=178, height=81,
                      command=sample(100))

# Grids
check_mark_button.grid(column=3, row=2)
deny_button.grid(column=1, row=2)
flash_card_canvas.grid(column=1, row=1, columnspan=3)
start_button.grid(column=2, row=2)

window.mainloop()
