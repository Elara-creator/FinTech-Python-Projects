# Day5 项目：金融交易文本文件批量清洗与读写工具
# 适配：银行流水处理、本地报文归档 / FinTech英硕作品集
# 技能点：本地文件读取、文本批量清洗、数据过滤、新文件写入

# Step 1: Simulate raw messy bank transaction text data (with garbage characters and spaces)
raw_text_data = """
SWIFT260801  9800.50  USD  HK  NORMAL
SWIFT260802  15200.00  USD  RU  RISK
SWIFT260803  3200.00  EUR  DE  NORMAL
SWIFT260804  21600.75  USD  IR  RISK
SWIFT260805  7900.00  GBP  UK  NORMAL
"""

# Step 2: Save original messy data to local text file
with open("raw_transaction.txt", "w", encoding="utf-8") as f:
    f.write(raw_text_data)

# Step 3: Read raw file data and clean invalid blank lines
with open("raw_transaction.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

clean_data = []
for line in lines:
    # Remove extra spaces and filter out empty lines
    clean_line = line.strip()
    if clean_line:
        clean_data.append(clean_line)

# Step 4: Screen high-risk transactions for AML compliance
risk_transaction = []
normal_transaction = []
for data in clean_data:
    if "RISK" in data:
        risk_transaction.append(data)
    else:
        normal_transaction.append(data)

# Step 5: Write standardized cleaned data to new file
with open("cleaned_transaction.txt", "w", encoding="utf-8") as f:
    f.write("===== STANDARD CLEANED TRANSACTION RECORD =====\n")
    for item in clean_data:
        f.write(item + "\n")

# Step 6: Write independent high-risk transaction file
with open("high_risk_record.txt", "w", encoding="utf-8") as f:
    f.write("===== AML HIGH-RISK TRANSACTION LIST =====\n")
    for risk_item in risk_transaction:
        f.write(risk_item + "\n")

# Terminal output statistical results
print("===== DAY5 FILE PROCESSING RESULT =====")
print(f"Total valid transaction records: {len(clean_data)}")
print(f"High-risk transaction quantity: {len(risk_transaction)}")
print(f"Normal transaction quantity: {len(normal_transaction)}")
print("\nFile export completed!")
print("Generated files: raw_transaction.txt / cleaned_transaction.txt / high_risk_record.txt")