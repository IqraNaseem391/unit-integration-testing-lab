def deposit(balance, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")
    return balance + amount


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdraw amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount


def calculate_interest(balance, rate, years):
    if balance < 0:
        raise ValueError("Balance cannot be negative")
    if rate < 0:
        raise ValueError("Rate cannot be negative")
    if years < 0:
        raise ValueError("Years cannot be negative")

    return round(balance * (1 + rate / 100) ** years, 2)


def check_loan_eligibility(balance, credit_score):
    if balance < 0:
        raise ValueError("Balance cannot be negative")
    return balance >= 5000 and credit_score >= 700


def transfer(balance_from, balance_to, amount):
    if amount <= 0:
        raise ValueError("Transfer amount must be positive")
    balance_from = withdraw(balance_from, amount)
    balance_to = deposit(balance_to, amount)
    return balance_from, balance_to
