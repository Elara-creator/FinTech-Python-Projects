# Day23 Project: Dual Engine SWIFT Parsing System V3.0
# Technique: Unified MT103 + ISO20022 parsing framework
# Business Scenario: Hybrid legacy & modern bank message processing
# Portfolio: FinTech Master Highlight Project

import re
import xml.etree.ElementTree as ET

class SwiftUnifiedParser:
    def parse_mt103(self, msg):
        ref = re.search(r":20:(\w+)",msg).group(1)
        dateamt = re.search(r":32A:(\d{6})([A-Z]{3})([\d\.]+)",msg)
        return {"Type":"MT103","Ref":ref,"Date":dateamt.group(1),"Currency":dateamt.group(2),"Amount":dateamt.group(3)}

    def parse_iso20022(self, xml):
        root = ET.fromstring(xml)
        return {
            "Type":"ISO20022",
            "UETR": root.find("UETR").text,
            "Amount": root.find("Amount").text,
            "Currency": root.find("Amount").attrib["Ccy"]
        }

# Test dual format input
parser = SwiftUnifiedParser()

mt103_sample = ":20:260804MT001\n:32A:260804USD9800.00"
iso_sample = "<Tx><UETR>ISO-2026-0804</UETR><Amount Ccy=\"EUR\">11200.00</Amount></Tx>"

res1 = parser.parse_mt103(mt103_sample)
res2 = parser.parse_iso20022(iso_sample)

print("===== UNIFIED SWIFT PARSING SYSTEM V3.0 OUTPUT =====")
print(res1)
print(res2)