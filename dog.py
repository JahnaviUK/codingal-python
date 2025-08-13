class dog:
    species = "golden retriever"
    def __init__(self,name,age):
        self.name = name 
        self.age = age
z = dog("momo","2.4 years")
print("name = ",z.name)
print("age = ",z.age)
print("it is a",z.species)