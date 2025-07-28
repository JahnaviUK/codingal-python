dict = {'swimming':9,'is':7,'the':8,'best':9,'sport':9}
print("the original dictionary"+str(dict))
k = 9
result = 0
for key in dict:
    if dict[key]==k:
        result = result + 1
print("frequency of k is",str(result))