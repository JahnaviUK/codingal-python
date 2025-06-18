def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide (p,q):
    return p/q
print("pls select the operation")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")
choice = input("please enter your choice a,b,c,d - ")
n1 = int(input("enter the first number"))
n2 = int(input("enter the second number" ))
if choice == "a":
    print(add(n1,n2))
elif choice == "b":
    print(subtract(n1,n2))
elif choice == "c":
    print(multiply(n1,n2))
elif choice == "d":
    print(divide(n1,n2))
else:
    print("invalid choice")