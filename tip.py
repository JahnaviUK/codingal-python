def totalcal(bill_amount,tip):
    total = bill_amount *(1 + 0.01*tip)
    total = round (total,2)
    print("please pay ",total)
totalcal(2000,20)