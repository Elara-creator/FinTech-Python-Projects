# FinTech Python Training - Day2
# Project: Structured Cross-Border Transaction Data Processing
# Core Skills: Python Dictionary, Structured Data, JSON Standard Format
# Business Scenario: Standardize messy bank transaction information into machine-readable data

# Step 1: Use dictionary to build standard cross-border transaction structure
# Contains complete core fields of real SWIFT cross-border transactions
transaction_data = {
    "transaction_id": "SWIFT260717001",
    "transaction_date": "260717",
    "amount": 15800.75,
    "currency": "USD",
    "sender_bic": "HSBCHKHH",
    "receiver_bic": "BARBGB2L",
    "sender_country": "HK",
    "receiver_country": "GB",
    "transaction_purpose": "Trade Remittance"
}

# Step 2: Read single field data (basic data extraction)
print("===== RAW TRANSACTION BASIC INFO =====")
print(f"Transaction ID: {transaction_data['transaction_id']}")
print(f"Transaction Date: {transaction_data['transaction_date']}")
print(f"Transfer Amount: {transaction_data['amount']} {transaction_data['currency']}")
print(f"Sender Bank BIC: {transaction_data['sender_bic']}")
print(f"Receiver Bank BIC: {transaction_data['receiver_bic']}")

# Step 3: Simple business judgment (basic risk identification logic)
# Rule: Transactions over 10000 USD are defined as large-value transactions
print("\n===== TRANSACTION RISK JUDGMENT =====")
if transaction_data["amount"] > 10000 and transaction_data["currency"] == "USD":
    print("Risk Level: HIGH - Large Value Cross-border Transaction")
else:
    print("Risk Level: NORMAL - Standard Transaction")

# Step 4: Convert dictionary to standard JSON format (financial industry standard)
import json

json_transaction = json.dumps(transaction_data, indent=4)
print("\n===== STANDARD JSON TRANSACTION DATA =====")
print(json_transaction)