import requests
import random
from tkinter import *
from tkinter import simpledialog, messagebox, filedialog
from tkmacosx import Button
from PIL import ImageTk, Image


class FlashCardApp:
    def __init__(self):
        self.background_color = "#B1DDC6"
        self.font_language = 'Arial 40 italic'
        self.font_word = 'Arial 60 bold'
        self.time_to_count_down = 3
        self.deck = []
        self.current_card = None
        self.cards_learned = []
        self.cards_missed = []

        self.window = Tk()
        self.window.title('Flashy')
        self.window.config(padx=50, pady=50, bg=self.background_color)

        self.check_mark_button = Button(image=ImageTk.PhotoImage(Image.open("images/right.png")),
                                        bg=self.background_color, highlightbackground=self.background_color,
                                        borderless=1, width=100, height=100, state=DISABLED,
                                        command=self.mark_as_learned)
        self.deny_button = Button(image=ImageTk.PhotoImage(Image.open("images/wrong.png")),
                                  bg=self.background_color, highlightbackground=self.background_color,
                                  borderless=1, width=100, height=100, state=DISABLED, command=self.mark_as_missed)
        self.start_button = Button(image=ImageTk.PhotoImage(Image.open("images/on-off-on.png")),
                                   bg=self.background_color, borderless=1, width=178, height=81, command=self.start)

        self.flash_card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=self.background_color)
        self.flash_card_canvas_image = ImageTk.PhotoImage(Image.open("images/card_front.png"))
        self.flash_card_canvas_image_back = ImageTk.PhotoImage(Image.open("images/card_back.png"))
        self.flash_card_canvas.create_image(400, 262, image=self.flash_card_canvas_image)
        self.original_language_text = self.flash_card_canvas.create_text(400, 150, text="", fill="black",
                                                                         font=self.font_language)
        self.english_word_text = self.flash_card_canvas.create_text(400, 263, fill='black', font=self.font_word,
                                                                    text="")
        self.timer_text = self.flash_card_canvas.create_text(400, 450, text="", fill="black",
                                                             font=(self.font_word, 35))

        self.check_marks = Label(text="", font=(self.font_word, 15), bg=self.background_color)

        self.check_mark_button.grid(column=3, row=2)
        self.deny_button.grid(column=1, row=2)
        self.flash_card_canvas.grid(column=1, row=1, columnspan=3)
        self.start_button.grid(column=2, row=2)
        self.check_marks.grid(column=2, row=4)

        self.dictionary = Dictionary()

    @staticmethod
    def get_sample_size():
        sample_size = None
        while sample_size is None:
            try:
                sample_size = simpledialog.askinteger(title="Flashy",
                                                      prompt="How many words do you want to learn today?")
            except ValueError:
                pass
        return sample_size

    def sample(self):
        sample_size = self.get_sample_size()
        self.deck = self.dictionary.to_dict(sample_size)
        print(self.deck)
        self.check_marks.config(
            text=f"Cards learned: {len(self.cards_learned)}\nCards missed: {len(self.cards_missed)}\n"
                 f"Deck: {len(self.deck)}")
        self.flash_card_canvas.itemconfig(self.english_word_text,
                                          font=self.font_word)
        self.show_card()

    def show_card(self):
        if len(self.deck) > 0:
            self.current_card = self.deck.pop()
            self.flash_card_canvas.itemconfig(self.english_word_text, text=self.current_card['English'])
            self.flash_card_canvas.itemconfig(self.original_language_text, text='English')
            self.flash_card_canvas.itemconfig(1, image=self.flash_card_canvas_image)
            self.window.after(1000, self.count_down, self.time_to_count_down)
        else:
            self.show_results()

    def count_down(self, count):
        self.check_mark_button.config(state=DISABLED)
        self.deny_button.config(state=DISABLED)
        self.start_button.config(state=DISABLED)
        self.flash_card_canvas.itemconfig(self.timer_text, text=count)
        if count > 0:
            self.window.after(1000, self.count_down, count - 1)
        else:
            self.flash_card_canvas.itemconfig(self.english_word_text, text=self.current_card['Russian'])
            self.flash_card_canvas.itemconfig(self.original_language_text, text="Russian")
            self.flash_card_canvas.itemconfig(1, image=self.flash_card_canvas_image_back)
            self.flash_card_canvas.itemconfig(self.timer_text, text='')
            self.check_mark_button.config(state=NORMAL)
            self.deny_button.config(state=NORMAL)

    def mark_as_learned(self):
        self.cards_learned.append(self.current_card)
        self.check_marks.config(
            text=f"Cards learned: {len(self.cards_learned)}\nCards missed: {len(self.cards_missed)}\n"
                 f"Deck: {len(self.deck)}")
        self.show_card()

    def mark_as_missed(self):
        self.cards_missed.append(self.current_card)
        self.check_marks.config(
            text=f"Cards learned: {len(self.cards_learned)}\nCards missed: {len(self.cards_missed)}\n"
                 f"Deck: {len(self.deck)}")
        self.show_card()

    @staticmethod
    def save_missed_words(cards_missed_words):
        save = messagebox.askyesno("Flashy", "Do you want to save missed words?")
        if save:
            filename = filedialog.asksaveasfilename(initialdir='/', title='Save Missed Cards',
                                                    defaultextension='.txt',
                                                    filetypes=(("Text Files", "*.txt"),))
            if filename:
                with open(filename, 'w') as f:
                    for card in cards_missed_words:
                        f.write(f"{card['English']}: {card['Russian']}\n")

    def show_results(self):
        self.check_marks.config(
            text=f"Cards learned: {len(self.cards_learned)}\nCards missed: {len(self.cards_missed)}\n"
                 f"Deck: {len(self.deck)}")
        self.flash_card_canvas.itemconfig(self.english_word_text, text="Great job!")
        self.flash_card_canvas.itemconfig(self.original_language_text, text="")
        self.check_mark_button.config(state=DISABLED)
        self.deny_button.config(state=DISABLED)
        if len(self.cards_missed) > 0:
            self.save_missed_words(self.cards_missed)
        # add delay of 1000ms before resetting the screen
        self.window.after(1000, self.reset_screen)

    def reset_screen(self):
        self.start_button.config(state=NORMAL)
        self.flash_card_canvas.itemconfig(self.original_language_text, text="")
        self.cards_learned.clear()
        self.cards_missed.clear()
        messagebox.showinfo(title="Flashy", message="Click the start button to try again")
        self.flash_card_canvas.itemconfig(self.timer_text, text="")
        self.flash_card_canvas.itemconfig(self.english_word_text,
                                          text="Press start button to try again",
                                          font=self.font_language)

    def start(self):
        self.sample()


class Dictionary:
    def __init__(self):
        response = requests.get("https://api.npoint.io/e10c8bb117f377353235")
        self.words = response.json()

    def to_dict(self, sample_size):
        deck = self.words
        random.shuffle(deck)
        return deck[:sample_size]


app = FlashCardApp()
app.start()
app.window.mainloop()
