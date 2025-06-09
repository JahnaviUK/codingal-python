string = input("please enter your word")
char = input ("please enter the charecter you want to check")
i = 0 
count = 0
while(i<len(string)):
    if (string[i]==char):
        count = count + 1 
    i = i + 1
print("the total number of times the charectar has occured ", count)

