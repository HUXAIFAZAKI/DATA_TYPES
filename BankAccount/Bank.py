class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance
    
    def deposit(self,amount:float):
        if(amount>0):
            self.__balance += amount    
            print(f"\nSuccesfully added {amount} into your account: {self.__account_number}\nYour new balance is {self.__balance}")
        else:
            print("Please enter a amount greater than 0")

    def withdraw(self,amount:float):
        if(self.__balance - amount >= 0):
            self.__balance -= amount
            print(f"\nSuccesfully withdrawed {amount} from your account: {self.__account_number}\nYour new balance is {self.__balance}")
        else:
            print("Insufficient amount")

    def _recieve_transfer(self,amount:float):
        self.__balance += amount

    def transfer_to(self, another_account, amount):
        if not isinstance(another_account, BankAccount):
            raise ValueError("Target must be a BankAccount")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if self.__balance < amount:
            print("Insufficient balance for transfer")
            return
        
        self.__balance -= amount
        another_account._recieve_transfer(amount)  
        print(f"Transfer of {amount} from account {self.__account_number} to account {another_account.__account_number} completed")
        # print(self.__balance)
        # print(another_account.__balance)
    
    def __str__(self):
        return f"Account[{self.__account_number}] - Holder: {self.__holder_name} - Balance: ${self.__balance}"
        
b1 = BankAccount(123,"Huxaifa",5000)
b2 = BankAccount(222,"Ali", 2500)
b1.transfer_to(b2,5000)
b2.transfer_to(b1,1000)

print(b1)
print(b2)

# will implement in future
class SavingAccount(BankAccount):
    pass

class CurrentAccount(BankAccount):
    pass