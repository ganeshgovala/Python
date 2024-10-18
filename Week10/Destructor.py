class Demo :
    name = "Demo"
    def __init__(self) :
        print("This is Constructor")
    def __del__(self) :
        print("This is destructor")
    def display(self) :
        print("This is Display method")

obj = Demo()
print(obj.name)
obj.display()
del obj

output :
This is Constructor
Demo
This is Display method
This is destructor
