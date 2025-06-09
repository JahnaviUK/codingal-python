num = int(input("enter the four digit number"))
t = num 
numlen = 0 
while t>0:
    numlen = numlen + 1
    t = int(t / 10)
if numlen >= 4:
    numlen = int(numlen / 2)
    c = 0 
    while num > 0 :
        rem = num % 10
        if c == numlen :
            mid1 = rem
        elif c == numlen - 1:
            mid2 = rem 
        num = int(num / 10)
        c = c + 1
    product = mid1 * mid2 
    print("required products", product)
else :
    print ("its not a 4 digit number ")