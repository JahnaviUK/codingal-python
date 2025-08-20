class bird:
    def __init__(self):
        print("bird is ready ")
    def whoisthis(self):
        print("bird")
    def run(self):
        print("run faster ")
class penguin(bird):
    def __init__(self):
        print("penguin is ready ")
    def whoisthis(self):
        print("penguin")
    def swim(self):
        print("swim faster ")
a = penguin()
a.whoisthis()
a.swim()
a.run()
