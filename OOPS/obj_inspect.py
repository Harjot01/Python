import inspect

#first class
class Employee:
    __num = 4
    no_of_leaves = 10
    def __init__(self, name, profession, salary) -> None:
        self.name = name
        self.profession = profession
        self.salary = salary

    def printDetails(self):
        print (f"The name of the person is {self.name} and his profession is {self.profession} and salary is {self.salary}")

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @staticmethod
    def greet(name):
        print("Hello {0}".format(name))


a = Employee("Harjot", "Programming", 345)

print(inspect.getmembers(a))