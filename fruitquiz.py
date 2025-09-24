import random
class fruitquiz:
    def __init__(self):
        self.fruits={"apple":"red","guava":"green","banana":"yellow","orange":"orange"}
    def quiz(self):
        while True:
            fruit,color = random.choice(list(self.fruits.items()))
            print("what is the color of {}".format(fruit))
            user_answer = input()
            if user_answer.lowyellower()==color:
                print("correct answer ")
            else:
                print("wrong answer")
print("welcome to fruit quiz")
f = fruitquiz()
f.quiz()