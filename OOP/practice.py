class Account:

    def __init__(self,balance,acc_number):
        self.balance=balance
        self.acc_number=acc_number

    def debit(self):
        result = int(input("Enter your acct number: "))
        if result == self.acc_number:
            money=input("Enter the amount to debit: ")
            self.balance+=money
            print("Amount debited successfully")

    def credit(self):
        result=int(input("Enter your acct number: "))
        if result==self.acc_number:
            amount=int(input("Enter the amount you want to credit: "))
            if amount>self.balance:
                print("Not enough balance!!")
                print(self.balance)
            else:
                self.balance-=amount
                print("Amount credited successfully")
                print(f"Total balance {self.balance}")
        else:
            print("Wrong Account Number")
    def balance(self):
        print(self.balance)

user1=Account(10000,24688642)
print("Welcome to Virtual Bank")
choice=input("Enter the operation you want to perform , Type (check balance/credit/debit): ")
if choice=="check balance":
    user1.balance()
elif choice=="credit":
    user1.credit()
else:
    user1.debit()
