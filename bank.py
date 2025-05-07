class BankAccount:
    def __init__(self, cust_name, account_number, balance, account_type, address):
        self.cust_name = cust_name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.address = address

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def displayDetails(self):
        print("\n----- Account Details -----")
        print(f"Customer Name : {self.cust_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type  : {self.account_type}")
        print(f"Address       : {self.address}")
        print(f"Balance       : ₹{self.balance}")
        print("----------------------------")


# Simulating Bank Operations
def simulate_bank_operations():
    # Create multiple bank accounts
    acc1 = BankAccount("Amit Sharma", "ACC1001", 5000, "Savings", "Delhi")
    acc2 = BankAccount("Neha Verma", "ACC1002", 10000, "Current", "Mumbai")

    # Display initial details
    acc1.displayDetails()
    acc2.displayDetails()

    # Perform operations
    print("\n--- Performing Transactions ---")
    acc1.deposit(2000)
    acc1.withdraw(1000)
    acc1.displayDetails()

    acc2.withdraw(12000)  # Test insufficient balance
    acc2.deposit(5000)
    acc2.withdraw(3000)
    acc2.displayDetails()


# Run the simulation
if __name__ == "__main__":
    simulate_bank_operations()
