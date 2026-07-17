# FinTech Python Training - Day1
# Project: SWIFT MT103 Message Field Extraction Tool
# Function: Automatically extract core transaction fields from raw SWIFT payment messages
# Core Skills: String cleaning, string slicing, field positioning and matching
# Simulate original SWIFT MT103 payment message with redundant spaces

swift_msg = "  260716 REMIT BANK BIC:STGBGB22 AMOUNT:28600.50 EUR  "

# Step 1: Clean redundant spaces at the beginning and end of the message
clean_msg = swift_msg.strip()

# Step 2: Extract transaction date (SWIFT standard: first 6 digits = YYMMDD)
trade_date = clean_msg[0:6]

# Step 3: Extract remittance bank BIC 8-digit identification code
bic_start = clean_msg.find("BIC:")
bic_code = clean_msg[bic_start+4 : bic_start+12]

# Step 4: Accurately extract transaction amount and currency type
amt_start = clean_msg.find("AMOUNT:")
amt_part = clean_msg[amt_start+7:].strip()
amount, currency = amt_part.split()

# Step 5: Output standardized structured transaction data

print("===== SWIFT CROSS-BORDER TRANSACTION RESULT =====")
print(f"Transaction Date: {trade_date}")
print(f"Remitter Bank BIC: {bic_code}")
print(f"Transaction Amount: {amount}")
print(f"Transaction Currency: {currency}")