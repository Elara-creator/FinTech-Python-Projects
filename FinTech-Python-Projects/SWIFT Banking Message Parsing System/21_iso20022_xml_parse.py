# Day21 Project: ISO20022 XML Core Message Parser
# Technique: XML tree traversal
# Business Scenario: Next-generation banking payment standard parsing
# Portfolio: FinTech Master Application

import xml.etree.ElementTree as ET

# Simulate standard ISO20022 pacs.008 payment message
iso_xml = """
<PaymentMessage>
    <UETR>UNIQUE-20260803-0001</UETR>
    <TransactionId>ISO20260803TX</TransactionId>
    <ValueDate>20260803</ValueDate>
    <Amount Ccy="USD">14250.35</Amount>
    <UltimateDebtor>GLOBAL TRADING FIRM</UltimateDebtor>
    <UltimateCreditor>OVERSEAS PARTNER LTD</UltimateCreditor>
</PaymentMessage>
"""

root = ET.fromstring(iso_xml)

# Parse core ISO20022 fields
uetr = root.find("UETR").text
tx_id = root.find("TransactionId").text
date = root.find("ValueDate").text
amount = root.find("Amount").text
currency = root.find("Amount").attrib["Ccy"]
debtor = root.find("UltimateDebtor").text
creditor = root.find("UltimateCreditor").text

print("===== ISO20022 NEXT-GEN PAYMENT MESSAGE =====")
print(f"UETR (Unique End-to-End ID): {uetr}")
print(f"Transaction ID: {tx_id}")
print(f"Value Date: {date}")
print(f"Amount: {amount} {currency}")
print(f"Ultimate Debtor: {debtor}")
print(f"Ultimate Creditor: {creditor}")