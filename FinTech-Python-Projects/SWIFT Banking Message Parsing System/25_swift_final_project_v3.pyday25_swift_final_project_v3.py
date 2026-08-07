# Day25 Project: SWIFT Message Parsing System V3.0 (Final Release)
# Full Integration: MT103 Regex + ISO20022 XML + Risk Engine
# Industrial Standard | Master Application Portfolio Final Work
# 100% English Version for Admissions & Interview

import re
import xml.etree.ElementTree as ET

class FinTechSwiftParser:
    def mt103_parse(self, text):
        ref = re.findall(r":20:(\w+)", text)[0]
        date, curr, amt = re.findall(r":32A:(\d{6})([A-Z]{3})([\d\.]+)", text)[0]
        return {"reference":ref,"date":date,"currency":curr,"amount":float(amt)}

    def iso20022_parse(self, xml_text):
        root = ET.fromstring(xml_text)
        return {
            "uetr": root.find("UETR").text,
            "amount": float(root.find("Amount").text),
            "currency": root.find("Amount").attrib["Ccy"]
        }

    def risk_assessment(self, amount, currency):
        if amount > 10000 and currency == "USD":
            return "HIGH RISK - LARGE VALUE CROSS-BORDER TRANSFER"
        return "NORMAL SAFE TRANSACTION"

# System Demo
if __name__ == "__main__":
    mt_data = FinTechSwiftParser().mt103_parse(":20:FIN260805\n:32A:260805USD13500.00")
    risk = FinTechSwiftParser().risk_assessment(mt_data["amount"], mt_data["currency"])

    print("===== SWIFT PARSING SYSTEM V3.0 | FINAL PROJECT =====")
    print(f"Transaction Reference: {mt_data['reference']}")
    print(f"Transaction Date: {mt_data['date']}")
    print(f"Amount: {mt_data['currency']} {mt_data['amount']}")
    print(f"Risk Evaluation: {risk}")
    print("System Status: Fully Operational")