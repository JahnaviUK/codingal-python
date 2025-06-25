def add(a, b):
    '''Adds two numbers using recursion'''
    if b == 0:
        print("The sum is:", a)
    else:
       print(a + b)
print(add.__doc__)
add(2,3)
add(3,0)