account = {
    "owner": "Savi",
    "balance": 1000.00,
    "transactions": []
}

def deposit(amount,account):
    if amount > 0:

        account["balance"] += amount
        account["transactions"].append(f"Deposited ${amount}")
        return f"New balance: ${account['balance']}"
    else:
        return "Invalid amount"


def withdraw(amount,account):
    if amount > account["balance"]:
        return "Insufficient funds"
    elif amount <= 0:
        return "Invalid amount"
    else:
        account["balance"] -= amount
        account["transactions"].append(f"Withdrew ${amount}")
        return f"New balance: ${account['balance']}"
    

def print_statement(account):
    for transaction in account["transactions"]:
        print(transaction)
    return f"Current balance: ${account['balance']}"

# Deposit
dep_amount = float(input("Enter deposit amount: "))
print(deposit(dep_amount, account))

# Withdraw
withdraw_amount = float(input("Enter withdrawal amount: "))
print(withdraw(withdraw_amount, account))


# Print statement
print("--- Transaction History ---")
print(print_statement(account))
