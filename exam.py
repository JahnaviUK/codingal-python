medical_cause = input("did you have a medical cause Y or N - ")
att = int(input("enter the attendence of the student - "))
if medical_cause == "Y":
    print("you are allowed")
else :
    if att>=75:
        print("allowed")
    else:
        print("not allowed")
        