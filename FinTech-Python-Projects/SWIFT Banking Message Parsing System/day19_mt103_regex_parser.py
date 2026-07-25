# Day19 Project: Automated MT103 Regex Field Extraction
# Technique: Regular expression field matching
# Business Scenario: Unstructured banking message auto-parsing
# Portfolio: FinTech Master Application

import re

mt103_raw = """
{1:F01DEUTDEFFXXXX0000000000}
{2:I103BARBGB2LXXXXN}
{4:
:20:260801SW0099
:23B:CRED
:32A:260801USD19650.20
:50K:GLOBAL TRADE LTD
:59:OVERSEAS RECEIVER CORP
}
"""

# Regex rules
ref_pattern = r":20:(\w+)"
date_amt_pattern = r":32A:(\d{6})([A-Z]{3})([\d\.]+)"
sender_pattern = r":50K:(.+)"
receiver_pattern = r":59:(.+)"

# Extract fields
trans_ref = re.findall(ref_pattern, mt103_raw)[0]
date_currency_amount = re.findall(date_amt_pattern, mt103_raw)
sender_name = re.findall(sender_pattern, mt103_raw)[0]
receiver_name = re.findall(receiver_pattern, mt103_raw)[0]

date, curr, amt = date_currency_amount[0]

print("===== AUTOMATED MT103 PARSED RESULT =====")
print(f"Transaction Reference: {trans_ref}")
print(f"Value Date: {date}")
print(f"Currency: {curr}")
print(f"Amount: {amt}")
print(f"Ordering Customer: {sender_name}")
print(f"Beneficiary Customer: {receiver_name}")