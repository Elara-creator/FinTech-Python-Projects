# Day15 Project: Batch AML Risk Labeling System
# Core Technique: Apply function, custom risk rule engine
# Business Scenario: Batch transaction risk classification
# Portfolio: FinTech Master Application

import pandas as pd

df = pd.DataFrame({
    "amount": [3200, 12500, 19800, 7500, 21000],
    "currency": ["USD", "USD", "USD", "EUR", "USD"],
    "country_code": ["US", "GB", "RU", "FR", "IR"]
})

# Custom financial risk rule function
def get_risk_label(row):
    if row["country_code"] in ["RU", "IR", "KP"]:
        return "HIGH RISK - SANCTIONED COUNTRY"
    elif row["currency"] == "USD" and row["amount"] > 10000:
        return "HIGH RISK - LARGE VALUE"
    elif row["amount"] > 5000:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

# Batch labeling
df["risk_result"] = df.apply(get_risk_label, axis=1)

print("===== BATCH RISK SCREENING RESULT =====")
print(df)