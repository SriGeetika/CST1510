"""
RECORD CHECK  -  my version
===========================

Name  : Sri Geetika kanakamedala
Lane  :  AI
Date  : 16/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value,limit):
    """Calculate the difference, percentage, and check if it is over the limit."""
    difference = limit - value
    percent = (value / limit) * 100 
    if percent >= 100:
        status = "OVER LIMIT" 
    else:
        status = "OK"
    return difference, percent, status

def print_report(label, differnce, percent, status):
    """Printing the report for a single line"""
    print(f"difference={differnce}, percent={percent}%, status={status}")



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
    """Read records from a file and return them as a list of dictionaries."""
    records = []
    
    try:
        with open(path, "r") as f:
            for x in f:
                parts = x.strip().split(",")
                label = parts[0]
                value = float(parts[1])
                limit = float(parts[2])
                
                record = {"label": label,"value": value,"limit": limit}
                records.append(record)
                
    except FileNotFoundError:
        print("The file could not be found.")
        
    return records
records = load_records("records_sample.txt")

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each
#  one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
over_limit = 0
with open("results.txt", "w") as f:
    
    for x in records:
        label = x["label"]
        value = x["value"]
        limit = x["limit"]
        
        check_record(value, limit)
        
        print_report(label, difference, percent, status)
        
        if status == "OVER LIMIT":
            over_limit+= 1
            
        f.write(f"{label},{status}\n")

print("Total OVER LIMIT records:" over_limit)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
 '''If the file does not exist then it will raise a file not found error'''
