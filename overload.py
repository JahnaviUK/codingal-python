class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if (self.a < other.a):
            return "ob1 is less than ob2"
        else :
            return "ob2 is less than ob1"
    def __eq__(self,other):
        if (self.a==other.a):
            return "both are equal"
        else :
            return" not equal "
ob1 = A(12)
ob2 = A(23)
print (ob1<ob2)
ob3 = A(45)
ob4 = A(42)
print(ob3 == ob4)
        