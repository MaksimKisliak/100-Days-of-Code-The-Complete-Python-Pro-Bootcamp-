# The __init__ method initializes a new instance of the Question class.
# It takes two arguments:
#   - q_text: a string representing the text of the question
#   - q_answer: a string representing the answer to the question

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
