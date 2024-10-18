class Parent1 :
    def P1method(self) :
        print("Parent 1 class")

class Parent2 :
    def P2method(self) :
        print("Parent 2 class")
        
class Child(Parent1, Parent2) :
    def Cmethod(self) :
        print("Child class")

obj = Child()
obj.P1method()
obj.P2method()
obj.Cmethod()

output :
Parent 1 class
Parent 2 class
Child class
