# Day27 Project: OFAC Sanction List Fuzzy Matching System
# Technique: String similarity matching & keyword screening
# Business Scenario: Counterparty high-risk entity identification
# Portfolio: FinTech Master Application

def sanction_fuzzy_check(counterparty_name):
    # Simulate official OFAC high-risk keyword list
    sanction_keywords = ["MILITARY", "BANK", "TRADE", "ENERGY", "OFFICIAL"]
    name_upper = counterparty_name.upper()

    match_result = "PASS"
    match_key = ""

    for key in sanction_keywords:
        if key in name_upper:
            match_result = "SANCTION RISK"
            match_key = key
            break
    
    return match_result, match_key

# Test real-world counterparty data
party_list = [
    "Global Trade Limited",
    "European Energy Corp",
    "Standard Logistics LTD",
    "North Military Investment"
]

print("===== DAY27 OFAC FUZZY SCAN RESULT =====")
for name in party_list:
    res, key = sanction_fuzzy_check(name)
    if res == "SANCTION RISK":
        print(f"[WARNING] {name} | MATCH KEY: {key} | STATUS: {res}")
    else:
        print(f"[SAFE] {name} | STATUS: {res}")