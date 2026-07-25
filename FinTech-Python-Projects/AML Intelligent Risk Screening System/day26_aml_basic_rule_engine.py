# Day26 Project: AML Core Rule Engine Construction
# Technique: Multi-dimensional anti-money laundering rule matching
# Business Scenario: Large-value alert, split transaction detection, sanction country block
# Portfolio: FinTech Master Application

def judge_transaction_risk(amount, currency, trade_count, country_code):
    sanction_countries = ["RU", "IR", "KP", "SY", "CU"]
    risk_level = "NORMAL"
    risk_reason = ""

    # Rule 1: Large-value USD transaction alert
    if currency == "USD" and amount > 10000:
        risk_level = "HIGH RISK"
        risk_reason = "Large-value cross-border USD transaction"
    
    # Rule 2: Sanctioned country interception
    elif country_code in sanction_countries:
        risk_level = "HIGH RISK"
        risk_reason = "Transaction involved sanctioned country"
    
    # Rule 3: Split transaction frequent transfer warning
    elif trade_count >= 3:
        risk_level = "MEDIUM RISK"
        risk_reason = "Potential split transaction behavior"

    return risk_level, risk_reason

# Batch test cases
transaction_list = [
    {"amount":12500, "currency":"USD", "trade_count":1, "country_code":"US"},
    {"amount":4800, "currency":"EUR", "trade_count":3, "country_code":"DE"},
    {"amount":9200, "currency":"USD", "trade_count":1, "country_code":"RU"}
]

print("===== DAY26 AML BASIC RULE ENGINE RESULT =====")
for idx, tx in enumerate(transaction_list, 1):
    level, reason = judge_transaction_risk(**tx)
    print(f"Transaction {idx} | Risk Level: {level} | Reason: {reason}")