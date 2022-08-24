class A:
    classvar1 = "I am a class variable of class A"
    def __init__(self) -> None:
        self.var1 = "I am an instance variable of class A"
        self.classvar1 = "Instance variable in class A"
        self.special = "special"

class B(A):
    classvar2 = "I am a class variable of class B"
    def __init__(self) -> None:
        super().__init__()
        self.var1 = "I am instance varible of class B"
        self.classvar1 = "Instance variable in class B"


a = A()
b = B()

print(b.var1)
print(b.classvar1)
        