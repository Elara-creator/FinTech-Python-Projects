# Day24 Project: SWIFT Unified Risk Labeling & Auto Report Export
# Technique: Rule engine + structured report generation
# Business Scenario: Industrial-level message auditing
# Portfolio: FinTech Master Final Project

import re

def analyze_transaction(amount,currency,country):
    if currency == "USD" and float(amount) > 10000 or country in ["RU","IR","KP"]:
        return "HIGH RISK TRANSACTION"
    return "STANDARD TRANSACTION"

# MT103 parsing + risk analysis
msg = ":20:260805FIN001\n:32A:260805USD17200.00\n:59:RECEIVER IN RUSSIA"
amt = re.search(r"USD([\d\.]+)",msg).group(1)
risk_result = analyze_transaction(amt,"USD","RU")

print("===== FINAL SWIFT TRANSACTION AUDIT REPORT =====")
print(f"Transaction Amount: USD {amt}")
print(f"Risk Verdict: {risk_result}")
print("Report Status: Generated Successfully")