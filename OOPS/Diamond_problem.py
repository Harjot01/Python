class A:
    @staticmethod
    def met():
        print("This is a method of class A")

class B(A):
    @staticmethod
    def met():
        print("This is a method of class B")

class C(A):
    @staticmethod
    def met():
        print("This is a method of class C")

class D(C, B):
    @staticmethod
    def met():
        print("This is a method of class D")

a = A()
b = B()
c = C()
d = D()

d.met()
    