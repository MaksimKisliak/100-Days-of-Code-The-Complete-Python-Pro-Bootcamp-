# Multiple answers: You can allow the player to choose more than one answer for each question by changing the check_answer method in the Question class to accept a list of answers and checking if the user's answer is in the list.
# Feedback on incorrect answers: You can display the correct answer when the player gets a question wrong by adding a correct_answer attribute to the Question class and printing it after the player gives an incorrect answer.
# High scores: You can keep track of the player's high scores by storing the scores in a file or database, and displaying the top scores after the game is over.
# Difficulty levels: You can categorize questions into different difficulty levels and allow the player to choose the level of difficulty for the quiz. You can add a difficulty attribute to the Question class to indicate the difficulty level of each question, and generate a quiz based on the chosen difficulty level.
# Timed quizzes: You can add a timer to the quiz and end the game after a certain amount of time has passed. You can use the time module in Python to implement this feature.
# These are just a few suggestions, and you can customize and enhance the game in many other ways as per your needs. The code is flexible and can be easily adapted to accommodate different features and functionalities.

import json
import time

class Question:
    def __init__(self, question, answers, correct_answer, difficulty):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        self.difficulty = difficulty

    def check_answer(self, answers):
        return set(answers) == set(self.correct_answer)

class Quiz:
    def __init__(self, questions, time_limit):
        self.questions = questions
        self.time_limit = time_limit
        self.score = 0

    def play(self):
        start_time = time.time()
        for question in self.questions:
            print(question.question)
            print("Possible answers:", question.answers)
            player_answer = input("Your answer (separate multiple answers with a comma): ").split(",")
            if question.check_answer(player_answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect.")
                print("Correct answer:", question.correct_answer)
            if time.time() - start_time >= self.time_limit:
                print("Time's up!")
                break
        print("Quiz complete. Your score is:", self.score)

def load_questions_from_file(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        questions = []
        for item in data:
            question = Question(item["question"], item["answers"], item["correct_answer"], item["difficulty"])
            questions.append(question)
        return questions

if __name__ == "__main__":
    questions = load_questions_from_file("questions.json")
    difficulty_level = input("Enter the difficulty level (easy, medium, hard): ")
    time_limit = int(input("Enter the time limit for the quiz (in seconds): "))
    filtered_questions = [q for q in questions if q.difficulty == difficulty_level]
    quiz = Quiz(filtered_questions, time_limit)
    quiz.play()

    
# This code implements the customizing and enhancing features as described above:

# The Question class now has a difficulty attribute and the check_answer method now accepts a list of answers and checks if it matches the correct answer.
# The Quiz class now has a time_limit attribute and the play method checks if the time limit has been reached before proceeding to the next question.
# The main code now allows the player to choose the difficulty level and the time limit for the quiz, and generates a quiz based on these inputs.
# The score is displayed after the quiz is complete.
# This code should give you a good starting point for building a full-fledged quiz game. You can continue to build upon this code and add more features as per your requirements.

#  This data file contains 8 questions with 4 answers each. The questions cover a variety of topics and are categorized into different difficulty levels (easy, medium). The data file can be easily extended by adding more questions. The code will automatically load the questions from this file and generate a quiz based on the chosen difficulty level and time limit.
[
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Rome", "Berlin"],
        "correct_answer": ["Paris"],
        "difficulty": "easy"
    },
    {
        "question": "What is the largest ocean in the world?",
        "answers": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        "correct_answer": ["Pacific Ocean"],
        "difficulty": "easy"
    },
    {
        "question": "What are the three primary colors?",
        "answers": ["Red, Green, Blue", "Yellow, Red, Blue", "Red, Yellow, Blue", "Green, Yellow, Red"],
        "correct_answer": ["Red, Green, Blue"],
        "difficulty": "medium"
    },
    {
        "question": "What is the formula for water?",
        "answers": ["H2O", "O2H", "OH2", "H20"],
        "correct_answer": ["H2O"],
        "difficulty": "easy"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "answers": ["Japan", "China", "India", "Thailand"],
        "correct_answer": ["Japan"],
        "difficulty": "easy"
    },
    {
        "question": "What is the smallest country in the world by land area?",
        "answers": ["Monaco", "Vatican City", "San Marino", "Nauru"],
        "correct_answer": ["Vatican City"],
        "difficulty": "medium"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "answers": ["Ag", "Au", "Pt", "Fe"],
        "correct_answer": ["Au"],
        "difficulty": "easy"
    },
    {
        "question": "Which country is the birthplace of Albert Einstein?",
        "answers": ["Germany", "Austria", "Switzerland", "Italy"],
        "correct_answer": ["Germany"],
        "difficulty": "easy"
    }
]

