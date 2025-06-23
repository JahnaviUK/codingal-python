def fectorial(x) :
    '''this is a recursive function to find the fectorial'''
    if x == 0 or x == 1 :
        return 1 
    else :
        return x * fectorial(x - 1)
print(fectorial.__doc__)
print("the fectorail of 25",fectorial(25))