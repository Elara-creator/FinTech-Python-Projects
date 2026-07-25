# Day14 Project: Automatic Financial Report Generation
# Core Technique: Pandas batch export, standardized report output
# Business Scenario: Daily AML risk report automation
# Portfolio: FinTech Master Application

import pandas as pd

df = pd.DataFrame({
    "transaction_id": ["SWIFT001", "SWIFT002", "SWIFT003"],
    "account_id": ["ACC001", "ACC002", "ACC003"],
    "amount": [12500, 18900, 9600],
    "risk_level": ["HIGH", "HIGH", "MEDIUM"]
})

# Auto generate standardized risk report
df.to_excel("daily_risk_transaction_report.xlsx", index=False)
print("===== REPORT GENERATION COMPLETE =====")
print("File saved: daily_risk_transaction_report.xlsx")
print("\n===== RISK TRANSACTION OVERVIEW =====")
print(df)