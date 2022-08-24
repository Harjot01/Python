class calculator:

    def __init__(self, x) -> None:
        self.num = x
        
    
    def sq(self):
        print(f"The value of square of {self.num} is {self.num**2}")

    def sc(self):
        print(f"The value of square root of {self.num} is {self.num**0.5}")

    def sqc(self):
        print(f"The value of cube of {self.num} is {self.num**3}")

d = calculator(5)
d.sqc()
    
