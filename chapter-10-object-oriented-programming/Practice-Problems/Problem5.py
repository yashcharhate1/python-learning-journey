# Q5. Write a class Train which has methods to book a ticket, get status (no. of seats) and get fare information of train runnig under Indian Railways.

from random import randint


class Train:
    def __init__(self, trainNo, fro, to):
        self.trainNo = trainNo
        self.fro = fro
        self.to = to

    def book(self):
        print(f"The ticket is booked in Train No. {self.trainNo} from {self.fro} to {self.to}.")

    def getStatus(self):
        print(f"Train No. {self.trainNo} is running on time")

    def getFare(self):
        print(f"Ticket fare in Train No. {self.trainNo} from {self.fro} to {self.to} is {randint(222, 555)}.")

IR = Train(17641, "Narkher", "Kacheguda")
IR.book()
IR.getStatus()
IR.getFare()