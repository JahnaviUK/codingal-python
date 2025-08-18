class employe:
    def __init__(self) :
        print("employee created")
    def __del__(self) :
        print("destructor called")
work = employe()
