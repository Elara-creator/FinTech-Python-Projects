# Day11 Project: AML Advanced Risk Detection
# Core Technique: Group statistics, frequency analysis
# Business Scenario: Split transaction & frequent transfer monitoring
# Portfolio: FinTech Master Application

import pandas as pd

df = pd.DataFrame({
    "account_id": ["ACC001", "ACC001", "ACC001", "ACC002", "ACC002"],
    "transaction_id": ["T001", "T002", "T003", "T004", "T005"],
    "amount": [3200, 3500, 3100, 15000, 12000],
    "trade_date": ["20260803", "20260803", "20260803", "20260803", "20260803"]
})

# Count daily transaction frequency per account
freq_count = df.groupby("account_id")["transaction_id"].count().reset_index()
freq_count.columns = ["account_id", "daily_trade_count"]

# Detect split transaction behavior (multiple small transfers in one day)
split_risk = freq_count[freq_count["daily_trade_count"] >= 3]

print("===== FREQUENT TRANSFER ACCOUNTS =====")
print(freq_count)
print("\n===== SPLIT TRANSACTION RISK ACCOUNTS =====")
print(split_risk)