decimal = int(input("Enter a decimal number: "))
binary = ""

for i in range(decimal, 0, -1):  
    while decimal > 0:           
        binary = str(decimal % 2) + binary
        decimal = decimal // 2

print("Binary representation:", binary)
