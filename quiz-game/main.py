from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

play = QuizBrain(question_bank)
play.play_quiz()

while play.still_has_questions():
    play.play_quiz()
