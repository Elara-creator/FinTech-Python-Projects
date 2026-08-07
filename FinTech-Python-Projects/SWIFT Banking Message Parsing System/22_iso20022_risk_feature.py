# Day22 Project: ISO20022 Risk Feature Extraction
# Technique: XML parsing + financial risk tagging
# Business Scenario: Modern payment transaction risk identification
# Portfolio: FinTech Master Application

import xml.etree.ElementTree as ET

iso_xml_batch = """
<BatchTransactions>
    <Tx>
        <UETR>ISO-TX-001</UETR>
        <Amount Ccy="USD">16800.00</Amount>
        <CountryCode>RU</CountryCode>
    </Tx>
    <Tx>
        <UETR>ISO-TX-002</UETR>
        <Amount Ccy="EUR">5200.00</Amount>
        <CountryCode>FR</CountryCode>
    </Tx>
</BatchTransactions>
"""

root = ET.fromstring(iso_xml_batch)
risk_list = []

for tx in root.findall("Tx"):
    uetr = tx.find("UETR").text
    amount = float(tx.find("Amount").text)
    curr = tx.find("Amount").attrib["Ccy"]
    country = tx.find("CountryCode").text

    if amount > 15000 or country in ["RU","IR","KP"]:
        risk = "HIGH RISK"
    else:
        risk = "NORMAL"

    risk_list.append({"UETR":uetr,"Risk":risk})

print("===== ISO20022 BATCH RISK SCAN RESULT =====")
for item in risk_list:
    print(f"{item['UETR']} | {item['Risk']}")