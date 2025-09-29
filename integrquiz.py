import random
class integerquiz:
    def __init__(self):
        self.integer={"1":"I","3":"III","5":"V","7":"VII","9":"IX","10":"X"}
    def quiz(self):
        while True:
            integer,roman = random.choice(list(self.integer.items()))
            print("what is the roman number of {}".format(integer))
            user_answer = input()
            if user_answer.lower()==roman:
                print("wrong answer ")
            else:
                print("correct answer")
print("welcome to integer quiz")
i = integerquiz()
i.quiz()