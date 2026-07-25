# Day10 Project: AML Multi-Condition Transaction Filtering
# Core Technique: Pandas boolean indexing, multi-condition screening
# Business Scenario: High-risk cross-border transaction identification
# Portfolio: FinTech Master Application

import pandas as pd

df = pd.DataFrame({
    "transaction_id": ["SWIFT001", "SWIFT002", "SWIFT003", "SWIFT004", "SWIFT005"],
    "amount": [12500.50, 3400.00, 18900.75, 9200.00, 21000.00],
    "currency": ["USD", "EUR", "USD", "GBP", "USD"],
    "country_code": ["US", "FR", "RU", "GB", "IR"]
})

# Define high-risk sanction countries
high_risk_countries = ["RU", "IR", "KP"]

# Screen high-risk transactions
risk_df = df[
    ((df["currency"] == "USD") & (df["amount"] > 10000)) |
    (df["country_code"].isin(high_risk_countries))
]

print("===== HIGH-RISK TRANSACTION LIST =====")
print(risk_df)