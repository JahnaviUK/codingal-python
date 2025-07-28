dict = {'codingal':2,'is':2,'best':2,'for':2,'coding':1}
print("the original dictionary"+str(dict))
k = 2
result = 0
for key in dict:
    if dict[key]==k:
        result = result + 1
print("frequency of k is",str(result))