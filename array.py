import array as arr
array_num = arr.array('i',[1,2,3,4,5,6,2,2])
print("original array"+ str(array_num))
print("number of opperences of number 2 in the array"+str(array_num.count(2)))
array_num.reverse()
print("reverse the array"+str(array_num))