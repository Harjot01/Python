class A:
    def met(self, a):
        self.a = a
        print(f"I am a method of class A {self.a}")

class B(A):
    super().met()


a = A()
b = B()

b.met(9)