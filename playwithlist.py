l1 = [405,905,35]
print("original list",l1)
count = 0
for i in l1:
    count += i
average = count / len(l1)
print("sum = ",count)
print("average = ",average)
l1.sort()
print("sorted list",l1)
print("smallest element is ",l1[0])
print("largest element is ",l1[-1])