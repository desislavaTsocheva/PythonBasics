class Bank_Account:
    def __init__(self,account_number,name,balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance
    def deposit(self,d):
        self.balance=d
    def withdrawing_money(self,w):
        if self.balance>w:
            self.balance-=w
            print("OKAY")
        else:
            print("Not enough money!")
    def print_info(self):
        print(f"Id: {self.account_number}, name: {self.name}, balance:{self.balance}")
account_list=[]
for i in range(2):
    id=int(input("Id: "))
    name=str(input("Name: "))
    balance=float(input("Balance: "))
    account=Bank_Account(id,name,balance)
    account_list.append(account)
def max_balance():
    max(account_list,key=lambda acc:acc.balance)
    print(max)

def sort_by_name():
    account_list.sort(key=lambda acc:acc.name)
    for i in account_list:
        print(i)
max_balance()
sort_by_name()