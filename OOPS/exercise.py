#Multilevel inheritance
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

    

    