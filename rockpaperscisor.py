import random 
while True :
    user = input("select rock paper or scissor :")
    possible = ["rock","paper","scissor"]
    computer = random.choice(possible)
    print("you chose ",user,"computer chose",computer)
    if user == computer:
        print("both players selected",user,"its a tie ")
    elif user == "rock" :
        if computer == "scissor" :
            print("rock smasher scissor u won ")
        else :
            print(" u lose")
    elif user == "paper" :
        if computer == "rock" :
            print(" u won ")
        else :
            print(" u lose")
    elif user == "scissor" :
        if computer == "paper" :
            print(" u won ")
        else :
            print("u lose")
            break