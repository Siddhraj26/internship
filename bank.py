class Bank():

    accounts = []

    def __init__(self,bal):

        self.bal=bal

        Bank.accounts.append(self)
 
    def show(self):

        print("Current balance is : ", self.bal)
 
    def deposite(self,val):

        self.bal += val
 
    def withdraw(self,val):

        if self.bal - val > 0 : self.bal-=val

        else: print(" garib ")
 
total = -1

cur=-1

print("0 : create account || 1 : show balance || 2 : diposite || 3 : withdraw || 4 : change")

while True:

    ch = int(input("Enter choise"))

    if ch == 0:

        obj = Bank(0)

        total+=1

        cur=total        

        print("your bank account has created your bank account number is : ",total)

    elif ch == 1:

        obj = Bank.accounts[cur]

        obj.show()

    elif ch == 2:

        ammount = int(input("Enter ammount"))

        obj = Bank.accounts[cur]

        obj.deposite(ammount)

        print("done")

    elif ch == 3:

        ammount = int(input("Enter ammount"))

        obj = Bank.accounts[cur]

        obj.withdraw(ammount)

        print("done")

    elif ch == 4:

        num = int(input("enter your bank account number"))

        try:

            obj = Bank.accounts[num]

            cur=num

            print("Account has changed to : ",cur)

        except Exception as e:

            print("enter valid aaccount number")
    else:
        break   
 