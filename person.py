class person():
    def __init__(self,name,IDnumber):
        self.name = name
        self.IDnumber = IDnumber
    def display(self):
        print (self.name)
        print(self.IDnumber)
class employee(person):
    def __init__(self,name,IDnumber,salary):
        self.salary = salary
        person.__init__(self,name,IDnumber)
a = employee("jahnavi",101,20000)
a.display()