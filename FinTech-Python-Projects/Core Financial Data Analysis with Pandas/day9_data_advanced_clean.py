# Day9 Project: Advanced Financial Dirty Data Cleaning
# Core Technique: Duplicate removal, abnormal value filtering
# Business Scenario: AML raw data standardization
# Portfolio: FinTech Master Application

import pandas as pd

# Simulate messy real-world transaction data
df = pd.DataFrame({
    "transaction_id": ["SWIFT001", "SWIFT001", "SWIFT002", "SWIFT003", "SWIFT004"],
    "trade_date": ["20260801", "20260801", "20260801", "20260802", "20260802"],
    "amount": [12500.50, 12500.50, -9999, 18900.75, 7600.20],
    "currency": ["USD", "USD", "EUR", "USD", "USD"],
    "country_code": ["US", "US", "FR", "RU", "HK"]
})

# Remove duplicate transactions
df = df.drop_duplicates(subset=["transaction_id"])

# Filter abnormal negative amount data (invalid financial record)
df = df[df["amount"] > 0]

print("===== STANDARDIZED TRANSACTION DATA =====")
print(df)