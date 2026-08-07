# Day13 Project: Financial Deep Feature Engineering
# Core Technique: Rolling statistics, financial indicator calculation
# Business Scenario: User transaction portrait construction
# Portfolio: FinTech Master Application

import pandas as pd

df = pd.DataFrame({
    "account_id": ["ACC001"] * 6,
    "trade_date": ["20260801","20260802","20260803","20260804","20260805","20260806"],
    "amount": [5200, 9800, 3500, 12000, 4800, 7200]
})

# Calculate cumulative transaction amount
df["cumulative_amount"] = df["amount"].cumsum()

# Calculate transaction fluctuation coefficient
df["amount_diff"] = df["amount"].diff()

print("===== FINANCIAL TRANSACTION FEATURE DATASET =====")
print(df)