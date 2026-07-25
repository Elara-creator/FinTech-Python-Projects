# Day28 Project: Automated AML Risk Report Generation
# Technique: Structured data statistics & standardized report output
# Business Scenario: Intelligent batch transaction auditing report
# Portfolio: FinTech Master Application

import pandas as pd

# Simulate audited transaction dataset
tx_data = [
    {"tx_id":"TX001","amount":12500,"currency":"USD","country":"US","risk":"HIGH RISK"},
    {"tx_id":"TX002","amount":4200,"currency":"EUR","country":"FR","risk":"NORMAL"},
    {"tx_id":"TX003","amount":9800,"currency":"USD","country":"RU","risk":"HIGH RISK"},
    {"tx_id":"TX004","amount":6500,"currency":"GBP","country":"GB","risk":"NORMAL"},
    {"tx_id":"TX005","amount":5200,"currency":"USD","country":"CN","risk":"MEDIUM RISK"}
]

df = pd.DataFrame(tx_data)

# Statistical analysis
total_count = len(df)
high_risk_count = len(df[df["risk"]=="HIGH RISK"])
medium_risk_count = len(df[df["risk"]=="MEDIUM RISK"])
normal_count = len(df[df["risk"]=="NORMAL"])

# Auto print formal report
print("===== DAY28 OFFICIAL AML DAILY RISK REPORT =====")
print(f"Total Transaction Volume: {total_count}")
print(f"High-risk Transaction: {high_risk_count}")
print(f"Medium-risk Transaction: {medium_risk_count}")
print(f"Normal Transaction: {normal_count}")

print("\n===== HIGH-RISK TRANSACTION DETAIL LIST =====")
high_df = df[df["risk"]=="HIGH RISK"]
print(high_df)