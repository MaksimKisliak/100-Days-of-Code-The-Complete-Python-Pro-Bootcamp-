import html

# Class to create an instance of the quiz and manage the questions and scores
class QuizBrain:

    def __init__(self, q_list):
        """
        Initialize the QuizBrain instance by setting the question number, score, and the question list
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        Returns True if the quiz still has questions to ask,
        False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Updates the current question and increments the question number by 1.
        Returns the text of the current question.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """
        Compares the user answer with the correct answer for the current question.
        If the answers match, increments the score by 1.
        Returns True if the answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

