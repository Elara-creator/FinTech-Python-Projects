# Day4 Project: Modular Financial Function Encapsulation
# Core Technique: Parameter passing, return value design, code reusability
# Business Scenario: Financial amount calculation, currency conversion & risk judgment
# Portfolio: FinTech Master Application

# 1. Function 1: Standard amount rounding (bank financial precision)
def round_amount(amount):
    """Keep 2 decimal places for financial transaction amount"""
    return round(amount, 2)

# 2. Function 2: USD & EUR exchange rate calculation (simulate real exchange)
def currency_convert(original_amount, rate):
    """Convert foreign currency amount based on given exchange rate"""
    result = original_amount * rate
    return round_amount(result)

# 3. Function 3: AML risk level judgment engine
def get_risk_level(amount, currency, risk_country_list):
    """
    Judge cross-border transaction risk level
    HIGH: USD > 10000 or from high-risk country
    MEDIUM: USD 5000-10000
    LOW: Normal small transaction
    """
    if currency == "USD" and amount > 10000 or risk_country_list:
        return "HIGH RISK"
    elif currency == "USD" and amount >= 5000:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

# ------------------- Business Test -------------------
if __name__ == "__main__":
    # Test 1: Amount precision processing
    raw_amount = 12568.3456
    fixed_amount = round_amount(raw_amount)
    print("===== FINANCIAL TOOL FUNCTION TEST =====")
    print(f"Original Amount: {raw_amount}")
    print(f"Standard Financial Amount: {fixed_amount}")

    # Test 2: Currency exchange calculation
    eur_amount = 8500
    usd_rate = 1.09
    usd_result = currency_convert(eur_amount, usd_rate)
    print(f"EUR {eur_amount} = USD {usd_result}")

    # Test 3: Transaction risk assessment
    trans1_risk = get_risk_level(12000, "USD", False)
    trans2_risk = get_risk_level(4800, "USD", True)
    trans3_risk = get_risk_level(3600, "EUR", False)

    print("\n===== TRANSACTION RISK ASSESSMENT =====")
    print(f"Transaction 1 Risk Level: {trans1_risk}")
    print(f"Transaction 2 Risk Level: {trans2_risk}")
    print(f"Transaction 3 Risk Level: {trans3_risk}")