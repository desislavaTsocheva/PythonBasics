#клас акаунт: с полета : номер банк. сметка, баланс, пин.
#Въвеждане на данни за сметката:номер,начален баланс,пин от потребителя!
#операции: депозит, теглене, извеждане на инф. сметка, изход.
#Когато се избере опция теглене,да не може да се теглят повече пари от наличните.
#клас спестовна сметка с поле: Лихвен процент по сметката.
#Изчислява лихвата, лихвен баланс, извеждане на инф. за сметката

class Accaunt():
    def __init__(self,iban,balance, pin):
        self.iban=iban
        self.balance=balance
        self.pin=pin
    """def enter_values(self):
        self.iban=int(input("enter your iban: "))
        self.balance=int(input("enter your balance:"))
        self.pin=int(input("enter your pin: "))"""
    def print(self):
        print(f"IBAN: {self.iban} have {self.balance} balance")
    def deposit(self):
        deposit=int(input("enter deposit: "))
        pin=int(input("enter your pin"))
        if self.pin!=pin:
            pin=int(input("enter valid pin: "))
        else:
            self.balance+=deposit
            print(f"Your balance is {self.balance} lv")
    def teglene(self):
        pincode=int(input("enter pin: "))
        money=int(input("enter money: "))
        if self.pin!=pincode:
            pincode=int(input("enter valid pin: "))
        elif self.balance<money:
            print("you don't have enough money in your accaunt: ")
            money=int(input("enter valid number: "))
        self.balance-=money
        print(f"Your balance is {self.balance}")
    def exit(self):
        print("exit. ")
class Spestovna(Accaunt):
    def __init__ (self, percent,iban,balance,pin):
        super().__init__(iban,balance,pin)
        self.percent=percent
    def lihva(self):
        lihva=self.balance*self.percent
        print("Lihva:",lihva)
    def lihven_balance(self):
        balance_lihva=self.balance*(1+self.percent)
        print("Lihven balance:", balance_lihva)
    def print(self):
        print(f"IBAN: {self.iban} have {self.percent} lihva")

accaunt_type=str(input("Choose your accaunt type: "))
match accaunt_type:
    case "Razplashtatelna":
        iban = str(input("enter your iban: ")).upper()
        balance = int(input("enter your balance:"))
        pin = int(input("enter your pin: "))
        operation = str(input("Enter operation: "))
        accaunt_f = Accaunt(iban, balance, pin)
        while operation != "Exit":
            match operation:
                case "Deposit":
                    accaunt_f.deposit()
                case "Teglene":
                    accaunt_f.teglene()
                case "Print":
                    accaunt_f.print()
                case "Exit":
                    accaunt_f.exit()
                    break
            operation = str(input("Next operation: "))
    case "Spestovna":
        iban = str(input("enter your iban: ")).upper()
        balance = int(input("enter your balance:"))
        pin = int(input("enter your pin: "))
        percent=int(input("percent: "))
        spestovna=Spestovna(percent,iban,balance,pin)
        operation_sp=str(input("Choose operation: "))
        while operation_sp!="Exit":
            match operation_sp:
                case "Lihva":
                    spestovna.lihva()
                case "Lihven Balance":
                    spestovna.lihven_balance()
                case "Print":
                    spestovna.print()
                case "Exit":
                    break
            operation_sp=str(input("Enter new operation: "))