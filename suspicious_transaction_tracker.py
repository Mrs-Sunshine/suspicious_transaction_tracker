High_Risk_Countries = {"North Korea", "Iran", "Myanmar", "Syria",
"Haiti", "Yemen", "Pakistan", "Barbados", "South Sudan",
"Nigeria", "Cameroon", "Democratic Repulic of the Congo"}

def is_high_risk_country(country):
    return country in High_Risk_Countries

def is_high_value_cash_transaction(amount, method):
    return amount >= 8800 and method.lower() == "cash"

def is_structured_small_transaction(amount):
    return 900 <= amount <= 999

def check_transaction_risk(transaction):
    country_risk = is_high_risk_country(transaction["country"])
    high_value_risk = is_high_value_cash_transaction(transaction["amount"], transaction["method"])
    structured_risk = is_structured_small_transaction(transaction["amount"])
    return country_risk or high_value_risk or structured_risk

def process_transactions(transactions):
    for tx in transactions:
        tx["suspicious"] = check_transaction_risk(tx)
    return transactions
    
example_transactions = [
    {"name": "John Doe", "amount": 950, "method": "bank", "country": "UK"},
    {"name": "Ali Reza", "amount": 12000, "method": "cash", "country": "Iran"},
    {"name": "Jane Smith", "amount": 5000, "method": "cash", "country": "USA"},
    {"name": "Samuel Okoro", "amount": 980, "method": "bank", "country": "Nigeria"},
    {"name": "Lee Minji", "amount": 15000, "method": "cash", "country": "South Korea"},
]
    
flagged = process_transactions(example_transactions)
for tx in flagged:
    print(f"{tx['name']} | Suspicious: {tx['suspicious']} | Amount: £{tx['amount']} | Country: {tx['country']}")
