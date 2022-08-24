class Employee:

    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
        
    @property
    def email(self):
        return f"{self.fname} {self.lname}@gmail.com"

    #property decorator simply makes the method as a property so that we don't need to call the method using parenthesis anymore

rohan = Employee('Rohan', 'Kumar')
mohan = Employee('Mohan', 'Singh')

#we want to change the name of rohan to sohan
rohan.fname = 'sohan'

print(rohan.email)

#abstract method is a method which has only declaration and doesn't have defination


    


