n1 = [8,5,3,4]
n2 = [7,6,9,1]
result = map(lambda x,y:x + y,n1,n2)
print("addition of two lists")
print(list(result))
n3 = [5,8,6,4,1]
def square (n):
 return n*n
result = map(square,n3)
print("square of the numbers in the list")
print(list(result))