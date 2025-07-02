import random 
number = str(random.randint(10,20))
print("guess the correct number between 10 to 20 to win the game ")
while True :
    guess = input("give me ur best guess")
    if number == guess :
        print("u won the game")
        print("the number was",number)
        break
    else :
        print("ur guess is incorrect. try again  ")