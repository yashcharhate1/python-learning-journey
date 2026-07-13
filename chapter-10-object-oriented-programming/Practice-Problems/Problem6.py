# Q6. Can you change the self parameter inside a class to something else (say "yash").
# Try changing self to "slf" or "yash" and see the effects.

# Q5. Write a class Train which has methods to book a ticket, get status (no. of seats) and get fare information of train runnig under Indian Railways.

from random import randint

''' we use slf, yash, ar any other words instead of self'''
class Train:
    def __init__(slf, trainNo, fro, to):
        slf.trainNo = trainNo
        slf.fro = fro
        slf.to = to

    def book(slf):
        print(f"The ticket is booked in Train No. {slf.trainNo} from {slf.fro} to {slf.to}.")

    def getStatus(slf):
        print(f"Train No. {slf.trainNo} is running on time")

    def getFare(slf):
        print(f"Ticket fare in Train No. {slf.trainNo} from {slf.fro} to {slf.to} is {randint(222, 555)}.")

IR = Train(17641, "Narkher", "Kacheguda")
IR.book()
IR.getStatus()
IR.getFare()