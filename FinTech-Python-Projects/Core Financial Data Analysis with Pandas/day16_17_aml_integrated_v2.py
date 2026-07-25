# Day16-17 Project: AML Transaction Cleaning &amp; Analysis System V2.0
# Integration: Data cleaning + filter + statistic + report export
# Business Scenario: Complete automated AML pre-processing pipeline
# Portfolio: FinTech Master Official Github V2.0

import pandas as pd

# Step1: Raw data import
df = pd.DataFrame({
    "transaction_id": ["T001", "T002", "T003", "T004", "T005", "T002"],
    "account_id": ["ACC01", "ACC02", "ACC01", "ACC03", "ACC02", "ACC02"],
    "amount": [12500, -500, 3200, 18900, 7600, 12500],
    "currency": ["USD", "EUR", "USD", "USD", "GBP", "EUR"],
    "country_code": ["US", "FR", "RU", "GB", "IR", "FR"],
    "trade_date": ["20260810", "20260810", "20260810", "20260811", "20260811", "20260810"]
})

# Step2: Full data cleaning pipeline
df = df.drop_duplicates(subset=["transaction_id"])
df = df[df["amount"] > 0]
df["amount"].fillna(df["amount"].mean(), inplace=True)

# Step3: AML risk rule engine
def risk_engine(row):
    if row["country_code"] in ["RU", "IR", "KP"] or (row["currency"] == "USD" and row["amount"] > 10000):
        return "HIGH RISK"
    elif row["amount"] > 5000:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

df["risk_level"] = df.apply(risk_engine, axis=1)

# Step4: Statistical analysis
summary = df.groupby("risk_level")["transaction_id"].count().reset_index()
summary.columns = ["risk_level", "transaction_count"]

# Step5: Auto export final report
df.to_excel("aml_cleaned_risk_report_v2.xlsx", index=False)

# Final output
print("===== PHASE2 AML SYSTEM V2.0 OUTPUT =====")
print("Cleaned Transaction Data:")
print(df)
print("\nRisk Distribution Summary:")
print(summary)
print("\nReport Export Successfully Completed!")