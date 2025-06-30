try :
    n1,n2=eval(input("enter two numbers that are seperated by a comma "))
    result = n1 / n2
    print ("result is ",result)
except ZeroDivisionError :
    print("division by zero is error")
except SyntaxError :
    print ("comma is missing")
except :
    print("wrong input")
else :
    print("no exceptions")
finally :
    print("this will excute no matter what")