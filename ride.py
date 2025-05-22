print("select your ride")
print("1.bike 2.car")
choice = int(input("ente your choice"))
if choice == 1:
    print("1.scootie 2.motorbike")
    choice2 = int(input("enter your choice"))
    if choice2 == 1:
        print("you have selected scootie")
    else:
        print("you have selected motorbike")
elif choice == 2:
    print("1.SUV 2.sedan") 
    choice3 = int(input("enter your choice"))
    if choice3 == 1:
        print("you have selected SUV")
    else:
        print("you have selected sedan") 
else:
    print("wrong choice") 
         