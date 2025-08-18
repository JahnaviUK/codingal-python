class pair_elements:
    def sum (self,nums,target) :
    # create an empty dictionary
       lookup = {}
       for i,num in enumerate(nums) :
           if target - num in lookup :
               return(lookup[target - num],i)
           lookup[num] = i 
#take input of sum from the user 
value = int(input("enter the sum for which u want to make this search "))
print("index1 =%d,index2 =%d"%pair_elements().sum((10,20,30,40,50,60,70,80,90),value))