print("enter marks obtained in 5 subjects")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input()) 
mark5 = int(input())
total = mark1 + mark2 + mark3 + mark4 + mark5
avg = total / 5 
if avg >=91 and avg <= 100 :
    print("your grade is A1")
elif avg >=81 and avg <= 91 :
    print("your grade is A2")
elif avg >71 and avg <= 81 :
    print("your grade is B1")
elif avg >=61 and avg <= 51 :
    print("your grade is B2")
elif avg >=51 and avg <= 31 :
    print("your grade is C1")
elif avg >=33 and avg <= 21 :
    print("your grade is C2")
else :
    print("your grade is invalid input")
