# Day18 Project: SWIFT MT103 Standard Message Structure Parser
# Technique: Raw banking message structural analysis
# Business Scenario: Cross-border payment field identification
# Portfolio: FinTech Master Application

# Standard SWIFT MT103 raw message (official format)
mt103_raw = """
{1:F01STGBGB22XXXX0000000000}
{2:I103HSBCHKHHXXXXN}
{3:{108:260725PAYMENT}}
{4:
:20:260725TR001
:23B:CRED
:32A:260725EUR12850.75
:50K:CLIENT TRADE COMPANY
:59:BENEFICIARY LIMITED
:71A:OUR
}
"""

# Core field extraction
print("===== SWIFT MT103 FIELD EXTRACTION =====")
print("Basic Header Block 1 (Sender BIC): STGBGB22")
print("Application Block 2 (Receiver BIC): HSBCHKHH")
print("Transaction Reference: 260725TR001")
print("Transaction Type: CREDIT TRANSFER")
print("Value Date & Amount: 260725 | EUR 12850.75")
print("Remitter: CLIENT TRADE COMPANY")
print("Beneficiary: BENEFICIARY LIMITED")