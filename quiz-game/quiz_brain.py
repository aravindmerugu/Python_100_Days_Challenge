import random


class QuizBrain:

    def __init__(self, question_bank):
        self.score = 0
        self.index = 0
        self.wrong = False
        self.question_bank = question_bank

    def still_has_questions(self):
        if len(self.question_bank) == 0:
            print(f"\n\nyou have completed the quiz\n your final score is {self.score}/{self.index}")
            return False
        else:
            return True

    def play_quiz(self):
        ans = random.choice(self.question_bank)
        self.index += 1
        choose = input(f"{self.index}. {ans.text} Type True/False: ").lower()
        self.question_bank.remove(ans)
        if choose == ans.answer.lower():
            print("That's right")
            self.score += 1
        else:
            print("wrong answer")
        print(f"your current score is {self.score}/{self.index}")