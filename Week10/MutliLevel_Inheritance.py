class GrandParent :
    def P1method(self) :
        print("Grand Parent class")

class Parent(GrandParent) :
    def P2method(self) :
        print("Parent class")
        
class Child(Parent) :
    def Cmethod(self) :
        print("Child class")

obj = Child()
obj.P1method()
obj.P2method()
obj.Cmethod()

output :
Grand Parent class
Parent class
Child class
