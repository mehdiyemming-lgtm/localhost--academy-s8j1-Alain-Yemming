class Bank_account:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
    def show_balance(self):
        print(f"Solde de {self.owner} : {self.balance}")
    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            print(f"Vous avez déposé {amount}. Nouveau solde : {self.balance}")
        else:
            print("Le montant est invalide.")




account = Bank_account("Alice", 1000)
account.show_balance()  # Output: Solde de Alice : 1000
account.deposit(500)    # Output: Vous avez déposé 500. Nouveau solde
account.show_balance()  # Output: Solde de Alice : 1500
account.deposit(-100)   # Output: Le montant est invalide.
account.show_balance()  # Output: Solde de Alice : 1500