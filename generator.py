"""
generate_reports.py
-------------------
Generates realistic defect inspection reports.
Combines:
✔ Defect-based logic (accuracy)
✔ Template-based logic (real-world feel)
✔ Faker for variation
"""

import csv
import random
from faker import Faker
from pathlib import Path

fake = Faker()
random.seed(42)

# -------------------------------
# MASTER DATA
# -------------------------------

PRODUCT_LINES = ["Line A", "Line B", "Line C"]

DEFECT_TYPES = {
    "Scratch": [
        "Minor surface scratch observed on outer panel",
        "Surface abrasion detected during inspection",
        "Light scratch found near edge area"
    ],
    "Crack": [
        "Crack detected near welding joint",
        "Hairline fracture observed in structural component",
        "Visible crack found in metal housing"
    ],
    "Loose Part": [
        "Bolt found loose during inspection",
        "Screw not tightened properly",
        "Component not securely fitted"
    ],
    "Overheating": [
        "Temperature exceeded safe operating limit",
        "Machine showing overheating signs",
        "Abnormal heat detected in motor unit"
    ],
    "Misalignment": [
        "Parts not aligned properly",
        "Axis misalignment detected",
        "Component shifted from correct position"
    ]
}

SEVERITIES = ["Low", "Medium", "High"]

# Realistic industrial context templates
TEMPLATES = [
    "Detected during end-of-line inspection. Batch {batch} placed on hold.",
    "Observed in shift {shift}. Maintenance team notified.",
    "Identified during routine quality check. Root cause under investigation.",
    "Machine parameter deviation detected on {line}. Process engineer alerted.",
    "Inspection performed by {inspector}. Further validation required.",
    "Issue recorded in station {station}. Immediate corrective action needed.",
]

# -------------------------------
# HELPER FUNCTIONS
# -------------------------------

def generate_report_id():
    return f"REP-{random.randint(1000, 9999)}"

def generate_note(defect):
    # Step 1: defect-specific base note
    base_note = random.choice(DEFECT_TYPES[defect])

    # Step 2: add industrial context
    template = random.choice(TEMPLATES)

    full_note = template.format(
        batch=fake.bothify("BATCH-####"),
        shift=random.choice(["A", "B", "C"]),
        line=random.choice(PRODUCT_LINES),
        inspector=fake.first_name(),
        station=random.randint(1, 10)
    )

    # Step 3: combine both
    return base_note + ". " + full_note

def generate_dataset(n=25):
    rows = []
    used_ids = set()

    for _ in range(n):
        defect = random.choice(list(DEFECT_TYPES.keys()))

        # unique ID
        rid = generate_report_id()
        while rid in used_ids:
            rid = generate_report_id()
        used_ids.add(rid)

        rows.append({
            "Report_ID": rid,
            "Product_Line": random.choice(PRODUCT_LINES),
            "Defect_Type": defect,
            "Severity": random.choice(SEVERITIES),
            "Inspector_Notes": generate_note(defect)
        })

    return rows

# -------------------------------
# SAVE DATASET
# -------------------------------

def save_dataset():
    Path("data").mkdir(exist_ok=True)

    rows = generate_dataset(25)

    file_path = "data/inspection_reports.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "Report_ID",
            "Product_Line",
            "Defect_Type",
            "Severity",
            "Inspector_Notes"
        ])
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Generated {len(rows)} reports → {file_path}")

    # preview
    for r in rows[:3]:
        print(r)


if __name__ == "__main__":
    save_dataset()