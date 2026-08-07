# Day8 Project: Financial DataFrame Basic & Data Cleaning
# Core Technique: Pandas data loading, structure checking, missing value handling
# Business Scenario: Cross-border transaction raw data preprocessing
# Portfolio: FinTech Master Application

import pandas as pd

# Load simulated transaction dataset
df = pd.DataFrame({
    "transaction_id": ["SWIFT001", "SWIFT002", "SWIFT003", "SWIFT004", "SWIFT005"],
    "trade_date": ["20260801", "20260801", None, "20260802", "20260802"],
    "amount": [12500.50, 3400.00, 18900.75, None, 7600.20],
    "currency": ["USD", "EUR", "USD", "GBP", "USD"],
    "country_code": ["US", "FR", "RU", "GB", "HK"]
})

# Check basic data structure
print("===== RAW DATA OVERVIEW =====")
print(df.info())
print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# Handle missing values (financial industry standard filling)
df["trade_date"].fillna("Unknown", inplace=True)
df["amount"].fillna(df["amount"].mean(), inplace=True)

print("\n===== CLEANED DATA =====")
print(df)