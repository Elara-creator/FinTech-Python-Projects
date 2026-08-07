# Day6 Project: SWIFT Message Precision Extraction with Regex
# Scenario: Unstructured bank message cleaning & financial field matching
# Technique: Regular Expression, Fuzzy Matching, Financial Data Parsing
# Portfolio: FinTech Master Application Project

import re

# Simulate real-world unstructured raw SWIFT payment message
raw_swift_message = """
DATE:260720 | TRANSFER 18900.75 USD
SENDER BIC: HSBCUSNY
RECEIVER BIC: BARCLONGB
REMARK: INTERNATIONAL TRADE PAYMENT
AMOUNT:18900.75 USD
"""

# Regular expression rules for standard financial field extraction
rule_trade_date = r"DATE:(\d{6})"                # Match YYMMDD date format
rule_trade_amount = r"AMOUNT:([\d\.]+)"           # Match transaction numeric amount
rule_bank_bic = r"BIC:\s*([A-Z0-9]{8})"           # Match 8-digit SWIFT BIC code

# Extract target fields from unstructured text
extracted_date = re.findall(rule_trade_date, raw_swift_message)
extracted_amount = re.findall(rule_trade_amount, raw_swift_message)
extracted_bic_list = re.findall(rule_bank_bic, raw_swift_message)

# Parse string data to float for financial risk calculation
transaction_amount = float(extracted_amount[0])

# Standard structured output
print("===== SWIFT REGEX EXTRACTION RESULT =====")
print(f"Transaction Date: {extracted_date[0]}")
print(f"Transaction Amount: {transaction_amount:.2f} USD")
print(f"Participating Bank BICs: {extracted_bic_list}")

# Financial AML risk detection logic
print("\n===== TRANSACTION RISK ASSESSMENT =====")
if transaction_amount > 15000:
    print("Risk Status: HIGH RISK - Large-value Cross-border Transaction")
else:
    print("Risk Status: NORMAL - Standard Cross-border Transaction")