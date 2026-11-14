"""
RECORD CHECK  -  my version
===========================

Name  : Sri Geetika Kanakamedala
Lane  :  AI 
Date  : 14/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    "Cleans a raw survey line and returns a dictionary with converted values"
    line = raw_line.strip().lower()
    lines = line.split(",")
    records = {}
    records["survey"] = lines[0].strip()

    for part in lines[1:]:
        key,value = part.split("=")
        records[key.strip()] = int(value.strip())
    return records

def status_of(records):
    "Returns Flagged for age lower than 18 otherwise OK"
    if records["age"]<18:
        return "FLAGGED"
    return "OK"

# ====================================================================== INPUT

raw_records = []  
with open(r"C:\Users\kgeet\OneDrive\Geetika\CST1510\Strings and Text Manipulation-20261102\Week 07 - Strings and Text Manipulation\Week 07 - Strings and Text Manipulation\LAB\records.txt","r") as f:
    for line in f:
        if line.strip():
            raw_records.append(line)

# =============================================================== PROCESS + OUTPUT

total_records = 0 
flagged_records = 0 
for raw_record in raw_records:
    clean_data = parse_line(raw_record)
    status_of_record = status_of(clean_data)

    total_records+=1
    if status_of_record == "FLAGGED":
        flagged_records+=1

print(f"Summary:{total_records} records, {flagged_records} flagged")

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
