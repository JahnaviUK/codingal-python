money = float(input("enter amount of money"))
print("your amount of money is", money)
if money >= 1000:
    print("you will get 40% discount")
elif money >=800:
    print(" you will get 30% discount")
elif money >= 500:
    print(" you will get 20% discount")
elif money >= 300:
    print(" you will get 10% discount")
else: 
    print(" you will not get a discount")