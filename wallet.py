class exception(Exception):
        pass

class Wallet:
        def __init__(self, initial_money, budget_name):
            self.money = initial_money
            self.name = budget_name
            print(f"\nBudget '{self.name}' created.\nMoney = ${self.money:.2f}")
        # A standard __init__ function for Python that initializes the objects
        
        def get_money(self):
            print(f"\nBudget '{self.name}' money = ${self.money:.2f}")
        # A function that prints the budget and the amount of money for the budget
        
        def add_money(self, amount):
            self.money += amount
            print("\nMoney added.")
            self.get_money()
        # A function that adds money to the budget
        
        def viable_transaction(self, amount):
            if self.money >= amount:
                return
            else:
                raise exception(f"\nSorry, budget '{self.name}' only has ${self.money:.2f}")
        # A function that checks if the budget has enough money to spend, I didn't need to make this a function on its own, but I kept it since I kind of like it
        
        def spend(self, amount):
            try:
                self.viable_transaction(amount)
                self.money -= amount
                print("\nMoney spent.")
                self.get_money()
            except exception as error:
                print(f'\nTransaction interrupted: {error}')
        # A function that "spends" or removes the money from the budget, it uses the aforementioned viable_transaction function to check if the budget has enough and other functions as well

def main():
        print("Welcome to.. your Wallet\n")
        budget_name = input("Enter budget name: ")
        initial_money = float(input("Enter initial money amount: "))
        wallet = Wallet(initial_money, budget_name)
        
        while True:
            print("\nMenu:")
            print("1. Check Money")
            print("2. Add Money")
            print("3. Spend Money")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                wallet.get_money()
            elif choice == '2':
                amount = float(input("Enter amount to add: "))
                wallet.add_money(amount)
            elif choice == '3':
                amount = float(input("Enter amount to spend: "))
                wallet.spend(amount)
            elif choice == '4':
                print("\Goodbye")
                break
            else:
                print("\nInvalid choice. Please try again.")

# A simple menu, I didn't have much time to include while loops to check for invalid inputs.
if __name__ == "__main__":
        main()