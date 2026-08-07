# Day12 Project: Financial Transaction Group Statistics
# Core Technique: Groupby, aggregation, feature extraction
# Business Scenario: Cross-border transaction feature analysis
# Portfolio: FinTech Master Application

import pandas as pd

df = pd.DataFrame({
    "account_id": ["ACC001", "ACC001", "ACC002", "ACC002", "ACC003"],
    "amount": [12000, 8500, 15000, 9200, 6800],
    "currency": ["USD", "USD", "USD", "EUR", "USD"],
    "trade_month": ["202608", "202608", "202608", "202608", "202608"]
})

# Multi-dimensional financial aggregation analysis
stat_result = df.groupby(["account_id", "currency"]).agg(
    total_amount=("amount", "sum"),
    avg_amount=("amount", "mean"),
    max_amount=("amount", "max"),
    trade_times=("amount", "count")
).reset_index()

print("===== MULTI-DIMENSIONAL TRANSACTION STATISTICS =====")
print(stat_result)