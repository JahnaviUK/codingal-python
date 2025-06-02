amount=int(input("enter the the amount you want to widraw"))
n1 = amount//100
n2 = (amount%100)//50
n3 = ((amount%100)%50)//10
print("number of 100 ruppee notes",n1)
print("number of 50 ruppee notes",n2)
print("number of 10 ruppee notes",n3)