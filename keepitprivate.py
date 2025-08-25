class myclass :
    __privatevar = 8
    def __privmath(self):
        print("i am inside my class")
    def hello(self):
        print("private variable value is",myclass.__privatevar)
pencil = myclass()
pencil.hello()
pencil.__privmath()
