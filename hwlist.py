l2 = [2800,1200,1400,2500,2300]
print("original list",l2)
count = 0
for i in l2:
    count += i
average = count / len(l2)
print("sum = ",count)
print("average = ",average)
l2.sort()
print("sorted list",l2)
print("smallest element is ",l2[0])
print("largest element is ",l2[-1])