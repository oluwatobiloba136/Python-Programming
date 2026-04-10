import os
from datetime import datetime

import pandas as pd

# --------------------------------------------------------------
# Configuration
# --------------------------------------------------------------
OUTPUT_DIR = r"C:\NGX\CsiDefinition"

# --------------------------------------------------------------
# Build the CSI definition table (same data as in your M code)
# --------------------------------------------------------------
data = [
    {
        "Code": 1,
        "CSICode": "BLS",
        "Name": "Below Listing Standard",
        "Description": "Comprises of all deficiencies regarding Continuing Listing Standards.",
    },
    {
        "Code": 2,
        "CSICode": "MRF",
        "Name": "Missed Regulatory Filing",
        "Description": "Issuer Missed Regulatory Filing Deadline",
    },
    {
        "Code": 3,
        "CSICode": "DWL",
        "Name": "Delisting Watch-list",
        "Description": (
            "These are companies that have been served with a delisting notice but the "
            "delisting process has been put on hold because they have received a stay "
            "of action from The Exchange for a defined period during which they "
            "undertake to cure the issues that led to the issuance of the delisting "
            "notice. If they fail to cure within the defined period or any extension "
            "thereof, the hold on the delisting process will be lifted."
        ),
    },
    {
        "Code": 4,
        "CSICode": "DIP",
        "Name": "Delisting in Progress",
        "Description": (
            "These are companies that are in the delisting process, mandatory or "
            "voluntary. The delisting process commences with a notice of intention to "
            "delist from The Exchange to an issuer (mandatory) or to The Exchange from "
            "an issuer (voluntary)."
        ),
    },
    {
        "Code": 5,
        "CSICode": "AWR",
        "Name": "Awaiting Regulatory Approval",
        "Description": (
            "These are companies that are awaiting the approval or no objection of "
            "their primary government regulator before releasing their audited "
            "financial statements"
        ),
    },
    {
        "Code": 6,
        "CSICode": "RST",
        "Name": "Restructuring",
        "Description": "These are companies that are in the process of restructuring.",
    },
    {
        "Code": 7,
        "CSICode": "BMF",
        "Name": "Below Listing Standard and Missed Regulatory Filing",
        "Description": "Missed Regulatory Filing and Below Listing Standard",
    },
    {
        "Code": 8,
        "CSICode": "BAA",
        "Name": "Below Listing Standard and Awaiting Regulatory Approval",
        "Description": "Below Listing Standard and Awaiting Regulatory Approval",
    },
    {
        "Code": 9,
        "CSICode": "BRS",
        "Name": "Below Listing Standard and Restructuring",
        "Description": "Below Listing Standard and Restructuring",
    },
    {
        "Code": 10,
        "CSICode": "MRS",
        "Name": "Missed Regulatory Filing and Restructuring",
        "Description": "Missed Regulatory Filing and Restructuring",
    },
    {
        "Code": 11,
        "CSICode": "BMR",
        "Name": "Below Listing Standard, Missed Regulatory Filing and Restructuring",
        "Description": (
            "Below Listing Standard, Missed Regulatory Filing and Restructuring"
        ),
    },
]

df = pd.DataFrame(data)

# --------------------------------------------------------------
# Write to CSV: C:\NGX\CsiDefinition\csi_definition_TIMESTAMP.csv
# --------------------------------------------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"csi_definition_{timestamp}.csv"
filepath = os.path.join(OUTPUT_DIR, filename)

df.to_csv(filepath, index=False, encoding="utf-8")

print(f"Saved {len(df)} rows to {filepath}")