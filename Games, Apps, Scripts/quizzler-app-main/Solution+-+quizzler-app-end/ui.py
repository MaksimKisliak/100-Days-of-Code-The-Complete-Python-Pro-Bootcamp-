from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    """
    A class that provides the graphical interface for the Quizzler application.
    """
    def __init__(self, quiz_brain: QuizBrain):
        """
        Initializes the quiz interface.
        
        :param quiz_brain: the QuizBrain object that contains the question data and score information.
        """
        # store the quiz brain object
        self.quiz = quiz_brain

        # initialize the Tkinter window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # create the score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # create the canvas for displaying questions
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # create the "True" button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # create the "False" button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # get the first question and display it
        self.get_next_question()

        # start the main event loop
        self.window.mainloop()


    def get_next_question(self):
        """
        Loads the next question from the quiz brain and displays it on the canvas.
        """
        # Reset the background color of the canvas to white
        self.canvas.config(bg="white")
        # Check if there are still questions to ask
        if self.quiz.still_has_questions():
            # Update the score label
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # Get the next question text
            q_text = self.quiz.next_question()
            # Display the question text on the canvas
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # If there are no more questions, display a message and disable the buttons
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """
        Called when the "True" button is pressed.
        """
        # Call give_feedback with the result of the quiz's check_answer method
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """
        Called when the "False" button is pressed.
        """
        # Call give_feedback with the result of the quiz's check_answer method
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """
        Displays feedback on the canvas indicating whether the answer was right or wrong.
        """
        # Change the background color of the canvas depending on whether the answer was right or wrong
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # Schedule the next question to be displayed after 1 second (1000 milliseconds)
        self.window.after(1000, self.get_next_question)




