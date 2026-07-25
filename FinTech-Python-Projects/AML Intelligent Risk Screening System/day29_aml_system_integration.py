# Day29 Project: AML Full System Integration & Encapsulation V4.0
# Technique: OOP encapsulation, full-process automated scanning
# Business Scenario: Industrial-grade anti-money laundering system
# Portfolio: FinTech Master Top-tier Project

class AMLRiskSystem:
    def __init__(self):
        self.sanction_countries = ["RU", "IR", "KP", "SY", "CU"]
        self.sanction_keywords = ["MILITARY", "TRADE", "ENERGY", "BANK"]

    def amount_country_check(self, amount, currency, country):
        if country in self.sanction_countries:
            return "HIGH RISK - SANCTIONED COUNTRY"
        if currency == "USD" and amount > 10000:
            return "HIGH RISK - LARGE VALUE TRANSFER"
        if amount > 5000:
            return "MEDIUM RISK"
        return "LOW RISK"

    def counterparty_check(self, name):
        upper_name = name.upper()
        for key in self.sanction_keywords:
            if key in upper_name:
                return True
        return False

# System test entry
if __name__ == "__main__":
    aml = AMLRiskSystem()

    # Test case 1
    res1 = aml.amount_country_check(13200, "USD", "US")
    flag1 = aml.counterparty_check("Global Trade Company")

    # Test case 2
    res2 = aml.amount_country_check(4500, "EUR", "DE")
    flag2 = aml.counterparty_check("Local Retail LTD")

    print("===== DAY29 INTEGRATED AML SYSTEM V4.0 =====")
    print(f"Transaction 1 Risk Result: {res1} | Entity Risk: {flag1}")
    print(f"Transaction 2 Risk Result: {res2} | Entity Risk: {flag2}")