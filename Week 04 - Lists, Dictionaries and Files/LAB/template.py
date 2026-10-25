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
