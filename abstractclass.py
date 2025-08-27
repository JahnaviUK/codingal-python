from abc import ABC,abstractmethod
class abs(ABC):
    def print(self,x):
        print ("passed value",x)
    @abstractmethod
    def task(self):
        print ("we are inside abstract class")
class pen(abs):
    def task (self):
        print("we are inside pen class")
scrunchie = pen()
scrunchie.task()
scrunchie.print(7)
