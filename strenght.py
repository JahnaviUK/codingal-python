class string():
    def __init__(self) :
        self.str1 = ""
    def get_string (self) :
        self.str1 = input("enter string -")
    def print_string(self) :
        print("result is ",self.str1.upper())
pen = string()
pen.get_string()
pen.print_string()
