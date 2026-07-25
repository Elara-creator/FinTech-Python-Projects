# Day20 Project: MT103 Full Structured Data Export
# Technique: Structured dictionary mapping + standardized output
# Business Scenario: Convert raw SWIFT text to machine-readable data
# Portfolio: FinTech Master Application

import re

def parse_mt103(message):
    data = {}
    data["transaction_ref"] = re.search(r":20:(\w+)", message).group(1)
    data["trade_type"] = re.search(r":23B:(\w+)", message).group(1)
    
    date_curr_amt = re.search(r":32A:(\d{6})([A-Z]{3})([\d\.]+)", message)
    data["value_date"] = date_curr_amt.group(1)
    data["currency"] = date_curr_amt.group(2)
    data["amount"] = float(date_curr_amt.group(3))

    data["sender"] = re.search(r":50K:(.+)", message).group(1)
    data["receiver"] = re.search(r":59:(.+)", message).group(1)
    
    return data

# Test official MT103 message
mt103_msg = """
:20:260802SW0100
:23B:CRED
:32A:260802GBP7520.80
:50K:UK EXPORT COMPANY
:59:EU IMPORT SERVICE
"""

result = parse_mt103(mt103_msg)

print("===== FULL STRUCTURED MT103 TRANSACTION DATA =====")
for key,value in result.items():
    print(f"{key.upper()}: {value}")