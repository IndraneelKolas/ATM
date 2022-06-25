class ATM(object):
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def checkBalance(self):
        print("Your balance is 2000$")

    def Withdrawl(self, amount):
        x = 2000 - amount
        print("You have withdrawed", amount)
        print("Your current balance is", x)

def main():
    
    newuser =  ATM(2929292929, 1020)
    print("Choose 1 for checking Balance:  \n Press 2 for Withdrawal: ")
    chooseactivity = int(input("Enter your option: "))
    if chooseactivity == 1:
        newuser.checkBalance()
    else:
        newuser.Withdrawl(200)
if(__name__ == "__main__"):
    main()

    