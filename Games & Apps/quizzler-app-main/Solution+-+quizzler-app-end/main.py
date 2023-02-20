from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


# Create a list of Question objects
question_bank = []
for question in question_data:
    # Extract the question text and answer from each data entry
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # Create a new Question object and add it to the question bank
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a QuizBrain object using the question bank
quiz = QuizBrain(question_bank)
# Create a QuizInterface object using the QuizBrain object
quiz_ui = QuizInterface(quiz)
