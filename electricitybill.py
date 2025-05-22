units = int(input("pls enter the number of unit you consumed"))
if units<50:
    amt = units*2.6
    tax = 25
elif units<=100:
    amt = units*3.25
    tax = 35
elif units<=200:
    amt = units*5.26
    tax = 45
else:
    amt = units*8.45
    tax = 75
total = amt + tax 
print("electricity bill = ",total)
   