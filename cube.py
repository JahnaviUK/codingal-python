def cube(number):
    return number * number * number
def divideby3(number) :
    if number % 3 == 0 :
        return cube(number)
    else :
        return False
print(divideby3(6)) 
print(divideby3(11)) 