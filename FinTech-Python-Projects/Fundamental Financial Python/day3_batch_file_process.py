# Simulate batch raw cross-border transaction dataset (10 real transaction records)
batch_transactions = [
    {"id":"SWIFT001","amt":6500,"currency":"EUR","country":"FR"},
    {"id":"SWIFT002","amt":12600,"currency":"USD","country":"RU"},
    {"id":"SWIFT003","amt":3200,"currency":"GBP","country":"DE"},
    {"id":"SWIFT004","amt":19800,"currency":"USD","country":"CN"},
    {"id":"SWIFT005","amt":7500,"currency":"CAD","country":"CA"},
    {"id":"SWIFT006","amt":25600,"currency":"USD","country":"SG"},
    {"id":"SWIFT007","amt":4100,"currency":"EUR","country":"IT"},
    {"id":"SWIFT008","amt":13500,"currency":"USD","country":"UA"},
    {"id":"SWIFT009","amt":8900,"currency":"AUD","country":"AU"},
    {"id":"SWIFT010","amt":11200,"currency":"USD","country":"HK"}
]

# Store screened high-risk transaction records
high_risk_list = []
normal_list = []

# Step 1: Batch loop to judge transaction risk
# AML Rule: USD amount over 10000 = high-risk cross-border transfer
print("===== BATCH TRANSACTION RISK SCAN REPORT =====")
for record in batch_transactions:
    trans_id = record["id"]
    amount = record["amt"]
    curr = record["currency"]
    area = record["country"]
    
    if curr == "USD" and amount > 10000:
        risk_tag = "HIGH RISK"
        high_risk_list.append(record)
    else:
        risk_tag = "NORMAL"
        normal_list.append(record)
    print(f"{trans_id} | {amount} {curr} | Region:{area} | Risk Status: {risk_tag}")

# Step 2: Statistical summary of batch data
print("\n===== BATCH STATISTICS SUMMARY =====")
print(f"Total transaction volume: {len(batch_transactions)}")
print(f"High-risk transaction count: {len(high_risk_list)}")
print(f"Normal transaction count: {len(normal_list)}")

# Step 3: Export high-risk data to standard JSON file
import json
with open("high_risk_transactions.json","w",encoding="utf-8") as f:
    json.dump(high_risk_list,f,indent=4)

print("\nExport complete: High-risk data saved to high_risk_transactions.json")