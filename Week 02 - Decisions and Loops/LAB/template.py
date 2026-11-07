"""
RECORD CHECK  -  my version
===========================

Name  : Sri Geetika Kanakamedala
Lane  :  AI 
Date  : 2/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
label = input("enter label name:")      
value = float(input("Enter a value:"))    
limit = float(input("Enter a limit:"))     


# ================================================================== PROCESS
difference = value - limit  
percent = value/limit * 100 

status = "" 
if value >= 100:
    status = "OVER LIMIT"
elif value >= 90:
    status=" WARNING"
else:
    status="OK"  


# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"Used : {value:>10.2f}")
print(f"Total: {limit:>10.2f}")
print(f"Difference : {difference:>10.2f}")
print(f"Percentage : {percent:>10.2f}%")
print(f"Status : {status}")
print("=" * 34)