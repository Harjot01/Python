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

rohan = Employee('Rohan','Athletics', '400')
print(rohan._Employee__num)  #Name mangling

#Second class
class player:
    def __init__(self, sport) -> None:
        self.sport = sport
        
    def printDetails(self):
        return f"The person plays {self.sport}"
        

#Concept of inheritance
#Single inheritance

class Programmer(Employee):
    def __init__(self, name, company, working_hours) -> None:
        self.name = name
        self.company = company
        self.working_hours = working_hours
        print(f"The name of the programmer is {self.name}, the name of his company is {self.company} and his working hours are {self.working_hours}")

    @staticmethod
    def working_project(name_of_project):
        return "The name of the current working project is {0} ".format(name_of_project)
        

harjot = Programmer("Harjot", "Google", 8)
harjot.working_project('Chrome')


#Multiple inheritance
class gamer(player, Programmer, Employee):
    pass

junaid = gamer("football")
print(junaid.printDetails())

print(rohan.working_project("Azure"))
print(rohan.no_of_leaves)


#Multilevel inheritance
#import exercise

#or 

class ElectronicDevice:
    use = "used in offices"
    processing = 1
    battery_capacity = '10,000' + ' mah'
    def __init__(self, name, no_of_cores, no_of_threads, company) -> None:
        self.name = name
        self.no_of_cores = no_of_cores
        self.no_of_threads =no_of_threads
        self.company = company

    def printDetails(self):
        print(f"The name of the electronic device is {self.name} and the number of cores and threads are {self.no_of_cores} and {self.no_of_threads} respectively and the name of the company is {self.company}")

Desktop = ElectronicDevice("DesktopPc", 8, 16, "Asus")
Desktop.printDetails()
    
class PocketGadget(ElectronicDevice):
    use = "used at home"
    battery_capacity = '8000' + ' mah'
    def __init__(self, name, company) -> None:
        self.name = name    
        self.company = company

    def printDetails(self):
        print(f"The name of the device is {self.name} and the name of the company is {self.company}")
        

ipad = PocketGadget("Ipad", "Apple")
ipad.printDetails()
print(ipad.processing)
print(ipad.battery_capacity)


class phone(PocketGadget):
    battery_capacity = '5000' + ' mah'
    
Phone = phone("Mob_phone", "Mi")
Phone.printDetails()
print(Phone.use)
print(phone.processing)

    

    
