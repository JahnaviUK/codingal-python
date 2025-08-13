class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name 
        self.age = age
z = parrot("zoe",12)
print("name ",z.name)
print("age",z.age)
print("it is a",z.species)