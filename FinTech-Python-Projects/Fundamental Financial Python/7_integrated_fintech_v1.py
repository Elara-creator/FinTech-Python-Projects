# Day7 Project: Integrated Cross-Border Transaction Parsing System V1.0
# Project Integration: SWIFT Parsing + Risk Engine + Local Database Storage
# Business Scenario: Automated financial message processing & AML screening
# Core Techniques: String Processing, Regex Matching, SQLite CRUD, Logic Encapsulation
# Portfolio: FinTech Master Application Standard Project

import re
import sqlite3

# ====================== INITIALIZE DATABASE ======================
def init_database():
    """Create and initialize financial transaction database"""
    conn = sqlite3.connect("transaction_database.db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS transaction_records (
        trans_id TEXT PRIMARY KEY,
        trans_date TEXT,
        amount REAL,
        currency TEXT,
        sender_bic TEXT,
        receiver_bic TEXT,
        risk_level TEXT
    )
    ''')
    conn.commit()
    return conn, cur

# ====================== SWIFT MESSAGE PARSER ======================
def parse_swift_message(msg):
    """Extract structured fields from unstructured SWIFT raw message"""
    date_pattern = r"DATE:(\d{6})"
    amount_pattern = r"AMOUNT:([\d\.]+)"
    bic_pattern = r"BIC:\s*([A-Z0-9]{8})"

    trade_date = re.findall(date_pattern, msg)[0]
    trade_amount = float(re.findall(amount_pattern, msg)[0])
    bic_list = re.findall(bic_pattern, msg)

    return {
        "date": trade_date,
        "amount": trade_amount,
        "currency": "USD",
        "sender_bic": bic_list[0],
        "receiver_bic": bic_list[1]
    }

# ====================== AML RISK JUDGMENT ======================
def assess_risk(amount):
    """Financial AML risk level classification"""
    if amount > 15000:
        return "HIGH RISK"
    elif amount > 8000:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

# ====================== MAIN SYSTEM ENTRY ======================
if __name__ == "__main__":
    # Raw unstructured SWIFT message input
    raw_swift = """
    DATE:260722 | TRADE PAYMENT
    SENDER BIC: STGBGB22
    RECEIVER BIC: HSBCUSNY
    AMOUNT:17250.80 USD
    """

    # Step 1: Parse message to structured data
    result = parse_swift_message(raw_swift)
    risk = assess_risk(result["amount"])

    # Step 2: Initialize database and insert record
    conn, cur = init_database()
    transaction_id = "SWIFT-260722-001"
    cur.execute(
        "INSERT OR IGNORE INTO transaction_records VALUES (?,?,?,?,?,?,?)",
        (transaction_id, result["date"], result["amount"], result["currency"],
         result["sender_bic"], result["receiver_bic"], risk)
    )
    conn.commit()

    # Step 3: Standard output report
    print("===== INTEGRATED SWIFT TRANSACTION REPORT V1.0 =====")
    print(f"Transaction ID: {transaction_id}")
    print(f"Transaction Date: {result['date']}")
    print(f"Transfer Amount: {result['amount']} {result['currency']}")
    print(f"Sender Bank BIC: {result['sender_bic']}")
    print(f"Receiver Bank BIC: {result['receiver_bic']}")
    print(f"Risk Assessment Result: {risk}")

    # Step 4: Query all stored records
    print("\n===== ALL STORED TRANSACTION RECORDS =====")
    for record in cur.execute("SELECT * FROM transaction_records"):
        print(record)

    conn.close()