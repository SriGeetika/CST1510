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
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = []  
with open(r"C:\Users\kgeet\OneDrive\Geetika\CST1510\Strings and Text Manipulation-20261102\Week 07 - Strings and Text Manipulation\Week 07 - Strings and Text Manipulation\LAB\records.txt","r") as f:
    for line in f:
        if line.strip():
            raw_records.append(line)

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.
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
