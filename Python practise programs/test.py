class Train:
    def __init__(self, name, fare, seats) -> None:
        self.name = name
        self.fare = fare
        self.seats = seats
        

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats availabile in the train are {self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs. {self.fare} ")

    def bookTicket(self):
        if (self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats-1

        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNO):
        self.seats = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        cancelSeat = input("Sir do you want to cancel your seat?(y/n)")
        if cancelSeat == "y":
            if seatNO in self.seats:
                print(f"Okay sir your {seatNO} number seat has been cancelled")
                self.seats.add(seatNO)
        

        

intercity = Train("Intercity Express: 14015", 90, 300 )
intercity.getStatus()
intercity.bookTicket() 
intercity.cancelTicket(3)
# intercity.getStatus()

        




        