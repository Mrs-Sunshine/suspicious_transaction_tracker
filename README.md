# 💼 Transaction Risk Analyzer (AML/Compliance Mini Project)

This is a beginner-friendly Python mini project designed to analyse and flag potentially suspicious transactions for compliance or financial crime purposes.

🔍 It evaluates transactions based on:
- **High-risk countries**
- **Large cash transactions (≥ £8,800)**
- **Structuring risks (frequent small amounts around £900–£999)**

---

## 🛠 Features

- Checks if the transaction involves a hAnalyserigh-risk country
- Flags large cash transactions over UK regulation thresholds
- Detects potentially structured small transactions
- Processes and tags each transaction as suspicious or not

---

### 📁 How It Works

🔹 1. High-Risk Country Detection
def is_high_risk_country(country):
    return country in High_Risk_Countries

Returns True if the transaction's country is on the high-risk list.

🔹 2. Large Cash Transaction Detection
def is_high_value_cash_transaction(amount, method):
    return amount >= 8800 and method.lower() == "cash"

Flags cash transactions above £8,800.

🔹 3. Structuring Pattern Detection
def is_structured_small_transaction(amount):
    return 900 <= amount <= 999

Flags suspiciously small repeated transaction values.

🔹 4. Risk Evaluation per Transaction
def check_transaction_risk(transaction):
    ...
    return country_risk or high_value_risk or structured_risk

This function checks one transaction for three types of risk:

1. Country risk – Is the transaction from a high-risk country?
2. High-value cash risk – Is it a large cash transaction (£8,800 or more)?
3. Structured risk – Is it a suspiciously small, repeated transaction (£900–£999)?

🔹 5. Process Multiple Transactions
def process_transactions(transactions):
    for tx in transactions:
        tx["suspicious"] = check_transaction_risk(tx)
    return transactions

This function:

1. Takes a list of transactions (dictionaries)
2. Applies the check_transaction_risk() function to each one
3. Adds a new key "suspicious": True/False to each transaction
4. Returns the updated list

🔹 6. Print Results
for tx in flagged:
    print(f"{tx['name']} | Suspicious: {tx['suspicious']} | Amount: £{tx['amount']} | Country: {tx['country']}")

This loop neatly prints the result for each transaction with:

1. Customer name
2. Whether it's flagged as suspicious
3. Amount and transaction country

🧪 Example Input & Output
example_transactions = [
    {"name": "John Doe", "amount": 950, "method": "bank", "country": "UK"},
    {"name": "Ali Reza", "amount": 12000, "method": "cash", "country": "Iran"},
]

# Output:
John Doe | Suspicious: True | Amount: £950 | Country: UK  
Ali Reza | Suspicious: True | Amount: £12000 | Country: Iran

✅ Why This Matters (Compliance Context)
This tool reflects simplified rules based on:

- UK Money Laundering Regulations 2017
- Practical AML red flags used in financial institutions

It’s a great starting point for aspiring financial crime analysts to understand how automated rule-based systems can flag suspicious activity.

📎 Notes
● High-risk countries are based on FATF and HMT watchlists.

● You can easily expand this project to include:
- Customer risk profiles
- Transaction frequency analysis
- Sanctions screening logic

