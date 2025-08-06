n1 = [3,9,5,7]
n2 = [7,6,5,4]
result = map(lambda x,y:x + y,n1,n2)
print("addition of two lists")
print(list(result))
n3 = [5,8,6,4,1]
def square (n):
 return n*n*n
result = map(square,n3)
print("square of the numbers in the list")
print(list(result))